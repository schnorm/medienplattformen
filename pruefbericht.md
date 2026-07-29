# Prüfbericht – Projektbericht

**Datum**: 29.07.2026 · **Geprüfter Stand**: alle Kapitel, Arbeitsverzeichnis sauber auf Commit `62e19ed` · **Audit-Typ**: Delta-Re-Audit
**Score: 77/100 – Überarbeitung empfohlen**

> **Was sich gegenüber dem 28.07. (43/100) geändert hat.** Vier der fünf Befunde des Vorberichts sind verifiziert erledigt: die drei falschen Seitenangaben (Vittuari 2×, Soma 1×), die unbelegte Autorennennung und die drei Quellen ohne Volltext. Teil-Check G läuft erstmals mit **19 von 19 Zitationen auf OK** — die Quellenlage der Arbeit ist damit vollständig am Volltext geprüft, und das war der größte Einzelposten des Vorberichts (−47 von −57).
>
> **Was offen bleibt und was neu ist.** Der Seitenumfang steht unverändert bei **11 Seiten** — die Kürzung um 60 Wörter hat die Seite nicht gekippt (−10). Dazu zwei Funde, die dieser Bericht erstmals sehen konnte, weil `lualatex`/`biber` in dieser Umgebung wieder verfügbar sind und der Build tatsächlich lief: ein sichtbarer Randüberstand unter der Wettbewerbstabelle (−8) und ein Ersatzzeichen im gedruckten Literaturverzeichnis (−5). Beide sind Altlasten, keine Regressionen — sie waren nur nie messbar. **Kein Befund betrifft These, Argumentation oder Aufbau.**

**Delta-Umfang**: die vier Befundstellen des Vorberichts (`03_konzept.tex:5`, `01_kernergebnisse_und_ausblick.tex:5`, `01_ausgangslage_und_problem.tex:5`, `04_community_und_feedback.tex:7`, `06_evaluation_reflexion.tex:7`), die drei Stellen der Nivedhitha-Korrektur vom 29.07., alle sechs Prüfskripte, ein vollständiger Neubau (`latexmk -g -lualatex`) samt Log-Auswertung und das gebaute `main.pdf`.

