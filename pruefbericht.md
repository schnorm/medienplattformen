# Prüfbericht — Projektbericht

**Datum**: 24.07.2026 · **Geprüfter Stand**: alle Kapitel (15 Dateien, Stand nach `AENDERUNGEN.md` Runde 6) · **Audit-Typ**: Voll-Audit
**Score: 49/100 — nicht einreichen, ein Prüf-Schreib-Zyklus vor der Abgabe**

**Einordnung des Scores vorweg**: Alle fünf Befunde sind mechanisch und in einer einzigen Schreib-Session behebbar; keiner betrifft These, Argumentation oder Aufgabenerfüllung. Die Abzugstabelle des Prüf-Modus kennt keine Teilstufen — ein Pflichtregel-Verstoß kostet 15 Punkte, egal ob eine ganze Sektion fehlt oder ein Halbsatz. Der Score sagt hier also: „vor der Abgabe muss noch eine Runde laufen", nicht „die Arbeit ist inhaltlich schwach". Nach der Überarbeitung ist ein Delta-Re-Audit im abgabereifen Bereich zu erwarten.

**Vorbedingungen geprüft**: Gegenlesung (Runden 5 und 6) und Gesamt-Stresstest (Runde 2, GS-1…GS-6) sind gelaufen und abgearbeitet; `AENDERUNGEN.md` → „Offen" ist bis auf Befund 6.3 leer. **Befund 6.3 (Plus-Button-Überlapp im Rettungs-Feed-Mockup) wurde auf ausdrückliche Nutzer-Anweisung aus diesem Audit ausgenommen** und ist weder als Fund noch als Abzug gewertet.

**Memory-Hinweise berücksichtigt**: `MEMORY.md` — Teil-Check E fließt in keinem Umfang in den Score ein (Nutzer-Festlegung 2026-07-19). `PERSISTENT.md` — `\SubmissionDate` bewusst auf `\today`; Grundprinzip „Erst prüfen, dann behaupten" angewandt (Prüfer-Anmerkung, ZITIERREGEL im Kapitelplan und `references.bib` vor jeder Formalia-Aussage konsultiert).

---

## Teil-Check A — Formalia

- [**FAIL**] **Zitationen** — narrative Nennung und Klammerzitat doppeln den Autornamen (Befund 1). BBT-Keys selbst fehlerfrei: `check_bib_keys.py` meldet 6/6 Keys valide, keine ungenutzten Einträge.
- [PASS] Eigene Werke — `\quelle{}` unter jeder eigenen Abbildung/Tabelle (`tab:wettbewerbsvergleich`, `tab:funktionsuebersicht`, `tab:phasenplanung`, `tab:persona`, `fig:konzeptfluss`), Caption jeweils über dem Objekt, kein `\cite{}` auf Eigenleistung. Die vier KI-Mockups tragen korrekt statt „Eigene Darstellung" die vollständige Prompt-, Werkzeug- und Nachbearbeitungsangabe.
- [PASS] Pronomen — `check_formalia.py`: 0 Treffer. Selbstbezug durchgehend pronomenfrei („diese Arbeit", „dieser Bericht").
- [PASS] LaTeX-Format — `check_formalia.py`: **0 FEHLER** über alle 15 Dateien (12 HINWEIS, siehe unten). Float `[H]`, Caption vor `\label{}`, `~\autoref`, `\enquote{}`, TikZ mit den vordefinierten Styles `box`/`arr`, `\input{}` statt `\include{}` in den Kapiteln — alles regelkonform.
- [**FAIL**] **Akronyme** — drei Abkürzungen ohne Einführung und ohne Eintrag in `pages/acronyms.tex` (Befund 2). `\ac{MVP}` ist dagegen korrekt gesetzt und definiert.
- [PASS] Cross-References & Labels — Präfixe `sec:`/`fig:`/`tab:` durchgehend konsistent, alle `\autoref`-Ziele existieren, keine doppelten Labels.
- [PASS] Anti-KI-Stil — fünf ausgeprägte „nicht X, sondern Y"-Konstruktionen auf geschätzt 9–10 Seiten (Regel: höchstens eine pro Seite). Runde 6 (Befund 6.9) hat hier gewirkt. Die TRIAS-Hinweise des Skripts sind Tabellenzellen mit sachlich genau drei Elementen und fallen unter die ausdrückliche Ausnahme der Regel.
- [PASS] Verständlichkeit — drei Sätze über 30 Wörter im gesamten Fließtext (37/33/33), Fachbegriffe werden fast durchgängig bei Erstnennung erklärt (Nudge, Drivers/Levers, MVP, UI/UX, Fairteiler, Influence by Osmosis). Die übrigen Satzlängen-Ausreißer des Skripts betreffen ausschließlich Tabellenzeilen. Drei kleinere Klarheits-Hinweise stehen unter „Kosmetik".
- [PASS] Quellen-Sperrliste — keine Skripte, Vorlesungsfolien oder Webinars zitiert. Die sechs Plattform-Domains stehen korrekt als eigene Sichtung in der `\quelle{}`-Zeile, nicht als `\parencite` (deckt sich mit der ZITIERREGEL in `kapitelplan.md`).
- [PASS] `main.tex` / `pages/cover.tex` unverändert seit der einmalig freigegebenen Änderung vom 23.07.2026 (Commit 44b115b); `references.bib` seither nicht angefasst. Projektangaben vollständig und ausschließlich in `pages/meta.tex`.
- [PASS] Offene `% UNVERIFIED:`-Marker — keine (`grep` über `chapters/` und `pages/`).
- [PASS] Quellenlose Kapitel — die Wettbewerbsanalyse trägt seit Runde 6 einen Methodensatz (Z. 15) plus sechs Domains und Sichtungsdatum in der `\quelle{}`-Zeile. Nachvollziehbarkeit gegeben.

