# Vorlage `pruefbericht.md` (Referenz zu pruef-modus)

Laden, sobald der Bericht geschrieben wird. Pro Lauf überschreiben.

## Feedback-Format

```markdown
# Prüfbericht – <Papiertyp>

**Datum**: <TT.MM.JJJJ> · **Geprüfter Stand**: <Kapitel <name> / alle Kapitel> · **Audit-Typ**: <Kapitel / Voll / Re-Audit / Abgabe>
**Score: <N>/100 – <abgabereif / Überarbeitung empfohlen / nicht einreichen>**

## Teil-Check A – Formalia
- [PASS / FAIL] Zitationen (inkl. Skript-Ergebnis)
- [PASS / FAIL] Eigene Werke
- [PASS / FAIL] Pronomen
- [PASS / FAIL] LaTeX-Format
- [PASS / FAIL] Akronyme
- [PASS / FAIL] Cross-References & Labels
- [PASS / FAIL] Anti-KI-Stil
- [PASS / FAIL] Verständlichkeit (einfache Sprache, Fachbegriffe erklärt)

## Teil-Check B – Argumentationsqualität (nur Pflicht-Punkte der Typ-Datei als FAIL)
- [PASS / FAIL] These erkennbar
- [PASS / FAIL / N.A.] Forschungslücke in Einleitung
- [PASS / FAIL / N.A.] Aktualität/Zeitbezug in Einleitung
- [PASS / FAIL] Gegenargumente reflektiert & entkräftet
- [PASS / FAIL] Syntheseleistung pro Hauptkapitel
- [PASS / FAIL] Limitationen dreischichtig
- [PASS / FAIL / N.A.] Ergebnisse ≠ Interpretation
- [PASS / FAIL] Typspezifisch (<Papiertyp>, aus typen/<typ>.md)
- [PASS / FAIL / N.A.] Leitfragen aus aufgabe.md beantwortet

## Teil-Check C – Struktur
- [PASS / FAIL] ½-Seiten-Regel
- [PASS / FAIL] Max. 3 Kapitelstufen
- [PASS / FAIL] Front-/Backmatter (Verzeichnisse ab 3, Anhang-Kennzeichnung & -Verweise)
- [PASS / FAIL] Outline-Check gegen bestätigtes Kapitelgerüst

## Teil-Check D – Build
- [PASS / FAIL / ÜBERSPRUNGEN] Kompiliert fehlerfrei (latexmk -lualatex)
- [PASS / FAIL / ÜBERSPRUNGEN] Keine undefined references/citations, fehlenden Bilder, doppelten Labels
- [PASS / FAIL / ÜBERSPRUNGEN] Seitenumfang Textteil innerhalb der Vorgabe (<gezählt> von <Vorgabe>)

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)
- [PASS / OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [PASS / OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [PASS / FAIL] Umfang im Soll (Spiegel aus Teil-Check D)
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko)

## Teil-Check F – Literaturverzeichnis (nur Voll-/Abgabe-Audit)
- [PASS / FAIL] Gerendertes Verzeichnis regelkonform (hard-rules-formal.md → Literaturverzeichnis; Funde als Zotero-Arbeitsliste)

## Teil-Check G – Quellentreue (Volltextabgleich)
- [PASS / FAIL] <N> Zitationen geprüft · OK <n> · offen <n> (Details: `quellencheck.md`)
- Befunde je Klasse (WORTLAUT / ZITAT WEICHT AB / SEITE VERDÄCHTIG / CLAIM SCHÄRFER / NICHT PRÜFBAR): <Stelle → Auflage>

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)
- <was nachzusehen ist> | <wo: Datei/Zeile, Quelle, Seite> | <woran zu erkennen, dass es stimmt> | <warum ich es nicht konnte>
## Claims
- Ungesicherte FACTUAL CLAIMS (inkl. Skript-Treffer „FEHLEND"): <Liste mit Stellen>
- Fehlende OWN WORK-Markierungen: <Liste>
- Ungenutzte Bib-Einträge (Aufräumhinweis, kein Score-Abzug): <Liste>

## Punkteabzug im Detail
- <Kategorie>: −<N> (<Anzahl> Vorkommen, gedeckelt bei −<Deckel>)

## Bewertungsschwerpunkte (<Papiertyp>)
- <Kriterium> (<Gewicht>): **je Dimension** [ABGEDECKT / SCHWACH / FEHLT] – <Fundstelle oder Lücke>

## Lieferobjekt-Abgleich
- [PASS / FAIL] Lieferobjekt-Abgleich (Artefakte, Anhang, Abbildungen)

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)
1. ...

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- <alle noch offenen Teil-Check-E-Punkte + offene Volltext-Verifikationen – dieser Block schließt jeden Bericht und jede Chat-Zusammenfassung ab>
```
