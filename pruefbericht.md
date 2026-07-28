# Prüfbericht – Projektbericht

**Datum**: 28.07.2026 · **Geprüfter Stand**: alle Kapitel, Commit `1f188dc` (nach Kürzungsrunde 1+2) · **Audit-Typ**: Delta-Re-Audit (Teil-Check G nach Nutzer-Einwand vollständig nachgeholt)
**Score: 43/100 – nicht in diesem Stand einreichen**

> Der Score des letzten Delta-Re-Audits (100/100, 26.07.) ist überholt: Er bezog sich auf den ungekürzten Textstand, erhob den Seitenumfang nur als Schätzung und kannte Teil-Check G noch nicht. Beide Prüfungen laufen hier erstmals wirklich — sie erzeugen sämtliche Abzüge. **Der Fließtext ist gegenüber dem 26.07. nicht schlechter geworden**; die Argumentation, die Struktur und alle Pflichtschichten sind intakt.
>
> **Einordnung des Scores.** Alle fünf Abzüge sind mechanischer Natur: drei falsche Seitenangaben, rund 100 Wörter zu viel, eine fehlende Zitation, drei fehlende Volltexte. Kein Befund betrifft These, Argumentation oder Aufbau, keiner verlangt Umschreiben. Nach Befund 1–4 liegt der Score bei **85/100** (die verbleibenden −15 hängen allein an den drei Quellen ohne Volltext, Befund 5). Aufwand: eine kurze Schreib-Session plus ein Zotero-Schritt.

**Delta-Umfang**: alle 15 Kapiteldateien (praktisch jede Datei hat sich seit `1843fa8` geändert), `pages/appendix.tex`, `pages/acronyms.tex`, `pages/chapters.tex`, `main.tex`, `references.bib`; dazu die Mockups per Bildsichtung, alle sechs Prüfskripte und das gebaute `main.pdf`.

