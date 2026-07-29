# Prüfbericht – Projektbericht

**Datum**: 29.07.2026 · **Geprüfter Stand**: alle Kapitel, Arbeitsverzeichnis sauber auf Commit `3ad42bb` · **Audit-Typ**: Delta-Re-Audit
**Score: 100/100 – abgabereif**

> **Was sich gegenüber dem Vorbericht (77/100, selber Tag) geändert hat.** Alle drei Befunde sind verifiziert behoben, jeder am gebauten PDF und nicht an der Wortzahl gemessen:
> **Befund 1 – Seitenumfang.** Textteil jetzt **exakt 10 Seiten** von 7–10. „1 Einleitung" steht auf PDF-Seite 6 (gedruckt 1), das Literaturverzeichnis auf PDF-Seite 16 (gedruckt 11) — die elfte Textseite ist weg. Die Kürzungsrunde (−77 Wörter) plus der Vittuari-Locator-Fix haben gereicht; die vorsorglich angekündigte Rückfrage zur Sechs-Plattform-Wettbewerbsanalyse ist damit gegenstandslos.
> **Befund 2 – Randüberstand.** `grep -c "Overfull \hbox" build/main.log` → **0**. Bemerkenswert: Die Ursache war nicht die im Vorbericht beschuldigte `\quelle{}`-Zeile, sondern die Tabellenkopfzelle „Nachhaltigkeits-/Restefokus" — der Vorbericht hatte den Fund falsch verortet. Der Fix sitzt jetzt an der richtigen Stelle (manuelle Trennstellen), und die ebenfalls umgestellte Quellenzeile spart nebenbei Wörter.
> **Befund 3 – Ersatzzeichen.** `grep -c "Missing character" build/main.log` → **0** (vorher 4). Im gedruckten Verzeichnis steht jetzt „Pro-environmental Behaviour" statt „pro?environmental".
>
> **Keine Regression durch die Überarbeitung.** Die fünf Streichungen sind gegen alle Pflichtschichten gegengeprüft: Limitationen weiter dreischichtig, alle Zählangaben stimmen, alle Anhänge weiter im Text referenziert, keine Datei unter die Halbseiten-Schwelle gerutscht.

> **Nachtrag in derselben Session (auf Nutzerwunsch, abweichend von der Regel „Audit und Überarbeitung trennen").** Die drei Feinschliff-Punkte sind direkt umgesetzt bzw. entschieden worden; die beiden freigabepflichtigen wurden per `AskUserQuestion` geklärt. Ergebnis: Haushalts-Claim umformuliert (Punkt 1 aus „Bitte manuell prüfen" damit **entschieden und erledigt**), App-Name in der Quellenzeile auf `\enquote{Zu gut für die Tonne!}` angeglichen, leftovercooking-Halbsatz **bewusst weggelassen** (Nutzer-Entscheidung: bei exakt 10 von 10 Seiten sind ~15 Zusatzwörter das schlechtere Geschäft). Nach den Edits erneut gebaut: **Textteil unverändert 10 Seiten**, 0 `!`-Fehler, 0 Overfull \hbox, 0 Missing character, `check_all.py` ohne harte Funde, Teil-Check G wieder 19/19 OK. **Score bleibt 100/100.**

**Delta-Umfang**: die drei Befundstellen des Vorberichts, der vollständige Textdiff `62e19ed..3ad42bb` (6 Kapiteldateien, `references.bib`, `pages/appendix.tex`), alle sechs Prüfskripte, ein vollständiger Neubau (`latexmk -g -lualatex`, Exit 0) samt Log-Auswertung sowie das gebaute `main.pdf` Seite für Seite.

