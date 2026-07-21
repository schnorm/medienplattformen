---
name: schreib-modus
description: Verfasst Kapitel wissenschaftlicher Arbeiten an der IU als LaTeX-Subsection-Dateien, basierend auf einem bestehenden kapitelplan.md. Nutzen, wenn ein Kapitelplan vorliegt und Kapitel geschrieben werden sollen — auch über mehrere Sessions verteilt, da jedes fertige Kapitel als eigene Datei gesichert wird. Wendet Zitierregeln, Voice und Claim-Regeln papiertyp-spezifisch an.
compatibility: Benötigt kapitelplan.md im Projekt-Root und references.bib mit BBT-Keys. .claude/skills/_shared/scripts/check_bib_keys.py benötigt Python 3.
---

# Schreib-Modus: Kapitel verfassen

## Voraussetzungen

- `kapitelplan.md` im Projekt-Root per Read-Tool geladen — nicht aus dem Gesprächsverlauf annehmen, auch wenn die Plan-Session kürzlich lief. **`aufgabe.md`** (falls vorhanden) für wörtliche Leitfragen und formale Vorgaben heranziehen statt des Aufgaben-PDFs.
- `references.bib` **nicht vollständig einlesen** — bei großen Zotero-Exporten ist das ein erheblicher Kontextposten. Keys werden per `check_bib_keys.py` deterministisch validiert; wird der Inhalt eines einzelnen Eintrags gebraucht (Autor, Jahr, Titel), gezielt nach dem Key greppen. BBT-Keys exakt übernehmen, **niemals erfinden**.
- Papiertyp bekannt → `.claude/skills/_shared/typen/<typ>.md` für Pflichtregeln, Voice, Synthese-Fragen, Claim-Regeln laden.
- `.claude/skills/_shared/hard-rules-formal.md` laden — Zitationen, LaTeX, Pronomen, Struktur, Schreibstil, Verständlichkeit (Details, die bewusst nicht in `CLAUDE.md` stehen, um Plan-Modus-Sessions schlank zu halten). Zusätzlich `.claude/skills/_shared/stilprofil.md` laden — Positiv-/Negativ-Beispiele aus real gut bzw. schlecht bewerteten Arbeiten als Stil-Kalibrierung.
- **`PERSISTENT.md` + `MEMORY.md`** (falls vorhanden) lesen — `[LERNEN:stil]`, `[LERNEN:struktur]`, `[LERNEN:zitation]` und `[LERNEN:prozess]`-Einträge ohne `[ÜBERHOLT]`-Markierung berücksichtigen (z. B. bevorzugte Absatzlänge, abweichende Kapitelgerüste, Workflow-Präferenzen); bei Widerspruch gewinnt `MEMORY.md`. Konsolidierungs-Hinweis: ab ~20 Einträgen mit Nutzer durchgehen.
- **`pruefbericht.md`** (falls vorhanden) lesen, wenn Kapitel mit Status ÜBERARBEITUNG NÖTIG anstehen — die dortigen Handlungsempfehlungen sind die Arbeitsliste für die Überarbeitung, nicht aus dem Gedächtnis rekonstruieren.

## Session-Start: welche Kapitel fehlen noch?

Schreib-Sessions laufen typischerweise über mehrere Tage — nicht auf Memory verlassen, um zu wissen, welches Kapitel als Nächstes dran ist. **Nur einmal beim ersten Aufruf dieses Skills innerhalb einer Session ausführen, nicht bei jeder weiteren Nachricht wiederholen** — danach reicht der bereits bekannte Stand, bis eine neue Session beginnt oder der Nutzer explizit nach dem aktuellen Stand fragt.

1. `chapters/` per Verzeichnis-Listing prüfen: welche `.tex`-Dateien existieren bereits (Dateiname = `sec:<slug>` aus dem Kapitelplan)?
2. Mit den Kapiteln aus `kapitelplan.md` abgleichen: welche fehlen noch?
3. Dem Nutzer die Lücke kurz nennen („Kapitel 1–2 sind vorhanden, Kapitel 3 (Diskussion) fehlt noch — damit weitermachen?") statt anzunehmen, das letzte besprochene Kapitel sei automatisch bekannt.
4. Falls eine bestehende `.tex`-Datei überarbeitet statt neu geschrieben werden soll: das explizit erfragen, nicht automatisch überschreiben.

**Strukturänderungen während des Schreibens**: Weicht die Umsetzung vom Plan ab (Kapitel zusammengelegt/geteilt, Subsection ergänzt/gestrichen — vom Nutzer bestätigt), wird `kapitelplan.md` **sofort im betroffenen Kapitelblock per Edit nachgezogen** (plus Statustabelle in `CLAUDE.md`), sichtbar quittiert. Sonst ist die „Dateien sind Wahrheit"-Quelle beim nächsten Sessionstart still falsch. Ist die Abweichung eine Dauer-Präferenz („bei uns immer ohne X"), zusätzlich `[LERNEN:struktur]` in `MEMORY.md`.

