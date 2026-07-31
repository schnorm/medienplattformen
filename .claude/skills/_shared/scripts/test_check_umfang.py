#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests für check_umfang.py – python -m unittest test_check_umfang

Diese Vorlage rechnet in **Wörtern** (die Thesis-Vorlage in Seiten). Der
wichtigste Regressionsschutz hier ist deshalb, dass eine Klammer nur dann als
Budget gilt, wenn eine Wort-Einheit dahintersteht: Ohne diese Bedingung würde
„(3–4 Seiten)" stillschweigend als Wortbudget gelesen, jede Prüfung ginge durch
und niemand bekäme eine Warnung.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_umfang import (MIN_PLAUSIBLE_GESAMT, WORDS_PER_PAGE,  # noqa: E402
                          count_words, parse_plan, strip_latex)


def write(content: str, suffix: str = ".tex") -> Path:
    with tempfile.NamedTemporaryFile("w", suffix=suffix, delete=False, encoding="utf-8") as f:
        f.write(content)
        return Path(f.name)


class TestStripLatex(unittest.TestCase):
    def test_kommentare_zaehlen_nicht(self):
        self.assertNotIn("geheim", strip_latex("Text.\n% geheim\n"))

    def test_maskiertes_prozentzeichen_ist_kein_kommentar(self):
        self.assertIn("Anteil", strip_latex("30\\% Anteil der Befragten."))

    def test_zitate_zaehlen_nicht_als_fliesstext(self):
        out = strip_latex("Ein Satz \\parencite[S. 5]{meyerCommitment1991}.")
        self.assertNotIn("meyerCommitment1991", out)
        self.assertIn("Satz", out)

    def test_textbf_inhalt_bleibt_erhalten(self):
        self.assertIn("wichtig", strip_latex("Das ist \\textbf{wichtig}."))

    def test_umgebungen_werden_entfernt_inhalt_bleibt(self):
        out = strip_latex("\\begin{itemize}\\item Eins\\end{itemize}")
        self.assertNotIn("itemize", out)
        self.assertIn("Eins", out)

    def test_tikz_inhalt_zaehlt_nicht_mit(self):
        # Knotenbeschriftungen eines Diagramms sind kein Fließtext
        out = strip_latex("Davor.\n\\begin{tikzpicture}\n\\node{Knotenbeschriftung};\n"
                          "\\end{tikzpicture}\nDanach.")
        self.assertNotIn("Knotenbeschriftung", out)
        self.assertIn("Davor", out)
        self.assertIn("Danach", out)


class TestCountWords(unittest.TestCase):
    def test_zaehlt_fliesstext(self):
        p = write("Dies sind genau fuenf Woerter.\n")
        try:
            self.assertEqual(count_words(p), 5)
        finally:
            p.unlink()

    def test_fehlende_datei_ist_null(self):
        self.assertEqual(count_words(Path("gibt-es-nicht.tex")), 0)

    def test_faustregel_bleibt_plausibel(self):
        self.assertTrue(300 <= WORDS_PER_PAGE <= 450)


class TestParsePlan(unittest.TestCase):
    def test_liest_wortbudget_und_ordner(self):
        p = write(
            "# Kapitelplan\n\n"
            "## Kapitel 2: Theoretischer Rahmen (1200–1400 Wörter)\n"
            "- **Datei**: `chapters/02_theorie/theorie.tex`\n",
            suffix=".md")
        try:
            budgets, gesamt, warnungen = parse_plan(p)
        finally:
            p.unlink()
        self.assertEqual(budgets, {"02_theorie": ("Theoretischer Rahmen", 1200, 1400)})
        self.assertIsNone(gesamt)
        self.assertEqual(warnungen, [])

    def test_bindestrich_variante(self):
        p = write("## Kapitel 1: Einleitung (500-600 Wörter)\n- `chapters/01_einleitung/`\n",
                  suffix=".md")
        try:
            budgets, _, _ = parse_plan(p)
        finally:
            p.unlink()
        self.assertEqual(budgets["01_einleitung"][1:], (500, 600))

    def test_seitenangabe_gilt_nicht_als_wortbudget(self):
        """Der Unterschied zur Thesis-Vorlage: Ohne Wort-Einheit kein Budget.

        Sonst würde „(3–4 Seiten)" als 3–4 Wörter gelesen; jedes Kapitel läge
        dann „deutlich über Budget" oder – bei umgekehrtem Vergleich – immer
        im Soll. Beides wäre eine falsche Aussage ohne Fehlermeldung.
        """
        p = write("## Kapitel 1: Einleitung (3–4 Seiten)\n- `chapters/01_einleitung/`\n",
                  suffix=".md")
        try:
            budgets, _, _ = parse_plan(p)
        finally:
            p.unlink()
        self.assertEqual(budgets, {})

    def test_fehlender_plan_ist_leer(self):
        budgets, gesamt, warnungen = parse_plan(Path("gibt-es-nicht.md"))
        self.assertEqual((budgets, gesamt, warnungen), ({}, None, []))

    def test_block_ohne_dateiangabe_wird_uebersprungen(self):
        p = write("## Kapitel 3: Methodik (800–900 Wörter)\nKeine Dateizeile.\n", suffix=".md")
        try:
            budgets, _, _ = parse_plan(p)
        finally:
            p.unlink()
        self.assertEqual(budgets, {})

    def test_gesamtwortzahl_als_spanne(self):
        p = write("**Gesamtwortzahl (Richtwert)**: 3000–3500\n", suffix=".md")
        try:
            _, gesamt, warnungen = parse_plan(p)
        finally:
            p.unlink()
        self.assertEqual(gesamt, (3000, 3500))
        self.assertEqual(warnungen, [])

    def test_gesamtwortzahl_als_einzelwert(self):
        p = write("**Gesamtwortzahl (Richtwert)**: 3200\n", suffix=".md")
        try:
            _, gesamt, _ = parse_plan(p)
        finally:
            p.unlink()
        self.assertEqual(gesamt, (3200, 3200))

    def test_tausenderpunkt_wird_gelesen(self):
        p = write("**Gesamtwortzahl (Richtwert)**: 3.000–3.500\n", suffix=".md")
        try:
            _, gesamt, _ = parse_plan(p)
        finally:
            p.unlink()
        self.assertEqual(gesamt, (3000, 3500))

    def test_seitenzahl_statt_wortzahl_ist_fehler(self):
        """Wer versehentlich die Seitenvorgabe einträgt, bekommt einen FEHLER –
        nicht stillschweigend einen Vergleich Wörter gegen Seiten."""
        p = write("**Gesamtwortzahl (Richtwert)**: 10\n", suffix=".md")
        try:
            _, gesamt, warnungen = parse_plan(p)
        finally:
            p.unlink()
        self.assertIsNone(gesamt, "Zielabgleich muss abgeschaltet sein, nicht falsch laufen")
        self.assertTrue(any(w.startswith("FEHLER") for w in warnungen), warnungen)

    def test_plausibilitaetsschwelle_bleibt_niedrig(self):
        # Ein echtes Kapitel liegt weit darüber; die Schwelle darf keine
        # regulären Kleinstprojekte abschneiden.
        self.assertTrue(10 <= MIN_PLAUSIBLE_GESAMT <= 500)


if __name__ == "__main__":
    unittest.main()