## Teil-Check A – Formalia
- [PASS] **Zitationen** – `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**, 51 HINWEIS (drei weniger als im Vorbericht, kein neuer). `check_bib_keys.py`: alle genutzten Keys valide. Die drei Vittuari-Stellen tragen jetzt einheitlich `[S. 105]` statt des Kapitel-/Absatz-Locators.
- [PASS] **Randüberstand behoben** – siehe Teil-Check D.
- [PASS] Eigene Werke · Pronomen · LaTeX-Format · Cross-References & Labels – keine Regression; alle `\autoref`-Ziele existieren, keine doppelten Labels.
- [PASS mit Hinweis] Akronyme – „KI" (`01_wettbewerbsanalyse.tex`) und „UX" (`03_konzept.tex`) ohne `\ac{}`-Einführung; seit dem 23.07. bewusst als optional eingestuft, kein Regelverstoß.
- [PASS] Anti-KI-Stil – zwei TRIAS-Hinweise (`03_konzept.tex`, `05_phasenplanung.tex`, je 4×), beide sachlich gedeckt. Keine Floskel-Öffner, keine Gedankenstrich-Häufung, keine rhetorischen Fragen.
- [PASS mit Hinweis] Verständlichkeit – 18 SATZLAENGE-Hinweise, davon 3 Tabellen-Artefakte. `05_phasenplanung.tex` (~29 W./Satz) und `07_iteratives_design.tex` (~27) liegen weiter über dem Richtwert 22; verteilt über sieben Dateien, damit unter dem Häufungs-Deckel und ohne Abzug.
- [Hinweis] DOPPELBELEGUNG – „Startseite" beschriftet `fig:mockup_start` und `fig:mockup_start_bookmarks`. Bekannt, kein Abzug.

## Teil-Check B – Argumentationsqualität (Pflicht-Punkte `typen/projektbericht.md`)
Im Delta gezielt an den geänderten Stellen geprüft. Keine Pflichtschicht ist durch die fünf Streichungen beschädigt worden:
- [PASS] **Limitationen weiter dreischichtig** – nachgezählt an allen drei. Limitation 1 trägt nach dem Wegfall der Kontrastfigur unverändert warum (keine Primärdaten, Annahmen hypothetisch) · Mitigation („Abgemildert wird die Grenze dadurch, dass …") · Folgeschritt (Beta-Test in `sec:phasenplanung`).
- [PASS] **Zählangabe mitgeführt** – „zwei Lehren" ist beim Streichen der zweiten Lehre korrekt auf „eine Lehre" gezogen worden; die verbliebene erste Lehre ist eine echte Prozesslehre und steht inhaltlich unverändert.
- [PASS] **Teilaufgaben- und Berichtsinhalte-Abgleich** – die verdichtete Aufzählung in `06_evaluation_reflexion.tex:3` nennt weiterhin alle fünf geforderten Berichtsinhalte (Zielgruppe, Funktionalitäten, UI/UX, Community-Building, Lebensmittel-Journaling). Die dabei entfallenen `\autoref`s sind kein Verlust: Anhang A ist über `02_zielgruppe.tex:9`, Anhang B und C über `03_konzept.tex:34` bzw. `02_limitationen.tex:5` weiter im Text verankert.
- [PASS] **Kein verwaister Einwand** – das gestrichene Reichweitenrisiko des Rettungs-Feeds hinterlässt keine offene Stelle: Ein Grep über „Mindestzahl", „setzt voraus", „hängt davon ab", „bleibt angewiesen" findet in `chapters/` keinen unbeantworteten Vorbehalt mehr.
- Übrige Pflicht-Punkte: unverändert PASS aus den Vorberichten.

## Teil-Check C – Struktur
- [PASS] ½-Seiten-Regel – kein HALBSEITE-Hinweis; keine der gekürzten Dateien ist unter die Schwelle gerutscht.
- [PASS] Outline-Check – Gerüst unverändert: 3 Kapitel, 12 Subsections.
- [PASS] Front-/Backmatter – Abbildungs- (5) und Tabellenverzeichnis (4) aktiv, Anhangsverzeichnis gesetzt, Anhänge A/B/C gekennzeichnet und je mindestens einmal im Text referenziert (am gebauten PDF nachgesehen, nicht nur am Quelltext).
- [PASS] **Redundanz Reflexion ↔ Fazit aufgelöst** – der Hinweis des Vorberichts ist erledigt: Die zweite „Lehre" in `06_evaluation_reflexion.tex` sagte dasselbe wie der Schlusssatz des Fazits und ist gestrichen; das Reichweitenrisiko war eine Limitation im Reflexionskapitel und ist ebenfalls weg. Die Arbeitsteilung Reflexion = Vorgehen, Fazit = Ergebnis ist damit sauber.
- [PASS] Roter Faden – Gesamt-Stresstest (Runde 2) und Gegenlesung (Runden 5/6) sind gelaufen und abgearbeitet; geprüft wurden daher nur Regressionen an den geänderten Stellen. Keine gefunden.
- [Hinweis, kein FAIL] Tabellenwertung `tab:wettbewerbsvergleich`, Spalte „Kommunikation \& Community" – unverändert offen (leftovercooking „mittel" gegen die verengte Kriteriendefinition in `:13`). Die Wertung geht in die selbstkritische Richtung, deshalb weiter kein FAIL.

## Teil-Check D – Build
Vollständiger Neubau in dieser Session: `latexmk -g -lualatex main.tex`, Exit 0, Log um 14:49 Uhr frisch geschrieben. `lualatex`, `latexmk` und `biber` verfügbar — der Umfang ist **gemessen, nicht geschätzt**.
- [PASS] Kompiliert fehlerfrei – 23 PDF-Seiten, **0** `!`-Fehler im Log.
- [PASS] Keine undefined references/citations, keine fehlenden Bilder, keine doppelten Labels. (Die einzige „not found"-Zeile ist eine harmlose biblatex-Info zu `biblatex-dm.cfg`.)
- [PASS] **Keine Overfull \hbox mehr** – 0 im gesamten Dokument, vorher eine mit 11,54 pt. Auch 0 Overfull \vbox. Die 26 Underfull-Meldungen sind Tabellenzellen-Artefakte ohne sichtbare Wirkung.
- [PASS] **Keine „Missing character"-Meldung mehr** – 0, vorher 4.
- [PASS] **Seitenumfang Textteil: 10 Seiten von 7–10.** „1 Einleitung" auf PDF-S. 6 (gedruckt 1), letzte Textseite PDF-S. 15 (gedruckt 10), Literaturverzeichnis ab PDF-S. 16 (gedruckt 11).

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)
- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [PASS] Umfang im Soll – Spiegel aus Teil-Check D (10 von 7–10)
- [OFFEN] `pages/meta.tex`: `\ModuleCode` und `\MatrikelNr` sind noch Platzhalter und stehen so auf dem Titelblatt und in den PDF-Metadaten (`check_formalia.py` meldet es als META-PLATZHALTER)
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)
- [ERINNERT] LanguageTool-Durchgang lokal über den Gesamttext

## Teil-Check F – Literaturverzeichnis
Im Delta-Re-Audit keine Vollprüfung; geprüft wurde der Befund des Vorberichts am gerenderten Verzeichnis.
- [PASS] **Zwei als Körperschaft gespeicherte Autorennamen behoben.** Gefunden in dieser Session beim Lesen des gerenderten Verzeichnisses: `nielsenUsabilityEngineering1993` trug `author = {{Jakob Nielsen}}`, `sauroLewisQuantifying2016` trug `author = {{Jeff Sauro} and {James R. Lewis}}` — doppelte Klammern kennzeichnen in BibTeX eine Körperschaft, also einen einteiligen Namen. Folge waren zwei sichtbare Fehler zugleich: ausgeschriebene Vornamen („Jakob Nielsen. (1993).") und **beide Einträge alphabetisch unter „J"** zwischen Erlhofer und Nivedhitha. Nach dem Zotero-Fix (Umschalten auf zwei Namensfelder) und Re-Export stehen sie korrekt als „Nielsen, J." und „Sauro, J. & Lewis, J. R." an der richtigen Stelle. **Vom Skript nicht gefunden** — `check_bib_hygiene.py` prüft das Autorenfeld nicht auf Körperschafts-Klammern; als Werkzeug-Befund unten aufgenommen.
- [PASS] **Ersatzzeichen behoben** – der Nivedhitha-Eintrag steht im gedruckten Verzeichnis (PDF-S. 16) korrekt als „How Green Social Network Affordances Enhance **Pro-environmental** Behaviour?". Der U+2010-Fix über Zotero hat gegriffen.
- [PASS] **`check_bib_hygiene.py`: 9 Einträge, 0 Hinweise** (vorher 28). Die Zotero-Arbeitsliste ist in dieser Session vollständig abgearbeitet und neu exportiert worden. Behoben: Title Case → Sentence Case bei sechs Einträgen (Barker, Erlhofer, Nivedhitha, Sauro & Lewis, Soma, UN — Nivedhitha hatte der Vorbericht fälschlich als korrekt geführt; am gerenderten Verzeichnis nachgesehen, nicht aus dem Skriptbefund abgeleitet), `urldate` bei sechs Einträgen geleert (nur beim UN-Eintrag war es überhaupt sichtbar: „Verfügbar 21. Juli 2026 unter"), URL neben DOI bei fünf entfernt, Sprachfeld bei vier gesetzt (Erlhofer korrekt `ngerman`), Verlagsort bei drei geleert, zwei Artikelnummern als `eid` statt `pages` — rendert jetzt als „Artikel 11099" bzw. „Artikel 107706". **Damit entfällt der Abzug von −5, den das Abgabe-Audit für die Sentence-Case-Klasse angesetzt hätte.**
- [Hinweis] Nivedhitha behält die eLocator-Form `48(2), e13038` im `pages`-Feld statt als `eid`. Bewusst so gelassen: Das ist die vom Verlag vergebene Schreibweise und in APA gängig; ein „Artikel e13038" wäre doppelt gemoppelt.
- [Hinweis] Deutscher Titel bei Erlhofer bleibt mit großen Substantiven („Website-Konzeption und Relaunch: Das Handbuch für die Praxis") — korrekt, Sentence Case gilt nicht gegen die deutsche Rechtschreibung.

## Teil-Check G – Quellentreue (Volltextabgleich)
- [PASS] **19 Zitationen geprüft · OK 19 · offen 0** (Details: `quellencheck.md`)

Kein WORTLAUT-Befund, kein abweichendes wörtliches Zitat, keine verdächtige oder außerhalb liegende Seitenangabe, kein nicht gedeckter Claim. Die drei Vittuari-Stellen laufen nach dem Zotero-Re-Export und dem gesetzten Seitenversatz (`--offset vittuariHowReduceConsumer2023=-103`) sauber auf die Verlagspaginierung; das `file`-Feld löst auf die Verlagsfassung auf, der Preprint liegt nur noch als unreferenzierte Zweitablage daneben.

**Eine Prüfnotiz korrigiert (kein Textbefund).** Der Urteilseintrag zu `01_ausgangslage_und_problem.tex:5` (Hash `d7fd6058a1`) trug die Begründung der beiden *anderen* Vittuari-Stellen — die Drivers/Levers-Definition —, während der Trägersatz dort den Haushalts-Anteil an der vermeidbaren Verschwendung behauptet. Das Urteil selbst ist richtig: Auf S. 105 der Verlagsfassung steht beides, direkt am Volltext nachgelesen. Notiz ersetzt. Das ist genau der in `SKILL-ANPASSUNGEN.md` als **P2-3** dokumentierte Fall — mit dem Zusatz, dass die Dublette hier *innerhalb desselben Bib-Keys* auftrat und der dort vorgeschlagene Wächter („Notiz-Dublette über verschiedene Bib-Keys") sie deshalb nicht gefangen hätte.

- Ungenutzte Bib-Einträge (Aufräumhinweis, kein Score-Abzug): `iso_9241_210` — Rest aus dem übersprungenen Befund 7.4.
- Volltexte ohne Bib-Verweis (Aufräumhinweis): Krug, Norman und der Vittuari-Preprint liegen in `sources/literatur/`, werden aber nicht zitiert. Kein Mangel.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)
1. ~~**Haushalts-Claim gegen die Quelle abwägen**~~ — **erledigt in derselben Session.** Nach Rückfrage umformuliert: „… entsteht dabei nicht im Handel oder in der Industrie, sondern auf der Verbraucherebene und dort vor allem in privaten Haushalten …". Die neue Fassung bildet den Quellensatz („the responsibility to consumers, particularly at the household level", S. 105) Ebene für Ebene ab und ist damit **enger als die Quelle statt weiter**; die Eurostat-Zahl von 65 % für Haushalte und Food Service deckt die Verbraucherebene korrekt mit ab. Am Volltext gegengeprüft und mit neuem Urteil quittiert (Hash `3ead511986`, alter Hash `d7fd6058a1` entfällt mit dem alten Satz). +8 Wörter, Seitenzahl unverändert.
2. **Prompt-Wortlaut der Mockup-Quellenzeilen** | `pages/appendix.tex`, `\quelle{}` zu den vier Mockups | Erkennbar korrekt, wenn der zitierte Prompt wörtlich dem entspricht, was in Claude Design eingegeben wurde | Warum nicht durch mich: kein Eingabeprotokoll vorhanden. *(Laut Statusnotiz vom 29.07. bereits geprüft und bestätigt — hier nur der Vollständigkeit halber geführt.)*

## Claims
- Ungesicherte FACTUAL CLAIMS: **keine.** Sämtliche 19 Zitationen sind am Volltext geprüft und quittiert.
- Die Plattform-Tatsachenbehauptungen der Wettbewerbsanalyse laufen weiterhin über den Methodensatz (`01_wettbewerbsanalyse.tex:13`) und die Quellenzeile mit Sichtungsdatum — zulässig, weil die Analyse laut ZITIERREGEL eigene Sichtung ist.
- Fehlende OWN WORK-Markierungen: keine.
- Offene `% TODO-QUELLE:` / `% UNVERIFIED:`-Marker: keine.

## Punkteabzug im Detail
- **Keiner.** Alle drei Befunde des Vorberichts sind am gebauten PDF verifiziert behoben, kein neuer Befund hinzugekommen.
- **Summe: −0 → Score 100/100**

Zur ehrlichen Einordnung: 100/100 heißt „alle im Delta-Umfang geprüften Kriterien erfüllt". Nicht enthalten sind die Vollprüfung des Literaturverzeichnisses (Teil-Check F, dort wartet die Sentence-Case-Klasse mit −5 auf das Abgabe-Audit) und die Sprachstichprobe des Abgabe-Audits.

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: ABGEDECKT – alle drei Teilaufgaben ausgeführt, alle sechs Lieferobjekte vorhanden, Seitenumfang jetzt im Soll. Der einzige Abzug dieser Achse aus dem Vorbericht ist damit weg.
- **Prozess (25 %)**: ABGEDECKT – Vorgehen dokumentiert, reflektiert mit zwei konkreten Kursänderungen, Grenzen in drei dreischichtigen Limitationen. Methodenfundierung des Beta-Tests (SEQ, Think-Aloud, Stichprobengröße) belegt.
- **Transfer (15 %)**: ABGEDECKT je Dimension – gesellschaftlich (SDG 12.3), wirtschaftlich (Freemium mit begründeter Trennlinie, Kooperationen), technisch (Funktionsübersicht, Datenvoraussetzung Rezeptbestand).
- **Kreativität (15 %)**: ABGEDECKT – expliziter Innovationsabsatz trennt Eigenes von Übernommenem; Vergleich zu Bestehendem über sechs Plattformen.
- **Dokumentation (10 %)**: ABGEDECKT – 19/19 Zitationen am Volltext geprüft und nachschlagbar, das Ersatzzeichen im Literaturverzeichnis ist behoben. Diese Achse war am 28.07. die schwächste und ist jetzt ohne Befund.
- **Ressourcen (10 %)**: ABGEDECKT – Phasenplanung mit Ressourcenspalte inkl. Daten, Puffer, Abhängigkeiten, zwei Risiken.

## Lieferobjekt-Abgleich
- [PASS] Alle sechs Lieferobjekte liegen vor: `tab:wettbewerbsvergleich`, Persona `tab:persona` (Anhang A), vier Mockups (Anhang B), Plattformname hergeleitet, `tab:funktionsuebersicht`, `tab:phasenplanung`.
- [PASS] Bildsichtung der gestalteten Artefakte vom 28.07. unverändert gültig — keine Bilddatei hat sich seither geändert (`git diff --stat` über `images/` leer).

## Handlungsempfehlungen (nach Priorität)

**Keine score-relevanten Befunde.** Die Arbeit ist aus Sicht dieses Audits abgabereif. Was bleibt, ist Feinschliff und Verwaltung:

1. ~~**Zotero-Arbeitsliste abarbeiten und neu exportieren**~~ — **erledigt in dieser Session**, in zwei Export-Runden (die erste ließ die beiden Artikelnummern fallen, weil `tex.eid` noch nicht im Extra-Feld stand). Ergebnis am gerenderten Verzeichnis geprüft: 0 Hygiene-Hinweise, Alphabetik korrigiert, Artikelnummern wieder da, Build sauber, Textteil unverändert 10 Seiten. Der einzige Posten mit Score-Wirkung im Abgabe-Audit ist damit vom Tisch.
2. **Nutzer-Checkliste unten abarbeiten** (myCampus, `meta.tex`, LanguageTool).
3. **Feinschliff — in dieser Session erledigt bzw. entschieden:**
   - Haushalts-Claim umformuliert (siehe „Bitte manuell prüfen" Punkt 1).
   - Quellenzeile `01_wettbewerbsanalyse.tex:29`: App-Name jetzt `\enquote{Zu gut für die Tonne!}`, deckungsgleich mit der Einleitung.
   - Halbsatz zur leftovercooking-Wertung in `:13` **bewusst nicht ergänzt** (Nutzer-Entscheidung). Der Punkt bleibt damit das, was er seit zwei Berichten ist: ein Hinweis ohne FAIL, weil die Wertung in die selbstkritische Richtung geht. Falls er später doch gewünscht wird, muss er gegenfinanziert werden — der Textteil steht auf der Obergrenze.

### Hinweis zur Quellenzeile (bewusst kein Befund)
Die Umstellung von den sechs Domains auf die sechs Plattformnamen war die im Vorbericht vorgeschlagene Variante und behebt den Randüberstand. Sie nimmt allerdings eine in Runde 6.1 ausdrücklich freigegebene Entscheidung teilweise zurück (damals: „Quellenzeile um sechs offizielle Plattform-Domains erweitern"). Bewertung: unkritisch, weil das Sichtungsdatum („Juli 2026") und die eindeutige Benennung aller sechs Plattformen erhalten sind — genau das, was `sources/Anmerkungen vom Prüfer.md` an Nachvollziehbarkeit einfordert. Falls Sie die Domains dennoch zurückwollen, gehören sie in eine Fußnote statt in die `\quelle{}`-Zeile, sonst kehrt der Überstand zurück.

### Werkzeug-Befunde (kein Abgabebestandteil)
- **P2-3 in `SKILL-ANPASSUNGEN.md` erweitern**: Der Notiz-Wächter muss auch Dubletten *innerhalb desselben Bib-Keys* melden — der heute gefundene Fall wäre dem vorgeschlagenen Schlüsselwechsel-Test entgangen.
- **Neu — `check_bib_hygiene.py` bemerkt eine *fehlende* Artikelnummer nicht.** Nach der ersten Export-Runde waren die `pages`-Felder von Barker und Shen geleert, ohne dass `eid` gesetzt war; im Verzeichnis fehlte die Artikelnummer dadurch ganz. Das Skript meldete **0 Hinweise**, weil es nur prüft, ob im `pages`-Feld etwas Artikelnummer-Artiges *steht* — ein leeres Feld ohne `eid` fällt ihm nicht auf. Die Regel „Artikel ohne Seitenspanne braucht eine Artikelnummer" fehlt also ganz. Aufgefallen ist es nur beim Lesen des gerenderten Verzeichnisses.
- **Neu — `check_bib_hygiene.py` prüft das Autorenfeld nicht.** Ein `author = {{Vorname Nachname}}` (Körperschafts-Klammern um einen Personennamen) führt zu ausgeschriebenem Vornamen und falscher alphabetischer Einsortierung, beides im gedruckten Verzeichnis sichtbar. Das Skript sieht es nicht, weil es nur Titel-, Orts-, Datums- und URL-Felder prüft. Gefunden wurde es erst beim Lesen des gerenderten Verzeichnisses — genau der Schritt, den Teil-Check F Punkt 2 vorschreibt und den ein Skript nicht ersetzt. Vorschlag: Warnung, wenn ein `author`-Feld in doppelten Klammern steht und ein Leerzeichen, aber kein Komma enthält (Körperschaften wie „United Nations General Assembly" bleiben so unauffällig, Personennamen fallen auf).
- **Neu, aus dem Nachtrag dieser Session — `check_umfang.py` verzählt sich bei verschachtelten Klammern.** Die Strip-Regex in `check_umfang.py:60` entfernt Makro-Argumente über `(\{[^{}]*\})+` und kann ein `\quelle{…}` deshalb nicht mehr fassen, sobald darin ein weiteres Makro mit Argument steht. Konkret: Nach der Änderung auf `\quelle{… \enquote{Zu gut für die Tonne!} …}` leckt die gesamte Quellenzeile in die Wortzahl — gemeldet wurden **+33 Wörter**, real geändert haben sich **+8**. Nur zwei Zeichen Unterschied im Quelltext, 25 Wörter Unterschied in der Messung. In `chapters/` ist derzeit genau diese eine Quellenzeile betroffen (die beiden anderen sind schlichte „Eigene Darstellung."); in `pages/appendix.tex` stünden alle fünf Quellenzeilen so da, was aber folgenlos bleibt, weil das Skript nur `chapters/` zählt. Wirkung: Das Frühwarn-Instrument für den Seitenumfang meldet zu viel und würde eine unnötige Kürzungsrunde auslösen. Fix wäre eine Regex mit einer Verschachtelungsebene oder ein Klammerzähler.
- **Neu**: Kein Check liest das Build-Log auf „Missing character". Befund 3 des Vorberichts wäre sonst schon am 28.07. sichtbar gewesen; heute musste er wieder von Hand gegriffen werden.
- **`kapitelplan.md:7`** trägt weiterhin `**Gesamtwortzahl (Richtwert)**: 7–10 Seiten (B.Sc.)`. Die Zeile erwartet eine **Wortzahl**; `check_umfang.py` überspringt den Zielabgleich deshalb stillschweigend. Auf `3750` setzen, dann greift die automatische Warnung.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- Eidesstattliche Erklärung elektronisch über myCampus abgeben — **ohne sie nimmt Turnitin die Einreichung nicht an**
- Einreichungs-Anleitung im myCampus-Kurs lesen
- `pages/meta.tex`: `\ModuleCode` und `\MatrikelNr` ausfüllen (stehen sonst als Platzhalter auf dem Titelblatt und in den PDF-Metadaten)
- ~~`check_bib_hygiene.py`-Arbeitsliste in Zotero abarbeiten~~ **erledigt 29.07., am gerenderten Verzeichnis verifiziert**
- **Jede weitere Textänderung mit einem Build abschließen und die gedruckte Seitenzahl gegenprüfen** — der Textteil steht exakt auf der Obergrenze 10, und `check_umfang.py` zählt derzeit zu hoch (siehe Werkzeug-Befunde); die Wortzahl allein ist kein Beleg
- LanguageTool-Durchgang lokal über den Gesamttext
- Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)
- Namensverfügbarkeit „Resteria" (DPMA / .de-Domain) — offene Restpflicht aus dem Plan-Modus