**Freigabepflichtige Punkte beim Abarbeiten von `AENDERUNGEN.md`/`pruefbericht.md`**: Trägt ein Punkt einen Vorbehalt wie „nur mit expliziter Freigabe ändern" (z. B. weil er die Leitfrage oder ein Kernargument betrifft, siehe `CLAUDE.md` → Grundprinzipien), diesen **nicht** kommentarlos auslassen. Per `AskUserQuestion` noch in derselben Session aktiv nachfragen, bevor der nächste Schritt (Audit, Commit, PR) beginnt — nicht nur in der Session-Zusammenfassung erwähnen und die Entscheidung dem Nutzer überlassen, sie von sich aus nachzufragen.

### Ein Kapitel = eine Subsection-Datei pro Slug; Master bindet Subsections

Pro Kapitel aus `kapitelplan.md` gibt es eine Subsection-Datei `chapters/<kap>/<nn>_<slug>.tex`, die mit `\subsection{...}\label{sec:<slug>}` beginnt. Bei Kapiteln mit **mehreren eigenständigen Unterkonzepten mit jeweils eigenem Kernargument** (typisch beim Theorie-Kapitel mit 2–3 Konzepten, siehe `typen/<typ>.md`) bekommt jedes Unterkonzept eine eigene Datei `<nn>_<slug>.tex` im selben Kapitelordner. Bei Unsicherheit, ob ein Kapitel eine oder mehrere Dateien braucht: den Kapitelplan prüfen, nicht raten — im Zweifel eine Datei, nur bei klar getrennten Unterkonzepten aufteilen. Der **Master** `chapters/<kap>/<kap>.tex` öffnet die Section und bindet die Subsection-Dateien per `\input{}` ein.

**Sichtbarkeitspflicht**: Nach jeder gespeicherten `.tex`-Datei im Chat kurz quittieren, z. B. „✅ Gespeichert: chapters/theorie/konzept-a.tex" — nicht nur den Kapiteltext im Chat zeigen und stillschweigend annehmen, dass die Datei geschrieben wurde. **Zusätzlich** die entsprechende Zeile in `CLAUDE.md` → „Aktueller Projektstatus" auf FERTIG setzen (bestehende Zeile überschreiben, nicht anhängen) und kurz mitquittieren.

## Ablauf pro Kapitel

