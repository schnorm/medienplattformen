#!/usr/bin/env python3
r"""
check_formalia.py – deterministische Formalia-Checks auf .tex-Dateien.

Ersetzt tokenintensives LLM-Durchlesen für alle mechanisch prüfbaren Regeln
aus hard-rules-formal.md. Inhaltliche Checks (Argumentation, Synthese, Stil)
bleiben beim Prüf-Modus – dieses Skript findet nur, was ein Regex sicher
finden kann.

Nutzung (vom Projekt-Root):
    python3 .claude/skills/_shared/scripts/check_formalia.py chapters/
    python3 .claude/skills/_shared/scripts/check_formalia.py chapters/01_einleitung/01_motivation.tex

Ausgabeformat: <datei>:<zeile>: [KATEGORIE] Meldung
Exit-Code: 1 wenn mindestens ein FEHLER (harter Verstoß), sonst 0.
HINWEIS-Funde beeinflussen den Exit-Code nicht.

Zusätzlich beim Verzeichnis-Lauf (nicht bei einer Einzeldatei, weil sie nur
über den Gesamtbestand entscheidbar sind):
  * Stellenangabe bei jeder Zitation (IU-Abweichung von APA)
  * \quelle{} unter jedem Float mit Bild/Diagramm/Tabelle
  * mindestens zwei Unterpunkte je Teilung
  * Abbildungs-/Tabellenverzeichnis und Anhang gegen die Aktivierungsblöcke
    in main.tex (Bestandteil geschrieben, aber nicht im PDF)
  * mindestens ein Textverweis je Anhang

Grenzen: Kommentare werden entfernt; Inhalte von lstlisting/verbatim werden
übersprungen. Wortgrenzen sind heuristisch – Funde immer im Kontext prüfen.
"""

import argparse
import re
import sys
from pathlib import Path

# Windows-Konsole (cp1252) kann Sonderzeichen wie „→“ in den Meldungen nicht
# kodieren und bräche beim Ausdruck ab – Ausgabe deshalb auf UTF-8 umstellen.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

# (Kategorie, Schwere, Regex, Meldung)
# Schwere: "FEHLER" = harter Verstoß laut hard-rules-formal.md, "HINWEIS" = prüfen.
LINE_CHECKS = [
    ("PRONOMEN", "FEHLER",
     re.compile(r"(?<![\\\w])(ich|wir|man)(?![\w])", re.IGNORECASE),
     "Verbotenes Pronomen (ich/wir/man) – umformulieren („Diese Arbeit …“)."),
    ("QUOTE-ENV", "FEHLER",
     re.compile(r"\\begin\{quote\}"),
     "\\begin{quote} statt \\begin{blockzitat} (IU: 1,27 cm links, ohne Anführungszeichen)."),
    ("INCLUDE", "FEHLER",
     re.compile(r"\\include\{"),
     "\\include{} in Kapiteldateien verboten – \\input{} verwenden."),
    ("AUTOREF", "HINWEIS",
     re.compile(r"(?<!~)\\autoref\{"),
     "\\autoref ohne führendes ~ (z. B. vgl.~\\autoref{...})."),
    ("REF", "HINWEIS",
     re.compile(r"\\ref\{"),
     "\\ref{} statt \\autoref{} – \\autoref erzeugt „Kapitel N“ automatisch."),
    ("QUOTES", "FEHLER",
     re.compile(r"[\"„“”]"),
     "Gerade/typografische Anführungszeichen im Quelltext – \\enquote{} verwenden."),
    ("UNDERLINE", "FEHLER",
     re.compile(r"\\underline\{"),
     "Unterstreichungen sind laut IU-Richtlinien nicht zulässig."),
    # Verständlichkeits-Heuristiken (hard-rules-formal.md → Verständlichkeit, stilprofil.md)
    ("META-VERB", "HINWEIS",
     re.compile(r"(?<![\\\w])(entfaltet|entfalten|bündelt|bündeln|verortet|verorten|adressiert|adressieren|konstatiert|konstatieren)(?![\w])", re.IGNORECASE),
     "Gestelztes Meta-Verb – einfaches Verb wählen (beschreibt/zeigt/fasst zusammen), siehe stilprofil.md."),
    ("NOMINALSTIL", "HINWEIS",
     re.compile(r"(?<![\\\w])(erfolgt|erfolgen|im Rahmen (der|des|dieser|dieses)|vor dem Hintergrund|unter Berücksichtigung)(?![\w])", re.IGNORECASE),
     "Nominalstil-Marker – aktive Verb-Formulierung prüfen („Die Arbeit untersucht X“ statt „Die Untersuchung erfolgt“)."),
]

SKIP_ENVS = ("lstlisting", "verbatim", "tikzpicture")

# `\cite{}` ist NICHT generell falsch: In der Quellenzeile einer Abbildung und im
# Sekundärzitat ist es die einzig richtige Form, weil dort kein Klammerpaar
# erzeugt werden darf (Zitierleitfaden 2.2.5 bzw. „zitiert nach"). Gemeldet wird
# es deshalb nur außerhalb dieser beiden Kontexte.
CITE_PLAIN_RE = re.compile(r"\\cite\{")
CITE_OK_KONTEXT_RE = re.compile(r"\\quelle\{|zitiert nach", re.IGNORECASE)

# Stellenangabe auch bei INDIREKTEN Zitaten ist die auffälligste IU-Abweichung
# von APA (Zitierleitfaden Anhang C: „Erforderlich" statt „Nicht erforderlich").
# Bis hierher war das der einzige rein manuelle Prüfpunkt in Teil-Check A.
CITE_ARGS_RE = re.compile(
    r"\\([Pp]arencites?|[Tt]extcites?|[Ff]ootcites?|[Aa]utocites?)\b"
    r"((?:\[[^\]]*\]|\{[^}]*\})*)")
ARG_TOKEN_RE = re.compile(r"\[([^\]]*)\]|\{([^}]*)\}")
# Was als Stellenangabe zählt – Seite, Kapitel, Absatz, Abschnitt, Zeitstempel
# (Zitierleitfaden 2.2.1, „Alternativen zur Seitenangabe").
# Das geschuetzte Leerzeichen gilt fuer ALLE Kuerzel gleich: Vorher liess nur
# „S.~47" es zu, „Kap.~2.1" dagegen nicht - obwohl beide Formen derselben
# Typografie-Regel folgen. Aufgefallen, als E-Book-Quellen den Kapitel-Locator
# zum Regelfall machten (check_quellentreue.py wertet [Kap. X] jetzt aus).
LOCATOR_RE = re.compile(
    r"(?:S|Kap|Abs|Rn)\.\s*~?\s*\d|Abschnitt|\d+:\d{2}|\bf{1,2}\.")

# Float ohne Quellenzeile: `\quelle{}` ist bei EIGENEN wie fremden Abbildungen
# Pflicht (IU: „Quelle: " unter jeder Abbildung/Tabelle, 10 Pt.).
FLOAT_INHALT_RE = re.compile(r"\\includegraphics|\\begin\{tikzpicture\}|\\begin\{tabular")

# Struktur: „Sobald ein Kapitel in Unterkapitel geteilt wird, müssen es
# mindestens zwei sein" (IU-Richtlinien 3.2). Genau ein Unterpunkt ist ein
# Verstoß, null ist erlaubt (dann wird eben nicht unterteilt).
# Nur NICHT-gesternte Überschriften zählen als Gliederungspunkte: `\subsection*`
# erscheint weder nummeriert noch im Inhaltsverzeichnis (Anhänge, Abstract,
# Verzeichnisse) und ist damit kein Unterpunkt im Sinne der Richtlinien.
SUBSECTION_NUM_RE = re.compile(r"\\subsection\{")
SUBSUBSECTION_RE = re.compile(r"\\subsubsection\{")

# Aktivierungsblöcke in main.tex – der in `handbuch.md` meistgenannte
# Bedienfehler: Bestandteil geschrieben, Block nie eingeschaltet.
LISTOF_RE = {"figures": re.compile(r"(?m)^(\s*%*\s*)\\listoffigures"),
             "tables": re.compile(r"(?m)^(\s*%*\s*)\\listoftables")}
APPENDIX_RE = re.compile(r"(?m)^(\s*%*\s*)\\include\{pages/appendix\}")
NEWAPPENDIX_RE = re.compile(r"\\newappendix\{")
# Textverweise („siehe Anhang B") und handgeschriebene Ueberschriften. Das „~"
# mitzuzaehlen ist keine Kulanz, sondern Pflicht: Wer die Ueberschrift von Hand
# setzt, schreibt sie wie die alte Vorlage mit geschuetztem Leerzeichen. Mit
# \s+ allein fand der Regex in einer vorlagenkonformen Arbeit NULL Anhaenge -
# und damit lief die Textverweis-Pflicht still ins Leere. Aufgefallen erst beim
# Lauf gegen eine fertige Seminararbeit, nicht in den Tests: Die hatten
# dieselbe falsche Annahme wie der Regex.
ANHANG_TITEL_RE = re.compile(r"Anhang[\s~]+([A-Z])\b")
MIN_VERZEICHNIS = 3   # Abbildungs-/Tabellenverzeichnis erst ab drei Stück
# Kein MIN_ANHANGSVERZEICHNIS mehr: Die Schwelle („Bei mehreren Anhängen ist ein
# Anhangsverzeichnis erforderlich", IU-Richtlinien 3.2) steckt seit der
# Umstellung in \listofappendices und wird beim Setzen entschieden. Ein Skript,
# das dieselbe Regel ein zweites Mal prueft, kann nur noch abweichen.

