#!/usr/bin/env python3
r"""
test_check_quellentreue.py – Tests für check_quellentreue.py.

Ausführen:
    python3 -m unittest test_check_quellentreue.py
oder (mit pytest, falls installiert):
    pytest test_check_quellentreue.py

Die kritischen Tests sind test_wortlaut_* (findet das Skript wörtliche
Übernahmen zuverlässig?) und test_satz_um_* (trifft es den Trägersatz, an dem
die Zitation wirklich hängt – sonst wird der falsche Text mit der Quelle
verglichen und jeder Folgebefund ist wertlos).
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_quellentreue import (  # noqa: E402
    BLOCKZITAT_RE, ENQUOTE_RE, KAPITEL_RE, MIN_ZITAT_WOERTER, PAAR_MIN_ZEICHEN,
    SEITE_RE, anspruchsverlauf, anzeige, ausschnitt, enthaelt_folge,
    epub_kapitel, epub_pfad,
    gesetzte_dateipfade, kalibriere, kernbegriffe, laengste_gemeinsame_folge,
    lies_bib, lies_tex, naechstes_zitat, ohne_zitattext, ortsangabe, pdf_pfad,
    notiz_warnungen, resolve_kapitel, seite_ausserhalb_pages, seiten_liste,
    seitenbereich, spanne, sprache, sprachwechsel, unreferenzierte_volltexte,
    versatz_aus_pages, normalisiere, satz_um, treffer_auf_seite, woerter,
    zitat_segmente, zugangsklasse, CITE_CMD_RE, Zitation)


def schreib(text: str, suffix: str = ".tex") -> Path:
    f = tempfile.NamedTemporaryFile("w", suffix=suffix, delete=False,
                                    encoding="utf-8")
    f.write(text)
    f.close()
    return Path(f.name)


class TestNormalisierung(unittest.TestCase):
    def test_latex_wird_entfernt(self):
        self.assertEqual(
            normalisiere(r"Die \enquote{Bindung} steigt \parencite[S. 5]{keyA}."),
            "die bindung steigt")

    def test_trennstriche_und_umlaute(self):
        self.assertEqual(woerter("Führungs\u00adkräfte prägen"),
                         ["führungskräfte", "prägen"])


class TestSatzErkennung(unittest.TestCase):
    def test_satz_um_nimmt_den_richtigen_satz(self):
        text = "Erster Satz. Zweiter Satz mit Beleg. Dritter Satz."
        self.assertEqual(satz_um(text, text.index("Beleg")),
                         "Zweiter Satz mit Beleg.")

    def test_satz_um_ignoriert_abkuerzungen(self):
        text = "Laut Meyer, S. 12, steigt die Bindung deutlich. Danach folgt Neues."
        self.assertTrue(satz_um(text, text.index("Bindung")).startswith("Laut Meyer"))

    def test_satz_um_bricht_nicht_in_der_zitation_ab(self):
        """Narrative Zitation mitten im Satz: Das „S. 59" darin darf nicht als
        Satzende gelesen werden, sonst fehlt genau die belegte Aussage."""
        text = ("Das Kriterium liefert \\textcite[S. 59]{keyA} mit dem Merkmal "
                "der Absicht. Danach folgt Neues.")
        satz = satz_um(text, text.index("textcite"))
        self.assertIn("Merkmal der Absicht", satz)
        self.assertNotIn("Danach folgt", satz)

    def test_satz_um_am_absatzanfang(self):
        text = "Nur ein Satz mit Beleg."
        self.assertEqual(satz_um(text, 5), text)


class TestTexParsing(unittest.TestCase):
    def test_key_und_seite(self):
        p = schreib(r"Die Bindung steigt \parencite[S.~12]{meyerAllen1991}.")
        z = lies_tex([p])[0]
        self.assertEqual((z.key, z.seite), ("meyerAllen1991", "12"))
        self.assertIn("Bindung steigt", z.satz)

    def test_seitenbereich_und_praefix(self):
        p = schreib(r"Text \parencite[vgl.][S. 12--14]{keyA}.")
        self.assertEqual(lies_tex([p])[0].seite, "12-14")

    def test_mehrere_werke_je_eigene_seite(self):
        """Jeder Block traegt seine eigene Seite – sonst wandert die Seite des
        einen Werks an das andere und erzeugt falsche Seitenbefunde."""
        p = schreib(r"Text \parencites[S. 12]{keyA}[S. 5]{keyB}.")
        z = lies_tex([p])
        self.assertEqual([(x.key, x.seite) for x in z],
                         [("keyA", "12"), ("keyB", "5")])

    def test_block_ohne_seite_erbt_keine(self):
        p = schreib(r"Text \parencites[S. 12]{keyA}{keyB}.")
        self.assertEqual([(x.key, x.seite) for x in lies_tex([p])],
                         [("keyA", "12"), ("keyB", "")])

    def test_mehrere_keys_in_einem_block_teilen_die_seite(self):
        p = schreib(r"Text \parencite[S. 12]{keyA, keyB}.")
        self.assertEqual([(x.key, x.seite) for x in lies_tex([p])],
                         [("keyA", "12"), ("keyB", "12")])

    def test_woertliches_zitat_wird_erkannt(self):
        p = schreib(r"Er nennt es \enquote{ein stabiles Muster} "
                    r"\parencite[S. 8]{keyA}.")
        self.assertEqual(lies_tex([p])[0].woertlich, "ein stabiles Muster")

    def test_begriffsanfuehrung_ist_kein_woertliches_zitat(self):
        """`\\enquote{}` ist an der IU auch das Anführungszeichen für Begriffe.

        Wird eine solche Anführung zum wörtlichen Zitat erklärt, muss sie exakt
        in der Quelle stehen – bei englischer Literatur nie der Fall. Der daraus
        entstehende ZITAT-WEICHT-AB-Befund blockiert das Abgabe-Audit.
        """
        p = schreib(r"Der Begriff \enquote{organisationale Bindung an das "
                    r"Unternehmen} beschreibt ein mehrdimensionales Konstrukt und "
                    r"wird seit den 1990er Jahren untersucht \parencite[S. 67]{keyA}.")
        self.assertEqual(lies_tex([p])[0].woertlich, "")

    def test_zitat_aus_dem_vorsatz_zaehlt_nicht(self):
        """Satzende zwischen Anführung und Beleg: verschiedene Aussagen."""
        p = schreib(r"Müller nennt es \enquote{ein stabiles Muster}. "
                    r"Die Bindung steigt dennoch \parencite[S. 8]{keyA}.")
        self.assertEqual(lies_tex([p])[0].woertlich, "")

    def test_zitat_mit_kurzem_einschub_zaehlt(self):
        """Übliche deutsche Form: Zitat, kurzer Trägereinschub, Beleg."""
        p = schreib(r"Es sei \enquote{ein stabiles Muster}, schreibt Müller "
                    r"\parencite[S. 8]{keyA}.")
        self.assertEqual(lies_tex([p])[0].woertlich, "ein stabiles Muster")

    def test_naechstgelegene_anfuehrung_gewinnt(self):
        p = schreib(r"Zwischen \enquote{Bindung} und \enquote{Fluktuation} "
                    r"\parencite[S. 8]{keyA}.")
        self.assertEqual(lies_tex([p])[0].woertlich, "Fluktuation")

    def test_zitat_nach_dem_beleg_wird_erkannt(self):
        """Narrative Form: erst der Beleg, dann das Zitat.

        `hard-rules-formal.md` rät fürs Theorie-Kapitel ausdrücklich dazu. Wurde
        sie nicht erkannt, lief für sie kein Wortlautabgleich – ein Fehlzitat
        erzeugte dort keinen Befund.
        """
        p = schreib(r"\textcite[S. 67]{keyA} nennt es "
                    r"\enquote{ein stabiles Muster der Bindung}.")
        self.assertEqual(lies_tex([p])[0].woertlich,
                         "ein stabiles Muster der Bindung")

    def test_blockzitat_nach_dem_beleg_wird_erkannt(self):
        p = schreib(r"\textcite[S. 67]{keyA} schreibt dazu: "
                    r"\begin{blockzitat}Ein langes Zitat.\end{blockzitat}")
        self.assertIn("Ein langes Zitat", lies_tex([p])[0].woertlich)

    def test_begriffsanfuehrung_nach_beleg_bleibt_unter_der_schwelle(self):
        """Preis der Symmetrie – gedeckelt, nicht blockierend.

        Die Anführung wird miterfasst, ist aber zu kurz für den blockierenden
        Befund: `pruefe` stuft sie über MIN_ZITAT_WOERTER auf PRÜFEN herunter.
        """
        p = schreib(r"Nach \textcite[S. 5]{keyA} ist der Begriff "
                    r"\enquote{Resilienz} zentral.")
        z = lies_tex([p])[0]
        self.assertEqual(z.woertlich, "Resilienz")
        self.assertLess(len(woerter(z.woertlich)), MIN_ZITAT_WOERTER)

    def test_satzende_zwischen_beleg_und_zitat_zaehlt_nicht(self):
        p = schreib(r"Das belegt \parencite[S. 5]{keyA}. Der Begriff "
                    r"\enquote{Resilienz} stammt aus der Psychologie.")
        self.assertEqual(lies_tex([p])[0].woertlich, "")

    def test_werkbezogen_ohne_seite(self):
        p = schreib(r"Überblick bei \textcite{keyA}.")
        self.assertEqual(lies_tex([p])[0].seite, "")

    def test_hash_stabil_bei_gleichem_inhalt(self):
        a = lies_tex([schreib(r"Gleicher Satz \parencite[S. 3]{keyA}.")])[0]
        b = lies_tex([schreib(r"Gleicher Satz  \parencite[S. 3]{keyA}.")])[0]
        self.assertEqual(a.hash, b.hash)

    def test_hash_aendert_sich_bei_anderer_seite(self):
        a = lies_tex([schreib(r"Gleicher Satz \parencite[S. 3]{keyA}.")])[0]
        b = lies_tex([schreib(r"Gleicher Satz \parencite[S. 4]{keyA}.")])[0]
        self.assertNotEqual(a.hash, b.hash)


class TestZitatAusnahme(unittest.TestCase):
    """Gekennzeichnete Direktzitate dürfen nicht als Wortlautübernahme gelten.

    Direktzitate sind ausdrücklich erlaubt (Zitierleitfaden S. 11: bis 40 Wörter
    im Fließtext, darüber als Blockzitat). Der Wortlaut-Vergleich sucht deshalb
    nur **unmarkierte** Übernahmen – sonst meldet das Skript ausgerechnet die
    korrekte Zitierweise.
    """

    quelle = ("Die organisationale Bindung von Beschaeftigten steigt messbar mit "
              "der wahrgenommenen Fairness der Fuehrungskraft.")

    def test_gekennzeichnetes_zitat_zaehlt_nicht_als_uebernahme(self):
        satz = (r"Dass die Bindung \enquote{steigt messbar mit der wahrgenommenen "
                r"Fairness der Fuehrungskraft}, gilt als gut belegt "
                r"\parencite[S. 8]{keyA}.")
        self.assertTrue(laengste_gemeinsame_folge(woerter(satz),
                                                  woerter(self.quelle), 7),
                        "Testfall taugt nicht, wenn schon roh nichts gefunden wird")
        self.assertEqual(laengste_gemeinsame_folge(woerter(ohne_zitattext(satz)),
                                                   woerter(self.quelle), 7), [])

    def test_unmarkierte_uebernahme_wird_weiter_gefunden(self):
        satz = ("Die Bindung steigt messbar mit der wahrgenommenen Fairness der "
                r"Fuehrungskraft \parencite[S. 8]{keyA}.")
        self.assertTrue(laengste_gemeinsame_folge(woerter(ohne_zitattext(satz)),
                                                  woerter(self.quelle), 7))


class TestWortlaut(unittest.TestCase):
    quelle = ("Die organisationale Bindung von Beschäftigten steigt messbar mit "
              "der wahrgenommenen Fairness der Führungskraft.")

    def test_wortlaut_uebernahme_wird_gefunden(self):
        satz = ("Empirisch zeigt sich: die organisationale Bindung von "
                "Beschäftigten steigt messbar mit der wahrgenommenen Fairness.")
        folge = laengste_gemeinsame_folge(woerter(satz), woerter(self.quelle), 7)
        self.assertGreaterEqual(len(folge), 7)
        self.assertIn("bindung", folge)

    def test_echte_paraphrase_schlaegt_nicht_an(self):
        satz = ("Fair erlebtes Führungsverhalten erhöht die Verbundenheit der "
                "Belegschaft mit ihrem Betrieb.")
        self.assertEqual(
            laengste_gemeinsame_folge(woerter(satz), woerter(self.quelle), 7), [])

    def test_kurze_fachwendung_unter_schwelle(self):
        satz = "Die organisationale Bindung ist hier zentral."
        self.assertEqual(
            laengste_gemeinsame_folge(woerter(satz), woerter(self.quelle), 7), [])

    def test_schwelle_wirkt(self):
        satz = "Die organisationale Bindung von Beschäftigten wächst."
        self.assertTrue(
            laengste_gemeinsame_folge(woerter(satz), woerter(self.quelle), 4))


class TestSeitenpruefung(unittest.TestCase):
    def test_kernbegriffe_ohne_stoppwoerter(self):
        b = kernbegriffe("Die Fairness der Führungskraft steigert die Bindung.")
        self.assertIn("führungskraft", b)
        self.assertNotIn("die", b)

    def test_treffer_auf_seite(self):
        self.assertEqual(
            treffer_auf_seite(["fairness", "bindung"], "Fairness prägt die Bindung."),
            2)

    def test_kein_treffer_bei_fremdem_text(self):
        self.assertEqual(
            treffer_auf_seite(["fairness", "bindung"], "Ein Kapitel über Bilanzen."),
            0)

    def test_kalibrierung_erkennt_versatz(self):
        # PDF-Seite 5 (1-basiert) trägt die gedruckte Seite 1 → Versatz 4
        texte = ["Titel", "", "Inhalt", "Vorwort"] + [f"Text\n{i}" for i in range(1, 9)]
        self.assertEqual(kalibriere(texte), 4)

    def test_kalibrierung_gibt_auf_statt_zu_raten(self):
        self.assertIsNone(kalibriere(["nur Fließtext", "ohne Zahlen"]))

    def test_kalibrierung_ignoriert_jahreszahlen(self):
        # Copyright-Jahr in jeder Fußzeile darf nicht als Seitenzahl zählen
        self.assertIsNone(kalibriere([f"Inhalt\n(c) 2024 Verlag" for _ in range(8)]))

    def test_kalibrierung_liest_zahl_aus_artikelfusszeile(self):
        # „907 R. Setola et al. / Journal" → gedruckt 907 auf PDF-Seite 1
        texte = [f"Fließtext\n{907 + i} R. Setola et al. / Journal" for i in range(6)]
        self.assertEqual(kalibriere(texte), 1 - 907)


class TestSprache(unittest.TestCase):
    de = ("Die Steuerung der Anlage wird durch das Prozessleitsystem "
          "uebernommen und ist nicht direkt erreichbar.")
    en = ("The control system of the plant is connected to the network and "
          "that is the reason why this attack works.")

    def test_sprachen_werden_erkannt(self):
        self.assertEqual(sprache(self.de), "de")
        self.assertEqual(sprache(self.en), "en")

    def test_kurzer_text_bleibt_unbestimmt(self):
        self.assertEqual(sprache("Zu kurz."), "?")

    def test_sprachwechsel_wird_erkannt(self):
        self.assertTrue(sprachwechsel(self.de, self.en))

    def test_gleiche_sprache_ist_kein_wechsel(self):
        self.assertFalse(sprachwechsel(self.de, self.de))


class TestSeitenbereich(unittest.TestCase):
    def test_bereich_wird_gelesen(self):
        self.assertEqual(seitenbereich("907--912"), (907, 912))

    def test_artikelnummer_ist_kein_bereich(self):
        self.assertIsNone(seitenbereich("104321"))

    def test_versatz_aus_pages_bei_passender_seitenzahl(self):
        # Artikel S. 907–912 (6 Seiten), PDF hat 6 Seiten → gedruckt 907 = PDF 1
        self.assertEqual(versatz_aus_pages("907--912", 6), 1 - 907)

    def test_versatz_aus_pages_toleriert_deckblatt(self):
        self.assertEqual(versatz_aus_pages("449--453", 6), 1 - 449)

    def test_versatz_null_ist_ein_gueltiges_ergebnis(self):
        """Konferenzpapier mit eigener Zählung 1–8: Versatz 0. Das Ergebnis darf
        nicht als „nichts gefunden" behandelt werden (0 ist in Python falsy)."""
        self.assertEqual(versatz_aus_pages("1--8", 8), 0)
        self.assertIsNotNone(versatz_aus_pages("1--8", 8))

    def test_versatz_aus_pages_lehnt_unpassenden_umfang_ab(self):
        # Buchkapitel-Bereich, PDF ist das ganze Buch → keine Aussage möglich
        self.assertIsNone(versatz_aus_pages("80--95", 400))


