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
- [PASS / FAIL / ÜBERSPRUNGEN] Kompiliert fehlerfrei (`scripts/build.ps1`, Exit-Code <0/1>)
- [PASS / FAIL / ÜBERSPRUNGEN] Keine undefined references/citations, fehlenden Bilder, doppelten Labels
- [HINWEIS] Randüberstand ab 5 pt: <Anzahl, Stellen> (kein FAIL, aber Formfehler im gesetzten PDF)
- [PASS / FAIL / ÜBERSPRUNGEN] Seitenumfang Textteil innerhalb der Vorgabe (<gezählt> von <Vorgabe>)

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)
- [PASS / OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [PASS / OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [PASS / FAIL] Umfang im Soll (Spiegel aus Teil-Check D)
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko)

## Teil-Check F – Literaturverzeichnis (nur Voll-/Abgabe-Audit)
- [PASS / FAIL] Gerendertes Verzeichnis regelkonform (`_shared/literaturverzeichnis.md`; Funde als Zotero-Arbeitsliste)

## Teil-Check G – Quellentreue (Volltextabgleich)
- [PASS / FAIL] <N> Zitationen geprüft · OK <n> · offen <n> (Details: `quellencheck.md`)
- Befunde je Klasse (WORTLAUT / ZITAT WEICHT AB / SEITE VERDÄCHTIG / CLAIM SCHÄRFER / NICHT PRÜFBAR): <Stelle → Auflage>

## Teil-Check H – Lesefluss (nur Voll-/Abgabe-Audit, max. −5)
- [PASS / FAIL / N.A.] Anschlüsse: „es"/„beide"/„daraus"/„diese" mit Bezugswort, das aufs Richtige zeigt
- [PASS / FAIL / N.A.] Absatzöffner sind Aussagen, keine abgeschnittenen Reste
- [PASS / FAIL / N.A.] Absatzlänge und Rhythmus ohne erkennbare Kürzungsnarben
- Befunde je Fundstelle, wo erkennbar mit der auslösenden Kürzungsrunde: <Datei:Absatz → was fehlt>

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

**Ein Satz, dessen Stütze mehrfach abgeschwächt werden musste, ist ein Ersetzungs-, kein Umformulierungskandidat.** Steht in `AENDERUNGEN.md` oder in den Statuszeilen, dass derselbe Beleg schon zwei- oder dreimal nachgebessert wurde, ist die nächste Abschwächung die falsche Empfehlung: Die Stütze trägt nicht mehr, sie wird nur höflicher formuliert. Realfall: Nach drei Hedging-Runden wurde die Zitation ersetzt – der Ersatzsatz brauchte in derselben Runde bereits eine Rücknahme und entfiel einen Tag später ganz. Wo die Reparaturhistorie sichtbar ist, gehört sie beim Befund mitzitiert; die Empfehlung lautet dann „Aussage streichen oder neu belegen“, nicht „vorsichtiger formulieren“. Dieselbe Frage stellt Teil-Check G für Zitationen (`RENTIERT NICHT`) – sie gilt für jede Stütze, auch für interne Verweise und die eigene Analyse.
