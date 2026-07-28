#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Umfangs-Tracker: Wörter je Kapitel gegen die Budgets aus kapitelplan.md.

Aufruf (vom Projekt-Root):
    python .claude/skills/_shared/scripts/check_umfang.py [chapters/] [--plan kapitelplan.md]

Zählt Wörter je Kapitelordner (LaTeX-Kommandos, Kommentare und Nicht-Text-
Umgebungen entfernt), vergleicht mit den Wortbudgets aus `kapitelplan.md`
(`## Kapitel N: <Name> (X–Y Wörter)`) und rechnet zusätzlich in Seiten um
(IU-Format: ~375 Wörter/Seite Fließtext).

**Warum das Skript existiert:** Der Seitenumfang wurde bis dahin nur in
Teil-Check D aus dem gerenderten PDF geprüft. Fehlt lualatex in der Umgebung,
wurde der Punkt kommentarlos übersprungen – und der Voll-Audit konnte
„abgabereif" melden, obwohl das eine Kriterium, dessen Nichterfüllung laut
IU-Richtlinien ausdrücklich Punktabzug kosten kann, nie geprüft wurde. Diese
Schätzung ist kein Messwert, aber sie macht den Umfang in jeder Session
sichtbar, unabhängig vom Build.

Die Zielgröße kommt aus `kapitelplan.md` → `**Gesamtwortzahl (Richtwert)**`;
fehlt sie, wird die Summe der Kapitelbudgets verwendet. Abbildungen und
Tabellen erhöhen den realen Seitenbedarf: Die Werte sind Untergrenzen.

