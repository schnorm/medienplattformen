#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt handbuch.pdf im Projekt-Root – direkt aus handbuch.md (reportlab benötigt).

Dünner Aufrufer um export_pdf.py, das den eigentlichen Markdown-Renderer
enthält (dasselbe Werkzeug erzeugt auch das Exposé-PDF). Es gibt hier bewusst
KEINEN hartkodierten Text: Gerendert wird die jeweils aktuelle handbuch.md,
das Skript kann also nach jeder Handbuch-Änderung erneut laufen, ohne einen
veralteten Stand zu reproduzieren.

Aufruf (vom Projekt-Root): python .claude/skills/_shared/scripts/generate_handbuch_pdf.py
"""

import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from export_pdf import render  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "handbuch.md"
OUT = ROOT / "handbuch.pdf"


def main() -> int:
    return render(SRC, OUT,
                  f"Erzeugt aus handbuch.md · Stand {datetime.date.today():%d.%m.%Y} · "
                  "bei Widerspruch gilt die Markdown-Datei")


if __name__ == "__main__":
    sys.exit(main())