## Teil-Check B — Argumentationsqualität (nur Pflicht-Punkte aus `typen/projektbericht.md` als FAIL)

- [PASS] These erkennbar, Leitfrage und These getrennt — Ziel in `02_zielsetzung_und_verengung.tex:3`, Kernthese (Kombination Reste-Matching + Social-Community) trägt Kapitel 2 und 3.
- [N.A.] Forschungslücke in der Einleitung — laut Typ-Datei optional.
- [PASS] Aktualität/Zeitbezug in der Einleitung — Pflicht, erfüllt über SDG 12.3 und Vittuari et al. (`01_ausgangslage_und_problem.tex:5`).
- [PASS] Gegenargumente reflektiert und entkräftet — vier Einwände in `01_wettbewerbsanalyse.tex:36`, SDG-versus-Nische-Spannung in `06_evaluation_reflexion.tex:5`. (Inhaltlich stark; der Widerspruch in Befund 3 betrifft die Schlussfolgerung, nicht die Reflexion selbst.)
- [PASS] Syntheseleistung pro Hauptkapitel — Kapitel 2 führt Marktbeobachtung, Verhaltensliteratur und eigene Konzeptleistung zusammen und trennt die Stützarten sauber (`03_konzept.tex:30`).
- [**FAIL**] **Limitationen dreischichtig** — Limitation 2 fehlt die Mitigations-Schicht (Befund 5).
- [N.A.] Ergebnisse ≠ Interpretation — laut Typ-Datei entfällt beim Projektbericht.
- [PASS] Typspezifisch (Projektbericht): dritte Person streng ✓ (siehe Anmerkung unten) · „Quelle: Eigene Darstellung." auf jeder eigenen Abb./Tab. ✓ · Produkt sichtbar dokumentiert ✓ (vier Mockups, Funktionsübersicht, Funktionslogik-Diagramm) · Phasenplanung als Tabelle ✓ · Reflexion mit Theorie-Praxis-Bezug ✓ · Quellen 5–10 ✓ (6).
- [PASS] Leitfragen aus `aufgabe.md` beantwortet — alle drei Teilaufgaben real ausgeführt, keine durch Simulation ersetzt. Teilaufgabe 3 verlangt ausdrücklich nur eine Beschreibung; `07_iteratives_design.tex:5` weist den geplanten Charakter korrekt aus.
- [PASS] Wörtliche Abhakliste — alle Berichtsinhalte und Schlüsselbegriffe per Grep belegt; die beiden Auslassungen (Event-Kalender, Gruppen/Foren) sind ausdrücklich und begründet ausgeschlossen, nicht übergangen. Die `[VERENGT]`-Begründung steht im Text.
- [PASS mit Hinweis] Genannte Materialien — Hansch & Rentschler (2012) und Kapoor et al. (2018) fehlen weiterhin in `references.bib`. Laut `aufgabe.md:26` ausdrücklich **nicht verpflichtend**, daher kein FAIL. Die Aufnahme wurde inzwischen dreimal bewusst übersprungen (Runden 1, 3, 6), weil `references.bib` nur per Zotero/BBT-Export befüllt werden darf. Siehe „Vor der Einreichung".
- [PASS] Dimensionsabgleich gegen die Abdeckungs-Tabelle in `kapitelplan.md` — alle sechs Bewertungskriterien mit allen Dimensionen im Text auffindbar; die beiden in Runde 6 als schwach markierten Dimensionen (Innovationskraft, Entstehungsgeschichte) sind seither ausgeschrieben (`03_konzept.tex:53`, `06_evaluation_reflexion.tex:9`).

**Anmerkung zur Voice**: `typen/projektbericht.md` schreibt „Die Projektgruppe …" als dritte-Person-Form vor. Die Arbeit nutzt stattdessen durchgehend pronomenfreie Selbstbezüge. Das ist eine begründete, projektspezifische Abweichung: Die Prüfer-Anmerkung adressiert ausdrücklich eine Einzelperson („Du bist also Projektverantwortliche"), es gibt kein Team. Die Regelabsicht — kein „ich/wir/man" — ist vollständig erfüllt. **Kein FAIL.** Die Entscheidung sollte als `[LERNEN:stil]`-Eintrag nach `PERSISTENT.md`, damit sie beim nächsten Projekt nicht erneut aufgerollt wird (siehe „Vor der Einreichung").

## Teil-Check C — Struktur

