#!/usr/bin/env python3
"""
check_status.py — Abgleich Statustabelle (CLAUDE.md) gegen das Dateisystem.

Macht die wichtigste Invariante des Workflows deterministisch prüfbar:
„Dateien sind Wahrheit" — ein Statuswert in CLAUDE.md, zu dem keine Datei
existiert, ist ein Widerspruch, den der jeweilige Skill melden und beheben
muss (Status korrigieren, nicht die Datei erfinden).

Nutzung (vom Projekt-Root):
    python .claude/skills/_shared/scripts/check_status.py
    python .claude/skills/_shared/scripts/check_status.py <projekt-root>

Prüft:
  1. FEHLER:STATUS-DATEI   — Komponente mit Status FERTIG / IN ARBEIT /
     ÜBERARBEITUNG NÖTIG, deren Pfad nicht existiert.
  2. HINWEIS:DATEI-OHNE-ZEILE — .tex-Datei unter chapters/, die von keiner
     Tabellenzeile abgedeckt ist (weder über den Pfad noch über sec:<slug>).
  3. HINWEIS:STATUS-WERT   — unbekannter Statuswert (Tippfehler-Schutz).

Platzhalter-Zeilen (Pfad mit „…" oder „<…>") werden übersprungen — sie sind
bis Plan-Schritt 2.5 vorgesehen. Exit-Code 1 bei mindestens einem FEHLER.
"""

import re
import sys
from pathlib import Path

KNOWN_STATUS = ("FERTIG", "IN ARBEIT", "ÜBERARBEITUNG NÖTIG", "NICHT BEGONNEN")
MUST_EXIST = ("FERTIG", "IN ARBEIT", "ÜBERARBEITUNG NÖTIG")
ROW_RE = re.compile(r"^\|(.+)\|\s*$")
SLUG_RE = re.compile(r"sec:([\w-]+)")


def parse_table(claude_md: str) -> list[dict]:
    """Extrahiert die Zeilen der Statustabelle (Spalten: Komponente, Pfad, Status, Notizen)."""
    rows = []
    in_table = False
    for line in claude_md.splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            in_table = False
            continue
        cells = [c.strip() for c in m.group(1).split("|")]
        if len(cells) < 3:
            continue
        if cells[0].startswith("Komponente"):
            in_table = True
            continue
        if set(cells[0]) <= {"-", " ", ":"}:
            continue
        if in_table:
            rows.append({
                "komponente": cells[0],
                "pfad": cells[1].strip("`").strip(),
                "status": cells[2],
            })
    return rows


def is_placeholder(row: dict) -> bool:
    text = row["komponente"] + row["pfad"]
    return "…" in text or "<" in text or "Platzhalter" in text


def check(root: Path) -> tuple[list[str], int]:
    findings: list[str] = []
    errors = 0

    claude = root / "CLAUDE.md"
    if not claude.exists():
        return [f"{claude}: FEHLER — CLAUDE.md nicht gefunden."], 1
    rows = parse_table(claude.read_text(encoding="utf-8", errors="replace"))
    if not rows:
        return [f"{claude}: HINWEIS — keine Statustabelle gefunden (Kopfzeile: | Komponente …)."], 0

    active_rows = [r for r in rows if not is_placeholder(r)]

    for r in active_rows:
        status_base = next((k for k in KNOWN_STATUS if r["status"].startswith(k)), None)
        if status_base is None:
            findings.append(
                f"CLAUDE.md: [HINWEIS:STATUS-WERT] „{r['komponente']}“ hat unbekannten Status „{r['status']}“ — erlaubt: {', '.join(KNOWN_STATUS)}.")
            continue
        if status_base in MUST_EXIST and r["pfad"]:
            p = root / r["pfad"]
            # Pfad kann Datei oder Kapitelordner sein; bei Ordnern muss er Inhalt haben
            exists = p.is_file() or (p.is_dir() and any(p.glob("*.tex")))
            if not exists:
                findings.append(
                    f"CLAUDE.md: [FEHLER:STATUS-DATEI] „{r['komponente']}“ ist {status_base}, aber `{r['pfad']}` existiert nicht (bzw. enthält keine .tex) — Dateisystem gilt: Status korrigieren und Widerspruch melden.")
                errors += 1

    # Umgekehrte Richtung: Kapiteldateien ohne Statuszeile
    chapters = root / "chapters"
    if chapters.is_dir():
        covered_paths = [r["pfad"].replace("\\", "/").rstrip("/") for r in active_rows if r["pfad"]]
        covered_slugs = {m for r in rows for m in SLUG_RE.findall(r["komponente"] + " " + r["pfad"])}
        for tex in sorted(chapters.rglob("*.tex")):
            rel = tex.relative_to(root).as_posix()
            slug = re.sub(r"^\d+_", "", tex.stem)
            dir_rel = tex.parent.relative_to(root).as_posix()
            covered = (
                slug in covered_slugs
                or any(rel == c or dir_rel == c or rel.startswith(c + "/") for c in covered_paths)
                or any(c.startswith(dir_rel) for c in covered_paths)
            )
            if not covered:
                findings.append(
                    f"{rel}: [HINWEIS:DATEI-OHNE-ZEILE] Kapiteldatei ohne Zeile in der Statustabelle — Zeile ergänzen (Identifikator sec:{slug}) oder Datei ist verwaist.")

    return findings, errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    findings, errors = check(root)
    for line in findings:
        print(line)
    print(f"\nStatus-Abgleich: {errors} FEHLER, {len(findings) - errors} HINWEIS(e).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
