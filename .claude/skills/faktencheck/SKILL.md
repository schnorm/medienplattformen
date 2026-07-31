---
name: faktencheck
description: Prüft unzitierte Tatsachenbehauptungen über die reale Außenwelt – Produkte, Institutionen, Zahlen, Funktionsansprüche –, die keine Quellenangabe tragen und deshalb für Teil-Check G, Stresstest und Autoref-Check unsichtbar sind. Läuft als kalte, isolierte Sitzung ohne Projektstatus, Prüfbericht und Änderungshistorie, verifiziert jeden Kandidaten einzeln per Websuche und schreibt faktencheck-bericht.md. Nutzen, sobald alle Kapitel FERTIG sind und ein Marktüberblick, eine Wettbewerbsanalyse, eine Werkzeugbeschreibung oder ein Zahlenbestand in der Arbeit steht – nach der Gegenlesung, vor dem Abgabe-Audit.
---

# Faktencheck – unzitierte Behauptungen über die Außenwelt

## Zweck

Teil-Check G prüft Sätze **mit** Zitation. Der `stresstest` prüft Kernargumente. `check_autoref.py` prüft interne Verweise. Ein Satz, der eine überprüfbare Tatsache über die reale Welt behauptet und **keine** Quellenangabe trägt, fällt durch alle drei Netze – und ist damit die einzige Behauptungsklasse der Arbeit ohne laufenden Wächter.

Zwei Eigenschaften machen sie gefährlicher, als ihre Unauffälligkeit vermuten lässt:

**Der Fehler sitzt im Nebensatz, nicht im Kernargument.** Deshalb greift das Verifikations-Gate des Stresstests nicht: Es löst erst aus, wenn ein *Argument* auf einer Außenweltbehauptung ruht. Ein Detail, das das Argument nur schmückt oder stützt, bleibt unter der Schwelle – und trägt trotzdem eine Wertung, eine Tabellenzelle oder eine Abgrenzung.

**Die Welt bewegt sich, der Text nicht.** Ein zitiertes PDF sagt in zwei Jahren dasselbe. Ein Ministerium wird umbenannt, ein Produkt bekommt die Funktion, die der Text ihm abspricht, ein Anbieter verschwindet. Ein Satz, der beim Schreiben stimmte, kann bei der Abgabe falsch sein, ohne dass sich ein Zeichen geändert hat. Kein Diff, kein Audit und kein Lesedurchgang zeigt das an.

Betroffen ist vor allem die Textklasse, die laut `aufgabe.md` → „## Prüfer-Steuerungen" als **eigene Sichtung ohne Zitationspflicht** läuft. Genau diese Ausnahme von der Zitierpflicht macht ihre Fakten für den regulären Workflow unsichtbar – ohne sie von der Wahrheitspflicht zu befreien.

## Wann

