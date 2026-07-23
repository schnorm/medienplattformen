# Prüfbericht — Projektbericht

**Datum**: 23.07.2026 · **Geprüfter Stand**: alle Kapitel (Einleitung, Durchführung, Fazit) + Anhang · **Audit-Typ**: Voll
**Score: 75/100 — Überarbeitung empfohlen** (die Abzüge stammen ausschließlich aus `main.tex`-Verdrahtung, die laut Projektregeln nur der Nutzer ändert; Inhalt und Formalia sind auditsauber — der Weg zur Abgabereife ist kurz)

**Vorbedingung erfüllt**: Gegenlesung (Runde 1) und Gesamt-Stresstest (Runde 2) sind gelaufen und vollständig abgearbeitet; `AENDERUNGEN.md` → „Offen" ist leer. `PERSISTENT.md`/`MEMORY.md` gelesen — keine abweichenden Audit-Kriterien, außer: Teil-Check E ist nie score-relevant (MEMORY 2026-07-19), berücksichtigt.

---

## Teil-Check A — Formalia
- [PASS] Zitationen — `check_bib_keys.py`: alle 6 Keys valide, keine ungenutzten Einträge. `\parencite[S. X]` bei stellenbezogenen Zitaten (vittuari S. 106/S. 1, barker S. 10, soma S. 9); werkbezogene Paraphrasen ohne Seite (un, nivedhitha, shen) regelkonform.
- [PASS] Eigene Werke — `\quelle{Eigene Darstellung.}` auf allen eigenen Tabellen/Abbildungen (tab:wettbewerbsvergleich, fig:konzeptfluss, tab:funktionsuebersicht, tab:phasenplanung, tab:persona); kein `\cite{}` auf Eigenwerke; KI-Mockups mit Pflichtmuster „Erstellt mit dem Prompt … durch Claude Design (Claude Sonnet 5), Abbildung nachträglich manuell bearbeitet."
- [PASS] Pronomen — `check_formalia.py` 0 FEHLER; dritte Person streng („Die Projektgruppe …").
- [PASS] LaTeX-Format — 0 FEHLER; `[H]`, Caption vor `\label`, `\enquote{}`, TikZ mit `box`/`arr`-Styles.
- [PASS] Akronyme — `\ac{MVP}` genutzt, in `acronyms.tex` definiert. (Minor, kein FAIL: UI/UX werden inline mit Vollform + Klammer eingeführt statt per `\ac{}` — zulässige Alternative, aber optional vereinheitlichbar.)
- [PASS] Cross-References & Labels — Präfixe `sec:`/`fig:`/`tab:` konsistent. **Aber**: fünf Verweise zeigen auf Anhang-Labels, die im kompilierten Dokument fehlen — siehe Teil-Check D / Handlungsempfehlung 1.
- [PASS] Anti-KI-Stil — keine gehäuften Marker (`check_formalia.py`: einzelne HINWEISE, keine >3-Häufung in einem Kapitel). USP-Motiv wird über die Subsections wiederholt (bekannter Gegenlesungs-Hinweis), bleibt aber unter der Score-Schwelle.
- [PASS] Verständlichkeit — einfache Sprache, Fachbegriffe bei Erstnennung erklärt (Drivers/Levers, Nudge, Influence by Osmosis, MVP). Vereinzelte lange Sätze (03_konzept 37 W., 04_community Ø 23 W., 05_phasenplanung Ø 26 W.) — HINWEIS-Ebene, nicht gehäuft, kein Abzug.

## Teil-Check B — Argumentationsqualität (nur Pflicht-Punkte der Typ-Datei als FAIL)
- [PASS] These erkennbar — Leitfrage/Ziel (Konzeption Resteria) und normative These (Reste-Matching + echte Social-Community als USP) getrennt.
- [N.A.] Forschungslücke in Einleitung — laut Typ-Datei nur „optional".
- [PASS] Aktualität/Zeitbezug in Einleitung (Pflicht) — SDG 12.3 / Lebensmittelverschwendung als projektbezogener Anlass.
- [PASS] Gegenargumente reflektiert & entkräftet (empfohlen) — vier Einwände in 01_wettbewerbsanalyse explizit behandelt (inkl. leftovercooking, Foodsharing).
- [PASS] Syntheseleistung pro Hauptkapitel — Durchführung verbindet Marktlücke, Literatur-Hebel und eigene Konzeptleistung.
- [PASS] Limitationen dreischichtig (Pflicht) — drei Grenzen je mit warum · Mitigation · zukünftiger Schritt.
- [N.A.] Ergebnisse ≠ Interpretation — entfällt (nicht empirisch).
- [PASS] Typspezifisch — Phasenplanung als Tabelle vorhanden; dritte Person streng; „Eigene Darstellung." durchgehend.
- [PASS] Leitfragen aus `aufgabe.md` beantwortet — alle drei Teilaufgaben real ausgeführt (Feedback-Schleifen sauber als „geplant" gekennzeichnet, von `aufgabe.md` gedeckt); Abhakliste, Schlüsselbegriffe und Berichtsinhalte vollständig adressiert (per Grep bestätigt: Event-Kalender-Verzicht begründet, Gruppen/Foren begründet ausgeschlossen, Journaling/Menüplanung eingebunden, Verengung begründet).
- [PASS] Dimensionsabgleich (Abdeckungs-Tabelle) — Transfer nun beidseitig (gesellschaftlich + wirtschaftlich/Freemium), alle sechs Bewertungskriterien im Text bedient.

## Teil-Check C — Struktur
- [PASS] ½-Seiten-Regel — HINWEIS auf 03_vorgehen_und_aufbau (~143 W.); zwei substanzielle Absätze, vertretbar, kein FAIL.
- [PASS] Max. 3 Kapitelstufen — Section → Subsection, keine vierte Ebene.
- [FAIL] Front-/Backmatter — **Abbildungs- und Tabellenverzeichnis fehlen, obwohl 5 Abbildungen und 4 Tabellen vorliegen** (IU: ab 3 einbinden). `\listoffigures`/`\listoftables` sind in `main.tex` auskommentiert. Anhang-Kennzeichnung (A/B) und mind. 1 Verweis pro Anhang im Text vorhanden — aber der Anhang selbst wird nicht kompiliert (siehe Handlungsempfehlung 1).
- [PASS] Outline-Check — Einleitung (10–15 %) → Durchführung inkl. Evaluation/Reflexion (70–80 %) → Fazit mit dreischichtigen Limitationen; identisch mit dem bestätigten Kapitelgerüst.
- **Roter Faden** (Gesamt-Stresstest lief → nur Regressions-Stichprobe): Zahlen konsistent nachgezählt — „sechs Plattformen" = 6 Tabellenzeilen, „vier Kriterien" = 4 Spalten, „fünf Phasen" = 5 Zeilen, „drei Teilaufgaben/Grenzen/Lehren" je 3. **Eine Unschärfe** (unter Score-Schwelle, siehe Handlungsempfehlung 3): 02_limitationen spricht von „vier Plattform-Kategorien", während 01_wettbewerbsanalyse Reste-Matching als „zweite Plattform-Kategorie" und leftovercooking als „dritte Reste-Matching-App" derselben Kategorie führt — die interne Zählung ergibt drei Kategorien. GS-4 (Foodsharing-Wertung) und GS-3 (Zeitpuffer) im Text als erledigt bestätigt; zum Zeitpuffer bleibt eine minimale Wortunschärfe (Tabelle: Puffer „inklusive" in MVP-Phase Woche 8–17; Text: „zwischen MVP-Entwicklung und Beta-Test") — Wochen widersprechen sich nicht mehr, nur die Formulierung.

## Teil-Check D — Build
- [ÜBERSPRUNGEN] Kompiliert fehlerfrei — `lualatex`/`latexmk`/`biber` in dieser Umgebung nicht verfügbar. **Lokaler Build durch den Nutzer nötig.**
- [FAIL — statisch bestimmt] Keine undefined references — **`\include{pages/appendix}` ist in `main.tex` (Zeile 339) auskommentiert**. Dadurch fehlen im kompilierten Dokument die Labels `tab:persona`, `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_profil`, `fig:mockup_feed` → fünf undefined references, und die vier UI/UX-Mockups (gefordertes Lieferobjekt) sowie die Persona-Tabelle erscheinen gar nicht. Der Fließtext behauptet zugleich ihre Existenz („liegt in Anhang B vor", „siehe Anhang A"). Dies ist faktisch die Wiederkehr des ursprünglich abgabekritischen Gegenlesungs-Befunds 1 auf der Kompilier-Ebene.
- [ÜBERSPRUNGEN] Seitenumfang — ohne Build nicht messbar; Nutzer prüft Textteil (7–10 S. B.Sc.) lokal.

## Teil-Check E — Abgabe (informativ, kein Score-Abzug)
- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben — Status laut `CLAUDE.md` → Fristen offen.
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen — nicht dokumentiert.
- [FAIL-Spiegel] Umfang im Soll — nicht verifiziert (Build übersprungen), siehe Teil-Check D.
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko).

## Claims
- Ungesicherte FACTUAL CLAIMS: keine erfundenen Belege; alle `\parencite` valide. Nivedhitha (2024) und Shen (2023) sind nur per Abstract belegt — vor Abgabe am Volltext verifizieren (Nutzer-Pflicht, IU-KI-Richtlinie).
- Fehlende OWN-WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: keine.
- Offene `% UNVERIFIED:`-Marker: keine im Text.

## Punkteabzug im Detail
- Undefined references / fehlendes Lieferobjekt im Build (Teil-Check D, Root Cause: Anhang nicht in `main.tex` eingebunden): −15 (5 undefined refs + fehlende Pflicht-Abbildungen, gedeckelt bei −15)
- Struktur — Abbildungs-/Tabellenverzeichnis nicht eingebunden trotz ≥ 3 (Teil-Check C): −10
- **Summe: −25 → 75/100**
- Nicht score-relevant (Empfehlungen): Kategorien-Zählung „vier" vs. drei; Zeitpuffer-Wortlaut; UI/UX-`\ac{}`-Vereinheitlichung; ½-Seiten-HINWEIS 03_vorgehen.

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: ABGEDECKT inhaltlich — Konzept erfüllt die Aufgabenstellung, Abgleich in 06_evaluation. SCHWACH im Auslieferungszustand, weil das geforderte UI/UX-Mockup im kompilierten Dokument fehlt (Anhang nicht eingebunden).
- **Prozess (25 %)**: ABGEDECKT — Phasenplanung, Reflexion, Lessons Learned, dreischichtige Limitationen.
- **Transfer (15 %)**: ABGEDECKT beide Dimensionen — gesellschaftlich (SDG 12.3) und wirtschaftlich (Freemium, Kooperationen).
- **Kreativität (15 %)**: ABGEDECKT — Wettbewerbsvergleich (6 Plattformen) + offensiv benannter Zero-Waste-Innovationskern.
- **Dokumentation (10 %)**: ABGEDECKT im Text; SCHWACH bis der Anhang kompiliert wird (Entstehungs-Artefakte sonst nicht sichtbar).
- **Ressourcen (10 %)**: ABGEDECKT — Aufwands-/Ressourcenschätzung je Phase.

## Lieferobjekt-Abgleich
- [FAIL] `appendix.tex` enthält alle Objekte (Persona-Tabelle, 4 Mockups) real, ist aber nicht in `main.tex` eingebunden → im Ergebnis-PDF nicht vorhanden. Wettbewerbsvergleich, Funktionsübersicht, Phasenplanung liegen im kompilierten Textteil vor. Bildateien (`images/durchfuehrung/*.png`) existieren. Fix ist rein Verdrahtung (siehe Handlungsempfehlung 1).

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)
1. **[Blockierend, Nutzer-Aktion in `main.tex`]** `\appendix` und `\include{pages/appendix}` (main.tex Z. 338–339) einkommentieren, damit Persona und die vier UI/UX-Mockups kompiliert werden und die fünf Anhang-`\autoref`s aufgelöst sind. Ohne diesen Schritt fehlt ein gefordertes Lieferobjekt im PDF und der Text behauptet dessen Existenz — nicht abgabefähig. (Ich ändere `main.tex` regelkonform nicht selbst.)
2. **[Nutzer-Aktion in `main.tex`]** Abbildungsverzeichnis (5 Abb.) und Tabellenverzeichnis (4 Tab.) einbinden: die je vier Zeilen bei `\listoffigures` (Z. 288–291) und `\listoftables` (Z. 296–299) einkommentieren.
3. **[Optional, Text]** Kategorien-Zählung angleichen: entweder in 02_limitationen „vier" → „drei Plattform-Kategorien" oder in 01_wettbewerbsanalyse die „zweite/dritte"-Nummerierung an eine Vier-Kategorien-Lesart anpassen. Ein Wort.
4. **[Optional, Text]** Zeitpuffer-Formulierung in 05_phasenplanung:23 an die Tabelle angleichen („innerhalb der MVP-Phase eingeplant" statt „zwischen MVP-Entwicklung und Beta-Test").
5. **[Optional]** UI/UX konsistent als `\ac{}` führen oder bei der aktuellen Inline-Form belassen.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- `main.tex`: Anhang einbinden (Handlungsempfehlung 1) **und** lokal mit `latexmk -lualatex main.tex` kompilieren; Log auf undefined references/citations, fehlende Bilder, doppelte Labels prüfen.
- `main.tex`: Abbildungs-/Tabellenverzeichnis einkommentieren (Handlungsempfehlung 2).
- Seitenumfang des Textteils (7–10 S. B.Sc., ab „1 Einleitung" bis vor Literaturverzeichnis) am kompilierten PDF prüfen.
- Nivedhitha (2024) und Shen (2023) am Volltext verifizieren (bislang nur Abstract).
- Eidesstattliche Erklärung elektronisch über myCampus abgeben (Voraussetzung, sonst nimmt Turnitin die Einreichung nicht an).
- Einreichungs-Anleitung im myCampus-Kurs lesen; keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko).
- LanguageTool-Durchgang (lokal) über den Gesamttext.
