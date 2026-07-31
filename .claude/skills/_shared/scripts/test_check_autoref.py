#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests für check_autoref.py – python -m unittest test_check_autoref

Der Kern ist der Zustandsübergang: Ein Paar, das einmal mit OK quittiert wurde,
muss ruhig bleiben – aber zurückkommen, sobald sich EINE der beiden Seiten
bewegt. Beides wird hier gegen ein echtes Mini-Projekt im Temp-Verzeichnis
gefahren, nicht gegen Attrappen.
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_autoref import (MARKER_RE, absaetze_mit_position,  # noqa: E402
                           kurz_hash, normalisieren, sammle_labels,
                           sammle_verweise, saetze)

SKRIPT = Path(__file__).parent / "check_autoref.py"


def projekt(dateien: dict[str, str]) -> Path:
    root = Path(tempfile.mkdtemp())
    for rel, inhalt in dateien.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(inhalt, encoding="utf-8")
    return root


def lauf(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SKRIPT), *args], cwd=root,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


ZIEL = ("\\subsection{Zielgruppe}\\label{sec:zielgruppe}\n"
        "Die Zielgruppe nennt zwei gleichrangige Anforderungen.\n\n"
        "Ein zweiter Absatz gehört noch ins Fenster.\n\n"
        "Ein dritter Absatz liegt bewusst ausserhalb.\n")
QUELLE = ("\\subsection{Community}\\label{sec:community}\n"
          "Laut~\\autoref{sec:zielgruppe} sucht die Zielgruppe vor allem Sichtbarkeit.\n")


class TestHilfsfunktionen(unittest.TestCase):
    def test_normalisieren_vereinheitlicht_whitespace(self):
        self.assertEqual(normalisieren("a  \n b\t c "), "a b c")

    def test_hash_ist_stabil_gegen_umbrueche(self):
        self.assertEqual(kurz_hash(normalisieren("ein satz\nmit umbruch")),
                         kurz_hash(normalisieren("ein satz mit umbruch")))

    def test_hash_unterscheidet_inhalt(self):
        self.assertNotEqual(kurz_hash("a"), kurz_hash("b"))

    def test_absaetze_trennen_an_leerzeile(self):
        self.assertEqual(len(absaetze_mit_position("a\n\nb\n\nc")), 3)

    def test_saetze_trennen_an_satzzeichen(self):
        self.assertEqual(len(saetze("Erster Satz. Zweiter Satz! Dritter?")), 3)

    def test_marker_findet_gewichtung(self):
        self.assertTrue(MARKER_RE.search("sucht vor allem Sichtbarkeit"))
        self.assertFalse(MARKER_RE.search("beschreibt den Ablauf"))


class TestSammeln(unittest.TestCase):
    def test_zielfenster_ist_absatz_plus_folgender(self):
        root = projekt({"chapters/01/a.tex": ZIEL})
        ziele = sammle_labels([root / "chapters/01/a.tex"], root)
        fenster = ziele["sec:zielgruppe"][2]   # (Datei, Art, Fenster)
        self.assertIn("zwei gleichrangige", fenster)
        self.assertIn("zweiter Absatz", fenster)
        self.assertNotIn("dritter Absatz", fenster,
                         "Fenster zu breit – genau das erzeugt die Fehlalarm-Lawine")

    def test_verweis_wird_mit_satz_erfasst(self):
        root = projekt({"chapters/01/b.tex": QUELLE})
        v = sammle_verweise([root / "chapters/01/b.tex"], root)
        self.assertEqual(len(v), 1)
        self.assertEqual(v[0]["label"], "sec:zielgruppe")
        self.assertIn("vor allem", v[0]["satz"])

    def test_auskommentierter_verweis_zaehlt_nicht(self):
        root = projekt({"chapters/01/b.tex": "% Laut~\\autoref{sec:x} gilt das.\nText.\n"})
        self.assertEqual(sammle_verweise([root / "chapters/01/b.tex"], root), [])


