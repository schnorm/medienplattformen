#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests für check_bib_hygiene.py – python -m unittest test_check_bib_hygiene"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_bib_hygiene import hints_for, parse_entries  # noqa: E402

SAMPLE = """
@article{meyerCommitment1991,
  title = {Three-Component Model},
  author = {Meyer, John},
  year = {1991},
  doi = {10.1016/1053-4822(91)90011-Z},
  url = {https://example.org/paper},
}

@book{normanDesign2013,
  title = {The Design of Everyday Things},
  author = {Norman, Don},
  year = {2013},
  urldate = {2026-03-01},
}
"""


class TestParseEntries(unittest.TestCase):
    def setUp(self):
        self.entries = {key: (etype, fields) for etype, key, fields in parse_entries(SAMPLE)}

    def test_findet_alle_eintraege(self):
        self.assertEqual(set(self.entries), {"meyerCommitment1991", "normanDesign2013"})

    def test_liest_eintragstyp(self):
        self.assertEqual(self.entries["meyerCommitment1991"][0], "article")
        self.assertEqual(self.entries["normanDesign2013"][0], "book")

    def test_felder_sind_kleingeschrieben_und_lesbar(self):
        fields = self.entries["meyerCommitment1991"][1]
        self.assertEqual(fields["year"], "1991")
        self.assertIn("doi", fields)
        self.assertIn("url", fields)

    def test_urldate_wird_erkannt(self):
        # IU-Abweichung von APA: kein Abrufdatum – das Feld muss auffindbar sein
        self.assertIn("urldate", self.entries["normanDesign2013"][1])

    def test_leerer_input_liefert_nichts(self):
        self.assertEqual(list(parse_entries("")), [])

    def test_jabref_kommentarblock_stoert_nicht(self):
        # BBT-Exporte enthalten @comment{jabref-meta: …}-Blöcke ohne Komma nach dem
        # „Key". Der Parser greift sie gar nicht erst auf – das ist gewollt, denn
        # main() würde sie ohnehin überspringen. Wichtig ist nur: kein Absturz und
        # keine Phantom-Einträge, die als fehlerhafte Quellen gemeldet würden.
        self.assertEqual(list(parse_entries("@comment{jabref-meta: groupstree;}\n")), [])

    def test_kommentarblock_neben_echtem_eintrag(self):
        text = "@comment{jabref-meta: x;}\n\n@book{a2020,\n  year = {2020},\n}\n"
        keys = [key for _etype, key, _f in parse_entries(text)]
        self.assertEqual(keys, ["a2020"])


class TestHintsFor(unittest.TestCase):
    """Erweiterungs-Checks aus der externen Prüfung ISSE01 (24.07.2026)."""

    def hints(self, etype="article", key="k", **fields):
        return "\n".join(hints_for(etype, key, fields))

    def test_gerade_anfuehrungszeichen_im_titel(self):
        out = self.hints(title='The Terms "Security" and "Safety"', doi="x", langid="english")
        self.assertIn("babel-ngerman", out)

    def test_verlagsort_wird_gemeldet(self):
        out = self.hints(etype="report", location="Genf")
        self.assertIn("kein Verlagsort", out)

    def test_reihentitel_wird_gemeldet(self):
        out = self.hints(etype="incollection", series="Lecture Notes in Computer Science")
        self.assertIn("Reihentitel", out)

    def test_datumsbereich_wird_gemeldet(self):
        out = self.hints(etype="inproceedings", date="2017-09-19/2017-09-22")
        self.assertIn("Datumsbereich", out)

    def test_phantom_volldatum_wird_gemeldet(self):
        out = self.hints(etype="incollection", date="2023-01-01")
        self.assertIn("Volldatum", out)

    def test_jahresdatum_bleibt_still(self):
        out = self.hints(etype="incollection", date="2023")
        self.assertNotIn("Volldatum", out)

    def test_abgekuerzte_institution(self):
        out = self.hints(etype="report", author="{IEC}")
        self.assertIn("abgekürzte Institution", out)

    def test_ausgeschriebene_institution_bleibt_still(self):
        out = self.hints(etype="report", author="{International Electrotechnical Commission}")
        self.assertNotIn("abgekürzte Institution", out)

    def test_title_case_verdacht_englisch(self):
        out = self.hints(title="Risk Assessments Considering Safety And Security", doi="x", langid="english")
        self.assertIn("Title Case", out)

    def test_sentence_case_bleibt_still(self):
        out = self.hints(title="Risk assessments considering safety and security", doi="x", langid="english")
        self.assertNotIn("Title Case", out)

    def test_deutscher_titel_ohne_title_case_meldung(self):
        out = self.hints(title="Einführung in die Softwaretechnik Grundlagen Praxis", doi="x", langid="ngerman")
        self.assertNotIn("Title Case", out)

    def test_fehlendes_sprachfeld(self):
        out = self.hints(title="Some title", doi="x")
        self.assertIn("kein Sprachfeld", out)

    def test_artikelnummer_als_seitenzahl(self):
        out = self.hints(pages="104373", doi="x", langid="english")
        self.assertIn("eid", out)

    def test_seitenbereich_bleibt_still(self):
        out = self.hints(pages="12033--12057", doi="x", langid="english")
        self.assertNotIn("eid", out)

    def test_gesetz_wird_gemeldet(self):
        out = self.hints(etype="report", url="https://www.gesetze-im-internet.de/bsig_2025/__32.html")
        self.assertIn("2.4.2", out)


if __name__ == "__main__":
    unittest.main()