- [PASS] ½-Seiten-Regel — kleinste Datei 153 Wörter (`07_iteratives_design.tex`), keine HALBSEITE-Meldung des Skripts.
- [PASS] Max. 2–3 Sätze zwischen Kapitel-Überschrift und erstem Unterkapitel — Einleitung 2, Durchführung 3, Fazit 2.
- [PASS] Max. 3 Kapitelstufen — `\section` → `\subsection`, im Anhang unnummerierte `\subsubsection*`.
- [PASS] Mindestens 2 Unterpunkte pro Kapitel — 3 / 7 / 2.
- [PASS] Front-/Backmatter — Abbildungsverzeichnis (5 Abbildungen) und Tabellenverzeichnis (4 Tabellen) liegen beide über der Dreier-Schwelle und sind eingebunden; Literaturverzeichnis vor dem Anhang; Anhang A und B fortlaufend gekennzeichnet, je mehrfach im Text verwiesen; Anhangsverzeichnis vorhanden und seit Runde 6 im Inhaltsverzeichnis verlinkt.
- [PASS] Outline-Check — Einleitung (Umfeld, Problem, Ziel, Vorgehen, Aufbau) → Hauptteil (Analyse, Zielgruppe, Konzept, Community, Iteration, Phasenplanung, Evaluation/Reflexion) → Fazit (Kernergebnisse, Ausblick, Limitationen). Identisch mit dem Kapitelgerüst aus `typen/projektbericht.md` und mit `kapitelplan.md` inklusive der in Runde 5 ergänzten Subsection `sec:iteratives_design`.
- [PASS] Kapitelanteile — 581 / 3.677 / 612 Wörter = 11,9 / 75,5 / 12,6 %, innerhalb der Vorgabe 10–15 / 70–80 / 10–15 %.

**Roter Faden (kapitelübergreifend)** — der Gesamt-Stresstest ist gelaufen (Runde 2), daher gemäß Skill kein vollständiger Zweitdurchgang, sondern Regressionsprüfung der seither geänderten Stellen:

- [**FAIL**] Widerspruch an der tragenden Aussage (Befund 3).
- [**FAIL**] Zeitlinien- und Akteurskonsistenz bei der ersten Feedback-Schleife (Befund 4).
- [PASS] Zahlenangaben nachgezählt: „drei Merkmale" (3 ✓), „drei weitere Kernfunktionen" (3 ✓), „drei Hauptbereiche" (3 ✓), „fünf Phasen" (5 Tabellenzeilen ✓), „zwei Risiken" (2 ✓), „drei Lehren" (3 ✓), „sechs Vertreter aus drei Plattform-Kategorien" (6 Tabellenzeilen, 3 Kategorien ✓), „ein bis drei Vertreter" je Kategorie (2/3/1 ✓), „mehrere Einwände / drei naheliegende Gegenargumente" (3 kurz abgehandelte + 1 gewichtigerer ✓ — der in Runde 4 entstandene Zählfehler ist behoben und nicht zurückgekehrt).
- [PASS] Kernbegriffs-Konsistenz — „Reste-Matching", „echte Social-Community", „Rettungspunkte", „Reste-Level", „Rettungs-Feed" laufen wortgleich durch alle drei Kapitel und die Tabellen.
- [PASS] Tabellenwertungen spaltenweise gegen die Kriteriendefinition (`01_wettbewerbsanalyse.tex:13`) geprüft — die Wertungen liegen je Kriterium auf einer Achse, kein Maßstabsbruch, keine Gefälligkeitswertung zugunsten des eigenen Konzepts. Eine Zelle ist unbelegt, siehe „Kosmetik".
- [PASS] Kriterienart einheitlich — alle fünf Spalten sind Merkmale, kein zusammenfassendes Gesamturteil als gleichrangige Spalte.
- [PASS] Offene Einwände — jeder selbst erhobene Einwand wird beantwortet oder als Limitation ausgewiesen; das Reichweitenrisiko des osmotischen Kanals ist in `06_evaluation_reflexion.tex:5` ausdrücklich benannt.
- [PASS] Redundanz Reflexion ↔ Fazit — saubere Arbeitsteilung: `06_evaluation_reflexion.tex:7` behandelt das Vorgehen, `02_limitationen.tex:3` ausdrücklich die Geltung der Ergebnisse; die Trennung wird im Text sogar explizit benannt.
- [PASS] Lieferobjekt-Abgleich — alle sechs Lieferobjekte aus `aufgabe.md` liegen vor: Wettbewerbsvergleich (`tab:wettbewerbsvergleich`), Persona (`tab:persona`, Anhang A), UI/UX-Mockups (vier Abbildungen, Anhang B), Plattformname (`03_konzept.tex:3`), Funktionsübersicht (`tab:funktionsuebersicht`), Phasenplanung (`tab:phasenplanung`). `pages/appendix.tex` enthält realen Inhalt. Die Grep-Kontrolle auf behauptete, aber nicht beiliegende Artefakte ergab **einen** Treffer — den Klick-Prototyp, siehe Befund 4.

## Teil-Check D — Build

