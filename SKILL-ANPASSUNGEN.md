# SKILL-ANPASSUNGEN.md

Offene Änderungsvorschläge an Skills, Skripten und `CLAUDE.md`. **Kein Abgabebestandteil.**

Angelegt 2026-07-29 nach der Gegenlesung Runde 8. Alle Punkte stammen aus dem, was in genau dieser Sitzung geklemmt hat — keine allgemeinen Verbesserungsideen. Jeder Punkt nennt die Datei, die zu ändern wäre, und wo möglich den Ersatztext.

**Status:** alle Punkte OFFEN, keiner umgesetzt.

---

## P1 — „Bitte manuell prüfen" fehlt als Pflichtbestandteil der Gegenlesungs-Runde und ggf. auch Audit-Runden

**Datei:** `.claude/skills/gegenlesung/SKILL.md` → Schritt 6 (Ausgabe). Gegebenenfalls auch im Audit-Skill.

**Befund.** Schritt 6 verlangt vier Dinge in der Runde: Befunde, Soll-Ist-Tabelle, Gesamteinschätzung, Umfangshinweis. Die Liste **„Bitte manuell prüfen"** steht nicht darunter — obwohl `CLAUDE.md` → Grundprinzipien sie global vorschreibt („Unsicherheit wird zur Prüfaufgabe für den Nutzer, nicht zur Fußnote"). In dieser Sitzung wurde Runde 8 folgerichtig ohne sie geschrieben; der Nutzer musste nachfragen, ob die unklaren Punkte überhaupt in der Schreib-Session ankommen. Nachgetragen wurde sie erst danach.