Exit-Code 0 = nur OK/HINWEIS · 1 = mindestens ein WARNUNG-Fund (Budget deutlich
überschritten oder Gesamtumfang über der Zielgröße).
"""

import re
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


WORDS_PER_PAGE = 375
# Umgebungen, deren INHALT kein Fließtext ist: Knotenbeschriftungen eines
# Diagramms und Quelltextzeilen zählen sonst als Wörter.
NON_TEXT_ENVS = ("tikzpicture", "lstlisting", "verbatim", "axis", "minted")

KAPITEL_RE = re.compile(r"Kapitel\s+\d+:\s*(.+?)\s*\((\d+)\s*[–\-—]\s*(\d+)\s*W", re.I)
DIR_RE = re.compile(r"chapters/([0-9a-zA-Z_\-]+)/")
GESAMT_RE = re.compile(
    r"Gesamtwortzahl[^:]*:\s*\D{0,12}(\d[\d.]*)(?:\s*[–\-—]\s*(\d[\d.]*))?", re.I)


def strip_latex(text: str) -> str:
    text = re.sub(r"(?<!\\)%.*", "", text)                      # Kommentare
    for env in NON_TEXT_ENVS:
        text = re.sub(r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}",
                      " ", text, flags=re.DOTALL)
    text = re.sub(r"\\begin\{[^}]*\}(\[[^\]]*\])?", " ", text)  # übrige Umgebungen
    text = re.sub(r"\\end\{[^}]*\}", " ", text)
    # Zitations-/Referenz-Kommandos samt Argument entfernen (kein Fließtext)
    text = re.sub(r"\\(parencites?|textcite|cite\w*|autoref|ref|label|input|include"
                  r"|includegraphics|ac|acro|quelle)\*?(\[[^\]]*\])*(\{[^{}]*\})+", " ", text)
    # übrige Kommandos: Befehl weg, Klammerinhalt behalten (\textbf{Wort} -> Wort)
    for _ in range(3):
        text = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])*\{([^{}]*)\}", r" \2 ", text)
    text = re.sub(r"\\[a-zA-Z@]+\*?", " ", text)
    text = re.sub(r"[{}~$&_^]", " ", text)
    return text


def count_words(path: Path) -> int:
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0
    return len(re.findall(r"\S+", strip_latex(raw)))


def _zahl(s: str) -> int:
    return int(s.replace(".", ""))


def parse_plan(plan_path: Path):
    """(Budgets je Kapitelordner, Gesamt-Zielspanne) aus kapitelplan.md."""
    budgets, gesamt = {}, None
    if not plan_path.is_file():
        return budgets, gesamt
    text = plan_path.read_text(encoding="utf-8", errors="replace")
    g = GESAMT_RE.search(text)
    if g:
        lo = _zahl(g.group(1))
        gesamt = (lo, _zahl(g.group(2)) if g.group(2) else lo)
    for block in re.split(r"(?m)^## ", text):
        head = KAPITEL_RE.match(block)
        if not head:
            continue
        mdir = DIR_RE.search(block)
        if mdir:
            budgets[mdir.group(1)] = (head.group(1), int(head.group(2)), int(head.group(3)))
    return budgets, gesamt


def main() -> int:
    args = list(sys.argv[1:])
    plan_path = Path("kapitelplan.md")
    if "--plan" in args:
        i = args.index("--plan")
        plan_path = Path(args[i + 1])
        del args[i:i + 2]
    chapters = Path(args[0]) if args else Path("chapters")
    if not chapters.is_dir():
        print(f"FEHLER: Ordner nicht gefunden: {chapters}")
        return 1

    budgets, gesamt = parse_plan(plan_path)
    rows, total_words, warn = [], 0, False
    for chap_dir in sorted(p for p in chapters.iterdir() if p.is_dir()):
        words = sum(count_words(f) for f in sorted(chap_dir.glob("*.tex")))
        if words == 0:
            continue
        total_words += words
        note = ""
        b = budgets.get(chap_dir.name)
        if b:
            _name, lo, hi = b
            if words > hi * 1.15:
                note, warn = f"WARNUNG: Budget {lo}–{hi} W. deutlich überschritten", True
            elif words > hi:
                note = f"HINWEIS: über Budget {lo}–{hi} W."
            elif words < lo * 0.5:
                note = f"HINWEIS: erst {words} von {lo}–{hi} W."
            else:
                note = f"OK (Budget {lo}–{hi} W.)"
        rows.append((chap_dir.name, words, words / WORDS_PER_PAGE, note))

    if not rows:
        print("Keine Kapiteltexte gefunden – noch nichts zu messen.")
        return 0

    width = max(len(r[0]) for r in rows)
    print(f"{'Kapitel':<{width}}  {'Wörter':>7}  {'~Seiten':>7}  Bewertung")
    for name, words, pages, note in rows:
        print(f"{name:<{width}}  {words:>7}  {pages:>7.1f}  {note}")

    total_pages = total_words / WORDS_PER_PAGE
    ziel = f" · Ziel {gesamt[0]}–{gesamt[1]} W." if gesamt else ""
    print(f"\nGesamt Textteil: {total_words} Wörter ≈ {total_pages:.1f} Seiten{ziel} "
          f"(Schätzung bei ~{WORDS_PER_PAGE} W./Seite; Abbildungen und Tabellen kommen hinzu)")
    if gesamt and total_words > gesamt[1]:
        print(f"WARNUNG: Gesamtumfang über der Zielgröße ({total_words} > {gesamt[1]}) – "
              f"Kürzungsbedarf. Erste Reserve sind mehrfach ausformulierte Kernbefunde "
              f"(pruef-modus Teil-Check B → Redundanz).")
        warn = True
    elif gesamt and total_words < gesamt[0]:
        print("HINWEIS: noch unter der Zielgröße (normal, solange Kapitel fehlen).")
    if not gesamt and not budgets:
        print("HINWEIS: keine Budgets in kapitelplan.md gefunden – nur Ist-Wert ausgegeben. "
              "Format: „## Kapitel N: <Name> (X–Y Wörter)" + "\" bzw. "
              "„**Gesamtwortzahl (Richtwert)**: X–Y\".")
    return 1 if warn else 0


if __name__ == "__main__":
    sys.exit(main())