- [ÜBERSPRUNGEN] Kompiliert fehlerfrei — `lualatex`, `latexmk` und `biber` sind in dieser Umgebung nicht installiert. Kein Abzug, da nicht prüfbar; statisch ist die Arbeit sauber (0 FEHLER im Formalia-Skript, alle Labels und Bilddateien vorhanden, `images/durchfuehrung/` enthält alle vier referenzierten PNG).
- [ÜBERSPRUNGEN] Undefined references/citations, fehlende Bilder, doppelte Labels — statisch geprüft, keine Auffälligkeiten; die Laufzeitprüfung bleibt Nutzer-Schritt.
- [ÜBERSPRUNGEN] Seitenumfang — gemessen 4.870 Wörter Fließtext einschließlich Tabellenzellen. Schätzung bei Arial 11 pt, 1,5-zeilig, 2 cm Rändern: **9–10 Seiten**, damit im Soll von 7–10, aber am oberen Rand. Kein Abzug, da nicht messbar; **die Bestätigung per lokalem Build ist der wichtigste offene Nutzer-Schritt**, weil ein Überschreiten laut IU-Richtlinien Punktabzug bedeuten kann.

## Teil-Check E — Abgabe (informativ, kein Score-Abzug)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben — Status laut `CLAUDE.md` → Fristen: offen. **Ohne diesen Schritt nimmt Turnitin die Einreichung nicht an.**
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen.
- [PASS, unbestätigt] Umfang im Soll — Spiegel aus Teil-Check D, Schätzung 9–10 von 7–10 Seiten.
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko).
- [ERINNERT] LanguageTool-Durchgang lokal über den Gesamttext — Sprache zählt in die Bewertung, und seit dem letzten Voll-Audit wurden über mehrere Änderungsrunden hinweg zahlreiche Sätze umformuliert.

---

## Befunde im Detail

### Befund 1 — Zitationen: Autorname steht doppelt (Formalia, −8)

**Wo**: `03_konzept.tex:7, :28 (2×), :30` · `04_community_und_feedback.tex:5, :7` · `01_kernergebnisse_und_ausblick.tex:5 (4×)` · `02_limitationen.tex:3` — elf Stellen.

**Was**: Die Arbeit nennt die Autorenschaft im Satz („Vittuari et al. unterscheiden …", „Barker et al. identifizieren …", „Nivedhitha et al. zeigen …", „eine Feldstudie von Soma et al.", „den Shen et al. als … beschreiben") und hängt an denselben Satz zusätzlich ein `\parencite`. `main.tex:207` lädt biblatex mit `style=apa`; `\parencite` erzeugt dort die volle Klammer inklusive Autornamen. Gerendert steht also: „Vittuari et al. unterscheiden zwischen „Drivers" … (Vittuari et al., 2023, S. 1)." — der Name erscheint zweimal im selben Satz. `\textcite` kommt in der gesamten Arbeit **kein einziges Mal** vor.

**Warum es zählt**: `hard-rules-formal.md` regelt genau diesen Fall: „Wenn die Autorenschaft selbst Thema des Satzes ist …, narrativ mit `\textcite[S. X]{key}` zitieren; sonst `\parencite`." Nach APA 7 ist die Doppelnennung ein Formfehler, nicht nur ein Stilproblem. Betroffen sind elf von dreizehn Fließtext-Zitaten — also praktisch die gesamte Zitierpraxis der Arbeit.

**Anweisung**: An den elf genannten Stellen `\parencite[…]{key}` durch `\textcite[…]{key}` ersetzen **und** dabei die vorangestellte Namensnennung im Satz streichen, weil `\textcite` Autor und Jahr selbst setzt. Beispiel: „Vittuari et al. unterscheiden … \parencite[S. 1]{vittuariHowReduceConsumer2023}" wird zu „\textcite[S. 1]{vittuariHowReduceConsumer2023} unterscheiden …". Die drei `\parencite` in den Tabellenzellen von `tab:funktionsuebersicht` und die beiden echten Klammerzitate in `01_ausgangslage_und_problem.tex:5` bleiben unverändert — dort ist die Autorenschaft nicht Thema des Satzes. Anschließend `check_bib_keys.py` erneut laufen lassen (`\textcite` läuft über dieselbe Validierung).

**Hinweis zur Historie**: Dieser Befund ist keine Regression aus den Runden 4–6, sondern besteht seit dem Erstschreiben. Die Voll-Audits vom 23.07. haben ihn übersehen, weil `check_formalia.py` die Unterscheidung narrativ/parenthetisch nicht prüft und der manuelle Zitations-Check auf Keys und Seitenangaben fokussiert war. Ein entsprechender Skript-Check wäre eine sinnvolle Ergänzung (Notiz für `SKILL-VERBESSERUNGEN.md`).

### Befund 2 — Drei Abkürzungen ohne Einführung (Formalia, −8)

**Wo**: `BMEL` — `01_ausgangslage_und_problem.tex:7` (Erstnennung), danach `01_wettbewerbsanalyse.tex` 5×, `03_konzept.tex:9`, `01_kernergebnisse_und_ausblick.tex:3`, `02_limitationen.tex:7`. `SDG` — `06_evaluation_reflexion.tex:5` (2×). `USP` — `01_wettbewerbsanalyse.tex:36`.

**Was**: Keine der drei Abkürzungen wird bei Erstnennung aufgelöst, keine steht in `pages/acronyms.tex`. Bei „SDG" ist das besonders auffällig, weil die Einleitung dasselbe Konzept ausgeschrieben einführt („Das Nachhaltigkeitsziel 12.3 der Vereinten Nationen") — die Abkürzung taucht dann erst viel später und unverbunden auf. „USP" erscheint genau einmal, mitten im tragenden Argumentationsabsatz.

