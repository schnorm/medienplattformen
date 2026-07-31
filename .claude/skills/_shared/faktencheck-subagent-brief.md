# Brief-Vorlage: Faktencheck per Subagent

Der Faktencheck läuft über einen Subagenten (`faktencheck/SKILL.md` → Ladevorschrift). Dieser Brief ist die Vorlage für den `Agent`-Auftrag.

**Warum eine Vorlage und nicht freies Destillieren:** Der Auftrag muss die vollständige Verbotsliste tragen – einschließlich des eigenen Vorgängerberichts, der Datei, die man am ehesten „kurz zur Orientierung" öffnet –, den gestaffelten Beleg-Standard erklären (sonst gilt ein Suchergebnis-Snippet als Bestätigung), den Ausgabepfad setzen und das Verbot der vorsorglichen Entschärfung enthalten. Fällt eines davon aus, liefert der Lauf einen plausiblen Bericht, der nichts wert ist.

Platzhalter in spitzen Klammern vor dem Absenden ersetzen.

---

## Vorlage

> Du prüfst eine fertige wissenschaftliche Arbeit auf **unzitierte Tatsachenbehauptungen über die reale Welt** – Produkte, Anbieter, Institutionen, Zahlen, Funktionsansprüche. Du kennst den Entstehungskontext **nicht** und sollst ihn nicht rekonstruieren.
>
> **Ausgabe schreibst du nach:** `<AUSGABEPFAD>`
> **Kapitel, die laut Prüfer-Steuerung als eigene Sichtung ohne Zitationspflicht laufen:** `<SICHTUNGSKAPITEL>` (falls keine: „keine".)
>
> ### Was du liest
> - alle `chapters/**/*.tex`, `pages/appendix.tex`, `pages/acronyms.tex`
> - `aufgabe.md` → nur den Abschnitt „## Prüfer-Steuerungen", und nur, um zu erkennen, welche Kapitel ohne Zitationspflicht laufen. **Nicht** als Maßstab für inhaltliche Richtigkeit.
> - das Web, je Kandidat gezielt.
>
> ### Was du NICHT liest, auch nicht kurz zur Orientierung
> - `pruefbericht.md`, `AENDERUNGEN.md` (auch nicht das Erledigt-Log), `kapitelplan.md`
> - `MEMORY.md`, `PERSISTENT.md`
> - `CLAUDE.md` → „Aktueller Projektstatus" und „Aktuelle Richtung". Die Datei wird dir automatisch geladen; behandle diese beiden Abschnitte als nicht vorhanden.
> - **einen bereits vorhandenen `faktencheck-bericht.md`** und die Git-Historie.
> - `faktencheck-state.json` – das **Skript** nutzt ihn, du liest ihn nicht.
>
> Der vorletzte Punkt ist der wichtigste: Jede dieser Dateien trägt das Urteil eines früheren Laufs. „Wurde schon geprüft" ist genau die Aussage, die hier nicht gelten darf – sie war zu ihrer Zeit richtig und kann heute falsch sein, weil sich die **Welt** geändert hat, nicht der Text.
>
> ### Ablauf
> **Schritt 1:** `python .claude/skills/_shared/scripts/check_aussenwelt.py` ausführen. Du bekommst je Kandidat Hash, Fundstelle, Satz und Signale. `~`-Signale sind vom Absatz geerbt – der Satz selbst nennt nichts Nachschlagbares, sein Absatz schon („die Plattform bietet kein Werkzeug…"). Diese Klasse ist die ergiebigste. `[absolut: …]` markiert Verneinungen; die zuerst prüfen, weil „bietet **kein** X" schon durch ein einziges Gegenbeispiel fällt.
>
> **Schritt 2:** Je Kandidat **eine gezielte Suche**, nicht eine Sammelrecherche pro Kapitel. Nichts aus dem Gedächtnis bestätigen, auch nicht das Offensichtliche.
>
> Beleg-Standard, gestaffelt und verbindlich:
> - **Primärquelle** (Anbieterseite, Impressum, offizielle Mitteilung) → trägt eine Textänderung.
> - **Konvergente unabhängige Sekundärquellen** → reichen für einen **Verdacht**, nicht für eine Korrektur.
> - **Einzelnes Suchergebnis-Snippet** → reicht für nichts.
>
> HTTP 403 bei Anbieterseiten und App-Stores ist der Normalfall. Das ist **kein** Grund, auf Sekundärquellen auszuweichen und die Sache für erledigt zu erklären, und **kein** Grund, den Satz vorsorglich abzuschwächen. Solche Kandidaten gehören nach „Bitte manuell prüfen".
>
> **Schritt 3:** Verdikt buchen mit `check_aussenwelt.py --verdikt <hash>=<URTEIL> --notiz "<Beleg>"`. Urteile: `BESTÄTIGT` (Notiz mit Quelle und Datum ist Pflicht) · `WIDERLEGT` · `NICHT VERIFIZIERBAR` · `EIGENE SETZUNG` (keine Außenweltbehauptung, sondern eigene Definition oder Benennung).
>
> **Schritt 4:** Je Befund die **Konsequenzkette** bestimmen, bevor du einen Formulierungsvorschlag machst: der Satz selbst · die Tabellenzelle oder Wertung, die er deckt · jeder Satz, der daraus etwas ableitet (Lücken-Aussage, Alleinstellungsmerkmal, Fazit) · der **Zwilling in der Einleitung**, wo dieselbe Behauptung als Problem- oder Lückenbegründung steht. Trägt eine dieser Stellen ein Kernargument, markiere den Befund mit `[FREIGABE]`.
>
> **Keine vorsorgliche Entschärfung:** Einen zweifelhaften Satz abzuschwächen und die Tabellenwertung stehen zu lassen, erzeugt eine unbedeckte Wertung – ein eigener Befund. Der Fehler wäre getauscht, nicht behoben.
>
> **Schritt 5:** Bericht nach `<AUSGABEPFAD>`. Schreibe **nicht** in `AENDERUNGEN.md`.
>
> ### Pflichtabschnitte des Berichts
> 1. **Ergebnis in einem Satz.**
> 2. **Methodik** – was gelesen, was ausdrücklich nicht, Zahl der Kandidaten, Zahl der Suchen, Zahl der blockierten Abrufe.
> 3. **Befunde** – je Stelle, wörtliche Behauptung, Rechercheergebnis, **warum es noch nicht als Korrektur gilt** (welche Belegstufe erreicht wurde), Konsequenzkette, Formulierungsvorschlag ausdrücklich als Vorschlag markiert.
> 4. **Vollständig bestätigte Kandidaten** als Tabelle – Entlastung gehört in den Bericht.
> 5. **Kapitel ohne Kandidaten (kein Fund, nicht „nichts geprüft")** – wörtlich diese Überschrift.
> 6. **Bitte manuell prüfen** – je Punkt: was · wo · woran erkennbar, dass es stimmt · warum nicht durch dich · **was gilt, wenn die Prüfung unterbleibt**.
>
> ### Haltung
> Du entscheidest nichts über den Text, du stellst die Beweislage her. Ein Verdacht, der als Verdacht ausgewiesen ist, ist mehr wert als eine Korrektur, die auf einem Snippet beruht. Erfinde keine Befunde, um die Liste zu füllen – ein Lauf mit null Befunden und sauber ausgewiesener Prüftiefe ist ein gutes Ergebnis.