## Teil-Check A – Formalia
- [FAIL] **Zitationen** – ein Fund, siehe Befund 4. `check_bib_keys.py`: alle genutzten Keys valide, `iso_9241_210` ungenutzt (Aufräumhinweis). `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**, 58 HINWEIS.
- [PASS] Eigene Werke – `\quelle{Eigene Darstellung.}` unter beiden Eigen-Tabellen, `\quelle{Erstellt mit dem Prompt … durch Anthropic, 2026 …}` unter allen fünf KI-Abbildungen, Beschriftung jeweils über dem Bild, kein `\cite` auf eigene Werke.
- [PASS] Pronomen – kein Ich/Wir, kein „Projektgruppe" (Einzelarbeit laut `aufgabe.md`).
- [PASS] LaTeX-Format – `\enquote{}` durchgängig, Floats mit `[H]`, Caption vor `\label`, kein `\underline`, `~\autoref` durchgängig.
- [PASS mit Hinweis] Akronyme – BMEL, SDG, MVP, SEQ sauber über `\ac{}`. UI/UX werden in `03_konzept.tex:34` einmal ausgeschrieben eingeführt, danach als Klartext weitergeführt statt über `\ac{}`; „KI" bleibt ohne Eintrag. Beides ist seit dem 23.07. bewusst als optional eingestuft, kein Regelverstoß.
- [PASS] Cross-References & Labels – alle 5 `fig:`, 4 `tab:` und 15 `sec:` im PDF aufgelöst, keine doppelten Labels.
- [PASS] Anti-KI-Stil – zwei TRIAS-Hinweise (`03_konzept.tex`, `05_phasenplanung.tex`, je 4×), beide sachlich gedeckt (drei Hauptbereiche, drei Kernfunktionen). Keine Floskel-Öffner, keine Gedankenstrich-Häufung, keine rhetorischen Fragen.
- [PASS mit Hinweis] Verständlichkeit – 20 SATZLAENGE-Hinweise, davon 3 reine Tabellen-Artefakte (der Parser liest `tabularx`-Zeilen als einen Satz). `05_phasenplanung.tex` (~30 W./Satz) und `07_iteratives_design.tex` (~27) liegen über dem Richtwert 22; beide Dateien haben in den Kürzungsrunden Sätze zusammengezogen. Unter dem Häufungs-Deckel (>3 in *einem* Kapitel wären score-relevant, es verteilt sich über sieben Dateien), daher kein Abzug — aber die Stelle, an der der nächste Durchgang gegensteuern sollte.

## Teil-Check B – Argumentationsqualität (Pflicht-Punkte `typen/projektbericht.md`)
- [PASS] These erkennbar – Leitfrage (Konzeption einer Zero-Waste-Plattform) und These (Marktlücke liegt in der Kombination Reste-Matching + wechselseitige Community) sind getrennt formuliert.
- [PASS] Marktlücke in der Einleitung – `01_ausgangslage_und_problem.tex:7`.
- [PASS] Aktualität/Zeitbezug – SDG 12.3 mit Zieljahr 2030, Sichtung Juli 2026.
- [PASS] Gegenargumente reflektiert & entkräftet – der gewichtigste Einwand („reine Community-Plattform genügt") wird in `01_wettbewerbsanalyse.tex:34` benannt und entkräftet; die SDG-vs.-Nische-Spannung in `06_evaluation_reflexion.tex:5` aufgelöst; die Grenzen der Soma-Studie in `03_konzept.tex:11` selbst benannt.
- [PASS] Syntheseleistung je Hauptkapitel – Kap. 2 endet auf Zielerreichung + Reflexion, Kap. 3 auf Kernergebnis + Grenzen.
- [PASS] Limitationen dreischichtig – alle drei Limitationen tragen warum · Mitigation · Folgeschritt (nachgezählt, `02_limitationen.tex:3,5,7`). Die Mitigationsschicht war am 24.07. schon einmal einer Kürzung zum Opfer gefallen; sie hat beide Kürzungsrunden dieses Mal überstanden.
- [N.A.] Ergebnisse ≠ Interpretation – nur empirische Seminararbeit.
- [PASS] Typspezifisch (Projektbericht) – Phasenplanung als Tabelle mit Zeitrahmen, Ressourcen, Abhängigkeiten und zwei Risiken; Prozessreflexion mit zwei konkreten Kursänderungen; Entstehungsgeschichte als Abfolge in `06_evaluation_reflexion.tex:9`.
- [PASS] Leitfragen aus `aufgabe.md` beantwortet – alle drei Teilaufgaben mit eigener Fundstelle; Teilaufgabe 3 seit Runde 5 mit eigener Subsection.
- [PASS] Abhakliste – alle sieben Schlüsselbegriffe per Grep belegt, inkl. begründetem Verzicht auf Event-Kalender (`03_konzept.tex:36`) und auf Gruppen/Foren (`04_community_und_feedback.tex:7`).
- [PASS] Dimensionsabgleich Bewertungskriterien – siehe Abschnitt „Bewertungsschwerpunkte".

## Teil-Check C – Struktur
- [PASS] ½-Seiten-Regel – kein HALBSEITE-Hinweis; die drei Grenzfälle (`02_zielsetzung`, `03_vorgehen`, `07_iteratives_design`) liegen weiter über der Schwelle.
- [PASS] Max. 3 Kapitelstufen · 2–3 Sätze zwischen Section und erster Subsection · mind. 2 Unterpunkte je Kapitel.
- [PASS] Front-/Backmatter – Abbildungs- (5) und Tabellenverzeichnis (4) aktiv, Anhangsverzeichnis bei drei Anhängen aktiv, Anhänge A/B/C gekennzeichnet, jeder Anhang mindestens einmal im Text referenziert (A in `02_zielgruppe.tex:9`, B und C in `03_konzept.tex:34`).
- [PASS] Outline-Check – Gerüst unverändert gegenüber `kapitelplan.md`: 3 Kapitel, 12 Subsections.
- [PASS] Roter Faden – Querverweise stichprobenartig semantisch geprüft (`sec:phasenplanung` aus `03_konzept.tex:7` und `02_limitationen.tex:3` zeigen tatsächlich auf den Beta-Test; `sec:wettbewerbsanalyse` aus dem Fazit auf die Lückenbeschreibung). Zählangaben nachgezählt: „sechs Vertreter aus drei Plattform-Kategorien … ein bis drei Vertreter" stimmt (2/3/1), „zwei Risiken" stimmt, „zwei Lehren" stimmt, „zwei Befunde aus der Nudge-Forschung" stimmt (Barker, Nivedhitha), „drei Hauptbereiche" stimmt. Keine Kürzungsregression gefunden.
- [PASS] Akteurskonsistenz – keine Ausschließlichkeitsregel wird später gebrochen; die Freemium-Trennlinie (Community kostenlos, Komfort kostenpflichtig) ist in allen betroffenen Kapiteln gleich beschrieben.
- [PASS] Redundanz – die in der Kürzungsrunde entfernten Dritt- und Viertnennungen sind nicht zurückgekehrt; die leftovercooking-Einordnung steht jetzt einmal (Wettbewerbsanalyse), das Fazit greift sie nicht mehr auf.
- [PASS] Zeitlinien-Konsistenz Entwurf ↔ Iteration – `07_iteratives_design.tex:3` weist die bereits gelaufenen Mockup-Schleifen aus, `03_konzept.tex` beschreibt durchgehend den finalen Stand; der Darstellungsstand ist einheitlich.
- [Hinweis, kein FAIL] Tabellenwertung `tab:wettbewerbsvergleich`, Spalte „Kommunikation \& Community" – siehe Befund 6.

## Teil-Check D – Build
Kein lokaler Build möglich: `lualatex`, `latexmk`, `biber` und `pdflatex` sind in dieser Session-Umgebung **nicht installiert** (anders als am 28.07. vormittags). Geprüft wurde stattdessen das im Repository liegende `main.pdf` — es ist **aktuell**: vier Textproben aus dem letzten Kürzungs-Commit `e6e024f` stehen im PDF, die jeweils ersetzten Vorgängerformulierungen nicht.
- [PASS, aus dem vorhandenen PDF] Kompiliert fehlerfrei – 24 Seiten, alle Verzeichnisse und Anhänge gesetzt.
- [PASS, aus dem vorhandenen PDF] Keine undefined references/citations, keine fehlenden Bilder, keine doppelten Labels – alle `\autoref`-Ziele und alle fünf Abbildungen aufgelöst.
- [FAIL] **Seitenumfang Textteil: 11 Seiten von 7–10.** „1 Einleitung" beginnt auf PDF-Seite 6 (gedruckt 1), das Literaturverzeichnis steht auf PDF-Seite 17 (gedruckt 12) — Textteil also gedruckte Seiten 1–11. Siehe Befund 2.

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)
- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [FAIL] Umfang im Soll – Spiegel aus Teil-Check D (11 von 7–10)
- [OFFEN] `pages/meta.tex`: `\ModuleCode` und `\MatrikelNr` sind noch Platzhalter und erscheinen so auf dem Titelblatt und in den PDF-Metadaten
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)
- [ERINNERT] LanguageTool-Durchgang lokal über den Gesamttext

## Teil-Check F – Literaturverzeichnis
Im Delta-Re-Audit nicht als Vollprüfung vorgesehen; `check_bib_hygiene.py` lief trotzdem mit: **9 Einträge, 28 Hinweise**, keine neue Klasse gegenüber dem letzten Stand. Sammelbild: `urldate` gesetzt (6×), DOI **und** URL gesetzt (5×), Title-Case-Verdacht (7×), fehlendes Sprachfeld (4×), Verlagsort bei drei Büchern, zwei Artikelnummern im `pages`-Feld. Korrektur ausschließlich über Zotero + BBT-Re-Export — Arbeitsliste steht in der Skriptausgabe.

## Teil-Check G – Quellentreue (Volltextabgleich)
- [FAIL] **19 Zitationen geprüft · OK 10 · offen 9** (Details: `quellencheck.md`)

**Vorbemerkung: Der erste Durchgang dieses Audits war falsch.** Das Skript meldete für Barker, Soma und Vittuari „kein PDF-Snapshot im file-Feld". Tatsächlich war das `file`-Feld gesetzt — es zeigte auf die Zotero-Ablage des Nutzers (`/home/normi/Zotero/storage/…`), die es in dieser Umgebung nicht gibt, während die Volltexte unter `sources/literatur/` bereitlagen. Ich habe die Skriptaussage übernommen, statt im Ordner nachzusehen, und daraus einen −15-Befund gebaut. Nach dem Nutzer-Einwand wurden alle drei am Volltext geprüft. Ursache und Gegenmaßnahmen: `SKILL-ANPASSUNGEN.md` → P1-1 und P1-2.

**Verifiziert und mit OK quittiert (10 Zitationen, alle am Volltext):**
- `somaFoodWasteReduction2020` [S. 9], 3×. Tabelle 3 auf S. 9 trägt die Zahlen exakt: Vielspieler:innen (11–12 Wochen, n = 14) 1,37 → 0,67 kg/Woche/Person = **51 %**, Wenigspieler:innen (0–10 Wochen, n = 12) 1,64 → 1,00 = **39 %**, Mann-Whitney U bei Audit 2 **p = 0,030** (bei Audit 1 noch p = 0,200). Prozentwerte, Zwölf-Wochen-Rahmen und Signifikanzaussage in `03_konzept.tex:11` sind damit vollständig gedeckt — die Quelle selbst schreibt nur „about 50 %", die genauere Angabe ist aus der Tabelle korrekt hergeleitet.
- `barkerWhatNudgeTechniques2021` [S. 10], 4×. Die vier als reliabel eingestuften Studien stehen auf S. 10, darunter Shearer et al. mit einem „visual prompt nudge reminder" und statistisch signifikantem Effekt; das Abstract nennt Reminders ausdrücklich unter den wirksamen Nudge-Typen. Gedeckt.
- `nielsenUsabilityEngineering1993` Kap. 6.8 (PDF-S. 207), `sauroLewisQuantifying2016` Kap. 8 (PDF-S. 192), `erlhoferWebsiteKonzeptionUndRelaunch2017` Kap. 17.2.2 — wie zuvor geprüft. Die SEQ-Erfolgsschwelle steht korrekt als **eigene** Festlegung und wird der Quelle nicht zugeschrieben.

**Offene Befunde (9 Zitationen):**
- **Falsche Seitenangabe, 3 Vorkommen** — siehe Befund 1 und Befund 3.
- **Nicht prüfbare Quelle ohne Volltext, 3 Quellen** (`nivedhithaHowGreenSocial2024`, `shenInfluenceOsmosisSocial2023`, `unTransformingOutWorld2030Agenda`, zusammen 5 Zitationen) — diese drei Bib-Einträge haben **kein** `file`-Feld, und der Live-Abruf scheitert: Wiley und Elsevier hinter Bezahlschranken, die UN-Resolution ohne Snapshot. Siehe Befund 5.
- Kein WORTLAUT-Befund, kein abweichendes wörtliches Zitat, kein nicht gedeckter Inhalts-Claim in den zehn geprüften Zitationen.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)
1. **Vittuari, Seitenangabe `[S. 106]`** | `01_ausgangslage_und_problem.tex:5` gegen die Verlagsfassung *Sustainable Production and Consumption* 38, S. 104–114 | Erkennbar korrekt, wenn auf der gedruckten S. 106 die Aussage steht, der Großteil vermeidbarer Verschwendung entstehe in privaten Haushalten | Warum nicht durch mich: hinterlegt ist die White-Rose-Preprint-Fassung mit eigener Zählung (23 Seiten). Die Aussage ist inhaltlich gedeckt — der Preprint nennt in der Einleitung „household and food service sectors accounted for about 65 % of food losses and waste (Eurostat, 2022)" —, nur ist das dort die zweite Textseite, was in der Verlagsfassung eher S. 104–105 entspricht als 106.
2. **Drei Quellen ohne Volltext** | `references.bib`: `nivedhithaHowGreenSocial2024`, `shenInfluenceOsmosisSocial2023`, `unTransformingOutWorld2030Agenda` — betroffene Stellen namentlich in `quellencheck.md` | Erkennbar erledigt, wenn jeder Eintrag ein auflösbares `file`-Feld trägt und `check_quellentreue.py` keine Zeile „LIVE PRÜFEN" mehr ausgibt | Warum nicht durch mich: kein `file`-Feld gesetzt, und der Live-Abruf scheitert — Wiley und Elsevier hinter Bezahlschranken, für die UN-Resolution existiert kein Snapshot.
3. **Prompt-Wortlaut der Mockup-Quellenzeilen** | `pages/appendix.tex`, `\quelle{}`-Zeilen zu `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_profil`, `fig:mockup_feed` | Erkennbar korrekt, wenn der zitierte Prompt wörtlich dem entspricht, was in Claude Design eingegeben wurde | Warum nicht durch mich: der Foto-Platzhalter-Prompt wurde sinngemäß aus `sources/claude-design-nachbesserung.md` übernommen, nicht aus einem Eingabeprotokoll.
4. **Style Tile: manuelle Nachbearbeitung ja oder nein** | `pages/appendix.tex`, `\quelle{}` zu `fig:styletile` | Erkennbar korrekt, wenn die Zeile den Zusatz „Abbildung nachträglich manuell bearbeitet." trägt, sofern nachbearbeitet wurde (die vier Mockups tragen ihn) | Warum nicht durch mich: dem Bild ist eine Nachbearbeitung nicht anzusehen.

## Claims
- Ungesicherte FACTUAL CLAIMS: keine. Die beiden Zahlenaussagen, die am weitesten tragen — 51 %/39 % Reduktion bei Viel- gegen Wenigspieler:innen und die Wirksamkeit von Reminders — sind in diesem Lauf am Volltext bestätigt worden.
- Die Plattform-Tatsachenbehauptungen der Wettbewerbsanalyse sind seit Runde 6 über den Methodensatz (`:13`) und die sechs offiziellen Domains ausgewiesen — zulässig, weil die Analyse laut ZITIERREGEL eigene Sichtung ist.
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge (Aufräumhinweis, kein Score-Abzug): `iso_9241_210` — Rest aus dem übersprungenen Befund 7.4.
- Offene `% TODO-QUELLE:` / `% UNVERIFIED:`-Marker: keine.

## Punkteabzug im Detail
- Falsche Seitenangabe (Teil-Check G): **−24** (3 Vorkommen × −8, Deckel −32) — Vittuari `[S. 1]` zweimal, Soma `[S. 9]` einmal
- Nicht prüfbare Quelle ohne Volltext (Teil-Check G): **−15** (3 Quellen × −5, Deckel −15)
- Seitenumfang außerhalb der Vorgabe: **−10** (11 statt 7–10 Seiten)
- Formalia-Verstoß (Zitation): **−8** (1 Vorkommen)
- **Summe: −57 → Score 43/100**

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: ABGEDECKT – alle drei Teilaufgaben ausgeführt, alle sechs Lieferobjekte vorhanden. Abzüge an dieser Achse: Seitenumfang, den die IU-Richtlinien ausdrücklich als punktrelevant führen.
- **Prozess (25 %)**: ABGEDECKT – Vorgehen dokumentiert (`03_vorgehen_und_aufbau.tex`), reflektiert mit zwei konkreten Kursänderungen (`06_evaluation_reflexion.tex:7`), Grenzen in drei Limitationen. Die Methodenfundierung des Beta-Tests (SEQ, Think-Aloud, Stichprobengröße) stärkt diese Achse deutlich gegenüber dem 26.07.
- **Transfer (15 %)**: ABGEDECKT je Dimension – gesellschaftlich (SDG 12.3), wirtschaftlich (Freemium mit begründeter Trennlinie, Kooperationen), technisch (Funktionsübersicht, Datenvoraussetzung Rezeptbestand).
- **Kreativität (15 %)**: ABGEDECKT – expliziter Innovationsabsatz (`03_konzept.tex:32`) trennt Eigenes von Übernommenem; Vergleich zu Bestehendem über sechs Plattformen.
- **Dokumentation (10 %)**: SCHWACH – hier sitzen drei der fünf Befunde. Zwei Zitationen zeigen auf eine Seite, die es in der zitierten Publikation nicht gibt (Befund 1), eine Seitenangabe trägt den Claim nicht (Befund 3), ein Autorenbezug hat gar keinen Beleg (Befund 4). Inhaltlich ist alles gedeckt — nachschlagen kann der Prüfer es an drei Stellen trotzdem nicht.
- **Ressourcen (10 %)**: ABGEDECKT – Phasenplanung mit Ressourcenspalte inkl. Daten, Puffer, Abhängigkeiten, zwei Risiken.

## Lieferobjekt-Abgleich
- [PASS] Alle sechs Lieferobjekte liegen vor: `tab:wettbewerbsvergleich`, Persona `tab:persona` (Anhang A), vier Mockups (Anhang B), Plattformname hergeleitet, `tab:funktionsuebersicht`, `tab:phasenplanung`.
- [PASS] **Bildsichtung der gestalteten Artefakte** (nicht nur Existenzprüfung): Die Startseite zeigt das Wochenplan-Banner („Wochenplan · Heute: Brokkoli-Suppe") — die Textaussage in `03_konzept.tex:13` („über die Startseite erreichbar") ist damit gedeckt, die seit dem 24.07. offene Mockup-Lücke geschlossen. Das Lesezeichen-Icon mit Zähler deckt „Gespeicherte Rezepte". Der Rettungs-Feed zeigt Challenge-Banner mit Rangliste, Reste-Tag ohne Präfix, Kommentar- und Bewertungselemente sowie den Plus-Button — dieser steht frei über dem Beitragsbild und überlappt die Aktionsleiste nicht mehr (**Befund 6.3 verifiziert behoben**). Die „Foto"-Platzhalter tragen keinen Doppelpunkt mehr.

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)

### Befund 1 — Vittuari zweimal auf eine Seite zitiert, die es nicht gibt (−16)
`chapters/02_durchfuehrung/03_konzept.tex:5` und `chapters/03_fazit/01_kernergebnisse_und_ausblick.tex:5`, beide `\parencite[S. 1]{vittuariHowReduceConsumer2023}`.
Der Bib-Eintrag weist die Arbeit als *Sustainable Production and Consumption* **38, S. 104–114** aus. Eine Seite 1 existiert dort nicht. Die „1" stammt aus der White-Rose-Preprint-Fassung, deren Fließtext bei 1 beginnt — und genau die liegt als PDF vor. Der Text zitiert also aus zwei unvereinbaren Zählungen: `[S. 1]` aus dem Preprint, `[S. 106]` in der Einleitung aus der Verlagsfassung.
Inhaltlich ist die Stelle einwandfrei: Das Skript findet den Drivers-/Levers-Wortlaut exakt, und die Definition steht in der Einleitung des Preprints („Under drivers, we understand the factors that impact behaviour … As levers, we consider those aspects of drivers that can be leveraged to influence …"). Es ist ein reiner Verweisfehler — aber einer, den ein Prüfer beim Nachschlagen sofort bemerkt, und Nachvollziehbarkeit ist genau das, was `sources/Anmerkungen vom Prüfer.md` einfordert.
Fix: In der Verlagsfassung liegt die Introduction auf S. 104–105; die Drivers-/Levers-Definition steht dort im ersten Abschnitt. Beide Stellen auf `[S. 105]` umstellen und **am Verlags-PDF gegenprüfen**. Steht die Verlagsfassung nicht zur Verfügung, stattdessen `[Abs. 1]` setzen — eine unauffindbare Seitenzahl ist schlechter als gar keine.

### Befund 2 — Seitenumfang: 11 statt 7–10 Seiten (−10)
`main.pdf`, gedruckte Seiten 1–11. **Die elfte Seite trägt nur 90 Wörter** (Ende von Limitation 3, ab „funktionsfähigen Prototyp folgen."). Es fehlen also rund 90–120 Wörter — ein einziger sauberer Kürzungsschritt genügt.
Der Umfang ist kein kosmetisches Kriterium: `aufgabe.md:19` nennt 7–10 Seiten, und die IU-Richtlinien weisen die Überschreitung ausdrücklich als punktrelevant aus.
Reserve, ohne Substanz zu verlieren, in dieser Reihenfolge:
1. `01_wettbewerbsanalyse.tex:5` — der TikTok-Absatz erklärt in einem eigenen Satz, dass TikTok stellvertretend für Instagram steht. Seit Runde 5 durch die Aufgabenstellung gefordert, ließe sich aber als Halbsatz im ersten Satz unterbringen (~15 W.).
2. `03_konzept.tex:9` — „Diese Mechanik greift zwei Befunde aus der Nudge-Forschung auf, also der Forschung zu verhaltenslenkenden Gestaltungsimpulsen." Die Definition steht als Einschub, obwohl „Nudge" im Text bereits geführt wird (~12 W.).
3. `05_phasenplanung.tex:21` — „weil sonst Entscheidungen zur Bedienführung nachträglich korrigiert werden müssten" begründet eine selbsterklärende Abhängigkeit (~10 W.).
4. `06_evaluation_reflexion.tex:3` — „User Interface und User Experience über die Mockups in Anhang B" ließe sich auf „UI/UX in Anhang B" verkürzen (~8 W.).
5. `02_zielgruppe.tex:7` — der Kontrastsatz („anders als für Hobbyköch:innen, die vor allem neue Gerichte entdecken wollen") wiederholt die Verengungsbegründung aus `02_zielsetzung_und_verengung.tex:5` (~20 W.).
**Danach zwingend neu bauen und die gedruckte Seitenzahl gegenprüfen** — Seitenumbrüche sind sprunghaft, die Wortzahl allein beweist nichts. Ankerwert: 3.658 Wörter ergeben 11 Seiten.

### Befund 3 — Soma `[S. 9]` trägt den Teilnahme-Claim nicht (−8)
`chapters/02_durchfuehrung/04_community_und_feedback.tex:7`: „Die Entscheidung stützt sich auf einen Befund von `\textcite[S. 9]{somaFoodWasteReduction2020}`: In ihrer Studie erreichten sowohl eine passive Informationsgruppe als auch eine Gamification-Gruppe deutlich höhere Teilnahme als eine Gruppe, die auf klassische Community-Diskussion setzte."
Die **Aussage ist richtig** — das Abstract der Studie formuliert sie fast wörtlich: „The passive and gamification groups had similarly high levels of participation, while participation in the community group was very low." Nur steht sie nicht auf S. 9. Dort liegt Tabelle 3 mit den Abfallmengen von Viel- und Wenigspieler:innen; die Teilnahmequoten stehen in Abschnitt 3.2 auf **S. 10–12** (Information: nur 16 % nutzten kein Material · Community: 16 % besuchten überhaupt einen Workshop, in drei von acht Workshops erschien ein einziger Haushalt · Game: 61 % spielten alle zwölf Level).
Dieser Befund wiegt schwerer als eine bloße Zahlendreher-Korrektur: Die Stelle trägt die **Begründung für den Verzicht auf Forum und Gruppen**, also eine Konzeptentscheidung, die die Aufgabenstellung ausdrücklich als Schlüsselbegriff abfragt.
Fix: `[S. 9]` → `[S. 10--12]`. Die drei anderen Soma-Zitationen bleiben bei `[S. 9]`, die sind dort korrekt.

### Befund 4 — Autorennennung ohne Beleg (−8)
`chapters/02_durchfuehrung/06_evaluation_reflexion.tex:7`: „Der zunächst naheliegende Community-Zuschnitt mit Forum und Nutzergruppen wich **nach dem Befund von Soma et al.** zeitlich begrenzten Challenges."
Der Autorname steht im Fließtext, aber ohne `\textcite`, ohne Jahr und ohne Stellenangabe. APA und der IU-Zitierleitfaden verlangen bei namentlicher Bezugnahme Autor **und** Jahr; wer nur dieses Kapitel liest, findet die Quelle nicht.
Fix: `… wich nach dem Befund von \textcite[S. 10--12]{somaFoodWasteReduction2020} zeitlich begrenzten Challenges` — oder, falls der Umfang drückt, den Namen streichen und rein auf `~\autoref{sec:community_und_feedback}` verweisen. Die zweite Variante ist die kürzere und im Reflexionskapitel die sauberere.

### Befund 5 — Drei Quellen ohne Volltext (−15, gedeckelt)
`nivedhithaHowGreenSocial2024` (Wiley), `shenInfluenceOsmosisSocial2023` (Elsevier), `unTransformingOutWorld2030Agenda` — zusammen fünf Zitationen. Diese drei Einträge haben **kein** `file`-Feld; Wiley und Elsevier liegen hinter Bezahlschranken, für die UN-Resolution existiert kein Snapshot. Kein Verdacht auf Falschzitat, sondern fehlende Nachweisbarkeit.
Auflage: Volltext bzw. PDF-Snapshot unter `sources/literatur/` ablegen und den Pfad **über Zotero** ins `file`-Feld ziehen, dann `check_quellentreue.py` erneut fahren. Die zehn bereits quittierten Zitationen prüft der inkrementelle Lauf nicht erneut.

### Befund 6 — Tabellenwertung leftovercooking, Spalte „Kommunikation \& Community" (kosmetisch, kein Score-Abzug)
`01_wettbewerbsanalyse.tex:13` definiert das Kriterium eng: „Bei Kommunikation \& Community zählt **nur tatsächlicher Austausch zwischen Nutzer:innen**." Der leftovercooking-Absatz (`:9`) stellt fest, ein solcher Austausch sei „nicht belegt", die Community-Ebene bleibe „auf das Verfolgen von Creator-Inhalten beschränkt" — die Zelle steht trotzdem auf „mittel", während Restegourmet mit derselben Begründung auf „schwach" steht.
Warum trotzdem kein FAIL: Die Wertung geht in die **selbstkritische** Richtung — sie stärkt den nächsten Wettbewerber, statt die eigene These zu schonen, und der Absatz erklärt sie ausführlich. Der Konflikt entstand erst, als Runde 5 die Kriteriendefinition verengte, nachdem die Zelle in Runde 2 (GS-1) gesetzt worden war; die Propagation blieb aus.
Fix in einem Halbsatz, falls gewünscht: in `:13` ergänzen, dass eine einseitige Creator-Following-Ebene ohne wechselseitigen Austausch als „mittel" gewertet wird. **Nicht** stattdessen die Zelle auf „schwach" ziehen — das würde den eigenen Alleinstellungsanspruch bequemer machen, als die Sichtung hergibt.

### Werkzeug-Befunde (kein Textbefund, dokumentiert in `SKILL-ANPASSUNGEN.md`)
- **P1-1**: `check_quellentreue.py` meldet ein gesetztes, aber nicht auflösbares `file`-Feld wortgleich wie ein fehlendes. Ursache des Fehlbefunds im ersten Durchgang dieses Audits.
- **P1-2**: Auditregel — vor einem „Quelle nicht prüfbar"-Befund erst `ls sources/literatur/`.
- **P2-1**: Kein Check vergleicht die Stellenangabe mit dem `pages`-Feld. Genau das hätte Befund 1 sofort gefunden.
- **P2-2**: Teil-Check D braucht den dokumentierten Weg über ein vorhandenes, auf Aktualität geprüftes PDF.
- **P3-1**: `check_formalia.py` meldet „Anhangsverzeichnis aktiv bei 0 Anhang", obwohl drei Anhänge existieren — die Zählung scheitert am `~` in `\section*{Anhang~A: …}`.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- Eidesstattliche Erklärung elektronisch über myCampus abgeben — **ohne sie nimmt Turnitin die Einreichung nicht an**
- Einreichungs-Anleitung im myCampus-Kurs lesen
- `pages/meta.tex`: `\ModuleCode` und `\MatrikelNr` ausfüllen (stehen sonst als Platzhalter auf dem Titelblatt)
- Lokalen Build nach der Kürzung fahren und die gedruckte Seitenzahl des Textteils gegenprüfen (Ziel: 10 oder weniger)
- Vittuari-Seitenangaben am **Verlags-PDF** gegenprüfen (Befund 1 und „Bitte manuell prüfen" Punkt 1)
- Volltexte der drei Quellen aus Befund 5 über Zotero nachtragen, dann `check_quellentreue.py` erneut fahren
- `check_bib_hygiene.py`-Arbeitsliste in Zotero abarbeiten (urldate, URL neben DOI, Sentence Case, Sprachfeld, Verlagsorte, Artikelnummern) und neu exportieren — dabei gehen die von Hand eingetragenen `file`-Pfade und die vier Runde-7-Einträge verloren, sie müssen vorher in Zotero angelegt sein
- LanguageTool-Durchgang lokal über den Gesamttext
- Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)
- Prompt-Wortlaut und Nachbearbeitungs-Zusatz der Abbildungs-Quellenzeilen prüfen („Bitte manuell prüfen" Punkte 3 und 4)
