#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests für check_aussenwelt.py – python -m unittest test_check_aussenwelt"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_aussenwelt import (  # noqa: E402
    Kandidat, aufraeumen, bewerte, buche, sammle)


def projekt(dateien: dict[str, str]) -> Path:
    root = Path(tempfile.mkdtemp())
    for rel, inhalt in dateien.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(inhalt, encoding="utf-8")
    return root


def kandidaten_von(root: Path) -> list[Kandidat]:
    return sammle(root, "chapters")[0]


def saetze(kandidaten: list[Kandidat]) -> str:
    return " || ".join(k.satz for k in kandidaten)


class TestVorfilter(unittest.TestCase):
    def test_absatz_traegt_signal_an_anaphorischen_satz_weiter(self):
        """Der teuerste reale Fall: Der Satz nennt nur „die Plattform"."""
        root = projekt({"chapters/02/01_wettbewerb.tex":
                        "Chefkoch.de zählt zu den etablierten Communities.\n"
                        "Für Resteverwertung bietet die Plattform kein "
                        "Werkzeug, das aus mehreren Resten Vorschläge "
                        "ableitet.\n"})
        k = kandidaten_von(root)
        treffer = [x for x in k if "kein Werkzeug" in x.satz]
        self.assertEqual(len(treffer), 1, saetze(k))
        self.assertEqual(treffer[0].signale, ["~DOMAIN"])
        self.assertIn("kein", treffer[0].absolut)

    def test_satz_ohne_signal_ausserhalb_eines_traegerabsatzes(self):
        root = projekt({"chapters/02/01_konzept.tex":
                        "Das Konzept sieht eine Feed-Ansicht vor.\n"})
        self.assertEqual(kandidaten_von(root), [])

    def test_zitierter_satz_gehoert_teil_check_g(self):
        root = projekt({"chapters/02/01_theorie.tex":
                        "Gamification erhöht die Teilnahme um 51 \\% "
                        "\\parencite[S. 12]{soma2020}.\n"})
        self.assertEqual(kandidaten_von(root), [])

    def test_woertliches_zitat_ist_ausgenommen(self):
        root = projekt({"chapters/02/01_theorie.tex":
                        "Der Bericht nennt \\enquote{TikTok im Jahr 2024} "
                        "als Beispiel.\n"})
        # Nur der maskierte Zitatinhalt trug Signale – bleibt also leer.
        self.assertEqual(kandidaten_von(root), [])

    def test_prozentangabe_ist_hartes_signal(self):
        root = projekt({"chapters/02/01_a.tex":
                        "Der Anteil liegt bei 37 Prozent.\n"})
        k = kandidaten_von(root)
        self.assertEqual(len(k), 1)
        self.assertEqual(k[0].signale, ["PROZENT"])

    def test_binnenmajuskel_erkennt_produktnamen(self):
        root = projekt({"chapters/02/01_a.tex":
                        "Auf TikTok entstehen kurze Rezeptvideos.\n"})
        self.assertEqual(kandidaten_von(root)[0].signale, ["PRODUKTNAME"])

    def test_normales_deutsches_substantiv_ist_kein_produktname(self):
        root = projekt({"chapters/02/01_a.tex":
                        "Die Zielgruppe erwartet Rückmeldung und "
                        "Sichtbarkeit.\n"})
        self.assertEqual(kandidaten_von(root), [])

    def test_institution_wird_erkannt(self):
        root = projekt({"chapters/02/01_a.tex":
                        "Das Bundesministerium für Ernährung stellt eine App "
                        "bereit.\n"})
        self.assertIn("INSTITUTION", kandidaten_von(root)[0].signale)

    def test_kommentarzeile_zaehlt_nicht(self):
        root = projekt({"chapters/02/01_a.tex":
                        "% TODO: TikTok noch pruefen, Stand 2024\n"
                        "Das Konzept sieht eine Feed-Ansicht vor.\n"})
        self.assertEqual(kandidaten_von(root), [])

    def test_dateien_ohne_kandidaten_werden_gemeldet(self):
        root = projekt({"chapters/02/01_a.tex": "Auf TikTok läuft das.\n",
                        "chapters/02/02_b.tex": "Das Konzept sieht X vor.\n"})
        _, ohne = sammle(root, "chapters")
        self.assertEqual(ohne, ["chapters/02/02_b.tex"])

    def test_acronyms_wird_immer_mitgeprueft(self):
        root = projekt({"chapters/02/01_a.tex": "Das Konzept sieht X vor.\n",
                        "pages/acronyms.tex":
                        "\\acro{BMLEH}{Bundesministerium für Landwirtschaft}\n"})
        k, _ = sammle(root, "chapters")
        self.assertTrue(any(x.datei == "pages/acronyms.tex" for x in k),
                        saetze(k))

    def test_gleicher_satz_zweimal_nur_einmal(self):
        satz = "Auf TikTok entstehen kurze Rezeptvideos.\n"
        root = projekt({"chapters/02/01_a.tex": satz,
                        "chapters/03/01_fazit.tex": satz})
        self.assertEqual(len(kandidaten_von(root)), 1)