# Stilregeln gelten dem eigenen Text, nicht woertlich zitiertem Fremdtext: In einem
# Zitat sind „ich“ oder ein Nominalstil-Marker die Formulierung der Quelle, nicht die
# des Verfassers. Bisher meldete das Skript sie trotzdem – dokumentiert als „bekannte
# False-Positive-Quelle“ in vier Dateien und in jedem Audit von Hand gegenzupruefen.
# Billiger ist es, den Zitatinhalt vor diesen Pruefungen auszublenden. Struktur-Checks
# (\include, \underline, Caption-Reihenfolge) laufen weiter ueber die ganze Zeile –
# sie haben mit Autorschaft nichts zu tun.
NUR_EIGENER_TEXT = {"PRONOMEN", "META-VERB", "NOMINALSTIL"}
BLOCKZITAT_BEGIN_RE = re.compile(r"\\begin\{blockzitat\}")
BLOCKZITAT_END_RE = re.compile(r"\\end\{blockzitat\}")
ZITAT_INHALT_RE = re.compile(r"(\\enquote\{)((?:[^{}]|\{[^{}]*\})*)(\})")

# Float-Platzierung: LaTeX erlaubt den Zeilenumbruch zwischen \begin{figure} und der
# Option, „[H]“ steht dann in der Folgezeile. Die reine Zeilen-Regex meldete das als
# fehlende Platzierung – der zweite dokumentierte False Positive.
FLOAT_BEGIN_RE = re.compile(r"\\begin\{(?:figure|table)\}(.*)$")
# Geviertstrich (U+2014, „—“) ist im Fließtext verboten: im Deutschen unüblich
# (englische Konvention), KI-Marker, Turnitin – immer durch den Halbgeviertstrich „–“
# ersetzen. Der Halbgeviertstrich „–“ mit Leerzeichen ist der korrekte deutsche
# Gedankenstrich; nur seine Häufung als Satzfüller wird gemeldet (Bis-Strich „7–10“
# ohne Leerzeichen zählt nicht mit).
EMDASH_RE = re.compile(r"—")   # U+2014, der verbotene Geviertstrich
GEDANKENSTRICH_RE = re.compile(r"\s–\s")

# Offene Arbeitsmarker aus dem schreib-modus. Sie stehen bewusst in LaTeX-
# Kommentaren und werden deshalb VOR dem Kommentar-Strippen geprüft – sonst
# überleben sie jede Prüfung und landen in der Abgabe.
#   TODO-QUELLE : fehlender BBT-Key; Quelle muss über Zotero nachgezogen werden.
#   UNVERIFIED  : Behauptung noch nicht am Original verifiziert (IU-KI-Richtlinie).
# Schwere HINWEIS, damit laufende Schreib-Sessions keinen Exit-Code 1 erzeugen;
# der pruef-modus listet jeden Treffer namentlich und wertet ihn im Abgabe-Audit
# als offenen Pflichtpunkt (Teil-Check E).
MARKER_RE = re.compile(r"%\s*(TODO-QUELLE|UNVERIFIED)\s*:?\s*(.*)")

# Dateiübergreifende Heuristik-Checks (½-Seiten-Regel, Überschriften-Dopplung, Blockzitat)
SECTION_RE = re.compile(r"\\(section|subsection|subsubsection)\*?\{([^}]*)\}")
ENQUOTE_RE = re.compile(r"\\enquote\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")
PAPERTITLE_RE = re.compile(r"\\newcommand\{\\PaperTitle\}\{([^}]*)\}")
MIN_WORDS_SUBSECTION = 150   # ½-Seiten-Heuristik: darunter Warnung
MAX_QUOTE_WORDS = 40         # > 40 Wörter → blockzitat statt \enquote

# Satzlängen-Heuristik (Verständlichkeit: ein Gedanke pro Satz)
MAX_SENT_WORDS = 30          # einzelner Satz länger → HINWEIS
AVG_SENT_WORDS = 22          # Datei-Durchschnitt darüber → HINWEIS
MIN_SENTS_FOR_AVG = 5        # Durchschnitt erst ab so vielen Sätzen melden
MAX_LONG_SENT_REPORTS = 10   # pro Datei höchstens so viele Einzelfunde listen
ABBREV_RE = re.compile(
    r"\b(z\.\s?B\.|d\.\s?h\.|u\.\s?a\.|u\.\s?U\.|o\.\s?Ä\.|bzw\.|vgl\.|ca\.|inkl\.|ggf\.|evtl\.|sog\.|etc\.|et al\.|Abb\.|Tab\.|Kap\.|Nr\.|S\.\s?\d+)")
SENT_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")

# Menschliche-Textur-Heuristiken (hard-rules-formal.md → Schreibstil, stilprofil.md)
TRIAS_RE = re.compile(r"\b[\w-]+,\s+[\w-]+\s+und\s+[\w-]+\b")
MAX_TRIAS_PER_FILE = 2       # mehr Dreier-Aufzählungen pro Datei → HINWEIS
MAX_RHET_REPORTS = 5         # pro Datei höchstens so viele Fragesatz-Funde listen
MIN_PARAS_FOR_RHYTHM = 6     # Absatz-Gleichförmigkeit erst ab so vielen Textabsätzen
#   „…, die die Ergebnisse zeigt" ist legitim (Relativpronomen nach Komma) –
#   deshalb Ausschluss, wenn direkt ein Komma vorausgeht.
DOUBLE_WORD_RE = re.compile(r"(?<![\w-])(?<!, )([A-Za-zÄÖÜäöüß]{2,})\s+\1(?![\w-])", re.IGNORECASE)

# Unerklärte Abkürzungen (Lernpunkt „PRISMA", externe Prüfung ISSE01 24.07.2026):
# Großbuchstaben-Token im Fließtext, die weder über \ac{} laufen (von _detex
# entfernt) noch in pages/acronyms.tex definiert sind. Ausgenommen: römische
# Zahlen, Normherausgeber vor Nummern („IEC 61508“) und Token, denen im selben
# Satz eine Klammer-Erklärung folgt.
CAPS_TOKEN_RE = re.compile(r"(?<![\wÄÖÜäöüß-])([A-ZÄÖÜ]{2}[A-ZÄÖÜ0-9]*)(?![a-zäöüß])")
ACRO_DEF_RE = re.compile(r"\\acro\{([^}]*)\}")
# Verwendung im Text: \ac{KI}, \acs{KI}, \acl{KI}, \acf{KI}, \acp{KI} …
ACRO_USE_RE = re.compile(r"\\ac[slfp]?\*?\{([^}]*)\}")
ROMAN_RE = re.compile(r"^[IVXLCDM]+$")
# Allgemein geläufige Abkürzungen und Organisations-/Technik-Eigennamen – laut
# Akronym-Regel gehören sie gerade NICHT ins Verzeichnis und wären nur Rauschen.
ACRO_COMMON = {"DIN", "EN", "ISO", "IEC", "IEEE", "ACM", "IU", "USA", "USB", "IP", "PC", "TU", "EU"}
MAX_ACRO_REPORTS = 5

# Vorlagen-Gerüst in pages/: reine Feldzuweisungen, \input-Einbindungen und fixe
# IU-Wortlaute – kein selbst verfasster Fließtext. Beim Verzeichnis-Scan erzeugen
# sie nur Rauschen (CAPS-Platzhalter als „unerklärte Abkürzung“, LaTeX-Maße als
# „langer Satz“) und werden deshalb übersprungen. Der selbst geschriebene Teil von
# pages/ – Abstract, Anhang, Abkürzungsverzeichnis – wird dagegen geprüft: Er geht
# in die Bewertung ein, stand aber bis dahin außerhalb jeder Prüfung.
# Ausdrücklich als Ziel genannte Dateien werden immer geprüft, auch diese hier.
# gender.tex und sperrvermerk.tex tragen fixe IU-Wortlaute (Richtlinien Anhang A
# bzw. Handbuch 5.6) und dürfen nicht umformuliert werden – Stilfunde darin wären
# nicht nur Rauschen, sondern falsche Arbeitsaufträge.
# appendix-setup.tex enthaelt ueberhaupt keinen Fliesstext, sondern nur
# Makrodefinitionen; die Satzlaengen-Heuristik hat dort auf einer \newcommand-
# Kette angeschlagen und einen „Satz mit 37 Woertern" gemeldet.
#
# main.tex ebenfalls: Das Wurzeldokument BINDET Dateien ein, es ist keine
# Kapiteldatei. Die Regel „\input statt \include" gilt Kapiteln; auf main.tex
# angewandt meldete sie sechs Fehler auf der unveraenderten Vorlage - und
# einen siebten, sobald jemand den Anhang einschaltet. Wer main.tex gezielt
# pruefen will, gibt den Pfad an; die dateiuebergreifenden Checks
# (AKTIVIERUNG, ANHANG-VERWEIS, META-PLATZHALTER) lesen main.tex ohnehin
# direkt von der Platte und sind davon nicht betroffen.
GERUEST_DATEIEN = {"cover.tex", "meta.tex", "chapters.tex", "erklaerung.tex",
                   "nutzungsrechte.tex", "gender.tex", "sperrvermerk.tex",
                   "appendix-setup.tex", "main.tex"}