class TestZustandsuebergang(unittest.TestCase):
    """Der eigentliche Zweck des Skripts."""

    def setUp(self):
        self.root = projekt({"chapters/01_ziel/a.tex": ZIEL,
                             "chapters/02_com/b.tex": QUELLE})

    def _hash(self) -> str:
        aus = lauf(self.root).stdout
        for zeile in aus.splitlines():
            if "hash " in zeile:
                return zeile.split("hash ")[1].rstrip(")")
        self.fail(f"kein Hash in der Ausgabe:\n{aus}")

    def test_neues_paar_ist_offen(self):
        r = lauf(self.root)
        self.assertEqual(r.returncode, 1)
        self.assertIn("[NEU]", r.stdout)
        self.assertIn("vor allem", r.stdout)

    def test_gewichtungsmarker_wird_benannt(self):
        self.assertIn("Gewichtungsmarker", lauf(self.root).stdout)

    def test_quittiertes_paar_bleibt_ruhig(self):
        h = self._hash()
        lauf(self.root, "--verdikt", f"{h}=OK", "--notiz", "geprueft")
        r = lauf(self.root)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("unverändert quittiert", r.stdout)

    def test_geaenderte_zielstelle_wirft_zurueck(self):
        h = self._hash()
        lauf(self.root, "--verdikt", f"{h}=OK", "--notiz", "geprueft")
        (self.root / "chapters/01_ziel/a.tex").write_text(
            ZIEL.replace("zwei gleichrangige Anforderungen",
                         "eine einzige Anforderung"), encoding="utf-8")
        r = lauf(self.root)
        self.assertEqual(r.returncode, 1)
        self.assertIn("ZIELSTELLE GEÄNDERT", r.stdout)

    def test_geaenderter_verweisender_satz_wirft_zurueck(self):
        h = self._hash()
        lauf(self.root, "--verdikt", f"{h}=OK", "--notiz", "geprueft")
        (self.root / "chapters/02_com/b.tex").write_text(
            QUELLE.replace("vor allem", "unter anderem"), encoding="utf-8")
        r = lauf(self.root)
        self.assertEqual(r.returncode, 1)
        self.assertIn("GEÄNDERT", r.stdout)

    def test_aenderung_ausserhalb_des_fensters_wirft_nicht_zurueck(self):
        """Der Unterschied zwischen brauchbar und ignoriert.

        Wird im Zielkapitel ein Absatz geändert, auf den sich niemand beruft,
        darf das Paar NICHT auf PRÜFEN springen – sonst wirft jede
        Kürzungsrunde alle Verweise gleichzeitig zurück.
        """
        h = self._hash()
        lauf(self.root, "--verdikt", f"{h}=OK", "--notiz", "geprueft")
        (self.root / "chapters/01_ziel/a.tex").write_text(
            ZIEL.replace("Ein dritter Absatz liegt bewusst ausserhalb.",
                         "Vollstaendig anderer Text an dieser Stelle."), encoding="utf-8")
        r = lauf(self.root)
        self.assertEqual(r.returncode, 0, f"Fehlalarm:\n{r.stdout}")

    def test_alle_erzwingt_neupruefung(self):
        h = self._hash()
        lauf(self.root, "--verdikt", f"{h}=OK", "--notiz", "geprueft")
        r = lauf(self.root, "--alle")
        self.assertEqual(r.returncode, 1)
        self.assertIn("erzwungen", r.stdout)

    def test_fehlendes_ziel_wird_gemeldet(self):
        (self.root / "chapters/02_com/b.tex").write_text(
            QUELLE.replace("sec:zielgruppe", "sec:gibtesnicht"), encoding="utf-8")
        r = lauf(self.root)
        self.assertIn("ZIEL FEHLT", r.stdout)
        self.assertEqual(r.returncode, 1)

    def test_ohne_kapitel_kein_fehler(self):
        leer = projekt({"main.tex": "\\documentclass{article}\n"})
        r = lauf(leer)
        self.assertEqual(r.returncode, 0)
        self.assertIn("Keine Kapiteldateien", r.stdout)

    def test_unbekannter_hash_bei_verdikt_ist_fehler(self):
        r = lauf(self.root, "--verdikt", "deadbeef=OK", "--notiz", "x")
        self.assertEqual(r.returncode, 2)   # 2 = Bedienfehler, 1 = offene Paare
        self.assertIn("kein Paar", r.stderr)


if __name__ == "__main__":
    unittest.main()


# --------------------------------------------------------------------------
# Zusammenführung zweier Implementierungen: Die Identitäts- und Fensterlogik
# stammt aus der einen, die folgenden Prüfungen aus der anderen.
# --------------------------------------------------------------------------

