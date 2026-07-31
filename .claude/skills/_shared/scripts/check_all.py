#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sammelaufruf: alle mechanischen Prüfungen in einem Lauf.

Aufruf (vom Projekt-Root):
    python .claude/skills/_shared/scripts/check_all.py
    python .claude/skills/_shared/scripts/check_all.py --mit-quellen
    python .claude/skills/_shared/scripts/check_all.py --kapitel chapters/02_theorie

Führt nacheinander aus und fasst zusammen:

  1. check_bib_keys.py     – erfundene/fehlende BBT-Keys, ungenutzte Einträge
  2. check_formalia.py     – Formalia, Stil-, Struktur- und Aktivierungs-Checks
  3. check_umfang.py       – Umfang je Kapitel gegen die Budgets aus dem Kapitelplan
  4. check_autoref.py      – interne Querverweise, deren Satz oder Ziel sich bewegt hat
  5. check_bib_hygiene.py  – Feld-Hygiene in references.bib (Zotero-Arbeitsliste)
  6. check_status.py       – Statustabelle gegen das Dateisystem
  7. check_quellentreue.py – Volltextabgleich (nur mit --mit-quellen; dauert,
                             weil jedes Quell-PDF gelesen wird)
  8. check_aussenwelt.py   – unzitierte Außenweltbehauptungen einsammeln (nur
                             mit --mit-fakten; die Verifikation macht danach
                             der `faktencheck`-Skill in kalter Sitzung)

Warum ein Sammelaufruf: Diese sechs bis sieben Läufe stehen in jedem Audit und in
jeder Schreib-Session ohnehin an. Einzeln aufgerufen kostet jeder einen eigenen
Durchgang samt vollständiger Ausgabe; hier läuft alles einmal, und pro Skript
erscheinen höchstens MAX_ZEILEN Zeilen. Fehlt ein Skript oder eine optionale
Abhängigkeit, wird das vermerkt statt abzubrechen.

Exit-Code: 1, sobald ein Teilskript ≠ 0 zurückgibt (mindestens ein harter Fund),
sonst 0. Die Einzelskripte bleiben unverändert aufrufbar – für Detailarbeit an
einem Befund ist der gezielte Einzelaufruf weiterhin der richtige Weg.
"""

import subprocess
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

MAX_ZEILEN = 40          # pro Skript ausgegebene Zeilen, danach Sammelhinweis
SKRIPTE = Path(__file__).resolve().parent


def lauf(name: str, argumente: list[str]) -> tuple[str, int, list[str]]:
    """Ein Teilskript ausführen und (Name, Exit-Code, Ausgabezeilen) liefern."""
    pfad = SKRIPTE / name
    if not pfad.is_file():
        return name, 2, [f"FEHLT: {pfad} nicht gefunden."]
    p = subprocess.run([sys.executable, str(pfad), *argumente],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    zeilen = [z for z in (p.stdout + p.stderr).splitlines() if z.strip()]
    return name, p.returncode, zeilen


def main() -> int:
    args = sys.argv[1:]
    mit_quellen = "--mit-quellen" in args
    mit_fakten = "--mit-fakten" in args
    kapitel = None
    if "--kapitel" in args:
        kapitel = args[args.index("--kapitel") + 1]

    ziel = kapitel or "chapters/"
    aufgaben: list[tuple[str, list[str]]] = [
        ("check_bib_keys.py", ["references.bib", "--dir", ziel, "--report-unused"]),
        ("check_formalia.py", [ziel, "pages/"] if not kapitel else [ziel]),
        ("check_umfang.py", []),
        ("check_autoref.py", ["--datei", kapitel] if kapitel else []),
        ("check_bib_hygiene.py", []),
        ("check_status.py", []),
    ]
    if mit_quellen:
        aufgaben.append(("check_quellentreue.py",
                         ["--datei", ziel] if kapitel else []))
    # Bewusst nicht im Standardsatz: Der Vorfilter meldet beim ersten Lauf jeden
    # noch nicht beurteilten Satz. Während des Schreibens wäre das Rauschen, das
    # man wegzuklicken lernt – gebraucht wird er in der kalten Faktencheck-
    # Sitzung und im Abgabe-Audit.
    if mit_fakten:
        aufgaben.append(("check_aussenwelt.py", ["--datei", ziel]))

    if not Path("references.bib").is_file():
        print("HINWEIS: references.bib fehlt – Key- und Hygiene-Prüfung entfallen.\n")
        aufgaben = [(n, a) for n, a in aufgaben
                    if n not in ("check_bib_keys.py", "check_bib_hygiene.py")]

    bilanz: list[tuple[str, int, int]] = []
    for name, argumente in aufgaben:
        name, code, zeilen = lauf(name, argumente)
        print("=" * 72)
        print(f"  {name}   {'→ Funde' if code else '→ ok'}")
        print("=" * 72)
        for z in zeilen[:MAX_ZEILEN]:
            print(z)
        if len(zeilen) > MAX_ZEILEN:
            print(f"… und {len(zeilen) - MAX_ZEILEN} weitere Zeilen – "
                  f"für die vollständige Ausgabe das Skript einzeln aufrufen.")
        print()
        bilanz.append((name, code, len(zeilen)))

    print("=" * 72)
    print("  Bilanz")
    print("=" * 72)
    for name, code, n in bilanz:
        print(f"  {'FUNDE ' if code else 'ok    '} {name:<26} ({n} Ausgabezeilen)")
    offen = [n for n, c, _ in bilanz if c]
    if offen:
        print(f"\n{len(offen)} Skript(e) mit Funden: {', '.join(offen)}")
    else:
        print("\nAlle mechanischen Prüfungen ohne harte Funde.")
    if not mit_quellen:
        print("Der Volltextabgleich (check_quellentreue.py) lief nicht mit – "
              "in jedem Audit Pflicht: --mit-quellen.")
    if not mit_fakten:
        print("Der Vorfilter für unzitierte Außenweltbehauptungen "
              "(check_aussenwelt.py) lief nicht mit – im Abgabe-Audit und im "
              "`faktencheck`-Skill fällig: --mit-fakten.")
    return 1 if offen else 0


if __name__ == "__main__":
    sys.exit(main())