## Teil-Check A – Formalia
- [PASS] **Zitationen** – `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**, 52 HINWEIS. `check_bib_keys.py`: alle genutzten Keys valide. Alle 19 Zitationen tragen einen Locator oder sind werkbezogene Paraphrasen (drei Fälle: Barker in `02_limitationen.tex:3`, UN in `01_ausgangslage_und_problem.tex:5`, Shen in `04_community_und_feedback.tex:5` — jeweils Bezug auf das ganze Werk, zulässig).
- [FAIL] **Sichtbarer Randüberstand** – `01_wettbewerbsanalyse.tex:28`, siehe Befund 2.
- [PASS] Eigene Werke · Pronomen · LaTeX-Format · Cross-References & Labels – unverändert gegenüber dem 28.07., keine Regression.
- [PASS mit Hinweis] Akronyme – „KI" (`01_wettbewerbsanalyse.tex`) und „UX" (`03_konzept.tex`) ohne `\ac{}`-Einführung; seit dem 23.07. bewusst als optional eingestuft, kein Regelverstoß.
- [PASS] Anti-KI-Stil – zwei TRIAS-Hinweise (`03_konzept.tex`, `05_phasenplanung.tex`, je 4×), beide sachlich gedeckt. Keine Floskel-Öffner, keine Gedankenstrich-Häufung, keine rhetorischen Fragen.
- [PASS mit Hinweis] Verständlichkeit – 20 SATZLAENGE-Hinweise, davon 3 Tabellen-Artefakte. `05_phasenplanung.tex` (~29 W./Satz) und `07_iteratives_design.tex` (~27) liegen weiter über dem Richtwert 22; verteilt über sieben Dateien, damit unter dem Häufungs-Deckel und ohne Abzug. Unverändert gegenüber dem Vorbericht.
- [Hinweis] DOPPELBELEGUNG – „Startseite" beschriftet `fig:mockup_start` und `fig:mockup_start_bookmarks`; im Rückverweis das unterscheidende Beiwort mitführen. Bekannt, kein Abzug.

## Teil-Check B – Argumentationsqualität (Pflicht-Punkte `typen/projektbericht.md`)
Im Delta nicht erneut vollständig gelesen — geprüft wurden ausschließlich die seit dem 28.07. geänderten Stellen. Keine Pflichtschicht ist dabei beschädigt worden:
- [PASS] Limitationen weiter dreischichtig – alle drei Limitationen tragen warum · Mitigation · Folgeschritt (`02_limitationen.tex:3,5,7`, nachgezählt).
- [PASS] Zählangabe „zwei Befunde aus der Nudge-Forschung" (`03_konzept.tex:9`) stimmt nach der Nivedhitha-Umformulierung weiterhin (Barker, Nivedhitha).
- [PASS] Der Beleg für den Verzicht auf Forum und Gruppen (`04_community_und_feedback.tex:7`) steht nach der Locator-Korrektur inhaltlich unverändert und ist jetzt auffindbar.
- [PASS] Der Rückverweis, der die gestrichene Autorennennung ersetzt (`06_evaluation_reflexion.tex:7` → `sec:community_und_feedback`), zeigt semantisch korrekt auf die Stelle, an der die Kursänderung begründet wird.
- Übrige Pflicht-Punkte: unverändert PASS aus dem Vorbericht vom 28.07.

## Teil-Check C – Struktur
- [PASS] ½-Seiten-Regel – kein HALBSEITE-Hinweis; keine Datei ist durch die Kürzung unter die Schwelle gerutscht.
- [PASS] Outline-Check – Gerüst unverändert: 3 Kapitel, 12 Subsections.
- [PASS] Front-/Backmatter – Abbildungs- (5) und Tabellenverzeichnis (4) aktiv, Anhangsverzeichnis gesetzt, Anhänge A/B/C gekennzeichnet und je mindestens einmal im Text referenziert.
- [PASS] Roter Faden – Gesamt-Stresstest (Runde 2) und Gegenlesung (Runden 5/6) sind gelaufen und abgearbeitet; geprüft wurden daher nur Regressionen an den geänderten Stellen. Keine gefunden.
- [Hinweis] **Redundanz Reflexion ↔ Fazit** – bei Umfangsüberschreitung ist dieser Punkt laut Skill der erste, der abgearbeitet wird. Zwei Stellen tragen Doppelungen: die zweite „Lehre" in `06_evaluation_reflexion.tex:11` (Trennung literaturbasierter Hebel von eigenen Entscheidungen) sagt dasselbe wie der Schlusssatz in `01_kernergebnisse_und_ausblick.tex:5`, und das Reichweitenrisiko in `06_evaluation_reflexion.tex:5` ist eine Limitation im Reflexionskapitel. Beides ist Kürzungsreserve, siehe Befund 1.
- [Hinweis, kein FAIL] Tabellenwertung `tab:wettbewerbsvergleich`, Spalte „Kommunikation \& Community" – unverändert offen aus dem Vorbericht (leftovercooking „mittel" gegen die verengte Kriteriendefinition in `:13`). Die Wertung geht in die selbstkritische Richtung, deshalb weiter kein FAIL.

## Teil-Check D – Build
Vollständiger Neubau in dieser Session: `latexmk -g -lualatex main.tex`, Exit 0. `lualatex`, `latexmk` und `biber` sind wieder verfügbar — der Umfang ist damit **gemessen, nicht geschätzt**.
- [PASS] Kompiliert fehlerfrei – 24 Seiten, keine `!`-Fehler im Log.
- [PASS] Keine undefined references/citations, keine fehlenden Bilder, keine doppelten Labels.
- [FAIL] **Overfull \hbox 11,54 pt (≈ 4 mm) in `01_wettbewerbsanalyse.tex:28`** – siehe Befund 2. Der einzige Overfull \hbox im gesamten Dokument; die 24 Underfull-Meldungen sind Tabellenzellen-Artefakte ohne sichtbare Wirkung. Ein Overfull \vbox (12,2 pt) beim Seitenausgleich bleibt unter der Sichtbarkeitsschwelle.
- [FAIL] **Seitenumfang Textteil: 11 Seiten von 7–10.** „1 Einleitung" auf PDF-Seite 6 (gedruckt 1), Literaturverzeichnis auf PDF-Seite 17 (gedruckt 12) → Textteil gedruckte Seiten 1–11. Siehe Befund 1.
- [Hinweis] 4× „Missing character: There is no ‐ (U+2010)" – Ursache und Wirkung siehe Teil-Check F.

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)
- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [FAIL] Umfang im Soll – Spiegel aus Teil-Check D (11 von 7–10)
- [OFFEN] `pages/meta.tex`: `\ModuleCode` und `\MatrikelNr` sind noch Platzhalter und stehen so auf dem Titelblatt und in den PDF-Metadaten (`check_formalia.py` meldet es als META-PLATZHALTER)
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)
- [ERINNERT] LanguageTool-Durchgang lokal über den Gesamttext

## Teil-Check F – Literaturverzeichnis
Im Delta-Re-Audit nicht als Vollprüfung vorgesehen; der Befund unten stammt aus der **Build-Log-Auswertung** und ist damit regulär im Delta-Umfang.
- [FAIL] **Ersatzzeichen im gedruckten Verzeichnis** – siehe Befund 3.
- [Hinweis, im Delta nicht gewertet] `check_bib_hygiene.py`: 9 Einträge, 28 Hinweise, keine neue Klasse. Sammelbild unverändert: `urldate` gesetzt (6×), DOI **und** URL gesetzt (5×), Title-Case-Verdacht (7×), fehlendes Sprachfeld (4×), Verlagsort bei drei Büchern, zwei Artikelnummern im `pages`-Feld. **Im gerenderten Verzeichnis sichtbar** ist davon vor allem die gemischte Titelschreibung: fünf Einträge stehen in Title Case (Barker, Erlhofer, Sauro & Lewis, Soma, UN — beim deutschen Erlhofer-Titel bis hin zu „Und", „Für", „Die"), drei korrekt in Sentence Case (Nivedhitha, Shen, Vittuari). Im **Abgabe-Audit** ist das eine score-relevante Klasse; hier bleibt es Arbeitsliste.

## Teil-Check G – Quellentreue (Volltextabgleich)
- [PASS] **19 Zitationen geprüft · OK 19 · offen 0** (Details: `quellencheck.md`)

Alle fünf zuvor unprüfbaren Zitationen sind aufgelöst: Nivedhitha, Shen und die UN-Resolution liegen als Volltext in `sources/literatur/` und sind über Zotero verknüpft. Kein WORTLAUT-Befund, kein abweichendes wörtliches Zitat, keine verdächtige Seitenangabe, kein nicht gedeckter Claim. Die drei Befunde des Vorberichts sind verifiziert behoben:

| Vorbericht | Stelle | Stand heute |
|---|---|---|
| Befund 1 – Vittuari `[S. 1]`, 2× | `03_konzept.tex:5`, `01_kernergebnisse_und_ausblick.tex:5` | `[Kap.~1, Abs.~3]`, zusätzlich auch `01_ausgangslage_und_problem.tex:5` von `[S. 106]` umgestellt — alle drei Vittuari-Stellen laufen jetzt auf derselben Zählung |
| Befund 3 – Soma `[S. 9]` trägt den Teilnahme-Claim nicht | `04_community_und_feedback.tex:7` | `[S. 10--12]`; die drei übrigen Soma-Zitationen stehen korrekt weiter auf `[S. 9]` |
| Befund 4 – Autorennennung ohne Beleg | `06_evaluation_reflexion.tex:7` | „nach dem Befund von Soma et al." gestrichen, ersetzt durch `~\autoref{sec:community_und_feedback}` |

- Ungenutzte Bib-Einträge (Aufräumhinweis, kein Score-Abzug): `iso_9241_210` — Rest aus dem übersprungenen Befund 7.4.
- Volltexte ohne Bib-Verweis (Aufräumhinweis): Krug, *Don't Make Me Think* und Norman, *The Design of Everyday Things* liegen in `sources/literatur/`, werden aber nicht zitiert. Kein Mangel — nur Ablage aus der Vorprojekt-Recherche.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)
1. **Vittuari-Locator gegen die Verlagsfassung** | `01_ausgangslage_und_problem.tex:5`, `03_konzept.tex:5`, `01_kernergebnisse_und_ausblick.tex:5` — jeweils `[Kap.~1, Abs.~3]` | Erkennbar erledigt, wenn in der Verlagsfassung (*Sustainable Production and Consumption* 38, S. 104–114) die Seitenzahl der Drivers-/Levers-Definition feststeht und eingesetzt ist | Warum nicht durch mich: Hinterlegt ist die White-Rose-Preprint-Fassung mit eigener Zählung; ScienceDirect und das WUR-Repository sind über den Proxy nicht erreichbar. Der Kapitel-/Absatz-Locator ist die regelkonforme Zwischenlösung, keine Notlösung — nur ist eine Seitenzahl für den Prüfer bequemer.
2. **Prompt-Wortlaut der Mockup-Quellenzeilen** | `pages/appendix.tex`, `\quelle{}` zu `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_profil`, `fig:mockup_feed` | Erkennbar korrekt, wenn der zitierte Prompt wörtlich dem entspricht, was in Claude Design eingegeben wurde | Warum nicht durch mich: Der Foto-Platzhalter-Prompt wurde sinngemäß aus `sources/claude-design-nachbesserung.md` übernommen, nicht aus einem Eingabeprotokoll.
3. **Style Tile: manuelle Nachbearbeitung ja oder nein** | `pages/appendix.tex`, `\quelle{}` zu `fig:styletile` | Erkennbar korrekt, wenn die Zeile den Zusatz „Abbildung nachträglich manuell bearbeitet." trägt, sofern nachbearbeitet wurde (die vier Mockups tragen ihn) | Warum nicht durch mich: Dem Bild ist eine Nachbearbeitung nicht anzusehen.

## Claims
- Ungesicherte FACTUAL CLAIMS: **keine.** Sämtliche 19 Zitationen sind am Volltext geprüft und quittiert.
- Die Plattform-Tatsachenbehauptungen der Wettbewerbsanalyse laufen weiterhin über den Methodensatz (`01_wettbewerbsanalyse.tex:13`) und die sechs offiziellen Domains in der Quellenzeile — zulässig, weil die Analyse laut ZITIERREGEL eigene Sichtung ist.
- Fehlende OWN WORK-Markierungen: keine.
- Offene `% TODO-QUELLE:` / `% UNVERIFIED:`-Marker: keine.

## Punkteabzug im Detail
- Seitenumfang außerhalb der Vorgabe (Teil-Check D): **−10** (11 statt 7–10 Seiten, am gebauten PDF gemessen)
- Formalia-Verstoß, sichtbarer Randüberstand (Teil-Check A/D): **−8** (1 Vorkommen)
- Literaturverzeichnis-Verstoß, kaputtes Sonderzeichen im Rendering (Teil-Check F): **−5** (1 Regelverstoß-Klasse)
- **Summe: −23 → Score 77/100**

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: ABGEDECKT – alle drei Teilaufgaben ausgeführt, alle sechs Lieferobjekte vorhanden. Einziger Abzug an dieser Achse ist der Seitenumfang, den die IU-Richtlinien ausdrücklich als punktrelevant führen.
- **Prozess (25 %)**: ABGEDECKT – Vorgehen dokumentiert (`03_vorgehen_und_aufbau.tex`), reflektiert mit zwei konkreten Kursänderungen (`06_evaluation_reflexion.tex:7`), Grenzen in drei dreischichtigen Limitationen. Methodenfundierung des Beta-Tests (SEQ, Think-Aloud, Stichprobengröße) belegt.
- **Transfer (15 %)**: ABGEDECKT je Dimension – gesellschaftlich (SDG 12.3), wirtschaftlich (Freemium mit begründeter Trennlinie, Kooperationen), technisch (Funktionsübersicht, Datenvoraussetzung Rezeptbestand).
- **Kreativität (15 %)**: ABGEDECKT – expliziter Innovationsabsatz trennt Eigenes von Übernommenem; Vergleich zu Bestehendem über sechs Plattformen.
- **Dokumentation (10 %)**: **von SCHWACH auf ABGEDECKT verbessert** – dies war beim 28.07. die schwächste Achse mit drei Befunden. Alle Fundstellen sind jetzt am Volltext geprüft und nachschlagbar; die einzige verbleibende Schwäche ist das Ersatzzeichen im Literaturverzeichnis (Befund 3).
- **Ressourcen (10 %)**: ABGEDECKT – Phasenplanung mit Ressourcenspalte inkl. Daten, Puffer, Abhängigkeiten, zwei Risiken.

## Lieferobjekt-Abgleich
- [PASS] Alle sechs Lieferobjekte liegen vor: `tab:wettbewerbsvergleich`, Persona `tab:persona` (Anhang A), vier Mockups (Anhang B), Plattformname hergeleitet, `tab:funktionsuebersicht`, `tab:phasenplanung`.
- [PASS] Bildsichtung der gestalteten Artefakte am 28.07. durchgeführt und unverändert gültig (keine Bilddatei hat sich seither geändert): Wochenplan-Banner, Lesezeichen-Zähler, Challenge-Banner, freistehender Plus-Button, Foto-Platzhalter ohne Doppelpunkt. Befund 6.3 bleibt verifiziert behoben.

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)

### Befund 1 — Seitenumfang: 11 statt 7–10 Seiten (−10)
`main.pdf`, gedruckte Seiten 1–11. **Die elfte Seite trägt 66 Wörter** — den Schluss von Limitation 3, beginnend mit „Die dritte Grenze liegt in der Wettbewerbsanalyse."

Die Kürzung vom 28.07. brachte 60 Wörter und hat die Seite nicht gekippt. Der Bedarf liegt jetzt bei **rund 90–110 Wörtern**, damit der Umbruch mit Reserve fällt und nicht am nächsten Absatz wieder umschlägt. Die fünf Stellen des Vorberichts sind aufgebraucht; die freie Redundanz ist knapp geworden, aber nicht erschöpft. Reserve in dieser Reihenfolge, alle aus dem Redundanz-Befund in Teil-Check C:

1. **`06_evaluation_reflexion.tex:11`, zweite „Lehre" (~23 W.)** — „Zweitens lohnt sich eine bewusste Trennung zwischen literaturbasierten Hebeln und eigenen Konzeptentscheidungen …" Das ist inhaltlich derselbe Punkt wie der Schlusssatz des Fazits (`01_kernergebnisse_und_ausblick.tex:5`: „Diese Trennung macht kenntlich, dass die Differenzierung auf eigener Marktbeobachtung beruht …"). Nach der Arbeitsteilung Reflexion = **Vorgehen**, Fazit = **Ergebnis** gehört er ins Fazit, wo er schon steht. Beim Streichen „zwei Lehren" auf „eine Lehre" mitziehen — die erste Lehre (früh eingegrenzte Zielgruppe) ist eine echte Prozesslehre und bleibt.
2. **`06_evaluation_reflexion.tex:3`, zweiter Satz (~37 W.)** — die Aufzählung der abgedeckten Berichtsinhalte ist reine Verweis-Buchhaltung; jeder Punkt ist an seinem Ort belegt. Nicht ersatzlos streichen (die Aufgabenstellung fragt die Abdeckung explizit ab), sondern auf einen Satz ohne Einzelaufzählung verdichten, etwa „Auch die geforderten Berichtsinhalte sind abgedeckt: Zielgruppe, Funktionalitäten, UI/UX, Community-Building und Lebensmittel-Journaling." (~15 W., spart ~22).
3. **`06_evaluation_reflexion.tex:5`, letzter Satz (~19 W.)** — das Reichweitenrisiko des Rettungs-Feeds ist eine Limitation und steht im Reflexionskapitel. Entweder streichen oder als Halbsatz in Limitation 1 einfalten; nicht doppelt führen.
4. **`02_limitationen.tex:3` (~10 W.)** — „Betroffen ist nicht das Vorgehen, sondern die Geltung der Ergebnisse." Kontrastfigur ohne eigenen Begründungswert; der Folgesatz trägt die Mitigation allein.
5. **`06_evaluation_reflexion.tex:9`, letzter Satz (~8 W.)** — „Diese wurden anschließend in die vier UI/UX-Mockups übersetzt." lässt sich als Anschluss in den Vorsatz ziehen.

1–4 ergeben zusammen ~92 Wörter. **Danach zwingend neu bauen und die gedruckte Seitenzahl gegenprüfen** — Seitenumbrüche sind sprunghaft, die Wortzahl allein beweist nichts. Ankerwerte: 3.658 W. → 11 Seiten, 3.610 W. → weiterhin 11 Seiten.

Vorsorglich, falls auch das nicht reicht: Die nächste Stufe wäre eine Rückfrage zur Wettbewerbsanalyse (sechs Plattformen, bisher zweimal auf Wunsch bei sechs belassen, ~90 W. Ertrag). Das ist eine `[FREIGABE]`-Entscheidung, weil `02_limitationen.tex:7` die Sechser-Auswahl als Stärke führt und das Alleinstellungsmerkmal gegen leftovercooking formuliert ist — bitte nicht ohne Rückfrage angehen.

### Befund 2 — Sichtbarer Randüberstand unter der Wettbewerbstabelle (−8)
`chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:28`, die `\quelle{}`-Zeile unter `tab:wettbewerbsvergleich`. Der Build meldet **Overfull \hbox (11,54 pt too wide)**, also gut 4 mm Text, die rechts in den Rand ragen. Ursache: Die Domainkette „chefkoch.de, tiktok.com, restegourmet.de, …" enthält keine trennbaren Stellen, LuaTeX findet keinen Umbruchpunkt und schiebt über den Satzspiegel hinaus. Im PDF (S. 8) ist die erste Zeile der Quellenangabe messbar länger als jede Textzeile der Seite.

Ein Randüberstand ist ein Formfehler, den ein Prüfer beim Durchblättern sieht — und er sitzt ausgerechnet unter dem Lieferobjekt, dessen Nachvollziehbarkeit `sources/Anmerkungen vom Prüfer.md` ausdrücklich einfordert.

Fix, ohne eine einzige Aussage zu verlieren: Vor den Punkt der Domainnamen einen weichen Trennpunkt setzen (`\allowbreak` nach jedem Komma der Kette) **oder** — die sauberere Variante — die Aufzählung auf die sechs Plattformnamen ohne Top-Level-Domain kürzen und den Sichtungsweg als Halbsatz voranstellen: `\quelle{Eigene Darstellung auf Basis eigener Sichtung der Web-Auftritte und Apps von Chefkoch, TikTok, Restegourmet, Zu gut für die Tonne, leftovercooking und Foodsharing, Juli 2026.}` Das spart nebenbei ~6 Wörter und zahlt auf Befund 1 ein. **Nach dem Fix den Build wiederholen und prüfen, dass keine Overfull \hbox mehr im Log steht** — es ist derzeit die einzige im ganzen Dokument.

### Befund 3 — Ersatzzeichen im gedruckten Literaturverzeichnis (−5)
`references.bib:38` (`nivedhithaHowGreenSocial2024`) enthält im `title`-Feld den **Unicode-Bindestrich U+2010** statt eines normalen Hyphens: `Pro‐environmental`. Arial hat für dieses Zeichen keine Glyphe, LuaTeX meldet viermal „Missing character: There is no ‐ (U+2010)" und setzt an der Stelle nichts. Im gedruckten Verzeichnis (PDF-S. 17) steht deshalb:

> Nivedhitha, K. S., Pasricha, P. & Angelin Vilma, G. (2024). How green social network affordances **enhance pro?environmental behaviour?** …

Ein sichtbar kaputtes Zeichen im Literaturverzeichnis ist genau die Fundklasse, die die externe Prüfung ISSE01 neunmal getroffen hat. Der Wiley-Import bringt U+2010 mit; das `abstract`-Feld derselben Quelle ist voll davon, dort aber folgenlos, weil es nicht gesetzt wird.

Fix ausschließlich über Zotero (`references.bib` wird nicht von Hand editiert): Im Eintrag *How green social network affordances…* den Titel neu tippen bzw. den Bindestrich in „Pro-environmental" durch ein normales `-` ersetzen, dann BBT neu exportieren und einmal kompilieren. Erkennbar erledigt, wenn `grep -c "Missing character" build/main.log` **0** ergibt.

### Weitere Hinweise ohne Score-Wirkung
- **`kapitelplan.md:7`** trägt `**Gesamtwortzahl (Richtwert)**: 7–10 Seiten (B.Sc.)`. Die Zeile erwartet eine **Wortzahl**; `check_umfang.py` erkennt die Seitenangabe und **überspringt den Zielabgleich stillschweigend** — das Skript hat den Umfang deshalb nie von sich aus als „über Ziel" gemeldet. Auf `3750` (10 Seiten × ~375 W.) setzen, dann greift die automatische Warnung.
- **Tabellenwertung leftovercooking** (`01_wettbewerbsanalyse.tex:13` gegen `:9`) – unverändert offen aus dem Vorbericht, weiter kein FAIL. Fix in einem Halbsatz, falls gewünscht: in `:13` ergänzen, dass eine einseitige Creator-Following-Ebene ohne wechselseitigen Austausch als „mittel" gilt. **Nicht** stattdessen die Zelle auf „schwach" ziehen.
- **Werkzeug-Befunde** aus dem Vorbericht bleiben in `SKILL-ANPASSUNGEN.md` dokumentiert (P1-1, P1-2, P2-1, P2-2, P2-3, P3-1). Neu hinzugekommen wäre: Kein Check liest das Build-Log auf „Missing character" — Befund 3 wäre sonst schon am 28.07. sichtbar gewesen.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- Eidesstattliche Erklärung elektronisch über myCampus abgeben — **ohne sie nimmt Turnitin die Einreichung nicht an**
- Einreichungs-Anleitung im myCampus-Kurs lesen
- `pages/meta.tex`: `\ModuleCode` und `\MatrikelNr` ausfüllen (stehen sonst als Platzhalter auf dem Titelblatt und in den PDF-Metadaten)
- Nach der Kürzung neu bauen und die gedruckte Seitenzahl des Textteils gegenprüfen (Ziel: 10 oder weniger)
- Vittuari-Locator am Verlags-PDF auf eine echte Seitenzahl umstellen, falls die Fassung beschaffbar wird („Bitte manuell prüfen" Punkt 1)
- `check_bib_hygiene.py`-Arbeitsliste in Zotero abarbeiten (U+2010 im Nivedhitha-Titel zuerst, dann urldate, URL neben DOI, Sentence Case bei den fünf Title-Case-Einträgen, Sprachfeld, Verlagsorte, Artikelnummern) und neu exportieren — die von Hand eingetragenen `file`-Pfade und die vier Runde-7-Einträge müssen vorher in Zotero angelegt sein, sonst gehen sie verloren
- LanguageTool-Durchgang lokal über den Gesamttext
- Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)
- Prompt-Wortlaut und Nachbearbeitungs-Zusatz der Abbildungs-Quellenzeilen prüfen („Bitte manuell prüfen" Punkte 2 und 3)