**Nach der Gegenlesung, vor dem Abgabe-Audit.** Wie die Gegenlesung ist dies ein reiner Lese-Schritt; seine Befunde ändern den Text und würden ein vorher gefahrenes Audit entwerten. Auf Zuruf jederzeit möglich („Faktencheck").

**Pflicht, sobald die Arbeit einen Marktüberblick, eine Wettbewerbsanalyse, eine Werkzeug- oder Systembeschreibung oder einen nennenswerten Zahlenbestand enthält.** Ohne eine solche Textklasse liefert der Vorfilter kaum Kandidaten – dann genügt das Verifikations-Gate in Prüferfrage 3 der `gegenlesung`, und dieser Skill entfällt mit einem Satz Begründung im Prüfbericht.

## Ladevorschrift – dieselbe Inversion wie bei der Gegenlesung

**Zu lesen, ausschließlich:**
- alle `chapters/**/*.tex`, `pages/appendix.tex`, `pages/acronyms.tex`
- `aufgabe.md` → „## Prüfer-Steuerungen" – nur, um zu erkennen, welche Kapitel als eigene Sichtung ohne Zitationspflicht laufen. **Nicht** als Maßstab für inhaltliche Richtigkeit.
- das Web, je Kandidat gezielt.

**Ausdrücklich NICHT zu lesen:**
- `pruefbericht.md`, `AENDERUNGEN.md` (auch nicht das Erledigt-Log), `kapitelplan.md`
- `MEMORY.md`, `PERSISTENT.md`
- `CLAUDE.md` → „Aktueller Projektstatus" und „Aktuelle Richtung"
- **den eigenen `faktencheck-bericht.md` einer früheren Runde** und die Git-Historie

Der letzte Punkt ist der wichtigste und der am leichtesten zu übergehende. Jede dieser Dateien trägt das Urteil eines früheren Laufs, und ein „wurde schon geprüft" ist genau die Aussage, die dieser Skill nicht übernehmen darf: Sie war zu ihrer Zeit richtig und kann heute falsch sein, weil sich die Welt geändert hat, nicht der Text. Wer sie liest, prüft nicht mehr, sondern bestätigt.

**`faktencheck-state.json` ist davon ausgenommen** – aber nur maschinell. Das Skript nutzt ihn, um beurteilte Sätze stumm zu schalten; **gelesen wird er nicht.** Der Unterschied ist wesentlich: Der Zustand steuert, *welche* Sätze überhaupt aufschlagen, nicht, wie sie zu bewerten sind.

**Ausführung: standardmäßig über einen Subagenten.** Auftrag per `Agent`-Tool, Brief nach `_shared/faktencheck-subagent-brief.md`. Begründung wie bei der `gegenlesung`: `CLAUDE.md` wird automatisch geladen, und „behandle das als nicht vorhanden" ist ab einer gewissen Kontextmenge keine ausführbare Anweisung mehr.

## Ablauf

### Schritt 1 – Kandidaten einsammeln

```
python .claude/skills/_shared/scripts/check_aussenwelt.py
```

Das Skript liefert je Kandidat Hash, Fundstelle, Satz und die Signale, die ihn aufgegriffen haben. `~`-Signale sind vom Absatz geerbt: Der Satz selbst nennt nichts Nachschlagbares, sein Absatz schon (typisch „**die Plattform** bietet kein Werkzeug…"). Diese Klasse ist erfahrungsgemäß die ergiebigste und zugleich die, die man beim Lesen überspringt.

`[absolut: …]` markiert Verneinungen und Absolutheitswörter. Sie entscheiden nichts, verändern aber die Beweislast: „bietet **kein** X" ist widerlegt, sobald es irgendwo ein X gibt; „bietet wenig X" ist kaum je falsch. Absolutbehauptungen deshalb zuerst prüfen.


**`% SICHTUNG:`-Marker als Rangfolge nutzen, nicht als Filter.** Kapitel, die sich per Kommentarzeile selbst als eigene Sichtung deklarieren (siehe `schreib-modus`), erscheinen in der Kandidatenliste **zuoberst** und tragen den Marker in der Ausgabe. Sie zuerst abarbeiten – dort ist die Trefferdichte am höchsten. **Der Lauf endet dort aber nicht:** Der Vorfilter geht über alle Kapitel, und genau die Datei, an die beim Deklarieren niemand gedacht hat, ist der Fall, für den dieser Skill überhaupt existiert. Ein Kapitel ohne Marker gilt nicht als geprüft.

### Schritt 2 – Je Kandidat einmal recherchieren

Eine gezielte Suche pro Behauptung, nicht eine Sammelrecherche pro Kapitel. Aus dem Gedächtnis wird nichts bestätigt – auch nicht das, was offensichtlich wirkt (`CLAUDE.md` → „Erst prüfen, dann behaupten").

**Beleg-Standard, gestaffelt:**
- **Primärquelle** (die Anbieterseite selbst, das Impressum, die offizielle Mitteilung) – trägt eine Textänderung.
- **Konvergente Sekundärquellen** (mehrere unabhängige Tests, Herstellertext in Release Notes) – reichen für einen **Verdacht**, nicht für eine Korrektur.
- **Einzelnes Suchergebnis-Snippet** – reicht für gar nichts.

**Bot-Schutz ist der Normalfall, nicht die Ausnahme.** Anbieterseiten, App-Stores und Testportale antworten regelmäßig mit HTTP 403. Das ist kein Grund, auf Sekundärquellen auszuweichen und die Sache für erledigt zu erklären – und auch kein Grund, den Satz vorsorglich zu entschärfen (siehe Schritt 4). Der Kandidat wandert dann in „Bitte manuell prüfen", mit der Angabe, **woran** der Nutzer die Antwort erkennt, wenn er selbst nachsieht.

### Schritt 3 – Verdikt buchen

```
python .claude/skills/_shared/scripts/check_aussenwelt.py --verdikt <hash>=BESTÄTIGT --notiz "chefkoch.de/wochenplaner, gesehen 31.07.2026"
```

Vier Verdikte: `BESTÄTIGT` (an einer Quelle verifiziert, Beleg in der Notiz – Pflicht) · `WIDERLEGT` (Befund) · `NICHT VERIFIZIERBAR` (recherchiert, keine belastbare Quelle; bleibt sichtbar) · `EIGENE SETZUNG` (keine Außenweltbehauptung, sondern eigene Definition oder Benennung – der Vorfilter kann das nicht wissen).

`EIGENE SETZUNG` ist der Grund, warum dieser Check bezahlbar bleibt: Eigene Konzept- und Produktnamen sehen wie Entitäten aus und schlagen sonst in jeder Runde neu auf. Einmal gebucht, sind sie still, bis der Satz sich ändert.

### Schritt 4 – Konsequenzkette je Befund bestimmen

**Vor dem Formulierungsvorschlag, nicht danach.** Eine Sachkorrektur an einer Wettbewerbs- oder Bewertungsaussage bleibt fast nie lokal. Je Befund zusammenstellen:

1. den Satz selbst,
2. die Tabellenzelle oder Wertung, die er deckt,
3. jeden Satz, der daraus etwas ableitet – Lücken-Aussage, Alleinstellungsmerkmal, Fazit,
4. den **Zwilling in der Einleitung**, wo dieselbe Behauptung eine Ebene grundsätzlicher als Problem- oder Lückenbegründung steht.

Trägt eine dieser Stellen ein Kernargument, ist der ganze Befund `[FREIGABE]` – auch wenn der Auslöser eine harmlose Detailkorrektur war.

**Keine vorsorgliche Entschärfung.** Naheliegend wäre, eine zweifelhafte Absolutbehauptung abzuschwächen und die Tabelle stehen zu lassen. Das ist unzulässig, wenn der Satz die einzige Deckung einer Wertung ist: Ein entschärfter Fließtext bei unveränderter Zelle erzeugt eine unbedeckte Wertung und damit einen eigenen Audit-Befund. Der Fehler wäre getauscht, nicht behoben. Entweder verifizieren und beides zusammen anpassen – oder offen lassen und in „Bitte manuell prüfen" führen.

### Schritt 5 – Bericht

Ausgabe nach `faktencheck-bericht.md`, verbindliche Abschnitte:

- **Ergebnis in einem Satz.**
- **Methodik** – was gelesen wurde, was ausdrücklich nicht, wie viele Kandidaten, wie viele Suchen.
- **Befunde**, je mit Stelle, wörtlicher Behauptung, Rechercheergebnis, **warum das noch nicht als Korrektur gilt** (Belegstufe!), der Konsequenzkette und einem Formulierungsvorschlag, der ausdrücklich als Vorschlag markiert ist.
- **Vollständig bestätigte Kandidaten** als Tabelle – die Entlastung gehört genauso in den Bericht wie der Befund.
- **Kapitel ohne Kandidaten (kein Fund, nicht „nichts geprüft")** – eigener Abschnitt, wörtlich mit dieser Überschrift. Ohne ihn liest sich die Abwesenheit von Befunden als Lücke der Prüfung statt als Ergebnis.
- **Bitte manuell prüfen** – je Punkt die fünf Angaben aus `CLAUDE.md` → Grundprinzipien: was, wo, woran erkennbar, warum nicht durch mich, **und was gilt, wenn die Prüfung unterbleibt**.

**Rollentrennung.** Der Bericht ist eine Arbeitsliste für eine eigene `schreib-modus`-Sitzung, keine Umsetzung im selben Lauf. Der Subagent schreibt seinen Bericht direkt nach `faktencheck-bericht.md`; die Hauptsession überträgt ihn **ohne zu entschärfen oder zusammenzufassen** – sie kennt den Entstehungskontext und ist damit die Instanz, die am ehesten geneigt ist, einen Befund „einzuordnen", der sich gegen eine eigene Entscheidung richtet.

## Verhältnis zu den anderen Prüfschritten

| Prüft | Zuständig | Sieht nicht |
|---|---|---|
| Wortlaut und Fundstelle zitierter Stellen | Teil-Check G (`check_quellentreue.py`) | Sätze ohne `\cite` |
| Reichweite zitierter Stellen | `gegenlesung`, Prüferfrage 3 | Sätze ohne `\cite` |
| Interne Verweise, Fundstelle und Reichweite | Teil-Check C (`check_autoref.py`) | alles Externe |
| Kernargumente gegen die Außenwelt | `stresstest`, Verifikations-Gate | Nebensätze |
| **Unzitierte Außenweltbehauptungen** | **dieser Skill** | Behauptungen ohne nachschlagbare Entität |

Die letzte Zelle ist ehrlich gemeint: Ein Satz, der weder Eigennamen noch Zahl noch Domain trägt und in einem Absatz ohne solche steht, wird vom Vorfilter nicht aufgegriffen. Die Auffanglinie dafür ist das Verifikations-Gate in Prüferfrage 3 der `gegenlesung` – ein lesender Mensch beziehungsweise ein kalter Leser, kein Regex.
