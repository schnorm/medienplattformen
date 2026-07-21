#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt handbuch.pdf im Projekt-Root — direkt aus handbuch.md (reportlab benötigt).

Anders als der frühere Generator (generate_anleitung.py, entfernt) enthält dieses Skript KEINEN
hartkodierten Text: Es rendert die jeweils aktuelle handbuch.md, kann also
nach jeder Handbuch-Änderung erneut laufen, ohne einen veralteten Stand zu
reproduzieren. Unterstützt wird das Markdown-Subset der Handbücher:
Überschriften (#/##/###), Absätze, Aufzählungen (-, 1.), Tabellen (|…|),
Inline-Fett (**…**) und Inline-Code (`…`).

Aufruf (vom Projekt-Root): python .claude/skills/_shared/scripts/generate_handbuch_pdf.py
"""

import datetime
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "handbuch.md"
OUT = ROOT / "handbuch.pdf"

ACCENT = colors.HexColor("#1a3e6e")
LIGHT = colors.HexColor("#eef2f8")
GREY = colors.HexColor("#666666")

# Unicode-Font (Pfeile, ≥, ½ …): Arial aus den Windows-Fonts; Fallback Helvetica
# mit Ersatzzeichen, falls das Skript einmal ohne Arial läuft.
FONT, FONT_B = "Helvetica", "Helvetica-Bold"
_arial = Path("C:/Windows/Fonts/arial.ttf")
if _arial.exists():
    pdfmetrics.registerFont(TTFont("HbArial", str(_arial)))
    pdfmetrics.registerFont(TTFont("HbArial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
    pdfmetrics.registerFontFamily("HbArial", normal="HbArial", bold="HbArial-Bold",
                                  italic="HbArial", boldItalic="HbArial-Bold")
    FONT, FONT_B = "HbArial", "HbArial-Bold"

body = ParagraphStyle("body", fontName=FONT, fontSize=9.5, leading=13.5, spaceAfter=5)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=14, bulletIndent=4, spaceAfter=3)
h1 = ParagraphStyle("h1", fontName=FONT_B, fontSize=13.5, leading=17,
                    spaceBefore=14, spaceAfter=6, textColor=ACCENT)
h2 = ParagraphStyle("h2", fontName=FONT_B, fontSize=11, leading=14,
                    spaceBefore=10, spaceAfter=4, textColor=ACCENT)
title_st = ParagraphStyle("t", fontName=FONT_B, fontSize=19, leading=24,
                          spaceAfter=4, textColor=ACCENT)
sub_st = ParagraphStyle("s", parent=body, fontSize=10.5, textColor=GREY, spaceAfter=10)
cell = ParagraphStyle("cell", parent=body, fontSize=8.5, leading=11, spaceAfter=0)
cellh = ParagraphStyle("cellh", parent=cell, fontName=FONT_B, textColor=colors.white)

TABLE_WIDTH = 17 * cm


def inline(md: str) -> str:
    """Inline-Markdown → reportlab-Markup. Code-Spans zuerst schützen,
    damit ** innerhalb von `chapters/**/*.tex` kein Fett auslöst."""
    # Emoji fehlen auch in Arial — immer ersetzen
    for a, b in (("✅", "[OK]"), ("📝", "[Notiz]")):
        md = md.replace(a, b)
    if FONT == "Helvetica":  # Fallback ohne Unicode-Font
        for a, b in (("→", "->"), ("≥", ">="), ("≈", "~"), ("↔", "<->")):
            md = md.replace(a, b)
    text = escape(md)
    stash: list[str] = []

    def _code(m):
        stash.append(f'<font face="Courier" size="8.3">{m.group(1)}</font>')
        return f"\x00{len(stash) - 1}\x00"

    text = re.sub(r"`([^`]+)`", _code, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def col_widths(rows: list[list[str]], ncols: int) -> list[float]:
    """Spaltenbreiten: proportional zum längsten Zelleninhalt, aber nie
    schmaler als das längste unteilbare Wort der Spalte — sonst bricht
    reportlab mitten im Wort um („schrei b-modus")."""
    charw = 0.18 * cm  # großzügig für 8.5pt inkl. Courier-Code-Spans
    weights, minw = [], []
    for i in range(ncols):
        cells = [r[i] for r in rows]
        weights.append(max(max(len(c) for c in cells), 8))
        longest_word = max((len(w) for c in cells
                            for w in re.split(r"[\s/]+", c.replace("`", ""))), default=4)
        minw.append(min(longest_word * charw + 0.5 * cm, TABLE_WIDTH / 2))
    total = sum(weights)
    widths = [TABLE_WIDTH * w / total for w in weights]
    for _ in range(4):  # Mindestbreiten durchsetzen, Rest proportional stauchen
        deficit = sum(max(0.0, minw[i] - widths[i]) for i in range(ncols))
        if deficit <= 0.01:
            break
        flex = [i for i in range(ncols) if widths[i] > minw[i]]
        flex_total = sum(widths[i] - minw[i] for i in flex) or 1.0
        for i in range(ncols):
            if widths[i] < minw[i]:
                widths[i] = minw[i]
            elif i in flex:
                widths[i] -= deficit * (widths[i] - minw[i]) / flex_total
    return widths


def render_table(rows: list[list[str]]):
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    widths = col_widths(rows, ncols)
    data = [[Paragraph(inline(c), cellh) for c in rows[0]]] + \
           [[Paragraph(inline(c), cell) for c in r] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#b8c4d8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return [Spacer(0, 3), t, Spacer(0, 6)]


def build_story(md_text: str) -> list:
    story: list = []
    lines = md_text.split("\n")
    i, para_buf, first_h1 = 0, [], True

    def flush_para():
        nonlocal para_buf
        if para_buf:
            story.append(Paragraph(inline(" ".join(para_buf)), body))
            para_buf = []

    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            flush_para()
        elif line.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= {"-", ":", " "} for c in cells):  # Trennzeile
                    rows.append(cells)
                i += 1
            story.extend(render_table(rows))
            continue
        elif line.startswith("# ") and first_h1:
            first_h1 = False
            story.append(Paragraph(inline(line[2:]), title_st))
            story.append(Paragraph(
                f"Erzeugt aus handbuch.md · Stand {datetime.date.today():%d.%m.%Y} · "
                "bei Widerspruch gilt die Markdown-Datei", sub_st))
        elif line.startswith("### "):
            flush_para()
            story.append(Paragraph(inline(line[4:]), h2))
        elif line.startswith("## "):
            flush_para()
            story.append(Paragraph(inline(line[3:]), h1))
        elif re.match(r"^(-|\d+\.)\s+", line):
            flush_para()
            m = re.match(r"^(-|\d+\.)\s+(.*)$", line)
            marker = "•" if m.group(1) == "-" else m.group(1)
            story.append(Paragraph(inline(m.group(2)), bullet, bulletText=marker))
        else:
            para_buf.append(line.strip())
        i += 1
    flush_para()
    return story


def main() -> int:
    if not SRC.exists():
        print(f"FEHLER: {SRC} nicht gefunden.", file=sys.stderr)
        return 1
    doc = BaseDocTemplate(str(OUT), pagesize=A4,
                          leftMargin=2 * cm, rightMargin=2 * cm,
                          topMargin=1.8 * cm, bottomMargin=1.8 * cm)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame])])
    doc.build(build_story(SRC.read_text(encoding="utf-8")))
    print(f"OK: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