**Warum das nicht kosmetisch ist.** Eine Gegenlesung produziert systematisch Punkte, die sie nicht selbst entscheiden kann — die Volltextlage, der reale Prompt eines Bildwerkzeugs, die gedruckte Seitenzahl. Stehen sie nur als Nebensatz in einer Anweisung („am Volltext prüfen, ob …"), liest die Schreib-Session sie als Option unter zwei gleichwertigen und wirft eine Münze. Genau das ist in Runde 8 bei 8.8 und 8.10 angelegt gewesen.

**Konkrete Änderung.** In Schritt 6 nach dem Umfangshinweis ergänzen:

> Zusätzlich am Ende der Runde eine eigene Sektion `#### Bitte manuell prüfen` – auch wenn sie nur einen Punkt enthält. Je Punkt fünf Angaben: (1) was zu prüfen ist, (2) wo – Datei, Zeile, Quelle, Seite, (3) woran erkennbar ist, dass es stimmt, (4) warum die Gegenlesung es nicht konnte, (5) **welche Option gilt, wenn die Prüfung unterbleibt**. Angabe (5) ist der Unterschied zwischen einer Prüfaufgabe und einer offenen Frage: Ohne sie steht die Schreib-Session vor zwei Optionen ohne Entscheidungsgrundlage.

**Zusatz:** In `_shared/aenderungen-format.md` das Runden-Gerüst um `#### Bitte manuell prüfen` erweitern, damit die Sektion einen festen Ort hat und `schreib-modus` sie beim Abarbeiten immer an derselben Stelle findet. Runde 7 hat diese Sektion bereits – aber als Eigenerfindung, nicht als Format.

---

## P2 — Prüferfrage 3 ist mit dem aktuellen Leseverbot nicht beantwortbar

**Datei:** `.claude/skills/gegenlesung/SKILL.md` → Ladevorschrift (Z. 20) und Schritt 4, Frage 3

**Befund.** Die Ladevorschrift erlaubt `references.bib` ausdrücklich „nur zur Zählung der Einträge (per Grep auf `^@`), **nicht inhaltlich**"; `sources/literatur/` kommt gar nicht vor, ist also verboten. Prüferfrage 3 lautet aber „**Ist jede Behauptung nachprüfbar?**". Beides zusammen geht nicht: Die kalte Lesung kann nur feststellen, ob eine Zitation *dasteht*, nicht ob sie *trägt*. In Runde 8 hat das genau einen halben Befund erzeugt — 8.8 („zwei Befunde aus der Nudge-Forschung", belegt ist einer) konnte die Auffälligkeit benennen, aber nicht auflösen, und musste die Entscheidung an eine manuelle Prüfung abgeben.

**Warum die Aufgabenteilung trotzdem stimmt – nur an der falschen Linie.** `pruef-modus` Teil-Check G prüft Zitationen mechanisch: Steht der Wortlaut auf der angegebenen Seite? Das ist eine andere Frage als die der Gegenlesung: **Trägt die Quelle die Rolle, die der Satz ihr im Argument zuweist?** Die zweite Frage kann nur ein kalter Leser stellen, weil sie am Absatz hängt, nicht an der Zitatzeile. Sie gehört hierher.

**Konkrete Änderung.** (a) Ladevorschrift, Z. 20 ersetzen:

> - `references.bib` vollständig, inklusive Inhalt (Autor, Jahr, Typ, Seitenbereich).
> - Die Volltexte in `sources/literatur/` – **aber nur für die Zitationen, deren Aussage die Lesung in Zweifel zieht**, nicht als Vollprüfung aller Stellen. Der lückenlose Abgleich ist `pruef-modus` Teil-Check G; hier geht es um die einzelne Stelle, an der der Trägersatz mehr verspricht, als er einlöst.

(b) In die Ladevorschrift unter „ausdrücklich NICHT zu lesen" aufnehmen: **`quellencheck.md` und `quellencheck-state.json`**, dazu das Verbot, `check_quellentreue.py` als Prüfskript auszuführen. Beide enthalten die bereits vergebenen Urteile früherer Läufe; wer sie liest, prüft nicht mehr, sondern bestätigt. Sie fehlen im Skill komplett und mussten in dieser Sitzung ad hoc in beide Subagenten-Briefs geschrieben werden.

(c) Prüferfrage 3 um die sieben Prüfachsen ergänzen, die sich in dieser Sitzung als die tragenden erwiesen haben: **Deckung** (sagt die Quelle das?) · **Richtung** (sagt sie es in dieselbe Richtung – der Klassiker ist die verworfene Hypothese, die als Beleg benutzt wird) · **Reichweite** (ist die Textaussage weiter als die Quelle?) · **Locator** (steht es auf der genannten Seite, passt sie zum Seitenbereich im Bib-Eintrag?) · **Ankündigung ↔ Einlösung** („zwei Befunde", „mehrere Studien") · **Attribution** (Autorname im Fließtext ohne Zitation oder umgekehrt) · **Doppelnutzung** (dieselbe Quelle für unterschiedlich starke Aussagen).

Der Nivedhitha-Fall dieses Projekts – die Studie verwirft den direkten Zusammenhang, den der Text ihr zuschrieb – ist genau die Achse „Richtung" und wurde von keiner Gegenlesung, sondern erst von einer Volltextprüfung gefunden.

**Empirischer Beleg, noch in derselben Sitzung.** Der Vorschlag wurde probeweise als zugeschnittene Runde gefahren (Runde 9, Zitatkontext, mit Lesefreigabe für `sources/literatur/`): **zehn Befunde über alle 19 Zitationen**, darunter drei echte Reichweiten-Überdehnungen – eine davon im Fazit („die *belegte* Wirksamkeit von Gamification", während die Quelle auf derselben Seite keine signifikante Gruppendifferenz berichtet). **Keiner dieser zehn Befunde wäre ohne Volltextzugriff auffindbar gewesen**; die Vollgegenlesung derselben Sitzung hat aus demselben Material genau einen halben Befund gezogen (8.8). Zugleich hat die Runde bestätigt, dass die Achse „Richtung" sauber ist – eine Entlastung, die ohne Volltexte ebenfalls nicht aussprechbar wäre.

---

## P3 — Der Subagent ist der Regelfall, nicht die Alternative

**Datei:** `.claude/skills/gegenlesung/SKILL.md` → Ladevorschrift, letzter Absatz (Z. 31)

**Befund.** Der Skill formuliert die Übergabe an einen Subagenten als Ausweichweg: „Wenn die Sitzung bereits Kontext zur Arbeit trägt – etwa weil vorher geschrieben oder geprüft wurde … Alternativ per `Agent`-Tool …". Tatsächlich trägt **jede** Sitzung Kontext, weil `CLAUDE.md` automatisch geladen wird und der Abschnitt „Aktueller Projektstatus" in diesem Projekt inzwischen über 10.000 Wörter Prüfhistorie enthält – jeden Befund, jede Behebung, jede Bewertung. Die Anweisung „behandle das als nicht vorhanden" ist für eine Kontamination dieser Größe nicht durchführbar. Beide bisherigen Gegenlesungen (Runde 6 am 24.07., Runde 8 am 29.07.) sind deshalb über Subagenten gelaufen.

**Konkrete Änderung.** Absatz ersetzen:

> **Ausführung: standardmäßig über einen Subagenten.** `CLAUDE.md` wird in jeder Sitzung automatisch geladen, und ihr Abschnitt „Aktueller Projektstatus" wächst mit jedem Audit – in einem reifen Projekt enthält er die vollständige Befundhistorie. Eine kalte Lesung ist in der Hauptsession dann nicht mehr simulierbar. Deshalb: Auftrag per `Agent`-Tool an einen Subagenten, Brief nach der Vorlage in `_shared/gegenlesung-subagent-brief.md`. Direkt in der Hauptsession lesen ist nur zulässig, solange der Projektstatus noch wenige Zeilen umfasst – und auch dann nur, wenn in dieser Sitzung noch nicht geschrieben oder geprüft wurde.

---

## P4 — Es fehlt eine Brief-Vorlage für den Subagenten

**Neue Datei:** `.claude/skills/_shared/gegenlesung-subagent-brief.md`, referenziert aus `gegenlesung/SKILL.md`

**Befund.** In dieser Sitzung wurde der Subagenten-Auftrag zweimal von Hand aus dem Skill destilliert (Vollgegenlesung, dann Zitatkontext). Jede Destillation ist eine Fehlerquelle: Die Verbotsliste muss vollständig wiederholt werden, die Reihenfolge „Erwartung vor Exposition" muss ausdrücklich erklärt werden (sonst liest der Subagent zuerst den Text), der Ausgabepfad muss gesetzt werden, und das Schreibverbot auf `AENDERUNGEN.md` muss dazu (siehe P5). Fällt eines davon aus, ist die Runde entwertet, ohne dass es auffällt.

**Konkrete Änderung.** Vorlage anlegen mit fixem Gerüst und benannten Platzhaltern:
`<ZUSATZPRÄMISSE>` (freier Nutzer-Kontext, z. B. „Abgabe in Woche 3") · `<WORTZAHL>` und `<SEITENSTAND aus dem letzten Build>` · `<AUSGABEPFAD im Scratchpad>` · `<SONDERAUFTRAG>` für zugeschnittene Runden.

Fixer Bestandteil der Vorlage, nicht verhandelbar: die vollständige Verbotsliste inkl. `quellencheck*` und Git-Historie, der Satz zur Behandlung des `CLAUDE.md`-Status als nicht vorhanden, Schritt 1 („zuerst nur `aufgabe.md`, den Text noch nicht"), die sieben Prüferfragen im Wortlaut, das Schreibverbot auf `AENDERUNGEN.md`, und die Aufforderung, Abwesenheiten als wertvollsten Befundtyp zu behandeln und nichts zu erfinden, um die Liste zu füllen.

---

## P5 — Rollentrennung bei der Ergebnis-Übergabe ist nirgends geregelt

**Datei:** `.claude/skills/gegenlesung/SKILL.md` → Schritt 6

**Befund.** Schritt 6 sagt „Befunde als **neue Runde in `AENDERUNGEN.md`**". Läuft die Lesung über einen Subagenten, kann der das nicht tun: Er darf `AENDERUNGEN.md` nicht lesen (Leseverbot), bräuchte die Datei aber, um die Rundennummer zu bestimmen und unter „## Offen" einzuhängen. In dieser Sitzung wurde das ad hoc gelöst – Subagent schreibt in den Scratchpad, Hauptsession überträgt.

**Konkrete Änderung.** Als Regel aufnehmen:

> **Rollentrennung:** Der Subagent ist der kalte Leser und schreibt seinen vollständigen Bericht in eine Scratchpad-Datei. Er schreibt **nicht** in `AENDERUNGEN.md` – die Datei steht auf seiner Verbotsliste, und Rundennummer wie Einhängepunkt kann nur kennen, wer sie lesen darf. Die Hauptsession überträgt den Bericht anschließend als neue Runde, ohne Befunde zu entschärfen oder zusammenzufassen: Sie ist Schreiber, nicht zweite Instanz.

Der letzte Halbsatz ist der wichtige. Die Hauptsession kennt den Entstehungskontext und ist damit die Instanz, die am ehesten geneigt ist, einen Befund „einzuordnen", der sich gegen eine Entscheidung richtet, die sie selbst getroffen hat.

---

## P6 — Der Umfangshinweis stützt sich auf die falsche Datengrundlage

**Dateien:** `.claude/skills/gegenlesung/SKILL.md` → Schritt 6 · `.claude/skills/_shared/scripts/check_umfang.py` · `kapitelplan.md:7`

**Befund, drei Teile.**

1. Schritt 6 schreibt: „Datengrundlage ist `check_umfang.py`, **nicht eine Schätzung**". Das Skript selbst schreibt in seine Ausgabe: „Das ist eine **SCHÄTZUNG**, keine Messung … beobachtet wurden bis zu +1,5 Seiten Abweichung nach oben." Der Skill erklärt also eine Schätzung zur Messung. In diesem Projekt hat das mehrfach getragen: Das Skript meldete 9,5–9,8 Seiten, gebaut wurden 10 bzw. 11.
2. `kapitelplan.md:7` trägt unter „**Gesamtwortzahl** (Richtwert)" den Wert „7–10 Seiten". Das Skript erkennt das, meldet einen HINWEIS – und **überspringt den Zielabgleich stillschweigend**. Seit dem 21.07. läuft die Umfangsprüfung also ohne Zielwert, ohne dass es je aufgefallen wäre.
3. Der einzige belastbare Wert ist die gedruckte Seitenzahl aus dem letzten `latexmk`-Lauf. Der Skill nennt ihn nicht.

**Konkrete Änderung.** (a) Schritt 6 umformulieren:

> Datengrundlage ist die **gedruckte Seitenzahl des letzten Builds**, nicht `check_umfang.py`. Das Skript liefert die Wortzahl und damit das Delta dieser Runde – seine Seitenschätzung liegt systematisch zu niedrig, weil sie Abbildungen, Tabellen und Float-Umbrüche nicht kennt. Ist der letzte Build älter als der aktuelle Textstand, gehört dieser Umstand ausdrücklich in den Umfangshinweis, statt die Schätzung als Stand auszugeben.

(b) `check_umfang.py`: Wenn der Richtwert im Kapitelplan wie eine Seitenangabe aussieht, **hart abbrechen** statt zu warnen und zu überspringen. Ein still übersprungener Zielabgleich ist schlechter als ein Fehler – er sieht aus wie ein bestandener Check.

(c) `kapitelplan.md:7` auf eine Wortzahl umstellen (7–10 Seiten × ~375 ≈ 2.600–3.750 Wörter) und die Seitenvorgabe daneben als eigenes Feld führen.

---

## P7 — Stilbefunde brauchen eine Zählung, und geprüfte Regeln brauchen eine ausdrückliche Entlastung

**Datei:** `.claude/skills/gegenlesung/SKILL.md` → Schritt 4, Frage 7 und Schritt 6 (Ehrlichkeitspflicht)

**Befund.** Prüferfrage 7 nennt Anhaltspunkte („generische Formulierungen, wiederkehrende Satzbaumuster, verdichtete Pointen-Schlusssätze"), aber kein Verfahren. In Runde 8 hat erst das Auszählen den Befund brauchbar gemacht: 30 Vorkommen „Doppelpunkt + Großbuchstabe", davon 3 in Tabellenzellen und ~4 legitime Aufzählungsdoppelpunkte, bleiben ~23 gegen den Richtwert von ~12 aus `hard-rules-formal.md`. Umgekehrt hat dieselbe Runde die Kontrastfiguren ausdrücklich **entlastet** („9–10 auf geschätzt 10 Seiten, an der Grenze, aber nicht darüber – bitte auch nicht vorsorglich umschreiben"). Ohne diese Entlastung hätte die nächste Runde sie erneut angestrichen und die Schreib-Session hätte etwas repariert, das in Ordnung war.

**Konkrete Änderung.** In Frage 7 ergänzen:

> Stilmuster werden **gezählt**, nicht empfunden: Vorkommen ermitteln, um Tabellenzellen und legitime Fälle bereinigen, gegen den Richtwert in `hard-rules-formal.md` → Schreibstil stellen und beide Zahlen im Befund nennen. Ein Stilbefund ohne Zahl ist eine Geschmacksäußerung.

In Schritt 6, Ehrlichkeitspflicht, ergänzen:

> Jede Stilregel, die geprüft wurde und **eingehalten ist**, bekommt einen eigenen Eintrag im Abschnitt „Was gut ist" – mit Zahl und dem ausdrücklichen Hinweis, dass hier nichts zu tun ist. Sonst prüft die nächste Runde dieselbe Regel kalt nach und meldet sie als neu.

---

## P8 — Bewusst verworfene Anforderungen kommen in jeder kalten Runde zurück

**Neue Datei:** `verworfen.md` im Projekt-Root · referenziert aus `gegenlesung/SKILL.md` Schritt 6

**Befund.** Die beiden in `aufgabe.md` namentlich genannten Einstiegstitel (Kapoor et al. 2018, Hansch & Rentschler 2012) sind in **Runde 1, 3, 6 und erneut als 8.17** aufgeschlagen und jedes Mal bewusst übersprungen worden. Das ist kein Fehler der Lesungen, sondern eine zwangsläufige Folge ihres Designs: Die Entscheidung liegt in `AENDERUNGEN.md` und im Projektstatus – beides Leseverbot. Jede kalte Runde muss den Punkt wiederfinden, und jedes Mal kostet er einen Befund-Slot, eine Freigabe-Rückfrage und Bearbeitungszeit.

**Konkrete Änderung.** Kleine Datei `verworfen.md` im Root: eine Zeile je bewusst verworfener Anforderung, mit Datum, Begründung und – wichtig – der Bedingung, unter der die Entscheidung wieder aufzumachen wäre. Der Gegenlesungs-Skill nimmt sie in die Ladevorschrift auf, **aber ausdrücklich erst in Schritt 6**, nach Erwartungsbildung und Textlesung. So bleibt die Inversion unbeschädigt: Die Lesung findet den Punkt weiterhin kalt, meldet ihn aber nicht als Befund, sondern unter einer eigenen Überschrift „Erneut gesehen, bewusst verworfen" – ohne Nummer, ohne Anweisung.

**Gegenprobe zum Risiko.** Eine solche Datei kann legitime Wiedervorlagen unterdrücken. Deshalb: Jeder Eintrag trägt eine Begründung, und die Lesung ist ausdrücklich beauftragt, ihn **doch** als Befund zu führen, wenn die Begründung inzwischen nicht mehr trägt (Beispiel: „übersprungen, weil die Quellen nicht in `references.bib` stehen" gilt nicht mehr, sobald sie dort stehen).

---

## P9 — Mehrere Prüfläufe in einer Sitzung sprengen das Runden-Format

**Datei:** `.claude/skills/_shared/aenderungen-format.md`

**Befund.** Das Format schreibt: „Jede prüfende Sitzung hängt **genau eine** neue Runde an." Diese Sitzung hat zwei erzeugt – Runde 8 (Vollgegenlesung) und eine zugeschnittene Zitatkontext-Runde auf Nutzerwunsch. Ohne Kennzeichnung kann `schreib-modus` beim Abarbeiten nicht unterscheiden, ob eine Runde die ganze Arbeit abgedeckt hat oder nur einen Ausschnitt – was für die Frage zählt, ob danach ein Voll-Audit oder ein Delta-Re-Audit fällig ist.

**Konkrete Änderung.** Regel ersetzen durch: „Jeder Prüflauf hängt genau eine Runde an. Läuft in einer Sitzung mehr als einer, trägt jede Runde ihren **Umfang im Titel** – `Runde 9 – Gegenlesung (Zitatkontext)` statt nur `Gegenlesung`." Dazu im Runden-Gerüst eine Zeile `**Umfang:** vollständig | zugeschnitten auf <Thema>` direkt unter der Überschrift.

---

## P10 — Die Bildprüfung ist der teuerste Teil der Runde und wird jedes Mal komplett wiederholt

**Datei:** `.claude/skills/gegenlesung/SKILL.md` → Schritt 4, Frage 1

**Befund.** Prüferfrage 1 verlangt zu Recht, gestaltete Artefakte per `Read`-Tool anzusehen – in Runde 8 war das der Teil, der die wertvollste Aussage lieferte („jede im Text behauptete Oberflächen-Eigenschaft ist im Bild belegt"). Es ist zugleich der teuerste Teil: fünf Bilder, jedes ein Vielfaches einer Textdatei. Ob sich seit der letzten Runde überhaupt etwas geändert hat, kann die Lesung nicht wissen – die Historie ist Leseverbot.

**Konkrete Änderung.** Die Runde protokolliert, **welche Bilddateien geprüft wurden, mit Kurz-Hash** (`sha1sum images/**/*.png | cut -c1-10`). Eine spätere Runde darf ein Bild überspringen, dessen Hash unverändert ist **und** dessen beschreibender Fließtext sich nicht geändert hat – die zweite Bedingung ist nötig, weil die Drift auch von der Textseite kommen kann. Kein Leseverbot wird dadurch verletzt: Der Hash steht in der Runde selbst, nicht in einer der gesperrten Dateien, und sagt nichts über frühere Befunde aus.

---

## P11 — Claim-Drift über Kapitelgrenzen: Keine Prüfung vergleicht mehrfach genutzte Quellen miteinander

**Dateien:** `.claude/skills/gegenlesung/SKILL.md` → Schritt 4, Frage 3 · `.claude/skills/_shared/scripts/check_quellentreue.py`

**Befund.** Runde 9 hat eine Fehlerklasse gefunden, die keine der bestehenden Prüfungen finden **kann**: Die Arbeit begrenzt eine Quelle bei der Erstnutzung mustergültig – `03_konzept.tex:11`: „Die Studie stützt damit die Entscheidung für Gamification, **belegt aber nicht** die Wirkung der konkreten Punkte- und Level-Mechanik …" – und lässt die Begrenzung im Fazit fallen: `01_kernergebnisse_und_ausblick.tex:5`: „die **belegte** Wirksamkeit von Gamification". Dieselbe Quelle, dieselbe Seite, stärkere Behauptung.

Warum das keine der Prüfungen sieht: `check_quellentreue.py` prüft jede Zitation **einzeln** gegen den Volltext – beide Stellen bestehen den Test für sich genommen. Der `pruef-modus` prüft kapitelweise. Die Gegenlesung liest linear und hat den Konzept-Satz 40 Absätze früher gesehen. Die Drift entsteht genau in der Lücke zwischen diesen drei Blickwinkeln, und sie entsteht systematisch: Fazitkapitel werden zuletzt und aus der Erinnerung geschrieben.

Zweiter Fall derselben Klasse in derselben Runde: **Tabellenzellen komprimieren Zitationen und verlieren dabei den Geltungsbereich.** `03_konzept.tex:22` deckt mit einer Stellenangabe zwei Mechanismen ab („Feedback/Fortschritt **sowie** geplante Erinnerungsbenachrichtigung `\parencite[S. 10]{barker…}`"), von denen die Quelle nur einen trägt. Im Fließtext wäre das aufgefallen; in einer Zelle liest es niemand als Behauptung.

**Konkrete Änderung.**

(a) Prüferfrage 3 um eine Achse erweitern: **Anspruchsverlauf.** Jede Quelle, die mehr als einmal zitiert wird, wird über **alle** ihre Fundstellen hinweg verglichen: Ist eine spätere Behauptung stärker als eine frühere? Die Erstnutzung setzt die Obergrenze – Fazit und Tabellen dürfen sie nicht überschreiten. Dazu die Regel: **Eine Zitation in einer Tabellenzelle deckt nur das zuletzt genannte Element**, sofern die Zelle nichts anderes sagt; steht davor ein zweiter Mechanismus, braucht er einen eigenen Beleg oder die ausdrückliche Kennzeichnung als eigene Gestaltung.

(b) `check_quellentreue.py` um einen **Anspruchsverlaufs-Bericht** ergänzen (deterministisch, keine Bewertung): für jeden Bib-Key, der mehr als einmal zitiert wird, alle Trägersätze untereinander ausgeben, mit Datei:Zeile und Locator. Optional als Warnung, wenn an einer Fundstelle ein Stärkewort steht (`belegt`, `beweist`, `zeigt`, `belegen`) und an einer anderen desselben Keys ein Hedge (`stützt`, `deutet`, `legt nahe`, `kann`). Das Skript entscheidet nichts – es legt die Sätze nebeneinander, was heute niemand tut. In diesem Projekt hätte allein das den Befund 9.3 sichtbar gemacht: Soma wird viermal zitiert, dreimal mit Hedge, einmal mit „belegte".

---

## P12 — „19/19 OK" bedeutet weniger, als es klingt

**Dateien:** `.claude/skills/pruef-modus/SKILL.md` → Teil-Check G · `.claude/skills/_shared/scripts/check_quellentreue.py` · `CLAUDE.md` → Statuszeilen-Konvention

**Befund.** Vor Runde 9 stand in diesem Projekt „**Teil-Check G 19/19 OK**" – als Beleg dafür, dass die Zitationen geprüft sind. Runde 9 hat an genau diesen 19 Stellen zehn Befunde gefunden, darunter drei echte Reichweiten-Überdehnungen. Beides ist richtig: Der Wortlaut **steht** jeweils auf der angegebenen Seite. Nur beantwortet das eine andere Frage als die, die der Leser hinter „OK" vermutet.

Das Urteilsvokabular verspricht mehr, als das Verfahren einlöst. „OK" heißt heute: *Ein zur Textstelle passender Wortlaut wurde in der Quelle an der angegebenen Stelle gefunden.* Es heißt **nicht**: *Die Quelle trägt die Behauptung in der Stärke, in der der Satz sie aufstellt.* Genau der Unterschied ist der Bewertungsunterschied.

**Konkrete Änderung.**

(a) Urteilswert umbenennen: `OK` → **`FUNDSTELLE OK`**. Ein Wort, und die Aussage stimmt wieder. Der `quellencheck-state.json`-Wert kann intern bleiben; die Ausgabe und die Statuszeilen ändern sich.

(b) In `pruef-modus` → Teil-Check G aufnehmen: „Teil-Check G prüft **Fundstelle und Wortlaut**, nicht die Reichweite. Die Frage, ob die Quelle die Behauptung in ihrer Stärke trägt, beantwortet die Gegenlesung (Prüferfrage 3) – ein bestandener Teil-Check G ist dafür **kein** Ersatz und darf im Bericht nicht als solcher dargestellt werden."

(c) Workflow-Folge, für den Fahrplan in `CLAUDE.md`: Die Reichweitenprüfung muss **vor** dem Abgabe-Audit laufen, weil ihre Befunde Textänderungen erzwingen und ein vorher gefahrenes Audit entwerten würden. Sie gehört damit in die Gegenlesungs-Phase – konsistent mit P2, aber hier ist es die Begründung aus der Reihenfolge, nicht aus der Zuständigkeit.

---

## P13 — Die Zusatzprämisse des Nutzers aktiv erfragen

**Datei:** `.claude/skills/gegenlesung/SKILL.md` → Schritt 1

**Befund.** In dieser Sitzung kam die Vorgabe „Abgabe innerhalb von Woche 3" vom Nutzer, unaufgefordert und beiläufig. Sie hat direkt zu **Befund 8.4** geführt (der Bericht kündigt eine Phase als bevorstehend an, in der er bei Abgabe selbst steht) und zu einer eigenen Prüftabelle, die belegt, dass die übrige Phasenplanung robust ist. Ohne die Prämisse wäre die ganze Zeitachse ungeprüft geblieben – nicht weil sie unauffällig ist, sondern weil ohne Abgabezeitpunkt kein Maßstab existiert.

Der Skill fragt nichts dergleichen ab. Er kennt nur `aufgabe.md` als Maßstab – und dort steht der Abgabezeitpunkt in diesem Projekt bewusst nicht („kein festes Datum, `\today`").

**Konkrete Änderung.** Schritt 1 um einen Vorlauf ergänzen: Vor der Erwartungsbildung **einmal per `AskUserQuestion` nach Prüfkontext fragen**, der nicht in `aufgabe.md` steht – Abgabezeitpunkt bzw. Projektwoche, bekannte Schwerpunkte der prüfenden Person, Vorgaben aus Kolloquium oder Sprechstunde. Antwort geht als `<ZUSATZPRÄMISSE>` in den Subagenten-Brief (P4) und wird in der Runde als eigener Prüfabschnitt geführt. Keine Antwort ist eine gültige Antwort; die Frage kostet eine Interaktion und hat hier einen Befund erzeugt, den keine noch so sorgfältige Lesung des Textes hätte finden können.

---

## P14 — Numeruskongruenz bei `\textcite` mit mehreren Autor:innen (klein, mechanisierbar)

**Datei:** `.claude/skills/_shared/scripts/check_formalia.py`

**Befund.** `07_iteratives_design.tex:5`: „Für die Gruppengröße **gibt** `\textcite[Kap.~17.2.2]{erlhoferWebsiteKonzeptionUndRelaunch2017}` den Maßstab" – der Eintrag hat zwei Autor:innen (Erlhofer und Brenner), `\textcite` rendert entsprechend, das Prädikat muss „geben" lauten. Der Fehler ist im Quelltext unsichtbar, weil dort nur der Citekey steht; er entsteht erst beim Rendern und überlebt jedes Korrekturlesen der `.tex`-Datei.

**Konkrete Änderung.** Prüfung in `check_formalia.py`: Für jedes `\textcite{key}` die Autorenzahl aus `references.bib` ermitteln; steht unmittelbar davor oder dahinter eine Verbform der 3. Person **Singular** aus einer kleinen Wortliste (`gibt`, `zeigt`, `nennt`, `stellt fest`, `identifiziert`, `belegt`, `unterscheidet`, `definiert`, `beschreibt`, `fordert`), als HINWEIS melden. Bewusst als HINWEIS, nicht als FEHLER: Deutsche Wortstellung lässt Ausnahmen zu, und eine Wortliste ist nie vollständig. Der Nutzen liegt im Auffinden, nicht im Urteilen – ein einziger solcher Fehler in der Endfassung ist der Sorte Befund, die ein Prüfer sofort sieht.

---

## Nicht vorgeschlagen, bewusst

- **Kein eigener „Zitatkontext"-Skill.** Die Prüfung gehört als erweiterte Prüferfrage 3 in die Gegenlesung (P2). Ein eigener Skill würde die Frage aus dem Absatzkontext lösen – und genau der Kontext ist es, der den Befund erzeugt.
- **Keine Lockerung des `CLAUDE.md`-Leseverbots.** Der Vorschlag, den Projektstatus „gefiltert" zu lesen, klingt praktikabel, ist aber nicht überprüfbar: Gelesen ist gelesen. Der Subagent (P3) löst dasselbe Problem sauber.
- **Kein automatischer Abgleich Text ↔ Bild.** Naheliegend, aber die Befunde dieser Runde („Banner oben statt Karte unten", „Wochentage fehlen") hängen an einer Bedeutungsprüfung, die kein Skript leistet.
- **Keine automatische Reichweiten-Bewertung durch ein Skript.** P11 (b) schlägt bewusst nur einen **Bericht** vor, der die Trägersätze einer mehrfach zitierten Quelle nebeneinanderlegt, plus eine grobe Stärkewort-Warnung. Ob „belegt" an einer Stelle zu stark ist, hängt am Studiendesign der Quelle – das entscheidet kein Regex, und eine Automatik würde entweder alles oder nichts melden.
- **Keine Nachprüfung der bereits mit `OK` quittierten Zitationen als Routine.** P12 benennt die Bedeutungslücke, verlangt aber keinen erneuten Volltextdurchlauf bei jedem Audit – das wäre teuer und träfe dieselben Stellen. Die Reichweitenprüfung läuft einmal als Gegenlesungs-Runde (Runde 9) und danach nur noch für Zitationen, deren Trägersatz sich geändert hat.