**Warum es zählt**: `hard-rules-formal.md` verlangt `\ac{}` mit Definition in `pages/acronyms.tex` für alle verwendeten, nicht allgemein geläufigen Abkürzungen sowie die Erklärung jedes Fachbegriffs bei Erstnennung. Die Arbeit hält das sonst vorbildlich ein — sie erklärt MVP, Nudge, Drivers/Levers, UI/UX, Fairteiler und Influence by Osmosis. Genau diese Sorgfalt macht die drei Ausreißer sichtbar.

**Anweisung**: Für BMEL und SDG je einen `\acro{}`-Eintrag in `pages/acronyms.tex` ergänzen (`\acro{BMEL}{Bundesministerium für Ernährung und Landwirtschaft}`, `\acro{SDG}{Sustainable Development Goal}`) und die Fundstellen auf `\ac{}` umstellen; die Erstnennung löst das Paket dann automatisch auf. Für „USP" ist der einfachere Weg, die Abkürzung im Zuge von Befund 3 ganz aufzulösen („Das Alleinstellungsmerkmal von Resteria …") statt sie ins Verzeichnis aufzunehmen — eine einmalig verwendete Abkürzung ist genau der Bequemlichkeitsfall, den die Regel ausschließt.

### Befund 3 — Widerspruch an der tragenden Aussage (Struktur, −10)

**Wo**: `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:36`, vorletzter Satz.

**Was**: Der Absatz entkräftet den Einwand, eine reine Community-Plattform mit Nachhaltigkeitsthema könnte genügen, mit dem Argument, ohne Matching-Werkzeug müssten Nutzer:innen weiterhin selbst suchen. Daraus folgert er: „Die USP von Resteria liegt damit nicht im bloßen Verbinden beider Elemente, sondern in einer echten, wechselseitigen Social-Community obendrauf." Der unmittelbar folgende Satz sagt das Gegenteil: „Die Kombination aus Reste-Matching und echter Social-Community bleibt damit die eigentliche Lücke im untersuchten Marktumfeld." Zwei „damit"-Schlussfolgerungen hintereinander, die in entgegengesetzte Richtungen zeigen.

**Warum es zählt**: Die Kombination ist die Kernthese der gesamten Arbeit. Sie trägt `01_wettbewerbsanalyse.tex:34` („Die Stärke liegt in genau dieser Kombination"), das Kernargument von Kapitel 2 und das Fazit („Resteria verbindet beide Seiten in einem Konzept … Diese Differenzierung beruht auf der eigenen Wettbewerbsanalyse"). Ein Satz, der sie verneint, steht ausgerechnet im Absatz, der die Einwände abräumt — also dort, wo ein Prüfer besonders genau liest. Hinzu kommt, dass das „damit" logisch nicht trägt: Der vorangehende Satz verteidigt das Matching-Werkzeug, die Folgerung wertet es ab.

**Vermutete Absicht**: Gemeint ist offenbar eine Präzisierung gegen leftovercooking, das Matching und Creator-Community bereits ansatzweise verbindet — die Unterscheidung liegt dann in der *Wechselseitigkeit* der Community, nicht im Verbinden an sich. Diese Präzisierung ist richtig und wertvoll, sie steht nur an der falschen Stelle und in einer Formulierung, die die eigene These verneint.

**Anweisung**: Den Satz so umschreiben, dass er präzisiert statt verneint, etwa: „Das Alleinstellungsmerkmal von Resteria liegt damit in der Verbindung beider Elemente um eine wechselseitige Community herum, die über das Verfolgen von Creator-Inhalten hinausgeht." Damit ist die Abkürzung „USP" zugleich aufgelöst (Befund 2), und der Folgesatz steht wieder in derselben Richtung. Kein weiterer Eingriff nötig — die vier Einwände und ihre Entkräftung bleiben unverändert.

### Befund 4 — Erste Feedback-Schleife: falscher Akteur, nicht vorhandener Klick-Prototyp (Struktur, −10)

**Wo**: `chapters/02_durchfuehrung/07_iteratives_design.tex:3`.

**Was**: „In der Design-Phase (Woche 5--7, siehe `tab:phasenplanung`) prüft **dieser Bericht** Bedienführungs-Entscheidungen wie die Drei-Bereiche-Navigation aus `sec:konzept` **am Klick-Prototyp**, bevor sie in die MVP-Entwicklung übergehen." Der Bericht wird damit zum handelnden Akteur einer Phase des künftigen Umsetzungsfahrplans, und der Klick-Prototyp erscheint als vorhandenes Prüfobjekt. Tatsächlich ist der Klick-Prototyp ein geplantes Artefakt (`tab:phasenplanung`, Zeile „Design \& Prototyp", Woche 5–7); im Anhang liegen vier Mockups, kein Prototyp.

Verschärft wird das durch den Folgeabsatz: „Die Feedback-Schleifen **im weiteren** Entwicklungsprozess … sind ausschließlich als geplantes Vorgehen beschrieben, nicht real durchgeführt." Das Wort „im weiteren" grenzt die zuvor beschriebene erste Schleife ausdrücklich aus — ein Prüfer liest daraus, dass diese eine Schleife tatsächlich stattgefunden hat, und sucht vergeblich nach dem Beleg.