1. Kapitelplan lesen — Kernargument, Belege, Wortzahl, **Slug** (`sec:<slug>`), geplante Subsections **mit Inhaltspunkten und Argumentationsfluss** aus dem Plan. Die Inhaltspunkte sind der Schreibleitfaden pro Subsection: Jeder Punkt muss im fertigen Text erkennbar vorkommen — als eigener Absatz, als Teilaussage oder als Beispiel. Reihenfolge der Punkte darf angepasst werden, keiner darf stillschweigend wegfallen. **Bereits geschriebene Kapitel nicht „zur Konsistenz" komplett laden** — die Argumentationslinie steht im Kapitelplan; für den Übergang genügt der Schlussabsatz der letzten Subsection-Datei des Vorkapitels (Read mit offset ans Dateiende).
2. **Faktenbasis prüfen:** Weist der Kapitelblock „eigene Recherche" aus und fehlt ein Rechercheprotokoll, **vor dem Schreiben** melden und die Recherche nachholen oder vom Nutzer freigeben lassen. Jede Einzelbehauptung ohne Beleg oder Protokoll bekommt im `.tex` einen Marker `% UNVERIFIED: <was genau zu prüfen ist>`. Beruht ein Kapitel auf eigener Erhebung, gehört das Protokoll als Anhang in die Arbeit — es ist ein Lieferobjekt, kein internes Arbeitspapier.
3. **Ersatzentscheidungen:** Betrifft das Kapitel eine Teilaufgabe, für die `aufgabe.md` → „Ersatzentscheidungen" einen Eintrag führt, wird die Begründung **als eigener Absatz ausgeschrieben** — die vier Angaben (Versuch, Hinderungsgrund, geprüfter Minimalersatz, Folgeschritt). Ein Nebensatz in der Einleitung genügt nicht.
4. Subsection-Datei schreiben — beginnt mit `\subsection{...}\label{sec:<slug>}`.
5. Hard Rules aus `.claude/skills/_shared/hard-rules-formal.md` beachten (Zitationen, Eigene Darstellung, Pronomen, Akronyme, Labels, Floats).
6. Vor jedem `\parencite{}`: Key gegen `references.bib` validieren — `python3 .claude/skills/_shared/scripts/check_bib_keys.py references.bib <key1> <key2> ...` oder, für eine ganze Datei, `python3 .claude/skills/_shared/scripts/check_bib_keys.py references.bib --tex chapters/<kap>/<nn>_<slug>.tex` (vom Projekt-Root aus aufrufen).
7. Nach dem Speichern: `python3 .claude/skills/_shared/scripts/check_formalia.py chapters/<kap>/` — mechanische Verstöße (Pronomen, Anführungszeichen, Floats …) deterministisch finden und sofort fixen, statt sie dem Prüf-Modus zu überlassen.
8. Nach jedem Kapitel: Self-Check (siehe unten).

## LaTeX-Schreibregeln (Kurzreminder — Details in `.claude/skills/_shared/hard-rules-formal.md`)

- Pro Hauptkapitel gibt es eine **Master-Datei** (`chapters/<kap>/<kap>.tex`, öffnet die Section mit `\section{...}\label{sec:<kap>}`) und je Subsection eine eigene Datei (`chapters/<kap>/<nn>_<slug>.tex`). Die Subsection-Datei beginnt mit `\subsection{...}\label{sec:<slug>}` — **keine Chapter-Wrapper, keine `\input{}` in der Subsection-Datei selbst**. Der Master bindet die Subsections per `\input{}` ein.
- Zitation: `\parencite[S. X]{key}`. Sekundärzitate vermeiden. Direkte Zitate > 40 Wörter: `\begin{blockzitat}` (in `main.tex` definiert), nicht `\enquote{}`.
- Eigene Abb./Tab.: `\quelle{Eigene Darstellung.}` (Makro aus `main.tex`) unter Bild/Tabelle, kein `\cite{}`.
- Akronyme: `\ac{KÜRZEL}` (Definition in `pages/acronyms.tex` per `\acro{}`). Cross-Ref: `\autoref{sec:label}`. Anführungszeichen: `\enquote{}`.
- Float `[H]`, Caption vor `\label{}`. Tabellen `booktabs`. Kompakte Listen: `itemize[nosep]` (enumitem).
- Keine Änderungen an `main.tex` / `pages/cover.tex`. Projektangaben (Titel, Modul, Tutor:in …) nur in `pages/meta.tex`.
- **Diagramme**: kein Mermaid. Stattdessen direkt `tikzpicture` in der `.tex`-Datei mit den **vordefinierten Styles aus `main.tex`** (`\node[box]`, `\node[decision]`, `\draw[arr]`, `\draw[dashedarr]`) — Styles nicht pro Diagramm neu definieren. Caption + `\label{fig:...}` darüber, `\quelle{...}` darunter. Datendiagramme als `pgfplots`-`axis`.
- Wenn Subsection oder Subsubsection die halbe Seite Regel verletzt, Umsetzbarkeit als `\paragraph{}` prüfen. Wenn möglich: Trotzdem als eigene Datei wie Subsection, damit Kapitelplan mit Latex Dateistruktur konsistent bleibt. Wenn nicht möglich: User explizit fragen.

## Schreibstil (Anti-KI-Muster + Verständlichkeit)

