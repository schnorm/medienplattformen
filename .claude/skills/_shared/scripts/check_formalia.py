#!/usr/bin/env python3
"""
check_formalia.py — deterministische Formalia-Checks auf .tex-Dateien.

Ersetzt tokenintensives LLM-Durchlesen für alle mechanisch prüfbaren Regeln
aus hard-rules-formal.md. Inhaltliche Checks (Argumentation, Synthese, Stil)
bleiben beim Prüf-Modus — dieses Skript findet nur, was ein Regex sicher
finden kann.

Nutzung (vom Projekt-Root):
    python3 .claude/skills/_shared/scripts/check_formalia.py chapters/
    python3 .claude/skills/_shared/scripts/check_formalia.py chapters/01_einleitung/01_motivation.tex

Ausgabeformat: <datei>:<zeile>: [KATEGORIE] Meldung
Exit-Code: 1 wenn mindestens ein FEHLER (harter Verstoß), sonst 0.
HINWEIS-Funde beeinflussen den Exit-Code nicht.

Grenzen: Kommentare werden entfernt; Inhalte von lstlisting/verbatim werden
übersprungen. Wortgrenzen sind heuristisch — Funde immer im Kontext prüfen.
"""

import argparse
import re
import sys
from pathlib import Path

# (Kategorie, Schwere, Regex, Meldung)
# Schwere: "FEHLER" = harter Verstoß laut hard-rules-formal.md, "HINWEIS" = prüfen.
LINE_CHECKS = [
    ("PRONOMEN", "FEHLER",
     re.compile(r"(?<![\\\w])(ich|wir|man)(?![\w])", re.IGNORECASE),
     "Verbotenes Pronomen (ich/wir/man) — umformulieren („Diese Arbeit …“)."),
    ("QUOTE-ENV", "FEHLER",
     re.compile(r"\\begin\{quote\}"),
     "\\begin{quote} statt \\begin{blockzitat} (IU: 1,27 cm links, ohne Anführungszeichen)."),
    ("INCLUDE", "FEHLER",
     re.compile(r"\\include\{"),
     "\\include{} in Kapiteldateien verboten — \\input{} verwenden."),
    ("AUTOREF", "HINWEIS",
     re.compile(r"(?<!~)\\autoref\{"),
     "\\autoref ohne führendes ~ (z. B. vgl.~\\autoref{...})."),
    ("REF", "HINWEIS",
     re.compile(r"\\ref\{"),
     "\\ref{} statt \\autoref{} — \\autoref erzeugt „Kapitel N“ automatisch."),
    ("QUOTES", "FEHLER",
     re.compile(r"[\"„“”]"),
     "Gerade/typografische Anführungszeichen im Quelltext — \\enquote{} verwenden."),
    ("CITE", "HINWEIS",
     re.compile(r"\\cite\{"),
     "\\cite{} gefunden — Standard ist \\parencite[S. X]{key} (bzw. \\textcite im Satz)."),
    ("FLOAT", "HINWEIS",
     re.compile(r"\\begin\{(figure|table)\}(?!\[H\])"),
     "Float ohne [H]-Platzierung."),
    ("UNDERLINE", "FEHLER",
     re.compile(r"\\underline\{"),
     "Unterstreichungen sind laut IU-Richtlinien nicht zulässig."),
    # Verständlichkeits-Heuristiken (hard-rules-formal.md → Verständlichkeit, stilprofil.md)
    ("META-VERB", "HINWEIS",
     re.compile(r"(?<![\\\w])(entfaltet|entfalten|bündelt|bündeln|verortet|verorten|adressiert|adressieren|konstatiert|konstatieren)(?![\w])", re.IGNORECASE),
     "Gestelztes Meta-Verb — einfaches Verb wählen (beschreibt/zeigt/fasst zusammen), siehe stilprofil.md."),
    ("NOMINALSTIL", "HINWEIS",
     re.compile(r"(?<![\\\w])(erfolgt|erfolgen|im Rahmen (der|des|dieser|dieses)|vor dem Hintergrund|unter Berücksichtigung)(?![\w])", re.IGNORECASE),
     "Nominalstil-Marker — aktive Verb-Formulierung prüfen („Die Arbeit untersucht X“ statt „Die Untersuchung erfolgt“)."),
]

