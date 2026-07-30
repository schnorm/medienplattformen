#!/usr/bin/env python3
"""Tests für check_formalia.py – python3 -m unittest test_check_formalia.py"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_formalia import (  # noqa: E402
    anhang_buchstaben, autorenschaft, caption_text, check_aktivierung,
    check_anhang_verweise, check_caption_doppelbelegung, check_file,
    check_gruppenbezug, check_meta_platzhalter, check_title_duplication,
    check_ungenutzte_acronyms, check_unterpunkte, check_zahlwoerter,
    find_acronyms, strip_comment)


def run_on(content: str):
    findings, errors, _meta = run_full(content)
    return findings, errors


def run_full(content: str):
    with tempfile.NamedTemporaryFile("w", suffix=".tex", delete=False, encoding="utf-8") as f:
        f.write(content)
        p = Path(f.name)
    try:
        return check_file(p)
    finally:
        p.unlink()


class TestChecks(unittest.TestCase):
    def assert_cat(self, findings, cat, expected=True):
        hit = any(f"[FEHLER:{cat}]" in f or f"[HINWEIS:{cat}]" in f for f in findings)
        self.assertEqual(hit, expected, f"{cat}: {findings}")

    def test_pronomen(self):
        findings, errors = run_on("Hier zeigt man die Ergebnisse.\n")
        self.assert_cat(findings, "PRONOMEN")
        self.assertEqual(errors, 1)

    def test_pronomen_not_in_word(self):
        findings, _ = run_on("Das Management der Wirtschaft.\n")  # man/wir als Teilwort
        self.assert_cat(findings, "PRONOMEN", expected=False)

    def test_pronomen_in_comment_ignored(self):
        findings, _ = run_on("% hier steht man nur im Kommentar\nText ohne Verstoss.\n")
        self.assert_cat(findings, "PRONOMEN", expected=False)

    def test_todo_quelle_marker_in_comment(self):
        # Arbeitsmarker leben in Kommentaren und müssen trotzdem gefunden werden
        findings, errors = run_on("% TODO-QUELLE: Meyer 1991 fehlt\nText.\n")
        self.assert_cat(findings, "TODO-QUELLE")
        self.assertEqual(errors, 0)  # HINWEIS, kein harter Fehler
        self.assertTrue(any("Meyer 1991 fehlt" in f for f in findings), findings)

    def test_unverified_marker_in_comment(self):
        findings, _ = run_on("% UNVERIFIED: Marktzahl pruefen\nText.\n")
        self.assert_cat(findings, "UNVERIFIED")

    def test_marker_without_detail(self):
        findings, _ = run_on("% TODO-QUELLE\nText.\n")
        self.assert_cat(findings, "TODO-QUELLE")

    def test_no_marker_in_plain_text(self):
        findings, _ = run_on("Der Text erwaehnt kein Marker-Schema.\n")
        self.assert_cat(findings, "TODO-QUELLE", expected=False)
        self.assert_cat(findings, "UNVERIFIED", expected=False)

    def test_quote_env(self):
        findings, errors = run_on("\\begin{quote}Zitat\\end{quote}\n")
        self.assert_cat(findings, "QUOTE-ENV")
        self.assertEqual(errors, 1)

    def test_blockzitat_ok(self):
        findings, errors = run_on("\\begin{blockzitat}Zitat\\end{blockzitat}\n")
        self.assertEqual(errors, 0)

    def test_pronomen_in_blockzitat_ignoriert(self):
        """Wörtlich zitierter Fremdtext ist nicht die Formulierung des Verfassers."""
        findings, errors = run_on(
            "\\begin{blockzitat}\nIch halte das fuer belegt.\n\\end{blockzitat}\n")
        self.assert_cat(findings, "PRONOMEN", expected=False)
        self.assertEqual(errors, 0)

    def test_pronomen_in_enquote_ignoriert(self):
        findings, errors = run_on(
            "Der Befragte sagt \\enquote{ich sehe das anders} dazu.\n")
        self.assert_cat(findings, "PRONOMEN", expected=False)
        self.assertEqual(errors, 0)

    def test_pronomen_neben_enquote_wird_gefunden(self):
        """Die Maskierung darf den eigenen Text der Zeile nicht mitverdecken."""
        findings, errors = run_on(
            "Wir folgern daraus \\enquote{ein stabiles Muster} als Befund.\n")
        self.assert_cat(findings, "PRONOMEN")
        self.assertEqual(errors, 1)

    def test_blockzitat_woerter_zaehlen_weiter(self):
        """Zitattext belegt Seiten – die ½-Seiten-Heuristik muss ihn mitzählen."""
        zitat = " ".join(["Wort"] * 60)
        _, _, meta = run_full(
            "\\subsection{T}\n\\begin{blockzitat}\n" + zitat + "\n\\end{blockzitat}\n")
        self.assertGreaterEqual(meta["word_count"], 60)

    def test_float_mit_h_in_folgezeile(self):
        """[H] darf laut LaTeX in der Folgezeile stehen (dokumentierter FP)."""
        findings, _ = run_on("\\begin{figure}\n[H]\n\\centering\n\\end{figure}\n")
        self.assert_cat(findings, "FLOAT", expected=False)

    def test_float_ohne_platzierung_wird_gefunden(self):
        findings, _ = run_on("\\begin{figure}\n\\centering\n\\end{figure}\n")
        self.assert_cat(findings, "FLOAT")

    def test_float_mit_h_in_derselben_zeile(self):
        findings, _ = run_on("\\begin{figure}[H]\n\\centering\n\\end{figure}\n")
        self.assert_cat(findings, "FLOAT", expected=False)

    def test_htbp_ist_zulaessig(self):
        # Seit 2026-07-30: [H] erzwingt die Position und laesst bei grossen
        # Tabellen eine halbe Seite leer – [htbp] ist dort die richtige Wahl
        # und darf nicht als Formfehler gemeldet werden.
        for opt in ("[htbp]", "[!ht]", "[tbp]"):
            with self.subTest(opt=opt):
                findings, _ = run_on(
                    f"\\begin{{table}}{opt}\n\\centering\n\\end{{table}}\n")
                self.assert_cat(findings, "FLOAT", expected=False)

    def test_unsinnige_option_gilt_nicht_als_platzierung(self):
        findings, _ = run_on("\\begin{figure}[xyz]\n\\centering\n\\end{figure}\n")
        self.assert_cat(findings, "FLOAT")

    def test_autoref_without_tilde(self):
        findings, _ = run_on("Siehe \\autoref{sec:x}.\n")
        self.assert_cat(findings, "AUTOREF")

    def test_autoref_with_tilde_ok(self):
        findings, _ = run_on("vgl.~\\autoref{sec:x}.\n")
        self.assert_cat(findings, "AUTOREF", expected=False)

    def test_straight_quotes(self):
        findings, errors = run_on('Das "Konzept" ist zentral.\n')
        self.assert_cat(findings, "QUOTES")
        self.assertEqual(errors, 1)

    def test_float_without_H(self):
        findings, _ = run_on("\\begin{figure}\n\\end{figure}\n")
        self.assert_cat(findings, "FLOAT")

    def test_float_with_H_ok(self):
        findings, _ = run_on("\\begin{figure}[H]\n\\caption{X}\\label{fig:x}\n\\end{figure}\n")
        self.assert_cat(findings, "FLOAT", expected=False)

    def test_caption_order(self):
        findings, errors = run_on(
            "\\begin{figure}[H]\n\\label{fig:x}\n\\caption{X}\n\\end{figure}\n")
        self.assert_cat(findings, "CAPTION-ORDER")
        self.assertEqual(errors, 1)

    def test_caption_order_ok(self):
        findings, _ = run_on(
            "\\begin{figure}[H]\n\\caption{X}\n\\label{fig:x}\n\\end{figure}\n")
        self.assert_cat(findings, "CAPTION-ORDER", expected=False)

    def test_label_outside_float_ok(self):
        findings, _ = run_on("\\subsection{X}\\label{sec:x}\nText.\n")
        self.assert_cat(findings, "CAPTION-ORDER", expected=False)

    def test_tikz_skipped(self):
        findings, errors = run_on(
            "\\begin{tikzpicture}\n\\node[box] {man wir ich};\n\\end{tikzpicture}\n")
        self.assert_cat(findings, "PRONOMEN", expected=False)
        self.assertEqual(errors, 0)

    def test_include_forbidden(self):
        findings, errors = run_on("\\include{chapters/x}\n")
        self.assert_cat(findings, "INCLUDE")
        self.assertEqual(errors, 1)

    def test_underline(self):
        findings, errors = run_on("\\underline{wichtig}\n")
        self.assert_cat(findings, "UNDERLINE")
        self.assertEqual(errors, 1)

    def test_strip_comment_escaped_percent(self):
        self.assertEqual(strip_comment(r"50\% der Fälle % Kommentar"), r"50\% der Fälle ")


class TestNewChecks(unittest.TestCase):
    """M7-Erweiterung: ½-Seiten-Heuristik, Blockzitat-Heuristik, Überschriften-Dopplung."""

    def assert_cat(self, findings, cat, expected=True):
        hit = any(f"[HINWEIS:{cat}]" in f for f in findings)
        self.assertEqual(hit, expected, f"{cat}: {findings}")

    def test_halbseite_short_subsection(self):
        findings, _, _ = run_full("\\subsection{Kurz}\\label{sec:kurz}\nNur wenige Worte stehen hier.\n")
        self.assert_cat(findings, "HALBSEITE")

    def test_halbseite_long_subsection_ok(self):
        text = "Wort " * 200
        findings, _, _ = run_full(f"\\subsection{{Lang}}\\label{{sec:lang}}\n{text}\n")
        self.assert_cat(findings, "HALBSEITE", expected=False)

    def test_halbseite_master_file_not_flagged(self):
        # Kapitel-Master (\section + \input) hat wenig Text, ist aber keine Subsection-Datei
        findings, _, _ = run_full("\\section{Kapitel}\\label{sec:kap}\n\\input{chapters/x/01_a}\n")
        self.assert_cat(findings, "HALBSEITE", expected=False)

    def test_blockzitat_long_enquote(self):
        quote = " ".join(f"wort{i}" for i in range(45))
        findings, _, _ = run_full(f"Er schreibt \\enquote{{{quote}}} im Text.\n" + "Fülltext. " * 200)
        self.assert_cat(findings, "BLOCKZITAT")

    def test_blockzitat_short_enquote_ok(self):
        findings, _, _ = run_full("Er nennt es \\enquote{ein kurzes Zitat}.\n" + "Fülltext. " * 200)
        self.assert_cat(findings, "BLOCKZITAT", expected=False)

    def test_titel_dopplung_subsection_vs_section(self):
        _, _, m1 = run_full("\\section{Digitale Transformation}\\label{sec:dt}\n" + "Text. " * 200)
        _, _, m2 = run_full("\\subsection{Digitale Transformation}\\label{sec:dt2}\n" + "Text. " * 200)
        findings = check_title_duplication({Path("a.tex"): m1, Path("b.tex"): m2}, None)
        self.assertTrue(any("TITEL-DOPPLUNG" in f for f in findings), findings)

    def test_titel_dopplung_papertitle(self):
        _, _, m = run_full("\\section{Digitale Transformation im Mittelstand}\n" + "Text. " * 200)
        findings = check_title_duplication(
            {Path("a.tex"): m}, "digitale transformation im mittelstand")
        self.assertTrue(any("PaperTitle" in f for f in findings), findings)

    def test_titel_keine_dopplung(self):
        _, _, m1 = run_full("\\section{Theorie}\n" + "Text. " * 200)
        _, _, m2 = run_full("\\subsection{Konzept A}\n" + "Text. " * 200)
        findings = check_title_duplication({Path("a.tex"): m1, Path("b.tex"): m2}, "ganz anderer titel")
        self.assertEqual(findings, [], findings)


class TestReadability(unittest.TestCase):
    """Verständlichkeits-Heuristiken: Satzlänge, Meta-Verben, Nominalstil."""

    def assert_cat(self, findings, cat, expected=True):
        hit = any(f"[HINWEIS:{cat}]" in f for f in findings)
        self.assertEqual(hit, expected, f"{cat}: {findings}")

    def test_satzlaenge_long_sentence(self):
        long_sentence = "Die Arbeit " + "sehr " * 32 + "lang formuliert.\n"
        findings, _ = run_on(long_sentence)
        self.assert_cat(findings, "SATZLAENGE")

    def test_satzlaenge_short_ok(self):
        findings, _ = run_on("Die Arbeit untersucht das Konzept. Sie zeigt drei Befunde. Diese sind kurz.\n")
        self.assert_cat(findings, "SATZLAENGE", expected=False)

    def test_satzlaenge_abbrev_not_split(self):
        # „z. B.“ darf keinen Satzschnitt erzeugen (sonst falsche Kurzsätze)
        text = "Das Konzept hilft z. B. bei der Analyse von Unternehmen und Teams.\n"
        findings, _ = run_on(text)
        self.assert_cat(findings, "SATZLAENGE", expected=False)

    def test_satzschnitt_average(self):
        s = "Wort " * 26
        findings, _ = run_on((s.strip() + ". ") * 6 + "\n")
        self.assert_cat(findings, "SATZSCHNITT")

    def test_meta_verb(self):
        findings, _ = run_on("Kapitel 3 entfaltet daraus das Konzept.\n")
        self.assert_cat(findings, "META-VERB")

    def test_meta_verb_simple_ok(self):
        findings, _ = run_on("Kapitel 3 beschreibt das Konzept.\n")
        self.assert_cat(findings, "META-VERB", expected=False)

    def test_nominalstil(self):
        findings, _ = run_on("Die Auswertung erfolgt in drei Schritten.\n")
        self.assert_cat(findings, "NOMINALSTIL")

    def test_nominalstil_not_in_word(self):
        findings, _ = run_on("Die erfolgreichen Teams arbeiten strukturiert.\n")
        self.assert_cat(findings, "NOMINALSTIL", expected=False)

    def test_citation_not_counted_in_sentence(self):
        # \parencite-Argumente dürfen die Satzlänge nicht aufblähen
        text = ("Die Studie zeigt klare Befunde " + "\\parencite[S. 5]{sehrlangerbibkeyname} " * 10 + ".\n")
        findings, _ = run_on(text)
        self.assert_cat(findings, "SATZLAENGE", expected=False)


class TestTextur(unittest.TestCase):
    """Menschliche-Textur-Heuristiken: TRIAS, RHETFRAGE, ABSATZ-UNIFORM, DOPPELWORT."""

    def assert_cat(self, findings, cat, expected=True):
        hit = any(f"[HINWEIS:{cat}]" in f for f in findings)
        self.assertEqual(hit, expected, f"{cat}: {findings}")

    def test_doppelwort(self):
        findings, errors = run_on("Die Studie zeigt die die Ergebnisse deutlich.\n")
        self.assert_cat(findings, "DOPPELWORT")
        self.assertEqual(errors, 0)  # HINWEIS, kein harter Fehler

    def test_doppelwort_nach_komma_ok(self):
        # Relativpronomen nach Komma ist legitim: „…, die die Plattform nutzen"
        findings, _ = run_on("Die Personen, die die Plattform nutzen, antworten schneller.\n")
        self.assert_cat(findings, "DOPPELWORT", expected=False)

    def test_rhetfrage(self):
        findings, _ = run_on("Doch was bedeutet das für die Praxis? Es zeigt sich ein klares Bild.\n")
        self.assert_cat(findings, "RHETFRAGE")

    def test_rhetfrage_ohne_frage_ok(self):
        findings, _ = run_on("Die Befunde zeigen ein klares Bild. Sie stützen die These deutlich.\n")
        self.assert_cat(findings, "RHETFRAGE", expected=False)

    def test_trias_haeufung(self):
        text = ("Der Ansatz ist schnell, einfach und robust. "
                "Die Methode wirkt klar, direkt und sparsam. "
                "Das Ergebnis bleibt stabil, messbar und belastbar.\n")
        findings, _ = run_on(text)
        self.assert_cat(findings, "TRIAS")

    def test_trias_einzeln_ok(self):
        findings, _ = run_on("Der Ansatz ist schnell, einfach und robust. Die Methode überzeugt.\n")
        self.assert_cat(findings, "TRIAS", expected=False)

    def test_absatz_uniform(self):
        para = "Das Modell zeigt klare Werte. Es trägt die Argumentation sicher.\n\n"
        findings, _ = run_on(para * 6)
        self.assert_cat(findings, "ABSATZ-UNIFORM")

    def test_absatz_variiert_ok(self):
        kurz = "Das Modell zeigt klare Werte. Es trägt die Argumentation sicher.\n\n"
        lang = ("Das Modell zeigt klare Werte. Es trägt die Argumentation sicher. "
                "Die Befunde stammen aus drei Quellen. Jede Quelle wurde einzeln geprüft. "
                "Die Prüfung ergab keine Widersprüche.\n\n")
        findings, _ = run_on(kurz * 3 + lang * 3)
        self.assert_cat(findings, "ABSATZ-UNIFORM", expected=False)


class TestStriche(unittest.TestCase):
    """Geviertstrich = Fehler; Halbgeviertstrich („–“) ist der korrekte
    Gedankenstrich, nur seine Häufung als Satzfüller gibt einen Hinweis."""

    def _has(self, findings, tag):
        return any(tag in f for f in findings)

    def test_geviertstrich_fehler(self):
        findings, errors = run_on("Die Studie zeigt X — ein zentraler Befund.\n")
        self.assertTrue(self._has(findings, "[FEHLER:GEVIERTSTRICH]"), findings)
        self.assertEqual(errors, 1)

    def test_geviertstrich_ohne_spaces_auch_fehler(self):
        # Geviertstrich ist immer verboten, auch ohne umgebende Leerzeichen
        findings, errors = run_on("Wort—Wort steht hier.\n")
        self.assertTrue(self._has(findings, "[FEHLER:GEVIERTSTRICH]"), findings)
        self.assertEqual(errors, 1)

    def test_gedankenstrich_einzeln_ok(self):
        # Halbgeviertstrich mit Leerzeichen ist korrekt; unter der Häufungsschwelle
        findings, errors = run_on("Das Konzept – so die These – trägt.\n")
        self.assertFalse(self._has(findings, "[FEHLER:"), findings)
        self.assertFalse(self._has(findings, "GEDANKENSTRICH"), findings)
        self.assertEqual(errors, 0)

    def test_gedankenstrich_haeufung_hinweis(self):
        # Mehr als drei „ – “ insgesamt: weicher Häufungs-Hinweis, kein Fehler
        findings, errors = run_on("Das – hier – und – dort – überall.\n")
        self.assertTrue(self._has(findings, "[HINWEIS:GEDANKENSTRICH]"), findings)
        self.assertEqual(errors, 0)

    def test_bisstrich_ok(self):
        # „7–10“ ohne umgebende Leerzeichen zählt nicht als Gedankenstrich
        findings, errors = run_on("Der Textteil umfasst 7–10 Seiten.\n")
        self.assertFalse(self._has(findings, "GEDANKENSTRICH"), findings)
        self.assertEqual(errors, 0)

    def test_latex_doppelhyphen_ok(self):
        # LaTeX-Bis-Strich als zwei Hyphen ist kein Unicode-Strich
        findings, errors = run_on("Siehe \\parencites[S. 12--13]{key}.\n")
        self.assertFalse(self._has(findings, "GEVIERTSTRICH"), findings)
        self.assertFalse(self._has(findings, "GEDANKENSTRICH"), findings)
        self.assertEqual(errors, 0)


class TestRunde4Erweiterungen(unittest.TestCase):
    """Titel-Phrasen- und Abkürzungs-Check (externe Prüfung ISSE01, 24.07.2026)."""

    def test_shared_phrase_findet_kernphrase(self):
        from check_formalia import _shared_phrase
        heading = "verschwimmen der grenze in entwicklung und betrieb"
        title = ("safety und security im software engineering unterschiede und das "
                 "verschwimmen der grenze zwischen it und betriebstechnik")
        self.assertEqual(_shared_phrase(heading, title), "verschwimmen der grenze")

    def test_shared_phrase_ignoriert_stoppwortfolgen(self):
        from check_formalia import _shared_phrase
        self.assertIsNone(_shared_phrase("und in der praxis", "theorie und in der folge"))

    def test_titelphrase_wird_gemeldet(self):
        from check_formalia import check_title_duplication
        metas = {Path("x.tex"): {"section_titles": [
            "Verschwimmen der Grenze in Entwicklung und Betrieb"], "subsection_titles": []}}
        title = ("safety und security im software engineering unterschiede und das "
                 "verschwimmen der grenze zwischen it und betriebstechnik")
        findings = check_title_duplication(metas, title)
        self.assertTrue(any("Titel-Phrase" in f for f in findings), findings)

    def test_unerklaerte_abkuerzung_wird_gemeldet(self):
        from check_formalia import check_unexplained_acronyms
        metas = {Path("x.tex"): {"caps_tokens": ["PRISMA"]}}
        findings = check_unexplained_acronyms(metas, {"SIL", "SL"})
        self.assertTrue(any("PRISMA" in f for f in findings), findings)

    def test_bekanntes_akronym_bleibt_still(self):
        from check_formalia import check_unexplained_acronyms
        metas = {Path("x.tex"): {"caps_tokens": ["SIL"]}}
        self.assertEqual(check_unexplained_acronyms(metas, {"SIL"}), [])

    def test_ohne_acronyms_datei_keine_meldung(self):
        from check_formalia import check_unexplained_acronyms
        metas = {Path("x.tex"): {"caps_tokens": ["PRISMA"]}}
        self.assertEqual(check_unexplained_acronyms(metas, None), [])

    def test_caps_sammlung_ueberspringt_normbezeichnung_und_klammer(self):
        findings, errors, meta = run_full(
            "Die IEC 61508 und die Reihe IEC TR 63069 gelten. "
            "Das PRISMA-Schema (Preferred Reporting Items) ist erklärt. "
            "Das SEMA-Rahmenwerk trennt beide Achsen. ")
        self.assertNotIn("IEC", meta["caps_tokens"])
        self.assertNotIn("PRISMA", meta["caps_tokens"])
        self.assertIn("SEMA", meta["caps_tokens"])


class TestStellenangabe(unittest.TestCase):
    """`\\parencite` ohne Seitenangabe – die IU verlangt sie auch bei indirekten
    Zitaten (Zitierleitfaden Anhang C). Der Check ersetzt einen bis dahin rein
    manuellen Prüfpunkt, deshalb muss vor allem die Abgrenzung sitzen."""

    def cats(self, text):
        findings, _errors, _m = run_full(text)
        return [f for f in findings if "SEITENANGABE" in f]

    def test_ohne_seitenangabe_gemeldet(self):
        self.assertEqual(len(self.cats("Aussage \\parencite{keyA}.\n")), 1)

    def test_mit_seitenangabe_still(self):
        self.assertEqual(self.cats("Aussage \\parencite[S. 5]{keyA}.\n"), [])

    def test_kapitel_und_absatz_zaehlen_als_stellenangabe(self):
        # Quellen ohne Seitenzahlen werden per Kap./Abs./Zeitstempel belegt.
        self.assertEqual(self.cats("Aussage \\parencite[Kap. 2.1]{keyA}.\n"), [])
        self.assertEqual(self.cats("Aussage \\parencite[Abs. 4]{keyA}.\n"), [])

    def test_geschuetztes_leerzeichen_in_jedem_locator(self):
        # Regression: „S.~47" galt, „Kap.~2.1" nicht – dieselbe Typografie-Regel,
        # zwei verschiedene Urteile. Mit E-Book-Quellen wird der Kapitel-Locator
        # zum Regelfall, damit wäre daraus ein täglicher Fehlalarm geworden.
        for locator in ("S.~47", "Kap.~2.1", "Kap.~17.2.2", "Abs.~4", "Rn.~12"):
            with self.subTest(locator=locator):
                self.assertEqual(
                    self.cats(f"Aussage \\parencite[{locator}]{{keyA}}.\n"), [])

    def test_prenote_ohne_stelle_reicht_nicht(self):
        # `[vgl.]` ist ein Präfix, keine Fundstelle.
        self.assertEqual(len(self.cats("Aussage \\parencite[vgl.]{keyA}.\n")), 1)

    def test_parencites_je_block_einzeln(self):
        # Erstes Werk mit Seite, zweites ohne -> genau ein Fund, und zwar für keyB.
        funde = self.cats("Aussage \\parencites[S. 5]{keyA}{keyB}.\n")
        self.assertEqual(len(funde), 1)
        self.assertIn("keyB", funde[0])

    def test_textcite_ebenfalls(self):
        self.assertEqual(len(self.cats("\\textcite{keyA} zeigt das.\n")), 1)


class TestQuelleUndCite(unittest.TestCase):
    def test_float_ohne_quelle(self):
        findings, errors, _m = run_full(
            "\\begin{figure}[H]\n\\caption{X}\\label{fig:x}\n"
            "\\includegraphics{a.png}\n\\end{figure}\n")
        self.assertTrue(any("QUELLE-FEHLT" in f for f in findings), findings)
        self.assertEqual(errors, 1)

    def test_float_mit_quelle_still(self):
        findings, errors, _m = run_full(
            "\\begin{figure}[H]\n\\caption{X}\\label{fig:x}\n"
            "\\includegraphics{a.png}\n\\quelle{Eigene Darstellung.}\n\\end{figure}\n")
        self.assertFalse(any("QUELLE-FEHLT" in f for f in findings), findings)

    def test_float_ohne_inhalt_kein_fund(self):
        # Ein Float ohne Bild/Tabelle (z. B. nur Text) braucht keine Quellenzeile.
        findings, _e, _m = run_full(
            "\\begin{figure}[H]\n\\caption{X}\\label{fig:x}\nNur Text.\n\\end{figure}\n")
        self.assertFalse(any("QUELLE-FEHLT" in f for f in findings), findings)

    def test_cite_in_quellenzeile_erlaubt(self):
        findings, _e, _m = run_full(
            "\\quelle{Eigene Darstellung in Anlehnung an \\cite{keyA}.}\n")
        self.assertFalse(any("[HINWEIS:CITE]" in f for f in findings), findings)

    def test_cite_im_sekundaerzitat_erlaubt(self):
        findings, _e, _m = run_full(
            "Aussage (Original, 2017, zitiert nach \\cite[S. 5]{keyA}).\n")
        self.assertFalse(any("[HINWEIS:CITE]" in f for f in findings), findings)

    def test_cite_sonst_gemeldet(self):
        findings, _e, _m = run_full("Eine Aussage \\cite{keyA} im Text.\n")
        self.assertTrue(any("[HINWEIS:CITE]" in f for f in findings), findings)


class TestStrukturUndAktivierung(unittest.TestCase):
    """Dateiübergreifende Checks: Unterpunkte, Aktivierungsblöcke, Anhang-Verweise."""

    def projekt(self, root: Path, *, listoffigures_aktiv=False,
                appendix_aktiv=False, anhaenge=("A",), figuren=0):
        (root / "pages").mkdir(parents=True, exist_ok=True)
        (root / "chapters" / "02_theorie").mkdir(parents=True, exist_ok=True)
        def block(aktiv, zeile):
            return zeile if aktiv else "%" + zeile
        (root / "main.tex").write_text("\n".join([
            "\\documentclass{article}",
            block(listoffigures_aktiv, "\\listoffigures"),
            "%\\listoftables",
            "\\begin{document}",
            block(appendix_aktiv, "\\include{pages/appendix}"),
            "\\end{document}", ""]), encoding="utf-8")
        # Vorlagenform: \newappendix{} je Anhang, Buchstabe aus der Reihenfolge.
        (root / "pages" / "appendix.tex").write_text(
            "\\listofappendices\n"
            + "".join(f"\\newappendix{{Titel {b}}}\n" for b in anhaenge)
            + "Fuellinhalt, damit der Anhang als nicht leer gilt und der Block zaehlt.\n",
            encoding="utf-8")
        floats = "".join(
            f"\\begin{{figure}}[H]\n\\caption{{Abb {i}}}\\label{{fig:{i}}}\n"
            f"\\includegraphics{{a{i}.png}}\n\\quelle{{Eigene Darstellung.}}\n\\end{{figure}}\n"
            for i in range(figuren))
        (root / "chapters" / "02_theorie" / "01_a.tex").write_text(
            "\\subsection{Begriffe}\\label{sec:begriffe}\nText dazu.\n" + floats,
            encoding="utf-8")

    def metas(self, root: Path):
        out = {}
        for tex in sorted(root.rglob("*.tex")):
            if tex.name in ("main.tex",):
                continue
            _f, _e, meta = check_file(tex)
            out[tex] = meta
        return out

    def test_eine_subsection_ist_fehler(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root)
            funde = check_unterpunkte(self.metas(root))
            self.assertTrue(any("UNTERPUNKTE" in f for f in funde), funde)

    def test_zwei_subsections_still(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root)
            (root / "chapters" / "02_theorie" / "02_b.tex").write_text(
                "\\subsection{Modelle}\\label{sec:modelle}\nText.\n", encoding="utf-8")
            self.assertEqual(check_unterpunkte(self.metas(root)), [])

    def test_drei_abbildungen_ohne_verzeichnis(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, figuren=3, appendix_aktiv=True)
            funde = check_aktivierung(self.metas(root), root)
            self.assertTrue(any("Abbildungsverzeichnis" in f for f in funde), funde)

    def test_drei_abbildungen_mit_verzeichnis_still(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, figuren=3, listoffigures_aktiv=True, appendix_aktiv=True)
            funde = check_aktivierung(self.metas(root), root)
            self.assertFalse(any("Abbildungsverzeichnis" in f for f in funde), funde)

    def test_anhangsverzeichnis_ist_keine_skriptsache_mehr(self):
        # Die Schwelle „ab zwei Anhängen" steckt seit der Umstellung in
        # \listofappendices. Zwei Anhänge, kein Verzeichnis-Block in main.tex –
        # das Skript darf dazu nichts mehr sagen, sonst prüfte es eine Regel,
        # die an anderer Stelle bereits entschieden wird.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, anhaenge=("A", "B"), appendix_aktiv=True)
            funde = check_aktivierung(self.metas(root), root)
            self.assertFalse(any("Anhangsverzeichnis" in f for f in funde), funde)

    def test_anhang_inhalt_ohne_aktivierung(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, appendix_aktiv=False)
            funde = check_aktivierung(self.metas(root), root)
            self.assertTrue(any("Block „Anhang“" in f for f in funde), funde)

    def test_anhang_ohne_textverweis(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, anhaenge=("A", "B"))
            funde = check_anhang_verweise(self.metas(root), root)
            self.assertEqual(len(funde), 2, funde)   # weder A noch B referenziert

    def test_anhang_mit_textverweis_still(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, anhaenge=("A",))
            (root / "chapters" / "02_theorie" / "01_a.tex").write_text(
                "\\subsection{Begriffe}\\label{sec:x}\nDer Leitfaden liegt bei (siehe Anhang A).\n",
                encoding="utf-8")
            self.assertEqual(check_anhang_verweise(self.metas(root), root), [])

    def test_einzelner_anhang_ist_kein_unterpunkte_fehler(self):
        # Regression: `\subsection*{Anhang A}` in pages/ ist kein Gliederungspunkt.
        # Vor dem Fix meldete jede Arbeit mit genau einem Anhang einen Fehlalarm.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, anhaenge=("A",))
            (root / "chapters" / "02_theorie" / "02_b.tex").write_text(
                "\\subsection{Modelle}\\label{sec:modelle}\nText.\n", encoding="utf-8")
            funde = check_unterpunkte(self.metas(root))
            self.assertEqual(funde, [], funde)

    def test_main_tex_wird_beim_ordnerlauf_uebersprungen(self):
        # Regression: main.tex ist das Wurzeldokument, keine Kapiteldatei. Die
        # \include-Regel gilt Kapiteln; auf main.tex angewandt meldete sie sechs
        # Fehler auf der unveränderten Vorlage – und einen siebten, sobald
        # jemand den Anhang einschaltet.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, appendix_aktiv=True)
            ausgabe = self.lauf_ueber(root)
            self.assertNotIn("INCLUDE", ausgabe, ausgabe)
            # Gezielt genannt wird main.tex weiterhin geprüft.
            self.assertIn("INCLUDE", self.lauf_ueber(root / "main.tex"))

    def lauf_ueber(self, ziel: Path) -> str:
        import io
        import contextlib
        import check_formalia
        puffer = io.StringIO()
        alt = sys.argv
        sys.argv = ["check_formalia.py", str(ziel)]
        try:
            with contextlib.redirect_stdout(puffer):
                check_formalia.main()
        finally:
            sys.argv = alt
        return puffer.getvalue()

    # --- ABKUERZUNG-UNGENUTZT: Einträge, die im Text nicht vorkommen ---

    def acro_projekt(self, root: Path, verzeichnis: str, text: str):
        (root / "pages").mkdir(parents=True, exist_ok=True)
        (root / "pages" / "acronyms.tex").write_text(verzeichnis, encoding="utf-8")
        (root / "chapters" / "01_kap").mkdir(parents=True, exist_ok=True)
        (root / "chapters" / "01_kap" / "a.tex").write_text(text, encoding="utf-8")
        out = {}
        for tex in sorted(root.rglob("*.tex")):
            _f, _e, meta = check_file(tex)
            out[tex] = meta
        return out

    def test_ungenutzter_eintrag_ist_fehler(self):
        # Das acronym-Paket druckt jeden Eintrag – ein verwaister landet im
        # abgegebenen Verzeichnis, ohne dass die Abkürzung im Text vorkommt.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.acro_projekt(
                root,
                "\\begin{acronym}[DSGVO]\n\\acro{KI}{Kuenstliche Intelligenz}\n"
                "\\acro{DSGVO}{Datenschutz-Grundverordnung}\n\\end{acronym}\n",
                "Die \\ac{KI} kommt vor, die andere nicht.\n")
            funde = check_ungenutzte_acronyms(metas, {"KI", "DSGVO"})
            self.assertEqual(len(funde), 1, funde)
            self.assertIn("ABKUERZUNG-UNGENUTZT", funde[0])
            self.assertIn("DSGVO", funde[0])
            self.assertNotIn(" KI ", funde[0])

    def test_alle_genutzt_bleibt_still(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.acro_projekt(
                root, "\\begin{acronym}[KI]\n\\acro{KI}{Kuenstliche Intelligenz}\n"
                      "\\end{acronym}\n",
                "Die \\ac{KI} kommt vor.\n")
            self.assertEqual(check_ungenutzte_acronyms(metas, {"KI"}), [])

    def test_verwendung_im_kommentar_zaehlt_nicht(self):
        # acronyms.tex erklaert die Verwendung selbst im Kommentar.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.acro_projekt(
                root, "% Verwendung: \\ac{KI}\n\\begin{acronym}[KI]\n"
                      "\\acro{KI}{Kuenstliche Intelligenz}\n\\end{acronym}\n",
                "Hier steht kein Akronym.\n")
            funde = check_ungenutzte_acronyms(metas, {"KI"})
            self.assertEqual(len(funde), 1, funde)

    def test_varianten_von_ac_zaehlen(self):
        # \acs, \acl, \acf, \acp sind ebenfalls Verwendungen.
        for befehl in ("\\acs{KI}", "\\acl{KI}", "\\acf{KI}", "\\acp{KI}"):
            with self.subTest(befehl=befehl):
                with tempfile.TemporaryDirectory() as d:
                    root = Path(d)
                    metas = self.acro_projekt(
                        root, "\\begin{acronym}[KI]\n\\acro{KI}{KI}\n\\end{acronym}\n",
                        f"Hier: {befehl} im Satz.\n")
                    self.assertEqual(check_ungenutzte_acronyms(metas, {"KI"}), [])

    def test_todo_eintrag_gilt_nicht_als_verwaist(self):
        # Der Platzhalter der Vorlage soll ersetzt werden – kein Verwaister.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "pages").mkdir(parents=True)
            (root / "pages" / "acronyms.tex").write_text(
                "\\begin{acronym}[MUSTER]\n"
                "    \\acro{MUSTER}{Platzhalter} % TODO\n"
                "    \\acro{DSGVO}{Datenschutz-Grundverordnung}\n"
                "\\end{acronym}\n", encoding="utf-8")
            self.assertEqual(find_acronyms(root, ohne_todo=True), {"DSGVO"})
            # Fuer die Gegenrichtung bleibt der Platzhalter bekannt.
            self.assertEqual(find_acronyms(root), {"MUSTER", "DSGVO"})

    # --- Anhänge zählen: \newappendix{} plus handgeschriebene Altform ---

    def appendix_datei(self, root: Path, inhalt: str):
        (root / "pages").mkdir(parents=True, exist_ok=True)
        (root / "pages" / "appendix.tex").write_text(inhalt, encoding="utf-8")

    def test_newappendix_bestimmt_buchstaben_ueber_die_reihenfolge(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.appendix_datei(root,
                                "\\listofappendices\n"
                                "\\newappendix{Interviewleitfaden}\nInhalt.\n"
                                "\\newappendix{Kategoriensystem}\nInhalt.\n"
                                "\\newappendix{Transkripte}\nInhalt.\n")
            self.assertEqual(anhang_buchstaben(root), {"A", "B", "C"})

    def test_auskommentiertes_newappendix_zaehlt_nicht(self):
        # Die Vorlage liefert die Beispielstruktur auskommentiert mit – sonst
        # hätte jedes frische Projekt zwei Anhänge, die es nicht gibt.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.appendix_datei(root,
                                "\\listofappendices\n"
                                "% \\newappendix{Interviewleitfaden}\n"
                                "% \\newappendix{Kategoriensystem}\n")
            self.assertEqual(anhang_buchstaben(root), set())

    def test_handgeschriebene_altform_wird_weiter_erkannt(self):
        # Regression zugleich: „Anhang~A" mit geschütztem Leerzeichen. Vor dem
        # Fix fand der Regex in einer vorlagenkonformen Arbeit null Anhänge.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.appendix_datei(root,
                                "\\section*{Anhang~A: Suchprotokoll}\nInhalt.\n"
                                "\\section*{Anhang B: Zweite Form}\nInhalt.\n")
            self.assertEqual(anhang_buchstaben(root), {"A", "B"})

    def test_gemischte_formen_ergeben_keine_luecke(self):
        # Ein Projekt mitten in der Umstellung: ein Makro, eine Handüberschrift.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.appendix_datei(root,
                                "\\newappendix{Interviewleitfaden}\nInhalt.\n"
                                "\\section*{Anhang~B: Altbestand}\nInhalt.\n")
            self.assertEqual(anhang_buchstaben(root), {"A", "B"})

    # --- DOPPELBELEGUNG: ein Wort, zwei Artefakte ---

    def float_datei(self, *captions_labels):
        text = "".join(
            f"\\begin{{figure}}[H]\n\\caption{{{cap}}}\n\\label{{{lab}}}\n"
            f"\\includegraphics{{x.png}}\n\\quelle{{Eigene Darstellung.}}\n\\end{{figure}}\n"
            for cap, lab in captions_labels)
        return text

    def test_caption_text_endet_an_der_eigenen_klammer(self):
        # Regression: Die erste Fassung las bis zur letzten „}" der Zeile und
        # schleppte „\label{fig:x}" in den Caption-Text. Direkt an der Funktion
        # geprüft – über check_caption_doppelbelegung wäre der Fehler unsichtbar
        # geblieben, weil das Extrahieren der Substantive ihn zufällig überdeckt.
        self.assertEqual(
            caption_text("\\caption{Persona-Skizze}\\label{fig:persona}"),
            "Persona-Skizze")
        self.assertEqual(
            caption_text("\\caption{Einsatz von \\ac{KI} im Prozess}"),
            "Einsatz von \\ac{KI} im Prozess")
        self.assertEqual(
            caption_text("\\caption[Kurzform]{Langform der Beschriftung}"),
            "Langform der Beschriftung")
        self.assertEqual(caption_text("\\includegraphics{bild.png}"), "")

    def doppel(self, floats: str, fliesstext: str):
        _f, _e, meta = run_full(floats + fliesstext)
        return check_caption_doppelbelegung({Path("a.tex"): meta})

    def test_doppelbelegung_mit_verkuerztem_rueckverweis(self):
        # Der Realfall: „Persona-Skizze" und „Mockup-Skizze", im Text „die Skizze".
        funde = self.doppel(
            self.float_datei(("Persona-Skizze der Zielgruppe", "fig:persona"),
                             ("Mockup-Skizze des Formulars", "fig:mockup")),
            "Wie die Skizze zeigt, bleibt der Ablauf zweistufig.\n")
        self.assertEqual(len(funde), 1, funde)
        self.assertIn("DOPPELBELEGUNG", funde[0])
        self.assertIn("Skizze", funde[0])

    def test_doppelbelegung_ohne_verkuerzung_still(self):
        # Beide Captions teilen das Wort, der Text bleibt aber eindeutig.
        funde = self.doppel(
            self.float_datei(("Persona-Skizze der Zielgruppe", "fig:persona"),
                             ("Mockup-Skizze des Formulars", "fig:mockup")),
            "Wie die Persona-Skizze zeigt, bleibt der Ablauf zweistufig.\n")
        self.assertEqual(funde, [], funde)

    def test_ein_label_ist_keine_doppelbelegung(self):
        funde = self.doppel(
            self.float_datei(("Persona-Skizze der Zielgruppe", "fig:persona")),
            "Wie die Skizze zeigt, bleibt der Ablauf zweistufig.\n")
        self.assertEqual(funde, [], funde)

    def test_beschreibende_caption_koepfe_still(self):
        # „Übersicht" in zwei Captions ist normal, kein Namenskonflikt.
        funde = self.doppel(
            self.float_datei(("Übersicht der Phasen", "fig:phasen"),
                             ("Übersicht der Rollen", "fig:rollen")),
            "Die Übersicht fasst den Stand zusammen.\n")
        self.assertEqual(funde, [], funde)

    # --- ZAHLWORT: Zählaussagen als Erinnerungsliste ---

    def test_zahlwort_wird_gelistet(self):
        _f, _e, meta = run_full("Daraus folgen drei Konsequenzen fuer die Praxis.\n")
        funde = check_zahlwoerter({Path("a.tex"): meta})
        self.assertEqual(len(funde), 1, funde)
        self.assertIn("ZAHLWORT", funde[0])
        self.assertIn("drei Konsequenzen", funde[0])

    def test_unbestimmter_artikel_loest_nicht_aus(self):
        # Bewusste Auslassung: „ein/eine" waere in jedem deutschen Satz Treffer.
        _f, _e, meta = run_full("Das ist eine Konsequenz, die ein Modell abbildet.\n")
        self.assertEqual(check_zahlwoerter({Path("a.tex"): meta}), [])

    def test_zahlwort_ohne_nomen_loest_nicht_aus(self):
        _f, _e, meta = run_full("Die Werte lagen bei drei komma fuenf im Mittel.\n")
        self.assertEqual(check_zahlwoerter({Path("a.tex"): meta}), [])

    def test_zahlwort_liste_wird_gedeckelt(self):
        text = "".join(f"Es gibt drei Faktor{i} in dieser Sache.\n" for i in range(20))
        _f, _e, meta = run_full(text)
        funde = check_zahlwoerter({Path("a.tex"): meta})
        self.assertIn("+8", funde[0])
        self.assertLess(funde[0].count("„"), 20)

    def test_bruchteile_und_zeitspannen_still(self):
        # Realtest an einer fertigen Seminararbeit: die einzigen Fehltreffer.
        _f, _e, meta = run_full(
            "Etwa drei Viertel der Befragten nannten dies; zwei Drittel der Faelle "
            "traten binnen drei Jahren auf, gemessen ueber zehn Jahren.\n")
        self.assertEqual(check_zahlwoerter({Path("a.tex"): meta}), [])

    def test_zahlwoerter_aus_mehreren_dateien_in_einem_block(self):
        _f, _e, m1 = run_full("Daraus folgen drei Konsequenzen fuer die Praxis.\n")
        _f, _e, m2 = run_full("Es bleiben zwei Einwaende gegen dieses Vorgehen.\n")
        funde = check_zahlwoerter({Path("a.tex"): m1, Path("b.tex"): m2})
        self.assertEqual(len(funde), 1, funde)          # ein Block, nicht zwei Befunde
        self.assertEqual(funde[0].count("ZAHLWORT"), 1)
        self.assertIn("drei Konsequenzen", funde[0])
        self.assertIn("zwei Einwaende", funde[0])

    def gruppen_projekt(self, root: Path, autorenschaft_zeile: str | None, text: str):
        (root / "chapters" / "02_umsetzung").mkdir(parents=True, exist_ok=True)
        if autorenschaft_zeile is not None:
            (root / "aufgabe.md").write_text(
                "# Aufgabenstellung\n\n" + autorenschaft_zeile + "\n", encoding="utf-8")
        (root / "chapters" / "02_umsetzung" / "01_a.tex").write_text(text, encoding="utf-8")
        return self.metas(root)

    def test_gruppenbezug_bei_einzelarbeit(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.gruppen_projekt(
                root, "**Autorenschaft**: Einzelarbeit",
                "\\subsection{U}\\label{sec:u}\nDie Projektgruppe waehlte ein iteratives Vorgehen.\n")
            funde = check_gruppenbezug(metas, root)
            self.assertEqual(len(funde), 1, funde)
            self.assertIn("GRUPPENBEZUG", funde[0])

    def test_gruppenbezug_bei_gruppenarbeit_still(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.gruppen_projekt(
                root, "**Autorenschaft**: Gruppenarbeit",
                "\\subsection{U}\\label{sec:u}\nDie Projektgruppe waehlte ein iteratives Vorgehen.\n")
            self.assertEqual(check_gruppenbezug(metas, root), [])

    def test_gruppenbezug_ohne_aufgabe_md_still(self):
        # Ohne Angabe wird nicht geraten – in der Bachelor-Vorlage gibt es die Datei gar nicht.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.gruppen_projekt(
                root, None,
                "\\subsection{U}\\label{sec:u}\nDie Projektgruppe waehlte ein Vorgehen.\n")
            self.assertEqual(check_gruppenbezug(metas, root), [])

    def test_gruppenbezug_ignoriert_kommentar(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.gruppen_projekt(
                root, "**Autorenschaft**: Einzelarbeit",
                "\\subsection{U}\\label{sec:u}\n% Die Projektgruppe stand hier mal.\nText.\n")
            self.assertEqual(check_gruppenbezug(metas, root), [])

    def test_gruppenbezug_keine_fehlalarme_auf_zielgruppe(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            metas = self.gruppen_projekt(
                root, "**Autorenschaft**: Einzelarbeit",
                "\\subsection{U}\\label{sec:u}\nDie Zielgruppe umfasst Studierende; "
                "das Team des Anbieters pflegt die Plattform.\n")
            self.assertEqual(check_gruppenbezug(metas, root), [])

    def test_autorenschaft_liest_verschiedene_schreibweisen(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "aufgabe.md").write_text("Autorenschaft: Einzelarbeit\n", encoding="utf-8")
            self.assertEqual(autorenschaft(root), "einzelarbeit")

    def test_meta_platzhalter_gefunden(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "pages").mkdir(parents=True)
            (root / "pages" / "meta.tex").write_text(
                "\\newcommand{\\PaperTitle}{THESISTITEL}\n"
                "\\newcommand{\\PaperType}{Bachelorarbeit}\n"
                "\\newcommand{\\AuthorName}{Max Mustermann}\n", encoding="utf-8")
            funde = check_meta_platzhalter(root)
            self.assertEqual(len(funde), 1, funde)
            self.assertIn("PaperTitle", funde[0])
            # Ausgefüllte Felder dürfen nicht mitgemeldet werden.
            self.assertNotIn("PaperType", funde[0])
            self.assertNotIn("AuthorName", funde[0])

    def test_meta_ohne_platzhalter_still(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "pages").mkdir(parents=True)
            (root / "pages" / "meta.tex").write_text(
                "\\newcommand{\\PaperTitle}{Ein echter Titel}\n", encoding="utf-8")
            self.assertEqual(check_meta_platzhalter(root), [])

    def test_anhang_buchstaben_ignoriert_fliesstext(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.projekt(root, anhaenge=("A", "B"))
            self.assertEqual(anhang_buchstaben(root), {"A", "B"})


if __name__ == "__main__":
    unittest.main()
