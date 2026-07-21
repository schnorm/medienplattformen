# Handbuch „schriftlich"

Nutzer-Handbuch für wissenschaftliche Arbeiten an der IU mit Claude — Hausarbeit, Fallstudie, Seminararbeit, Projektbericht. Diese Datei ist die **einzige Quelle** für die Bedienungsanleitung; `workflow-anleitung.pdf` ist ein optionales, bei Bedarf daraus erzeugtes Derivat und kann veralten — bei Widerspruch gilt diese Datei.

**Quellen**: `CLAUDE.md`, Skill-Dateien (`.claude/skills/`), `_shared/typen/`, `_shared/modell-empfehlung.md`.

## Wozu dieses Handbuch

Der Projektordner **schriftlich** ist eine LaTeX-Vorlage plus ein geführter Claude-Workflow für kleine wissenschaftliche Arbeiten (7–10 Seiten). Der Workflow besteht aus fünf Skills in fester Reihenfolge: **setup-check → plan-modus → schreib-modus → pruef-modus**, dazu **stresstest** als jederzeit einsetzbares Werkzeug. Dieses Handbuch beschreibt die Bedienung von Projektstart bis Abgabe — inklusive der Schnellspur „Plan kompakt", mit der der Kapitelplan in einer einzigen Session steht.

## Schnellreferenz: So startet jede Session

| Du willst … | Schreibe in neuer Session |
|---|---|
| Umgebung prüfen (einmalig zu Beginn) | „Setup-Check" |
| Kapitelplan erstellen (Standard, 1 Session) | „Plan kompakt" |
| Kapitelplan ausführlich (empirische Seminararbeit) | „Plan ausführlich" |
| Nächstes Kapitel schreiben | „Schreib-Modus: nächstes Kapitel" |
| Ein Argument prüfen lassen | „Stresstest auf: <Argument>" |
| Erstes Kapitel gegenprüfen (früh, ohne Score) | „Audit Kapitel: <name>" |
| Arbeit oder Kapitelplan prüfen | „Audit" |
| Status erfahren | „Wo stehen wir?" |

Diese Tabelle steht auch in `CLAUDE.md` ganz oben — ihr müsst nie überlegen, wie eine Session startet.

## Grundprinzipien (gelten immer)

