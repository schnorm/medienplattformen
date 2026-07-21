#!/usr/bin/env python3
"""Tests für check_formalia.py — python3 -m unittest test_check_formalia.py"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_formalia import (  # noqa: E402
    check_file, check_title_duplication, strip_comment)


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

    def test_quote_env(self):
        findings, errors = run_on("\\begin{quote}Zitat\\end{quote}\n")
        self.assert_cat(findings, "QUOTE-ENV")
        self.assertEqual(errors, 1)

    def test_blockzitat_ok(self):
        findings, errors = run_on("\\begin{blockzitat}Zitat\\end{blockzitat}\n")
        self.assertEqual(errors, 0)

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


if __name__ == "__main__":
    unittest.main()
