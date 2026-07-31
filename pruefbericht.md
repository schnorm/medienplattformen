# Prüfbericht – Projektbericht

**Datum**: 31.07.2026 · **Geprüfter Stand**: alle 15 Kapiteldateien, `pages/appendix.tex`, `pages/acronyms.tex`, `pages/meta.tex`, `references.bib`, neu gebautes `main.pdf` (Arbeitsstand über Commit `7b597b4`) · **Audit-Typ**: **Abgabe-Audit** (Voll-Audit A–D, F, G, H + Teil-Check E als Hinweisliste + Sprachstichprobe)

**Score: 88/100 – abgabereif** (Schwelle ≥ 80; die verbleibenden Punkte sind optional nachbesserbar)

> **Einordnung gegenüber dem Vorbericht (Delta-Re-Audit vom selben Tag, 100/100).** Der Vorbericht war ein Delta-Lauf über die Chefkoch-Korrekturen und hat den Text nicht als Ganzes gegen Teil-Check C gelesen. Dieser Lauf tut das – und findet dabei einen Befund in der Vergleichstabelle, den bisher kein Durchgang aufgegriffen hat. **Der Score ist nicht gefallen, weil der Text schlechter geworden wäre**, sondern weil erstmals die vollständige spaltenweise Tabellenprüfung und die Reichweitenprüfung über alle 29 internen Verweise (`check_autoref.py`) gelaufen sind. Beide Befunde sind mechanisch und berühren weder These noch Argumentation noch Aufbau.

**Vorbedingungen des Voll-Audits erfüllt:** Gegenlesungen (Runden 3, 5, 6, 8, 9) abgearbeitet, `AENDERUNGEN.md` → „Offen" ist leer, `faktencheck-bericht.md` vollständig erledigt. Der **Gesamt-Stresstest wurde bewusst übersprungen** – Default der Kompakt-Prüfkette beim Papiertyp Projektbericht (Gegenlesung → Abarbeiten → Voll-Audit). Der davon abgedeckte Prüfblock „Roter Faden" wurde deshalb in diesem Bericht vollständig selbst geprüft statt referenziert.

---

## Teil-Check A – Formalia

