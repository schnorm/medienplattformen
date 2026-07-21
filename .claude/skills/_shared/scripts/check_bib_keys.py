#!/usr/bin/env python3
"""
check_bib_keys.py — validiert BibLaTeX-Keys gegen references.bib.

Verhindert erfundene \\parencite{}-Keys, indem Keys deterministisch statt
promptbasiert geprüft werden. Kann zusätzlich ungenutzte Bib-Einträge melden
(Aufräumhinweis vor der Abgabe).

Nutzung:
    # Einzelne Keys direkt prüfen
    python3 check_bib_keys.py references.bib normanDesignEverydayThings2013 someOtherKey2020

    # Alle \\parencite{...}/\\parencites{...}/\\cite{...}-Keys aus einer .tex-Datei prüfen
    python3 check_bib_keys.py references.bib --tex pages/theorie.tex

    # Ganzes Verzeichnis rekursiv prüfen (z. B. chapters/)
    python3 check_bib_keys.py references.bib --dir chapters/

    # Zusätzlich ungenutzte Bib-Einträge melden (nur sinnvoll mit --tex/--dir,
    # da sonst nicht bekannt ist, was "genutzt" bedeuten soll)
    python3 check_bib_keys.py references.bib --dir chapters/ --report-unused

Exit-Code 0 = alle geprüften Keys gefunden, 1 = mindestens ein Key fehlt.
Ungenutzte Einträge beeinflussen den Exit-Code nicht (kein Fehler, nur Hinweis).
"""

import argparse
import re
import sys
from pathlib import Path

BIB_KEY_RE = re.compile(r"@\w+\{\s*([^,\s]+)\s*,", re.MULTILINE)
# Erfasst \parencite, \parencites, \cite, \textcite, \footcite, \autocite etc.
# Die Argument-Liste eines Cite-Befehls ist eine Folge aus optionalen
# [...]-Präfixen und genau einem {...}-Key. Mehrere ([prefix]*){key}-Blöcke
# hintereinander (z. B. \parencites) sind erlaubt; pro Block können beliebig
# viele Präfixe vor dem Key stehen (z. B. [vgl.][S. 5]{key}). Die Capture-
# Gruppe nimmt die gesamte Argument-Liste; KEY_GROUP_RE extrahiert danach
# alle {...}-Inhalte.
CITE_CMD_RE = re.compile(
    r"\\(?:[Pp]arencites?|[Cc]ites?|[Tt]extcites?|[Ff]ootcites?|[Aa]utocites?"
    r"|[Cc]iteauthor|[Cc]iteyear|[Cc]itetitle)\b"
    r"((?:\[[^\]]*\]|\{[^}]*\})*)"
)
KEY_GROUP_RE = re.compile(r"\{([^}]*)\}")


def load_bib_keys(bib_path: Path) -> set[str]:
    text = bib_path.read_text(encoding="utf-8", errors="replace")
    return set(BIB_KEY_RE.findall(text))


def extract_used_keys(text: str) -> set[str]:
    used = set()
    for match in CITE_CMD_RE.finditer(text):
        for key in KEY_GROUP_RE.findall(match.group(1)):
            for k in key.split(","):
                k = k.strip()
                if k:
                    used.add(k)
    return used


def main() -> int:
    parser = argparse.ArgumentParser(description="Validiert BBT-Keys gegen references.bib")
    parser.add_argument("bib", type=Path, help="Pfad zu references.bib")
    parser.add_argument("keys", nargs="*", help="Einzelne Keys, die geprüft werden sollen")
    parser.add_argument("--tex", type=Path, help="Einzelne .tex-Datei nach Keys durchsuchen")
    parser.add_argument("--dir", type=Path, help="Verzeichnis rekursiv nach .tex-Dateien durchsuchen")
    parser.add_argument(
        "--report-unused", action="store_true",
        help="Zusätzlich Bib-Einträge melden, die in den durchsuchten Dateien nie zitiert werden",
    )
    args = parser.parse_args()

    if not args.bib.exists():
        print(f"FEHLER: {args.bib} nicht gefunden.", file=sys.stderr)
        return 1

    bib_keys = load_bib_keys(args.bib)

    to_check: set[str] = set(args.keys)

    if args.tex:
        if not args.tex.exists():
            print(f"FEHLER: {args.tex} nicht gefunden.", file=sys.stderr)
            return 1
        to_check |= extract_used_keys(args.tex.read_text(encoding="utf-8", errors="replace"))

    if args.dir:
        if not args.dir.exists():
            print(f"FEHLER: {args.dir} nicht gefunden.", file=sys.stderr)
            return 1
        for tex_file in args.dir.rglob("*.tex"):
            to_check |= extract_used_keys(tex_file.read_text(encoding="utf-8", errors="replace"))

    if not to_check:
        print("Keine Keys zum Prüfen übergeben (weder direkt noch via --tex/--dir gefunden).")
        return 0

    missing = sorted(to_check - bib_keys)
    found = sorted(to_check & bib_keys)

    if found:
        print(f"OK ({len(found)}): {', '.join(found)}")

    exit_code = 0
    if missing:
        print(f"FEHLEND in {args.bib.name} ({len(missing)}): {', '.join(missing)}", file=sys.stderr)
        print("→ Key ist erfunden oder Zotero/BBT-Export ist nicht aktuell. Nicht verwenden.", file=sys.stderr)
        exit_code = 1
    else:
        print(f"Alle {len(to_check)} Keys existieren in {args.bib.name}.")

    if args.report_unused:
        unused = sorted(bib_keys - to_check)
        if unused:
            print(f"UNGENUTZT in {args.bib.name} ({len(unused)}, kein Fehler, nur Aufräumhinweis): {', '.join(unused)}")
        else:
            print(f"Keine ungenutzten Einträge in {args.bib.name}.")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
