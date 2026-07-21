---
name: stresstest
description: Fordert ein einzelnes Argument, eine These oder einen bereits geschriebenen Satz/Absatz mit Gegenargumenten heraus und bewertet dessen Stärke. Nutzen, wenn der Nutzer während Plan- oder Schreib-Modus (oder unabhängig davon) ein bestimmtes Argument hinterfragt haben will — nicht gebunden an eine bestimmte Phase. Wird auch von plan-modus in Schritt 4 aufgerufen, dort aber auf alle Kernargumente gleichzeitig statt auf ein einzelnes. Kennt zusätzlich einen Gesamt-Stresstest über die fertige Arbeit („Gesamt-Stresstest", „Stresstest auf die gesamte Arbeit") als inhaltliche Prüfebene, sobald alle Kapitel FERTIG sind — nach der Gegenlesung, vor dem Voll-Audit.
---

# Stresstest: Gegenargumente prüfen

## Wann dieser Skill greift

- Direkt während des Schreibens, wenn ein gerade formulierter Satz/Absatz unsicher wirkt.
- Auf Zuruf für ein einzelnes Argument, unabhängig vom Kapitelplan.
- Aus `plan-modus` Schritt 4 heraus, dort für alle Kernargumente aus `kapitelplan.draft.md` in einem Durchgang (siehe „Mehrfach-Modus" unten).

## Ablauf (Einzelargument)

1. Das zu prüfende Argument identifizieren — entweder ein vom Nutzer benannter Satz/Absatz oder ein explizit genanntes Argument.
2. 1–3 Gegenargumente formulieren, die ein kritischer Gutachter vorbringen würde. Nicht nur Standardeinwände — auf die spezifische Formulierung eingehen (z. B. Gültigkeitsbereich der zitierten Quelle, Sprung von deskriptivem Befund zu normativer Schlussfolgerung, unbelegte Verallgemeinerung).
3. Stärke jedes Gegenarguments einschätzen: **Stark** (Argument muss überarbeitet werden) / **Mittel** (Einschränkung sollte ergänzt werden) / **Schwach** (Argument hält, Gegenargument selbst schwach).
4. Nutzer reagiert inhaltlich — die Reaktion kommt vom Nutzer, nicht von mir (siehe `CLAUDE.md` → Grundprinzipien: These/Kernargumente bleiben beim Nutzer).
5. Auf Wunsch: geschärfte Formulierung vorschlagen (z. B. Gültigkeitsbereich einschränken), aber als Vorschlag, nicht als automatische Ersetzung im Fließtext.

### Ausgabeformat

```
Argument: <Originalformulierung oder Paraphrase>

Gegenargument 1: ...
Stärke: Stark/Mittel/Schwach — Begründung: ...

Gegenargument 2: ...
Stärke: Stark/Mittel/Schwach — Begründung: ...

Empfehlung: <überarbeiten / Einschränkung ergänzen / so lassen>
```

## Mehrfach-Modus (aus Plan-Modus Schritt 4)

Wenn aus `plan-modus` heraus aufgerufen: Tabelle „Kernargumente" aus `kapitelplan.draft.md` lesen (nicht aus der INSIGHT-Sammlung heraus parsen — die Tabelle ist die einzige vorgesehene Quelle, genau dafür angelegt), je Zeile 1–2 Gegenargumente, Ergebnis als Tabelle statt Einzelblöcke:

| Argument | Gegenargument | Stärke |
|---|---|---|
| ... | ... | Stark/Mittel/Schwach |

Alle Argumente mindestens **Mittel** → zurück an `plan-modus` für den Checkpoint. Sonst: an `plan-modus` zurückmelden, welche Argumente vor dem Checkpoint nachgeschärft werden müssen.

## Gesamt-Stresstest (ganze Arbeit)

Auszuführen, **sobald alle Kapitel FERTIG sind und die Gegenlesung gelaufen ist — bevor das Voll-Audit läuft**. Der `pruef-modus` prüft Regeln, der Gesamt-Stresstest prüft Argumente und Passung zur Aufgabenstellung. Inhaltliche Befunde ändern den Text — ein vorher gefahrenes Voll-Audit wäre danach hinfällig. Ein bestandenes Audit ersetzt ihn umgekehrt nie.

**Vorbedingung:** Läuft nach der `gegenlesung`. Deren Befunde in `AENDERUNGEN.md` dürfen gelesen werden — der Stresstest braucht keine kalten Augen, sondern maximale Argumentkenntnis. Doppelbefunde nicht erneut aufführen, sondern auf die Nummer der Gegenlesungs-Runde verweisen.

1. **Laden**: `aufgabe.md` (Prüfmaßstab), alle `chapters/**/*.tex` vollständig, `pruefbericht.md` nur laden, falls vorhanden (Kontext, nicht Maßstab). `kapitelplan.md` nur bei Struktur-Zweifeln.
2. **Prüfdimensionen** (jede explizit abarbeiten):
   - **Argumente**: pro Kernargument das stärkste Gegenargument eines kritischen Gutachters — besonders auf Gegenbeispiele **in den eigenen Daten/Tabellen** achten (die übersieht man beim Schreiben am leichtesten).
   - **Aufgabenstellung**: wörtliche Teilaufgaben und geforderte Berichtsinhalte aus `aufgabe.md` Punkt für Punkt abhaken, nicht sinngemäß — auch einzelne Begriffe („Medienformate", „Prototyp", „Bewertungen") müssen adressierbar sein. Zusätzlich je Teilaufgabe fragen: **Wurde sie ausgeführt oder ersetzt?** Bei Ersatz die Gegenfrage eines kritischen Gutachters vorwegnehmen — „Warum war der billigste reale Ersatz nicht möglich?" — und prüfen, ob der Text darauf eine Antwort gibt.
   - **Quellen-Overclaims**: trägt der zitierte Befund die daran geknüpfte Behauptung, oder wird aus einem deskriptiven Befund mehr gemacht?
   - **Kapitelübergreifende Konsistenz**: Zeitlinie (Entwurf ↔ Iteration), Zählungen im Text gegen Tabellen, Begriffs-Konsistenz inkl. Überschriften, Tabellenwertungen gegen Kriteriendefinition und Fließtext, semantische Korrektheit von Querverweisen. Zusätzlich: **Akteurs- und Rollenkonsistenz** (wer darf was, kapitelübergreifend gegengelesen — Ausschließlichkeitsformulierungen sind der Ansatzpunkt) und **selbst erhobene, unbeantwortete Einwände** (nennt die Arbeit eine Bedingung ihres eigenen Gelingens, ohne sie zu adressieren?).
   - **Aufbau und Formulierungen**: Kapitel-Logik, Satzanfangs-Monotonie, Dubletten, Formulierungen, die Ergebnisse präjudizieren („Ziel ist es, X zu finden").
3. **Ausgabe**: Befunde mit Stärke (Stark/Mittel/Schwach) und je Befund einer konkreten, ausführbaren Anweisung (Datei, Stelle, Formulierungsvorschlag). Zusätzlich eine nüchterne Gesamteinschätzung gegen `aufgabe.md` (Tabelle: Anforderung → Erfüllung).
4. **Persistenz ist Pflicht**: Befunde als neue Runde in `AENDERUNGEN.md` schreiben (Konvention siehe `CLAUDE.md` → Ordnerstruktur), Punkte mit These-/Kernargument-/Eigenrecherche-Bezug als **[FREIGABE]** markieren. Chat-Zusammenfassung zusätzlich, ersetzt die Datei aber nicht.
5. **Keine Umsetzung in derselben Session** — Prüfer- und Autorrolle trennen, wie beim Audit (`pruef-modus` → „Audit und Überarbeitung trennen"). Umsetzung in frischer Session: „Schreib-Modus: AENDERUNGEN.md abarbeiten", **danach das Voll-Audit** (nicht Delta-Re-Audit — es liegt noch kein Vorbericht vor). Ausnahme wie beim Einzelaufruf: Der Nutzer entscheidet über jeden Befund; ich setze nichts eigenmächtig um.

**Was dieser Skill nicht leistet:** Er liest die Arbeit gegen ihre eigene Argumentation, nicht gegen die Aufgabenstellung. Fehlende Teilaufgaben, nicht beiliegende Artefakte und unbediente Berichtsinhalte findet die `gegenlesung`, nicht dieser Skill.

## Persistenz bei Einzelaufruf

Bei Einzelaufruf (außerhalb `plan-modus` Schritt 4) wird das Ergebnis nirgends automatisch gespeichert. **Empfehlung**: das Stresstest-Ergebnis manuell festhalten — entweder als Notiz in `kapitelplan.draft.md` (im `## INSIGHT-Sammlung`-Block unter einem neuen Tag wie `[stresstest:<argument-slug>]`), als Kommentar im `.tex`-Code (`% TODO: Gegenargument X entkräften`), oder im laufenden Chat. Sonst geht die Stresstest-Einschätzung beim nächsten Sessionstart verloren.

## Wichtig

Dieser Skill liefert Gegenargumente und Stärke-Einschätzungen — er liefert nicht die überarbeitete inhaltliche Position selbst. Die Entscheidung, wie auf ein Gegenargument reagiert wird, bleibt beim Nutzer.
