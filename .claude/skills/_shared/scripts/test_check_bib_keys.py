#!/usr/bin/env python3
r"""
test_check_bib_keys.py — Tests für check_bib_keys.py.

Ausführen:
    python3 -m unittest test_check_bib_keys.py
oder (mit pytest, falls installiert):
    pytest test_check_bib_keys.py

Der kritische Test ist test_parencites_multiblock: vor dem Regex-Fix wurde
der zweite Key-Block in \parencites[S. X]{keyA}[S. Y]{keyB} nicht erfasst,
wodurch erfundene Keys im zweiten Block unentdeckt blieben.
"""

import sys
import unittest
from pathlib import Path

# check_bib_keys.py im selben Verzeichnis importieren
sys.path.insert(0, str(Path(__file__).parent))
from check_bib_keys import extract_used_keys, load_bib_keys  # noqa: E402


class TestExtractUsedKeys(unittest.TestCase):
    def test_simple_cite(self):
        self.assertEqual(extract_used_keys(r"\cite{keyA}"), {"keyA"})

    def test_parencite_with_page(self):
        self.assertEqual(extract_used_keys(r"\parencite[S. 5]{keyA}"), {"keyA"})

    def test_parencite_with_prefix(self):
        self.assertEqual(extract_used_keys(r"\parencite[vgl.][S. 5]{keyA}"), {"keyA"})

    def test_parencite_multiple_keys_same_page(self):
        self.assertEqual(
            extract_used_keys(r"\parencite[S. 5]{keyA, keyB, keyC}"),
            {"keyA", "keyB", "keyC"},
        )

    def test_parencites_multiblock(self):
        """Der ursprüngliche Bug: nur der erste Block wurde erfasst."""
        self.assertEqual(
            extract_used_keys(r"\parencites[S. 12--13]{keyA}[S. 5]{keyB}"),
            {"keyA", "keyB"},
        )

    def test_parencites_three_blocks(self):
        self.assertEqual(
            extract_used_keys(
                r"\parencites[S. 1]{keyA}[S. 2]{keyB}[vgl.][S. 3]{keyC}"
            ),
            {"keyA", "keyB", "keyC"},
        )

    def test_textcite(self):
        self.assertEqual(extract_used_keys(r"\textcite{keyA}"), {"keyA"})

    def test_footcite(self):
        self.assertEqual(extract_used_keys(r"\footcite[S. 7]{keyA}"), {"keyA"})

    def test_autocite(self):
        self.assertEqual(extract_used_keys(r"\autocite{keyA}"), {"keyA"})

    def test_no_command(self):
        self.assertEqual(extract_used_keys("kein Cite hier"), set())

    def test_multiple_cites_in_text(self):
        text = (
            r"Erstens \parencite[S. 5]{keyA}, zweitens \parencites"
            r"[S. 12]{keyB}[S. 7]{keyC} und drittens \cite{keyD}."
        )
        self.assertEqual(
            extract_used_keys(text), {"keyA", "keyB", "keyC", "keyD"}
        )

    def test_command_word_boundary_protects_text(self):
        # \citekey ist ein hypothetischer anderer Befehl — darf NICHT erfasst
        # werden. Der \b in der Regex stellt das sicher.
        self.assertEqual(extract_used_keys(r"\citekey{keyA}"), set())

    def test_citeauthor(self):
        # Muster aus main.tex für Quellenzeilen: \citeauthor{key}, \citeyear{key}
        self.assertEqual(extract_used_keys(r"\citeauthor{keyA}"), {"keyA"})

    def test_citeyear(self):
        self.assertEqual(extract_used_keys(r"\citeyear{keyA}"), {"keyA"})

    def test_citetitle(self):
        self.assertEqual(extract_used_keys(r"\citetitle{keyA}"), {"keyA"})

    def test_citeauthor_and_citeyear_in_caption(self):
        text = r"Eigene Darstellung in Anlehnung an \citeauthor{keyA}, \citeyear{keyA}"
        self.assertEqual(extract_used_keys(text), {"keyA"})

    def test_capitalized_sentence_start_variants(self):
        # biblatex erlaubt großgeschriebene Varianten am Satzanfang.
        self.assertEqual(extract_used_keys(r"\Parencite{keyA}"), {"keyA"})
        self.assertEqual(extract_used_keys(r"\Textcite{keyA}"), {"keyA"})
        self.assertEqual(extract_used_keys(r"\Autocite{keyA}"), {"keyA"})


class TestLoadBibKeys(unittest.TestCase):
    def test_loads_standard_entries(self):
        bib = (
            "@book{keyA,\n  author = {Foo},\n  year = {2020}\n}\n"
            "@article{keyB,\n  author = {Bar},\n  year = {2021}\n}\n"
        )
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".bib", delete=False) as f:
            f.write(bib)
            path = Path(f.name)
        try:
            self.assertEqual(load_bib_keys(path), {"keyA", "keyB"})
        finally:
            path.unlink()


if __name__ == "__main__":
    unittest.main()
