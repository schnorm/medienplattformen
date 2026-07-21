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
| Arbeit/Kapitelplan prüfen | „Audit" |
| Status erfahren | „Wo stehen wir?" |

## Grundprinzipien

- **Kompilieren ist Sache des Nutzers, nicht meine.** Nach Edits an `.tex`-Dateien nicht ad-hoc selbst `lualatex`/`latexmk` laufen lassen, um die eigene Änderung zu verifizieren — der Nutzer kompiliert lokal. Ausnahme: Teil-Check D (Build) im `pruef-modus` bleibt bestehen, da er ein bewusster, score-relevanter Audit-Bestandteil ist und kein Ad-hoc-Selbstcheck.
- **Dateien sind Wahrheit, nicht der Chat-Verlauf.** `aufgabe.md`, `kapitelplan.md`, `kapitelplan.draft.md` und `chapters/**/*.tex` gelten immer vor Erinnerung/Memory — bei Zweifel lesen, nicht annehmen.
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
├── handbuch.md                  # Nutzer-Handbuch (einzige Quelle; workflow-anleitung.pdf ist optionales Derivat)
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
├── sources/                     # IU-Leitfäden pro Papiertyp — nur bei konkretem Zweifelsfall lesen
└── .claude/skills/
    ├── _shared/                 # hard-rules-formal.md, typen/<typ>.md, scripts/
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
| Schreiben | `schreib-modus` | `kapitelplan.md` existiert | `chapters/**/*.tex` |
| Gegenlesen | `gegenlesung` | Sobald alle Kapitel FERTIG — **vor** Gesamt-Stresstest und Voll-Audit | neue Runde in `AENDERUNGEN.md` |
| Stresstest | `stresstest` | Jederzeit einzelnes Argument · Gesamt-Stresstest über die ganze Arbeit, **sobald alle Kapitel FERTIG sind — nach der Gegenlesung, vor dem Voll-Audit** (Stresstest prüft Inhalt, Prüf-Modus prüft Regeln; inhaltliche Befunde ändern den Text und würden ein vorher gefahrenes Audit entwerten) | Gegenargumente + Stärke · Gesamt: neue Runde in `AENDERUNGEN.md` |
| Prüfen | `pruef-modus` | Kapitel-Audit nach Kapitel 1 · Voll-Audit vor Abgabe, **erst nach abgearbeiteter Gegenlesung und abgearbeitetem Gesamt-Stresstest** (Umfänge: siehe Skill) | `pruefbericht.md` mit Score |

**Mehrsession-Fähigkeit Plan-Modus**: Zwischenstand liegt fortlaufend in `kapitelplan.draft.md` (Checkpoint nach jedem Schritt). Bei Sessionstart immer zuerst prüfen, ob `kapitelplan.draft.md` existiert, statt bei Schritt 0 neu zu beginnen. Schreib-Modus liest `kapitelplan.md` per Read-Tool, nie aus dem Gesprächsverlauf.

## Papiertyp- und Formalia-Regeln

- **Papiertyp-spezifisch** (Pflichtregeln, Bewertungsgewichte, Kapitelgerüst, Kernfragen, Voice, Audit-Checks): eine Datei pro Typ in `.claude/skills/_shared/typen/<typ>.md` — geladen, sobald der Papiertyp feststeht, bewusst nicht hier. Quellen-Zahlen dort sind Richtwerte aus der Praxis, keine IU-Vorgabe.
- **Formale Hard Rules** (Zitationen, LaTeX, Pronomen, Struktur, Schreibstil): `.claude/skills/_shared/hard-rules-formal.md` — braucht nur `schreib-modus`/`pruef-modus`. Die sicherheitskritische Ausnahme (`main.tex`/`cover.tex`/`references.bib` nie ändern) steht oben in den Grundprinzipien.

## Aktueller Projektstatus

**Zwei Arten von Information, zwei Regeln:**
- **Zeilenbestand** (welche Komponenten existieren) wird aus `kapitelplan.draft.md` (bzw. `kapitelplan.md`, sobald final) abgeleitet — nie geschätzt.
- **Statuswerte** (FERTIG / IN ARBEIT / ÜBERARBEITUNG NÖTIG / NICHT BEGONNEN) pflegt ausschließlich der jeweilige Skill nach Speichern/Audit — Datei-Existenz ≠ fertig. Fehlt die Datei einer FERTIG-Komponente, gilt das Dateisystem: Status korrigieren und Widerspruch melden.

| Komponente (Identifikator) | Pfad | Status | Notizen |
|---|---|---|---|
| Aufgabenstellung | `aufgabe.md` | NICHT BEGONNEN | |
| Kapitelplan | `kapitelplan.md` | NICHT BEGONNEN | |
| `sec:<slug-1>` (Platzhalter) | `chapters/…` | NICHT BEGONNEN | wird in Plan-Phase ersetzt |
| Prüf-Audit | `pruefbericht.md` | NICHT BEGONNEN | |

**Update-Regel:** Eine Komponente = eine Zeile, bestehende Zeile überschreiben, nie anhängen. Identifikator = `sec:<slug>` (in Plan-Modus Schritt 2.5 festgelegt) — hält Tabelle, Dateinamen und LaTeX-Labels synchron. Platzhalter-Zeilen spätestens bei Schritt 2.5 durch echte Einträge ersetzen; aus dem Plan entfernte Komponenten löschen.

**Aktuelle Richtung**: [1–2 Sätze: woran wird gerade gearbeitet, unmittelbar nächster Schritt.]

> **Format (verbindlich):** höchstens **5 Zeilen**, ausschließlich (1) Stand von heute in einem Satz, (2) letzter abgeschlossener Schritt mit Datum, (3) **nächster Schritt** als konkreter Session-Einstieg, (4) blockierende offene Punkte. **Keine Historie** — kein „Zuvor …". Die Verlaufsdarstellung steht ausschließlich im Erledigt-Log von `AENDERUNGEN.md`; bei jedem Update wird der bisherige Text **ersetzt, nicht ergänzt**.

**Offene Fragen**: [unentschiedene Punkte für die nächste Session, z. B. „Methodik-Kapitel nötig? Noch nicht final entschieden."]

**Fristen**: Abgabe: [—] · Eidesstattliche Erklärung (myCampus): [offen]

> Aktualisiert nach jedem Checkpoint bzw. jeder gespeicherten Datei, sichtbar quittiert. Für Planungsinhalte gilt bei Widerspruch der Plan/Draft, für Statuswerte diese Tabelle.

## BBT-Konfiguration (Zotero)

Siehe `.claude/skills/setup-check/references/bbt-setup.md` (Setup-Wissen, einmalig pro Projekt — nicht in jeder Session benötigt).