class TestZustand(unittest.TestCase):
    def setUp(self):
        self.root = projekt({"chapters/02/01_a.tex":
                             "Auf TikTok entstehen kurze Rezeptvideos.\n"})
        self.k = kandidaten_von(self.root)
        self.state = {"urteile": {}}
        bewerte(self.k, self.state)

    def test_neuer_kandidat_ist_neu(self):
        self.assertEqual(self.k[0].status, "NEU")

    def test_urteil_haelt_bei_unveraendertem_satz(self):
        buche(self.state, self.k, [f"{self.k[0].hash}=BESTÄTIGT"], "tiktok.com")
        neu = kandidaten_von(self.root)
        bewerte(neu, self.state)
        self.assertEqual(neu[0].status, "BESTÄTIGT")

    def test_geaenderter_satz_wird_wieder_neu(self):
        buche(self.state, self.k, [f"{self.k[0].hash}=BESTÄTIGT"], "tiktok.com")
        (self.root / "chapters/02/01_a.tex").write_text(
            "Auf TikTok entstehen seit 2020 kurze Rezeptvideos.\n",
            encoding="utf-8")
        neu = kandidaten_von(self.root)
        bewerte(neu, self.state)
        self.assertNotEqual(neu[0].hash, self.k[0].hash)
        self.assertEqual(neu[0].status, "NEU")

    def test_eigene_setzung_bleibt_dauerhaft_still(self):
        buche(self.state, self.k, [f"{self.k[0].hash}=EIGENE SETZUNG"], "")
        neu = kandidaten_von(self.root)
        bewerte(neu, self.state)
        self.assertEqual(neu[0].status, "EIGENE SETZUNG")

    def test_bestaetigt_ohne_beleg_wird_abgelehnt(self):
        fehler = buche(self.state, self.k, [f"{self.k[0].hash}=BESTÄTIGT"], "")
        self.assertEqual(fehler, 1)
        self.assertEqual(self.state["urteile"], {})

    def test_widerlegt_ohne_notiz_ist_erlaubt(self):
        self.assertEqual(
            buche(self.state, self.k, [f"{self.k[0].hash}=WIDERLEGT"], ""), 0)

    def test_unbekanntes_verdikt_wird_abgelehnt(self):
        self.assertEqual(
            buche(self.state, self.k, [f"{self.k[0].hash}=EGAL"], "x"), 1)

    def test_aufraeumen_entfernt_verwaiste_urteile(self):
        buche(self.state, self.k, [f"{self.k[0].hash}=WIDERLEGT"], "")
        (self.root / "chapters/02/01_a.tex").write_text(
            "Das Konzept sieht X vor.\n", encoding="utf-8")
        self.assertEqual(aufraeumen(self.state, kandidaten_von(self.root)), 1)
        self.assertEqual(self.state["urteile"], {})


class TestSichtungsmarker(unittest.TestCase):
    """`% SICHTUNG:` ist eine Rangfolge, kein Tor – der Filter läuft über alles."""

    def test_deklariertes_kapitel_kommt_zuerst(self):
        root = projekt({
            "chapters/02/01_a.tex": "Auf TikTok entstehen kurze Rezeptvideos.\n",
            "chapters/02/02_b.tex": "% SICHTUNG: eigene Sichtung 07/2026\n"
                                    "Chefkoch.de ist eine etablierte Community.\n"})
        k = kandidaten_von(root)
        self.assertEqual(len(k), 2)
        self.assertTrue(k[0].sichtung, "deklariertes Kapitel muss zuerst stehen")
        self.assertFalse(k[1].sichtung)

    def test_undeklariertes_kapitel_faellt_nicht_raus(self):
        root = projekt({"chapters/02/01_a.tex": "Auf TikTok entstehen Rezeptvideos.\n"})
        self.assertEqual(len(kandidaten_von(root)), 1,
                         "ohne Marker dürfen Kandidaten nicht verschwinden")

    def test_marker_ohne_doppelpunkt_zaehlt(self):
        root = projekt({"chapters/02/01_a.tex":
                        "% SICHTUNG\nAuf TikTok entstehen Rezeptvideos.\n"})
        self.assertEqual(kandidaten_von(root)[0].sichtung, "deklariert")

    def test_aehnliches_wort_loest_nicht_aus(self):
        root = projekt({"chapters/02/01_a.tex":
                        "% SICHTUNGSWEISE egal\nAuf TikTok entstehen Rezeptvideos.\n"})
        self.assertEqual(kandidaten_von(root)[0].sichtung, "")

    def test_ueberschrift_steht_nicht_im_kandidatensatz(self):
        root = projekt({"chapters/02/01_a.tex":
                        "\\subsection{Wettbewerb}\\label{sec:w}\n"
                        "Chefkoch.de ist etabliert.\n"})
        self.assertNotIn("subsection", kandidaten_von(root)[0].satz)


if __name__ == "__main__":
    unittest.main()