**Warum es zählt**: Die Prüfer-Anmerkung erlaubt KI-gestützte Designvorlagen nur ohne inhaltliche Fehler und fragt in Punkt 1d ausdrücklich nach Belegbarkeit des Vorgehens. Eine behauptete, aber nicht belegte Prüfung ist der teuerste Fehlertyp in diesem Kriterium — und sachlich unnötig, weil die Aufgabenstellung für Teilaufgabe 3 ausdrücklich nur eine *Beschreibung* geplanter Feedback-Schleifen verlangt. Die Arbeit macht sich hier grundlos angreifbar. Die Subsection ist in Runde 5 (Befund 5.2) neu entstanden und deshalb nie in einem Voll-Audit geprüft worden.

**Anweisung**: Den Satz in denselben Planungsmodus setzen wie den Folgeabsatz und den Akteur korrigieren, etwa: „In der Design-Phase (Woche 5--7, siehe `tab:phasenplanung`) sollen Bedienführungs-Entscheidungen wie die Drei-Bereiche-Navigation aus `sec:konzept` am Klick-Prototyp geprüft werden, bevor sie in die MVP-Entwicklung übergehen." Im Folgeabsatz zusätzlich „im weiteren Entwicklungsprozess" zu „im Entwicklungsprozess" kürzen, damit die Ausnahmelesart entfällt. Zwei Wortänderungen, kein Umfangseffekt. **Nicht** anfassen: `06_evaluation_reflexion.tex:9` — die dort beschriebene Mockup-Nachbesserungsrunde hat real stattgefunden und ist korrekt als Entstehungsgeschichte des Berichts ausgewiesen, nicht als Feedback-Schleife der Plattform.

### Befund 5 — Limitation 2 ohne Mitigations-Schicht (Pflichtregel Typ-Datei, −15)

**Wo**: `chapters/03_fazit/02_limitationen.tex:5`.

**Was**: `typen/projektbericht.md` führt „Limitationen dreischichtig (warum · Mitigation · zukünftige Projekte)" als Pflichtregel. Limitation 1 und Limitation 3 erfüllen das vollständig. Limitation 2 (KI-generiertes Mockup) nennt nur den Grund und den Zukunftsschritt (Usability-Test); die mittlere Schicht fehlt ersatzlos.

