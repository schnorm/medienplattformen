# CLAUDE.md — Wissenschaftliches Schreiben an der IU

**Projekt:** [wird pro Arbeit ausgefüllt — Titel/Arbeitstitel] · **Papiertyp:** [Hausarbeit/Fallstudie/Seminararbeit/Projektbericht] · **Institution:** IU Internationale Hochschule

## Schnellreferenz — Session starten

| Du willst … | Schreibe in neuer Session |
|---|---|
| Umgebung prüfen (einmalig zu Beginn) | „Setup-Check" |
| Kapitelplan erstellen (Standard, 1 Session) | „Plan kompakt" |
| Kapitelplan ausführlich (empirische Seminararbeit) | „Plan ausführlich" |
| Nächstes Kapitel schreiben | „Schreib-Modus: nächstes Kapitel" |
| Ein Argument prüfen lassen | „Stresstest auf: <Argument>" |
| Arbeit mit fremden Augen gegen die Aufgabenstellung prüfen (alle Kapitel FERTIG) | „Gegenlesung" |
| Ganze Arbeit inhaltlich prüfen (sobald alle Kapitel FERTIG, **vor** dem Voll-Audit) | „Gesamt-Stresstest" |
| Erstes Kapitel gegenprüfen (früh, ohne Score) | „Audit Kapitel: <name>" |
| Kapitelplan auf Kohärenz prüfen (empfohlen vor dem Schreiben) | „Plan-Audit" |
| Mechanisch prüfen, ob das Schreiben starten kann | „Bereitschafts-Check" |
| Arbeit/Kapitelplan prüfen | „Audit" |
| Status erfahren | „Wo stehen wir?" |

## Grundprinzipien

