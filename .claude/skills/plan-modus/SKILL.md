---
name: plan-modus
description: Geleitetes Planen wissenschaftlicher Arbeiten (Hausarbeit, Fallstudie, Seminararbeit, Projektbericht) an der IU, vor dem Schreiben — mit zwei Betriebsarten („kompakt" als Default für kleine Arbeiten, „ausführlich" für empirische Seminararbeiten). Nutzen, wenn eine Aufgabenstellung vorliegt und noch kein Kapitelplan existiert, wenn der Nutzer eine Leitfrage, These oder Gliederung entwickeln will, oder wenn eine kapitelplan.draft.md im Projekt bereits existiert und eine frühere Plan-Session fortgesetzt werden soll. Deckt Readiness-Check (inkl. aufgabe.md), Literaturrecherche (Consensus MCP), Thesenkristallisation, Kapitelgerüst-Bestätigung, Kapitel-für-Kapitel-Planung und Argumentations-Stresstest ab. Ergebnis ist die Datei kapitelplan.md.
compatibility: Literaturrecherche in Schritt 1 nutzt die Consensus MCP (220M+ peer-reviewed Papers). Falls nicht verbunden, Schritt 1 überspringen und Nutzer auf manuelle Literaturbeschaffung hinweisen.
---

# Plan-Modus: Geleitetes Planen wissenschaftlicher Arbeiten

Alle Schritte als Dialog: Fragen stellen, Nutzer antwortet. Nach jedem Schritt INSIGHT extrahieren, Bestätigung einholen, Checkpoint schreiben.

Papiertyp-spezifische Details (Pflichtregeln, Bewertungsgewichte, Kapitelgerüst, Kernfragen) liegen zentral in `.claude/skills/_shared/typen/<typ>.md` — laden, sobald der Papiertyp in Schritt 0 feststeht. Die dortigen „Pflicht"-Punkte bestimmen, welche Fragen in Schritt 2/3 zwingend gestellt werden.

**`PERSISTENT.md` + `MEMORY.md`** (falls vorhanden) lesen — `[LERNEN:...]`-Einträge ohne `[ÜBERHOLT]`-Markierung anwenden; bei Widerspruch gewinnt `MEMORY.md`.

## Betriebsarten

In Schritt 0 festlegen und im Draft-Status notieren (`Betriebsart: kompakt` / `ausführlich`), damit Resume konsistent bleibt.

**Kompakt (Default** für Hausarbeit, Fallstudie, Projektbericht und Literatur-Seminararbeit): Kleine Arbeiten (7–10 Seiten, oft enge Aufgabenstellung) brauchen keine mehrwöchige Planungsphase — die Aufgabenstellung liefert Leitfrage und Rahmen meist schon. Deshalb:
- Schritt 0 + These (Schritt 2) + Kapitelgerüst (Schritt 2.5) in **einer** Dialogrunde bündeln — abfragen statt sokratisch herleiten.
- Schritt 1 (Literatur) nur auf Wunsch oder wenn Schritt 0 „Literatur fehlt" ergibt.
- Schritt 3: **eine Runde pro Hauptteil-Kapitel**. Einleitung/Schluss ohne eigene Runde — deren Inhalt ergibt sich aus These + Gerüst; im Kapitelplan trotzdem als eigener Block ausweisen.
- Schritt 4 (Stresstest) **Pflicht-Minimalpass**: **ein** Durchgang über die Kernargumente-Tabelle ist auch im Kompakt-Modus verbindlich (kostet eine Runde, kein voller Mehrfach-Modus). Grund: „nur wenn etwas wackelt" ist unzuverlässig — wer das Argument gebaut hat, ist der schlechteste Richter über seine Schwächen; ein Stark-Befund erreicht so unbemerkt den finalen Plan. Vertiefung auf einzelne Argumente nur auf Wunsch.
- Ziel: `kapitelplan.md` in **einer Session**.