- [PASS] **Zitationen** – `check_bib_keys.py`: alle 9 im Text genutzten Keys existieren in `references.bib`. Alle stellenbezogenen Zitate tragen eine Stellenangabe (`[S. …]`, `[Kap. …]`); `check_formalia.py` meldet keinen SEITENANGABE-Fehler. Narrative (`\textcite`) und parenthetische (`\parencite`) Form sind sachgerecht gemischt.
- [PASS] **Eigene Werke** – alle vier Tabellen und alle fünf Abbildungen tragen eine `\quelle{}`-Zeile, die Beschriftung steht jeweils über dem Objekt, Caption vor `\label{}`. Kein `\cite{}` auf ein eigenes Werk. Die vier KI-Mockups und der Style Tile sind nach Zitierleitfaden 2.2.5 gekennzeichnet („Erstellt mit dem Prompt … durch Anthropic, 2026"), das Persona-Foto mit Urheberin, Datenbank und Lizenz.
- [PASS] **Pronomen** – kein „ich/wir/man", kein „Die Projektgruppe" (Einzelarbeit laut `aufgabe.md`); dritte Person durchgehend.
- [PASS] **LaTeX-Format** – `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**, 59 Hinweiszeilen (Aufschlüsselung unten). Kein Geviertstrich im gesetzten Text, kein `\underline`, kein `\include` in Kapiteln, `~\autoref` durchgehend, Tabellen in `booktabs` + `\footnotesize`.
- [PASS] **Akronyme** – vier Einträge in `pages/acronyms.tex` (BMLEH, MVP, SDG, SEQ), alle im Text per `\ac{}` verwendet, kein ungenutzter Eintrag. „UI", „UX" und „KI" werden bei Erstnennung ausgeschrieben statt als Akronym geführt – zulässig, allgemein geläufige Abkürzungen gehören laut IU-Richtlinien nicht ins Verzeichnis.
- [PASS] **Cross-References & Labels** – 29 interne Verweise, 27 Labels, alle Ziele existieren; der Build meldet keine undefinierte Referenz. Labels konsistent `sec:`/`fig:`/`tab:`. Semantische Prüfung siehe Teil-Check C.
- [PASS] **Anti-KI-Stil** – keine Floskel-Öffner, keine gehäuften Klischee-Übergänge, keine rhetorischen Fragen, keine Pointen-Schlusssätze, keine Gedankenstrich-Häufung. Zwei TRIAS-Hinweise (`03_konzept.tex`, `05_phasenplanung.tex`, je 4×) betreffen sachliche Dreiergruppen (drei Hauptbereiche, drei Kategorien, drei Risiken) und fallen unter die ausdrückliche Ausnahme.
- [PASS] **Verständlichkeit** – am **Fließtext ohne Tabellenmarkup** nachgemessen: durchschnittliche Satzlänge 16–25 Wörter je Subsection, nur `01_wettbewerbsanalyse.tex` (25,1) und `03_konzept.tex` (22,7) liegen über dem Richtwert 22. Die SATZSCHNITT-Hinweise des Skripts (~28/~30) sind dadurch verzerrt, dass es Tabellenumgebungen als „Sätze" mitzählt (119/126/135 Wörter). Die als überlang gemeldeten Sätze sind fast durchweg angekündigte Aufzählungen nach Doppelpunkt und beim ersten Lesen verständlich – **kein gehäufter Verständlichkeitsverstoß, daher kein Abzug**. Dichtester Absatz: `03_konzept.tex:9` (kosmetischer Hinweis unten).
- [PASS] **Offene Arbeitsmarker** – kein `% TODO-QUELLE:`, kein `% UNVERIFIED:`.
- [PASS] **`main.tex`/`cover.tex` unverändert**, Projektangaben ausschließlich in `pages/meta.tex`, dort alle Felder befüllt (`\SubmissionDate{\today}` ist bewusste Nutzer-Entscheidung laut `PERSISTENT.md`).
- [PASS] **Quellen-Sperrliste** – keine Skripte, Vorlesungsfolien oder Webinare zitiert; kein Sekundärzitat.

**Sprachstichprobe (nur Abgabe-Audit, zwei Absätze je Hauptkapitel, ausschließlich auf Sprachfehler):** Keine Rechtschreib-, Grammatik- oder Kommafehler gefunden; `check_formalia.py` meldet keine Wortdopplung. Zwei Formulierungen mit Stolperpotenzial, beide ohne Score-Wirkung – siehe kosmetische Hinweise.

---

## Teil-Check B – Argumentationsqualität (nur Pflicht-Punkte aus `typen/projektbericht.md`)

- [PASS] **These erkennbar, Leitfrage ≠ These** – Ziel („Konzeption der Plattform Resteria", `02_zielsetzung_und_verengung.tex:3`) und These (die Kombination aus Reste-Matching und echter Zero-Waste-Community schließt eine Marktlücke) sind getrennt formuliert.
- [PASS] **Normative Ebene der These** (Pflicht) – „Resteria soll Reste-Matching … mit einer echten Social-Community verbinden" (`02_zielsetzung:3`); Funktionsableitung aus den Levers (`03_konzept:5`).
- [PASS] **Aktualität/Zeitbezug in der Einleitung** (Pflicht) – SDG 12.3 mit Zieljahr 2030 (`01_ausgangslage:5`), belegt.
- [N.A.] **Forschungslücke in der Einleitung** – laut Typ-Datei „Optional"; faktisch als Marktlücke ausformuliert (`01_ausgangslage:7`).
- [PASS] **Gegenargument reflektiert & entkräftet** (empfohlen) – `01_wettbewerbsanalyse:38` erhebt den stärksten Einwand („eine reine Community-Plattform mit Nachhaltigkeitsthema könnte bereits ausreichen") und entkräftet ihn.
- [PASS] **Syntheseleistung pro Hauptkapitel** (Pflicht) – Einleitung schließt mit der Lücke, Durchführung mit `sec:evaluation_reflexion`, Fazit mit Kernergebnissen und Limitationen.
- [PASS] **Limitationen dreischichtig** (Pflicht) – alle drei Grenzen nachgezählt vollständig: (1) kein Nutzertest · verhaltenswissenschaftliche Fundierung der Kernfunktionen · Beta-Test; (2) KI-Mockups ohne Nutzerrückmeldung · Anspruch auf die drei Navigationsbereiche begrenzt · Klick-Prototyp-Test; (3) nur sechs Vertreter · gezielte Auswahl mit ein bis drei je Kategorie · breitere Marktanalyse.
- [PASS] **Phasenplanung als Tabelle** (Pflicht) – `tab:phasenplanung`, fünf Phasen mit Zeitrahmen und Ressourcen.
- [PASS] **Dritte Person streng** (Pflicht) – siehe Teil-Check A.
- [N.A.] **Ergebnisse ≠ Interpretation** – laut Typ-Datei „Entfällt" beim Projektbericht.
- [PASS] **Typspezifische Audit-Checks** – Produkt sichtbar dokumentiert; Reflexion mit Theorie-Praxis-Bezug; 9 zitierte Quellen (Richtwert 5–10) plus eigene Artefakte.
- [PASS] **Leitfragen aus `aufgabe.md` beantwortet** – (1) Analyse bestehender Plattformen → `sec:wettbewerbsanalyse` mit sechs Plattformen und Kriterienmatrix; (2) Konzeptentwicklung mit innovativen Funktionen → `sec:konzept`, Innovationsabsatz `:15`; (3) Iteratives Design und Feedback → `sec:iteratives_design`, ausdrücklich als geplantes Vorgehen.
- [PASS] **Teilaufgaben-Abgleich** – alle drei Teilaufgaben real ausgeführt, keine durch eine Simulation ersetzt. Der hypothetische Charakter der Feedback-Schleifen ist in `07_iteratives_design.tex:5` benannt und laut `aufgabe.md` ausdrücklich zulässig („Beschreibung genügt – keine reale Durchführung verlangt").
- [PASS] **Abhakliste** (per Grep über `chapters/`, nicht aus dem Leseeindruck) – Rezept-Uploads `03:13` · Kommentar-/Bewertungssystem `03:13` · Personalisierte Empfehlungen `03:13` · Gruppen und Foren `04:9` (erwogen, begründet verworfen) · Event-Kalender `03:38` (Auslassung begründet) · Lebensmittel-Journaling/Menüplanung `03:13` · Verengung der Zielgruppe `02_zielsetzung:5`. Die vier geforderten Berichtsinhalte (Zielgruppe, Funktionalitäten, UI und UX, Community-Building) haben je einen zusammenhängenden Ort.
- [PASS] **Genannte Materialien** – Hansch & Rentschler (2012) und Kapoor et al. (2018) fehlen im Literaturverzeichnis. Laut `aufgabe.md` nicht verpflichtend; der Verzicht ist am 29.07.2026 als endgültige Nutzer-Entscheidung festgehalten. Kein FAIL.
- [PASS] **Dimensionsabgleich** gegen die Abdeckungs-Tabelle in `kapitelplan.md` – keine Dimension ohne Ort im Text, Aufstellung unter „Bewertungsschwerpunkte".

---

## Teil-Check C – Struktur

- [PASS] **½-Seiten-Regel** – ein Hinweis: `03_vorgehen_und_aufbau.tex` mit ~136 Wörtern unter der 150-Wörter-Schwelle des Skripts. Im gesetzten PDF füllt der Abschnitt mit zwei Absätzen deutlich mehr als eine halbe Seite; Heuristik-Artefakt, kein Verstoß.
- [PASS] **Max. 3 Kapitelstufen** – `\section` / `\subsection`, keine dritte Ebene.
- [PASS] **Mindestens 2 Unterpunkte je Kapitel** – Einleitung 3, Durchführung 7, Fazit 2.
- [PASS] **Front-/Backmatter** – Titelblatt, Inhalts-, Abbildungs- (5 Abb.), Tabellen- (4 Tab.) und Abkürzungsverzeichnis, Literaturverzeichnis, Anhangsverzeichnis, Anhänge A–C. Beide `\listof…`-Schalter sind aktiviert und liegen über der Pflichtschwelle von 3. Je Anhang mindestens ein Textverweis (A → `02_zielgruppe:9`; B → `03_konzept:36`; C → `03_konzept:36` und `02_limitationen:5`); das Anhangsverzeichnis A/B/C stimmt mit der Reihenfolge im Dokument überein.
- [PASS] **Vorspann je Kapitel** – alle drei Master-Dateien mit einem bzw. zwei Sätzen, kein VORSPANN-Hinweis.
- [PASS] **Outline-Check** – Einleitung (Umfeld, Problem, Ziel, Vorgehen) → Durchführung (Analyse, Zielgruppe, Konzept, Community, Iteration, Phasenplanung, Evaluation/Reflexion) → Fazit (Kernergebnisse, Ausblick, Limitationen). Identisch mit dem Gerüst in `typen/projektbericht.md` und mit dem in `kapitelplan.md` bestätigten Skelett.

### Roter Faden (kapitelübergreifend, vollständig selbst geprüft)

- [PASS] **Querverweise semantisch – Fundstelle *und* Reichweite.** Alle **29** internen Verweise einzeln gegen ihre Zielstelle gelesen und in `autorefcheck.md` mit Begründung quittiert. Besonders geprüft wurden die vier Verweise mit Gewichtungsmarker: `03_konzept:7` („allein"), `03_konzept:9` („vor allem"), `06_evaluation:9` („nur"), `01_kernergebnisse:7` („vor allem") – alle vier tragen. Der im Vorbericht behobene Reichweitenfehler in `04_community_und_feedback.tex:9` ist verifiziert weg: Der Satz schreibt `sec:zielgruppe` keine Rangfolge mehr zu, und die Zielstelle nennt weiterhin zwei gleichrangige Anforderungen.
- [PASS] **Zeitlinien-Konsistenz Entwurf ↔ Iteration** – `07_iteratives_design.tex:3` beschreibt die Mockup-Runden ausdrücklich als „Abgleich gegen die Konzeptbeschreibung"; das Konzeptkapitel steht damit zu Recht vor der Iteration. Der Darstellungsstand ist durchgehend der finale, und die eine echte Konzeptänderung (Gruppen/Foren → Challenges) ist in `06:5` als Kursänderung ausgewiesen und in `04:9` begründet.
- [PASS] **Rückgriffe auf die eigene Analyse** – `04:3`, `03_konzept:7` und `01_kernergebnisse:3` überdehnen die Wettbewerbsanalyse nicht; `01_kernergebnisse:5` weist die Differenzierung selbst ausdrücklich als „unbelegte Marktbeobachtung" aus.
- [PASS] **Kernbegriffs-Konsistenz** – Reste-Matching, Rettungs-Feed, Rettungspunkte, Reste-Level, Challenges, Zero-Waste-Woche, Gruppen und Foren, nachhaltigkeitsorientierte Hobbyköch:innen: durchgehend identisch benannt, keine Synonym-Variation bei Kernbegriffen.
- [PASS] **Zahlenangaben nachgezählt** – 24 Zählaussagen einzeln gegen Tabellen und Aufzählungen geprüft (drei Merkmale · zwei Anforderungen · sechs Plattformen · drei Kategorien · drei Vertreter · „die dritte Reste-Matching-App" · fünf Phasen · drei Risiken · drei Hauptbereiche · vier Mockups · sechs Funktionen · drei Limitationen · „ein bis drei Vertreter" · zwei Kursänderungen · „die zweite dieser Kursänderungen" · zwei bis drei Wochen ↔ Woche 15–17 · zehn bis fünfzehn Personen ↔ 10–15 · zwei Wochen Puffer · fünf Testpersonen · siebenstufige Skala · Mittelwert ≥ 5 · 51/39 Prozent · „eine vierte Funktion" · drei Plattform-Kategorien). **Alle stimmen.**
- [PASS] **Kriterien derselben Art** – alle fünf Spalten sind Merkmale, kein zusammenfassendes Gesamturteil geht als gleichrangige Spalte ein.
- [PASS] **Keine Matrix-Verzerrung** – das Objekt, gegen das sich die These richtet, erhält nicht durchgehend die schlechtesten Werte (Chefkoch 3× „stark", leftovercooking 2× „stark"); `02_limitationen:7` weist die Auswahlgrenze zusätzlich aus.
- [PASS] **Akteurskonsistenz** – Nutzer:innen, Food-Creator:innen, Beta-Gruppe und externe Testpersonen bleiben widerspruchsfrei. Die Ausschließlichkeitsaussage des Freemium-Modells („Kostenpflichtig sind … **nur** Komfortfunktionen der individuellen Planung; Reste-Matching, Rettungs-Feed und Challenges bleiben kostenlos", `03:3`) wird an keiner späteren Stelle verletzt – die Menüplanung selbst ist kostenlos, nur die Vorratsübersicht gehört ins Bezahlpaket.
- [PASS] **Offene Einwände** – Grep über „setzt voraus", „hängt davon ab", „bleibt angewiesen", „nur wenn": drei Treffer, alle beantwortet (Rezeptbestand → Phase 3 und Risiko 2; MVP vor Beta-Test → Abhängigkeitsabsatz; Prototyp-Voraussetzung im Ausblick → Phasenplanung und Limitation 1).
- [PASS] **Redundanz über den ganzen Text** – der zentrale Befund (Marktlücke) steht auf Behauptungsebene in der Einleitung, belegt in der Wettbewerbsanalyse und einmal wiederaufgenommen im Fazit; das ist die zulässige Trichter-Struktur, keine Dublette. Der Vorbehalt „kein Nutzertest" erscheint viermal, davon dreimal als Halbsatz bzw. Ausblick und einmal ausführlich als Limitation 1. Der Umfang liegt im Soll, es besteht kein Kürzungsdruck.
- [PASS] **Wirkungsaussagen gegen den beschriebenen Mechanismus** – Grep über „macht sichtbar", „bewirkt", „führt dazu", „sorgt dafür", „ermöglicht", „stellt sicher", „damit wird": jede Behauptung hat einen im Text beschriebenen Mechanismus. Insbesondere `02_zielgruppe:7` („sichtbar machen, wie viel eine Person tatsächlich einspart") wird durch `03:13` (Reste-Journal → Rettungspunkte **und** Einsparangabe) und durch das Profil-Mockup („12,4 kg Lebensmittel gerettet") eingelöst.
- **[FAIL] Tabellenwertungen mit den eigenen Kriteriendefinitionen vereinbar – spaltenweise geprüft: ein Befund (siehe Befund 1).**

---

## Teil-Check D – Build

- [PASS] **Kompiliert fehlerfrei.** Vollständiger Neubau aus leerem Zustand (`build/` und `main.pdf` vorher gelöscht), `latexmk main.tex` über die projekteigene `.latexmkrc` (lualatex · biber · lualatex · lualatex), **Exit-Code 0**. `scripts/build.ps1` existiert in diesem Projekt nicht – die Umgebung ist Linux, `lualatex`, `biber`, `latexmk` und `pdflatex` liegen auf dem PATH, und die `.latexmkrc` ist passend eingestellt (`$pdf_mode = 4`, `$aux_dir = 'build'`).
- [PASS] **Log sauber.** 0 Fehler (`^!`), 0 undefinierte Referenzen, 0 undefinierte Zitationen, 0 doppelte Labels, 0 fehlende Dateien, **0 Missing character**. Die vier „undefined"-Treffer im Log sind `Package acronym Info`-Meldungen der ersten Durchläufe, keine Warnungen.
- [PASS] **Randüberstand** – **0 Overfull \hbox**. 11 Underfull \hbox, sämtlich in schmalen Tabellenspalten (zu locker gesetzte Zeilen, kein Überstand in den Rand) – kein Formfehler.
- [PASS] **Projekt-Root sauber** – nach dem Lauf liegen dort weder `.aux`, `.bcf`, `.log`, `.out`, `.run.xml`, `.toc` noch `.bbl`/`.blg`; alle Hilfsdateien stehen in `build/`. Das PDF trägt also ein regulär über biber erzeugtes Literaturverzeichnis.
- [PASS] **Seitenumfang Textteil: 10 Seiten von 7–10.** Am gebauten PDF gemessen: „1 Einleitung" auf PDF-Seite 6 (gedruckt 1), Literaturverzeichnis auf PDF-Seite 16 (gedruckt 11); 23 PDF-Seiten gesamt. Im Soll, exakt auf der Obergrenze. `check_umfang.py`: 3.710 Wörter gegen das Ziel 2.625–3.750 – ebenfalls im Korridor (Einleitung 496 / Durchführung 2.821 / Fazit 393 Wörter = 13,4 / 76,0 / 10,6 %, alle drei Anteile im Soll).
- **Weißraum gemessen** (kein Kürzungsanlass, aber relevant für spätere Ergänzungen): Auf der letzten Textseite steht die unterste Fließtextzeile bei y ≈ 229,5 pt, die Satzspiegel-Unterkante bei y ≈ 56,7 pt, der Zeilenabstand beträgt 16,4 pt → **≈ 173 pt ≈ 10 freie Zeilen**. Kein Float erzeugt eine auffällige Weißraum-Reserve auf einer früheren Seite. Die im Projektstatus geführten Werte (37 pt bzw. 134 pt) stammen aus älteren Textständen und sind damit überholt.

---

## Teil-Check E – Abgabe (informativ, **kein** Score-Abzug – Festlegung `MEMORY.md` 19.07.2026)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben – ohne sie nimmt Turnitin die Einreichung nicht an.
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen.
- [PASS] Umfang im Soll – Spiegel aus Teil-Check D (10 von 7–10 Seiten).
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko).
- [OFFEN] LanguageTool-Durchgang lokal über den Gesamttext – die Sprachstichprobe oben ersetzt keine Vollprüfung.

---

## Teil-Check F – Literaturverzeichnis

- [PASS] **Feld-Hygiene** – `check_bib_hygiene.py`: 10 Einträge, **0 Fehler, 0 Hinweise**.
- [PASS] **Gerendertes Verzeichnis** (PDF-Seite 16) gegen `_shared/literaturverzeichnis.md` gelesen: Alphabetik korrekt (Barker · Erlhofer · Hasanbekava · Nielsen · Nivedhitha · Sauro · Shen · Soma · United Nations General Assembly · Vittuari), Sentence Case durchgehend, keine kaputten Sonderzeichen, Artikelnummern einheitlich als „Artikel N" (11099, e13038, 107706, 907), DOI ohne zusätzliche URL, kein `urldate`, keine APA-Disambiguierung nötig. Der Pexels-Eintrag folgt exakt dem Muster für Datenbank-Bilder (Urheberin · n. d. · Titel mit `[Foto]` · Datenbank · URL); die Lizenz steht regelkonform in der Quellenzeile der Abbildung, nicht im Verzeichnis.
- [PASS] **Stichprobe Feld für Feld gegen die Titelei des Volltexts** (4 Einträge):
  - **Nielsen 1993** – Titelblatt „Usability Engineering / Jakob Nielsen / Morgan Kaufmann", Copyright 1993. Verlag korrekt als Titelblatt-Imprint übernommen. Das Inhaltsverzeichnis bestätigt „6.8 Thinking Aloud, S. 195" und damit den Locator `[Kap.~6.8]` im Text.
  - **Sauro & Lewis 2016** – Titelblatt „Quantifying the User Experience / Practical Statistics for User Research / 2nd Edition / Morgan Kaufmann", Copyright 2016. Auflage, Verlag und Jahr stimmen; rendert als „(2. Aufl.)".
  - **Soma et al. 2020** – *Sustainability*, „Published: 26 January 2020", DOI 10.3390/su12030907, Artikelnummer 907.
  - **Shen et al. 2023** – Kopfzeile „Computers in Human Behavior 143 (2023) 107706"; Band, Jahr und Artikelnummer stimmen.

  Keine Abweichung – keine Zotero-Arbeitsliste nötig.

---

## Teil-Check G – Quellentreue (Volltextabgleich, im Abgabe-Audit blockierend)

- [PASS] **19 Zitationen in 15 Dateien geprüft · 19× FUNDSTELLE OK · 0 offen** (Details: `quellencheck.md`).
- Keine Befunde der Klassen WORTLAUT, ZITAT WEICHT AB, SEITE VERDÄCHTIG, SEITE AUSSERHALB, NICHT GEFUNDEN, CLAIM SCHÄRFER oder RENTIERT NICHT. Kein `NICHT PRÜFBAR`, kein `LIVE PRÜFEN`, kein `ZUGANG PRÜFEN`, kein `VOLLTEXT BESCHAFFBAR` – alle neun zitierten Werke liegen als Volltext unter `sources/literatur/<citekey>.<ext>` und lösen damit rechnerunabhängig auf.
- Kein `[NOTIZ-DUBLETTE]`- und kein `[NOTIZ-FREMDER-AUTOR]`-Hinweis.
- Kein Trägersatz hat sich seit dem letzten Urteil geändert; die einmalige Migration der Tabellen-Zitationen (Trägersatz auf Zeilenkopf + Zelle begrenzt) ist bereits vollzogen und erzeugt hier keine Neuprüfung.

> **Grenze dieses Checks, ausdrücklich vermerkt:** Teil-Check G prüft Fundstelle und Wortlaut, **nicht die Reichweite**. „19/19 FUNDSTELLE OK" belegt also nicht, dass jede Quelle ihre Aussage in der behaupteten Stärke trägt. Die Reichweitenprüfung hat die Gegenlesung Runde 9 (29.07.2026) über alle 19 Zitationen geleistet; ihre zehn Befunde sind abgearbeitet.

---

## Teil-Check H – Lesefluss (max. −5)

- [PASS] **Anschlüsse** – jedes „es", „beide", „diese", „daraus", „letztere", „deren" hat ein Bezugswort und zeigt aufs Richtige; alle 12 Subsections einzeln am Stück gelesen. Kein ANAPHER-Hinweis des Skripts, keine satzinterne Ausnahme gefunden.
- [PASS] **Absatzöffner** – jeder Absatz beginnt mit einer Aussage, kein abgeschnittener Rest.
- **[FAIL] Absatzlänge und Rhythmus** – ein Befund in `06_evaluation_reflexion.tex` (siehe Befund 2).

---

## Befunde

### Befund 1 (Struktur, −10) – „Rezept-Austausch" ist das einzige undefinierte Kriterium, und zwei Wertungen sind im Text nicht gedeckt

**Stelle:** `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:15` (Kriteriendefinition) und `tab:wettbewerbsvergleich`, Spalte „Rezept-Austausch", Zeilen **Restegourmet** und **`\ac{BMLEH}`-App** (beide „mittel").

**Was ist:** Der Definitionsabsatz erklärt die dreistufige Skala allgemein und präzisiert danach ausdrücklich **drei** der fünf Kriterien: „Bei Kommunikation \& Community zählt tatsächlicher Austausch zwischen Nutzer:innen …", „Rezept-Entdeckung erfasst, wie leicht sich überhaupt ein passendes Rezept finden lässt", „… während die reste-spezifische Suche das Kriterium Reste-Matching-Werkzeug abdeckt". **„Rezept-Austausch" wird nirgends erklärt** – das Wort kommt im gesamten Textteil nur zweimal vor: in der Herleitung der Achsen und in der Tabellenüberschrift.

**Warum das ein Befund ist und nicht bloß eine Lücke:** Der Definitionsabsatz reserviert „Austausch zwischen Nutzer:innen" ausdrücklich für die Spalte „Kommunikation \& Community". Wer „Rezept-Austausch" trotzdem in seiner naheliegenden Bedeutung liest – Nutzer:innen tauschen Rezepte –, findet in jeder anderen Zelle dieser Spalte ein im Text beschriebenes Teilen-Merkmal: Chefkoch „stark" (Upload, Bewerten, Kommentieren, `:3`), leftovercooking „mittel" (Food-Creator:innen teilen eigene Rezepte, `:9`), TikTok „mittel" (Rezeptvideos, `:5`), Foodsharing „schwach" (keine Rezepte, `:11`). Für **Restegourmet und die `\ac{BMLEH}`-App** beschreibt der Text dagegen **kein** Teilen: `:7` nennt Zutaten-Eingabe, Portionenrechner und Rezeptdatenbank und hält ausdrücklich fest, dass Restegourmets „Fokus auf individuelle Rezeptverwaltung … keinen Ort für Austausch" schafft. `:36` verschärft das: „Die Matching-Apps lösen das Zutaten-Problem **ohne Austausch zwischen den Nutzer:innen**." Zwei „mittel"-Wertungen stehen damit ohne Deckung neben zwei Textstellen, die dasselbe Merkmal verneinen.

**Einordnung:** Das beschädigt die Argumentation **nicht** – die Wertungen sind zugunsten der Konkurrenz zu hoch, eine Korrektur nach unten würde die Marktlücke sogar deutlicher machen. Der Befund ist ein Nachvollziehbarkeitsproblem an genau dem Lieferobjekt, das die gesamte Lückenbehauptung trägt, und die Art Stelle, an der eine Prüferin oder ein Prüfer eine Randnotiz setzt.

**Zwei Wege, beide klein:**

- **(a) Definieren, keine Zelle ändert sich** – in `:15` einen Halbsatz ergänzen, der klarstellt, dass „Rezept-Austausch" die Verfügbarkeit und Weitergabe von Rezepten auf der Plattform erfasst (einseitig wie beidseitig), während der Austausch *zwischen* Nutzer:innen in der Kommunikationsspalte steht. Rund 15 Wörter, keine Folgeaussage betroffen.
- **(b) Wertungen angleichen** – Restegourmet und `\ac{BMLEH}`-App in dieser Spalte auf „schwach" setzen. Kostet kein Wort. Gegengeprüft: `:36` und `:38` bleiben unberührt (sie argumentieren über Reste-Matching und Community, nicht über Rezept-Austausch), `02_limitationen:7` ebenfalls.

**Empfehlung: (a).** Die kleinere Änderung, macht die Spalte für jede Leseart eindeutig und folgt der bereits gewählten Systematik des Absatzes, der die kritischen Kriterien einzeln erläutert. Beide Varianten verlangen anschließend einen Neubau mit Seitenkontrolle; bei (a) reicht die gemessene Reserve von ~10 Zeilen dafür klar.

### Befund 2 (Lesefluss, −2) – Absatzreihenfolge in der Projektreflexion

**Stelle:** `chapters/02_durchfuehrung/06_evaluation_reflexion.tex`, Absätze `:5`, `:7`, `:9`.

**Was ist:** `:5` benennt die beiden Kursänderungen (Community-Zuschnitt, Namenskollision). `:9` zieht daraus die Lehre und beginnt mit „Aus der **zweiten dieser Kursänderungen** …". Dazwischen steht `:7` mit einem thematisch anderen Gegenstand – der chronologischen Entstehungsgeschichte –, und zwar als **Ein-Satz-Absatz von 50 Wörtern**, dem längsten Satz des Kapitels. Der Rückbezug in `:9` springt damit über einen fremden Absatz hinweg, und `:7` steht rhythmisch allein zwischen zwei mehrsätzigen Absätzen.

**Warum es zählt – und warum nur −2:** Der Bezug ist formal korrekt und löst sich nach dem Doppelpunkt sofort auf, ein Leser verliert also nichts. Der Absatz `:7` trägt aber ausgerechnet das Kriterium **Dokumentation** („Entstehungsgeschichte lückenlos", 10 %) und steht dort als isolierter Einschub, statt die Erzählung zu tragen.

**Fix ohne ein einziges neues Wort:** `:7` vor `:5` ziehen. Die Reihenfolge lautet dann: Spannung SDG ↔ Nische (`:3`) → Entstehungsgeschichte (`:7`) → Methodenbewertung und die zwei Kursänderungen (`:5`) → Lehre aus der zweiten (`:9`). Nennung und Auswertung der Kursänderungen stehen damit nebeneinander, und die Chronologie eröffnet die Reflexion, statt sie zu unterbrechen. Reine Verschiebung, ±0 Wörter, keine Zitation und kein `\autoref` betroffen (`:7` enthält keinen).

---

## Kosmetische Hinweise (kein Score-Abzug, kein Handlungsdruck)

- **`01_wettbewerbsanalyse.tex:36`, SWOT-Schlusssatz:** „… Chancen bieten die wachsende Relevanz … und Partnerschaften mit bestehenden Initiativen, ein Risiko das dichte Umfeld etablierter Reste-Apps." Die Ellipse ist grammatisch vertretbar, führt aber in einen Holzweg: „ein Risiko das …" liest sich zunächst als Relativsatz mit fehlendem Komma. Ein Wort behebt es: „…, ein Risiko **ist** das dichte Umfeld etablierter Reste-Apps."
- **`07_iteratives_design.tex:5`:** „Wie beim Klick-Prototyp-Test gilt auch hier **Erlhofers** Maßstab von fünf Testpersonen" – der Genitiv Singular nennt nur den ersten von zwei Autoren; das Verzeichnis führt „Erlhofer, S. & Brenner, D.". Da die vollständige Zitation zwei Sätze davor steht, genügt „gilt auch hier **der** Maßstab von fünf Testpersonen" (−1 Wort). Verwandt mit Befund 9.7 der Gegenlesung, der an derselben Stelle den Numerus korrigiert hat.
- **`03_konzept.tex:9`** ist mit sieben Sätzen und vier Belegen der dichteste Absatz der Arbeit (Rettungspunkte, Nudge-Definition, Reminders, Nivedhitha). Verständlich, aber der einzige Absatz, der beim ersten Lesen Tempo kostet. Eine Teilung vor „Ergänzend plant Resteria eine wiederkehrende Erinnerungsbenachrichtigung …" wäre kostenlos – lohnt aber nur, wenn ohnehin neu gebaut wird.
- **Geviertstriche in den KI-Mockups** (Style Tile: „Salbeigrün — Primär"; Profil: „Level 4 — Resteheld:in"). Sie stehen im Bild, nicht im Text, und sind von der Geviertstrich-Regel nicht erfasst – erwähnt, weil sie im abgegebenen PDF sichtbar sind. Eine Korrektur hieße neue Mockup-Runde; das steht in keinem Verhältnis.
- **`check_aussenwelt.py`-Zustandsdatei:** Die 14 Kandidaten stehen unquittiert auf „NEU", obwohl `faktencheck-bericht.md` sie inhaltlich abgearbeitet hat. Reine Buchführung, ohne Wirkung auf die Arbeit.
- **`check_status.py`:** 0 Fehler, 15 `DATEI-OHNE-ZEILE`-Hinweise. Projektkonvention – die Statustabelle in `CLAUDE.md` führt Hauptkomponenten, nicht jede Subsection-Datei.

---

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

1. **Wortlaut der zitierten Claude-Design-Prompts** | `pages/appendix.tex`, Zeilen 30, 39, 46, 53, 60 (`\quelle{}`-Zeilen der fünf Abbildungen) | Stimmt der zitierte Prompt-Text wörtlich mit der Eingabe im Claude-Design-Chat überein, einschließlich der Folge-Prompts bei Rettungs-Feed und Profil? | Der Chatverlauf liegt außerhalb des Repositorys; ich kann nur prüfen, dass die Zitate formal korrekt gesetzt und in sich geschlossen sind. **Zur Entlastung:** Der Zitierleitfaden (Kap. 2.2.5) verlangt nur „den verwendeten Prompt" im Singular – ein fehlender Folge-Prompt wäre kein Regelverstoß, ein *falsch wiedergegebener* Prompt schon.
2. **Aktualität der IU-Leitfäden zum Abgabezeitpunkt** | `sources/Zitierleitfaden.pdf` und `sources/Richtlinien für die Gestaltung wissenschaftlicher Arbeiten.pdf` (Datumszeile auf der Impressumsseite) gegen den Prüfungs-Guide auf myCampus; Register `_shared/quellen-versionen.md` | Tragen beide dort ebenfalls den Stand 01.10.2025? | Die Spalte „zuletzt vom Nutzer bestätigt" ist im Register für **alle** Zeilen leer. Die PDFs wurden am 25.07.2026 ausgetauscht und das Destillat am 28.07.2026 dagegen geprüft – die Regeln sind also mit hoher Wahrscheinlichkeit aktuell, formal bestätigt ist es nicht. Laut Richtlinien gilt die zum Abgabezeitpunkt gültige Fassung. myCampus kann ich nicht abrufen.
3. **Namensverfügbarkeit „Resteria"** | DPMA-Markenregister und `.de`-Domain | keine eingetragene Marke und keine aktive Domain im selben Themenfeld | Steht seit Projektbeginn als Nutzer-Restpflicht in `kapitelplan.md`; nicht abgabekritisch, aber vor einer realen Nutzung des Namens relevant.

---

## Claims

- **Ungesicherte FACTUAL CLAIMS**: keine. Die unzitierten Außenweltbehauptungen der Wettbewerbsanalyse sind Gegenstand des eigenständigen `faktencheck`-Laufs vom 30.07.2026 (`faktencheck-bericht.md`): 12 Kandidaten, 10 vollständig bestätigt, beide Befunde am 30. und 31.07. abgearbeitet – der Bericht ist vollständig erledigt.
- **Fehlende OWN WORK-Markierungen**: keine.
- **Ungenutzte Bib-Einträge (Aufräumhinweis)**: `check_bib_keys.py` meldet `pexelsHasanbekavaBasket` als ungenutzt. **Fehlalarm durch den Prüfumfang** – der Eintrag wird in `pages/appendix.tex:21` über `\citeauthor`/`\citeyear` verwendet, das Skript scannt nur `chapters/`. Am gerenderten Verzeichnis verifiziert: Der Eintrag steht dort korrekt. Kein Handlungsbedarf.
- **Volltexte ohne Bib-Verweis (Aufräumhinweis)**: `sources/literatur/` enthält drei Dateien ohne zugehörigen Bib-Eintrag – Krug „Don't Make Me Think", Norman „The Design of Everyday Things" (beide bewusst nicht zitiert) und die Preprint-Fassung von Vittuari (durch die Verlagsfassung ersetzt).

---

## Punkteabzug im Detail

| Kategorie | Abzug | Begründung |
|---|---|---|
| Struktur-Verstoß (Teil-Check C) | **−10** | Befund 1 – Tabellenwertung nicht durch die eigene Kriteriendefinition gedeckt (1 Vorkommen, Deckel −30) |
| Lesefluss-Befund (Teil-Check H) | **−2** | Befund 2 – Absatzreihenfolge und Ein-Satz-Absatz (1 Vorkommen, Deckel −5) |
| **Summe** | **−12** | **Score 88/100 – abgabereif** |

Keine Abzüge in den Kategorien BBT-Keys, Pflicht-Punkte der Typ-Datei, Formalia, Build, undefinierte Referenzen, Seitenumfang, Literaturverzeichnis, Anti-KI-Stil, Verständlichkeit, Quellentreue.

---

## Bewertungsschwerpunkte (Projektbericht) – je Dimension

| Kriterium | Gewicht | Dimension | Status | Fundstelle |
|---|---|---|---|---|
| **Qualität** | 25 % | Erfüllt das Ergebnis die Aufgabenstellung | ABGEDECKT | alle drei Teilaufgaben ausgeführt, alle sechs Lieferobjekte vorhanden, Abhakliste vollständig |
| **Prozess** | 25 % | Vorgehen dokumentiert, reflektiert, Grenzen aufgezeigt | ABGEDECKT | `sec:evaluation_reflexion`, `sec:iteratives_design`, Limitationen dreischichtig |
| **Transfer** | 15 % | Technologie ↔ gesellschaftliche/wirtschaftliche Bedeutung, Ansätze begründet | ABGEDECKT | SDG 12.3 (`01_ausgangslage:5`), Freemium-Modell mit Begründung (`03_konzept:3`), Drivers/Levers, Nudge, Osmosis, Gamification je mit Beleg |
| **Kreativität** | 15 % | Vergleich zu bestehendem Produkt + Innovationskraft | ABGEDECKT | `sec:wettbewerbsanalyse` mit sechs Plattformen; Innovationsabsatz `03_konzept:15` trennt Neues von bewusst Übernommenem. *Einschränkung:* Befund 1 sitzt im Vergleichsteil dieser Dimension |
| **Dokumentation** | 10 % | Entstehungsgeschichte lückenlos | ABGEDECKT | `06:5`, `06:7`, `06:9` plus `tab:phasenplanung`. *Einschränkung:* Befund 2 betrifft genau diesen Absatz |
| **Ressourcen** | 10 % | Zeit/Material/Tools effizient | ABGEDECKT | `tab:phasenplanung` (Ressourcenspalte je Phase), Budgethinweis `05:23`, drei Risiken mit Mitigation |

---

## Lieferobjekt-Abgleich

- [PASS] **Wettbewerbsvergleich (Tabelle)** – `tab:wettbewerbsvergleich`, sechs Plattformen × fünf Kriterien.
- [PASS] **Zielgruppen-/Persona-Beschreibung (Text/Abbildung)** – `sec:zielgruppe` plus `tab:persona` in Anhang A, mit Portraitfoto (Urheberin und Lizenz ausgewiesen).
- [PASS] **UI/UX-Skizze/Mockup (Abbildung)** – vier Mockups in Anhang C plus Style Tile in Anhang B. **Alle fünf Bilddateien einzeln per `Read` gesichtet**, nicht nur auf Existenz geprüft: Die Startseite zeigt die Reste-Eingabe als Chip-Tags, Rezeptkarten mit Zubereitungszeit und „2 Zutaten fehlen", das Wochenplan-Banner und das Lesezeichen-Icon; die Bookmark-Variante zeigt den ausgeklappten Bereich „Gespeicherte Rezepte"; der Rettungs-Feed zeigt Challenge-Banner mit Rangliste („Platz 4"), einen Beitrag mit Foto, Nutzername, Zutaten-Tag sowie Like- und Kommentar-Icon und den frei stehenden Plus-Button; das Profil zeigt Level-Badge „Level 4 — Resteheld:in", 1.240 Rettungspunkte mit Fortschrittsbalken, „12,4 kg Lebensmittel gerettet", das Reste-Journal mit Punktevergabe und das Raster eigener Beiträge. **Jede im Text behauptete Oberflächen-Eigenschaft ist im Bild belegt.**
- [PASS] **Plattformname** – „Resteria", hergeleitet in `03_konzept:3`, Namenskollision dokumentiert in `06:9`.
- [PASS] **Funktionsübersicht** – `tab:funktionsuebersicht`, sechs Funktionen mit Kurzbeschreibung und Herleitung.
- [PASS] **Phasenplanung (Tabelle)** – `tab:phasenplanung`, fünf Phasen mit Zeitrahmen und Ressourcen.
- [PASS] **`pages/appendix.tex`** enthält echten Inhalt, nicht nur Kommentare; kein im Text behauptetes Artefakt fehlt (Grep über „Prototyp", „Formular", „Skizze", „Erhebung": alle Treffer verweisen auf Geplantes oder auf ein vorliegendes Objekt).

---

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)

1. **Befund 1 – Kriterium „Rezept-Austausch" definieren** (`01_wettbewerbsanalyse.tex:15`, Variante (a), ~15 Wörter). Größter Hebel: −10. Berührt weder These noch Kernargumente noch eine per Freigabe fixierte Formulierung.
2. **Befund 2 – Absatz `:7` in `06_evaluation_reflexion.tex` vor `:5` ziehen.** −2, reine Verschiebung, ±0 Wörter.
3. **Kosmetik in einem Aufwasch, falls ohnehin gebaut wird:** „ein Risiko **ist** das dichte Umfeld" (`01_wettbewerbsanalyse.tex:36`, +1 Wort) · „gilt auch hier **der** Maßstab" (`07_iteratives_design.tex:5`, −1 Wort) · optional die Absatzteilung in `03_konzept.tex:9`.
4. **Danach neu bauen und die gedruckte Seitenzahl gegenprüfen.** Der Textteil steht exakt auf der Obergrenze 10; die gemessene Reserve auf der letzten Textseite beträgt ≈ 173 pt ≈ 10 Zeilen, die Änderungen aus 1–3 kosten netto rund eine Zeile. Ein Kippen auf 11 Seiten ist unwahrscheinlich – beweisen kann es nur der Build.
5. **`main.pdf` einchecken.** `git status` meldet `M main.pdf`; zusätzlich liegt die abgabefertig benannte Kopie `20260731_Pelz_Sascha_3210267_DLBMIMPFS01-01.pdf` untracked im Root. **Beide sind inhaltlich identisch mit dem in diesem Audit gebauten PDF** (Textvergleich über alle 23 Seiten: deckungsgleich) – es besteht also kein Aktualitätsproblem, nur ein Versionierungsschritt. Werden 1–3 umgesetzt, muss die Abgabekopie danach neu erzeugt werden.

**Nicht in dieser Session weiterarbeiten.** Für die Überarbeitung eine frische Session öffnen: „Schreib-Modus: Überarbeitung nach Prüfbericht". Danach genügt ein Delta-Re-Audit; erwarteter Score nach vollständiger Umsetzung: **100/100**.

**Werden 1–3 bewusst nicht umgesetzt, ist die Arbeit in diesem Stand einreichbar** – 88/100 liegt deutlich über der Abgabeschwelle, und beide Befunde sind Nachvollziehbarkeits- und Lesbarkeitspunkte ohne Wirkung auf Substanz, Belege oder Formalia.

---

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

1. **Eidesstattliche Erklärung elektronisch über myCampus abgeben** – ohne sie nimmt Turnitin die Einreichung nicht an. Das Fristfeld in `CLAUDE.md` steht auf `[offen]`.
2. **Einreichungs-Anleitung im myCampus-Kurs lesen.**
3. **LanguageTool-Durchgang lokal über den Gesamttext** (3.710 Wörter). Die Sprachstichprobe dieses Audits hat zwei Absätze je Hauptkapitel geprüft und ersetzt keine Vollprüfung.
4. **Die Arbeit einmal am fertigen PDF am Stück durchlesen.**
5. **Keine externe Plagiatssoftware vorab** – Selbsttreffer-Risiko bei Turnitin.
6. **Prompt-Wortlaut der fünf Abbildungen gegen den Claude-Design-Chatverlauf abgleichen** (siehe „Bitte manuell prüfen", Punkt 1).
7. **Auf myCampus prüfen, ob Zitierleitfaden und Gestaltungsrichtlinien noch den Stand 01.10.2025 tragen** (siehe „Bitte manuell prüfen", Punkt 2). Danach in `_shared/quellen-versionen.md` die Spalte „zuletzt vom Nutzer bestätigt" setzen.
8. **Namensverfügbarkeit „Resteria"** (DPMA, `.de`-Domain) – nicht abgabekritisch, aber offen.
9. **Das eingereichte PDF muss aus dem letzten Build stammen.** Wird nach diesem Audit noch etwas geändert: neu bauen, Seitenzahl gegen 7–10 prüfen, Abgabekopie neu erzeugen.

---

## Nachtrag – Abarbeitung (31.07.2026, `schreib-modus`-Sitzung)

Handlungsempfehlungen 1–3 vollständig umgesetzt; der Bericht oben bleibt als Momentaufnahme des Audit-Stands unverändert stehen.

- **Befund 1 – erledigt, Variante (a).** `01_wettbewerbsanalyse.tex:15` trägt jetzt zwischen der Kommunikations- und der Entdeckungs-Definition den Satz: „Rezept-Austausch bezieht sich dagegen allein auf die Rezepte selbst, also darauf, ob eine Plattform sie bereitstellt und weitergibt; die Spanne reicht von der reinen Rezeptdatenbank bis zum Einstellen eigener Beiträge durch Nutzer:innen." (+33 Wörter). **Alle sechs Wertungen der Spalte einzeln gegen die neue Definition geprüft, keine Zelle geändert:** Chefkoch „stark" (`:3`) · TikTok „mittel" (`:5`) · Restegourmet „mittel" (Rezeptvorschläge und Kochbuch bereitgestellt, kein Einstellen, `:7`) · `\ac{BMLEH}`-App „mittel" (umfangreiche Rezeptdatenbank, `:7`) · leftovercooking „mittel" (`:9`) · Foodsharing „schwach" (`:11`). `:36`, `:38` und `02_limitationen:7` bleiben unberührt, wie im Bericht gegengeprüft; ein Zwilling in der Einleitung existiert nicht (die Lücken-Begründung dort läuft über die kostenlose Resteverwertung, nicht über die Vergleichsachsen).
- **Befund 2 – erledigt.** `06_evaluation_reflexion.tex`: Entstehungsgeschichte-Absatz vor den Methoden-/Kursänderungs-Absatz gezogen, ±0 Wörter, kein `\autoref` und keine Zitation betroffen. Neue Reihenfolge wie empfohlen.
- **Handlungsempfehlung 3 – erledigt**, einschließlich des optionalen Punktes: „ein Risiko **ist** das dichte Umfeld" (`01_wettbewerbsanalyse.tex:36`, +1 Wort) · „gilt auch hier **der** Maßstab" (`07_iteratives_design.tex:5`, −1 Wort) · Absatzteilung in `03_konzept.tex:9` vor „Ergänzend plant Resteria …" (±0 Wörter, beide Hälften mit eigenen Belegen).
- **Prüfungen:** `check_all.py --kapitel chapters/02_durchfuehrung --mit-quellen` — alle sieben Skripte ohne harte Funde, `check_formalia.py` 0 FEHLER, `check_bib_hygiene.py` 0 Hinweise, `check_autoref.py` 24 Verweise unverändert quittiert. `check_quellentreue.py --datei chapters/`: **19/19 FUNDSTELLE OK**. `check_umfang.py`: **3.743 Wörter** (Korridor 2.625–3.750), netto **+33 Wörter**.
- **Offen (Nutzer-Schritte, Handlungsempfehlung 4 und 5):** Neubau mit Seitenkontrolle, `main.pdf` einchecken, Abgabekopie neu erzeugen. Danach Delta-Re-Audit, erwarteter Score 100/100.
