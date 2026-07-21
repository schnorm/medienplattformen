---
name: pruef-modus
description: Prüft eine wissenschaftliche Arbeit oder einen Kapitelplan an der IU gegen Formalia, Argumentationsqualität, Struktur und Abgabe-Voraussetzungen (Turnitin, Eidesstattliche Erklärung) vor der Abgabe, mit numerischem Score und Abgabe-Schwelle. Nutzen, wenn ein Entwurf, ein fertiges Kapitel oder ein kapitelplan.md vorliegt und ein Audit gewünscht ist — oder wenn benotetes Tutor-Feedback in Lernpunkte übersetzt werden soll („Feedback einarbeiten", Umfang Feedback-Destillat). Prüft nur die für den jeweiligen Papiertyp laut Typ-Datei pflichtigen Kriterien, nicht pauschal alle. Dies ist der einzige Einstiegspunkt für Audits — führt intern mehrere fokussierte Teil-Checks nacheinander aus, statt sich auf separat aufgerufene Skills zu verlassen.
compatibility: .claude/skills/_shared/scripts/check_bib_keys.py benötigt Python 3 und Zugriff auf references.bib. Teil-Check D (Build) benötigt lualatex + biber; falls nicht verfügbar, wird er übersprungen und im Bericht vermerkt.
---

# Prüf-Modus: Audit und Review

**Wichtig zur Nutzung**: Dieser Skill ist der alleinige Einstiegspunkt für Audits — nicht mehrere separate Skills. Die Teil-Checks laufen automatisch nacheinander innerhalb dieses einen Aufrufs, mit jeweils engem Fokus statt einer vermischten Gesamtliste. Nur bei einer gezielten Einzelanfrage („prüf nur die Zitate") wird ausschließlich der passende Teil-Check ausgeführt.

## Audit-Umfänge (zuerst bestimmen, welcher gemeint ist)

- **Kapitel-Audit** („Audit Kapitel: <name>" — empfohlen nach dem ersten Hauptteil-Kapitel): nur Teil-Check A + B auf dieses eine Kapitel, plus beide Skripte. Kein Build, kein Outline-Check, **kein Score** — die Score-Skala ist auf die Gesamtarbeit kalibriert und wäre für ein Einzelkapitel irreführend. Ergebnis: kurze Fundliste im Chat + ggf. Statuszeile. Zweck: systematische Muster (Zitierweise, Stil, Absatzlogik) früh erkennen, **bevor sie sich in die Folgekapitel kopieren.**
- **Plan-Audit** („Plan-Audit" — **empfohlen**, sobald `kapitelplan.md` final ist, **vor** dem ersten `schreib-modus`-Aufruf; **Pflicht**, sobald die Arbeit mehr als 3 Kapitel oder eine eigene Vergleichsmatrix/Rubrik-Karte hat — dann vor dem Schreiben aktiv vorschlagen statt nur anzubieten): prüft ausschließlich `kapitelplan.md` (plus `aufgabe.md` als Maßstab) auf innere Kohärenz, **bevor** Schreib-Sessions investiert werden. Kein Score (analog Kapitel-Audit) — Ergebnis ist eine kurze Fundliste als Arbeitsliste, keine Umsetzung im selben Lauf (Prüfer/Autor trennen). Prüfpunkte:
  - **Roter Faden über Inhaltspunkte:** Führt jede Subsection über ihren Argumentationsfluss zum Kapitel-Kernargument? Bauen die Kapitel-Kernargumente aufeinander auf (Einleitung → Hauptteil → Fazit ohne Sprung/Bruch)?
  - **Inhaltspunkt → Argument-Verknüpfung:** Dient jeder Inhaltspunkt entweder einem Argument oder einer Pflicht-Abdeckung (Abhakliste/Lieferobjekt)? **Waisen** (Punkte, die nichts tragen) markieren — Kürzen oder Zuordnen.
  - **Redundanz/Widerspruch zwischen Subsections:** Steht derselbe Punkt an zwei Stellen? Widersprechen sich Aussagen (z. B. Feature in einem Kapitel zugesagt, in einem anderen verneint)?
  - **Flughöhe:** Sind Inhaltspunkte inhaltlich („was kommt vor") statt stilistisch („wie formulieren")? Stil-Punkte umschreiben.
  - **Abdeckungs-Re-Verify:** Jeden `aufgabe.md`-Abhakliste-Eintrag **und** jedes Lieferobjekt erneut gegen die *finalen* Inhaltspunkte in `kapitelplan.md` prüfen — nicht gegen den Draft. Details driften zwischen Schritt 2.5 und Schritt 3 der Planung.
  - **Budget-Realismus:** Passt die Inhaltspunkt-Dichte je Subsection zum %-Budget? Überladene Subsections (zu viele Punkte für den Umfang) früh markieren.
- **Bereitschafts-Check** („Bereitschafts-Check" — **empfohlen** direkt vor dem allerersten `schreib-modus`-Aufruf, nach abgeschlossenem Plan-Audit): rein **mechanische** Checkliste, keine inhaltliche Bewertung, kein Score. Zweck: Blocker-Aussagen werden hier **geprüft statt geschätzt** — eine Schätzung („Zotero wird schon nötig sein") kann falsch sein, wo ein Dateicheck es in Sekunden klärt. Punkte:
  - [ ] `references.bib` enthält einen Key für **jede** als `[zitiert]` klassifizierte Quelle aus `kapitelplan.md` (`check_bib_keys.py references.bib --dir chapters/` bzw. Grep der Belege-Zeilen gegen die Keys, falls noch nichts geschrieben ist).
  - [ ] Jeder `aufgabe.md`-Abhakliste-Eintrag **und** jedes Lieferobjekt hat einen Ort im Plan (Spalte „adressiert in" bzw. Lieferobjekt-Zuordnung in `kapitelplan.md` vollständig?).
  - [ ] Kein offener **Stark**-Stresstest-Befund; `AENDERUNGEN.md` (falls vorhanden) → „Offen" ist leer.
  - [ ] Namens-Kollisionscheck erfolgt (falls die Arbeit einen Produkt-/Plattformnamen setzt); Prüfer-Steuerungen aus `aufgabe.md` → „## Prüfer-Steuerungen" sind im Plan berücksichtigt.
  - [ ] Jeder Papiertyp-Pflichtpunkt aus `typen/<typ>.md` hat ein zuständiges Kapitel in `kapitelplan.md`.

  Ergebnis als PASS/FAIL-Liste im Chat, kein `pruefbericht.md` (zu kurzlebig für einen Snapshot). Bei FAIL: den fehlenden Schritt konkret benennen (z. B. „BBT-Key für Konkurrenzquelle X fehlt — Zotero-Export nachholen"), nicht nur „nicht bereit" melden.
- **Voll-Audit** („Audit"): alle Teil-Checks A–D + Score + `pruefbericht.md`, Teil-Check E informativ — der Ablauf unten. **Vorbedingung:** Ein Voll-Audit wird erst gefahren, wenn **Gegenlesung und Gesamt-Stresstest** gelaufen sind und `AENDERUNGEN.md` → „Offen" leer ist. **Ausnahme Kompakt-Prüfkette:** Bei Hausarbeit und Projektbericht genügt die abgearbeitete Gegenlesung — ein bewusst übersprungener Gesamt-Stresstest ist dort Default und wird im Bericht als „übersprungen (Kompakt-Kette)" vermerkt. Andernfalls melden und den fehlenden Schritt vorschlagen. Der Nutzer kann alles überstimmen — dann im Bericht vermerken.
- **Re-Audit nach Überarbeitung**: Delta statt Vollprüfung — nur die FAIL-Punkte aus dem letzten `pruefbericht.md` gezielt nachprüfen, dazu beide Skripte und Teil-Check D (Build ist billig und fängt Regressionen). Nicht alle Kapitel erneut lesen. Score aktualisieren, `pruefbericht.md` überschreiben.
- **Abgabe-Audit** (letzter Lauf vor der Einreichung): Voll-Audit + Teil-Check E als Abschluss-Hinweisliste. Teil-Check E fließt **nie** in den Score ein — die Verwaltungsschritte (myCampus) liegen außerhalb der Arbeit und würden einen textseitig fertigen Stand verzerren; sie stehen stattdessen als „Vor der Einreichung"-Hinweis am Ende des Berichts.
  **Sprachstichprobe (nur im Abgabe-Audit):** pro Hauptkapitel zwei Absätze ausschließlich auf Sprachfehler lesen — Rechtschreibung, Grammatik, Kommasetzung, Bezugsfehler, verwaiste Satzreste nach Umbauten — nicht auf Stil (den prüft Teil-Check A). Zielgruppe der Stichprobe sind Nutzer-Nachbearbeitungen; KI-generierter Text ist grammatisch meist sauber, von Hand eingefügte Halbsätze nicht. Mechanische Wortdopplungen findet bereits `check_formalia.py` (DOPPELWORT). Funde als Formalia-Hinweise; für die **flächige** Prüfung gehört „LanguageTool-Durchgang (lokal) über den Gesamttext" als Punkt in die „Vor der Einreichung"-Checkliste — das ist Nutzer-Schritt, kein Audit-Bestandteil.
- **Feedback-Destillat** („Feedback einarbeiten" — nach Rückgabe einer benoteten Arbeit oder substanziellem Tutor-Feedback): kein Audit der Arbeit, sondern die Lernschleife des Workflows — Benotungs-Feedback ist die wertvollste Korrekturquelle und geht ohne diesen Schritt verloren. Eigener, schlanker Ablauf, kein Score, kein `pruefbericht.md`:
  1. Feedback-Dokument (PDF/Text/Mail) vollständig lesen; jeden Kritik- **und** Lobpunkt einzeln erfassen.
  2. Je Punkt die betroffene Stelle in der Arbeit identifizieren und klassifizieren: Stil / Zitation / Struktur / Argumentation / Prozess.
  3. **Workflow-Ursache bestimmen**: Welcher Skill oder Check hätte den Punkt fangen müssen — und warum hat er nicht? (Regel fehlt · Regel zu schwach · Regel vorhanden, aber nicht angewendet.)
  4. Je Punkt einen `[LERNEN:kategorie]`-Eintrag schreiben — Default `PERSISTENT.md`, denn Benotungs-Feedback ist fast immer projektübergreifend; nur rein themenspezifische Punkte nach `MEMORY.md`. Auch bestätigtes Lob festhalten („so weitermachen: …") — die nächste Arbeit darf Stärken nicht wegschreiben.
  5. Zeigt Schritt 3 eine Regel-Lücke: konkrete Ergänzung für `hard-rules-formal.md`, `stilprofil.md`, `typen/<typ>.md` oder einen `check_formalia.py`-Check **vorschlagen** — dem Nutzer zur Freigabe vorlegen, nicht still einbauen.
  6. Sichtbar quittieren, welche Einträge geschrieben wurden.

**Plan-Audit-Ablauf (eigener, schlanker Ablauf — nicht der Ablauf unten):** `kapitelplan.md` vollständig lesen, `aufgabe.md` als Maßstab lesen. Kein `hard-rules-formal.md`, keine Skripte, keine Teil-Checks A–D, kein Score, kein `pruefbericht.md`. Die sechs Prüfpunkte oben durchgehen, Befunde als kurze Fundliste im Chat ausgeben (Format: `[Prüfpunkt] Fund — betroffene Stelle in kapitelplan.md — Empfehlung`). Bei Funden: dem Nutzer vorschlagen, vor `schreib-modus` in einer neuen `plan-modus`-Session nachzuschärfen — nicht selbst in `kapitelplan.md` schreiben (Prüfer/Autor trennen).

**Bereitschafts-Check-Ablauf (eigener, schlanker Ablauf — nicht der Ablauf unten):** `kapitelplan.md`, `aufgabe.md`, `AENDERUNGEN.md` (falls vorhanden) lesen. Kein `hard-rules-formal.md`, kein Teil-Check A–D, kein Score, kein `pruefbericht.md`. Nur `check_bib_keys.py` läuft (für den ersten Punkt); die übrigen vier Punkte sind Dateiabgleiche, keine Textbewertung. Ergebnis direkt im Chat als Checkliste, PASS/FAIL je Punkt — bei allen PASS: „Bereit für schreib-modus" quittieren.

## Ablauf (Orchestrierung)

**Gilt für Kapitel-/Voll-/Re-/Abgabe-Audit — nicht für Plan-Audit oder Bereitschafts-Check** (eigene Abläufe siehe oben).

1. **`PERSISTENT.md` + `MEMORY.md`** (falls vorhanden) lesen — `[LERNEN:...]`-Einträge können abweichende Audit-Kriterien oder Sonderfälle enthalten, die Vorrang vor den Standard-Checks haben (z. B. „Methodik-Kapitel entfällt auch empirisch"); bei Widerspruch gewinnt `MEMORY.md`. Im Bericht als Hinweis vermerken, nicht stillschweigend übergehen.
2. Papiertyp bestimmen → `.claude/skills/_shared/typen/<typ>.md` laden (Pflichtregeln, Bewertung, Audit-Checks, Outline-Check, Claim-Extraction). **`aufgabe.md`** (falls vorhanden) lesen — die dortigen wörtlichen Leitfragen sind Prüfmaßstab für den Outline-Check (beantwortet die Arbeit die gestellte Frage?). **Lese-Trigger Prüfer-Steuerungen**: Taucht bei einem Fund eine Frage zu Formalia/Anforderungen/Methodik auf, bevor er als FAIL gewertet wird `aufgabe.md` → „## Prüfer-Steuerungen" gegenprüfen — eine dort dokumentierte Steuerung kann die Standardregel für dieses Projekt außer Kraft setzen (siehe `CLAUDE.md` → „Erst prüfen, dann behaupten").
3. `.claude/skills/_shared/hard-rules-formal.md` laden — Grundlage für Teil-Check A (Zitationen, LaTeX, Pronomen, Struktur, Schreibstil, Verständlichkeit), bewusst nicht in `CLAUDE.md`. Für den Verständlichkeits-Prüfpunkt zusätzlich `.claude/skills/_shared/stilprofil.md` als Kalibrier-Referenz. Teil-Check B wertet nur die „Pflicht"-Punkte aus `typen/<typ>.md` als FAIL.
4. BBT-Keys deterministisch validieren (inkl. ungenutzter Einträge): `python .claude/skills/_shared/scripts/check_bib_keys.py references.bib --dir chapters/ --report-unused` (vom Projekt-Root aus).
5. Mechanische Formalia deterministisch prüfen: `python .claude/skills/_shared/scripts/check_formalia.py chapters/` — die Skript-Funde direkt in Teil-Check A übernehmen, diese Punkte **nicht** zusätzlich per Durchlesen prüfen (Tokenersparnis, keine False Negatives). **Bekannte False-Positive-Quelle**: PRONOMEN schlägt auch innerhalb wörtlicher Zitate an (`\enquote{…ich…}`, `blockzitat`-Umgebung), FLOAT meldet `\begin{figure}` fälschlich, wenn `[H]` erst in der Folgezeile steht. Solche Funde vor der Übernahme kurz im Kontext gegenprüfen, nicht blind als FEHLER werten.
6. **Teil-Check A — Formalia** ausführen (nur die nicht skript-prüfbaren Punkte lesen).
7. **Teil-Check B — Argumentationsqualität** ausführen (nur Matrix-Pflichtzeilen als FAIL).
8. **Teil-Check C — Struktur** ausführen (inkl. Outline-Check gegen bestätigtes Kapitelgerüst).
9. **Teil-Check D — Build** ausführen (siehe unten; überspringen und vermerken, falls lualatex/biber nicht verfügbar).
9b. **Teil-Check E — Abgabe** ausführen (immer informativ, nie Score-relevant — siehe unten).
10. Score berechnen (siehe „Score-Regel" unten).
11. Feedback-Bericht mit Score ausgeben **und als `pruefbericht.md` im Projekt-Root speichern** (bei jedem Audit überschreiben — der Bericht ist ein Snapshot, kein Verlauf; Datum + geprüfter Stand in die Kopfzeile). Ohne diese Datei sind die Handlungsempfehlungen beim nächsten Sessionstart verloren.
12. `CLAUDE.md` → „Aktueller Projektstatus" aktualisieren: Prüf-Audit-Zeile (Score + Datum) **und** betroffene Kapitel-Zeilen auf ÜBERARBEITUNG NÖTIG setzen (mit Kurzverweis „siehe pruefbericht.md"), sichtbar quittiert im Chat. Danach `python .claude/skills/_shared/scripts/check_status.py` — der deterministische Abgleich Tabelle ↔ Dateisystem gehört zu jedem Voll-/Abgabe-Audit; Funde in den Bericht übernehmen.
13. **Nach bestandenem Abgabe-Audit** (Score ≥ 80): Den Bericht und die Chat-Zusammenfassung mit dem „Vor der Einreichung"-Hinweis abschließen — alle noch offenen Teil-Check-E-Punkte + alle offenen `% UNVERIFIED:`-Marker mit Datei und Zeile als Nutzer-Checkliste, ohne Score-Wirkung. Zusätzlich `MEMORY.md` **Eintrag für Eintrag** mit dem Nutzer durchgehen und je Eintrag entscheiden: projektspezifisch (bleibt) oder projektübergreifend (wandert nach `PERSISTENT.md`). Nicht nur allgemein erinnern — die Datei bleibt sonst leer, während `MEMORY.md` das gesamte Gelernte enthält und mit dem Projekt endet.

**Audit und Überarbeitung trennen**: Nach dem Audit nicht in derselben Session mit dem Überarbeiten beginnen — der Kontext ist voll mit allen geprüften Kapiteln, und `pruefbericht.md` trägt alles Nötige (priorisierte Handlungsempfehlungen) in die nächste Session hinüber. Dem Nutzer stattdessen den Einstieg nennen: neue Session, „Schreib-Modus: Überarbeitung nach Prüfbericht" (laut Modellempfehlung, siehe `_shared/modell-empfehlung.md`, zudem günstiger: Audit Opus, Abarbeiten der Liste Sonnet).

---

## Teil-Check A: Formalia

**Skript-gedeckt** (Ergebnis aus `check_formalia.py` übernehmen, nicht erneut lesen): Pronomen · `\enquote{}` statt gerader Anführungszeichen · quote-Env statt `blockzitat` · Float `[H]` · Caption vor `\label{}` · `\underline` · `\include` in Kapiteln · `~\autoref` · Gedankenstrich-Häufung · **Blockzitat-Heuristik** (`\enquote{}` > 40 Wörter) · **½-Seiten-Heuristik** (Subsection-Datei < ~150 Wörter) · **Überschriften-Dopplung** (Subsection ≈ Section bzw. ≈ `\PaperTitle`) · **Satzlängen-Heuristik** (Sätze > 30 Wörter, Datei-Durchschnitt > 22) · **Meta-Verben-/Nominalstil-Marker** („entfaltet/bündelt/verortet", „erfolgt", „im Rahmen der" …) · **Dreier-Aufzählungs-Häufung** (TRIAS) · **Absatz-Gleichförmigkeit** (ABSATZ-UNIFORM) · **Fragesätze im Fließtext** (RHETFRAGE — die wörtlich formulierte Leitfrage/Forschungsfrage ist legitim, im Kontext gegenprüfen) · **Wortdopplungen** (DOPPELWORT — Tippfehler oder fehlendes Komma).

Manuell nur noch diese Punkte:

- [ ] Zitationen: `\parencite[S. X]{key}` bei stellenbezogenen Zitaten? Keys aus `references.bib`? — per `check_bib_keys.py` geprüft, nicht nur gelesen.
- [ ] Eigene Werke: `\quelle{Eigene Darstellung.}` unter Abb./Tab.? Kein `\cite{}` auf eigene Werke? Beschriftung über dem Bild?
- [ ] Diagramme mit den vordefinierten TikZ-Styles (`box`/`decision`/`arr`), nicht als externes Bild oder Ad-hoc-Styles?
- [ ] Akronyme: `\ac{}` verwendet, Definitionen in `pages/acronyms.tex`?
- [ ] Labels konsistent: `sec:`, `fig:`, `tab:`, `eq:`?
- [ ] Sekundärzitate korrekt und vermieden (nur bei nicht beschaffbarer Primärquelle)?
- [ ] Quellen-Sperrliste: keine Skripte/Vorlesungsfolien/Webinars zitiert?
- [ ] Keine Bequemlichkeits-Abkürzungen; geläufige Abkürzungen (z. B., u. a.) nicht im Abkürzungsverzeichnis?
- [ ] Keine Änderungen an `main.tex` / `pages/cover.tex`? Projektangaben nur in `pages/meta.tex`, Platzhalter dort ausgefüllt?
- [ ] Anti-KI-Stil (Vollversion in `hard-rules-formal.md` → Schreibstil): keine Floskel-Öffner, keine Klischee-Übergänge gehäuft? (Gedankenstrich-Zählung liefert das Skript.)
- [ ] Verständlichkeit (`hard-rules-formal.md` → Verständlichkeit): Sätze kurz und klar (ein Gedanke pro Satz), kein gehäufter Nominalstil oder gestelzte Meta-Verben, Fachbegriffe bei erster Nennung erklärt, keine stilistische Verdichtung? Maßstab: Ein Laie versteht jeden Absatz beim ersten Lesen.
- [ ] Offene `% UNVERIFIED:`-Marker (`grep -rn "UNVERIFIED" chapters/`) — jeder Treffer erscheint namentlich in der „Vor der Einreichung"-Checkliste. Kein Score-Abzug, aber niemals stillschweigend übergehen.
- [ ] **Quellenlose Kapitel:** Enthält ein Kapitel mit Recherche- oder Analysecharakter keine einzige Quellenangabe, prüfen, ob die Erhebungsgrundlage anderweitig dokumentiert ist (Anhang, Methodenabsatz mit Zeitraum und Zugängen). Fehlt beides, ist das ein Struktur-FAIL: Eigenleistung entbindet nicht von Nachvollziehbarkeit.

## Teil-Check B: Argumentationsqualität

Enger Fokus, nur „Pflicht"-Punkte aus `typen/<typ>.md` → Pflichtregeln als FAIL werten:

- [ ] These erkennbar? (Leitfrage ↔ These getrennt)
- [ ] Forschungslücke in der Einleitung benannt? — *nur wenn laut Typ-Datei „Pflicht"*
- [ ] Aktualität/Zeitbezug in der Einleitung? — *nur wenn laut Typ-Datei „Pflicht"*
- [ ] Pro zentralem Argument: stärkstes Gegenargument reflektiert und entkräftet? — bei Unsicherheit: `stresstest`-Skill auf das konkrete Argument anwenden statt selbst zu spekulieren.
- [ ] Syntheseleistung pro Hauptkapitel?
- [ ] Limitationen dreischichtig? (warum · Mitigation · zukünftige Forschung)
- [ ] Ergebnisse/Diskussion: Befunde zuerst (FACTUAL), Interpretation danach (ARGUMENTATION)? — *nur Seminararbeit, nur empirisch*
- [ ] Typspezifische Punkte aus `typen/<typ>.md` (Audit-Checks, Claim-Extraction)?
- [ ] Beantwortet die Arbeit die **wörtlichen Leitfragen aus `aufgabe.md`**? (falls Datei vorhanden)
- [ ] **Teilaufgaben-Abgleich:** Ist jede wörtliche Teilaufgabe aus `aufgabe.md` real ausgeführt? Wurde eine durch eine Simulation, Annahme oder ein Gedankenexperiment ersetzt, liegt dafür eine ausgeschriebene Begründung mit allen vier Angaben vor (Versuch, Hinderungsgrund, geprüfter Minimalersatz, Folgeschritt)? Fehlt die Begründung, ist das ein FAIL — unabhängig davon, wie sauber der hypothetische Charakter gekennzeichnet ist.
- [ ] Sind alle Einträge der **wörtlichen Abhakliste** aus `aufgabe.md` adressiert? Prüfung per Grep über `chapters/`, nicht aus dem Leseeindruck. Bei Berichtsinhalten zusätzlich: Gibt es einen zusammenhängenden Ort, oder ist der Inhalt nur über die Arbeit verstreut? Bei `[VERENGT]`-Begriffen: Steht die Begründung im Text?
- [ ] Sind alle in `aufgabe.md` → „Genannte Materialien" aufgeführten Quellen im Literaturverzeichnis vertreten oder ist ihr Fehlen begründet?
- [ ] **Dimensionsabgleich:** Jede Dimension jedes Bewertungskriteriums gegen die Zuordnungstabelle aus `kapitelplan.md` prüfen. Eine Dimension, die im Text nicht vorkommt, ist ein FAIL — auch wenn die übrigen Dimensionen desselben Kriteriums stark abgedeckt sind.

## Teil-Check C: Struktur

Enger Fokus, nur diese Punkte (½-Seiten-Regel und Überschriften-Dopplung liefert das Skript — Funde aus Teil-Check A übernehmen, nicht erneut lesen):

- [ ] Max. 2–3 Sätze zwischen Kapitel-Überschrift und erstem Unterkapitel?
- [ ] Maximal 3 Kapitelstufen?
- [ ] Inhaltsverzeichnis: nur 1. Ebene fett?
- [ ] Front-Matter: Titelblatt, Verzeichnisse, Literaturverzeichnis?
- [ ] Mindestens 2 Unterpunkte pro Kapitel (kein einzelnes 1.1 ohne 1.2)?
- [ ] Abbildungs-/Tabellenverzeichnis nur eingebunden, wenn ≥ 3 Abbildungen bzw. Tabellen?
- [ ] Anhänge: „Anhang A/B/…"-Kennzeichnung, mind. 1 Verweis pro Anhang im Text, Anhangsverzeichnis bei mehreren?
- [ ] Outline-Check gegen das in `typen/<typ>.md` hinterlegte Kapitelgerüst — identisch mit dem Skelett, das im Plan-Modus (Schritt 2.5) bestätigt wurde?

**Roter Faden (nur Voll- und Abgabe-Audit — kapitelübergreifend prüfen, nicht pro Kapitel; Funde zählen als Struktur-Verstoß in die Score-Regel):** Diese Punkte findet weder ein Skript noch der Build — der Build prüft nur, ob ein Label existiert, nicht, ob es auf die richtige Stelle zeigt.

**Doppelarbeit vermeiden:** Ist der Gesamt-Stresstest gelaufen (erkennbar an seiner Runde in `AENDERUNGEN.md`), hat er genau diese kapitelübergreifenden Dimensionen bereits mit vollem Kontext geprüft. Dann hier **nicht** alle Kapitel erneut querlesen, sondern: die Stresstest-Runde referenzieren, prüfen, ob deren einschlägige Punkte im Erledigt-Log abgearbeitet sind, und nur stichprobenartig auf Regressionen durch die Überarbeitung achten (geänderte Stellen gegen ihre Querverweise und Zählungen). Vollständig selbst geprüft wird dieser Block nur, wenn der Gesamt-Stresstest übersprungen wurde (Kompakt-Prüfkette bei Hausarbeit/Projektbericht) — das erspart dem teuersten Audit einen kompletten Lesedurchgang, ohne eine Prüfdimension zu verlieren.

- [ ] Querverweise **semantisch** korrekt: Steht an der Stelle, auf die ein `\autoref` zeigt, tatsächlich der behauptete Inhalt (z. B. „die in X offengebliebene Frage" — ist sie dort wirklich offen geblieben)?
- [ ] Zeitlinien-Konsistenz Entwurf ↔ Iteration: Was das Iterationskapitel als Ergebnis/Anpassung einführt, darf im Konzeptkapitel nicht bereits als Bestandteil des ursprünglichen Entwurfs stehen — und der gewählte Darstellungsstand (Vor-Iteration vs. final) muss für **alle** Anpassungen einheitlich sein, nicht nur für einige.
- [ ] Zentrale Begriffe der Leitfrage in Einleitung, Hauptteil-Überschriften (inkl. Inhaltsverzeichnis), Tabellen und Fazit identisch benannt?
- [ ] Zahlenangaben im Fließtext („sechs Kernfunktionen", „vier Kriterien") gegen die zugehörigen Tabellen/Aufzählungen tatsächlich nachgezählt?
- [ ] Tabellenwertungen mit den eigenen Kriteriendefinitionen vereinbar? Prüfung **spaltenweise, nicht zeilenweise**: Für jedes Kriterium alle Wertungen nebeneinanderlegen und fragen, ob sie auf **einer** Achse liegen (Rubrik-Karte heranziehen). Ein „mittel" ohne das definierende Merkmal neben einem „schwach" mit dem Merkmal ist ein Maßstabsbruch.
- [ ] Sind alle Kriterien derselben Art (Merkmal statt Gesamturteil), oder geht ein zusammenfassendes Urteil als gleichrangige Spalte ein?
- [ ] Erhält das Objekt, gegen das sich die These richtet, in allen Spalten die schlechtesten Werte — und wird dieser Anschein im Text entkräftet?
- [ ] **Lieferobjekt-Abgleich:** Jedes Objekt aus `aufgabe.md` → „Lieferobjekte" liegt in der Arbeit vor (per Verzeichnis- und Grep-Prüfung, nicht aus dem Leseeindruck). Zusätzlich: Enthält `pages/appendix.tex` außer Kommentaren tatsächlich Inhalt, falls Anhänge geplant waren? Gibt es mindestens eine visuelle Darstellung des Entworfenen, falls die Arbeit ein Produkt oder System konzipiert? Behauptet der Text irgendwo ein Artefakt, das nicht beiliegt (Grep über `chapters/` nach „Prototyp", „Formular", „Skizze", „Erhebung")?
- [ ] **Akteurskonsistenz:** Alle Rollen, Nutzergruppen und Zugangsregeln, die die Arbeit definiert, gegeneinander prüfen. Wer darf hinein, wer sieht was, wer handelt mit wem? Besonders auf Ausschließlichkeitsformulierungen achten („ausschließlich", „nur", „begrenzt auf") und dann kapitelübergreifend suchen, ob später Akteure auftreten, die diese Regel verletzen.
- [ ] **Offene Einwände:** Jeden Einwand, den die Arbeit **selbst** gegen ihre Position erhebt, verfolgen. Wird er beantwortet, entkräftet oder ausdrücklich als Limitation ausgewiesen? Ein Einwand, der zweimal genannt und nie beantwortet wird — besonders im Schlusssatz — ist die schwächste denkbare Stelle. Grep-Hilfe: „bleibt angewiesen", „hängt davon ab", „setzt voraus", „nur wenn".
- [ ] **Redundanz zwischen Reflexion und Fazit:** Erzählen beide dieselben Limitationen? Saubere Arbeitsteilung ist: Reflexion behandelt das **Vorgehen**, Fazit behandelt **Ergebnis und Grenzen**. Doppelungen sind zugleich die erste Kürzungsreserve, wenn der Umfang am Anschlag steht.

## Teil-Check D: Build

Deterministischer Kompilier-Check — Textprüfung allein findet keine kaputten Referenzen:

1. `latexmk -lualatex main.tex` vom Projekt-Root ausführen (nutzt `.latexmkrc`, Build-Artefakte landen in `build/`).
2. Log auswerten — **nie vollständig einlesen** (latexmk-Logs haben tausende Zeilen): gezielt greppen nach `^!`/`Error`, `undefined references`, `undefined citations`, `not found` (fehlende Bilder), `multiply defined` (doppelte Labels). Warnings vom Typ Over-/Underfull nur als Hinweis.
3. Seitenumfang aus dem PDF bestimmen: Textteil zählt ab „1 Einleitung" bis vor das Literaturverzeichnis (inkl. Abb./Tab.) — gegen die Umfangsvorgabe aus `aufgabe.md` bzw. `typen/<typ>.md` halten.
4. Falls lualatex/biber fehlt: Teil-Check D als ÜBERSPRUNGEN ausweisen, Nutzer auf lokalen Build hinweisen — nicht raten, ob es kompiliert.

## Teil-Check E: Abgabe (immer informativ — nie Score-relevant)

Alle vier IU-Prüfungsleitfäden: Abgabe ausschließlich über Turnitin im myCampus-Kurs — und die **Eidesstattliche Erklärung wird vorab elektronisch über myCampus abgegeben; vorher nimmt Turnitin die Einreichung gar nicht an.** Dieser Check verhindert, dass eine inhaltlich fertige Arbeit an einem Verwaltungsschritt scheitert.

- [ ] Eidesstattliche Erklärung elektronisch über myCampus abgegeben? (Status aus `CLAUDE.md` → Fristen)
- [ ] Anleitung zur Einreichung im myCampus-Kurs gelesen?
- [ ] Umfang im Soll (`typen/<typ>.md`; Fallstudie: 7–10 Seiten ohne Master-Variante)?
- [ ] Erinnerung: keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)?
- [ ] Erinnerung: LanguageTool-Durchgang (lokal) über den Gesamttext — die Sprachstichprobe des Abgabe-Audits ersetzt keine Vollprüfung (Sprache zählt in die Bewertung)?

Diese Punkte werden in **keinem** Audit-Umfang mit Score-Abzug bewertet (Nutzer-Festlegung 2026-07-19, siehe `MEMORY.md`): Sie betreffen Verwaltungsschritte außerhalb des Textes. Offene Punkte als `[OFFEN]` listen und am Ende des Berichts sowie der Chat-Zusammenfassung als „Vor der Einreichung"-Checkliste an den Nutzer wiederholen — das ist ihre einzige Konsequenz. Ausnahme: „Umfang im Soll" wird bereits in Teil-Check D score-relevant geprüft und hier nur gespiegelt.

---

## Score-Regel

Abzüge von 100 Punkten, nach Schweregrad — nicht additiv über beliebig viele Kleinigkeiten, sondern gedeckelt pro Kategorie (max. Abzug in Klammern):

| Fund | Abzug pro Vorkommen | Kategorie-Deckel |
|---|---|---|
| Erfundener/fehlender BBT-Key | −20 | −40 |
| Fehlender Pflicht-Punkt aus Typ-Datei (Teil-Check B) | −15 | −45 |
| Formalia-Verstoß (Teil-Check A, außer BBT-Keys) | −8 | −32 |
| Struktur-Verstoß (Teil-Check C) | −10 | −30 |
| Build schlägt fehl (Teil-Check D) | −20 | −20 |
| Undefined reference/citation, fehlendes Bild, doppeltes Label (Teil-Check D) | −5 | −15 |
| Seitenumfang außerhalb der Vorgabe (Teil-Check D) | −10 | −10 |
| Anti-KI-Stil-Verstoß, gehäuft (>3 Vorkommen in einem Kapitel; Skript-Funde GEDANKENSTRICH/TRIAS/RHETFRAGE/ABSATZ-UNIFORM zählen mit) | −5 | −10 |
| Verständlichkeits-Verstoß, gehäuft (>3 Vorkommen in einem Kapitel; Skript-Funde SATZLAENGE/SATZSCHNITT/META-VERB/NOMINALSTIL zählen mit) | −5 | −15 |

Teil-Check E fließt nicht in den Score ein — offene Abgabe-Punkte erscheinen ausschließlich als „Vor der Einreichung"-Hinweis (siehe Teil-Check E).

Ungenutzte Bib-Einträge fließen **nicht** in den Score ein — reiner Aufräumhinweis, kein Qualitätsproblem.

**Schwellenwerte**:
- **≥ 80/100** — abgabereif, verbleibende Punkte optional nachbessern.
- **60–79/100** — Überarbeitung empfohlen, mit `schreib-modus` gezielt an den Kritikpunkten arbeiten.
- **< 60/100** — nicht einreichen, mindestens einen weiteren Prüf-Schreib-Zyklus einplanen.

Score ist ein Hilfswert zur Priorisierung, keine Zusicherung; die inhaltliche Entscheidung "einreichen oder nicht" bleibt beim Nutzer.

---

## Feedback-Format

```markdown
# Prüfbericht — <Papiertyp>

**Datum**: <TT.MM.JJJJ> · **Geprüfter Stand**: <Kapitel <name> / alle Kapitel> · **Audit-Typ**: <Kapitel / Voll / Re-Audit / Abgabe>
**Score: <N>/100 — <abgabereif / Überarbeitung empfohlen / nicht einreichen>**

## Teil-Check A — Formalia
- [PASS / FAIL] Zitationen (inkl. Skript-Ergebnis)
- [PASS / FAIL] Eigene Werke
- [PASS / FAIL] Pronomen
- [PASS / FAIL] LaTeX-Format
- [PASS / FAIL] Akronyme
- [PASS / FAIL] Cross-References & Labels
- [PASS / FAIL] Anti-KI-Stil
- [PASS / FAIL] Verständlichkeit (einfache Sprache, Fachbegriffe erklärt)

## Teil-Check B — Argumentationsqualität (nur Pflicht-Punkte der Typ-Datei als FAIL)
- [PASS / FAIL] These erkennbar
- [PASS / FAIL / N.A.] Forschungslücke in Einleitung
- [PASS / FAIL / N.A.] Aktualität/Zeitbezug in Einleitung
- [PASS / FAIL] Gegenargumente reflektiert & entkräftet
- [PASS / FAIL] Syntheseleistung pro Hauptkapitel
- [PASS / FAIL] Limitationen dreischichtig
- [PASS / FAIL / N.A.] Ergebnisse ≠ Interpretation
- [PASS / FAIL] Typspezifisch (<Papiertyp>, aus typen/<typ>.md)
- [PASS / FAIL / N.A.] Leitfragen aus aufgabe.md beantwortet

## Teil-Check C — Struktur
- [PASS / FAIL] ½-Seiten-Regel
- [PASS / FAIL] Max. 3 Kapitelstufen
- [PASS / FAIL] Front-/Backmatter (Verzeichnisse ab 3, Anhang-Kennzeichnung & -Verweise)
- [PASS / FAIL] Outline-Check gegen bestätigtes Kapitelgerüst

## Teil-Check D — Build
- [PASS / FAIL / ÜBERSPRUNGEN] Kompiliert fehlerfrei (latexmk -lualatex)
- [PASS / FAIL / ÜBERSPRUNGEN] Keine undefined references/citations, fehlenden Bilder, doppelten Labels
- [PASS / FAIL / ÜBERSPRUNGEN] Seitenumfang Textteil innerhalb der Vorgabe (<gezählt> von <Vorgabe>)

## Teil-Check E — Abgabe (informativ, kein Score-Abzug)
- [PASS / OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [PASS / OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [PASS / FAIL] Umfang im Soll (Spiegel aus Teil-Check D)
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko)

## Claims
- Ungesicherte FACTUAL CLAIMS (inkl. Skript-Treffer „FEHLEND"): <Liste mit Stellen>
- Fehlende OWN WORK-Markierungen: <Liste>
- Ungenutzte Bib-Einträge (Aufräumhinweis, kein Score-Abzug): <Liste>

## Punkteabzug im Detail
- <Kategorie>: −<N> (<Anzahl> Vorkommen, gedeckelt bei −<Deckel>)

## Bewertungsschwerpunkte (<Papiertyp>)
- <Kriterium> (<Gewicht>): **je Dimension** [ABGEDECKT / SCHWACH / FEHLT] — <Fundstelle oder Lücke>

## Lieferobjekt-Abgleich
- [PASS / FAIL] Lieferobjekt-Abgleich (Artefakte, Anhang, Abbildungen)

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)
1. ...

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- <alle noch offenen Teil-Check-E-Punkte + offene Volltext-Verifikationen — dieser Block schließt jeden Bericht und jede Chat-Zusammenfassung ab>
```
