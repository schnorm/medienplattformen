# Prüfbericht – Projektbericht

**Datum**: 28.07.2026 · **Geprüfter Stand**: alle Kapitel, Commit `1f188dc` (nach Kürzungsrunde 1+2) · **Audit-Typ**: Delta-Re-Audit
**Score: 67/100 – Überarbeitung empfohlen**

> Der Score des letzten Delta-Re-Audits (100/100, 26.07.) ist überholt: Er bezog sich auf den ungekürzten Textstand und erhob den Seitenumfang nur als Schätzung. Dieser Lauf misst ihn erstmals am gebauten PDF und fährt erstmals Teil-Check G (Volltextabgleich) über alle Zitationen. Beide Erweiterungen erzeugen die Abzüge — der Fließtext selbst ist gegenüber dem 26.07. nicht schlechter geworden.

**Delta-Umfang**: alle 15 Kapiteldateien (praktisch jede Datei hat sich seit `1843fa8` geändert), `pages/appendix.tex`, `pages/acronyms.tex`, `pages/chapters.tex`, `main.tex`, `references.bib`; dazu die Mockups per Bildsichtung, alle sechs Prüfskripte und das gebaute `main.pdf`.

## Teil-Check A – Formalia
- [FAIL] **Zitationen** – ein Fund, siehe Befund 3. `check_bib_keys.py`: alle genutzten Keys valide, `iso_9241_210` ungenutzt (Aufräumhinweis). `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**, 58 HINWEIS.
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
- [Hinweis, kein FAIL] Tabellenwertung `tab:wettbewerbsvergleich`, Spalte „Kommunikation \& Community" – siehe Befund 4.

## Teil-Check D – Build
Kein lokaler Build möglich: `lualatex`, `latexmk`, `biber` und `pdflatex` sind in dieser Session-Umgebung **nicht installiert** (anders als am 28.07. vormittags). Geprüft wurde stattdessen das im Repository liegende `main.pdf` — es ist **aktuell**: vier Textproben aus dem letzten Kürzungs-Commit `e6e024f` stehen im PDF, die jeweils ersetzten Vorgängerformulierungen nicht.
- [PASS, aus dem vorhandenen PDF] Kompiliert fehlerfrei – 24 Seiten, alle Verzeichnisse und Anhänge gesetzt.
- [PASS, aus dem vorhandenen PDF] Keine undefined references/citations, keine fehlenden Bilder, keine doppelten Labels – alle `\autoref`-Ziele und alle fünf Abbildungen aufgelöst.
- [FAIL] **Seitenumfang Textteil: 11 Seiten von 7–10.** „1 Einleitung" beginnt auf PDF-Seite 6 (gedruckt 1), das Literaturverzeichnis steht auf PDF-Seite 17 (gedruckt 12) — Textteil also gedruckte Seiten 1–11. Siehe Befund 1.

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
- [FAIL] **19 Zitationen geprüft · OK 3 · offen 16** (Details: `quellencheck.md`)
- Befunde je Klasse: kein WORTLAUT, kein ZITAT WEICHT AB, kein SEITE VERDÄCHTIG, kein NICHT GEFUNDEN, kein CLAIM SCHÄRFER. **Alle 16 offenen Fälle sind derselbe Typ: Quelle ohne Volltext-Snapshot** — siehe Befund 2.
- Neu verifiziert und mit OK quittiert (alle drei am Volltext, nicht aus dem Gedächtnis):
  - `nielsenUsabilityEngineering1993`, Kap. 6.8 „Thinking Aloud" (PDF-S. 207): Verbalisierung macht „major misconceptions" sichtbar, die Methode taugt ausdrücklich nicht für Performance-Messung. Deckt `07_iteratives_design.tex:5` exakt, inklusive der Abgrenzung gegen die reine Erfolgsmessung.
  - `sauroLewisQuantifying2016`, Kap. 8 „Standardized Usability Questionnaires" (PDF-S. 192): SEQ ist dort als Post-Task-Einzelfrage gelistet und ausdrücklich empfohlen; die siebenstufige Skala ist an anderer Stelle im Band belegt. Die Erfolgsschwelle „mindestens fünf im Mittel" steht im Text korrekt als **eigene** Festlegung und wird der Quelle nicht zugeschrieben — die Entschärfung vom 28.07. hält.
  - `erlhoferWebsiteKonzeptionUndRelaunch2017`, Kap. 17.2.2 (Praxistipp „Fünf Test-User reichen meist"): deckt die Aussage; 10–15 Personen sind damit nicht unterdimensioniert.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)
1. **Sechs Quellen ohne Volltext-Snapshot** | `references.bib`: `unTransformingOutWorld2030Agenda`, `vittuariHowReduceConsumer2023`, `barkerWhatNudgeTechniques2021`, `nivedhithaHowGreenSocial2024`, `somaFoodWasteReduction2020`, `shenInfluenceOsmosisSocial2023` — betroffen sind 16 Zitationen, die Stellen stehen namentlich in `quellencheck.md` | Erkennbar erledigt, wenn jeder Eintrag ein `file`-Feld mit einem PDF unter `sources/literatur/` trägt und `check_quellentreue.py` keine Zeile „LIVE PRÜFEN" mehr ausgibt | Warum nicht durch mich: kein Snapshot im `file`-Feld, und der Live-Abruf scheitert — MDPI (Barker, Soma) antwortet aus dieser Session mit HTTP 403, Elsevier (Vittuari, Shen) und Wiley (Nivedhitha) liegen hinter Verlagsschranken. Die betroffenen Aussagen tragen die gesamte verhaltenswissenschaftliche Fundierung, unter anderem die beiden Prozentwerte 51 % / 39 % aus der Soma-Feldstudie.
2. **Prompt-Wortlaut der Mockup-Quellenzeilen** | `pages/appendix.tex`, `\quelle{}`-Zeilen zu `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_profil`, `fig:mockup_feed` | Erkennbar korrekt, wenn der zitierte Prompt wörtlich dem entspricht, was tatsächlich in Claude Design eingegeben wurde | Warum nicht durch mich: der Foto-Platzhalter-Prompt wurde sinngemäß aus `sources/claude-design-nachbesserung.md` übernommen, nicht aus einem Eingabeprotokoll — nur der Nutzer kennt den echten Wortlaut.
3. **Style Tile: manuelle Nachbearbeitung ja oder nein** | `pages/appendix.tex`, `\quelle{}` zu `fig:styletile` | Erkennbar korrekt, wenn die Zeile den Zusatz „Abbildung nachträglich manuell bearbeitet." trägt, sofern das Bild nachbearbeitet wurde (die vier Mockups tragen ihn) | Warum nicht durch mich: ob am Style Tile nachbearbeitet wurde, ist dem Bild nicht anzusehen.

## Claims
- Ungesicherte FACTUAL CLAIMS: keine neuen. Die Plattform-Tatsachenbehauptungen der Wettbewerbsanalyse sind seit Runde 6 über den Methodensatz (`:13`) und die sechs offiziellen Domains in der `\quelle{}`-Zeile ausgewiesen — zulässig, weil die Analyse laut ZITIERREGEL eigene Sichtung ist.
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge (Aufräumhinweis, kein Score-Abzug): `iso_9241_210` — Rest aus dem übersprungenen Befund 7.4.
- Offene `% TODO-QUELLE:` / `% UNVERIFIED:`-Marker: keine.

## Punkteabzug im Detail
- Quellentreue, nicht prüfbare Quelle ohne Volltext: **−15** (6 Quellen × −5 = −30, gedeckelt bei −15)
- Seitenumfang außerhalb der Vorgabe: **−10** (11 statt 7–10 Seiten)
- Formalia-Verstoß (Zitation): **−8** (1 Vorkommen)
- **Summe: −33 → Score 67/100**

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: ABGEDECKT – alle drei Teilaufgaben ausgeführt, alle sechs Lieferobjekte vorhanden. Einziger Abzug an dieser Achse ist der Seitenumfang, den die IU-Richtlinien ausdrücklich als punktrelevant führen.
- **Prozess (25 %)**: ABGEDECKT – Vorgehen dokumentiert (`03_vorgehen_und_aufbau.tex`), reflektiert mit zwei konkreten Kursänderungen (`06_evaluation_reflexion.tex:7`), Grenzen in drei Limitationen. Die Methodenfundierung des Beta-Tests (SEQ, Think-Aloud, Stichprobengröße) stärkt diese Achse deutlich gegenüber dem 26.07.
- **Transfer (15 %)**: ABGEDECKT je Dimension – gesellschaftlich (SDG 12.3), wirtschaftlich (Freemium mit begründeter Trennlinie, Kooperationen), technisch (Funktionsübersicht, Datenvoraussetzung Rezeptbestand).
- **Kreativität (15 %)**: ABGEDECKT – expliziter Innovationsabsatz (`03_konzept.tex:32`) trennt Eigenes von Übernommenem; Vergleich zu Bestehendem über sechs Plattformen.
- **Dokumentation (10 %)**: ABGEDECKT – Entstehungsgeschichte als Abfolge, KI-Herkunft aller Abbildungen nach Zitierleitfaden Kap. 2.2.5 gekennzeichnet. SCHWACH an einer Stelle: Befund 3, ein namentlicher Quellenbezug ohne Beleg.
- **Ressourcen (10 %)**: ABGEDECKT – Phasenplanung mit Ressourcenspalte inkl. Daten, Puffer, Abhängigkeiten, zwei Risiken.

## Lieferobjekt-Abgleich
- [PASS] Alle sechs Lieferobjekte liegen vor: `tab:wettbewerbsvergleich`, Persona `tab:persona` (Anhang A), vier Mockups (Anhang B), Plattformname hergeleitet, `tab:funktionsuebersicht`, `tab:phasenplanung`.
- [PASS] **Bildsichtung der gestalteten Artefakte** (nicht nur Existenzprüfung): Die Startseite zeigt jetzt das Wochenplan-Banner („Wochenplan · Heute: Brokkoli-Suppe") — die Textaussage in `03_konzept.tex:13` („über die Startseite erreichbar") ist damit gedeckt, die seit dem 24.07. offene Mockup-Lücke geschlossen. Das Lesezeichen-Icon mit Zähler ist sichtbar und deckt „Gespeicherte Rezepte". Der Rettungs-Feed zeigt Challenge-Banner mit Rangliste, Reste-Tag ohne Präfix, Kommentar- und Bewertungselemente sowie den Plus-Button — dieser steht jetzt frei über dem Beitragsbild und überlappt die Aktionsleiste nicht mehr (**Befund 6.3 verifiziert behoben**). Die „Foto"-Platzhalter tragen keinen Doppelpunkt mehr.

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)

### Befund 1 — Seitenumfang: 11 statt 7–10 Seiten (−10)
`main.pdf`, gedruckte Seiten 1–11. **Die elfte Seite trägt nur 90 Wörter** (Ende von Limitation 3, ab „funktionsfähigen Prototyp folgen."). Es fehlen also rund 90–120 Wörter, nicht mehr — ein einziger sauberer Kürzungsschritt genügt.
Der Umfang ist kein kosmetisches Kriterium: `aufgabe.md:19` nennt 7–10 Seiten, und die IU-Richtlinien weisen die Überschreitung ausdrücklich als punktrelevant aus.
Reserve, ohne Substanz zu verlieren, in dieser Reihenfolge:
1. `01_wettbewerbsanalyse.tex:5` — der TikTok-Absatz erklärt in einem eigenen Satz, dass TikTok stellvertretend für Instagram steht. Das ist seit Runde 5 durch die Aufgabenstellung gefordert, ließe sich aber als Halbsatz im ersten Satz unterbringen (~15 W.).
2. `03_konzept.tex:9` — „Diese Mechanik greift zwei Befunde aus der Nudge-Forschung auf, also der Forschung zu verhaltenslenkenden Gestaltungsimpulsen." Die Definition steht als Einschub, obwohl „Nudge" im Text bereits geführt wird (~12 W.).
3. `05_phasenplanung.tex:21` — „weil sonst Entscheidungen zur Bedienführung nachträglich korrigiert werden müssten" begründet eine selbsterklärende Abhängigkeit (~10 W.).
4. `06_evaluation_reflexion.tex:3` — der Berichtsinhalte-Abgleich listet sechs Fundstellen mit voll ausgeschriebenen Bezeichnungen; „User Interface und User Experience über die Mockups in Anhang B" ließe sich auf „UI/UX in Anhang B" verkürzen (~8 W.).
5. `02_zielgruppe.tex:7` — der Kontrastsatz („anders als für Hobbyköch:innen, die vor allem neue Gerichte entdecken wollen") wiederholt die Verengungsbegründung aus `02_zielsetzung_und_verengung.tex:5` (~20 W.).
**Danach zwingend neu bauen und die gedruckte Seitenzahl gegenprüfen** — Seitenumbrüche sind sprunghaft, die Wortzahl allein beweist nichts. Ankerwert: 3.658 Wörter ergeben 11 Seiten.

### Befund 2 — Sechs Quellen ohne Volltext-Snapshot (−15, gedeckelt)
`references.bib`. Sechs der neun Einträge tragen kein `file`-Feld; damit sind **16 von 19 Zitationen** weder maschinell noch durch mich prüfbar, und der Live-Abruf scheitert an 403 bzw. Bezahlschranke. Betroffen sind ausgerechnet alle verhaltenswissenschaftlichen Belege, auf denen die Gamification- und Community-Herleitung ruht.
Kein Verdacht auf Falschzitat — das Skript hat in keiner der 19 Zitationen einen Wortlaut-, Zitat- oder Seitenbefund gefunden. Der Abzug betrifft die **Nachweisbarkeit**, und genau die verlangt der Prüfer laut `sources/Anmerkungen vom Prüfer.md`.
Auflage: Für jede der sechs Quellen den Volltext (bzw. bei der UN-Resolution einen PDF-Snapshot der Seite) unter `sources/literatur/` ablegen und den Pfad **über Zotero** ins `file`-Feld ziehen, dann `check_quellentreue.py` erneut fahren. Die drei PDF-gestützten Zitationen sind bereits mit OK quittiert und werden im inkrementellen Lauf nicht erneut geprüft.

### Befund 3 — Autorennennung ohne Beleg (−8)
`chapters/02_durchfuehrung/06_evaluation_reflexion.tex:7`: „Der zunächst naheliegende Community-Zuschnitt mit Forum und Nutzergruppen wich **nach dem Befund von Soma et al.** zeitlich begrenzten Challenges."
Der Autorname steht im Fließtext, aber ohne `\textcite`, ohne Jahr und ohne Stellenangabe. APA und der IU-Zitierleitfaden verlangen bei namentlicher Bezugnahme Autor **und** Jahr; wer nur dieses Kapitel liest, findet die Quelle nicht. Dass derselbe Befund in `04_community_und_feedback.tex:7` korrekt als `\textcite[S. 9]{somaFoodWasteReduction2020}` belegt ist, heilt die Stelle nicht — es macht die Inkonsistenz nur sichtbar.
Fix: `… wich nach dem Befund von \textcite[S. 9]{somaFoodWasteReduction2020} zeitlich begrenzten Challenges` — oder, falls der Umfang drückt, den Namen streichen und rein auf `~\autoref{sec:community_und_feedback}` verweisen. Die zweite Variante ist die kürzere und im Reflexionskapitel die sauberere.

### Befund 4 — Tabellenwertung leftovercooking, Spalte „Kommunikation \& Community" (kosmetisch, kein Score-Abzug)
`01_wettbewerbsanalyse.tex:13` definiert das Kriterium eng: „Bei Kommunikation \& Community zählt **nur tatsächlicher Austausch zwischen Nutzer:innen**." Der leftovercooking-Absatz (`:9`) stellt fest, ein solcher Austausch sei „nicht belegt", die Community-Ebene bleibe „auf das Verfolgen von Creator-Inhalten beschränkt" — die Zelle steht trotzdem auf „mittel", während Restegourmet mit derselben Begründung („schafft keinen Ort für Austausch") auf „schwach" steht.
Warum trotzdem kein FAIL: Die Wertung geht in die **selbstkritische** Richtung — sie stärkt den nächsten Wettbewerber, statt die eigene These zu schonen, und der Absatz erklärt sie ausführlich. Der Konflikt entstand erst, als Runde 5 die Kriteriendefinition auf „nur tatsächlicher Austausch" verengte, nachdem die Zelle in Runde 2 (GS-1) gesetzt worden war; die Propagation blieb aus.
Fix in einem Halbsatz, falls gewünscht: in `:13` ergänzen, dass eine einseitige Creator-Following-Ebene ohne wechselseitigen Austausch als „mittel" gewertet wird. Dann lesen Definition und Zelle wieder deckungsgleich. **Nicht** stattdessen die Zelle auf „schwach" ziehen — das würde den eigenen Alleinstellungsanspruch bequemer machen, als die Sichtung hergibt.

### Skript-Blindfleck (kein Textbefund, Notiz für `SKILL-ANPASSUNGEN.md`)
`check_formalia.py` meldet „`main.tex`: Anhangsverzeichnis aktiv bei 0 Anhang". Tatsächlich enthält `pages/appendix.tex` drei Anhänge (`\section*{Anhang~A: …}` bis `Anhang~C`); die Zählung greift offenbar nicht, wenn zwischen „Anhang" und dem Buchstaben ein geschütztes Leerzeichen `~` steht — dieselbe Klasse Fehlalarm wie beim `LOCATOR_RE`-Blindfleck für `[Kap.~8]` vom 28.07. Das Anhangsverzeichnis ist bei drei Anhängen korrekt aktiv, hier ist am Text nichts zu ändern.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- Eidesstattliche Erklärung elektronisch über myCampus abgeben — **ohne sie nimmt Turnitin die Einreichung nicht an**
- Einreichungs-Anleitung im myCampus-Kurs lesen
- `pages/meta.tex`: `\ModuleCode` und `\MatrikelNr` ausfüllen (stehen sonst als Platzhalter auf dem Titelblatt)
- Lokalen Build nach der Kürzung fahren und die gedruckte Seitenzahl des Textteils gegenprüfen (Ziel: 10 oder weniger)
- Volltexte der sechs Quellen aus Befund 2 über Zotero nachtragen, dann `check_quellentreue.py` erneut fahren
- `check_bib_hygiene.py`-Arbeitsliste in Zotero abarbeiten (urldate, URL neben DOI, Sentence Case, Sprachfeld, Verlagsorte, Artikelnummern) und neu exportieren — dabei gehen die vier von Hand eingetragenen Runde-7-Einträge verloren, sie müssen vorher in Zotero angelegt werden
- LanguageTool-Durchgang lokal über den Gesamttext
- Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)
- Prompt-Wortlaut und Nachbearbeitungs-Zusatz der Abbildungs-Quellenzeilen prüfen (Punkte 2 und 3 unter „Bitte manuell prüfen")
