#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bib-Hygiene: prüft references.bib gegen die IU-Zitierleitfaden-Abweichungen.

Aufruf (vom Projekt-Root):
    python .claude/skills/_shared/scripts/check_bib_hygiene.py [references.bib]

Ergänzt check_bib_keys.py (Key-Validierung) um Feld-Hygiene:

  HINWEIS: `urldate` gesetzt – die IU will KEIN Abrufdatum (Abweichung von APA);
           Feld in Zotero leeren („Heruntergeladen am") oder Eintrag prüfen.
  HINWEIS: `doi` UND `url` gesetzt – DOI reicht; URL nur bei frei zugänglichen
           Werken ohne DOI (Bezahl-Datenbank → gar keine URL, wie Druckversion).
  HINWEIS: Journal-Artikel (@article) ohne `doi` – DOI angeben, wenn vorhanden.
  HINWEIS: `note`/`addendum` mit „zitiert nach" – Sekundärzitate gehören in den
           Text, nur die Sekundärquelle ins Verzeichnis.

Erweiterung (Lernpunkte aus der externen Prüfung ISSE01, 24.07.2026 – neun
Verzeichnis-Befunde, die kein interner Check angesehen hatte):

  HINWEIS: gerade Anführungszeichen (") in `title`/`booktitle` – kollidieren mit
           babel-ngerman-Shorthands ("S→SS, "a→ä) und zerstören den Titel im PDF.
  HINWEIS: `location`/`address` gesetzt – APA 7: kein Verlagsort.
  HINWEIS: `series` gesetzt – IU: „Reihentitel werden im Literaturverzeichnis
           nicht genannt" (z. B. LNCS samt Bandnummer).
  HINWEIS: Datumsbereich (2017-09-19/2017-09-22) – rendert als verstümmeltes
           Eventdatum. Volldatum nur bei Eintragstypen, wo das Jahr genügt
           (Bücher, Sammelwerke, Proceedings, Hochschulschriften). Zeitungs-
           artikel, Internetquellen und Blogbeiträge brauchen das Volldatum
           laut Zitierleitfaden 2.3.5/2.3.6 – dort wird nichts gemeldet.
  HINWEIS: abgekürzter Zeitschriftentitel („J. Netw. Comput. Appl.") – APA
           verlangt den vollen Namen; häufige Altlast aus EBSCO-/ACM-Importen.
  HINWEIS: Sprachfeld weder deutsch noch englisch – die Arbeit zitiert laut
           hard-rules-formal.md nur deutsch- oder englischsprachige Quellen.
  HINWEIS: Autor sieht wie eine abgekürzte Institution aus ({IEC}) – IU:
           Institutionsnamen im Verzeichnis nicht abkürzen. Die Kurzform im
           Text kommt aus `tex.shortauthor:` (Zotero-Feld Extra), nicht aus
           einem gekürzten Autorenfeld.
  HINWEIS: englischer Titel wirkt wie Title Case – IU: Sentence Case. Nötig sind
           BEIDE Schritte: Titel in Zotero umstellen UND in Better BibTeX das
           Feld „Titel-Casing auf Titel anwenden" (Erweitert → Miscellaneous)
           auf `off` setzen; sonst caset der Export jedes Mal zurück.
  HINWEIS: @article-`pages` sieht wie eine Artikelnummer aus (z. B. 104373) –
           gehört als `eid` in den Eintrag (Zotero: Extra-Feld `tex.eid: N`).
  HINWEIS: Eintrag sieht wie ein Gesetz aus – juristische Textarten gehören
           laut Zitierleitfaden 2.4.2 nur in den Text, nie ins Verzeichnis.

Nur Hinweise, kein Exit-Code ≠ 0 außer bei Parse-Fehlern – Korrekturen laufen
IMMER über Zotero (references.bib nie manuell editieren).
"""

import re
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

FULLDATE_RE = re.compile(r"^\d{4}-\d{2}(-\d{2})?$")
DAYDATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INSTITUTION_ABBREV_RE = re.compile(r"^\{?[A-ZÄÖÜ]{2,8}\}?$")

# Eintragstypen, bei denen laut Zitierleitfaden das JAHR genügt. Ein Volldatum
# ist dort ein Import-Artefakt („1. Januar") und rendert als Phantomdatum.
# Bewusst NICHT enthalten: @online/@misc (Internetquellen) und @article –
# Zeitungsartikel, Websites, PDF-Dokumente und Blogbeiträge brauchen laut
# Zitierleitfaden 2.3.5/2.3.6 das VOLLSTÄNDIGE Datum („Tag. Monat Jahr").
# Ein pauschaler Hinweis riete dort zur Verschlechterung.
DATUM_NUR_JAHR = {"book", "inbook", "incollection", "collection", "inproceedings",
                  "proceedings", "thesis", "phdthesis", "mastersthesis",
                  "report", "techreport", "manual", "booklet"}

# Abgekürzter Zeitschriftentitel („J. Netw. Comput. Appl."). APA verlangt den
# vollen Namen; die Abkürzung ist die häufigste Altlast aus EBSCO/ACM-Importen.
JOURNAL_ABK_RE = re.compile(r"(?<![\w.])[A-ZÄÖÜ][a-zäöü]{0,5}\.(?!\w)")
MIN_JOURNAL_ABK = 2

# Sprachfelder, die zur Projektregel „nur deutsch- oder englischsprachige
# Quellen" passen (hard-rules-formal.md → Zitationen).
LANG_OK = ("de", "ger", "ngerman", "german", "en", "eng", "american", "british",
           "usenglish", "ukenglish", "australian", "canadian", "newzealand")
# Großgeschriebenes Wort mit Kleinbuchstaben-Rest – Indiz für Title Case,
# wenn es (nach dem ersten Wort) gehäuft auftritt.
CAPWORD_RE = re.compile(r"(?<![\w{])[A-Z][a-zäöü]+")
ARTNO_PAGES_RE = re.compile(r"^\d{5,}$")


def parse_entries(text: str):
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", text, re.DOTALL):
        etype, key, body = m.group(1).lower(), m.group(2), m.group(3)
        fields = {fm.group(1).lower(): fm.group(2).strip()
                  for fm in re.finditer(r"(\w+)\s*=\s*[{\"](.*?)[}\"]\s*,?\s*\n", body, re.DOTALL)}
        yield etype, key, fields


def hints_for(etype: str, key: str, fields: dict) -> list[str]:
    """Alle Hinweise für einen Eintrag – Korrektur immer über Zotero."""
    hints: list[str] = []
    if "urldate" in fields:
        hints.append(f"[HINWEIS] {key}: `urldate` gesetzt – IU-Vorgabe: kein Abrufdatum; in Zotero leeren.")
    if "doi" in fields and fields.get("url"):
        hints.append(f"[HINWEIS] {key}: DOI und URL gesetzt – DOI reicht, URL entfernen (über Zotero).")
    if etype == "article" and "doi" not in fields:
        hints.append(f"[HINWEIS] {key}: Journal-Artikel ohne DOI – DOI ergänzen, falls vorhanden.")
    for f in ("note", "addendum"):
        if "zitiert nach" in fields.get(f, "").lower():
            hints.append(f"[HINWEIS] {key}: „zitiert nach“ im Feld `{f}` – Sekundärzitat gehört in den Text.")

    # – Erweiterungen (externe Prüfung ISSE01, 24.07.2026) –
    for f in ("title", "booktitle"):
        if '"' in fields.get(f, ""):
            hints.append(
                f"[HINWEIS] {key}: gerades Anführungszeichen (\") im Feld `{f}` – kollidiert mit "
                f"babel-ngerman (\"S→SS); in Zotero typografische Anführungszeichen setzen.")
    for f in ("location", "address"):
        if fields.get(f):
            hints.append(f"[HINWEIS] {key}: `{f}` = „{fields[f]}“ – APA 7: kein Verlagsort; in Zotero leeren.")
    if fields.get("series"):
        hints.append(
            f"[HINWEIS] {key}: `series` = „{fields['series']}“ – IU: Reihentitel werden im "
            f"Literaturverzeichnis nicht genannt; Reihe (und zugehörige Bandnummer) in Zotero leeren.")
    date = fields.get("date", "")
    if "/" in date:
        hints.append(
            f"[HINWEIS] {key}: Datumsbereich „{date}“ – rendert als verstümmeltes Eventdatum; "
            f"in Zotero nur das Jahr eintragen.")
    elif (DAYDATE_RE.match(date) or FULLDATE_RE.match(date)) and etype in DATUM_NUR_JAHR:
        hints.append(
            f"[HINWEIS] {key}: Volldatum „{date}“ bei @{etype} – hier reicht das Jahr "
            f"(Phantomdaten wie „1. Januar“ stammen aus Datenbank-Importen); in Zotero prüfen. "
            f"Achtung: Bei Zeitungsartikeln, Internetquellen und Blogbeiträgen ist das "
            f"Volldatum dagegen VORGESCHRIEBEN – dort nichts löschen.")
    author = fields.get("author", "")
    if INSTITUTION_ABBREV_RE.match(author):
        hints.append(
            f"[HINWEIS] {key}: Autor „{author}“ wirkt wie eine abgekürzte Institution – IU: "
            f"„Der Name einer Institution wird im Literaturverzeichnis nicht abgekürzt“; ausschreiben. "
            f"Fürs Kurzzitat im Text nicht nötig: `tex.shortauthor: <Kürzel>` ins Zotero-Feld "
            f"Extra – biblatex-apa führt die Abkürzung dann beim ersten Zitat selbst ein.")
    langid = fields.get("langid", "")
    title = fields.get("title", "")
    if title and not langid.startswith(("ngerman", "german")):
        capwords = CAPWORD_RE.findall(title)
        # erstes Wort nicht mitzählen, falls es selbst so beginnt
        if capwords and title.lstrip("{").startswith(capwords[0]):
            capwords = capwords[1:]
        if len(capwords) >= 3:
            hints.append(
                f"[HINWEIS] {key}: Titel wirkt wie Title Case ({len(capwords)} großgeschriebene Wörter) – "
                f"IU: Sentence Case. Zwei Schritte, beide nötig: Titel in Zotero in Sentence Case "
                f"eintragen UND in Better BibTeX das Feld „Titel-Casing auf Titel anwenden\" "
                f"(Erweitert → Miscellaneous) auf `off` setzen – sonst schreibt der Export englische "
                f"Titel bei jedem Lauf zurück in Title Case. Sprachfeld `en` trotzdem setzen.")
        if not langid:
            hints.append(
                f"[HINWEIS] {key}: kein Sprachfeld – in Zotero `en` (bzw. `de`) setzen, sonst greifen "
                f"Sentence-Case und Silbentrennung des Stils nicht.")
    if etype == "article" and ARTNO_PAGES_RE.match(fields.get("pages", "")):
        hints.append(
            f"[HINWEIS] {key}: `pages` = „{fields['pages']}“ sieht wie eine Artikelnummer aus – "
            f"gehört als `eid` (Zotero: Extra-Feld `tex.eid: {fields['pages']}`), `pages` leeren.")
    journal = fields.get("journaltitle") or fields.get("journal") or ""
    if len(JOURNAL_ABK_RE.findall(journal)) >= MIN_JOURNAL_ABK:
        hints.append(
            f"[HINWEIS] {key}: Zeitschriftentitel „{journal}“ wirkt abgekürzt – APA verlangt den "
            f"vollen Namen („Journal of Network and Computer Applications“ statt „J. Netw. Comput. "
            f"Appl.“). Häufige Altlast aus EBSCO-/ACM-Importen; in Zotero ausschreiben.")
    if langid and not langid.lower().startswith(LANG_OK):
        hints.append(
            f"[HINWEIS] {key}: Sprachfeld „{langid}“ – die Arbeit zitiert nur deutsch- oder "
            f"englischsprachige Quellen (hard-rules-formal.md). Sprachfeld prüfen: Ist der "
            f"VOLLTEXT tatsächlich anderssprachig, Quelle ersetzen; ist nur das Feld falsch "
            f"gesetzt, in Zotero korrigieren.")
    if "gesetze-im-internet" in fields.get("url", "") or etype in ("legislation", "jurisdiction"):
        hints.append(
            f"[HINWEIS] {key}: Eintrag wirkt wie ein Gesetz/juristische Textart – gehört laut "
            f"Zitierleitfaden 2.4.2 nur in den Text (z. B. „§ 32 BSIG“ + Abkürzungsverzeichnis), "
            f"Eintrag in Zotero löschen.")
    return hints


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("references.bib")
    if not path.is_file():
        print(f"FEHLER: {path} nicht gefunden.")
        return 1
    text = path.read_text(encoding="utf-8", errors="replace")
    n = hints = 0
    for etype, key, fields in parse_entries(text):
        if etype in ("comment", "preamble", "string"):
            continue
        n += 1
        for h in hints_for(etype, key, fields):
            print(h)
            hints += 1
    print(f"\n{n} Einträge geprüft, {hints} Hinweis(e). Korrekturen ausschließlich über Zotero + BBT-Export.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