def _shared_phrase(a: str, b: str, min_words: int = 3) -> str | None:
    """Längste gemeinsame Wortfolge (≥ min_words) mit ≥ 2 inhaltstragenden Wörtern (≥ 4 Zeichen).

    Fängt Überschriften, die eine Kernphrase des Arbeitstitels aufgreifen, ohne
    ihn wortgetreu zu enthalten (Lernpunkt „Verschwimmen der Grenze“, ISSE01
    24.07.2026 – die Enthaltensein-Heuristik allein übersah den Fall).
    """
    aw = a.split()
    b_padded = " " + b + " "
    best: list[str] | None = None
    for i in range(len(aw)):
        for j in range(i + min_words, len(aw) + 1):
            cand = aw[i:j]
            if " " + " ".join(cand) + " " not in b_padded:
                break
            if sum(1 for w in cand if len(w) >= 4) >= 2 \
                    and (best is None or len(cand) > len(best)):
                best = cand
    return " ".join(best) if best else None


def _normalize_title(s: str) -> str:
    """Titel für den Dopplungs-Vergleich normalisieren (Kleinschreibung, ohne Makros/Satzzeichen)."""
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    s = re.sub(r"[^\wäöüß ]", " ", s.lower())
    return " ".join(s.split())


def _count_words(text: str) -> int:
    """Grobe Wortzählung auf entkommentiertem Text ohne Makronamen."""
    text = re.sub(r"\\[a-zA-Z]+\*?", " ", text)
    text = re.sub(r"[{}\[\]]", " ", text)
    return len([w for w in text.split() if any(c.isalpha() for c in w)])