**Ursache**: Die Mitigation stand bis zur Kürzungsrunde im Text. Commit `3249b0f` („kürzungen", `AENDERUNGEN.md` Runde 4) hat drei Sätze entfernt: „Die Projektgruppe begegnet dieser Grenze auf zwei Wegen. Erstens ist die Herkunft des Mockups transparent gekennzeichnet, wie es der IU-Zitierleitfaden für KI-generierte Abbildungen verlangt. Zweitens konzentriert sich das Mockup auf die Kernfunktion Reste-Matching statt auf eine vollständige Ausarbeitung aller Bildschirme." Damit ist eine Pflicht-Schicht als Kollateralschaden einer Umfangskürzung weggefallen. Das Delta-Re-Audit vom 24.07. hat das nicht bemerkt, weil es nur die angekündigten Kürzungsbefunde nachgeprüft hat, nicht deren Wirkung auf die Pflichtregeln.

**Warum der Abzug so hoch ausfällt**: Die Abzugstabelle kennt für Pflicht-Punkte keine Teilstufen. Substanziell fehlt hier ein Halbsatz, formal ein Pflichtkriterium — der Score bildet das nicht differenziert ab. Inhaltlich ist das der leichteste der fünf Befunde.

**Anweisung**: Einen Mitigationssatz in `02_limitationen.tex:5` zwischen Grund und Zukunftsschritt einfügen, kürzer als das gestrichene Original, etwa: „Diese Grenze mildert der Bericht, indem die Herkunft des Mockups transparent gekennzeichnet ist und sich die Darstellung auf die Kernfunktion Reste-Matching statt auf eine vollständige Ausarbeitung aller Bildschirme beschränkt." Kosten: rund 30 Wörter. Angesichts des Umfangs am oberen Rand lässt sich das gegenfinanzieren, indem der letzte Satz des Kapitels (`02_limitationen.tex:9`, reiner Pointen-Schlusssatz, der den Ausblick aus `01_kernergebnisse_und_ausblick.tex:7` wiederholt) gestrichen wird.

## Kosmetik (kein Score-Abzug, freiwillig)

- `01_wettbewerbsanalyse.tex`, `tab:wettbewerbsvergleich`, Zelle BMEL-App / Rezept-Austausch: Die Wertung „mittel" ist die einzige Tabellenwertung ohne Entsprechung im Fließtext — bei Restegourmet („einfaches Teilen und Bewerten") und leftovercooking („Food-Creator:innen teilen eigene Rezepte") ist dieselbe Stufe jeweils belegt. Ein Prüfer, der spaltenweise liest, wird genau hier nachfragen. Ein Halbsatz in Z. 7 würde das schließen. Die Wertung selbst ist Ergebnis eigener Sichtung und wird hier nicht angezweifelt.
- `03_konzept.tex:28`: „Diese Mechanik greift zwei Befunde aus der Nudge-Forschung auf" — zwei Befunde stimmt (Barker, Nivedhitha), aber Nivedhitha et al. forschen zu Green Social Network Affordances, nicht zu Nudges. „aus der Verhaltensforschung" wäre präziser.
- `05_phasenplanung.tex:3` erklärt das MVP („die erste, funktionsfähige Version …"), doch die Erstnennung steht seit der Umstellung der `\input`-Reihenfolge in Runde 5 eine Subsection früher in `07_iteratives_design.tex:3`. Die Erklärung kommt also nach der Erstnennung. Der Halbsatz gehört nach `07_iteratives_design.tex:3` verschoben.
- `01_wettbewerbsanalyse.tex:36`: „was die Hürde ist, welche die Reste-Matching-Apps bereits gelöst haben" — eine Hürde wird genommen, ein Problem gelöst; „welche" ist zudem gestelzt. Vorschlag: „und genau diese Hürde nehmen die Reste-Matching-Apps den Nutzer:innen bereits ab".
- `02_zielgruppe.tex:7`: „ob sich am Ende weniger im Müll wiederfindet als vorher" — der Vergleichspunkt „als vorher" bleibt offen.

## Claims

- **Ungesicherte FACTUAL CLAIMS**: keine im Text. Zwei bekannte Verifikations-Vorbehalte bestehen fort (nicht neu, in `kapitelplan.md` und `CLAUDE.md` dokumentiert): Nivedhitha et al. (2024) und Shen et al. (2023) sind nur über das Abstract erschlossen, ein Volltext liegt nicht vor. Beide werden entsprechend vorsichtig und werkbezogen zitiert — formal korrekt, aber laut IU-KI-Richtlinie vom Nutzer am Original zu prüfen. Siehe „Vor der Einreichung".
- **Fehlende OWN WORK-Markierungen**: keine.
- **Ungenutzte Bib-Einträge**: keine (`check_bib_keys.py --report-unused`).

## Punkteabzug im Detail

| Kategorie | Abzug | Vorkommen |
|---|---|---|
| Fehlender Pflicht-Punkt aus Typ-Datei (Limitationen dreischichtig) | −15 | 1 (Deckel −45) |
| Struktur-Verstoß (Widerspruch tragende Aussage) | −10 | 1 |
| Struktur-Verstoß (Zeitlinie/Akteur, behauptetes Artefakt) | −10 | 1 (zusammen 2 von Deckel −30) |
| Formalia-Verstoß (Zitationen narrativ/parenthetisch) | −8 | 1 Prüfpunkt, 11 Stellen |
| Formalia-Verstoß (Akronyme) | −8 | 1 Prüfpunkt, 3 Abkürzungen (zusammen 2 von Deckel −32) |
| **Summe** | **−51** | **Score 49/100** |

Nicht abgezogen: Build (nicht prüfbar, ausgewiesen als ÜBERSPRUNGEN) · Seitenumfang (nicht messbar) · Teil-Check E (laut `MEMORY.md` nie score-relevant) · Anti-KI-Stil und Verständlichkeit (jeweils unter der Häufungsschwelle) · fehlende Einstiegsliteratur (laut `aufgabe.md` nicht verpflichtend).

## Bewertungsschwerpunkte (Projektbericht)

| Kriterium | Dimension | Stand | Fundstelle |
|---|---|---|---|
| Qualität (25 %) | Erfüllt das Ergebnis die Aufgabenstellung | ABGEDECKT | alle 3 Teilaufgaben, 4 Berichtsinhalte, 6 Lieferobjekte vorhanden |
| Prozess (25 %) | Vorgehen dokumentieren | ABGEDECKT | `03_vorgehen_und_aufbau.tex:3`, `01_wettbewerbsanalyse.tex:15`, `06_evaluation_reflexion.tex:9` |
| Prozess (25 %) | Vorgehen reflektieren | ABGEDECKT | `06_evaluation_reflexion.tex:7`, zwei konkrete Kursänderungen statt Leerformel |
| Prozess (25 %) | Grenzen aufzeigen | SCHWACH | `02_limitationen.tex:5` — Mitigations-Schicht fehlt (Befund 5) |
| Transfer (15 %) | Gesellschaftliche Bedeutung | ABGEDECKT | `01_ausgangslage_und_problem.tex:5`, Abwägung in `06_evaluation_reflexion.tex:5` |
| Transfer (15 %) | Wirtschaftliche Bedeutung | ABGEDECKT | `03_konzept.tex:5`, Freemium und Kooperationen; Community-Kollision in Runde 6 aufgelöst |
| Transfer (15 %) | Ansätze/Modelle begründen | ABGEDECKT | Drivers/Levers-Rahmen, jede Gamification-Funktion literaturgestützt |
| Kreativität (15 %) | Vergleich zu bestehendem Produkt | ABGEDECKT | `tab:wettbewerbsvergleich`, 6 Plattformen × 5 Kriterien, differenziert |
| Kreativität (15 %) | Innovationskraft | ABGEDECKT | `03_konzept.tex:53`, seit Runde 6 explizit ausgewiesen |
| Dokumentation (10 %) | Entstehungsgeschichte lückenlos | ABGEDECKT | `06_evaluation_reflexion.tex:9`, seit Runde 6 chronologisch |
| Ressourcen (10 %) | Zeit und Material effizient | ABGEDECKT | `tab:phasenplanung` mit Zeitrahmen, Ressourcenträgern, Abhängigkeiten, Puffer |

## Handlungsempfehlungen (nach Score-Hebel sortiert)

1. **Befund 5 — Mitigationssatz in `02_limitationen.tex:5` ergänzen** (+15). Größter Hebel, geringster Aufwand. Gegenfinanzierung über den Pointen-Schlusssatz in Z. 9.
2. **Befund 3 — Widerspruchssatz in `01_wettbewerbsanalyse.tex:36` umformulieren** (+10). Löst nebenbei die Abkürzung „USP" auf.
3. **Befund 4 — `07_iteratives_design.tex:3` in den Planungsmodus setzen, „im weiteren" streichen** (+10). Zwei Wortänderungen.
4. **Befund 1 — elf `\parencite` auf `\textcite` umstellen und die doppelten Namensnennungen streichen** (+8). Mechanisch, aber die meisten Einzelstellen; danach `check_bib_keys.py`.
5. **Befund 2 — `\acro{BMEL}` und `\acro{SDG}` in `pages/acronyms.tex`, Fundstellen auf `\ac{}` umstellen** (+8).
6. Optional: die fünf Kosmetik-Punkte. Kein Score-Effekt.

**Erwarteter Score nach vollständiger Umsetzung: 100/100.** Danach genügt ein Delta-Re-Audit (nur die fünf Befunde plus beide Skripte), kein weiterer Voll-Audit.

**Nächster Schritt**: neue Session, „Schreib-Modus: Überarbeitung nach Prüfbericht". Nicht in dieser Audit-Session weiterarbeiten — der Kontext trägt alle 15 Kapitel, und dieser Bericht enthält alles Nötige.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

- [ ] **Lokalen Build fahren** (`latexmk -lualatex main.tex`) — in dieser Umgebung nicht möglich. Danach prüfen: keine undefined references/citations, alle vier Mockups eingebunden, keine doppelten Labels.
- [ ] **Seitenumfang des Textteils bestätigen** (ab „1 Einleitung" bis vor das Literaturverzeichnis, inkl. Abbildungen/Tabellen im Text): Vorgabe 7–10 Seiten, Schätzung 9–10. Bei Überschreitung zuerst die Kosmetik-Kürzungen und den Schlusssatz in `02_limitationen.tex:9` nutzen.
- [ ] **Eidesstattliche Erklärung elektronisch über myCampus abgeben** — Voraussetzung dafür, dass Turnitin die Einreichung überhaupt annimmt.
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen.
- [ ] **LanguageTool-Durchgang lokal über den Gesamttext** — seit dem letzten Voll-Audit sind über mehrere Änderungsrunden viele Sätze umformuliert worden.
- [ ] **Nivedhitha et al. (2024) und Shen et al. (2023) am Volltext verifizieren**, sobald zugänglich (bisher nur Abstract; IU-KI-Richtlinie verlangt die Prüfung am Original). Die Formulierungen sind bewusst vorsichtig gehalten und tragen auch ohne Seitenangabe, weil sie werkbezogen zitieren.
- [ ] **Namensverfügbarkeit „Resteria" prüfen** (DPMA, .de-Domain) — offener Punkt seit der Plan-Phase.
- [ ] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko).
- [ ] Optional, seit Runde 1 dreimal bewusst übersprungen: Einstiegsliteratur Hansch & Rentschler (2012) und Kapoor et al. (2018) per Zotero/BBT nach `references.bib` importieren und je einmal zitieren. Laut `aufgabe.md` nicht verpflichtend; **entweder jetzt entscheiden oder als endgültig verworfen abhaken**, damit der Punkt nicht in jeder Runde erneut auftaucht.
- [ ] Nach bestandenem Abgabe-Audit: `MEMORY.md` Eintrag für Eintrag durchgehen und projektübergreifende Punkte nach `PERSISTENT.md` übertragen. Zwei Kandidaten aus diesem Audit: (a) die Voice-Abweichung „pronomenfreier Selbstbezug statt ‚Die Projektgruppe'" bei Einzelautorenschaft, (b) die Beobachtung, dass Kürzungsrunden Pflicht-Schichten mitreißen können und ein Delta-Re-Audit deshalb die Pflichtregeln der berührten Kapitel mitprüfen sollte.

## Anhang: Status-Abgleich (`check_status.py`)

`0 FEHLER, 10 HINWEIS(e)`. Zwei Arten, beide ohne inhaltliche Folge:

- Der Statuswert „ÜBERHOLT" in der Prüf-Audit-Zeile war kein zulässiger Wert — mit diesem Audit auf einen gültigen Wert korrigiert.
- Neun `DATEI-OHNE-ZEILE`-Hinweise für die Subsection-Dateien von Kapitel 2 und 3. Die Statustabelle führt bewusst Kapitel-Zeilen (`sec:einleitung`, `sec:durchfuehrung`, `sec:fazit`) statt einer Zeile je Subsection. Das ist die etablierte Konvention dieses Projekts und keine Inkonsistenz zwischen Tabelle und Dateisystem; das Skript kennt sie nur nicht.