**Ausführlich** (= voller Ablauf unten, Default nur für die empirische Seminararbeit; sonst opt-in per „plan ausführlich"): jeder Schritt einzeln, sokratische Herleitung, Pflicht-Stresstest.

Die Checkpoint-Mechanik gilt in beiden Betriebsarten unverändert — auch eine Kompakt-Session ist jederzeit unterbrechbar.

**Ablauf**: Schritt 0 Readiness (inkl. `aufgabe.md`) → Schritt 1 Literatur (nur wenn nötig) → Schritt 2 These → **Schritt 2.5 Kapitelgerüst bestätigen** → Schritt 3 Kapitel für Kapitel → Schritt 4 Stresstest (kompakt: optional) → Output `kapitelplan.md`.

---

## Resume-Check (immer zuerst, vor Schritt 0)

1. Prüfen, ob `kapitelplan.draft.md` im Projekt-Root existiert (Read-Tool, nicht aus Memory oder Gesprächsverlauf annehmen).
2. **Falls nein**: neue Arbeit → direkt mit Schritt 0 beginnen, `kapitelplan.draft.md` bei erstem Checkpoint neu anlegen.
3. **Falls ja**: **nur den Kopf der Datei lesen** (Read mit limit ≈ 25 Zeilen — `## Status` und `## Papierinfo` stehen per Format ganz oben) und dem Nutzer in 2–3 Sätzen den bisherigen Stand zusammenfassen (Papiertyp, Betriebsart, zuletzt abgeschlossener Schritt, Kernthese falls vorhanden). Den vollständigen Draft **nicht** pauschal laden — erst die Abschnitte nachlesen, die der wiederaufzunehmende Schritt tatsächlich braucht (Schritt 3: Kapitelgerüst + letzte Kapitelzusammenfassung; Schritt 4: nur Kernargumente-Tabelle; Output: dann vollständig). Dann fragen:
   - „Weitermachen bei Schritt `<nächster Schritt aus Status>`?" oder
   - „Von vorn beginnen (bisheriger Entwurf wird überschrieben)?"
4. Erst nach Antwort des Nutzers mit dem entsprechenden Schritt fortfahren. **Nie** stillschweigend bei Schritt 0 neu beginnen, wenn ein Entwurf existiert — das würde bereits erarbeitete Entscheidungen (These, Kapitelgerüst) verwerfen, ohne dass der Nutzer das gemerkt hat.

### Format `kapitelplan.draft.md`

```markdown
# Kapitelplan (Entwurf — in Bearbeitung)

## Status
Betriebsart: kompakt / ausführlich
Zuletzt abgeschlossen: Schritt <N> — <Name>
Nächster Schritt: Schritt <N+1> — <Name>
Letzte Aktualisierung: <Datum>

## Papierinfo
- Titel: ...
- Papiertyp: ... · Forschungstyp: ...

## INSIGHT-Sammlung (bisher)
1. [readiness] ...
2. [literaturrecherche] ... (falls durchgeführt)
3. [these] ... (falls erreicht)
4. [kapitelgeruest] ... (falls erreicht)
5. [<kapitel>_zusammenfassung] ... (je fertiges Kapitel aus Schritt 3)

## Kapitelgerüst (bestätigt, sobald Schritt 2.5 erreicht)
| Kapitel | Wortanteil | Zweck |
|---|---|---|
| ... | ... | ... |

## Kernargumente (laufend befüllt in Schritt 3 — einzige Lesequelle für Stresstest)
| Kapitel | Kernargument |
|---|---|
| ... | ... |

## Stresstest-Ergebnisse (sobald Schritt 4 erreicht)
| Argument | Stärke | Begründung |
|---|---|---|
```

**Checkpoint-Regel (append-only)**: Nach jedem Schritt (0, 1, 2, 2.5, jedem einzelnen Kapitel in Schritt 3, 4 — im Kompakt-Modus nach jeder gebündelten Runde) `kapitelplan.draft.md` **per Edit** aktualisieren — nicht per Vollrewrite. Konkret:
- Nur den `## Status`-Block per Edit anpassen (nächster Schritt, Datum).
- Neue INSIGHT-Einträge an die bestehende `## INSIGHT-Sammlung` anhängen.
- Neue Kapitelzeilen an die bestehenden Tabellen (`## Kapitelgerüst`, `## Kernargumente`, `## Stresstest-Ergebnisse`) anhängen.
- So bleibt jeder Checkpoint klein (~200–400 Tokens Edit-Größe), unabhängig von der Gesamtlänge des Drafts — kein quadratischer Tokenverbrauch über die Session.

**Zusätzlich** `CLAUDE.md` → „Aktueller Projektstatus" nach der dort hinterlegten Update-Regel aktualisieren (bestehende Zeile überschreiben, Platzhalter bei Schritt 2.5 durch echte `sec:<slug>`-Einträge ersetzen, „Aktuelle Richtung" auf den nächsten Schritt setzen).

**Sichtbarkeitspflicht**: Jeder Checkpoint wird im Chat kurz quittiert, nicht nur still in die Datei geschrieben — z. B. „✅ Checkpoint gespeichert: Schritt 2 (These) abgeschlossen, weiter mit Schritt 2.5. Projektstatus in CLAUDE.md aktualisiert." Ohne diese Zeile hat der Nutzer keine Möglichkeit zu erkennen, ob das Schreiben der Datei tatsächlich stattgefunden hat (z. B. bei einem stillen Schreibfehler).

---

## Schritt 0: Readiness-Check (1 Runde)

Aus der Aufgabenstellung (PDF/Text/Bild — einlesen, sonst `NOT READY`) extrahieren:
- **Rahmenthema**, **konkrete Leitfragen** (vorgegeben oder frei?), **formale Vorgaben** (Seiten, Quellen, Struktur, Abgabefrist), **spezifische Materialien** (Fall-PDF, Datensatz, vorgeschriebene Literatur), **Eigenanteil**, **Bewertungsbezüge** (falls die Aufgabenstellung eigene Kriterien nennt).