- **Kompilieren ist Sache des Nutzers, nicht meine.** Nach Edits an `.tex`-Dateien nicht ad-hoc selbst `lualatex`/`latexmk` laufen lassen, um die eigene Änderung zu verifizieren — der Nutzer kompiliert lokal. Ausnahme: Teil-Check D (Build) im `pruef-modus` bleibt bestehen, da er ein bewusster, score-relevanter Audit-Bestandteil ist und kein Ad-hoc-Selbstcheck.
- **Dateien sind Wahrheit, nicht der Chat-Verlauf.** `aufgabe.md`, `kapitelplan.md`, `kapitelplan.draft.md` und `chapters/**/*.tex` gelten immer vor Erinnerung/Memory — bei Zweifel lesen, nicht annehmen.
- **Erst prüfen, dann behaupten.** Bevor eine belastbare Aussage über die Außenwelt (Marktlage, Konkurrenzprodukte, Werkzeuge, Zahlen) **oder** eine formale/prozedurale Behauptung („das ist ein Blocker", „so darf man nicht zitieren", „die Regel verlangt X") getroffen wird: die maßgebliche Quelle konsultieren — Web für Außenwelt-Fakten, die **Projektdatei** für interne Regeln (`aufgabe.md`, `sources/Anmerkungen vom Prüfer.md`, `hard-rules-formal.md`, `typen/<typ>.md`). Kein Rating, kein Blocker, keine Formalia-Aussage aus dem Gedächtnis. Im Zweifel als Hypothese kennzeichnen und verifizieren, nicht als Fakt formulieren.
- **`main.tex`, `pages/cover.tex` und `references.bib` nie verändern** (Ausnahme: `references.bib` per Zotero/BBT-Auto-Export) — gilt unabhängig vom aktiven Skill. Projektspezifische Angaben (Titel, Papiertyp, Modul, Tutor:in, Abgabedatum, PDF-Schlagworte) stehen **ausschließlich in `pages/meta.tex`** — einmalig beim Projektstart ausfüllen; `cover.tex` und die PDF-Metadaten ziehen sich alles von dort.
- **Single Source of Truth**: `aufgabe.md` für die Aufgabenstellung (destilliert in Plan-Modus Schritt 0 — spätere Sessions lesen diese Datei, nicht das Aufgaben-PDF), `kapitelplan.md` für Struktur/Argumentation, `chapters/**/*.tex` für den finalen Text, `references.bib` für Zitationen (nie manuell editieren).
- **These und Kernargumente kommen vom Nutzer.** Ich hinterfrage und schärfe, liefere aber nicht die inhaltliche Position selbst. Das ist zugleich die Bedingung der IU-KI-Richtlinie: Die Verantwortung für alle Inhalte liegt beim Studierenden; jede von mir gelieferte Quelle, Zahl oder Behauptung muss der Nutzer am Original verifizieren, bevor sie in die Arbeit übernommen wird.
- **Freigabepflichtige Punkte aktiv per `AskUserQuestion` klären, nicht nur im Fließtext vermerken.** Trägt ein Arbeitsauftrag (z. B. ein Punkt in `AENDERUNGEN.md`, `pruefbericht.md`) einen Vorbehalt wie „nur mit expliziter Freigabe ändern", oder betrifft er These/Kernargumente/Leitfrage, dann reicht es nicht, den Punkt auszulassen und die Begründung nur in der Zusammenfassung zu erwähnen — das verlagert die Entscheidung stillschweigend auf den Nutzer, der sie leicht überliest. Stattdessen noch in derselben Session aktiv nachfragen, bevor der nächste Schritt (Audit, Commit, PR) beginnt.
- **Keine personenbezogenen Daten in die Session geben** (KI-Richtlinie der IU): Interview-Transkripte vor der Verarbeitung anonymisieren (Namen → B1, B2 …), keine vertraulichen Unternehmensdaten ohne Freigabe.
- **Nur „Pflicht"-Regeln aus `typen/<typ>.md` zählen als FAIL.** „Optional"/„empfohlen" sind Hinweise, „entfällt" wird gar nicht geprüft.
- **Checkpoints und gespeicherte Dateien werden im Chat sichtbar quittiert**, nie nur still geschrieben (siehe `plan-modus`/`schreib-modus` → Sichtbarkeitspflicht).
- **Explizite Korrekturen des Nutzers sofort in `MEMORY.md` als `[LERNEN:kategorie]` eintragen** (nicht am Sessionende sammeln — Sessions enden abrupt) und quittieren („📝 In MEMORY.md gelernt: …"). Widersprüchliche neue Einträge markieren den alten als `[ÜBERHOLT]` (siehe `MEMORY.md` → Housekeeping). **Default ist `PERSISTENT.md`** — die Datei, die der Nutzer von Projekt zu Projekt kopiert. Ein `[LERNEN:...]`-Eintrag gehört nur dann nach `MEMORY.md`, wenn er sich konkret auf *diese* Arbeit bezieht (dieses Thema, dieser Papiertyp, diese Aufgabenstellung, dieses Kapitelgerüst). Alles zu Stil, Ton, Zitier-Sonderfällen, Modellwahl, Session-Führung und Reihenfolge der Arbeitsschritte ist projektübergreifend — sonst geht es beim nächsten Projekt verloren, denn nur diese eine Datei wandert mit. Überall, wo Skills `MEMORY.md` lesen, gilt: `PERSISTENT.md` + `MEMORY.md` lesen; bei Widerspruch gewinnt `MEMORY.md`.

## Session-Regeln (Memory-Management)

Kern des Workflows: **viele kurze Sessions statt einer großen.** Lange Sessions verbrennen Tokens und werden gegen Ende unzuverlässig. Deshalb:

1. **Session-Start-Ritual (<1 Min.):** Statustabelle unten + „Aktuelle Richtung" lesen → `PERSISTENT.md`-/`MEMORY.md`-Einträge beachten → nur die Dateien laden, die das heutige Arbeitspaket braucht (der aktive Skill listet sie). Nicht pauschal Plan und alle Kapitel einlesen.
2. **Arbeitspaket-Größen:** Plan kompakt = 1 Session · Plan ausführlich = 1–2 (**Schnitt idealerweise nach Schritt 1** — die Literaturrecherche ist der größte Kontextposten; ihr Ergebnis liegt destilliert im Draft, und Schritt 2–4 nutzt ohnehin ein anderes Modell) · Schreiben = 1 Hauptteil-Kapitel pro Session (**Ausnahme klein:** Einleitung + Schluss dürfen gemeinsam in eine Session — je ~10 %, inhaltlich zusammenhängend) · Audit = 1 Session (**Überarbeitung danach = eigene Schreib-Session** — `pruefbericht.md` trägt die Arbeitsliste hinüber, nicht im vollen Audit-Kontext weiterschreiben).
3. **Session-Ende-Ritual:** Checkpoint in der Draft-/Plan-Datei → Statustabelle aktualisieren → „Aktuelle Richtung" auf den nächsten Schritt setzen → im Chat quittieren.
4. **Kontext fast voll oder Session driftet?** Nicht „noch schnell fertig machen" — Checkpoint schreiben, Session beenden, frisch weitermachen. Die Dateien garantieren verlustfreie Fortsetzung.

## Ordnerstruktur

```
<latex-projektordner>/
├── CLAUDE.md                    # diese Datei, immer automatisch geladen
├── handbuch.md                  # Nutzer-Handbuch (einzige Quelle; handbuch.pdf ist daraus erzeugtes Derivat — generate_handbuch_pdf.py)
├── MEMORY.md                    # Korrekturen/Lernpunkte NUR für dieses Projekt
├── PERSISTENT.md                # projektübergreifende Dauer-Präferenzen — wandert per Kopie von Projekt zu Projekt
├── aufgabe.md                   # destillierte Aufgabenstellung (Plan-Modus Schritt 0) — Single Source statt Aufgaben-PDF
├── kapitelplan.draft.md         # Zwischenstand Plan-Modus (nach Abschluss: INSIGHT-Archiv)
├── kapitelplan.md               # finaler, bestätigter Kapitelplan
├── AENDERUNGEN.md               # Änderungsaufträge in Runden (aus Gesamt-Stresstest/Review/Nutzer-Feedback): je Punkt eine konkrete Anweisung; [FREIGABE]-Punkte nur nach aktiver Rückfrage umsetzen; Abarbeitung im schreib-modus, danach leeren und Delta-Re-Audit
├── pruefbericht.md              # letzter Audit-Bericht (Prüf-Modus überschreibt pro Lauf)
├── main.tex                     # Wurzeldokument — NIE ändern
├── references.bib               # BBT-Export aus Zotero — NIE manuell editieren
├── pages/
│   ├── meta.tex                 # Projektangaben — EINZIGE projektspezifische Stelle
│   ├── acronyms.tex             # Abkürzungsverzeichnis (\acro{}-Einträge)
│   ├── appendix.tex             # Anhang
│   ├── cover.tex                # Titelblatt (nutzt meta.tex) — NIE ändern
│   └── chapters.tex             # bindet alle Hauptkapitel-Master per \input{} ein
├── chapters/                    # Kapitel gemäß kapitelplan.md
│   └── 01_einleitung/
│       ├── einleitung.tex        # Kapitel-Master (\section), bindet Subsections per \input{}
│       └── 01_<slug>.tex         # Subsection-Dateien
├── images/<kapitel>/            # Abbildungen, gespiegelt zur Kapitelstruktur (Konvention: hard-rules-formal.md → LaTeX)
├── logos/ · tables/             # Logos bzw. Tabellen-Fragmente
├── sources/                     # IU-Leitfäden pro Papiertyp (Zweifelsfall) + Anmerkungen vom Prüfer.md (Pflichtquelle, siehe plan-modus Schritt 0)
│   └── literature/              # EIGENE Quellen (Ebooks, Paper) — jederzeit befüllbar, auch vor dem Setup; Anleitung in literature/README.md. Wird in plan-modus Schritt 1 VOR der Consensus-Suche gesichtet. Nicht versioniert (.gitignore)
└── .claude/skills/
    ├── _shared/                 # hard-rules-formal.md, typen/<typ>.md, aenderungen-format.md, scripts/
    ├── setup-check/             # einmaliger Umgebungscheck
    ├── plan-modus/              # Betriebsarten kompakt/ausführlich, Schritt 0–4
    ├── schreib-modus/           # Kapitel schreiben
    ├── pruef-modus/             # Audit vor Abgabe (inkl. Build- und Abgabe-Check)
    ├── gegenlesung/             # kalte Prüfer-Gegenlesung gegen aufgabe.md (alle Kapitel FERTIG)
    └── stresstest/              # Gegenargumente prüfen, jederzeit einzeln aufrufbar
```

## Workflow-Fahrplan

| Phase | Skill | Wann | Output |
|---|---|---|---|
| Setup | `setup-check` | Einmalig bei neuem Projektordner | Bestätigung: Umgebung bereit |
| Planen | `plan-modus` | Aufgabenstellung liegt vor, kein Kapitelplan | `aufgabe.md` + `kapitelplan.md` |
| Plan-Audit | `pruef-modus` (Umfang „Plan-Audit") | **Empfohlen**, sobald `kapitelplan.md` final ist — **vor** `schreib-modus`; Pflicht ab > 3 Kapiteln oder eigener Vergleichsmatrix | kurze Fundliste, kein Score |
| Bereitschafts-Check | `pruef-modus` (Umfang „Bereitschafts-Check") | **Empfohlen**, direkt vor dem allerersten `schreib-modus`-Aufruf, nach dem Plan-Audit | PASS/FAIL-Checkliste im Chat, kein Score |
| Schreiben | `schreib-modus` | `kapitelplan.md` existiert | `chapters/**/*.tex` |
| Gegenlesen | `gegenlesung` | Sobald alle Kapitel FERTIG — **vor** Gesamt-Stresstest und Voll-Audit | neue Runde in `AENDERUNGEN.md` |
| Stresstest | `stresstest` | Jederzeit einzelnes Argument · Gesamt-Stresstest über die ganze Arbeit, **sobald alle Kapitel FERTIG sind — nach der Gegenlesung, vor dem Voll-Audit** (Stresstest prüft Inhalt, Prüf-Modus prüft Regeln; inhaltliche Befunde ändern den Text und würden ein vorher gefahrenes Audit entwerten) | Gegenargumente + Stärke · Gesamt: neue Runde in `AENDERUNGEN.md` |
| Prüfen | `pruef-modus` | Kapitel-Audit nach Kapitel 1 · Voll-Audit vor Abgabe, **erst nach abgearbeiteter Gegenlesung und abgearbeitetem Gesamt-Stresstest** (Umfänge: siehe Skill) | `pruefbericht.md` mit Score |

**Kompakt-Prüfkette (nur Hausarbeit & Projektbericht):** Bei den beiden kleinsten Formaten ist der Gesamt-Stresstest **optional** — Default-Kette dort: Gegenlesung → Abarbeiten → Voll-Audit. Grund: Bei 7–10 Seiten prüft die Gegenlesung dieselben wenigen Kernargumente ohnehin mit; ein voller Extra-Durchgang kostet mehr Session, als er findet. Auf Wunsch oder bei erkennbar wackliger Argumentation bleibt die volle Kette jederzeit möglich; ein bewusst übersprungener Gesamt-Stresstest wird im Prüfbericht vermerkt. **Fallstudie und Seminararbeit fahren immer die volle Kette** (eigene Analysen bzw. Empirie sind die typischen Overclaim-Quellen).

**Mehrsession-Fähigkeit Plan-Modus**: Zwischenstand liegt fortlaufend in `kapitelplan.draft.md` (Checkpoint nach jedem Schritt). Bei Sessionstart immer zuerst prüfen, ob `kapitelplan.draft.md` existiert, statt bei Schritt 0 neu zu beginnen. Schreib-Modus liest `kapitelplan.md` per Read-Tool, nie aus dem Gesprächsverlauf.

## Format `AENDERUNGEN.md`

Verbindliches Runden-Format in `.claude/skills/_shared/aenderungen-format.md` — laden nur die Skills, die die Datei schreiben oder abarbeiten (`gegenlesung`, `stresstest` → Gesamt, `schreib-modus` → Abarbeiten). Kurzfassung: Befunde in Runden unter „## Offen" (je Punkt Befund · Warum · Anweisung), `[FREIGABE]` bei These-/Kernargument-Bezug nur nach aktiver Rückfrage umsetzen, abgearbeitete Runden ins Erledigt-Log; „Offen" ist leer, bevor ein Voll-Audit läuft.

## Papiertyp- und Formalia-Regeln

- **Papiertyp-spezifisch** (Pflichtregeln, Bewertungsgewichte, Kapitelgerüst, Kernfragen, Voice, Audit-Checks): eine Datei pro Typ in `.claude/skills/_shared/typen/<typ>.md` — geladen, sobald der Papiertyp feststeht, bewusst nicht hier. Quellen-Zahlen dort sind Richtwerte aus der Praxis, keine IU-Vorgabe.
- **Formale Hard Rules** (Zitationen, LaTeX, Pronomen, Struktur, Schreibstil): `.claude/skills/_shared/hard-rules-formal.md` — braucht nur `schreib-modus`/`pruef-modus`. Die sicherheitskritische Ausnahme (`main.tex`/`cover.tex`/`references.bib` nie ändern) steht oben in den Grundprinzipien.

## „Wo stehen wir?" (Status-Anfrage — definierter Ablauf)

Reine Lese-Operation, keine Arbeitssession:
1. Statustabelle unten + „Aktuelle Richtung" + „Fristen" lesen (sind ohnehin geladen).
2. `python .claude/skills/_shared/scripts/check_status.py` laufen lassen — meldet Widersprüche Tabelle ↔ Dateisystem deterministisch.
3. Antwort in höchstens 8 Zeilen: Stand heute (1 Satz) · zuletzt abgeschlossener Schritt · **nächster Schritt** als konkreter Session-Einstieg · offene Blocker/Fristen · check_status-Funde, falls vorhanden.
4. Keine Kapitel, keinen Plan, kein MEMORY pauschal laden. Bei Widerspruch Tabelle ↔ Dateisystem gilt das Dateisystem — Status korrigieren und quittieren ist die einzige zulässige Änderung in dieser Anfrage.

## Aktueller Projektstatus

**Zwei Arten von Information, zwei Regeln:**
- **Zeilenbestand** (welche Komponenten existieren) wird aus `kapitelplan.draft.md` (bzw. `kapitelplan.md`, sobald final) abgeleitet — nie geschätzt.
- **Statuswerte** (FERTIG / IN ARBEIT / ÜBERARBEITUNG NÖTIG / NICHT BEGONNEN) pflegt ausschließlich der jeweilige Skill nach Speichern/Audit — Datei-Existenz ≠ fertig. Fehlt die Datei einer FERTIG-Komponente, gilt das Dateisystem: Status korrigieren und Widerspruch melden.

| Komponente (Identifikator) | Pfad | Status | Notizen |
|---|---|---|---|
| Aufgabenstellung | `aufgabe.md` | FERTIG | Aufgabenstellung 2 (Hobbyköch:innen), Nische Zero-Waste |
| Kapitelplan | `kapitelplan.md` | FERTIG | Plattform „Resteria" (Name 2026-07-21 gesetzt, Kollision „Restlos Glücklich" behoben) — 3 Kapitel, 11 Subsections geplant |
| `sec:einleitung` | `chapters/01_einleitung/einleitung.tex` | FERTIG | 3 Subsections geschrieben, `check_formalia.py` 0 FEHLER |
| `sec:durchfuehrung` | `chapters/02_durchfuehrung/…` | FERTIG | 6 Subsections, `check_formalia.py` 0 FEHLER, alle 6 BBT-Keys genutzt; AENDERUNGEN.md Runde 2 (GS-1…GS-6, 2026-07-21) und Runde 3 (3.1–3.8, 2026-07-23) vollständig eingearbeitet; 4 Tabellen (Wettbewerbsvergleich 6 Plattformen × 5 Kriterien inkl. neuer Spalte „Rezept-Entdeckung", Funktionsübersicht, Persona, Phasenplanung) + 5 Abbildungen (Funktionslogik, 4× echtes UI/UX-Mockup-Foto in Anhang B); Zeitpuffer-Formulierung in `05_phasenplanung.tex:23` an Tabelle angeglichen (2026-07-23, Prüfbericht-Handlungsempfehlung 4) |
| `sec:fazit` | `chapters/03_fazit/…` | FERTIG | 2 Subsections (`01_kernergebnisse_und_ausblick`, `02_limitationen`), `check_formalia.py` 0 FEHLER, 4 BBT-Keys (Vittuari, Barker, Soma, Nivedhitha) validiert, Limitationen dreischichtig; „vier" → „drei Plattform-Kategorien" korrigiert (2026-07-23, Prüfbericht-Handlungsempfehlung 3) |
| Prüf-Audit | `pruefbericht.md` | ÜBERARBEITUNG NÖTIG | Letzter Score (100/100, Delta-Re-Audit 2026-07-23) bezieht sich auf den Textstand **vor** Runde 3; seit Runde-3-Abarbeitung (Wettbewerbsmatrix, Chefkoch-/leftovercooking-Wertung geändert) veraltet. Nächster Schritt: neues Voll-Audit |

**Update-Regel:** Eine Komponente = eine Zeile, bestehende Zeile überschreiben, nie anhängen. Identifikator = `sec:<slug>` (in Plan-Modus Schritt 2.5 festgelegt) — hält Tabelle, Dateinamen und LaTeX-Labels synchron. Platzhalter-Zeilen spätestens bei Schritt 2.5 durch echte Einträge ersetzen; aus dem Plan entfernte Komponenten löschen.

**Aktuelle Richtung**: `AENDERUNGEN.md` Runde 2 (GS-1…GS-6) vollständig abgearbeitet (2026-07-21). GS-1 nach aktiver Rückfrage (`AskUserQuestion`) mit Nutzer-Entscheidung „volle Aufnahme": leftovercooking per Web-Recherche (Verbraucherzentrale-Test 2024 + leftovercooking.app) als 6. Plattform in Wettbewerbsanalyse aufgenommen, USP dadurch geschärft statt widerlegt. GS-2 bis GS-6 wie in `AENDERUNGEN.md` angewiesen umgesetzt. `check_formalia.py` (0 FEHLER) und `check_bib_keys.py` (alle Keys valide) auf allen betroffenen Kapiteln bestätigt. **Runde-1-Befund 1 ist jetzt erledigt (2026-07-23):** Nutzer hat vier echte Mockup-Screenshots (Startseite, Startseite mit ausgeklappten „Gespeicherte Rezepte", Profil, Rettungs-Feed) unter `images/durchfuehrung/` geliefert. Alle drei Tikzpicture-Platzhalter in `pages/appendix.tex` durch `\includegraphics` ersetzt, ein viertes Mockup (Bookmarks-Screen) neu ergänzt, da dessen Feature „Gespeicherte Rezepte" im Screenshot sichtbar war, aber noch nicht im Fließtext stand — nach Rückfrage (`AskUserQuestion`) in `chapters/02_durchfuehrung/03_konzept.tex` per Satz ergänzt und auf die neue Abbildung verwiesen. Alle vier Quellenzeilen folgen dem Pflichtmuster „Erstellt mit dem Prompt [...] durch Claude Design (Claude Sonnet 5)" mit vom Nutzer bestätigten, aus `sources/claude-design-brief.md` abgeleiteten Prompt-Texten; da der Nutzer die KI-Outputs zusätzlich manuell nachbearbeitet hat (im Zitierleitfaden nicht explizit geregelter Fall), wurde nach Prüfung des Original-PDFs (`sources/Zitierleitfaden.pdf`, Kap. 2.2.5) je Quellenzeile der Zusatz „, Abbildung nachträglich manuell bearbeitet." ergänzt. `check_formalia.py` läuft auf `03_konzept.tex` und `appendix.tex` mit 0 FEHLER (nach Umstellung der geraden Anführungszeichen auf `\enquote{}`).

**Prüfbericht abgearbeitet (2026-07-23).** Nutzer hat für diese Session einmalig explizite Freigabe erteilt, `main.tex` zu ändern (Abweichung vom Grundprinzip „main.tex nie ändern"). Umgesetzt: (1) **Handlungsempfehlung 1** — `\appendix`/`\include{pages/appendix}` in `main.tex` einkommentiert; die vier UI/UX-Mockups + Persona-Tabelle werden jetzt kompiliert, die fünf Anhang-`\autoref`s sind aufgelöst. (2) **Handlungsempfehlung 2** — `\listoffigures`/`\listoftables` in `main.tex` einkommentiert. (3) **Handlungsempfehlung 3** — „vier" → „drei Plattform-Kategorien" in `chapters/03_fazit/02_limitationen.tex`. (4) **Handlungsempfehlung 4** — Zeitpuffer-Formulierung in `chapters/02_durchfuehrung/05_phasenplanung.tex:23` an die Tabelle angeglichen („innerhalb der MVP-Phase" statt „zwischen MVP-Entwicklung und Beta-Test"). Handlungsempfehlung 5 (UI/UX `\ac{}`-Vereinheitlichung) bewusst ausgelassen — als rein optional markiert, keine Regelverletzung. `check_formalia.py` auf beiden geänderten Kapiteldateien: 0 FEHLER. Teil-Check D (Build) bleibt vom Nutzer lokal zu verifizieren — `lualatex`/`latexmk` in dieser Umgebung nicht verfügbar.

**Delta-Re-Audit (2026-07-23, Score 100/100) ist durch Runde-3-Gegenlesung überholt** — der damalige Score bezog sich auf den Textstand vor den unten beschriebenen Änderungen an `01_wettbewerbsanalyse.tex`, `02_limitationen.tex` und `03_konzept.tex`; `pruefbericht.md` selbst wurde nicht überschrieben und ist als Momentaufnahme des alten Stands zu lesen, nicht als aktuell gültiger Score.

**AENDERUNGEN.md Runde 3 (Gegenlesung 2026-07-23) vollständig abgearbeitet.** Acht Befunde (3.1–3.8): 3.1 (Zähl-/Aufzählungsdrift „drei"→„vier" Einwände, „ein bis zwei"→„ein bis drei" Vertreter) und 3.6 (unbelegte Marktbehauptung abgeschwächt) mechanisch ohne Freigabe umgesetzt. Die vier `[FREIGABE]`-Punkte per `AskUserQuestion` einzeln geklärt: 3.2 Chefkoch Community-Funktionen nach Web-Faktencheck auf „stark" gehoben; 3.3 leftovercooking-Belohnungspunkte als individuelles Spar-Feedback vom Gamification-Kriterium abgegrenzt, Zelle „mittel" bleibt; 3.4 unbelegter Verbraucherzentrale-Verweis gestrichen, leftovercooking-Bewertung läuft rein als eigene Sichtung; 3.5 neue Matrixspalte „Rezept-Entdeckung" in `tab:wettbewerbsvergleich` ergänzt (jetzt 5 Kriterien statt 4). 3.7 (optionale Einstiegsliteratur) übersprungen wie in Runde 1 — Quellen fehlen weiter in `references.bib`. 3.8 ist ein reiner Build-Grenzvermerk ohne Textauftrag. `check_formalia.py` (0 FEHLER) und `check_bib_keys.py` (6/6 Keys valide) auf allen betroffenen Dateien bestätigt.

**Nächster Schritt: Voll-Audit** (`pruef-modus`) — ersetzt den überholten Delta-Re-Audit-Stand, prüft insbesondere die neue Matrixspalte, die veränderten Chefkoch-/leftovercooking-Wertungen und Teil-Check D (Build/Anhang-Einbindung). Teil-Check D war zuletzt ÜBERSPRUNGEN, da `lualatex`/`biber` in dieser Umgebung nicht verfügbar sind — Nutzer kompiliert weiterhin lokal (`latexmk -lualatex main.tex`).

**Offene Fragen**: Keine blockierenden Punkte. Nutzer-Restpflichten (nicht-blockierend): Namensverfügbarkeit „Resteria" (DPMA / .de-Domain) · Nivedhitha/Shen nur per Abstract → beim Schreiben vorsichtig formulieren, bis Volltext vorliegt.

**Fristen**: Abgabe: kein festes Datum (`\today` auf Nutzerwunsch, siehe `PERSISTENT.md`) · Eidesstattliche Erklärung (myCampus): [offen]

> Aktualisiert nach jedem Checkpoint bzw. jeder gespeicherten Datei, sichtbar quittiert. Für Planungsinhalte gilt bei Widerspruch der Plan/Draft, für Statuswerte diese Tabelle.

## BBT-Konfiguration (Zotero)

Siehe `.claude/skills/setup-check/references/bbt-setup.md` (Setup-Wissen, einmalig pro Projekt — nicht in jeder Session benötigt).