class TestBib(unittest.TestCase):
    def test_feldnamen_sind_verankert(self):
        """`numpages` darf nicht als `pages` gelesen werden – sonst kommt statt
        des Seitenbereichs die Seitenanzahl heraus und der Versatz ist falsch."""
        p = schreib("@inproceedings{keyA,\n  numpages = {8},\n"
                    "  pages = {1--8},\n  booktitle = {Proceedings},\n"
                    "  title = {Der echte Titel},\n  urldate = {2026-01-01},\n"
                    "  date = {2022},\n}\n", suffix=".bib")
        eintrag = lies_bib(p)["keyA"]
        self.assertEqual(eintrag["pages"], "1--8")
        self.assertEqual(eintrag["title"], "Der echte Titel")
        self.assertEqual(eintrag["date"], "2022")

    def test_felder_werden_gelesen(self):
        p = schreib("@article{keyA,\n  title = {Ein Titel},\n"
                    "  file = {C:/pfad/quelle.pdf},\n  year = {2019},\n}\n",
                    suffix=".bib")
        eintrag = lies_bib(p)["keyA"]
        self.assertEqual(eintrag["title"], "Ein Titel")
        self.assertTrue(eintrag["file"].endswith("quelle.pdf"))



class TestExitCode(unittest.TestCase):
    """Buchungen duerfen nicht wie Fehlschlaege aussehen.

    Ein reiner Prueflauf gibt 1 zurueck, solange etwas offen ist (Torfunktion
    fuer Ketten wie `check && latexmk`). Wer dagegen ein Urteil, einen Versatz
    oder eine Ausnahme eintraegt, hat genau das getan, was er wollte – dieser
    Aufruf endet mit 0, auch wenn danach noch Zitationen offen sind.
    """

    def projekt(self, ordner: Path) -> None:
        (ordner / "chapters").mkdir()
        (ordner / "chapters" / "a.tex").write_text(
            "Ein Satz mit Beleg \\parencite[S. 3]{keyA}.\n", encoding="utf-8")
        (ordner / "references.bib").write_text(
            "@article{keyA,\n  title = {Ohne Volltext},\n  year = {2020},\n}\n",
            encoding="utf-8")

    def lauf(self, ordner: Path, *args: str) -> int:
        skript = Path(__file__).parent / "check_quellentreue.py"
        return subprocess.run([sys.executable, str(skript), *args],
                              cwd=ordner, capture_output=True).returncode

    def test_prueflauf_meldet_offene_punkte(self):
        with tempfile.TemporaryDirectory() as d:
            self.projekt(Path(d))
            self.assertEqual(self.lauf(Path(d)), 1)

    def test_buchung_endet_mit_null(self):
        with tempfile.TemporaryDirectory() as d:
            self.projekt(Path(d))
            self.assertEqual(self.lauf(Path(d), "--offset", "keyA=0"), 0)

    def test_fehlende_bib_bleibt_fehler(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "chapters").mkdir()
            self.assertEqual(self.lauf(Path(d), "--offset", "keyA=0"), 2)