Fragen an den Nutzer:
1. Leitfrage formuliert (ein Satz) oder aus Aufgabenstellung übernommen?
2. Systematische Literaturrecherche bereits durchgeführt?
3. Papiertyp? (Hausarbeit/Fallstudie/Seminararbeit/Projektbericht)
4. Fehlen geforderte Materialien?
5. **Forschungstyp** (nur bei Seminararbeit relevant): empirisch (eigene Erhebung) oder Literaturarbeit (nur Sekundärquellen)? — **Achtung**: Auch bei Literaturarbeit bleibt das Methodik-Kapitel bestehen (als „Vorgehen der Literaturanalyse"), weil die IU 20 % Methodik IMMER bewertet (Details: `typen/seminararbeit.md` → Forschungstyp-Zusatzregel). Entscheidung im Draft dokumentieren.

Daraus ergibt sich die **Betriebsart** (siehe oben): empirische Seminararbeit → ausführlich, sonst kompakt — es sei denn, der Nutzer wünscht explizit anders.

```
[READINESS CHECK: PASS / NOT READY]
Aufgabenstellung: <vorhanden / fehlt>
Papiertyp: ... · Betriebsart: kompakt / ausführlich
Forschungstyp: <empirisch / Literaturarbeit>
Rahmenthema: ...
Konkrete Leitfragen: ...
Formale Vorgaben: Seiten: ... · Quellen: ... · Struktur: ... · Abgabe: ...
Materialien: ...
Eigenanteil: ...
```

**`aufgabe.md` schreiben (Single Source für die Aufgabenstellung):** Die extrahierten Punkte einmalig nach `aufgabe.md` im Projekt-Root destillieren — Papiertyp, Rahmenthema, **wörtliche** Leitfragen/Wahlaufgabe, formale Vorgaben (Seiten, Abgabefrist, geforderte Materialien), Bewertungsbezüge aus der Aufgabenstellung, Eigenanteil. Alle späteren Sessions (auch Schreib-/Prüf-Modus) lesen `aufgabe.md` statt des Aufgaben-PDFs — schneller, tokeneffizient, und die Aufgabenstellung ist Teil des Gedächtnisses. Die Abgabefrist zusätzlich in `CLAUDE.md` → „Fristen" eintragen.

**Prüfer-Anmerkungen destillieren (Pflichtbestandteil, falls die Datei existiert):** `sources/Anmerkungen vom Prüfer.md` (oder ähnlich benannt) auf **bindende Steuerungen** prüfen — Vorgaben, die von der reinen Aufgabenstellung abweichen oder sie präzisieren (z. B. „Wettbewerbsanalyse gilt als eigene Analyse, nicht als Zitat", „keine Primärdaten nötig", „KI-generierte Mockups kennzeichnen"). Diese **wörtlich** in `aufgabe.md` → eigener Abschnitt **„## Prüfer-Steuerungen"** übernehmen, je Steuerung mit kurzer Einordnung, wo sie im Plan wirkt. Existiert die Datei nicht, den Abschnitt mit „— keine Prüfer-Anmerkungen vorhanden —" anlegen, nicht stillschweigend weglassen (macht sichtbar, dass geprüft wurde). Grund: Diese Steuerungen sind bindend, tauchen aber in keiner anderen Pflichtquelle auf — ohne aktive Destillation werden sie nur gefunden, wenn der Nutzer zufällig darauf zeigt.

Sobald Papiertyp feststeht: `.claude/skills/_shared/typen/<typ>.md` laden.

**Machbarkeits-Check (Pflichtbestandteil — vor dem Kapitelgerüst):** Aus der Aufgabenstellung alle **Tätigkeiten** ableiten, die der Nutzer real ausführen muss — nicht nur schriftlich behandeln, sondern tatsächlich tun: Interviews führen, Prototypen bauen, Umfragen durchführen, Nutzertests machen, Daten erheben, Produkte analysieren, Vergleiche erstellen. Diese als Liste formulieren und **per `AskUserQuestion` aktiv mit dem Nutzer durchgehen**: „Die Aufgabenstellung erfordert X — ist das in Ihrem Rahmen möglich?" Nicht annehmen, dass es möglich ist, nur weil es in der Aufgabenstellung steht.

**Stellt sich heraus, dass eine Tätigkeit nicht real ausführbar ist** (kein Zugang zur Zielgruppe, keine Testumgebung, keine Daten, kein Werkzeug), wird das nicht stillschweigend durch eine Simulation ersetzt. Stattdessen in dieser Reihenfolge:

1. **Billigsten realen Ersatz suchen.** Was ist die Minimalvariante, die die Aufgabe *tatsächlich* erfüllt? Drei Kurzgespräche statt einer Studie, fünf Testpersonen statt fünfzig, eine Papierskizze statt eines lauffähigen Systems, ein Online-Fragebogen statt eines Interviews, Bekannte aus dem erweiterten Umfeld statt einer Fachzielgruppe, öffentliche Foren oder Communities statt direktem Zugang. Reale Miniaturen schlagen aufwendige Simulationen fast immer — sie erfüllen die Teilaufgabe tatsächlich und kosten oft weniger als deren sorgfältige Nachahmung.
2. **Aufgabenstellung-Justierung prüfen.** Wenn weder Original noch Minimalersatz möglich sind: Lässt die Aufgabenstellung Spielraum, die Perspektive so zu verschieben, dass eine andere, machbare Tätigkeit die Anforderung bedient? (Beispiel: Statt „Interview mit professionellen Fotografen" → „Befragung aktiver Nutzer einer Fotoplattform", falls die Aufgabenstellung nicht explizit Fotografen vorschreibt.) Die Aufgabenstellung dabei nicht verletzen — aber der Gültigkeitsbereich der These kann angepasst werden.
3. **Erst wenn auch die Justierung ausscheidet**, wird simuliert — und die Simulation als solche geplant, mit Herleitung ihrer Annahmen aus der Literatur.
4. **Jede Ersatzentscheidung wird dokumentiert** in `aufgabe.md` → **„## Ersatzentscheidungen"**: was versucht wurde, welche konkrete Rahmenbedingung es verhinderte, welcher Minimalersatz geprüft und warum verworfen wurde, und womit ein Folgeprojekt beginnen würde. Diese vier Angaben kommen später in das betroffene Kapitel.

**Lieferobjekt-Liste (Pflichtbestandteil von `aufgabe.md`):** Zusätzlich zu Text und Argumentation hält `aufgabe.md` einen Abschnitt **„## Lieferobjekte"** fest: alles, was am Ende **physisch in der Arbeit liegen muss**, nicht nur beschrieben wird. Auszugehen ist von den Substantiven der Aufgabenstellung: Nennt sie einen *Prototyp*, muss ein Prototyp vorliegen — als Skizze, Wireframe, Papiermodell oder Screenshot im Anhang. Nennt sie *Tests* oder *Nutzerfeedback*, müssen Erhebungsinstrument und Ergebnis vorliegen. Nennt sie einen *Vergleich*, muss die Erhebungsgrundlage vorliegen. Je Lieferobjekt eine Zeile: Objekt · Form (Abbildung, Tabelle, Anhang) · Zielort in der Arbeit · Status.

**Faustregel für Konzeptarbeiten:** Wer ein Produkt, System oder eine Plattform entwirft, liefert mindestens (a) **eine visuelle Darstellung** des Entworfenen, (b) **jedes selbst entwickelte Instrument** als Anhang (Formular, Fragebogen, Kriterienraster) und (c) **einen Namen** für das Konzipierte. Ohne (a) bleibt der Entwurf unanschaulich, ohne (b) ist er nicht nachvollziehbar, ohne (c) liest er sich wie eine Anforderungsliste statt wie ein Konzept. Diese drei Punkte in der Lieferobjekt-Liste voreintragen und mit dem Nutzer bestätigen oder streichen — mit Begründung, falls gestrichen.

**Namens-Kollisionscheck (Pflicht, sobald ein Name gesetzt wird):** Bevor ein Produkt-/Plattform-/Konzeptname final in den Plan übernommen wird, einmal kurz online prüfen (eine Suche genügt), ob der Name — oder sein Wortstamm — im selben Themenfeld bereits als Marke, App, Verein oder Projekt belegt ist. Eine Kollision (z. B. gleicher Name einer etablierten Marke im identischen Feld) untergräbt den im Bewertungsraster geforderten Eigenständigkeits-/Innovationsanspruch und ist markenrechtlich heikel. Fund → dem Nutzer als Entscheidung vorlegen (umbenennen oder bewusst abgrenzen), nicht stillschweigend übernehmen. Die finale Verfügbarkeitsprüfung (DPMA/Domain) bleibt Nutzer-Pflicht; dieser Check fängt nur die offensichtliche Kollision früh ab.

**Wörtliche Abhakliste (Pflichtbestandteil von `aufgabe.md`):** `aufgabe.md` enthält zusätzlich den Abschnitt **„## Wörtliche Abhakliste"** mit vier Blöcken, je Eintrag eine Zeile mit Spalte „adressiert in":

1. **Teilaufgaben** — jede nummerierte Aufgabe der Aufgabenstellung.
2. **Geforderte Berichtsinhalte** — jede Überschrift beziehungsweise jeder Block, den die Aufgabenstellung als Berichtsinhalt benennt. Diese brauchen einen erkennbaren *Ort* im Text, nicht nur verstreute Abdeckung: Wer die Arbeit gegen die Aufgabenstellung abhakt, sucht sie als Ganzes.
3. **Schlüsselbegriffe** — alle Substantive, die die Aufgabenstellung wörtlich nennt (etwa „Kategorisierung", „Medienformate", „Prototyp", „Bewertungen", „Foren"). Sinngemäße Abdeckung genügt der Bewertung nicht immer.
4. **Genannte Materialien** — jede in der Aufgabenstellung erwähnte Literatur, jeder Datensatz, jedes Werkzeug. Auch als „nicht verpflichtend" markierte Einstiegsliteratur gehört hierher: Dass ein empfohlener Titel im Literaturverzeichnis fehlt, fällt auf.

**Regel zur Begriffsverengung:** Verengt die Arbeit einen Zentralbegriff der Aufgabenstellung (etwa „Multimediaplattform" auf reine Standbilder, „Künstler:innen" auf eine Teilgruppe), ist das legitim — **aber die Verengung muss im Text ausdrücklich benannt und begründet werden.** Eine stillschweigende Verengung liest sich als Versäumnis, eine begründete als Fokussierung. Solche Fälle in der Abhakliste mit `[VERENGT]` markieren.

**Checkpoint**: `kapitelplan.draft.md` anlegen/aktualisieren — Betriebsart + Papierinfo + `[INSIGHT: readiness]` eintragen, Status auf „Nächster Schritt: 1 oder 2" setzen. `aufgabe.md`-Erstellung mitquittieren.

---

## Schritt 1: Literatur-Recherche (Consensus MCP)

Nur wenn Schritt 0 ergibt, dass Literatur fehlt/ergänzt werden muss — im Kompakt-Modus zusätzlich nur auf Wunsch. Sonst direkt zu Schritt 2.

| Papiertyp | Nötig? | Suchbudget |
|---|---|---|
| Hausarbeit | Ja | 3–5 Suchen |
| Seminararbeit | Ja | 5–8 Suchen, mit `study_types`-Filter |
| Fallstudie | Gezielt | 2–3 Suchen, nur Theorie-Konzepte |
| Projektbericht | Optional | 1–2 Suchen, nur bei Theorie-Bezug |

**Framework wählen** (mit Nutzer, 4–5 Sub-Bereiche, Suchbudget Quick 3–5 / Standard 5–8):
- **PICO** — Gesundheit, Psychologie, Pädagogik, Sozialwissenschaften mit Intervention.
- **SPIDER** — qualitative/erfahrungsbasierte Fragen ohne klare Intervention.
- **Dekomposition** (Mechanismus/Anwendungen/Limitationen/Vergleiche) — Technik, Wirtschaft, IT.

**Regeln beim Suchen**: sequenziell (1 Query/Sek. Rate-Limit); Query 4–8 Wörter, akademische Terminologie; **nur tatsächlich von Consensus zurückgegebene Papers zitieren, nie erfinden**; wenig Ergebnisse → ehrlich melden, nicht mit Modellwissen auffüllen; mehrfach auftauchende Papers = wahrscheinlich seminal; Sekundärquellen vermeiden, Primärquellen direkt zitieren.

**Parameter**: `query` (Pflicht, 4–8 Wörter) · `year_min`/`year_max` · `study_types` (Seminararbeit-Pflicht: `rct`, `meta-analysis`, `systematic review`, `literature review`, `case report`, `non-rct experimental`, `non-rct observational study`) · `sjr_max` (1=Q1, 2=Q2) · `human` (bool) · `sample_size_min` · `exclude_preprints` · `medical_mode`.

Nach allen Suchen synthetisieren:

```
[INSIGHT: literaturrecherche]
Frameworks: ...
Sub-Bereiche: 1. ... 2. ... 3. ...
Gefundene Papers: <Anzahl>
Seminal/Foundational: ...
Haupt-Themen: ...
Forschungslücken: ...
Empirische Papers (Seminararbeit): <Liste mit study_type>
```

Output an Nutzer: Priority Reading Order (3–5 Papers, geordnet), pro Paper Titel/Autoren/Journal/Jahr/Citation-Count/1-Satz-Relevanz, Forschungslücken.

**Zotero-Erinnerung (nicht überspringen, eigene Zeile im Chat, nicht nur Nebensatz)**: Gefundene Paper jetzt in Zotero importieren — auch ohne PDF, Metadaten reichen für den BBT-Key — und Better BibTeX exportieren lassen, damit `references.bib` rechtzeitig vor Schreib-Modus bereitsteht. Ohne diesen Schritt fehlen dort die BBT-Keys für `\parencite{}`, und Schreib-Modus darf laut eigener Regel keine Keys erfinden.

**Checkpoint**: `[INSIGHT: literaturrecherche]` + Priority Reading Order in `kapitelplan.draft.md` eintragen, Zotero-Erinnerung im Chat quittiert, Status auf „Nächster Schritt: 2" setzen.

**Session-Schnitt empfohlen**: Nach diesem Checkpoint dem Nutzer aktiv vorschlagen, die Session zu beenden und Schritt 2 frisch zu starten. Begründung: Die Consensus-Rohtreffer sind der größte Kontextposten der Planung, aber alles Weiterverwendbare steht destilliert im Draft — eine neue Session startet schlanker und günstiger. Zudem wechselt hier laut Modellempfehlung (siehe `_shared/modell-empfehlung.md`) ohnehin das Modell (Schritt 0–1: Sonnet · Schritt 2–4: Opus/hohes Thinking), was nur per Sessionwechsel geht. Nichts geht verloren: Der Resume-Check setzt exakt bei Schritt 2 wieder auf.

---

## Schritt 2: These kristallisieren (kompakt: mit 2.5 gebündelt · ausführlich: 1–2 Runden)

Leitfrage ist keine These. Template: „Diese Arbeit argumentiert _____, weil _____, basierend auf _____."

Mehrstufige These prüfen (deskriptiv immer, erklärend/normativ je nach Typ — siehe `typen/<typ>.md` → Pflichtregeln, Einträge „Normative Ebene" und „Erklärende Ebene"):

Nachfragen: Wie würde jemand widersprechen (stärkstes Gegenargument)? Was bedeutet das für Praxis/Fall/Projekt? Welche laut Pflichtregeln pflichtige Ebene fehlt noch?

```
[INSIGHT: these]
Kernthese: ...
Ebenen: deskriptiv: ... · erklärend: ... · normativ: ...
Argumentationstyp: ...
Gültigkeitsbereich: ...
Grenzen: ...
```

**Checkpoint**: `[INSIGHT: these]` in `kapitelplan.draft.md` eintragen, Status auf „Nächster Schritt: 2.5" setzen (kompakt: Checkpoint erst nach der gebündelten Runde 0+2+2.5).

---

## Schritt 2.5: Kapitelgerüst bestätigen (1 Runde)

**Zweck**: Bevor Schritt 3 in Detailfragen pro Kapitel geht, das Kapitel-Skelett sichtbar machen und vom Nutzer bestätigen lassen. Verhindert, dass Strukturprobleme (z. B. „Ergebnisse/Diskussion soll zusammengelegt werden", „kein Methodik-Kapitel nötig") erst nach mehreren investierten Dialogrunden auffallen.

1. `typen/<typ>.md` → Abschnitte „Bewertung" und „Kapitelgerüst & Kernfragen" heranziehen.
2. Skelett als Tabelle vorlegen: Kapitel, Wortanteil (%), Zweck in einem Satz.
3. **Seitenbudget an den Bewertungsgewichten ausrichten** (aus `typen/<typ>.md` → Bewertung) und dem Nutzer die Ableitung kurz zeigen — Beispiele: Hausarbeit: Argumentation 40 % → Diskussion ist das größte Kapitel; Fallstudie: Analyse + Konzepte + Ergebnis = 75 % → Theorie bewusst knapp (IU-Reproduktionsverbot); Projektbericht: Prozess + Qualität = 50 % → Durchführung + Reflexion dominieren. So fließt das Bewertungsraster direkt in die Budgetverteilung ein, statt erst im Audit aufzutauchen.
   **Abdeckung statt nur Gewicht:** Neben dem Seitenbudget bekommt jedes Bewertungskriterium aus `aufgabe.md` beziehungsweise `typen/<typ>.md` ein **zuständiges Kapitel** zugewiesen — und, wo das Kriterium mehrere Dimensionen nennt, **jede Dimension einzeln**. Ein Kriterium wie „Transfer: Technologie ↔ gesellschaftliche und wirtschaftliche Bedeutung" hat drei Dimensionen; zwei davon abzudecken und die dritte auszulassen ist der wahrscheinlichste Fehler, weil zwei starke Dimensionen den Eindruck von Vollständigkeit erzeugen. Ergebnis als Tabelle in `kapitelplan.md`:
   | Bewertungskriterium | Dimension | Zuständiges Kapitel | Wie eingelöst |
   |---|---|---|---|
   **Besonders zu beachten:**
   - **Technische Dimension.** Bei Konzept- und Produktarbeiten ist sie die am häufigsten ausgelassene, weil sich Zielgruppe, Nutzen und Markt leichter schreiben. Fordert das Kriterium einen Technologiebezug, gehört mindestens ein Absatz zur technischen Umsetzung in den Plan.
   - **Innovationsanspruch.** Verlangt ein Kriterium Innovationskraft oder den Vergleich zu bestehenden Produkten, wird schon im Plan festgehalten, **was genau neu ist** und in welchem Kapitel das ausgesprochen wird. Besteht die Leistung in einer Kombination bestehender Elemente, ist das ein tragfähiges Argument — es muss dann aber offensiv als der innovative Kern benannt werden, nicht beiläufig relativiert.
4. **Slug pro Kapitel festlegen** — gemeinsam mit dem Nutzer, Dateiname-Basis in snake_case, ASCII (z. B. `einfuehrung`, `theorie_konzept_a`, `fallanalyse`, `schluss`). Wird zur Grundlage für:
   - Datei: `chapters/<kapitelordner>/<slug>.tex` (Master) bzw. `chapters/<kapitelordner>/<nn>_<slug>.tex` (Subsections)
   - Label: `\label{sec:<slug>}`
   - Status-Tabellen-Eintrag in `CLAUDE.md` (Identifikator = `sec:<slug>`)
5. Nutzer bestätigt oder passt an (z. B. Kapitel zusammenlegen, bei Literaturarbeit-Seminararbeit Ergebnisse-Zeile streichen).
6. **Lieferobjekt-Zuordnung:** Jedes Objekt aus `aufgabe.md` → „Lieferobjekte" genau einem Kapitel oder dem Anhang zuweisen und im Kapitelblock von `kapitelplan.md` eintragen. Bleibt ein Objekt ohne Ort, ist das Skelett unvollständig — vor Schritt 3 mit dem Nutzer klären. **Ein Lieferobjekt ohne zugewiesenes Kapitel wird am Ende nicht existieren.**
7. **Begriffs-Zuordnung:** Jeden Eintrag der wörtlichen Abhakliste aus `aufgabe.md` genau einem Kapitel zuordnen und die Spalte „adressiert in" ausfüllen. Bleibt ein Eintrag ohne Kapitel, ist das Skelett unvollständig — vor Schritt 3 klären. Bei `[VERENGT]`-Einträgen zusätzlich festhalten, **wo** die Begründung der Verengung stehen soll. **Sonderfall Vergleichsarbeiten:** Nennt die Aufgabenstellung mehrere zu untersuchende Schlüsseleigenschaften, muss jede davon **eigenständig erhoben** werden — als eigenes Kriterium beziehungsweise eigene Tabellenspalte, und für **alle** untersuchten Objekte, nicht nur für die, bei denen sie auffällt.
8. **Rubrik-Karte bei eigenen Bewertungsmatrizen:** Plant die Arbeit eine selbst definierte Vergleichstabelle (Kriterien × Objekte mit Wertungen), wird je Kriterium festgehalten: **(a)** was es misst, **(b)** was „stark", „mittel", „schwach" jeweils konkret bedeuten, **(c)** welche Achse *nicht* gemeint ist (typische Verwechslung, etwa „Vorhandensein eines Werkzeugs" gegen „Aktivität der Nutzung"). Ohne (c) driften Definition und Wertung auseinander. **Sortenreinheit:** Alle Kriterien einer Matrix müssen **von derselben Art** sein. Ein Kriterium, das kein Merkmal misst, sondern ein Gesamturteil über die Eignung fällt, gehört nicht als gleichrangige Spalte in dieselbe Tabelle. Solche Kriterien entweder ausdrücklich als zusammenfassende Spalte kennzeichnen oder in den Fließtext verlagern.
9. Bestätigtes Skelett wird zur Grundlage für Schritt 3 — jedes Kapitel dort in genau dieser Reihenfolge behandeln.

```
[INSIGHT: kapitelgeruest]
Papiertyp: ...
Forschungstyp: ...
Kapitel (bestätigt): 1. ... (X %) · sec:<slug> | 2. ... (Y %) · sec:<slug> | ...
Budget-Ableitung aus Bewertung: ...
Abweichungen vom Standard-Skelett: ...
```

**Checkpoint**: `[INSIGHT: kapitelgeruest]` + bestätigte Kapitelgerüst-Tabelle in `kapitelplan.draft.md` eintragen, Status auf „Nächster Schritt: 3 — Kapitel <erstes Kapitel>" setzen.

---

## Schritt 3: Kapitel für Kapitel (kompakt: 1 Runde je Hauptteil-Kapitel · ausführlich: 1–2 Runden je Kapitel, Theorie bei Seminararbeit bis 3)

Pro Kapitel aus dem in Schritt 2.5 bestätigten Skelett: Kernfragen stellen (aus `typen/<typ>.md`) → diskutieren → Kapitelzusammenfassung → INSIGHT extrahieren → Bestätigung einholen. **Kompakt**: nur Hauptteil-Kapitel einzeln behandeln; Einleitung und Schluss aus These + Gerüst ableiten und im Kapitelplan als eigene Blöcke ausweisen (ohne eigene Dialogrunde). **Ausführlich**: alle Kapitel einzeln; bei komplexen Theorie-Kapiteln zweite/dritte Runde für Literatur-Landkarte und Synthese, falls laut Pflichtregeln pflichtig.

Nach Bestätigung des Kernarguments und der Belege: **Inhaltspunkte pro Subsection gemeinsam mit dem Nutzer festlegen.** Dabei den Argumentationsfluss klären — wie führt jede Subsection zum Kernargument des Kapitels hin? Bei Kompakt-Modus: Inhaltspunkte vorschlagen und bestätigen lassen (nicht sokratisch herleiten). Bei Ausführlich-Modus: gemeinsam erarbeiten.

### Techniken (aus `typen/<typ>.md` anwenden, falls dort als Pflicht/empfohlen markiert)

**Turning Point**: Anerkanntes Seminal-Paper benennen → methodische/inhaltliche Lücke identifizieren → Platz für eigene Arbeit eröffnen. Formulierungshilfe: „Obwohl [Seminal Paper] [Feststellung], ergeben sich aus [methodische Lücke] Zweifel an [Gültigkeitsbereich] — hier setzt diese Arbeit an."

**Literatur-Landkarte**: Verortung der eigenen Arbeit in der bestehenden Forschung (Text oder ASCII-Skizze). Beantwortet: „An welcher Kreuzung der Forschung steht diese Arbeit?"

**Limitationen dreischichtig** (im Schluss-/Diskussionskapitel, bei allen Typen Pflicht): (1) warum ist es eine Limitation, (2) was wurde zur Mitigation getan, (3) wie kann zukünftige Forschung sie überwinden. Reines Auflisten ist unzureichend.

### Kapitelzusammenfassung (Template)

```
### Kapitel: <Name>
Zweck: ...
Kernargument: ...
Belege: 1. ... 2. ... 3. ...
Risiko: ...
Wortzahl (Richtwert): ...
Faktenbasis: Literatur / eigene Recherche / eigene Konzeptleistung
Zu verifizieren vor dem Schreiben: <Liste konkreter Behauptungen, oder „—">
Geplante Subsections:
  1. <nn>_<slug> — <Titel>
     Argumentationsfluss: <wie diese Subsection zum Kapitelargument beiträgt — 1 Satz>
     Inhaltspunkte:
     - <konkreter Punkt, der im Text vorkommen muss>
     - <...>
     - <3–5 Punkte; inhaltlich (was), nicht stilistisch (wie)>
  2. <nn>_<slug> — <Titel>
     Argumentationsfluss: ...
     Inhaltspunkte:
     - ...
(mind. 2 Subsections oder keine Unterteilung — Schreib-Modus übernimmt diese Struktur 1:1)

**Regeln für Inhaltspunkte:**
- Inhaltlich, nicht stilistisch: „Definition OC nach Meyer & Allen einführen" — nicht „einen klaren Einstiegssatz schreiben".
- Konkret genug, dass der Schreib-Modus nicht raten muss, aber offen genug, dass der Text nicht zum Lückentext wird.
- Jeder Punkt = eine prüfbare Aussage: Nach dem Schreiben muss erkennbar sein, ob der Punkt im Text vorkommt oder nicht.
- Belege aus dem Kapitelblock den passenden Inhaltspunkten zuordnen, wo möglich.
Lieferobjekte: <Abbildung/Tabelle/Anhang> — <Bezeichnung> — <Zielort> (nur wenn diesem Kapitel zugeordnet)
Rubrik-Karte (nur bei eigener Bewertungsmatrix):
  | Kriterium | Art (Merkmal/Gesamturteil) | misst | stark = | mittel = | schwach = | NICHT gemeint |
  |---|---|---|---|---|---|---|
Rechercheprotokoll (nur bei eigener Recherche): <Behauptung> — <Quelle> — <Datum> — <Beobachtungsmerkmal>
Bestätigung: Ja / Nein
[INSIGHT: <name>_zusammenfassung] ...
```

**Zitier-Klassifikation (Pflicht, je Quelle unter „Belege"):** Nicht jede genannte Quelle ist eine Zitierquelle. Jede Quelle eindeutig einordnen und als Suffix hinter der Belege-Zeile vermerken:
- **(a) zitiert** — geht in `\parencite`, braucht einen BBT-Key in `references.bib`.
- **(b) eigene Analyse/Sichtung** — eigene Beobachtung oder Vergleichsanalyse (z. B. Plattform-Sichtung, Konkurrenzvergleich, SWOT): `\quelle{Eigene Darstellung.}` bzw. eigene Beobachtung im Fließtext, **kein** `\parencite`, **nicht** in `references.bib`.
- **(c) unzulässig** — Skripte, Vorlesungsfolien, Webinars (siehe `hard-rules-formal.md` → Zitationen, Sperrliste): auf eine zitierfähige Primärquelle ausweichen, nicht in den Plan übernehmen.

Beispiel: `Belege: 1. Meyer & Allen 1991 [zitiert] · 2. eigene Sichtung von 5 Konkurrenzplattformen [eigene Analyse]`. Nur Klasse (a) geht in die BBT-Key-Prüfung von `schreib-modus` ein — sonst droht dort ein erfundener Key für eine Quelle, die gar keinen braucht.

**Recherche-Gate:** Steht bei „Faktenbasis" *eigene Recherche* (Produktfeatures, Marktdaten, Werkzeugvergleiche, Preise), wird der Faktenstand **vor** dem Schreiben erhoben. Solche Angaben tragen meist eine Vergleichstabelle, auf die spätere Kapitel aufsetzen; eine Korrektur nach dem Schreiben schlägt auf jede daran hängende Stelle durch. Das Ergebnis kommt als **Rechercheprotokoll** in den Kapitelblock: je Behauptung Datum, Quelle, Befund — und, bei Aktivitäts- oder Qualitätsurteilen, **das Beobachtungsmerkmal**, an dem das Urteil hängt. Ein Urteil wie „wenig belebt" ohne benennbares Merkmal ist eine Behauptung, keine Erhebung. Die abschließende Verifikation am Original bleibt Nutzer-Pflicht (IU-KI-Richtlinie); das Protokoll ersetzt sie nicht, macht aber sichtbar, *was* zu verifizieren ist.

**Optional — Literatur-Volltexte bereits während der Planung sichten:** Liegen zu Schritt 1 gefundene Paper bereits als PDF vor (z. B. Open-Access-Download), kann es sich lohnen, sie schon jetzt nach zitierfähigen Stellen zu durchsuchen, statt das komplett dem Schreib-Modus zu überlassen — spart eine zweite Lektüre und sichert früh ab, dass die geplante Argumentation wirklich durch den Volltext gedeckt ist (nicht nur durchs Abstract). Ergebnis kommt mit Seitenzahl in `kapitelplan.draft.md` **und** in den finalen `kapitelplan.md`-Output unter „Zitat-Kandidaten" (siehe Output-Template unten) — Schreib-Modus liest nur `kapitelplan.md`, nicht den Draft.

**Checkpoint (Schritt 3, präzisiert)**: Pro Kapitel NUR per Edit:
1. Kapitelzusammenfassung + INSIGHT an die `## INSIGHT-Sammlung` anhängen.
2. Die Zeile `<Kapitel> | <Kernargument>` an die Tabelle „Kernargumente" anhängen (nicht nur im Fließtext der Kapitelzusammenfassung belassen — das ist die einzige Stelle, die der Stresstest in Schritt 4 liest).
3. Status auf „Nächster Schritt: 3 — Kapitel <nächstes Kapitel>" bzw. bei letztem Kapitel „Nächster Schritt: 4" (kompakt: „Nächster Schritt: Output") setzen.
4. **Niemals** die gesamte Datei neu schreiben — bei 6+ Kapiteln mit Zusammenfassungen, INSIGHTs und Tabellen wächst jeder Checkpoint sonst quadratisch über die Session.

---

## Schritt 4: Argumentations-Stresstest (ausführlich: voller Mehrfach-Modus · kompakt: Pflicht-Minimalpass)

**Kompakt**: **ein** Pflicht-Durchgang über die Kernargumente-Tabelle — nicht mehr optional. Der Selbst-Check „wackelt hier etwas?" ist strukturell blind für die eigenen Schwächen; ein einzelner Mehrfach-Modus-Durchlauf kostet eine Runde und fängt genau die Stark-Befunde ab, die sonst unbemerkt in den finalen Plan wandern. Vertiefung auf einzelne Argumente nur zusätzlich auf Wunsch.

Ruft den eigenständigen `stresstest`-Skill im **Mehrfach-Modus** auf (siehe `stresstest/SKILL.md`): alle Kernargumente aus `kapitelplan.draft.md` in einem Durchgang prüfen, Ergebnis als Tabelle.

Alle Argumente mind. **Mittel** → weiter zum Output. Sonst: Argumente nachschärfen (Nutzer reagiert inhaltlich, nicht ich).

**Checkpoint**: Stresstest-Tabelle aus `stresstest`-Skill in `kapitelplan.draft.md` eintragen, Status auf „Nächster Schritt: Output" setzen.

---

## Output: `kapitelplan.md` erzeugen

Alle Inhalte liegen bereits in `kapitelplan.draft.md` (Checkpoints aus Schritt 0–4). Dieser letzte Schritt konsolidiert sie nur noch zur finalen Datei — es müssen keine Inhalte neu erfragt werden.

1. `kapitelplan.draft.md` vollständig lesen.
2. Daraus `kapitelplan.md` **im Projekt-Root** nach dem Format unten schreiben (Schreib-Modus liest später nur diese Datei, nicht den Draft). `kapitelplan.md` enthält bewusst **keine** vollständige INSIGHT-Sammlung — die ist im Draft archiviert und blockiert sonst den Schreib-Modus-Token-Budget mit Ballast.
3. **Output-Integritätscheck (Pflicht, vor Fertigstellung):** Output ⊇ Draft-Entscheidungen prüfen. Jede bestätigte Zuordnung aus dem Draft — Abhakliste-Einträge, Lieferobjekte, im INSIGHT bestätigte Feature-/Begriffs-Ideen — muss im finalen `kapitelplan.md` einen erkennbaren Ort haben. Dazu jede `[INSIGHT: ...]`-Zeile und jede Tabellenzeile aus dem Draft gegen den geschriebenen Output abgleichen (Grep-artig, Begriff für Begriff). Fehlt einer, entweder ergänzen oder bewusst mit einem Satz Begründung streichen — nicht stillschweigend verlieren. Anlass: „Journaling/Menüplanung" fiel bei einer Konsolidierung so heraus, obwohl im Draft zugeordnet.
4. `kapitelplan.draft.md` **nicht löschen** — stattdessen mit Hinweis markieren:
   ```markdown
   # Kapitelplan (Entwurf — abgeschlossen)
   ## Status
   Zuletzt abgeschlossen: Output — siehe kapitelplan.md
   Letzte Aktualisierung: <Datum>
   ```
   So bleibt die INSIGHT-Sammlung als Archiv verfügbar, blockiert aber keine Resume-Verwechslung in einer späteren Session.

```markdown
# Kapitelplan

## Papierinfo
- **Titel**: ...
- **Papiertyp**: ... · **Forschungstyp**: ...
- **Gesamtwortzahl (Richtwert)**: ...
- **Erstellt am**: <Datum> · **Plan-Session-Checkpoints**: `kapitelplan.draft.md` (Archiv)

## Kapitel 1: <Name> (X–Y Wörter)
- **Datei**: `chapters/<kap>/<kap>.tex` (Master) · **Label**: `sec:<slug>`
- **Kernargument**: ...
- **Belege**: ... (je Quelle mit Zitier-Klassifikation `[zitiert]` / `[eigene Analyse]` / `[unzulässig — ersetzt durch ...]`)
- **Gegenargumente**: ...
- **Antwort**: ...
- **Argumentationsstärke**: Stark/Mittel (kompakt ohne Stresstest: „ungeprüft")
- **Faktenbasis**: Literatur / eigene Recherche / eigene Konzeptleistung
- **Rechercheprotokoll** (nur bei eigener Recherche): <Behauptung> — <Quelle> — <Datum> — <Beobachtungsmerkmal>
- **Lieferobjekte**: <Abbildung/Tabelle/Anhang> — <Bezeichnung> — <Zielort> (nur wenn zugeordnet)
- **Rubrik-Karte** (nur bei eigener Bewertungsmatrix):
  | Kriterium | Art (Merkmal/Gesamturteil) | misst | stark = | mittel = | schwach = | NICHT gemeint |
  |---|---|---|---|---|---|---|

### Subsection: <nn>_<slug> — <Titel>
- **Argumentationsfluss**: <1 Satz>
- **Inhaltspunkte**:
  - <Punkt 1>
  - <Punkt 2>
  - <...>

### Subsection: <nn>_<slug> — <Titel>
- **Argumentationsfluss**: ...
- **Inhaltspunkte**:
  - ...

[... alle Kapitel aus dem in Schritt 2.5 bestätigten Skelett, inkl. Einleitung/Schluss-Blöcken ...]

## Literaturliste (nur wenn Schritt 1 durchgeführt)
### Priority Reading Order
1. <Titel> — <Autoren>, <Journal>, <Jahr> (citations: <N>) — <Consensus-URL>

### Forschungslücken (für Theorie & Argumentation)
- ...

## Zitat-Kandidaten (nur falls Volltexte bereits geprüft wurden, siehe Schritt 3 → Recherche-Gate)
| Paper | Seite | Fundstelle (paraphrasiert/Zitat) | Verwendungszweck (Subsection) |
|---|---|---|---|
| ... | ... | ... | ... |

Hinweis: Recherche-Vorarbeit — Nutzer prüft Seitenzahlen/Formulierungen final am Original (IU-KI-Richtlinie).

## Nächste Schritte
→ pruef-modus (Umfang „Plan-Audit"): Kapitelplan auf Kohärenz prüfen — **empfohlen** vor dem Schreiben, **Pflicht** ab > 3 Kapiteln oder eigener Vergleichsmatrix/Rubrik-Karte
→ pruef-modus (Umfang „Bereitschafts-Check"): mechanische Checkliste direkt vor dem ersten schreib-modus-Aufruf — **empfohlen**
→ danach schreib-modus: Kapitel nacheinander verfassen
```