FLOAT_QUELLE = (
    "\\subsection{Wettbewerb}\\label{sec:wettbewerb}\n"
    "Wie~\\autoref{tab:vergleich} zeigt, ist das Werkzeug schwach.\n\n"
    "\\begin{table}[H]\\caption{Vergleich}\\label{tab:vergleich}\n"
    "\\begin{tabular}{ll}Chefkoch & schwach \\\\\\end{tabular}\n"
    "\\end{table}\n")


class TestZielarten(unittest.TestCase):
    """Nicht nur `sec:` – eine geänderte Tabellenzelle zieht Sätze mit."""

    def test_float_ziel_wird_ueberwacht(self):
        root = projekt({"chapters/01_a/a.tex": FLOAT_QUELLE})
        ziele = sammle_labels([root / "chapters/01_a/a.tex"], root)
        self.assertEqual(ziele["tab:vergleich"][1], "Float")

    def test_geaenderte_tabellenzelle_wirft_zurueck(self):
        root = projekt({"chapters/01_a/a.tex": FLOAT_QUELLE})
        aus = lauf(root).stdout
        h = next(z.split("hash ")[1].rstrip(")") for z in aus.splitlines() if "hash " in z)
        lauf(root, "--verdikt", f"{h}=OK", "--notiz", "Zelle deckt den Satz")
        self.assertEqual(lauf(root).returncode, 0)
        (root / "chapters/01_a/a.tex").write_text(
            FLOAT_QUELLE.replace("Chefkoch & schwach", "Chefkoch & mittel"),
            encoding="utf-8")
        r = lauf(root)
        self.assertEqual(r.returncode, 1)
        self.assertIn("ZIELSTELLE GEÄNDERT", r.stdout)

    def test_selbstverweis_auf_eigene_subsection_entfaellt(self):
        root = projekt({"chapters/01_a/a.tex":
                        "\\subsection{A}\\label{sec:a}\n"
                        "Wie in~\\autoref{sec:a} gezeigt, gilt das.\n"})
        ziele = sammle_labels([root / "chapters/01_a/a.tex"], root)
        self.assertEqual(sammle_verweise([root / "chapters/01_a/a.tex"], root, ziele), [])

    def test_label_im_anhang_wird_gefunden(self):
        root = projekt({"chapters/01_a/a.tex":
                        "\\subsection{A}\\label{sec:a}\nSiehe~\\autoref{tab:persona}.\n",
                        "pages/appendix.tex":
                        "\\begin{table}[H]\\caption{P}\\label{tab:persona}\n"
                        "\\begin{tabular}{ll}A & B \\\\\\end{tabular}\n"
                        "\\end{table}\n"})
        r = lauf(root)
        self.assertNotIn("ZIEL FEHLT", r.stdout)
        self.assertIn("tab:persona", r.stdout)


class TestUrteilsdisziplin(unittest.TestCase):
    def setUp(self):
        self.root = projekt({"chapters/01_ziel/a.tex": ZIEL,
                             "chapters/02_com/b.tex": QUELLE})

    def _hash(self) -> str:
        aus = lauf(self.root).stdout
        return next(z.split("hash ")[1].rstrip(")") for z in aus.splitlines() if "hash " in z)

    def test_ok_ohne_notiz_wird_abgelehnt(self):
        r = lauf(self.root, "--verdikt", f"{self._hash()}=OK")
        self.assertEqual(r.returncode, 2)
        self.assertIn("braucht --notiz", r.stderr)

    def test_befund_ohne_notiz_ist_erlaubt(self):
        r = lauf(self.root, "--verdikt", f"{self._hash()}=RENTIERT NICHT")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_unbekanntes_verdikt_wird_abgelehnt(self):
        r = lauf(self.root, "--verdikt", f"{self._hash()}=PASST-SCHON", "--notiz", "x")
        self.assertEqual(r.returncode, 2)

    def test_entfallener_verweis_raeumt_sein_urteil_ab(self):
        h = self._hash()
        lauf(self.root, "--verdikt", f"{h}=OK", "--notiz", "geprueft")
        (self.root / "chapters/02_com/b.tex").write_text(
            "\\subsection{Community}\\label{sec:community}\nOhne Verweis.\n",
            encoding="utf-8")
        lauf(self.root)
        state = json.loads((self.root / "autoref-state.json").read_text(encoding="utf-8"))
        self.assertEqual(state, {})

    def test_bericht_wird_geschrieben(self):
        lauf(self.root)
        self.assertTrue((self.root / "autorefcheck.md").is_file())