SKIP_ENVS = ("lstlisting", "verbatim", "tikzpicture")
DASH_RE = re.compile(r"\s[—–]\s")

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
    lieber zwei kurze Sätze als ein langer. Heuristisch — Funde im Kontext prüfen.
    """
    findings: list[str] = []
    sents = _split_sentences(text)
    long_sents = [(s, len(s.split())) for s in sents if len(s.split()) > MAX_SENT_WORDS]
    for s, n in long_sents[:MAX_LONG_SENT_REPORTS]:
        excerpt = " ".join(s.split()[:8])
        findings.append(
            f"{path}: [HINWEIS:SATZLAENGE] Satz mit {n} Wörtern (> {MAX_SENT_WORDS}): „{excerpt} …“ — aufteilen (ein Gedanke pro Satz).")
    if len(long_sents) > MAX_LONG_SENT_REPORTS:
        findings.append(
            f"{path}: [HINWEIS:SATZLAENGE] … und {len(long_sents) - MAX_LONG_SENT_REPORTS} weitere Sätze > {MAX_SENT_WORDS} Wörter.")
    if len(sents) >= MIN_SENTS_FOR_AVG:
        avg = sum(len(s.split()) for s in sents) / len(sents)
        if avg > AVG_SENT_WORDS:
            findings.append(
                f"{path}: [HINWEIS:SATZSCHNITT] Durchschnittliche Satzlänge ~{avg:.0f} Wörter (> {AVG_SENT_WORDS}) — Verständlichkeitsregeln prüfen (kürzere Sätze, siehe stilprofil.md).")
    return findings


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

    Metadaten: section_titles / subsection_titles (roh) und word_count —
    Grundlage für die dateiübergreifenden Checks in main().
    """
    findings: list[str] = []
    errors = 0
    skip_depth = 0
    caption_seen_in_float = None  # None = außerhalb Float
    dash_count = 0
    meta = {"section_titles": [], "subsection_titles": [], "word_count": 0}
    content_parts: list[str] = []
    readability_parts: list[str] = []

    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for no, raw in enumerate(lines, start=1):
        line = strip_comment(raw)
        if not line.strip():
            continue

        # Caption-vor-Label- und Caption-vor-Inhalt-Reihenfolge innerhalb von Floats
        # (vor dem SKIP_ENVS-Block geprüft, da \begin{tikzpicture} selbst als
        # Inhaltsmarker zählt, sein Rumpf aber übersprungen wird)
        if re.search(r"\\begin\{(figure|table)\}", line):
            caption_seen_in_float = False
            content_before_caption = False
        if caption_seen_in_float is not None:
            if caption_seen_in_float is False and re.search(
                    r"\\includegraphics|\\begin\{tikzpicture\}|\\begin\{tabular", line):
                content_before_caption = True
            if r"\caption" in line:
                caption_seen_in_float = True
                if content_before_caption:
                    findings.append(
                        f"{path}:{no}: [FEHLER:CAPTION-POSITION] \\caption nach Bild-/Tabelleninhalt — laut IU-Zitierleitfaden (2.2.5) muss die Beschriftung ÜBER Abbildung/Tabelle stehen (Caption vor \\includegraphics/\\begin{{tikzpicture}}/\\begin{{tabular}}).")
                    errors += 1
            if r"\label{" in line and caption_seen_in_float is False:
                findings.append(
                    f"{path}:{no}: [FEHLER:CAPTION-ORDER] \\label vor \\caption im Float — Caption muss zuerst kommen.")
                errors += 1
            if re.search(r"\\end\{(figure|table)\}", line):
                caption_seen_in_float = None

        # verbatim-/listing-/tikz-Blöcke überspringen (dort gelten Textregeln nicht)
        if any(re.search(r"\\begin\{" + env + r"\}", line) for env in SKIP_ENVS):
            skip_depth += 1
        if skip_depth:
            if any(re.search(r"\\end\{" + env + r"\}", line) for env in SKIP_ENVS):
                skip_depth -= 1
            continue

        for cat, severity, rx, msg in LINE_CHECKS:
            if rx.search(line):
                findings.append(f"{path}:{no}: [{severity}:{cat}] {msg}")
                if severity == "FEHLER":
                    errors += 1

        dash_count += len(DASH_RE.findall(line))

        for kind, title in SECTION_RE.findall(line):
            if kind == "section":
                meta["section_titles"].append(title)
            elif kind == "subsection":
                meta["subsection_titles"].append(title)
        meta["word_count"] += _count_words(line)
        content_parts.append(line)
        # Für die Satzlängen-Heuristik: Überschriften- und Caption-Zeilen ausnehmen
        if not SECTION_RE.search(line) and r"\caption" not in line:
            readability_parts.append(line)

    if dash_count > 3:
        findings.append(
            f"{path}: [HINWEIS:GEDANKENSTRICH] {dash_count}× „Wort — Wort“ — Anti-KI-Stilregel prüfen (Gedankenstrich als Satzfüller).")

    # Blockzitat-Heuristik: \enquote{} mit > 40 Wörtern gehört in die blockzitat-Umgebung
    for m in ENQUOTE_RE.finditer(" ".join(content_parts)):
        n = _count_words(m.group(1))
        if n > MAX_QUOTE_WORDS:
            findings.append(
                f"{path}: [HINWEIS:BLOCKZITAT] \\enquote mit {n} Wörtern (> {MAX_QUOTE_WORDS}) — direkte Zitate > 40 Wörter gehören in \\begin{{blockzitat}}.")

    # ½-Seiten-Heuristik: Subsection-Datei mit sehr wenig Text
    if meta["subsection_titles"] and not meta["section_titles"] \
            and meta["word_count"] < MIN_WORDS_SUBSECTION:
        findings.append(
            f"{path}: [HINWEIS:HALBSEITE] Nur ~{meta['word_count']} Wörter in dieser Subsection-Datei (< {MIN_WORDS_SUBSECTION}) — ½-Seiten-Regel pro Unterkapitel prüfen.")

    findings.extend(check_readability(path, _detex(" ".join(readability_parts))))

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

    Heuristik: Vergleich auf normalisierten Titeln — exakt gleich oder die eine
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
                        f"{path}: [HINWEIS:TITEL-DOPPLUNG] Subsection „{t}“ wiederholt Section-Titel „{sec_raw}“ — Unterpunkte nicht wortgetreu wiederholen.")
                    break
            if paper_title and repeats(norm, paper_title):
                findings.append(
                    f"{path}: [HINWEIS:TITEL-DOPPLUNG] Subsection „{t}“ wiederholt den Titel der Arbeit (\\PaperTitle).")
        for t in m["section_titles"]:
            if paper_title and repeats(_normalize_title(t), paper_title):
                findings.append(
                    f"{path}: [HINWEIS:TITEL-DOPPLUNG] Kapitelüberschrift „{t}“ wiederholt den Titel der Arbeit (\\PaperTitle).")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministische Formalia-Checks auf .tex-Dateien")
    parser.add_argument("targets", nargs="+", type=Path,
                        help=".tex-Dateien oder Verzeichnisse (rekursiv)")
    args = parser.parse_args()

    files: list[Path] = []
    for t in args.targets:
        if t.is_dir():
            files.extend(sorted(t.rglob("*.tex")))
        elif t.exists():
            files.append(t)
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

    for line in total_findings:
        print(line)
    n_hints = len(total_findings) - total_errors
    print(f"\n{len(files)} Datei(en) geprüft: {total_errors} FEHLER, {n_hints} HINWEIS(e).")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