class TestZitatEingriffe(unittest.TestCase):
    """Die vom Zitierleitfaden erlaubten Eingriffe dürfen keinen Befund erzeugen.

    Das ist der teuerste False Positive des ganzen Skripts: ZITAT WEICHT AB
    blockiert im Abgabe-Audit. Vor dem Fix scheiterte jedes regelkonform
    bearbeitete Direktzitat am Vergleich.
    """

    QUELLE = woerter(
        "Als Beispiele können Kauf von Bio- oder fair gehandelten Produkten, "
        "Wohnen in einem Passivhaus oder Nutzung von energiesparenden Lampen "
        "genannt werden.")

    def gedeckt(self, zitat: str) -> bool:
        segmente = zitat_segmente(zitat)
        return bool(segmente) and all(enthaelt_folge(s, self.QUELLE) for s in segmente)

    def test_eigene_ergaenzung_in_klammern(self):
        self.assertTrue(self.gedeckt(
            "Als Beispiele [für nachhaltigen Konsum] können Kauf von Bio- oder fair "
            "gehandelten Produkten"))

    def test_sprung_ohne_auslassungszeichen_faellt_auf(self):
        # Dieselbe Stelle, aber der Sprung ist nicht als Auslassung markiert –
        # dann ist es keine erlaubte Kürzung, sondern ein falsches Zitat.
        self.assertFalse(self.gedeckt(
            "Als Beispiele [für nachhaltigen Konsum] können Kauf von Bio- oder fair "
            "gehandelten Produkten genannt werden"))

    def test_auslassung_mit_drei_punkten(self):
        self.assertTrue(self.gedeckt(
            "Als Beispiele können Kauf von Bio- oder fair gehandelten Produkten ... "
            "oder Nutzung von energiesparenden Lampen genannt werden"))

    def test_auslassung_als_ellipse(self):
        self.assertTrue(self.gedeckt(
            "Als Beispiele können Kauf von Bio- oder fair gehandelten Produkten … "
            "oder Nutzung von energiesparenden Lampen genannt werden"))

    def test_sic_und_hervorhebung(self):
        self.assertTrue(self.gedeckt(
            "Wohnen in einem Passivhaus [sic] oder Nutzung von energiesparenden "
            "Lampen [Hervorhebung d. Verf.] genannt werden"))

    def test_weggelassener_buchstabe(self):
        # „prozessorientierte[n]" – der Eingriff steht in eckigen Klammern.
        quelle = woerter("eine prozessorientierte Ausrichtung der wertschöpfenden Aktivitäten")
        segmente = zitat_segmente("prozessorientierte[n] Ausrichtung der wertschöpfenden Aktivitäten")
        self.assertTrue(all(enthaelt_folge(s, quelle) for s in segmente))

    def test_echte_abweichung_faellt_weiter_auf(self):
        self.assertFalse(self.gedeckt(
            "Als Beispiele [sic] können ausschließlich Bioprodukte genannt werden"))

    def test_grossschreibung_und_schlusszeichen_egal(self):
        # Der erste Buchstabe darf angepasst, die Zeichensetzung am Ende geändert werden.
        self.assertTrue(self.gedeckt("Wohnen in einem Passivhaus oder Nutzung von "
                                     "energiesparenden Lampen genannt werden!"))

    def test_kurzes_segment_wird_verworfen(self):
        # Zwei Wörter tragen keinen Vergleich – sie würden überall „gefunden".
        self.assertEqual(zitat_segmente("im Passivhaus"), [])