Vollversion in `.claude/skills/_shared/hard-rules-formal.md` → Schreibstil **und** Verständlichkeit (dort einzige Kopie). Kurzerinnerung: keine Gedankenstriche als Satzfüller, keine Floskel-Öffner, keine Klischee-Übergänge, keine unbegründeten Absicherungsfloskeln, aktiv statt passiv, kurze klare Sätze; keine Kontrastfiguren (auch nicht zweisätzig aufgespalten oder als „statt"-Dauermuster), keine Pointen-Schlusssätze, Doppelpunkt-Ankündigungen und Betonungswörter („bewusst", „genau", „gezielt") sparsam, Satzrhythmus variieren (keine Staccato-Ketten). **Zusätzlich gilt: einfache Sprache vor akademischem Klang** — ein Gedanke pro Satz, Verben statt Nominalstil, alltagsnahe Wortwahl, Fachbegriffe bei erster Nennung in einem Halbsatz erklären, konkrete Beispiele; keine stilistische Verdichtung. Diese Regeln gelten zusätzlich zu den Voice-Vorgaben in `typen/<typ>.md`, nicht anstelle davon.

## Inhaltliche Qualitätsregeln (nur die für den aktuellen Papiertyp laut `typen/<typ>.md` pflichtigen anwenden)