def _detex(text: str) -> str:
    """Text von LaTeX-Makros befreien (für die Satzlängen-Heuristik).

    Zitations-/Verweis-Makros samt Argumenten entfernen (deren Keys sind keine
    Satzwörter); übrige Makronamen entfernen, Klammern zu Leerzeichen.
    """
    text = re.sub(
        r"\\(parencites?|textcite|autoref|ref|ac|label|input|includegraphics|quelle|caption)\*?"
        r"(\[[^\]]*\])*(\{[^{}]*\})*", " ", text)
    text = re.sub(r"\\[a-zA-Z]+\*?", " ", text)
    text = re.sub(r"[{}\[\]~]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _split_sentences(text: str) -> list[str]:
    text = ABBREV_RE.sub(" ", text)
    return [s.strip() for s in SENT_SPLIT_RE.split(text) if len(s.split()) >= 3]


def check_readability(path: Path, text: str) -> list[str]:
    """Satzlängen-Heuristik auf entkommentiertem, de-TeX-tem Fließtext.

    Verständlichkeitsregel (hard-rules-formal.md): ein Gedanke pro Satz,
    lieber zwei kurze Sätze als ein langer. Heuristisch – Funde im Kontext prüfen.
    """
    findings: list[str] = []
    sents = _split_sentences(text)
    long_sents = [(s, len(s.split())) for s in sents if len(s.split()) > MAX_SENT_WORDS]
    for s, n in long_sents[:MAX_LONG_SENT_REPORTS]:
        excerpt = " ".join(s.split()[:8])
        findings.append(
            f"{path}: [HINWEIS:SATZLAENGE] Satz mit {n} Wörtern (> {MAX_SENT_WORDS}): „{excerpt} …“ – aufteilen (ein Gedanke pro Satz).")
    if len(long_sents) > MAX_LONG_SENT_REPORTS:
        findings.append(
            f"{path}: [HINWEIS:SATZLAENGE] … und {len(long_sents) - MAX_LONG_SENT_REPORTS} weitere Sätze > {MAX_SENT_WORDS} Wörter.")
    if len(sents) >= MIN_SENTS_FOR_AVG:
        avg = sum(len(s.split()) for s in sents) / len(sents)
        if avg > AVG_SENT_WORDS:
            findings.append(
                f"{path}: [HINWEIS:SATZSCHNITT] Durchschnittliche Satzlänge ~{avg:.0f} Wörter (> {AVG_SENT_WORDS}) – Verständlichkeitsregeln prüfen (kürzere Sätze, siehe stilprofil.md).")
    # Rhetorische Fragen: Fragesätze im Fließtext sind ein KI-Marker.
    # Ausnahme (im Kontext prüfen): die wörtlich formulierte Leitfrage/Forschungsfrage.
    questions = [s for s in sents if s.rstrip().endswith("?")]
    for s in questions[:MAX_RHET_REPORTS]:
        excerpt = " ".join(s.split()[:8])
        findings.append(
            f"{path}: [HINWEIS:RHETFRAGE] Fragesatz im Fließtext: „{excerpt} …“ – rhetorische Fragen vermeiden; nur die wörtliche Leitfrage/Forschungsfrage ist legitim.")
    return findings


def maskiere_zitate(line: str) -> str:
    """Inhalt von \\enquote{} durch Leerzeichen ersetzen, die Hülle behalten.

    Grundlage für die Stil- und Lesbarkeits-Heuristiken: Was in Anführungszeichen
    steht, hat der Verfasser nicht formuliert. Die Hülle bleibt stehen, damit die
    Blockzitat-Heuristik (\\enquote > 40 Wörter) unberührt weiterläuft.
    """
    return ZITAT_INHALT_RE.sub(
        lambda m: m.group(1) + " " * len(m.group(2)) + m.group(3), line)


# Zulaessige Platzierungen. Bis 2026-07-30 war nur „[H]" erlaubt; das erzwang bei
# grossen Tabellen einen Seitenumbruch mit halbleerer Vorseite. Gemessen an einem
# realen Projekt: 389 pt und 136 pt Weissraum auf zwei Seiten - zusammen mehr,
# als die dadurch entstandene Extraseite an Text trug. Vier Kuerzungsrunden mit
# ueber 1.000 Woertern waren teils gar nicht noetig, die Ursache war Layout.
FLOAT_OPT_RE = re.compile(r"^\[[Hhtbp!]+\]")


def float_platzierung_ok(lines: list[str], idx: int, rest: str) -> bool:
    """Steht eine Platzierungsoption hinter \\begin{figure} – oder in der Folgezeile?"""
    if rest.strip():
        return bool(FLOAT_OPT_RE.match(rest.lstrip()))
    for weiter in lines[idx + 1:]:
        w = strip_comment(weiter).strip()
        if not w:
            continue
        return bool(FLOAT_OPT_RE.match(w))
    return False


def caption_text(line: str) -> str:
    """Argument von \\caption{…} klammerbalanciert lesen, sonst "".

    Nicht per Regex bis zur ersten „}": Caption und Label stehen oft in
    derselben Zeile (`\\caption{Titel}\\label{fig:x}`), und ein simples rstrip
    haengt den Label-Rest an den Titel. Verschachtelte Befehle im Titel
    (`\\ac{KI}`) sind derselbe Fall.
    """
    m = re.search(r"\\caption(?:\[[^\]]*\])?\{", line)
    if not m:
        return ""
    tiefe, out = 1, []
    for ch in line[m.end():]:
        if ch == "{":
            tiefe += 1
        elif ch == "}":
            tiefe -= 1
            if tiefe == 0:
                break
        out.append(ch)
    return "".join(out).strip()


def strip_comment(line: str) -> str:
    """Entfernt LaTeX-Kommentare (unmaskiertes %) aus einer Zeile."""
    out = []
    prev = ""
    for ch in line:
        if ch == "%" and prev != "\\":
            break
        out.append(ch)
        prev = ch
    return "".join(out)


def check_file(path: Path) -> tuple[list[str], int, dict]:
    """Liefert (Fundliste, Anzahl harter FEHLER, Metadaten) für eine Datei.

    Metadaten: section_titles / subsection_titles (roh) und word_count –
    Grundlage für die dateiübergreifenden Checks in main().
    """
    findings: list[str] = []
    errors = 0
    skip_depth = 0
    in_blockzitat = False
    caption_seen_in_float = None  # None = außerhalb Float
    dash_count = 0
    meta = {"section_titles": [], "subsection_titles": [], "word_count": 0,
            "figures": 0, "tables": 0, "subsections_nummeriert": 0,
            "subsubsections": 0, "anhang_refs": set(), "zahlwoerter": [],
            "captions": [], "bestimmte_nomen": set()}
    float_caption = ""
    float_label = ""
    float_typ = ""
    float_zeile = 0
    float_hat_inhalt = False
    float_hat_quelle = False
    content_parts: list[str] = []
    readability_parts: list[str] = []

    # Absatz-Rhythmus: Sätze je Textabsatz (Absatzgrenze = echte Leerzeile im Quelltext;
    # reine Kommentarzeilen beenden in LaTeX keinen Absatz und trennen deshalb nicht).
    para_buf: list[str] = []
    para_sent_counts: list[int] = []

    def _flush_para() -> None:
        if para_buf:
            n = len(_split_sentences(_detex(" ".join(para_buf))))
            if n >= 2:
                para_sent_counts.append(n)
            para_buf.clear()

    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for no, raw in enumerate(lines, start=1):
        # Arbeitsmarker zuerst – sie leben in Kommentaren und würden sonst
        # gleich weggeschnitten (auch innerhalb von SKIP_ENVS relevant).
        mk = MARKER_RE.search(raw)
        if mk:
            kind = mk.group(1)
            detail = mk.group(2).strip()
            hint = ("Quelle über Zotero importieren und \\parencite setzen"
                    if kind == "TODO-QUELLE"
                    else "Behauptung am Original verifizieren und Marker entfernen")
            findings.append(
                f"{path}:{no}: [HINWEIS:{kind}] Offener Arbeitsmarker"
                f"{': „' + detail + '“' if detail else ''} – {hint}; vor der Abgabe muss die Stelle geklärt oder gestrichen sein.")

        if not raw.strip():
            if skip_depth == 0:
                _flush_para()
            continue
        line = strip_comment(raw)
        if not line.strip():
            continue

        # Zitierter Fremdtext wird für Stil- und Lesbarkeitsprüfungen ausgeblendet;
        # Wortzählung, Struktur-Checks und die Blockzitat-Heuristik sehen weiter die
        # ganze Zeile. Das Ende erst NACH der Maskierung zurücksetzen, damit auch
        # Text vor einem \end{blockzitat} in derselben Zeile noch als Zitat gilt.
        if BLOCKZITAT_BEGIN_RE.search(line):
            in_blockzitat = True
        line_eigen = "" if in_blockzitat else maskiere_zitate(line)
        if BLOCKZITAT_END_RE.search(line):
            in_blockzitat = False

        # Caption-vor-Label- und Caption-vor-Inhalt-Reihenfolge innerhalb von Floats
        # (vor dem SKIP_ENVS-Block geprüft, da \begin{tikzpicture} selbst als
        # Inhaltsmarker zählt, sein Rumpf aber übersprungen wird)
        mfloat = re.search(r"\\begin\{(figure|table)\}", line)
        if mfloat:
            caption_seen_in_float = False
            content_before_caption = False
            float_typ = mfloat.group(1)
            float_zeile = no
            float_hat_inhalt = False
            float_hat_quelle = False
            float_caption = ""
            float_label = ""
        if caption_seen_in_float is not None:
            if not float_caption:
                float_caption = caption_text(line)
            mlab = re.search(r"\\label\{([^}]+)\}", line)
            if mlab:
                float_label = mlab.group(1)
            if FLOAT_INHALT_RE.search(line):
                float_hat_inhalt = True
                if caption_seen_in_float is False:
                    content_before_caption = True
            if r"\quelle{" in line:
                float_hat_quelle = True
            if r"\caption" in line:
                caption_seen_in_float = True
                meta["figures" if float_typ == "figure" else "tables"] += 1
                if content_before_caption:
                    findings.append(
                        f"{path}:{no}: [FEHLER:CAPTION-POSITION] \\caption nach Bild-/Tabelleninhalt – laut IU-Zitierleitfaden (2.2.5) muss die Beschriftung ÜBER Abbildung/Tabelle stehen (Caption vor \\includegraphics/\\begin{{tikzpicture}}/\\begin{{tabular}}).")
                    errors += 1
            if r"\label{" in line and caption_seen_in_float is False:
                findings.append(
                    f"{path}:{no}: [FEHLER:CAPTION-ORDER] \\label vor \\caption im Float – Caption muss zuerst kommen.")
                errors += 1
            if re.search(r"\\end\{(figure|table)\}", line):
                if float_hat_inhalt and not float_hat_quelle:
                    findings.append(
                        f"{path}:{float_zeile}: [FEHLER:QUELLE-FEHLT] {float_typ}-Float ohne \\quelle{{}} – "
                        f"unter jeder Abbildung/Tabelle steht eine Quellenzeile in 10 Pt., auch bei "
                        f"eigenen: \\quelle{{Eigene Darstellung.}} (IU-Zitierleitfaden 2.2.5).")
                    errors += 1
                if float_caption and float_label:
                    meta["captions"].append((float_label, float_caption))
                caption_seen_in_float = None

        # verbatim-/listing-/tikz-Blöcke überspringen (dort gelten Textregeln nicht)
        if any(re.search(r"\\begin\{" + env + r"\}", line) for env in SKIP_ENVS):
            skip_depth += 1
        if skip_depth:
            if any(re.search(r"\\end\{" + env + r"\}", line) for env in SKIP_ENVS):
                skip_depth -= 1
            continue

        for cat, severity, rx, msg in LINE_CHECKS:
            if rx.search(line_eigen if cat in NUR_EIGENER_TEXT else line):
                findings.append(f"{path}:{no}: [{severity}:{cat}] {msg}")
                if severity == "FEHLER":
                    errors += 1

        if CITE_PLAIN_RE.search(line) and not CITE_OK_KONTEXT_RE.search(line):
            findings.append(
                f"{path}:{no}: [HINWEIS:CITE] \\cite{{}} außerhalb einer Quellenzeile oder eines "
                f"Sekundärzitats – Standard ist \\parencite[S. X]{{key}} (bzw. \\textcite im Satz). "
                f"In \\quelle{{}} und nach „zitiert nach\" ist \\cite dagegen richtig, weil dort "
                f"keine zusätzliche Klammer entstehen darf.")

        # Stellenangabe bei Zitationen (IU-Abweichung von APA)
        for mc in CITE_ARGS_RE.finditer(line):
            hat_locator = False
            for tok in ARG_TOKEN_RE.finditer(mc.group(2)):
                if tok.group(1) is not None:
                    hat_locator = hat_locator or bool(LOCATOR_RE.search(tok.group(1)))
                    continue
                if not hat_locator:
                    findings.append(
                        f"{path}:{no}: [HINWEIS:SEITENANGABE] \\{mc.group(1)}{{{tok.group(2)}}} ohne "
                        f"Stellenangabe – die IU verlangt sie auch bei indirekten Zitaten "
                        f"(Zitierleitfaden Anhang C). Zulässig ohne: werkbezogene Paraphrasen, die "
                        f"sich auf das ganze Werk beziehen. Sonst [S. X] ergänzen; bei Quellen ohne "
                        f"Seitenzahlen [Kap. X] / [Abs. X] / Zeitstempel.")
                hat_locator = False   # nächster Block beginnt ohne Angabe

        meta["subsections_nummeriert"] += len(SUBSECTION_NUM_RE.findall(line))
        meta["subsubsections"] += len(SUBSUBSECTION_RE.findall(line))
        meta["anhang_refs"].update(ANHANG_TITEL_RE.findall(line))

        fb = FLOAT_BEGIN_RE.search(line)
        if fb and not float_platzierung_ok(lines, no - 1, fb.group(1)):
            findings.append(
                f"{path}:{no}: [HINWEIS:FLOAT] Float ohne Platzierungsoption – auch "
                f"nicht in der Folgezeile. `[H]` für alles, was sicher auf eine "
                f"halbe Seite passt, `[htbp]` für größere Tabellen: Sonst schiebt "
                f"LaTeX sie auf die nächste Seite und lässt die vorige halb leer.")

        dw = DOUBLE_WORD_RE.search(line_eigen)
        if dw:
            findings.append(
                f"{path}:{no}: [HINWEIS:DOPPELWORT] „{dw.group(0)}“ – Wortdopplung (Tippfehler) oder fehlendes Komma davor?")

        if EMDASH_RE.search(line):
            findings.append(
                f"{path}:{no}: [FEHLER:GEVIERTSTRICH] Geviertstrich („—“) im Fließtext – im Deutschen unüblich (KI-Marker, Turnitin); durch den Halbgeviertstrich „–“ ersetzen (hard-rules-formal.md → Schreibstil).")
            errors += 1
        dash_count += len(GEDANKENSTRICH_RE.findall(line))

        for kind, title in SECTION_RE.findall(line):
            if kind == "section":
                meta["section_titles"].append(title)
            elif kind == "subsection":
                meta["subsection_titles"].append(title)
        meta["word_count"] += _count_words(line)
        content_parts.append(line)
        # Für Satzlängen- und Absatz-Heuristik: Überschriften- und Caption-Zeilen ausnehmen
        if not SECTION_RE.search(line) and r"\caption" not in line:
            readability_parts.append(line_eigen)
            para_buf.append(line_eigen)

    if dash_count > 3:
        findings.append(
            f"{path}: [HINWEIS:GEDANKENSTRICH] {dash_count}× „Wort – Wort“ – Häufung von Gedankenstrichen (Anti-KI-Stilregel: Gedankenstrich als Satzfüller); umformulieren mit Komma, Semikolon oder eigenem Satz (hard-rules-formal.md → Schreibstil).")

    # Blockzitat-Heuristik: \enquote{} mit > 40 Wörtern gehört in die blockzitat-Umgebung
    for m in ENQUOTE_RE.finditer(" ".join(content_parts)):
        n = _count_words(m.group(1))
        if n > MAX_QUOTE_WORDS:
            findings.append(
                f"{path}: [HINWEIS:BLOCKZITAT] \\enquote mit {n} Wörtern (> {MAX_QUOTE_WORDS}) – direkte Zitate > 40 Wörter gehören in \\begin{{blockzitat}}.")

    # ½-Seiten-Heuristik: Subsection-Datei mit sehr wenig Text
    if meta["subsection_titles"] and not meta["section_titles"] \
            and meta["word_count"] < MIN_WORDS_SUBSECTION:
        findings.append(
            f"{path}: [HINWEIS:HALBSEITE] Nur ~{meta['word_count']} Wörter in dieser Subsection-Datei (< {MIN_WORDS_SUBSECTION}) – ½-Seiten-Regel pro Unterkapitel prüfen.")

    _flush_para()
    # Absatz-Gleichförmigkeit: viele Textabsätze mit (fast) identischer Satzzahl
    if len(para_sent_counts) >= MIN_PARAS_FOR_RHYTHM \
            and max(para_sent_counts) - min(para_sent_counts) <= 1:
        findings.append(
            f"{path}: [HINWEIS:ABSATZ-UNIFORM] {len(para_sent_counts)} Textabsätze mit nahezu gleicher Länge ({min(para_sent_counts)}–{max(para_sent_counts)} Sätze) – Absatzlängen bewusst variieren (stilprofil.md → Absatzbau).")

    detexed_read = _detex(" ".join(readability_parts))

    # Kandidaten für unerklärte Abkürzungen sammeln (Abgleich gegen acronyms.tex in main())
    caps_tokens: dict[str, None] = {}
    for cm in CAPS_TOKEN_RE.finditer(detexed_read):
        tok = cm.group(1)
        if ROMAN_RE.match(tok) or tok in ACRO_COMMON:
            continue
        tail = detexed_read[cm.end():cm.end() + 80]
        if re.match(r"[\s/-]*(?:[A-Z]{1,4}\s*)?\d", tail):  # Normbezeichnung („IEC 61508“, „IEC TR 63069“)
            continue
        if "(" in tail.split(".")[0]:           # Klammer-Erklärung folgt im selben Satz
            continue
        caps_tokens.setdefault(tok, None)
    meta["caps_tokens"] = list(caps_tokens)
    # Über die rohen Zeilen, nicht über detexed_read: Dort ist der \ac-Befehl
    # schon entfernt, und genau er ist hier das Suchmuster. Kommentare müssen
    # aber raus – acronyms.tex erklärt die Verwendung im Kommentar („\ac{MUSTER}"),
    # und das zählte sonst als Verwendung.
    meta["ac_verwendet"] = set(ACRO_USE_RE.findall(
        "\n".join(strip_comment(z) for z in lines)))

    # Dreier-Aufzählungs-Häufung („X, Y und Z" als Standardmuster)
    meta["zahlwoerter"] = ZAHLWORT_RE.findall(detexed_read)
    meta["bestimmte_nomen"] = {n.lower() for n in BESTIMMTES_NOMEN_RE.findall(detexed_read)}

    trias_matches = TRIAS_RE.findall(detexed_read)
    if len(trias_matches) > MAX_TRIAS_PER_FILE:
        findings.append(
            f"{path}: [HINWEIS:TRIAS] {len(trias_matches)}× Dreier-Aufzählung (z. B. „{trias_matches[0]}“) – KI-Standardmuster; nur belassen, wo es sachlich genau drei Dinge sind (hard-rules-formal.md → Schreibstil).")

    findings.extend(check_readability(path, detexed_read))
    findings.extend(check_anaphern(path, lines))

    return findings, errors, meta


def find_paper_title(start: Path) -> str | None:
    """Sucht pages/meta.tex (ab cwd bzw. oberhalb des Zielpfads) und liest \\PaperTitle."""
    candidates = [Path("pages/meta.tex")]
    base = start if start.is_dir() else start.parent
    for parent in [base, *base.parents]:
        candidates.append(parent / "pages" / "meta.tex")
    for c in candidates:
        if c.exists():
            m = PAPERTITLE_RE.search(c.read_text(encoding="utf-8", errors="replace"))
            if m:
                t = _normalize_title(m.group(1))
                return t or None
    return None


def check_title_duplication(metas: dict[Path, dict], paper_title: str | None) -> list[str]:
    """Überschriften-Dopplung: Subsection ≈ Section bzw. Überschrift ≈ \\PaperTitle.

    Heuristik: Vergleich auf normalisierten Titeln – exakt gleich oder die eine
    Überschrift enthält die andere wortgetreu (ab 2 Wörtern Länge).
    """
    findings: list[str] = []

    def repeats(a: str, b: str) -> bool:
        if not a or not b:
            return False
        if a == b:
            return True
        shorter, longer = (a, b) if len(a) <= len(b) else (b, a)
        return len(shorter.split()) >= 2 and shorter in longer

    all_sections = [(_normalize_title(t), t) for m in metas.values() for t in m["section_titles"]]
    for path, m in metas.items():
        for t in m["subsection_titles"]:
            norm = _normalize_title(t)
            for sec_norm, sec_raw in all_sections:
                if repeats(norm, sec_norm):
                    findings.append(
                        f"{path}: [HINWEIS:TITEL-DOPPLUNG] Subsection „{t}“ wiederholt Section-Titel „{sec_raw}“ – Unterpunkte nicht wortgetreu wiederholen.")
                    break
            if paper_title and repeats(norm, paper_title):
                findings.append(
                    f"{path}: [HINWEIS:TITEL-DOPPLUNG] Subsection „{t}“ wiederholt den Titel der Arbeit (\\PaperTitle).")
            elif paper_title and (phrase := _shared_phrase(norm, paper_title)):
                findings.append(
                    f"{path}: [HINWEIS:TITEL-DOPPLUNG] Subsection „{t}“ greift die Titel-Phrase „{phrase}“ auf – Überschriften wiederholen nicht das Thema der Arbeit.")
        for t in m["section_titles"]:
            norm = _normalize_title(t)
            if paper_title and repeats(norm, paper_title):
                findings.append(
                    f"{path}: [HINWEIS:TITEL-DOPPLUNG] Kapitelüberschrift „{t}“ wiederholt den Titel der Arbeit (\\PaperTitle).")
            elif paper_title and (phrase := _shared_phrase(norm, paper_title)):
                findings.append(
                    f"{path}: [HINWEIS:TITEL-DOPPLUNG] Kapitelüberschrift „{t}“ greift die Titel-Phrase „{phrase}“ auf – Kapitelüberschriften wiederholen nicht das Thema der Arbeit.")
    return findings


def find_acronyms(start: Path, ohne_todo: bool = False) -> set[str] | None:
    """Sucht pages/acronyms.tex (analog find_paper_title) und liest die \\acro-Kürzel.

    `ohne_todo=True` lässt als TODO markierte Zeilen weg. Die beiden Prüfungen
    brauchen verschiedene Mengen: Für „unerklärte Abkürzung im Text" zählt der
    Platzhalter der Vorlage als bekannt (sonst meldet ein frisches Projekt sein
    eigenes „MUSTER"), für „ungenutzter Eintrag im Verzeichnis" nicht (er soll
    ersetzt werden und ist kein verwaister Eintrag).
    """
    candidates = [Path("pages/acronyms.tex")]
    base = start if start.is_dir() else start.parent
    for parent in [base, *base.parents]:
        candidates.append(parent / "pages" / "acronyms.tex")
    for c in candidates:
        if c.exists():
            gefunden: set[str] = set()
            for zeile in c.read_text(encoding="utf-8", errors="replace").splitlines():
                if ohne_todo and re.search(r"%.*\bTODO\b", zeile):
                    continue
                gefunden.update(ACRO_DEF_RE.findall(zeile))
            return gefunden
    return None


def check_unexplained_acronyms(metas: dict[Path, dict], acros: set[str] | None) -> list[str]:
    """Abkürzungen im Fließtext ohne \\ac{}-Einführung und ohne acronyms.tex-Eintrag."""
    if acros is None:
        return []
    findings: list[str] = []
    for path, m in metas.items():
        unknown = [t for t in m.get("caps_tokens", []) if t not in acros]
        for tok in unknown[:MAX_ACRO_REPORTS]:
            findings.append(
                f"{path}: [HINWEIS:ABKUERZUNG] „{tok}“ weder per \\ac{{}} eingeführt noch in pages/acronyms.tex – ausschreiben oder als Akronym einführen; allgemein geläufige Abkürzungen und Eigennamen ignorieren.")
        if len(unknown) > MAX_ACRO_REPORTS:
            findings.append(
                f"{path}: [HINWEIS:ABKUERZUNG] … und {len(unknown) - MAX_ACRO_REPORTS} weitere unerklärte Abkürzungen.")
    return findings


# Anaphern, die ein Bezugswort im vorangehenden Satz brauchen. Geprueft wird
# bewusst nur die ABSATZINITIALE Stellung: Dort gibt es konstruktionsbedingt
# keinen vorangehenden Satz, der das Bezugswort liefern koennte - der Befund ist
# damit sicher, ohne Numerus- und Genusabgleich ueber Satzgrenzen, der im
# Deutschen unweigerlich rauschen wuerde.
#
# Anlass: Drei gebrochene Bezuege in einer fremden Arbeit, jeder einer
# Kuerzungsrunde zuzuordnen („Es beginnt mit der Wettbewerbsanalyse" - der Satz,
# der „Kapitel 2" einfuehrte, war gestrichen). Alle drei haben Audits mit
# 100/100 ueberlebt: Geprueft wird der Diff, und im Diff sieht jede einzelne
# Streichung sauber aus. Der Schaden entsteht im Satz davor.
ANAPHER_RE = re.compile(
    r"^(Es|Beide|Daraus|Dabei|Dort|Damit|Letztere[rs]?|Diese[rs]?|Jene[rs]?|"
    r"Ebenso|Dazu|Hierbei)\s+[a-zäöüß]")


def check_anaphern(path: Path, lines: list[str]) -> list[str]:
    """Absatzinitiale Anaphern ohne Bezugswort.

    Ein Absatz, der mit „Es", „Beide" oder „Daraus" beginnt, verweist auf etwas,
    das im Absatz davor stand – nach einer Kürzung womöglich auf nichts mehr.
    HINWEIS, nicht FEHLER: Es gibt legitime Fälle („Es zeigt sich, dass …" als
    unpersönliche Konstruktion), und das Urteil braucht den Kontext.
    """
    findings: list[str] = []
    absatzanfang = True
    for no, roh in enumerate(lines, 1):
        z = strip_comment(roh).strip()
        if not z:
            absatzanfang = True
            continue
        if z.startswith("\\") or z.startswith("%"):
            absatzanfang = True          # Struktur-/Befehlszeile trennt ebenfalls
            continue
        if absatzanfang:
            m = ANAPHER_RE.match(z)
            if m:
                findings.append(
                    f"{path}:{no}: [HINWEIS:ANAPHER] Absatz beginnt mit "
                    f"„{m.group(1)}“ – das Bezugswort steht dann im Absatz davor "
                    f"oder nirgends. Nach Kürzungen der häufigste stille Schaden: "
                    f"Der gestrichene Satz war das Bezugswort. Absatz und "
                    f"Vorgängerabsatz zusammen lesen, nicht den Diff.")
        absatzanfang = False
    return findings


def check_ungenutzte_acronyms(metas: dict[Path, dict], acros: set[str] | None) -> list[str]:
    """Die Gegenrichtung: Einträge im Verzeichnis, die im Text nicht vorkommen.

    Das `acronym`-Paket druckt **jeden** deklarierten `\\acro`-Eintrag, ob
    benutzt oder nicht. Ein Kürzel, das beim Kürzen aus dem Text verschwindet,
    bleibt damit im abgegebenen Abkürzungsverzeichnis stehen – nachgewiesen an
    der leeren Vorlage, deren Platzhalter „MUSTER" nirgends verwendet wird und
    trotzdem im PDF erscheint. Die IU-Richtlinien verlangen ausdrücklich nur
    tatsächlich verwendete Abkürzungen im Verzeichnis.

    FEHLER, nicht Hinweis: Anders als eine unerklärte Abkürzung im Text ist das
    kein Ermessensfall, sondern eine Zeile im PDF, die dort nicht hingehört.
    """
    if not acros:
        return []
    benutzt: set[str] = set()
    for path, m in metas.items():
        # Das Verzeichnis selbst zählt nicht als Verwendungsort.
        if path.name == "acronyms.tex":
            continue
        benutzt |= set(m.get("ac_verwendet", set()))
    ungenutzt = sorted(a for a in acros if a not in benutzt)
    if not ungenutzt:
        return []
    return [f"pages/acronyms.tex: [FEHLER:ABKUERZUNG-UNGENUTZT] "
            f"{', '.join(ungenutzt)} – im Verzeichnis deklariert, im Text nirgends "
            f"per \\ac{{}} verwendet. Das acronym-Paket druckt jeden Eintrag; die "
            f"Zeile steht also im abgegebenen Verzeichnis, ohne dass die Abkürzung "
            f"vorkommt (IU-Richtlinien: nur tatsächlich verwendete aufnehmen). "
            f"Entweder im Text verwenden oder den \\acro-Eintrag streichen."]


def _projekt_root(start: Path) -> Path:
    """Projekt-Root suchen (Ordner mit main.tex) – ab cwd bzw. oberhalb des Ziels."""
    base = start if start.is_dir() else start.parent
    for parent in [Path("."), base, *base.parents]:
        if (parent / "main.tex").is_file():
            return parent
    return Path(".")


def check_unterpunkte(metas: dict[Path, dict]) -> list[str]:
    """„Mindestens zwei Unterpunkte je Teilung" (IU-Richtlinien 3.2).

    Je Kapitelordner die Subsections zählen, je Datei die Subsubsections. Genau
    ein Unterpunkt ist ein Verstoß; null ist erlaubt (dann wird nicht geteilt).
    Bewusst ordner- und dateiweise statt über die Dokumentreihenfolge: Die
    Sortierung der Dateien entspricht nicht zwingend der Lesereihenfolge.
    """
    findings: list[str] = []
    je_ordner: dict[Path, int] = {}
    for path, m in metas.items():
        # Nur Kapiteldateien: In `pages/` stehen Anhänge und Verzeichnisse mit
        # gesternten Überschriften – die sind keine Gliederungspunkte, und ein
        # einzelner Anhang ist selbstverständlich erlaubt.
        if "pages" in path.parts:
            continue
        je_ordner[path.parent] = je_ordner.get(path.parent, 0) + m.get("subsections_nummeriert", 0)
        if m.get("subsubsections") == 1:
            findings.append(
                f"{path}: [FEHLER:UNTERPUNKTE] genau eine \\subsubsection in dieser Datei – "
                f"wird ein Abschnitt geteilt, braucht er mindestens zwei Unterpunkte "
                f"(IU-Richtlinien 3.2). Zweiten ergänzen oder die Unterteilung auflösen.")
    for ordner, n in je_ordner.items():
        if n == 1:
            findings.append(
                f"{ordner}: [FEHLER:UNTERPUNKTE] Kapitel mit genau einer Subsection – "
                f"kein einzelnes 1.1 ohne 1.2. Zweite Subsection ergänzen oder den Inhalt "
                f"ohne Unterteilung ins Kapitel ziehen (IU-Richtlinien 3.2).")
    return findings


def check_aktivierung(metas: dict[Path, dict], root: Path) -> list[str]:
    """Abbildungs-/Tabellenverzeichnis und Anhang gegen die Blöcke in main.tex.

    Der laut `handbuch.md` häufigste Bedienfehler: Bestandteil geschrieben, den
    Aktivierungsblock in main.tex nie eingeschaltet – der Inhalt steht dann in
    der Datei, aber nicht im PDF. Rein mechanisch prüfbar, bis hierher aber ein
    manueller Punkt in Teil-Check C/E.
    """
    main_tex = root / "main.tex"
    if not main_tex.is_file():
        return []
    text = main_tex.read_text(encoding="utf-8", errors="replace")
    findings: list[str] = []
    zahlen = {"figures": sum(m.get("figures", 0) for m in metas.values()),
              "tables": sum(m.get("tables", 0) for m in metas.values())}
    label = {"figures": ("Abbildung(en)", "Abbildungsverzeichnis", r"\listoffigures"),
             "tables": ("Tabelle(n)", "Tabellenverzeichnis", r"\listoftables")}
    for art, rx in LISTOF_RE.items():
        m = rx.search(text)
        if not m:
            continue
        aktiv = "%" not in m.group(1)
        n = zahlen[art]
        was, verzeichnis, befehl = label[art]
        if n >= MIN_VERZEICHNIS and not aktiv:
            findings.append(
                f"main.tex: [FEHLER:AKTIVIERUNG] {n} {was} im Text, aber der Block "
                f"„{verzeichnis}“ ist auskommentiert – ab {MIN_VERZEICHNIS} ist das "
                f"Verzeichnis Pflicht. Die vier Zeilen um {befehl} einkommentieren.")
        elif n < MIN_VERZEICHNIS and aktiv:
            findings.append(
                f"main.tex: [FEHLER:AKTIVIERUNG] nur {n} {was}, aber {verzeichnis} ist "
                f"aktiv – es wird erst ab {MIN_VERZEICHNIS} geführt. Block wieder "
                f"auskommentieren.")
    anhang = root / "pages" / "appendix.tex"
    if anhang.is_file():
        roh = anhang.read_text(encoding="utf-8", errors="replace")
        inhalt = "\n".join(strip_comment(z) for z in roh.splitlines()).strip()
        m = APPENDIX_RE.search(text)
        aktiv = bool(m) and "%" not in m.group(1)
        if len(inhalt) > 40 and not aktiv:
            findings.append(
                "main.tex: [FEHLER:AKTIVIERUNG] pages/appendix.tex enthält Inhalt, aber der "
                "Block „Anhang“ ist auskommentiert – der Anhang erscheint dann NICHT im PDF. "
                "\\include{pages/appendix} einkommentieren.")
    return findings


def anhang_buchstaben(root: Path) -> set[str]:
    """Welche Anhänge (A, B, C …) sind in pages/appendix.tex tatsächlich angelegt?

    Regelfall ist die Vorlagenform `\\newappendix{Titel}`: Der Buchstabe steht
    dort nirgends, er ergibt sich aus der Reihenfolge – der dritte Aufruf ist
    Anhang C. Genau das ist der Zweck des Makros, denn ein von Hand gesetzter
    Buchstabe kann veralten, eine Position nicht.

    Handgeschriebene Überschriften („\\section*{Anhang~C: …}") werden weiter
    erkannt: Arbeiten, die vor der Umstellung begonnen wurden, sollen nicht
    stillschweigend als anhanglos gelten.
    """
    anhang = root / "pages" / "appendix.tex"
    if not anhang.is_file():
        return set()
    zeilen = [strip_comment(z)
              for z in anhang.read_text(encoding="utf-8", errors="replace").splitlines()]
    n_makro = sum(len(NEWAPPENDIX_RE.findall(z)) for z in zeilen)
    gefunden = {chr(ord("A") + i) for i in range(n_makro)}
    for z in zeilen:
        if re.search(r"\\(sub)*section\*?\{", z) or r"\item" in z:
            gefunden.update(ANHANG_TITEL_RE.findall(z))
    return gefunden


PLATZHALTER_RE = re.compile(r"\\newcommand\{\\(\w+)\}\{([^}]*)\}")

# Zaehlaussagen. Bewusst OHNE den unbestimmten Artikel „ein/eine": Der ist im
# Deutschen allgegenwaertig, die Liste waere unbrauchbar lang und wuerde deshalb
# ueberblaettert. Zahlwoerter dagegen sind selten, und jedes einzelne ist eine
# ueberpruefbare Behauptung ueber eine Anzahl - genau die Stellen, die beim
# Umbauen veralten („zwei Einwaende", es sind vier).
ZAHLWORT_RE = re.compile(
    r"(?<![\wäöüß])(zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|beide|mehrere|"
    r"erste[nrs]?|zweite[nrs]?|dritte[nrs]?)\s+([A-ZÄÖÜ][\wäöüß-]{3,})")
# Bruchteile, Zeitspannen und Maßangaben sind zwar Zahlen, aber keine Aussagen
# ueber die eigene Gliederung: „zwei Drittel der Befragten" und „drei Jahre
# Laufzeit" bleiben richtig, egal wie oft das Kapitel umgebaut wird. Aus dem
# Realtest an einer fertigen Seminararbeit - dort waren sie die einzigen
# Fehltreffer.
ZAHLWORT_STOPWORTE = {
    "viertel", "drittel", "fünftel", "sechstel", "achtel", "zehntel", "hälfte",
    "prozent", "prozentpunkte", "jahre", "jahren", "jahrzehnte", "jahrzehnten",
    "monate", "monaten", "wochen", "tage", "tagen", "stunden", "minuten",
    "sekunden", "mal", "male", "euro", "seiten",
}
MAX_ZAHLWORT_REPORTS = 12

# Verkuerzter Rueckverweis im Fliesstext: „die Skizze", „das Mockup". Genau
# diese Form macht eine Doppelbelegung schaedlich - mit Beiwort („die
# Persona-Skizze") bleibt eindeutig, welches Artefakt gemeint ist.
BESTIMMTES_NOMEN_RE = re.compile(
    r"(?<![\wäöüß-])[Dd](?:ie|er|as|en|em)\s+([A-ZÄÖÜ][\wäöüß]{3,})(?![\wäöüß-])")
# Beschreibende Caption-Koepfe. Dass zwei Abbildungen eine „Übersicht" zeigen,
# ist kein Namenskonflikt, sondern normal - solche Woerter benennen die Form der
# Darstellung, nicht das Artefakt.
CAPTION_STOPWORTE = {
    "übersicht", "überblick", "darstellung", "abbildung", "tabelle", "grafik",
    "diagramm", "vergleich", "ergebnis", "ergebnisse", "aufbau", "struktur",
    "verlauf", "ablauf", "beispiel", "auszug", "ausschnitt", "zusammenfassung",
    "verteilung", "entwicklung", "anteil", "eigene", "quelle", "phase", "schritt",
}


def check_caption_doppelbelegung(metas: dict[Path, dict]) -> list[str]:
    """Ein Wort, zwei Artefakte – und im Text steht nur noch „die Skizze".

    Realfall: „Skizze" bezeichnete zugleich die Persona-Skizze im Anhang und –
    über „Mockup-Skizze" verkürzt – die Mockups. Beide Captions für sich waren
    korrekt; erst der verkürzte Rückverweis im Fließtext machte unentscheidbar,
    welches Artefakt gemeint ist. Deshalb schlägt der Check nur an, wenn beides
    zusammenkommt: dasselbe Substantiv in Captions zu **zwei verschiedenen**
    Labels *und* mindestens ein Rückverweis ohne unterscheidendes Beiwort.
    """
    nomen_zu_labels: dict[str, set[str]] = {}
    anzeige: dict[str, str] = {}
    for meta in metas.values():
        for label, caption in meta.get("captions", []):
            for wort in re.findall(r"[A-ZÄÖÜ][\wäöüß]{3,}", caption):
                # Kompositum mitzählen: „Mockup-Skizze" belegt auch „Skizze".
                for teil in {wort, wort.split("-")[-1]}:
                    key = teil.lower()
                    if key in CAPTION_STOPWORTE:
                        continue
                    nomen_zu_labels.setdefault(key, set()).add(label)
                    anzeige.setdefault(key, teil)
    verkuerzt: set[str] = set()
    for meta in metas.values():
        verkuerzt |= meta.get("bestimmte_nomen", set())

    findings = []
    for key, labels in sorted(nomen_zu_labels.items()):
        if len(labels) < 2 or key not in verkuerzt:
            continue
        findings.append(
            f"[HINWEIS:DOPPELBELEGUNG] „{anzeige[key]}“ beschriftet zwei verschiedene "
            f"Objekte ({', '.join(sorted(labels))}) und wird im Text zugleich verkürzt "
            f"als „die/der/das {anzeige[key]}“ aufgegriffen – dort ist nicht "
            f"entscheidbar, welches gemeint ist. Entweder je Objekt ein eigener Name "
            f"oder im Rückverweis das unterscheidende Beiwort mitführen.")
    return findings


def check_zahlwoerter(metas: dict[Path, dict]) -> list[str]:
    """Zählaussagen als Hinweisliste – die Prüfung der Zahl bleibt menschlich.

    Kein FEHLER: Ob „drei Kriterien" stimmt, weiß nur, wer nachzählt. Der Check
    nimmt lediglich das Erinnern ab, welche Stellen beim nächsten Umbau
    nachzuziehen sind.

    Ausgabe bewusst als **ein** Block statt als Befund je Datei: An einer
    fertigen Seminararbeit waren es zehn Dateien, und die Begründung zehnmal zu
    wiederholen kostet mehr Kontext als die Fundstellen selbst.
    """
    zeilen = []
    for path in sorted(metas):
        treffer = [(a, b) for a, b in metas[path].get("zahlwoerter", [])
                   if b.lower() not in ZAHLWORT_STOPWORTE]
        if not treffer:
            continue
        gezeigt = ", ".join(f"„{a} {b}“" for a, b in treffer[:MAX_ZAHLWORT_REPORTS])
        rest = (f" … +{len(treffer) - MAX_ZAHLWORT_REPORTS}"
                if len(treffer) > MAX_ZAHLWORT_REPORTS else "")
        zeilen.append(f"    {path}: {gezeigt}{rest}")
    if not zeilen:
        return []
    return ["[HINWEIS:ZAHLWORT] Zählaussagen zum Gegenprüfen – nach jedem Umbau "
            "nachzählen, veraltete Anzahlen überleben Streichungen und Ergänzungen "
            "am häufigsten:\n" + "\n".join(zeilen)]


# Selbstbezeichnung als Gruppe, obwohl die Arbeit allein geschrieben wurde.
# Bewusst eng: nur die beiden eindeutigen Komposita. „die Gruppe" oder „das
# Team" k\u00f6nnen im Fachtext legitim vorkommen (Zielgruppe, Entwicklungsteam der
# untersuchten Firma) – ein Treffer darauf w\u00e4re Rauschen statt Befund.
AUTORENSCHAFT_RE = re.compile(r"(?mi)^\s*\**\s*Autorenschaft\s*\**\s*:\s*\**\s*(\w+)")
GRUPPENBEZUG_RE = re.compile(r"\b(Projektgruppe|Projektteams?|Projektgruppen)\b")


def autorenschaft(root: Path) -> str | None:
    """„Einzelarbeit" / „Gruppenarbeit" aus aufgabe.md – None, wenn nicht gesetzt."""
    p = root / "aufgabe.md"
    if not p.is_file():
        return None
    m = AUTORENSCHAFT_RE.search(p.read_text(encoding="utf-8", errors="replace"))
    return m.group(1).lower() if m else None


def check_gruppenbezug(metas: dict[Path, dict], root: Path) -> list[str]:
    """Bei Einzelarbeit: Selbstbezeichnung als Projektgruppe ist ein Sachfehler.

    Die Typ-Datei `projektbericht.md` schrieb bis 07/2026 unbedingt „Die
    Projektgruppe …" vor. Ein daraus entstandener falscher Selbstbezug ist
    formal einwandfrei und überlebt deshalb jedes Audit – er behauptet nur eine
    Autorenschaft, die es nicht gab. Deterministisch prüfbar, sobald
    `aufgabe.md` die Autorenschaft ausweist.
    """
    if autorenschaft(root) != "einzelarbeit":
        return []
    findings: list[str] = []
    for path in sorted(metas):
        if "pages" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for no, zeile in enumerate(text.splitlines(), start=1):
            m = GRUPPENBEZUG_RE.search(strip_comment(zeile))
            if m:
                findings.append(
                    f"{path}:{no}: [FEHLER:GRUPPENBEZUG] „{m.group(1)}“ bei Einzelarbeit "
                    f"(laut `aufgabe.md`) – die Arbeit behauptet damit eine Autorenschaft, "
                    f"die es nicht gab. Pronomenfrei umformulieren: „Dieser Bericht …“, "
                    f"„Das Projekt folgte …“, „Die Umsetzung erfolgte …“.")
    return findings


def check_meta_platzhalter(root: Path) -> list[str]:
    """Stehen in pages/meta.tex noch CAPS-Platzhalter der Vorlage?

    Titelblatt und PDF-Metadaten ziehen sich alles von dort; ein übersehener
    Platzhalter steht sichtbar auf Seite I. Läuft nur beim Audit-Lauf (wenn
    `pages/` mitgeprüft wird), nicht in der Schreib-Session – zu Projektbeginn
    sind offene Felder der Normalfall, nicht ein Fund.
    """
    meta = root / "pages" / "meta.tex"
    if not meta.is_file():
        return []
    offen = []
    for m in PLATZHALTER_RE.finditer(meta.read_text(encoding="utf-8", errors="replace")):
        feld, wert = m.group(1), m.group(2).strip()
        if wert and re.fullmatch(r"[A-ZÄÖÜ0-9 ,._-]{3,}", wert):
            offen.append(f"\\{feld}")
    if not offen:
        return []
    return [f"pages/meta.tex: [HINWEIS:META-PLATZHALTER] noch nicht ausgefüllt: "
            f"{', '.join(offen)} – die Felder erscheinen so auf dem Titelblatt und in "
            f"den PDF-Metadaten. Vor der Abgabe müssen alle ersetzt sein."]


def check_anhang_verweise(metas: dict[Path, dict], root: Path) -> list[str]:
    """Jeder Anhang braucht mindestens einen Verweis im Fließtext.

    „Im Text ist mindestens einmal auf den Anhang zu verweisen (z. B. ‚siehe
    Anhang A‘)" (IU-Richtlinien 3.2) – sonst gilt er als nicht eingebunden.
    """
    vorhanden = anhang_buchstaben(root)
    if not vorhanden:
        return []
    verwiesen: set[str] = set()
    for path, m in metas.items():
        if path.name == "appendix.tex":
            continue
        verwiesen.update(m.get("anhang_refs", set()))
    fehlend = sorted(vorhanden - verwiesen)
    return [
        f"pages/appendix.tex: [FEHLER:ANHANG-VERWEIS] Anhang {b} wird im Text nirgends "
        f"erwähnt – zu jedem Anhang gehört mindestens ein Verweis („siehe Anhang {b}“), "
        f"sonst gilt er als nicht eingebunden (IU-Richtlinien 3.2)."
        for b in fehlend]


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministische Formalia-Checks auf .tex-Dateien")
    parser.add_argument("targets", nargs="+", type=Path,
                        help=".tex-Dateien oder Verzeichnisse (rekursiv)")
    args = parser.parse_args()

    files: list[Path] = []
    uebersprungen: list[Path] = []
    for t in args.targets:
        if t.is_dir():
            for f in sorted(t.rglob("*.tex")):
                (uebersprungen if f.name in GERUEST_DATEIEN else files).append(f)
        elif t.exists():
            files.append(t)   # ausdrücklich genannt → auch Gerüstdateien prüfen
        else:
            print(f"FEHLER: {t} nicht gefunden.", file=sys.stderr)
            return 1

    total_findings: list[str] = []
    total_errors = 0
    metas: dict[Path, dict] = {}
    for f in files:
        findings, errors, meta = check_file(f)
        total_findings.extend(findings)
        total_errors += errors
        metas[f] = meta

    total_findings.extend(check_title_duplication(metas, find_paper_title(args.targets[0])))
    acros = find_acronyms(args.targets[0])
    total_findings.extend(check_unexplained_acronyms(metas, acros))
    # Ungenutzte Einträge nur bewerten, wenn der ganze Textbestand im Lauf war –
    # bei `check_formalia.py chapters/02_theorie/` gälte jede Abkürzung der
    # übrigen Kapitel als ungenutzt.
    if any(t.is_dir() and t.resolve() in (_projekt_root(args.targets[0]).resolve(),
                                          (_projekt_root(args.targets[0]) / "chapters").resolve())
           for t in args.targets if t.is_dir()):
        ungenutzt = check_ungenutzte_acronyms(
            metas, find_acronyms(args.targets[0], ohne_todo=True))
        total_errors += sum(1 for f in ungenutzt if "[FEHLER:" in f)
        total_findings.extend(ungenutzt)

    # Dateiübergreifende Struktur- und Aktivierungs-Checks. Sie ergeben nur über
    # den GESAMTEN Bestand Sinn (drei Abbildungen können auf drei Dateien liegen),
    # deshalb nur bei einem Verzeichnis-Lauf und nicht bei einer Einzeldatei.
    if any(t.is_dir() for t in args.targets):
        root = _projekt_root(args.targets[0])
        struktur = (check_unterpunkte(metas) + check_gruppenbezug(metas, root)
                    + check_caption_doppelbelegung(metas) + check_zahlwoerter(metas))
        # Abbildungs-/Tabellenzahl und Anhang-Verweise nur bewerten, wenn der
        # GESAMTE Kapitelbestand im Lauf war. Bei `check_formalia.py
        # chapters/02_theorie/` zählte man sonst die Abbildungen eines einzelnen
        # Kapitels gegen das Verzeichnis der ganzen Arbeit und meldete jedes Mal
        # einen erfundenen Aktivierungsfehler.
        vollstaendig = any(
            t.is_dir() and t.resolve() in (root.resolve(), (root / "chapters").resolve())
            for t in args.targets)
        if vollstaendig:
            struktur += check_aktivierung(metas, root) + check_anhang_verweise(metas, root)
        # Platzhalter-Prüfung nur, wenn `pages/` im Lauf ist – also im Audit,
        # nicht in der Schreib-Session, wo offene Felder normal sind.
        if any(t.is_dir() and (t.name == "pages" or (t / "pages").is_dir())
               for t in args.targets):
            struktur += check_meta_platzhalter(root)
        total_errors += sum(1 for f in struktur if "[FEHLER:" in f)
        total_findings.extend(struktur)

    for line in total_findings:
        print(line)
    n_hints = len(total_findings) - total_errors
    if uebersprungen:
        print(f"\nÜbersprungen (Vorlagen-Gerüst ohne eigenen Fließtext): "
              f"{', '.join(f.name for f in uebersprungen)} – gezielt prüfbar durch "
              f"Angabe des Dateipfads.")
    print(f"\n{len(files)} Datei(en) geprüft: {total_errors} FEHLER, {n_hints} HINWEIS(e).")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