class TestSeitenListe(unittest.TestCase):
    """Zitierleitfaden 2.2.1 kennt Bereich (S. 24–25) UND Komma (S. 12, 34)."""

    def test_bereich(self):
        self.assertEqual(seiten_liste("24-25"), [(24, 25)])

    def test_kommaliste(self):
        self.assertEqual(seiten_liste("12,34"), [(12, 12), (34, 34)])

    def test_gemischt(self):
        self.assertEqual(seiten_liste("12-13,34"), [(12, 13), (34, 34)])

    def test_leer(self):
        self.assertEqual(seiten_liste(""), [])

    def test_regex_liest_kommaform(self):
        m = SEITE_RE.search("S. 12, 34")
        self.assertEqual(seiten_liste(m.group(1)), [(12, 12), (34, 34)])

    def test_regex_liest_bereich_mit_tilde(self):
        m = SEITE_RE.search("S.~24--25")
        self.assertEqual(seiten_liste(m.group(1)), [(24, 25)])

    def test_lies_tex_normalisiert_kommaform(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "k.tex"
            p.write_text("Aussage \\parencite[S. 12, 34]{keyA}.\n", encoding="utf-8")
            zitate = lies_tex([p])
        self.assertEqual(zitate[0].seite, "12,34")


class TestBlockzitatZuordnung(unittest.TestCase):
    """Die IU-Normalform setzt den Beleg einen Absatz vor das Blockzitat.

    Mit dem engen `\\enquote`-Fenster lief für lange Direktzitate gar kein
    Wortlautabgleich – also dort, wo eine Abweichung am teuersten ist.
    """

    def zuordnung(self, tex: str) -> str:
        zitate = spanne(tex, ENQUOTE_RE) + spanne(tex, BLOCKZITAT_RE, block=True)
        m = CITE_CMD_RE.search(tex)
        return naechstes_zitat(tex, zitate, m.start(), m.end())

    def test_beleg_vor_blockzitat_wird_zugeordnet(self):
        tex = ("\\textcite[S.~40]{steinecke2013} fasst die aktuelle Entwicklung "
               "wie folgt zusammen:\n\n\\begin{blockzitat}\n"
               "In dem unuebersichtlichen Markt suchen die Urlauber nach Transparenz.\n"
               "\\end{blockzitat}\n")
        self.assertIn("Transparenz", self.zuordnung(tex))

    def test_beleg_nach_blockzitat_wird_zugeordnet(self):
        tex = ("\\begin{blockzitat}\nIn dem unuebersichtlichen Markt suchen die "
               "Urlauber nach Transparenz.\n\\end{blockzitat}\n\n"
               "\\parencite[S.~40]{steinecke2013}\n")
        self.assertIn("Transparenz", self.zuordnung(tex))

    def test_weit_entferntes_blockzitat_nicht(self):
        tex = ("\\begin{blockzitat}\nZitattext.\n\\end{blockzitat}\n\n"
               + "Fuelltext. " * 60 + "\n\\parencite[S.~40]{keyA}\n")
        self.assertEqual(self.zuordnung(tex), "")

    def test_entfernte_begriffsanfuehrung_bleibt_unbeachtet(self):
        # `\enquote` ist an der IU auch das Anführungszeichen für Begriffe –
        # das enge Fenster bleibt dafür bestehen.
        tex = ("Der Begriff \\enquote{Resilienz} bezeichnet die Faehigkeit eines "
               "Systems, Stoerungen auszuhalten und danach weiterzuarbeiten "
               "\\parencite[S.~5]{keyA}.\n")
        self.assertEqual(self.zuordnung(tex), "")


class TestAusschnitt(unittest.TestCase):
    """Prüfpaar-Kürzung: spart Kontext, darf aber nie Treffer verstecken."""

    def test_kurzer_text_bleibt_ungekuerzt(self):
        text, gekuerzt = ausschnitt("Kurzer Seitentext.", ["kurzer"])
        self.assertFalse(gekuerzt)
        self.assertEqual(text, "Kurzer Seitentext.")

    def test_alle_treffer_im_ausschnitt(self):
        text = "A" * 500 + " Commitment " + "B" * 500 + " Fluktuation " + "C" * 3000
        aus, gekuerzt = ausschnitt(text, ["commitment", "fluktuation"])
        self.assertTrue(gekuerzt)
        self.assertIn("Commitment", aus)
        self.assertIn("Fluktuation", aus)

    def test_mindestlaenge_wird_nicht_unterschritten(self):
        text = "Commitment " + "X" * 4000
        aus, _ = ausschnitt(text, ["commitment"])
        self.assertGreaterEqual(len(aus), PAAR_MIN_ZEICHEN)

    def test_ohne_treffer_kein_raten(self):
        text = "Z" * 5000
        aus, gekuerzt = ausschnitt(text, ["commitment"])
        self.assertTrue(gekuerzt)
        self.assertTrue(text.startswith(aus))   # Anfang der Seite, nicht irgendwo


def baue_epub(ziel: Path, *, mit_ncx: bool = True) -> Path:
    """Minimales, aber echtes EPUB2 – container.xml → OPF → NCX → XHTML.

    Bewusst mit dem Fall, an dem eine naive Implementierung scheitert: 17.2.1
    und 17.2.2 liegen in DERSELBEN HTML-Datei und sind nur durch Anker
    getrennt. Wer je Datei einmal schneidet, bekommt beide Unterkapitel in
    einen Topf und vergleicht danach den falschen Text mit der Zitation.
    """
    import zipfile
    container = ('<?xml version="1.0"?><container><rootfiles><rootfile '
                 'full-path="OEBPS/content.opf"/></rootfiles></container>')
    opf = ('<?xml version="1.0"?><package><manifest>'
           '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>'
           '<item id="k17" href="17_001.html" media-type="application/xhtml+xml"/>'
           '</manifest><spine toc="ncx"></spine></package>')
    ncx = ('<?xml version="1.0"?><ncx><navMap>'
           '<navPoint><navLabel><text>Vorwort</text></navLabel>'
           '<content src="17_001.html"/></navPoint>'
           '<navPoint><navLabel><text>17.2.1 Ladezeiten senken</text></navLabel>'
           '<content src="17_001.html#u17.2.1"/></navPoint>'
           '<navPoint><navLabel><text>17.2.2 Websites optimieren</text></navLabel>'
           '<content src="17_001.html#u17.2.2"/></navPoint>'
           '</navMap></ncx>')
    html_doc = ('<html><body>'
                '<h2 id="u17.2.1" class="t3">Ladezeiten senken</h2>'
                '<p>Der erste Abschnitt handelt von Antwortzeiten.</p>'
                '<h2 id="u17.2.2" class="t3">Websites optimieren</h2>'
                '<p>Der zweite Abschnitt handelt von Benutzerf&#252;hrung.</p>'
                '</body></html>')
    with zipfile.ZipFile(str(ziel), "w") as z:
        z.writestr("META-INF/container.xml", container)
        z.writestr("OEBPS/content.opf", opf if mit_ncx else opf.replace(
            '<item id="ncx" href="toc.ncx" '
            'media-type="application/x-dtbncx+xml"/>', ""))
        if mit_ncx:
            z.writestr("OEBPS/toc.ncx", ncx)
        z.writestr("OEBPS/17_001.html", html_doc)
    return ziel


class TestKapitelLocator(unittest.TestCase):
    """[Kap. X] statt [S. X] – der Locator für Quellen ohne Seitenzahlen."""

    def test_hierarchische_nummer_vollstaendig(self):
        self.assertEqual(KAPITEL_RE.search("Kap. 17.2.2").group(1), "17.2.2")
        self.assertEqual(KAPITEL_RE.search("Kap.~3").group(1), "3")

    def test_kapitel_landet_in_der_zitation(self):
        p = schreib("Eine Aussage \\parencite[Kap. 17.2.2]{mueller2020}.\n")
        try:
            z = lies_tex([p])[0]
            self.assertEqual(z.kapitel, "17.2.2")
            self.assertEqual(z.seite, "")
            self.assertEqual(ortsangabe(z), "Kap. 17.2.2")
        finally:
            p.unlink()

    def test_kapitel_geht_in_den_hash(self):
        # Sonst teilen sich zwei Zitationen desselben Satzes aus verschiedenen
        # Kapiteln ein Urteil – ein OK für Kap. 3 gälte still auch für Kap. 9.
        a = schreib("Gleiche Aussage \\parencite[Kap. 3]{k}.\n")
        b = schreib("Gleiche Aussage \\parencite[Kap. 9]{k}.\n")
        try:
            self.assertNotEqual(lies_tex([a])[0].hash, lies_tex([b])[0].hash)
        finally:
            a.unlink()
            b.unlink()


class TestEpub(unittest.TestCase):
    """E-Books ohne Seitenzahlen: Kapiteltext aus dem eigenen NCX auflösen."""

    def test_anker_trennen_kapitel_in_einer_datei(self):
        with tempfile.TemporaryDirectory() as d:
            epub = baue_epub(Path(d) / "buch.epub")
            texte, index = epub_kapitel(epub)
            self.assertIn("17.2.1", index)
            self.assertIn("17.2.2", index)
            eins = texte[index["17.2.1"]]
            zwei = texte[index["17.2.2"]]
            self.assertIn("Antwortzeiten", eins)
            self.assertNotIn("Benutzerführung", eins)
            self.assertIn("Benutzerführung", zwei)

    def test_kein_tag_rumpf_im_text(self):
        # Der Schnitt setzt am öffnenden Tag an, nicht mitten im Attribut –
        # sonst bliebe ein Rest wie 'class="t3">' vor dem Kapiteltext stehen.
        with tempfile.TemporaryDirectory() as d:
            texte, index = epub_kapitel(baue_epub(Path(d) / "buch.epub"))
            self.assertNotIn("t3", texte[index["17.2.2"]])
            self.assertTrue(texte[index["17.2.2"]].startswith("Websites"))

    def test_unnummerierte_eintraege_zaehlen_nicht(self):
        # „Vorwort" trägt keine [Kap. X]-Angabe und ist damit nicht zitierbar.
        with tempfile.TemporaryDirectory() as d:
            _texte, index = epub_kapitel(baue_epub(Path(d) / "buch.epub"))
            self.assertEqual(set(index), {"17.2.1", "17.2.2"})

    def test_ohne_ncx_wird_geworfen(self):
        # Der Aufrufer behandelt das wie ein defektes PDF (NICHT PRÜFBAR) –
        # entscheidend ist, dass es nicht still ein leeres Ergebnis liefert.
        with tempfile.TemporaryDirectory() as d:
            epub = baue_epub(Path(d) / "buch.epub", mit_ncx=False)
            with self.assertRaises(Exception):
                epub_kapitel(epub)

    def test_resolve_faellt_auf_oberebene_zurueck(self):
        index = {"17": 0, "17.2": 1}
        self.assertEqual(resolve_kapitel("17.2.2", index), (1, "17.2"))
        self.assertEqual(resolve_kapitel("17.9.9", index), (0, "17"))
        self.assertEqual(resolve_kapitel("4.1", index), (None, ""))

    def test_resolve_bevorzugt_die_genaue_ebene(self):
        index = {"17": 0, "17.2": 1, "17.2.2": 2}
        self.assertEqual(resolve_kapitel("17.2.2", index), (2, "17.2.2"))


class TestDateifeld(unittest.TestCase):
    """`file`-Feld: Zotero trennt mit ';', Dateinamen enthalten aber selbst welche."""

    def test_semikolon_im_dateinamen(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            name = "Meier; Schulz - Handbuch.epub"
            (root / name).write_bytes(b"x")
            self.assertEqual(epub_pfad(name, root), root / name)

    def test_zotero_mehrfachfeld_wird_aufgeteilt(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "b.epub").write_bytes(b"x")
            feld = "a.pdf:application/pdf;b.epub:application/epub+zip"
            self.assertEqual(epub_pfad(feld, root), root / "b.epub")

    def test_epub_pfad_nimmt_kein_pdf(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "a.pdf").write_bytes(b"x")
            self.assertIsNone(epub_pfad("a.pdf", root))
            self.assertEqual(pdf_pfad("a.pdf", root), root / "a.pdf")


class TestPfadFallback(unittest.TestCase):
    """Zotero schreibt absolute Pfade seiner lokalen Ablage – die lösen nur
    auf dem exportierenden Rechner auf. Der Volltext liegt trotzdem im Projekt."""

    def test_zotero_pfad_faellt_auf_projektablage_zurueck(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "sources" / "literature").mkdir(parents=True)
            (root / "sources" / "literature" / "Barker2021.pdf").write_bytes(b"x")
            feld = "/home/normi/Zotero/storage/X6D69NPM/Barker2021.pdf"
            self.assertEqual(pdf_pfad(feld, root),
                             root / "sources" / "literature" / "Barker2021.pdf")

    def test_auch_deutsche_ordnerschreibweise(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "sources" / "literatur").mkdir(parents=True)
            (root / "sources" / "literatur" / "Soma2020.pdf").write_bytes(b"x")
            self.assertIsNotNone(pdf_pfad("/nirgends/Soma2020.pdf", root))

    def test_kein_fuzzy_match_auf_aehnliche_namen(self):
        # Bewusst KEIN unscharfer Abgleich: Ein Fehltreffer prüfte die Zitation
        # gegen das falsche Werk und meldete dafür OK – ein stiller
        # Falschbefund, teurer als der laute Fehlalarm.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "sources" / "literature").mkdir(parents=True)
            (root / "sources" / "literature"
             / "Barker2021_NudgeTechniques.pdf").write_bytes(b"x")
            self.assertIsNone(pdf_pfad("/home/x/Barker2021.pdf", root))

    def test_epub_nutzt_denselben_rueckfall(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "sources" / "literature").mkdir(parents=True)
            (root / "sources" / "literature" / "Buch.epub").write_bytes(b"x")
            self.assertIsNotNone(epub_pfad("/home/x/Zotero/Buch.epub", root))

    def test_gesetzte_pfade_unabhaengig_von_der_existenz(self):
        # Grundlage für die Unterscheidung „kein Volltext" vs. „Pfad ins Leere".
        self.assertEqual(
            gesetzte_dateipfade("/home/x/A.pdf:application/pdf"), ["/home/x/A.pdf"])
        self.assertEqual(gesetzte_dateipfade(""), [])
        self.assertEqual(gesetzte_dateipfade("https://example.org/seite"), [])

    def test_unreferenzierte_volltexte(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "sources" / "literature").mkdir(parents=True)
            for n in ("Genannt.pdf", "Verwaist.pdf", "README.md"):
                (root / "sources" / "literature" / n).write_bytes(b"x")
            bib = {"k": {"file": "/home/x/Genannt.pdf"}}
            self.assertEqual(unreferenzierte_volltexte(bib, root),
                             ["sources/literature/Verwaist.pdf"])


class TestCitekeyAnker(unittest.TestCase):
    """`sources/literature/<citekey>.pdf` – der einzige Bezug, den ein
    BBT-Export nicht überschreiben kann."""

    def projekt(self, dateien: dict[str, bytes]):
        d = tempfile.mkdtemp()
        root = Path(d)
        (root / "sources" / "literature").mkdir(parents=True)
        for name, inhalt in dateien.items():
            (root / "sources" / "literature" / name).write_bytes(inhalt)
        return root

    def test_citekey_loest_ohne_file_feld_auf(self):
        # Der Realfall: zweiter Rechner, BBT-Pfad zeigt ins Nichts.
        root = self.projekt({"barkerWhatNudgeTechniques2021.pdf": b"x"})
        self.assertEqual(
            pdf_pfad("", root, "barkerWhatNudgeTechniques2021"),
            root / "sources" / "literature" / "barkerWhatNudgeTechniques2021.pdf")

    def test_citekey_schlaegt_abweichenden_zotero_namen(self):
        # Vor dieser Aenderung scheiterte genau das: Zotero nennt die Datei
        # anders als das Projekt, der Basename-Rueckfall traf nie.
        root = self.projekt({"barkerWhatNudgeTechniques2021.pdf": b"x"})
        feld = ("/home/normi/Zotero/storage/ABC/"
                "Barker et al. - 2021 - What Nudge Techniques Work.pdf")
        self.assertIsNotNone(pdf_pfad(feld, root, "barkerWhatNudgeTechniques2021"))

    def test_epub_analog(self):
        root = self.projekt({"erlhoferWebsiteKonzeption2017.epub": b"x"})
        self.assertIsNotNone(epub_pfad("", root, "erlhoferWebsiteKonzeption2017"))

    def test_ohne_key_kein_anker(self):
        root = self.projekt({"irgendwas.pdf": b"x"})
        self.assertIsNone(pdf_pfad("", root, ""))

    def test_citekey_datei_gilt_nicht_als_verwaist(self):
        root = self.projekt({"barker2021.pdf": b"x", "Fremd.pdf": b"x"})
        bib = {"barker2021": {"file": "/home/x/ganz-anders.pdf"}}
        self.assertEqual(unreferenzierte_volltexte(bib, root),
                         ["sources/literature/Fremd.pdf"])


class TestNotizWaechter(unittest.TestCase):
    """Ein OK-Urteil wird nie wieder angesehen – seine Notiz ist die einzige Spur."""

    def zit(self, key, notiz, satz="Eine Aussage im Text.", hash_teil="a"):
        z = Zitation(datei="k.tex", zeile=1, key=key, seite="1", satz=satz,
                     woertlich="", notiz=notiz, status="OK")
        return z

    def test_gleiche_notiz_bei_verschiedenen_werken(self):
        bib = {"soma2020": {"author": "Soma, Tammara"},
               "vittuari2023": {"author": "Vittuari, Matteo"}}
        zitate = [self.zit("soma2020", "S. 12 nennt 41 Prozent Haushaltsabfall."),
                  self.zit("vittuari2023", "S. 12 nennt 41 Prozent Haushaltsabfall.")]
        w = notiz_warnungen(zitate, bib)
        self.assertTrue(any("NOTIZ-DUBLETTE" in x for x in w), w)

    def test_gleiche_notiz_bei_derselben_quelle_still(self):
        # Zwei Zitationen desselben Werks duerfen dieselbe Begruendung teilen.
        bib = {"soma2020": {"author": "Soma, Tammara"}}
        zitate = [self.zit("soma2020", "Kap. 1 traegt beide Aussagen."),
                  self.zit("soma2020", "Kap. 1 traegt beide Aussagen.")]
        self.assertEqual(
            [x for x in notiz_warnungen(zitate, bib) if "DUBLETTE" in x], [])

    def test_fremder_autorname_in_der_notiz(self):
        bib = {"soma2020": {"author": "Soma, Tammara"},
               "vittuari2023": {"author": "Vittuari, Matteo"}}
        zitate = [self.zit("vittuari2023", "Soma zeigt das auf S. 12.")]
        w = notiz_warnungen(zitate, bib)
        self.assertTrue(any("NOTIZ-FREMDER-AUTOR" in x for x in w), w)
        self.assertIn("Soma", w[0])

    def test_eigener_autorname_still(self):
        bib = {"vittuari2023": {"author": "Vittuari, Matteo"}}
        zitate = [self.zit("vittuari2023", "Vittuari nennt das in Kap. 1.")]
        self.assertEqual(notiz_warnungen(zitate, bib), [])

    def test_name_aus_dem_traegersatz_still(self):
        # „Wie Soma zeigt, …" im Text – dann ist der Name in der Notiz korrekt.
        bib = {"soma2020": {"author": "Soma, Tammara"},
               "vittuari2023": {"author": "Vittuari, Matteo"}}
        zitate = [self.zit("vittuari2023", "Bestaetigt den Befund von Soma.",
                           satz="Anders als Soma kommt Vittuari zu dem Schluss.")]
        self.assertEqual(
            [x for x in notiz_warnungen(zitate, bib) if "FREMDER" in x], [])

    def test_ohne_notiz_keine_warnung(self):
        bib = {"a2020": {"author": "Alpha, Anna"}}
        self.assertEqual(notiz_warnungen([self.zit("a2020", "")], bib), [])


class TestZugangsklasse(unittest.TestCase):
    """Drei Faelle mit sehr verschiedenem Aufwand statt eines Sammelstatus."""

    def test_buch_ist_beschaffbar(self):
        self.assertEqual(zugangsklasse({"_typ": "book"}), "VOLLTEXT BESCHAFFBAR")
        self.assertEqual(zugangsklasse({"_typ": "incollection"}),
                         "VOLLTEXT BESCHAFFBAR")

    def test_bezahlschranke_wird_erkannt(self):
        self.assertEqual(
            zugangsklasse({"_typ": "article", "doi": "10.1111/ijcs.13038",
                           "url": "https://onlinelibrary.wiley.com/doi/10.1111/x"}),
            "ZUGANG PRÜFEN")

    def test_freier_anbieter_bleibt_still(self):
        # MDPI, Frontiers, PLOS, UN – die behalten den bisherigen Status.
        for url in ("https://www.mdpi.com/2071-1050/13/1/1",
                    "https://digitallibrary.un.org/record/3923923",
                    "https://journals.plos.org/plosone/article?id=10.1371/x"):
            with self.subTest(url=url):
                self.assertEqual(zugangsklasse({"_typ": "article", "url": url}), "")

    def test_explizites_feld_schlaegt_heuristik(self):
        # `zugang` aus dem Bib-Eintrag (via Zotero Extra: tex.zugang).
        eintrag = {"_typ": "article",
                   "url": "https://sciencedirect.com/x", "zugang": "bibliothek"}
        self.assertEqual(zugangsklasse(eintrag), "VOLLTEXT BESCHAFFBAR")
        self.assertEqual(zugangsklasse({"_typ": "book", "zugang": "kein-zugang"}),
                         "ZUGANG PRÜFEN")

    def test_gewoehnlicher_artikel_ohne_hinweis(self):
        self.assertEqual(zugangsklasse({"_typ": "article"}), "")

    def test_eintragstyp_wird_gelesen(self):
        p = schreib("@book{mueller2020,\n  title = {Handbuch},\n"
                    "  author = {Mueller, Anna},\n  date = {2020}\n}\n", ".bib")
        try:
            self.assertEqual(lies_bib(p)["mueller2020"]["_typ"], "book")
        finally:
            p.unlink()


class TestAnspruchsverlauf(unittest.TestCase):
    """Drift zwischen zwei Fundstellen derselben Quelle – die Lücke, die keine
    Einzelprüfung sehen kann, weil beide Stellen für sich bestehen."""

    def z(self, key, satz, zeile=1):
        return Zitation(datei="k.tex", zeile=zeile, key=key, seite="10",
                        satz=satz, woertlich="")

    def test_staerkewort_und_hedge_faellt_auf(self):
        zitate = [
            self.z("soma2020", "Die Studie stützt die Entscheidung, belegt aber "
                               "nicht die Wirkung der konkreten Mechanik."),
            self.z("soma2020", "Damit steht die belegte Wirksamkeit fest.", 40)]
        funde = anspruchsverlauf(zitate)
        self.assertEqual(len(funde), 1, funde)
        self.assertIn("ANSPRUCHSVERLAUF", funde[0])
        self.assertIn("Erstnutzung setzt die Obergrenze", funde[0])

    def test_einheitlich_vorsichtig_bleibt_still(self):
        zitate = [self.z("soma2020", "Die Studie stützt diese Annahme."),
                  self.z("soma2020", "Auch hier deutet darauf einiges hin.", 40)]
        self.assertEqual(anspruchsverlauf(zitate), [])

    def test_einmal_zitiert_bleibt_still(self):
        self.assertEqual(
            anspruchsverlauf([self.z("soma2020", "Das belegt die Wirkung.")]), [])

    def test_verlauf_zeigt_auf_wunsch_alles(self):
        zitate = [self.z("soma2020", "Erste Nennung."),
                  self.z("soma2020", "Zweite Nennung.", 40)]
        funde = anspruchsverlauf(zitate, nur_auffaellig=False)
        self.assertEqual(len(funde), 1, funde)
        self.assertIn("Erste Nennung", funde[0])
        self.assertIn("Zweite Nennung", funde[0])
        # Ohne Auffaelligkeit keine Deutung dazuschreiben.
        self.assertNotIn("Obergrenze", funde[0])


class TestStatusAnzeige(unittest.TestCase):
    """„OK" sagt nur, dass der Wortlaut an der Stelle steht – gelesen wird es
    als „die Quelle trägt die Behauptung"."""

    def test_ok_heisst_nach_aussen_fundstelle_ok(self):
        self.assertEqual(anzeige("OK"), "FUNDSTELLE OK")

    def test_andere_status_unveraendert(self):
        for s in ("PRÜFEN", "WORTLAUT", "SEITE AUSSERHALB", "AUSNAHME"):
            with self.subTest(status=s):
                self.assertEqual(anzeige(s), s)


class TestSeiteAusserhalbPages(unittest.TestCase):
    """Preprint-Zählung gegen Verlagsseiten – reine Feldprüfung, ohne Volltext."""

    def test_preprint_seite_wird_erkannt(self):
        self.assertEqual(seite_ausserhalb_pages("1", "104--114"), (1, 104, 114))

    def test_seite_innerhalb_still(self):
        self.assertIsNone(seite_ausserhalb_pages("106", "104--114"))
        self.assertIsNone(seite_ausserhalb_pages("104", "104--114"))
        self.assertIsNone(seite_ausserhalb_pages("114", "104--114"))

    def test_spanne_teilweise_ausserhalb(self):
        self.assertEqual(seite_ausserhalb_pages("113-120", "104--114"),
                         (120, 104, 114))

    def test_ohne_echten_bereich_kein_befund(self):
        # Bücher, Artikelnummern, Einzelseiten – dort ist nichts abzuleiten.
        for pages in ("", "e12345", "250", "S. 7"):
            with self.subTest(pages=pages):
                self.assertIsNone(seite_ausserhalb_pages("1", pages))

    def test_ohne_seitenangabe_kein_befund(self):
        self.assertIsNone(seite_ausserhalb_pages("", "104--114"))


if __name__ == "__main__":
    unittest.main()