- **Absatzlogik (IU-Pflicht, alle Typen)**: Jeder Absatz folgt dem Muster (1) Hauptaussage identifizieren und an den Anfang stellen, (2) erläutern, diskutieren, mit Nebenaussagen ergänzen, (3) Schlüsse ziehen, die zum nächsten Absatz überleiten. Kein Absatz endet mit reiner Beschreibung oder Selbstzweck-Aufzählung.
- **These erkennbar**: Kapitel trägt die Gesamtaussage mit, nicht nur Beschreibung. Kein Kapitel endet mit reiner Aufzählung — Syntheseleistung („Diese Arbeit schließt daraus …").
- **Gegenargumente**: stärkstes Gegenargument pro zentralem Argument reflektieren und entkräften.
- **Ergebnisse ≠ Interpretation** (nur Seminararbeit, nur empirisch): Befunde zuerst rein berichten (FACTUAL, `\parencite{}` für Methodik/Instrumente), Interpretation folgt (ARGUMENTATION). Auch bei zusammengeführtem Kapitel klar getrennt.
- **Limitationen dreischichtig**: (1) warum Limitation, (2) Mitigation, (3) wie zukünftige Forschung sie überwinden kann.
- **Aktualität/Zeitbezug**: in der Einleitung, sofern laut Typ-Datei pflichtig.

## Iterationsrhythmus (Schreiben ↔ Prüfen)

Skripte + Self-Check sind das Qualitätstor **pro Kapitel** — ein Voll-Audit nach jedem Kapitel ist nicht vorgesehen (lädt jedes Mal Typ-Datei, Hard Rules und alle Kapitel neu). Stattdessen:

1. **Nach dem ersten Hauptteil-Kapitel**: dem Nutzer ein **Kapitel-Audit** vorschlagen („Audit Kapitel: <name>", siehe `pruef-modus` → Audit-Umfänge). Das erste Kapitel prägt Zitierweise, Stil und Absatzlogik — ein systematischer Fehler, der hier gefunden wird, kopiert sich sonst in alle Folgekapitel. **Einmaliges Angebot:** Ist das erste Hauptteil-Kapitel bereits vorbei (egal ob das Audit damals durchgeführt wurde oder nicht), wird es nicht erneut vorgeschlagen — sonst verdrängt es den eigentlich fälligen Schreibschritt.
2. Danach die restlichen Kapitel schreiben. Solange noch eine Komponente in der Statustabelle nicht FERTIG ist, ist der nächste Schritt immer ein Schreibschritt, kein Audit.
3. **Sind alle Kapitel FERTIG, ist der nächste Schritt die Prüfer-Gegenlesung — nicht das Voll-Audit und nicht der Stresstest.** Vollständige Kette: Gegenlesung (frische Sitzung, kalt) → Gesamt-Stresstest → beide Runden gemeinsam abarbeiten (eine Schreib-Sitzung) → Voll-Audit → ggf. Delta-Re-Audit. Gegenlesung und Stresstest sind beide reine Lese-Schritte und ändern nichts; deshalb laufen sie hintereinander, bevor überhaupt überarbeitet wird — das spart eine komplette Überarbeitungs- und Prüfrunde.
4. Überarbeitung entlang `pruefbericht.md` in eigenen Sessions; danach Re-Audit als Delta (nur FAIL-Punkte), kein erneutes Voll-Audit — das kommt erst als Abgabe-Audit.

**Nächsten Schritt nie aus dem Gedächtnis nennen.** Die im Chat empfohlene nächste Aktion wird aus der Reihenfolge in `kapitelplan.md` → „Nächste Schritte" und der Statustabelle in `CLAUDE.md` abgelesen und muss mit der „Aktuellen Richtung" übereinstimmen, die dieselbe Nachricht in `CLAUDE.md` schreibt. Weicht die Empfehlung im Chat von der Datei ab, gilt die Datei — dann die Empfehlung korrigieren, nicht die Datei.

## Self-Check nach jedem Kapitel

- [ ] `check_formalia.py` gelaufen und 0 FEHLER? (deckt Pronomen, Anführungszeichen, quote-Env, `[H]`, Caption-Reihenfolge, `\underline`, `\include`, Blockzitat > 40 Wörter, ½-Seiten-Heuristik und Überschriften-Dopplung mechanisch ab — nicht erneut manuell prüfen)
- [ ] Kernargument aus dem Kapitelplan umgesetzt?
- [ ] Alle **Inhaltspunkte** aus dem Kapitelplan für diese Subsection im Text erkennbar umgesetzt? Kein Punkt stillschweigend ausgelassen?
- [ ] Alle Belege mit korrekten `\parencite{}`, per Skript gegen `references.bib` validiert?
- [ ] Eigene Abb./Tab. mit `\quelle{Eigene Darstellung.}`?
- [ ] Max. 3 Kapitelstufen?
- [ ] Akronyme per `\ac{}`? Labels konsistent (`sec:`, `fig:`, `tab:`)?
- [ ] Absätze pro Subsection im Richtwert laut `typen/<typ>.md`?
- [ ] Hauptkapitel schließt mit eigener Syntheseleistung?
- [ ] Für den Papiertyp laut `typen/<typ>.md` → Pflichtregeln pflichtige Punkte erfüllt (Gegenargument, Limitationen dreischichtig, ggf. Ergebnisse≠Interpretation)?
- [ ] Einleitung: Forschungslücke und — falls laut Typ-Datei pflichtig — Aktualität/Zeitbezug enthalten?
- [ ] Keine Anti-KI-Stil-Verstöße (Gedankenstrich-Füller, Floskel-Öffner, Klischee-Übergänge, unbegründete Absicherungsfloskeln, Kontrastfiguren inkl. Tarnformen, Pointen-Schlusssätze, Doppelpunkt-/Signalwort-Häufung, Staccato-Ketten)?
- [ ] Verständlichkeit: Sätze kurz und klar, Fachbegriffe bei erster Nennung erklärt, kein Nominalstil/keine stilistische Verdichtung — würde ein Laie jeden Absatz beim ersten Lesen verstehen?
- [ ] Alle diesem Kapitel zugewiesenen **Lieferobjekte** existieren tatsächlich als Datei beziehungsweise als `figure`/`table`/Anhangseintrag — nicht nur im Fließtext erwähnt? **Sonderregel:** Behauptet der Text die Existenz eines Artefakts („als Prototyp diente …", „das Formular gliedert …", „die Erhebung ergab …"), muss dieses Artefakt gezeigt oder im Anhang beigelegt sein.
- [ ] Alle diesem Kapitel zugeordneten Einträge der **wörtlichen Abhakliste** kommen im Text tatsächlich vor — Schlüsselbegriffe wörtlich, Berichtsinhalte als erkennbarer zusammenhängender Ort, `[VERENGT]`-Begriffe mit ausgeschriebener Begründung?
- [ ] Bei selbst definierter Bewertungstabelle: **jede Zelle spaltenweise gegen die Rubrik-Karte geprüft** — liegen alle Zeilen eines Kriteriums auf derselben Achse, und deckt der Fließtext jede Wertung? **Gegenprobe:** Bekommt das Objekt, gegen das sich die These richtet, durchweg die schlechtesten Wertungen? Dann ausdrücklich einräumen, worin seine reale Stärke besteht.
- [ ] Erhebt das Kapitel einen Einwand gegen die eigene Position oder benennt es eine Bedingung des eigenen Gelingens: wird sie im selben oder in einem späteren Kapitel beantwortet oder ausdrücklich als Limitation geführt — statt nur genannt zu werden?
- [ ] Alle nicht-belegten Eigenrecherche-Behauptungen entweder recherchiert (Protokoll im Kapitelplan **und** im Anhang) oder mit `% UNVERIFIED:` markiert?