- **Dateien sind Wahrheit, nicht der Chat-Verlauf.** `aufgabe.md`, `kapitelplan.md`, `kapitelplan.draft.md` und `chapters/**/*.tex` gelten vor jeder Erinnerung — bei Zweifel lesen lassen, nicht annehmen.
- **Nie ändern**: `main.tex`, `pages/cover.tex`, `references.bib` (Letzteres nur über den Zotero/Better-BibTeX-Auto-Export). Projektangaben stehen ausschließlich in `pages/meta.tex` (einmalig beim Projektstart ausfüllen).
- **These und Kernargumente kommen von euch.** Claude hinterfragt und schärft, liefert aber nicht die inhaltliche Position. Das ist zugleich die Bedingung der IU-KI-Richtlinie: Die Verantwortung liegt beim Studierenden — jede gelieferte Quelle, Zahl oder Behauptung am Original verifizieren, bevor sie in die Arbeit übernommen wird.
- **Keine personenbezogenen Daten in Sessions** (IU-KI-Richtlinie): Interview-Transkripte vor der Verarbeitung anonymisieren (Namen → B1, B2 …), keine vertraulichen Unternehmensdaten ohne Freigabe.
- **Checkpoints werden im Chat sichtbar quittiert** („✅ Checkpoint gespeichert …"). Fehlt die Quittung, nachfragen.
- **Zwei Memory-Dateien**: Projektspezifische Korrekturen → `MEMORY.md`; projektunabhängige Dauer-Präferenzen (Stil, Zitation, Prozess) → `PERSISTENT.md` — die einzige Datei, die ihr von Projekt zu Projekt kopiert. Bei Widerspruch gewinnt `MEMORY.md`. Überholte Einträge werden als `[ÜBERHOLT]` markiert, nicht gelöscht.
- **Nur „Pflicht"-Regeln aus `typen/<typ>.md` zählen im Audit als FAIL.** „Optional"/„empfohlen" sind Hinweise; „entfällt" wird für den Papiertyp gar nicht geprüft. Pro Papiertyp existiert genau eine Typ-Datei (`_shared/typen/`) mit Pflichtregeln, Bewertungsgewichten, Kapitelgerüst, Voice und Audit-Checks.
- **Verständlichkeit ist Teil der Formalia-Prüfung.** Maßstab: Ein Laie versteht jeden Absatz beim ersten Lesen — kein gehäufter Nominalstil, keine gestelzten Meta-Verben, Fachbegriffe bei erster Nennung erklärt. Details in `_shared/hard-rules-formal.md` → Verständlichkeit; Kalibrier-Referenz mit Positiv-/Negativ-Beispielen in `_shared/stilprofil.md`.

## Session-Regeln (Memory-Management)

Kern des Workflows: **viele kurze Sessions statt einer großen.** Lange Sessions verbrennen Tokens und werden gegen Ende unzuverlässig.

- **Start-Ritual (<1 Min.)**: Statustabelle + „Aktuelle Richtung" in `CLAUDE.md` lesen → `PERSISTENT.md`/`MEMORY.md` beachten → nur die Dateien laden, die das heutige Arbeitspaket braucht.
- **Arbeitspaket-Größen**: Plan kompakt = 1 Session · Plan ausführlich = 1–2 (Schnitt idealerweise nach Schritt 1) · Schreiben = 1 Hauptteil-Kapitel pro Session (Ausnahme: Einleitung + Schluss gemeinsam — je ~10 %, inhaltlich zusammenhängend) · Audit = 1 Session.
- **Ende-Ritual**: Checkpoint → Statustabelle → „Aktuelle Richtung" auf nächsten Schritt → Quittung im Chat.
- **Kontext fast voll oder Session driftet?** Nicht „noch schnell fertig machen" — Checkpoint schreiben, Session beenden, frisch weitermachen.

## Der Workflow im Überblick

| Phase | Skill | Wann | Ergebnis |
|---|---|---|---|
| Setup | `setup-check` | Einmalig bei neuem Projektordner | Umgebung bereit; Frist erfasst |
| Planen | `plan-modus` | Aufgabenstellung liegt vor, noch kein Kapitelplan | `aufgabe.md` + `kapitelplan.md` |
| Schreiben | `schreib-modus` | `kapitelplan.md` existiert | `chapters/**/*.tex`, Kapitel für Kapitel |
| Prüfen | `pruef-modus` | Vor der Abgabe (und nach Überarbeitungen) | `pruefbericht.md` mit Score 0–100 |
| Stresstest | `stresstest` | Jederzeit, für ein einzelnes Argument | Gegenargumente + Stärke |

**Typischer Gesamtablauf**: Setup (10 min) → 1 Kompakt-Plan-Session → 2–4 Schreib-Sessions → Prüf-Audit → gezielte Überarbeitung → erneutes Audit → Abgabe. Jeder Zwischenstand liegt in Dateien, nie nur im Chat.

## Phase 0: Setup (setup-check)

Einmalig beim ersten Öffnen ausführen. Geprüft werden: lualatex + biber, `references.bib`, Python-Skripte, Shared-Referenzen (inkl. `typen/`), `pages/meta.tex`, Aufgabenstellung + Abgabefrist (Frist wird in `CLAUDE.md` → Fristen eingetragen), `PERSISTENT.md` (noch Seed? → Datei aus dem Vorgängerprojekt hierher kopieren), Consensus-MCP, Ordnerstruktur.

- Zotero mit Better-BibTeX-Auto-Export auf `references.bib` einrichten (Anleitung: `setup-check/references/bbt-setup.md`). Nie manuell in die `.bib`-Datei schreiben.
- Gibt es eine frühere Arbeit? Deren `PERSISTENT.md` jetzt hierher kopieren — sonst gehen die arbeitenübergreifenden Lernpunkte verloren.
- Bei „NOCH EINRICHTUNG NÖTIG": erst die genannten Punkte beheben, dann weiter.

## Phase 1: Planen (plan-modus) — zwei Betriebsarten

**Kompakt** (Default für Hausarbeit, Fallstudie, Projektbericht, Literatur-Seminararbeit): Readiness + These + Kapitelgerüst in einer Dialogrunde, eine Runde pro Hauptteil-Kapitel, Einleitung/Schluss ohne eigene Runde, Stresstest optional. Ziel: `kapitelplan.md` in einer Session.
**Ausführlich** (Default nur für die empirische Seminararbeit, sonst opt-in „Plan ausführlich"): jeder Schritt einzeln, sokratische Herleitung, Pflicht-Stresstest.

Checkpoints nach jedem Schritt in `kapitelplan.draft.md` — beide Betriebsarten sind jederzeit unterbrechbar.

| Schritt | Inhalt | Euer Beitrag |
|---|---|---|
| 0 — Readiness | Aufgabenstellung nach `aufgabe.md` destillieren (wörtliche Leitfragen, Vorgaben, Frist, Bewertungsbezüge). Papiertyp + Betriebsart festlegen. | Aufgabenstellung bereitstellen, Papiertyp nennen |
| 1 — Literatur | Nur falls Literatur fehlt: Consensus-Recherche, Priority Reading Order + Forschungslücken | Framework mitwählen; Papers in Zotero importieren |
| 2 — These | Leitfrage ≠ These. „Diese Arbeit argumentiert ___, weil ___, basierend auf ___" | These selbst formulieren; stärkstes Gegenargument mitdenken |
| 2.5 — Kapitelgerüst | Skelett mit Wortanteilen, an Bewertungsgewichten ausgerichtet; Slugs festlegen | Skelett bestätigen oder anpassen — hier, nicht später! |
| 3 — Kapitel für Kapitel | Pro Hauptteil-Kapitel: Kernfragen → Kernargument, Belege, Risiko, Subsections | Jedes Kapitel einzeln bestätigen |
| 4 — Stresstest | Kompakt: optional. Ausführlich: Pflicht — alle Kernargumente gegen Gegenargumente | Auf starke Gegenargumente inhaltlich reagieren |

- Session-Wiedereinstieg: Existiert `kapitelplan.draft.md`, bietet Claude „Weitermachen bei Schritt X?" an. Nie stillschweigend von vorn beginnen lassen.
- **Session-Schnitt nach Schritt 1**: Die Literaturrecherche ist der größte Kontextposten der Planung. Danach Session beenden — alles Weiterverwendbare liegt destilliert im Draft, und für Schritt 2–4 wechselt ohnehin das Modell (siehe `_shared/modell-empfehlung.md`).
- Nur echte Consensus-Treffer zitieren lassen — wenige Ergebnisse werden ehrlich gemeldet, nicht mit Modellwissen aufgefüllt.

## Phase 2: Schreiben (schreib-modus)

Verfasst Kapitel als LaTeX-Dateien auf Basis von `kapitelplan.md` (+ `aufgabe.md` für die wörtlichen Leitfragen). Master-Datei pro Hauptkapitel, Subsections als eigene Dateien per `\input{}`.

- Vor jedem `\parencite{}`: Keys per `check_bib_keys.py` validieren — Keys werden niemals erfunden.
- Nach dem Speichern: `check_formalia.py` — deckt Blockzitat > 40 Wörter, ½-Seiten-Heuristik, Überschriften-Dopplung, Satzlängen und Verständlichkeits-Marker deterministisch ab.
- Self-Check gegen die Pflicht-Punkte aus `typen/<typ>.md` (Absatzlogik, Synthese, Gegenargumente, Limitationen dreischichtig, Anti-KI-Stil, Verständlichkeit gegen `stilprofil.md`).
- Strukturabweichungen sofort nachziehen lassen (`kapitelplan.md` per Edit), sonst ist die „Dateien sind Wahrheit"-Quelle still falsch.
- Überarbeitungen nach Audit entlang `pruefbericht.md` abarbeiten, nicht aus dem Gedächtnis.

## Phase 3: Prüfen (pruef-modus)

**Iterationsrhythmus**: Skripte + Self-Check im Schreib-Modus sind das Qualitätstor pro Kapitel — kein Voll-Audit nach jedem Kapitel. Empfohlener Ablauf: nach dem ersten Hauptteil-Kapitel ein Kapitel-Audit („Audit Kapitel: <name>", ohne Score) → restliche Kapitel schreiben → Voll-Audit, wenn alles FERTIG ist → Überarbeitung in eigenen Sessions → Re-Audit als Delta (nur FAIL-Punkte + Skripte + Build) → Abgabe-Audit.

Einziger Einstiegspunkt für Audits. Fünf Teil-Checks: **A** Formalia (Skripte + manuelle Punkte) · **B** Argumentationsqualität (nur Pflicht-Punkte der Typ-Datei als FAIL; inkl. Abgleich mit den Leitfragen aus `aufgabe.md`) · **C** Struktur · **D** Build (`latexmk`, Seitenumfang) · **E** Abgabe. Ergebnis: Score 0–100 als `pruefbericht.md`.

**Teil-Check E — Abgabe**: Abgabe läuft ausschließlich über Turnitin im myCampus-Kurs, und die Eidesstattliche Erklärung muss vorab elektronisch über myCampus abgegeben werden — vorher nimmt Turnitin nichts an. Der Status steht in `CLAUDE.md` → Fristen. Teil-Check E fließt **in keinem Audit-Umfang in den Score ein**, auch nicht im Abgabe-Audit — die Verwaltungsschritte liegen außerhalb des Textes. Offene Punkte erscheinen stattdessen als „Vor der Einreichung"-Checkliste am Ende jedes Berichts.

| Score | Bedeutung | Nächster Schritt |
|---|---|---|
| ≥ 80 | Abgabereif | Verbleibende Punkte optional nachbessern; `PERSISTENT.md` fürs nächste Projekt aktualisieren |
| 60–79 | Überarbeitung empfohlen | Mit `schreib-modus` gezielt an den Kritikpunkten arbeiten |
| < 60 | Nicht einreichen | Mindestens einen weiteren Prüf-Schreib-Zyklus einplanen |

- **Audit und Überarbeitung trennen**: Nach dem Audit neue Session starten — `pruefbericht.md` trägt die priorisierte Arbeitsliste hinüber, und die Überarbeitung läuft mit dem günstigeren Modell (siehe `_shared/modell-empfehlung.md`).
- Das Audit frühzeitig einsetzen — auch auf den Kapitelplan oder einzelne Kapitel, nicht erst am Abgabetag.
- Der Score ist ein Priorisierungs-Hilfswert, keine Zusicherung — die Entscheidung „einreichen oder nicht" bleibt bei euch.
- **Bekannte False-Positive-Quelle der Skripte**: `check_formalia.py` meldet PRONOMEN auch in wörtlichen Zitaten (`\enquote{…ich…}`, `blockzitat`) und FLOAT bei `[H]` in der Folgezeile — solche Funde im Kontext gegenprüfen statt blind zu übernehmen.

## Modell- und Thinking-Empfehlung je Phase

Siehe `_shared/modell-empfehlung.md` für die vollständige Tabelle. Faustregel: teures Modell und hohes Thinking dort, wo wenige Tokens über die Qualität der ganzen Arbeit entscheiden (These, Stresstest, finales Audit); Sonnet überall sonst.

## Welche Datei ist wofür (Schnellreferenz)

| Datei | Rolle | Wer schreibt |
|---|---|---|
| `CLAUDE.md` | Schnellreferenz, Regeln, Session-Regeln, Statustabelle, Fristen | Skills (Status), sonst fix |
| `aufgabe.md` | Destillierte Aufgabenstellung — Single Source statt Aufgaben-PDF | `plan-modus` (Schritt 0) |
| `kapitelplan.draft.md` | Checkpoint-Datei des Plan-Modus; danach INSIGHT-Archiv | `plan-modus` |
| `kapitelplan.md` | Finaler Kapitelplan — Single Source für Struktur und Argumente | `plan-modus` (Output) |
| `chapters/**/*.tex` | Der finale Text (Master- + Subsection-Dateien) | `schreib-modus` |
| `pruefbericht.md` | Letzter Audit-Bericht; Arbeitsliste für Überarbeitungen | `pruef-modus` |
| `MEMORY.md` | Projektspezifische Korrekturen (`[LERNEN:kategorie]`) | Skills bei euren Korrekturen |
| `PERSISTENT.md` | Projektübergreifende Dauer-Präferenzen — wandert per Kopie ins nächste Projekt | Skills; ihr kopiert sie weiter |
| `_shared/typen/<typ>.md` | Alle papiertyp-spezifischen Regeln (Pflicht, Bewertung, Gerüst, Voice, Audit) | Fix (Vorlage) |
| `_shared/stilprofil.md` | Positiv-/Negativ-Stilbeispiele als Verständlichkeits-Kalibrierung | Fix (Vorlage) |
| `references.bib` | Zitationen — nur über Zotero/BBT-Auto-Export | Zotero (nie manuell) |
| `pages/meta.tex` | Einzige Stelle für Projektangaben | Ihr, einmalig beim Start |
| `main.tex` / `pages/cover.tex` | Wurzeldokument und Titelblatt | Niemand — nie ändern |

**Häufige Bedienfehler**: `main.tex` oder `cover.tex` anfassen lassen · `references.bib` von Hand editieren · Schreib-Session ohne `kapitelplan.md` starten · Plan-Session neu beginnen, obwohl ein Draft existiert · Checkpoints ohne Chat-Quittung durchgehen lassen · Strukturänderungen nur im Chat besprechen · Audit erst am Abgabetag · `PERSISTENT.md` beim Projektwechsel vergessen · Eidesstattliche Erklärung erst am Abgabetag abgeben wollen.
