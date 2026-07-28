---
name: pruef-modus
description: Prüft eine wissenschaftliche Arbeit oder einen Kapitelplan an der IU gegen Formalia, Argumentationsqualität, Struktur und Abgabe-Voraussetzungen (Turnitin, Eidesstattliche Erklärung) vor der Abgabe, mit numerischem Score und Abgabe-Schwelle. Nutzen, wenn ein Entwurf, ein fertiges Kapitel oder ein kapitelplan.md vorliegt und ein Audit gewünscht ist – oder wenn benotetes Tutor-Feedback in Lernpunkte übersetzt werden soll („Feedback einarbeiten", Umfang Feedback-Destillat). Prüft nur die für den jeweiligen Papiertyp laut Typ-Datei pflichtigen Kriterien, nicht pauschal alle. Dies ist der einzige Einstiegspunkt für Audits – führt intern die Teil-Checks A–G nacheinander aus (inklusive Volltextabgleich aller Zitationen), statt sich auf separat aufgerufene Skills zu verlassen.
compatibility: .claude/skills/_shared/scripts/check_bib_keys.py benötigt Python 3 und Zugriff auf references.bib. Teil-Check D (Build) benötigt lualatex + biber; falls nicht verfügbar, wird er übersprungen und im Bericht vermerkt.
---

# Prüf-Modus: Audit und Review

**Wichtig zur Nutzung**: Dieser Skill ist der alleinige Einstiegspunkt für Audits – nicht mehrere separate Skills. Die Teil-Checks laufen automatisch nacheinander innerhalb dieses einen Aufrufs, mit jeweils engem Fokus statt einer vermischten Gesamtliste. Nur bei einer gezielten Einzelanfrage („prüf nur die Zitate") wird ausschließlich der passende Teil-Check ausgeführt.

## Audit-Umfänge (zuerst bestimmen, welcher gemeint ist)

| Umfang | Auslöser | Kurzcharakter |
|---|---|---|
| **Kapitel-Audit** | „Audit Kapitel: <name>" (nach dem ersten Hauptteil-Kapitel empfohlen) | Teil-Check A + B auf dieses eine Kapitel, beide Skripte, **kein Score** |
| **Plan-Audit** | „Plan-Audit", sobald `kapitelplan.md` final ist – **Pflicht** ab 3 Kapiteln oder eigener Vergleichsmatrix | nur `kapitelplan.md` gegen `aufgabe.md`, kein Score, **eigener Ablauf** |
| **Bereitschafts-Check** | „Bereitschafts-Check" vor dem ersten `schreib-modus` | rein mechanische PASS/FAIL-Liste, kein Score, **eigener Ablauf** |
| **Voll-Audit** | „Audit" | Teil-Checks A–D + Score + `pruefbericht.md`, E informativ. **Vorbedingung:** Gegenlesung und Gesamt-Stresstest gelaufen, „Offen" leer (Ausnahme Kompakt-Kette bei Hausarbeit/Projektbericht: Gegenlesung genügt) |
| **Re-Audit** | nach einer Überarbeitung | Delta: nur die FAIL-Punkte des letzten Berichts + Build, nicht alles neu lesen |
| **Abgabe-Audit** | letzter Lauf vor der Einreichung | Voll-Audit + Teil-Check E als Hinweisliste (nie score-relevant) + Sprach- und Quellentreue-Stichprobe |
| **Feedback-Destillat** | „Feedback einarbeiten" | kein Audit: benotetes Feedback → `[LERNEN:…]`-Einträge, **eigener Ablauf** |

**Sobald der Umfang feststeht, `references/umfaenge.md` laden** – dort stehen je Umfang die Prüfpunkte, Vorbedingungen und die eigenen Abläufe von Plan-Audit, Bereitschafts-Check und Feedback-Destillat sowie die beiden Stichproben des Abgabe-Audits. Die Tabelle oben reicht zur Zuordnung, **nicht zur Durchführung**.

## Ablauf (Orchestrierung)

**Gilt für Kapitel-/Voll-/Re-/Abgabe-Audit – nicht für Plan-Audit oder Bereitschafts-Check** (eigene Abläufe siehe oben).

1. **`PERSISTENT.md` + `MEMORY.md`** (falls vorhanden) lesen – `[LERNEN:...]`-Einträge können abweichende Audit-Kriterien oder Sonderfälle enthalten, die Vorrang vor den Standard-Checks haben (z. B. „Methodik-Kapitel entfällt auch empirisch"); bei Widerspruch gewinnt `MEMORY.md`. Im Bericht als Hinweis vermerken, nicht stillschweigend übergehen.
2. Papiertyp bestimmen → `.claude/skills/_shared/typen/<typ>.md` laden (Pflichtregeln, Bewertung, Audit-Checks, Outline-Check, Claim-Extraction). **`aufgabe.md`** (falls vorhanden) lesen – die dortigen wörtlichen Leitfragen sind Prüfmaßstab für den Outline-Check (beantwortet die Arbeit die gestellte Frage?). **Lese-Trigger Prüfer-Steuerungen**: Taucht bei einem Fund eine Frage zu Formalia/Anforderungen/Methodik auf, bevor er als FAIL gewertet wird `aufgabe.md` → „## Prüfer-Steuerungen" gegenprüfen – eine dort dokumentierte Steuerung kann die Standardregel für dieses Projekt außer Kraft setzen (siehe `CLAUDE.md` → „Erst prüfen, dann behaupten").
3. `.claude/skills/_shared/hard-rules-formal.md` laden – Grundlage für Teil-Check A (Zitationen, LaTeX, Pronomen, Struktur, Schreibstil, Verständlichkeit), bewusst nicht in `CLAUDE.md`. Für den Verständlichkeits-Prüfpunkt zusätzlich `.claude/skills/_shared/stilprofil.md` als Kalibrier-Referenz. Teil-Check B wertet nur die „Pflicht"-Punkte aus `typen/<typ>.md` als FAIL.
4. **Alle mechanischen Prüfungen in einem Lauf**: `python .claude/skills/_shared/scripts/check_all.py --mit-quellen` (vom Projekt-Root aus). Er fährt nacheinander `check_bib_keys.py` (inkl. ungenutzter Einträge), `check_formalia.py chapters/ pages/`, `check_bib_hygiene.py`, `check_status.py` und `check_quellentreue.py` (Teil-Check G) und gibt pro Skript höchstens 40 Zeilen aus; bei mehr Funden das betroffene Skript einzeln nachfahren. Ohne `--mit-quellen` bleibt der Volltextabgleich aus – im Audit ist er Pflicht.
5. `check_formalia.py` läuft dabei über **beide Verzeichnisse**, denn `pages/appendix.tex` und `pages/acronyms.tex` sind selbst geschriebener Text und gehen in die Bewertung ein. Die reinen Gerüstdateien (`cover.tex`, `meta.tex`, `chapters.tex`, `gender.tex`) überspringt das Skript von sich aus und weist das in der Ausgabe aus. Nur beim Lauf über den **gesamten** Kapitelbestand greifen zusätzlich die dateiübergreifenden Checks – Abbildungs-/Tabellenverzeichnis ab drei, Anhangsverzeichnis ab zwei Anhängen, Textverweis je Anhang (AKTIVIERUNG, ANHANG-VERWEIS); beim Kapitel-Audit fehlen sie bewusst, weil sie dort falsch rechnen würden. Die Skript-Funde direkt in Teil-Check A übernehmen, diese Punkte **nicht** zusätzlich per Durchlesen prüfen (Tokenersparnis, keine False Negatives). Neu gegenüber früher und deshalb nicht mehr manuell zu prüfen: **fehlende Stellenangabe** (SEITENANGABE – nur werkbezogene Paraphrasen dürfen ohne, im Kontext gegenprüfen), **Float ohne Quellenzeile** (QUELLE-FEHLT), **Kapitel mit genau einem Unterpunkt** (UNTERPUNKTE), **`\cite` außerhalb von Quellenzeile und Sekundärzitat** (CITE). **Zitierter Fremdtext ist von den Stilprüfungen ausgenommen** (Inhalt von `\enquote{}` und der ganzen `blockzitat`-Umgebung): Ein „ich" im wörtlichen Zitat ist die Formulierung der Quelle, nicht die des Verfassers. Ebenso akzeptiert die Float-Prüfung `[H]` in der Folgezeile. Beide früheren Fehlalarm-Quellen liegen im Skript, nicht mehr beim Gegenprüfen – Funde deshalb direkt übernehmen.
6. **Teil-Check A – Formalia** ausführen (nur die nicht skript-prüfbaren Punkte lesen).
7. **Teil-Check B – Argumentationsqualität** ausführen (nur Matrix-Pflichtzeilen als FAIL).
8. **Teil-Check C – Struktur** ausführen (inkl. Outline-Check gegen bestätigtes Kapitelgerüst).
9. **Teil-Check D – Build** ausführen (siehe unten; überspringen und vermerken, falls lualatex/biber nicht verfügbar).
9b. **Teil-Check E – Abgabe** ausführen (immer informativ, nie Score-relevant – siehe unten).
9d. **Teil-Check G – Quellentreue** ausführen: `python .claude/skills/_shared/scripts/check_quellentreue.py` (im Kapitel-Audit mit `--datei chapters/<kap>`), Befunde übernehmen, offene `PRÜFEN`-Paare semantisch entscheiden – läuft in **jedem** Audit.
9c. **Teil-Check F – Literaturverzeichnis** ausführen (nur Voll-/Abgabe-Audit – siehe unten; Befunde als Zotero-Arbeitsliste, nie in `references.bib`).
10. Score berechnen (siehe „Score-Regel" unten).
11. Feedback-Bericht mit Score ausgeben **und als `pruefbericht.md` im Projekt-Root speichern** (bei jedem Audit überschreiben – der Bericht ist ein Snapshot, kein Verlauf; Datum + geprüfter Stand in die Kopfzeile). Ohne diese Datei sind die Handlungsempfehlungen beim nächsten Sessionstart verloren.
12. `CLAUDE.md` → „Aktueller Projektstatus" aktualisieren: Prüf-Audit-Zeile (Score + Datum) **und** betroffene Kapitel-Zeilen auf ÜBERARBEITUNG NÖTIG setzen (mit Kurzverweis „siehe pruefbericht.md"), sichtbar quittiert im Chat. Danach `python .claude/skills/_shared/scripts/check_status.py` – der deterministische Abgleich Tabelle ↔ Dateisystem gehört zu jedem Voll-/Abgabe-Audit; Funde in den Bericht übernehmen.
13. **Nach bestandenem Abgabe-Audit** (Score ≥ 80): Den Bericht und die Chat-Zusammenfassung mit dem „Vor der Einreichung"-Hinweis abschließen – alle noch offenen Teil-Check-E-Punkte + alle offenen `% UNVERIFIED:`-Marker mit Datei und Zeile als Nutzer-Checkliste, ohne Score-Wirkung. Zusätzlich `MEMORY.md` **Eintrag für Eintrag** mit dem Nutzer durchgehen und je Eintrag entscheiden: projektspezifisch (bleibt) oder projektübergreifend (wandert nach `PERSISTENT.md`). Nicht nur allgemein erinnern – die Datei bleibt sonst leer, während `MEMORY.md` das gesamte Gelernte enthält und mit dem Projekt endet.

**Audit und Überarbeitung trennen**: Nach dem Audit nicht in derselben Session mit dem Überarbeiten beginnen – der Kontext ist voll mit allen geprüften Kapiteln, und `pruefbericht.md` trägt alles Nötige (priorisierte Handlungsempfehlungen) in die nächste Session hinüber. Dem Nutzer stattdessen den Einstieg nennen: neue Session, „Schreib-Modus: Überarbeitung nach Prüfbericht" (laut Modellempfehlung, siehe `_shared/modell-empfehlung.md`, zudem günstiger: Audit Opus, Abarbeiten der Liste Sonnet).

---

## Teil-Check A: Formalia

**Skript-gedeckt** (Ergebnis aus `check_formalia.py` übernehmen, nicht erneut lesen): Pronomen · `\enquote{}` statt gerader Anführungszeichen · quote-Env statt `blockzitat` · Float `[H]` · Caption vor `\label{}` · `\underline` · `\include` in Kapiteln · `~\autoref` · Gedankenstrich-Häufung · **Blockzitat-Heuristik** (`\enquote{}` > 40 Wörter) · **½-Seiten-Heuristik** (Subsection-Datei < ~150 Wörter) · **Überschriften-Dopplung** (Subsection ≈ Section bzw. ≈ `\PaperTitle`) · **Satzlängen-Heuristik** (Sätze > 30 Wörter, Datei-Durchschnitt > 22) · **Meta-Verben-/Nominalstil-Marker** („entfaltet/bündelt/verortet", „erfolgt", „im Rahmen der" …) · **Dreier-Aufzählungs-Häufung** (TRIAS) · **Absatz-Gleichförmigkeit** (ABSATZ-UNIFORM) · **Fragesätze im Fließtext** (RHETFRAGE – die wörtlich formulierte Leitfrage/Forschungsfrage ist legitim, im Kontext gegenprüfen) · **Wortdopplungen** (DOPPELWORT – Tippfehler oder fehlendes Komma) · **offene Arbeitsmarker** (TODO-QUELLE, UNVERIFIED).

Manuell nur noch diese Punkte:

- [ ] Zitationen: `\parencite[S. X]{key}` bei stellenbezogenen Zitaten? Keys aus `references.bib`? – per `check_bib_keys.py` geprüft, nicht nur gelesen.
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
- [ ] Offene Arbeitsmarker? `check_formalia.py` meldet beide Sorten (TODO-QUELLE, UNVERIFIED) mit Datei und Zeile – Funde übernehmen, nicht erneut greppen. **`% TODO-QUELLE:` ist der schwerere Fall**: Dort fehlt eine Quelle, die Stelle ist also unbelegt; im Abgabe-Audit zählt jeder Treffer als fehlender BBT-Key (−20, Deckel −40). `% UNVERIFIED:` kostet keinen Score-Abzug, erscheint aber namentlich in der „Vor der Einreichung"-Checkliste – niemals stillschweigend übergehen.
- [ ] **Quellenlose Kapitel:** Enthält ein Kapitel mit Recherche- oder Analysecharakter keine einzige Quellenangabe, prüfen, ob die Erhebungsgrundlage anderweitig dokumentiert ist (Anhang, Methodenabsatz mit Zeitraum und Zugängen). Fehlt beides, ist das ein Struktur-FAIL: Eigenleistung entbindet nicht von Nachvollziehbarkeit.

## Teil-Check B: Argumentationsqualität

Enger Fokus, nur „Pflicht"-Punkte aus `typen/<typ>.md` → Pflichtregeln als FAIL werten:

- [ ] These erkennbar? (Leitfrage ↔ These getrennt)
- [ ] Forschungslücke in der Einleitung benannt? – *nur wenn laut Typ-Datei „Pflicht"*
- [ ] Aktualität/Zeitbezug in der Einleitung? – *nur wenn laut Typ-Datei „Pflicht"*
- [ ] Pro zentralem Argument: stärkstes Gegenargument reflektiert und entkräftet? – bei Unsicherheit: `stresstest`-Skill auf das konkrete Argument anwenden statt selbst zu spekulieren.
- [ ] Syntheseleistung pro Hauptkapitel?
- [ ] Limitationen dreischichtig? (warum · Mitigation · zukünftige Forschung)
- [ ] Ergebnisse/Diskussion: Befunde zuerst (FACTUAL), Interpretation danach (ARGUMENTATION)? – *nur Seminararbeit, nur empirisch*
- [ ] Typspezifische Punkte aus `typen/<typ>.md` (Audit-Checks, Claim-Extraction)?
- [ ] Beantwortet die Arbeit die **wörtlichen Leitfragen aus `aufgabe.md`**? (falls Datei vorhanden)
- [ ] **Teilaufgaben-Abgleich:** Ist jede wörtliche Teilaufgabe aus `aufgabe.md` real ausgeführt? Wurde eine durch eine Simulation, Annahme oder ein Gedankenexperiment ersetzt, liegt dafür eine ausgeschriebene Begründung mit allen vier Angaben vor (Versuch, Hinderungsgrund, geprüfter Minimalersatz, Folgeschritt)? Fehlt die Begründung, ist das ein FAIL – unabhängig davon, wie sauber der hypothetische Charakter gekennzeichnet ist.
- [ ] Sind alle Einträge der **wörtlichen Abhakliste** aus `aufgabe.md` adressiert? Prüfung per Grep über `chapters/`, nicht aus dem Leseeindruck. Bei Berichtsinhalten zusätzlich: Gibt es einen zusammenhängenden Ort, oder ist der Inhalt nur über die Arbeit verstreut? Bei `[VERENGT]`-Begriffen: Steht die Begründung im Text?
- [ ] Sind alle in `aufgabe.md` → „Genannte Materialien" aufgeführten Quellen im Literaturverzeichnis vertreten oder ist ihr Fehlen begründet?
- [ ] **Dimensionsabgleich:** Jede Dimension jedes Bewertungskriteriums gegen die Zuordnungstabelle aus `kapitelplan.md` prüfen. Eine Dimension, die im Text nicht vorkommt, ist ein FAIL – auch wenn die übrigen Dimensionen desselben Kriteriums stark abgedeckt sind.

## Teil-Check C: Struktur

Enger Fokus, nur diese Punkte (½-Seiten-Regel und Überschriften-Dopplung liefert das Skript – Funde aus Teil-Check A übernehmen, nicht erneut lesen):

- [ ] Max. 2–3 Sätze zwischen Kapitel-Überschrift und erstem Unterkapitel?
- [ ] Maximal 3 Kapitelstufen?
- [ ] Inhaltsverzeichnis: nur 1. Ebene fett?
- [ ] Front-Matter: Titelblatt, Verzeichnisse, Literaturverzeichnis?
- [ ] Mindestens 2 Unterpunkte pro Kapitel (kein einzelnes 1.1 ohne 1.2)?
- [ ] Abbildungs-/Tabellenverzeichnis nur eingebunden, wenn ≥ 3 Abbildungen bzw. Tabellen?
- [ ] Anhänge: „Anhang A/B/…"-Kennzeichnung, mind. 1 Verweis pro Anhang im Text, Anhangsverzeichnis bei mehreren?
- [ ] Outline-Check gegen das in `typen/<typ>.md` hinterlegte Kapitelgerüst – identisch mit dem Skelett, das im Plan-Modus (Schritt 2.5) bestätigt wurde?

**Roter Faden (nur Voll- und Abgabe-Audit – kapitelübergreifend prüfen, nicht pro Kapitel; Funde zählen als Struktur-Verstoß in die Score-Regel):** Diese Punkte findet weder ein Skript noch der Build – der Build prüft nur, ob ein Label existiert, nicht, ob es auf die richtige Stelle zeigt.

**Doppelarbeit vermeiden:** Ist der Gesamt-Stresstest gelaufen (erkennbar an seiner Runde in `AENDERUNGEN.md`), hat er genau diese kapitelübergreifenden Dimensionen bereits mit vollem Kontext geprüft. Dann hier **nicht** alle Kapitel erneut querlesen, sondern: die Stresstest-Runde referenzieren, prüfen, ob deren einschlägige Punkte im Erledigt-Log abgearbeitet sind, und nur stichprobenartig auf Regressionen durch die Überarbeitung achten (geänderte Stellen gegen ihre Querverweise und Zählungen). Vollständig selbst geprüft wird dieser Block nur, wenn der Gesamt-Stresstest übersprungen wurde (Kompakt-Prüfkette bei Hausarbeit/Projektbericht) – das erspart dem teuersten Audit einen kompletten Lesedurchgang, ohne eine Prüfdimension zu verlieren.

- [ ] Querverweise **semantisch** korrekt: Steht an der Stelle, auf die ein `\autoref` zeigt, tatsächlich der behauptete Inhalt (z. B. „die in X offengebliebene Frage" – ist sie dort wirklich offen geblieben)?
- [ ] Zeitlinien-Konsistenz Entwurf ↔ Iteration: Was das Iterationskapitel als Ergebnis/Anpassung einführt, darf im Konzeptkapitel nicht bereits als Bestandteil des ursprünglichen Entwurfs stehen – und der gewählte Darstellungsstand (Vor-Iteration vs. final) muss für **alle** Anpassungen einheitlich sein, nicht nur für einige.
- [ ] Zentrale Begriffe der Leitfrage in Einleitung, Hauptteil-Überschriften (inkl. Inhaltsverzeichnis), Tabellen und Fazit identisch benannt?
- [ ] Zahlenangaben im Fließtext („sechs Kernfunktionen", „vier Kriterien") gegen die zugehörigen Tabellen/Aufzählungen tatsächlich nachgezählt?
- [ ] Tabellenwertungen mit den eigenen Kriteriendefinitionen vereinbar? Prüfung **spaltenweise, nicht zeilenweise**: Für jedes Kriterium alle Wertungen nebeneinanderlegen und fragen, ob sie auf **einer** Achse liegen (Rubrik-Karte heranziehen). Ein „mittel" ohne das definierende Merkmal neben einem „schwach" mit dem Merkmal ist ein Maßstabsbruch.
- [ ] Sind alle Kriterien derselben Art (Merkmal statt Gesamturteil), oder geht ein zusammenfassendes Urteil als gleichrangige Spalte ein?
- [ ] Erhält das Objekt, gegen das sich die These richtet, in allen Spalten die schlechtesten Werte – und wird dieser Anschein im Text entkräftet?
- [ ] **Lieferobjekt-Abgleich:** Jedes Objekt aus `aufgabe.md` → „Lieferobjekte" liegt in der Arbeit vor (per Verzeichnis- und Grep-Prüfung, nicht aus dem Leseeindruck). Zusätzlich: Enthält `pages/appendix.tex` außer Kommentaren tatsächlich Inhalt, falls Anhänge geplant waren? Gibt es mindestens eine visuelle Darstellung des Entworfenen, falls die Arbeit ein Produkt oder System konzipiert? Behauptet der Text irgendwo ein Artefakt, das nicht beiliegt (Grep über `chapters/` nach „Prototyp", „Formular", „Skizze", „Erhebung")?
- [ ] **Akteurskonsistenz:** Alle Rollen, Nutzergruppen und Zugangsregeln, die die Arbeit definiert, gegeneinander prüfen. Wer darf hinein, wer sieht was, wer handelt mit wem? Besonders auf Ausschließlichkeitsformulierungen achten („ausschließlich", „nur", „begrenzt auf") und dann kapitelübergreifend suchen, ob später Akteure auftreten, die diese Regel verletzen.
- [ ] **Offene Einwände:** Jeden Einwand, den die Arbeit **selbst** gegen ihre Position erhebt, verfolgen. Wird er beantwortet, entkräftet oder ausdrücklich als Limitation ausgewiesen? Ein Einwand, der zweimal genannt und nie beantwortet wird – besonders im Schlusssatz – ist die schwächste denkbare Stelle. Grep-Hilfe: „bleibt angewiesen", „hängt davon ab", „setzt voraus", „nur wenn".
- [ ] **Redundanz zwischen Reflexion und Fazit:** Erzählen beide dieselben Limitationen? Saubere Arbeitsteilung ist: Reflexion behandelt das **Vorgehen**, Fazit behandelt **Ergebnis und Grenzen**. Doppelungen sind zugleich die erste Kürzungsreserve, wenn der Umfang am Anschlag steht.

## Teil-Check D: Build

Deterministischer Kompilier-Check – Textprüfung allein findet keine kaputten Referenzen:

1. `latexmk -lualatex main.tex` vom Projekt-Root ausführen (nutzt `.latexmkrc`, Build-Artefakte landen in `build/`).
   **Scheitert der Aufruf mit „MiKTeX could not find the script engine 'perl'" (oder einer anderen latexmk-Startmeldung), ist das kein Build-Fehler** – `latexmk` ist ein Perl-Skript und unter MiKTeX ohne Perl-Installation nicht lauffähig. Dann **nicht** abbrechen und Teil-Check D auch nicht überspringen, sondern die Kette von Hand fahren, die latexmk sonst automatisiert:

   ```
   lualatex -interaction=nonstopmode -output-directory=build main.tex
   biber --output-directory=build main
   lualatex -interaction=nonstopmode -output-directory=build main.tex
   lualatex -interaction=nonstopmode -output-directory=build main.tex
   ```

   Drei LuaLaTeX-Läufe, dazwischen Biber: Der zweite Lauf löst die Zitate auf, der dritte die Verweise und Verzeichnisse. Im Bericht als „Build über direkten Aufruf (latexmk ohne Perl nicht lauffähig)" vermerken. Dauerhafte Abhilfe für den Nutzer: Strawberry Perl installieren oder auf TeX Live wechseln (bringt Perl mit).
2. Log auswerten – **nie vollständig einlesen** (latexmk-Logs haben tausende Zeilen): gezielt greppen nach `^!`/`Error`, `undefined references`, `undefined citations`, `not found` (fehlende Bilder), `multiply defined` (doppelte Labels). Zusätzlich `Overfull \hbox` greppen: Überstände über ~5 pt (≈ 2 mm) in Tabellen/Anhang als benannten Fund mit Stelle listen – sichtbarer Randüberstand ist ein Formfehler (Lernpunkt Anhang-A-Datumsspalte, ISSE01 24.07.2026); kleinere Over-/Underfull nur als Hinweis.
3. Seitenumfang aus dem PDF bestimmen: Textteil zählt ab „1 Einleitung" bis vor das Literaturverzeichnis (inkl. Abb./Tab.) – gegen die Umfangsvorgabe aus `aufgabe.md` bzw. `typen/<typ>.md` halten.
4. Falls lualatex/biber fehlt: Teil-Check D als ÜBERSPRUNGEN ausweisen, Nutzer auf lokalen Build hinweisen – nicht raten, ob es kompiliert.

## Teil-Check E: Abgabe (immer informativ – nie Score-relevant)

Alle vier IU-Prüfungsleitfäden: Abgabe ausschließlich über Turnitin im myCampus-Kurs – und die **Eidesstattliche Erklärung wird vorab elektronisch über myCampus abgegeben; vorher nimmt Turnitin die Einreichung gar nicht an.** Dieser Check verhindert, dass eine inhaltlich fertige Arbeit an einem Verwaltungsschritt scheitert.

- [ ] Eidesstattliche Erklärung elektronisch über myCampus abgegeben? (Status aus `CLAUDE.md` → Fristen)
- [ ] Anleitung zur Einreichung im myCampus-Kurs gelesen?
- [ ] Umfang im Soll (`typen/<typ>.md`; Fallstudie: 7–10 Seiten ohne Master-Variante)?
- [ ] Erinnerung: keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko)?
- [ ] Erinnerung: LanguageTool-Durchgang (lokal) über den Gesamttext – die Sprachstichprobe des Abgabe-Audits ersetzt keine Vollprüfung (Sprache zählt in die Bewertung)?

Diese Punkte werden in **keinem** Audit-Umfang mit Score-Abzug bewertet (Nutzer-Festlegung 2026-07-19): Sie betreffen Verwaltungsschritte außerhalb des Textes. **Achtung, in der Bachelor-Vorlage gilt das Gegenteil** – dort sind Abstract und Eidesstattliche Erklärung Dokumentbestandteile und Teil-Check E ist im Abgabe-Audit score-relevant; die Regel hier ist deshalb bewusst templategebunden und steht nicht in `PERSISTENT.md`. Offene Punkte als `[OFFEN]` listen und am Ende des Berichts sowie der Chat-Zusammenfassung als „Vor der Einreichung"-Checkliste an den Nutzer wiederholen – das ist ihre einzige Konsequenz. Ausnahme: „Umfang im Soll" wird bereits in Teil-Check D score-relevant geprüft und hier nur gespiegelt.

## Teil-Check F: Literaturverzeichnis (nur Voll-/Abgabe-Audit)

Lernpunkt aus der externen Prüfung ISSE01 (24.07.2026): Neun Verzeichnis-Befunde, weil kein interner Check das Literaturverzeichnis je angesehen hatte – „references.bib nie manuell editieren" darf nicht zu „nie prüfen" werden. Alle Korrekturen laufen über Zotero + BBT-Re-Export; danach kompilieren und Delta-Re-Audit.

1. Deterministisch: `python .claude/skills/_shared/scripts/check_bib_hygiene.py` – Feld-Hygiene (gerade Anführungszeichen ↔ babel-Shorthands, Verlagsorte, Reihentitel, Voll-/Bereichsdaten, abgekürzte Institutionen, Title-Case-Verdacht, Artikelnummern als Seitenzahl, Gesetzes-Einträge, urldate/DOI/URL).
2. Das **gerenderte** Verzeichnis lesen (PDF-Literaturverzeichnis bzw. `build/main.bbl`) gegen `_shared/literaturverzeichnis.md` (jetzt laden) – das Skript sieht nur die Felder, nicht das Renderergebnis (kaputte Sonderzeichen wie „SSecurityänd", Sentence Case im Ergebnis, Alphabetik, APA-Disambiguierung).
3. Stichprobe: 3–5 Einträge Feld für Feld gegen das Deckblatt des Volltexts (Zotero-Importe übernehmen Datenbank-Fehler, z. B. „Conference" statt „Symposium" oder eine falsche Artikelnummer; die PDF-Pfade stehen im `file`-Feld der `references.bib`).
4. Befunde als **Zotero-Arbeitsliste** je Eintrag ausgeben (Feld → neuer Wert) – nie `references.bib` direkt ändern.

---

## Teil-Check G: Quellentreue (Volltextabgleich – in jedem Audit)

Prüft für **jede** Zitation, nicht für eine Stichprobe: Steht die Aussage auf der zitierten Seite? Ist sie paraphrasiert statt abgeschrieben? Stimmt die Seitenangabe? Grundlage ist immer der Volltext der Quelle (PDF aus dem `file`-Feld, ersatzweise die URL) – nie das Gedächtnis und nie der Titel des Werks.

1. **Deterministisch zuerst:**
   `python .claude/skills/_shared/scripts/check_quellentreue.py`
   Das Skript ordnet jeder Zitation den Volltext zu, rechnet die gedruckte Seitenzahl auf die PDF-Seite um, vergleicht Trägersatz und Seitentext und schreibt `quellencheck.md`. Läufe sind **inkrementell** – bereits mit OK quittierte Zitationen werden nur mit `--alle` erneut geprüft; genau das macht die Vollprüfung bei jedem Audit bezahlbar.
2. **Befunde des Skripts** (kein Modellurteil nötig, direkt in den Bericht übernehmen):
   - `WORTLAUT` – sieben oder mehr Wörter am Stück aus der Quelle, ohne Kennzeichnung als Zitat. Auflage: umformulieren **oder** als `\enquote{}` mit Seitenangabe kennzeichnen.
   - `ZITAT WEICHT AB` – ein als wörtlich gekennzeichnetes Zitat steht so nicht in der Quelle.
   - `SEITE VERDÄCHTIG` – kein Kernbegriff des Trägersatzes auf der zitierten Seite; das Skript nennt die wahrscheinlich gemeinte Seite.
   - `NICHT GEFUNDEN` – Key fehlt in `references.bib`.
3. **Semantischer Teil (mein Urteil, nicht delegierbar):** Zitationen mit Status `PRÜFEN` blockweise abrufen (`--paare 8`, nicht alle auf einmal – Kontext) und je Paar entscheiden. Der Quellentext kommt als Ausschnitt um die Kernbegriffe und ist als gekürzt markiert; reicht er nicht, `--paare N --voll` oder `--seite <key> <n>` nachladen – ein OK auf zu dünnem Ausschnitt ist schlimmer als ein zweiter Aufruf. Zu entscheiden ist: Deckt die Seite die Aussage inhaltlich? Ist die Paraphrase **enger oder gleich weit** wie die Quelle? Urteil zurückschreiben mit `--verdikt <hash>=OK --notiz "<Begründung>"`. Nicht gedeckte Aussagen bleiben als Befund stehen. Der typische reale Fund ist keine Erfindung, sondern eine Paraphrase, die **schärfer** formuliert ist als die Quelle (Quantoren, Absolutaussagen) – als „Claim präzisieren" listen, nicht als Plagiatsverdacht.
4. **Nicht prüfbare Quellen sind ein Befund, kein Freifahrtschein:**
   - `… (Versatz unbekannt)` im Befund → das Skript konnte gedruckte und PDF-Seite nicht zuordnen (typisch bei Artikel-PDFs) und hat gegen das **ganze** Dokument geprüft: Wortlaut und Inhalt sind gedeckt, nur die Seitenangabe nicht bestätigt. Für seitengenaue Prüfung den Versatz einmalig setzen: `--offset <key>=<n>` (gedruckte Seite + n = PDF-Seite).
   - `NICHT PRÜFBAR` (Scan ohne Textebene, defektes PDF) → OCR oder manuelle Prüfung durch den Nutzer; im Bericht ausweisen.
   - `LIVE PRÜFEN` (Webquelle ohne Snapshot) → Seite abrufen, Aussage prüfen, Urteil eintragen **und** den Nutzer an die Snapshot-Pflicht erinnern (Seite als PDF nach `sources/literature/`, Pfad über Zotero ins `file`-Feld). Ohne Snapshot ist der geprüfte Stand später nicht mehr nachweisbar.
5. **Alles, was ich nicht selbst klären kann, wird zur Prüfaufgabe des Nutzers** – nicht zu einer Randnotiz. Jeder Fall mit Status NICHT PRÜFBAR oder LIVE PRÜFEN und jeder Seitenbefund, der auf der Begriffs-Heuristik beruht (die Heuristik erzeugt bei sauberen Paraphrasen Fehlalarme), gehört in den Berichtsabschnitt „Bitte manuell prüfen" mit den vier Angaben aus `CLAUDE.md` -> Grundprinzipien: was, wo, woran erkennbar, warum nicht durch mich. Erst danach darf eine Zitation als erledigt gelten.
6. **Im Abgabe-Audit blockierend.** Offene Befunde der Klassen WORTLAUT, ZITAT WEICHT AB, SEITE VERDÄCHTIG, NICHT GEFUNDEN und CLAIM SCHÄRFER verhindern die Abgabe-Freigabe – das sind genau die Fälle, die in einer Bewertung als Falschzitat oder Übernahme gelten. In früheren Audits sind sie Arbeitsaufträge mit Score-Abzug.

## Score-Regel

Abzüge von 100 Punkten, nach Schweregrad – nicht additiv über beliebig viele Kleinigkeiten, sondern gedeckelt pro Kategorie (max. Abzug in Klammern):

| Fund | Abzug pro Vorkommen | Kategorie-Deckel |
|---|---|---|
| Erfundener/fehlender BBT-Key | −20 | −40 |
| Fehlender Pflicht-Punkt aus Typ-Datei (Teil-Check B) | −15 | −45 |
| Formalia-Verstoß (Teil-Check A, außer BBT-Keys) | −8 | −32 |
| Struktur-Verstoß (Teil-Check C) | −10 | −30 |
| Build schlägt fehl (Teil-Check D) | −20 | −20 |
| Undefined reference/citation, fehlendes Bild, doppeltes Label (Teil-Check D) | −5 | −15 |
| Seitenumfang außerhalb der Vorgabe (Teil-Check D) | −10 | −10 |
| Literaturverzeichnis-Verstoß (Teil-Check F, pro Regelverstoß-Klasse) | −5 | −15 |
| Anti-KI-Stil-Verstoß, gehäuft (>3 Vorkommen in einem Kapitel; Skript-Funde GEDANKENSTRICH/TRIAS/RHETFRAGE/ABSATZ-UNIFORM zählen mit) | −5 | −10 |
| Verständlichkeits-Verstoß, gehäuft (>3 Vorkommen in einem Kapitel; Skript-Funde SATZLAENGE/SATZSCHNITT/META-VERB/NOMINALSTIL zählen mit) | −5 | −15 |
| Wortlautübernahme oder abweichendes Zitat (Teil-Check G) | −15 | −45 |
| Falsche Seitenangabe oder nicht gedeckter Claim (Teil-Check G) | −8 | −32 |
| Nicht prüfbare Quelle ohne Volltext (Teil-Check G) | −5 | −15 |

Teil-Check E fließt nicht in den Score ein – offene Abgabe-Punkte erscheinen ausschließlich als „Vor der Einreichung"-Hinweis (siehe Teil-Check E).

Ungenutzte Bib-Einträge fließen **nicht** in den Score ein – reiner Aufräumhinweis, kein Qualitätsproblem.

**Schwellenwerte**:
- **≥ 80/100** – abgabereif, verbleibende Punkte optional nachbessern.
- **60–79/100** – Überarbeitung empfohlen, mit `schreib-modus` gezielt an den Kritikpunkten arbeiten.
- **< 60/100** – nicht einreichen, mindestens einen weiteren Prüf-Schreib-Zyklus einplanen.

Score ist ein Hilfswert zur Priorisierung, keine Zusicherung; die inhaltliche Entscheidung "einreichen oder nicht" bleibt beim Nutzer.

---

## Feedback-Format (`pruefbericht.md`)

Vollständige Berichtsvorlage samt allen Abschnitten (Kopfzeile, Teil-Check-Blöcke A–F, Claims, Punkteabzug, Bewertungsschwerpunkte, Lieferobjekt-Abgleich, Handlungsempfehlungen, „Vor der Einreichung"-Checkliste): `references/berichtvorlage.md` – **laden, sobald der Bericht geschrieben wird** (Kapitel-, Voll-, Re- und Abgabe-Audit; Plan-Audit und Bereitschafts-Check schreiben keinen Bericht). Pro Lauf überschreiben, Datum und geprüften Stand in die Kopfzeile.

