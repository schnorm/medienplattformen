#!/usr/bin/env python3
"""Tests für check_status.py — python -m unittest test_check_status"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_status import check, parse_table  # noqa: E402

TABLE_HEAD = (
    "| Komponente (Identifikator) | Pfad | Status | Notizen |\n"
    "|---|---|---|---|\n"
)


def make_project(claude_table: str, tex_files: list[str]) -> Path:
    root = Path(tempfile.mkdtemp())
    (root / "CLAUDE.md").write_text(
        "# CLAUDE.md\n\n## Aktueller Projektstatus\n\n" + TABLE_HEAD + claude_table,
        encoding="utf-8")
    for rel in tex_files:
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\\subsection{X}\\label{sec:x}\nText.\n", encoding="utf-8")
    return root


class TestCheckStatus(unittest.TestCase):
    def assert_cat(self, findings, cat, expected=True):
        hit = any(cat in f for f in findings)
        self.assertEqual(hit, expected, f"{cat}: {findings}")

    def test_fertig_ohne_datei_ist_fehler(self):
        root = make_project(
            "| `sec:einleitung` | `chapters/01_einleitung/` | FERTIG | |\n", [])
        findings, errors = check(root)
        self.assert_cat(findings, "STATUS-DATEI")
        self.assertEqual(errors, 1)

    def test_fertig_mit_datei_ok(self):
        root = make_project(
            "| `sec:einleitung` | `chapters/01_einleitung/` | FERTIG | |\n",
            ["chapters/01_einleitung/01_einleitung.tex"])
        findings, errors = check(root)
        self.assert_cat(findings, "STATUS-DATEI", expected=False)
        self.assertEqual(errors, 0)

    def test_nicht_begonnen_ohne_datei_ok(self):
        root = make_project(
            "| Kapitelplan | `kapitelplan.md` | NICHT BEGONNEN | |\n", [])
        _, errors = check(root)
        self.assertEqual(errors, 0)

    def test_platzhalter_wird_uebersprungen(self):
        root = make_project(
            "| `sec:<slug-1>` (Platzhalter) | `chapters/…` | NICHT BEGONNEN | |\n", [])
        findings, errors = check(root)
        self.assertEqual(errors, 0)

    def test_datei_ohne_zeile(self):
        root = make_project(
            "| `sec:einleitung` | `chapters/01_einleitung/` | FERTIG | |\n",
            ["chapters/01_einleitung/01_einleitung.tex",
             "chapters/02_theorie/01_konzept.tex"])
        findings, _ = check(root)
        self.assert_cat(findings, "DATEI-OHNE-ZEILE")

    def test_datei_mit_slug_zeile_gedeckt(self):
        root = make_project(
            "| `sec:konzept` | `chapters/02_theorie/` | IN ARBEIT | |\n",
            ["chapters/02_theorie/01_konzept.tex"])
        findings, _ = check(root)
        self.assert_cat(findings, "DATEI-OHNE-ZEILE", expected=False)

    def test_unbekannter_status(self):
        root = make_project(
            "| `sec:x` | `chapters/01_x/` | HALBFERTIG | |\n", [])
        findings, errors = check(root)
        self.assert_cat(findings, "STATUS-WERT")
        self.assertEqual(errors, 0)

    def test_parse_table_liest_zeilen(self):
        rows = parse_table(TABLE_HEAD + "| A | `b.md` | FERTIG | note |\n")
        self.assertEqual(rows, [{"komponente": "A", "pfad": "b.md", "status": "FERTIG"}])


if __name__ == "__main__":
    unittest.main()
