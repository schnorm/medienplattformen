# Vorlagen für Draft und finalen Plan (Referenz zu plan-modus)

Enthält beide Strukturen: `kapitelplan.draft.md` (Checkpoints während der Planung) und `kapitelplan.md` (finaler Plan). Beim ersten Checkpoint laden und bis zum Sessionende offen halten.

### Format `kapitelplan.draft.md`

```markdown
# Kapitelplan (Entwurf – in Bearbeitung)

## Status
Betriebsart: kompakt / ausführlich
Zuletzt abgeschlossen: Schritt <N> – <Name>
Nächster Schritt: Schritt <N+1> – <Name>
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

## Kernargumente (laufend befüllt in Schritt 3 – einzige Lesequelle für Stresstest)
| Kapitel | Kernargument |
|---|---|
| ... | ... |

## Stresstest-Ergebnisse (sobald Schritt 4 erreicht)
| Argument | Stärke | Begründung |
|---|---|---|
```

**Checkpoint-Regel (append-only)**: Nach jedem Schritt (0, 1, 2, 2.5, jedem einzelnen Kapitel in Schritt 3, 4 – im Kompakt-Modus nach jeder gebündelten Runde) `kapitelplan.draft.md` **per Edit** aktualisieren – nicht per Vollrewrite. Konkret:
- Nur den `## Status`-Block per Edit anpassen (nächster Schritt, Datum).
- Neue INSIGHT-Einträge an die bestehende `## INSIGHT-Sammlung` anhängen.
- Neue Kapitelzeilen an die bestehenden Tabellen (`## Kapitelgerüst`, `## Kernargumente`, `## Stresstest-Ergebnisse`) anhängen.
- So bleibt jeder Checkpoint klein (~200–400 Tokens Edit-Größe), unabhängig von der Gesamtlänge des Drafts – kein quadratischer Tokenverbrauch über die Session.

**Zusätzlich** `CLAUDE.md` → „Aktueller Projektstatus" nach der dort hinterlegten Update-Regel aktualisieren (bestehende Zeile überschreiben, Platzhalter bei Schritt 2.5 durch echte `sec:<slug>`-Einträge ersetzen, „Aktuelle Richtung" auf den nächsten Schritt setzen).

**Sichtbarkeitspflicht**: Jeder Checkpoint wird im Chat kurz quittiert, nicht nur still in die Datei geschrieben – z. B. „✅ Checkpoint gespeichert: Schritt 2 (These) abgeschlossen, weiter mit Schritt 2.5. Projektstatus in CLAUDE.md aktualisiert." Ohne diese Zeile hat der Nutzer keine Möglichkeit zu erkennen, ob das Schreiben der Datei tatsächlich stattgefunden hat (z. B. bei einem stillen Schreibfehler).

---

## Output: `kapitelplan.md` erzeugen

Alle Inhalte liegen bereits in `kapitelplan.draft.md` (Checkpoints aus Schritt 0–4). Dieser letzte Schritt konsolidiert sie nur noch zur finalen Datei – es müssen keine Inhalte neu erfragt werden.

1. `kapitelplan.draft.md` vollständig lesen.
2. Daraus `kapitelplan.md` **im Projekt-Root** nach dem Format unten schreiben (Schreib-Modus liest später nur diese Datei, nicht den Draft). `kapitelplan.md` enthält bewusst **keine** vollständige INSIGHT-Sammlung – die ist im Draft archiviert und blockiert sonst den Schreib-Modus-Token-Budget mit Ballast.
3. **Output-Integritätscheck (Pflicht, vor Fertigstellung):** Output ⊇ Draft-Entscheidungen prüfen. Jede bestätigte Zuordnung aus dem Draft – Abhakliste-Einträge, Lieferobjekte, im INSIGHT bestätigte Feature-/Begriffs-Ideen – muss im finalen `kapitelplan.md` einen erkennbaren Ort haben. Dazu jede `[INSIGHT: ...]`-Zeile und jede Tabellenzeile aus dem Draft gegen den geschriebenen Output abgleichen (Grep-artig, Begriff für Begriff). Fehlt einer, entweder ergänzen oder bewusst mit einem Satz Begründung streichen – nicht stillschweigend verlieren. Anlass: „Journaling/Menüplanung" fiel bei einer Konsolidierung so heraus, obwohl im Draft zugeordnet.
4. `kapitelplan.draft.md` **nicht löschen** – stattdessen mit Hinweis markieren:
   ```markdown
   # Kapitelplan (Entwurf – abgeschlossen)
   ## Status
   Zuletzt abgeschlossen: Output – siehe kapitelplan.md
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
- **Belege**: ... (je Quelle mit Zitier-Klassifikation `[zitiert]` / `[eigene Analyse]` / `[unzulässig – ersetzt durch ...]`)
- **Gegenargumente**: ...
- **Antwort**: ...
- **Argumentationsstärke**: Stark/Mittel (kompakt ohne Stresstest: „ungeprüft")
- **Faktenbasis**: Literatur / eigene Recherche / eigene Konzeptleistung
- **Rechercheprotokoll** (nur bei eigener Recherche): <Behauptung> – <Quelle> – <Datum> – <Beobachtungsmerkmal>
- **Lieferobjekte**: <Abbildung/Tabelle/Anhang> – <Bezeichnung> – <Zielort> (nur wenn zugeordnet)
- **Rubrik-Karte** (nur bei eigener Bewertungsmatrix):
  | Kriterium | Art (Merkmal/Gesamturteil) | misst | stark = | mittel = | schwach = | NICHT gemeint |
  |---|---|---|---|---|---|---|

### Subsection: <nn>_<slug> – <Titel>
- **Argumentationsfluss**: <1 Satz>
- **Inhaltspunkte**:
  - <Punkt 1>
  - <Punkt 2>
  - <...>

### Subsection: <nn>_<slug> – <Titel>
- **Argumentationsfluss**: ...
- **Inhaltspunkte**:
  - ...

[... alle Kapitel aus dem in Schritt 2.5 bestätigten Skelett, inkl. Einleitung/Schluss-Blöcken ...]

## Literaturliste (nur wenn Schritt 1 durchgeführt)
### Priority Reading Order
1. <Titel> – <Autoren>, <Journal>, <Jahr> (citations: <N>) – <Consensus-URL>

### Forschungslücken (für Theorie & Argumentation)
- ...

## Zitat-Kandidaten (nur falls Volltexte bereits geprüft wurden, siehe Schritt 3 → Recherche-Gate)
| Paper | Seite | Fundstelle (paraphrasiert/Zitat) | Verwendungszweck (Subsection) |
|---|---|---|---|
| ... | ... | ... | ... |

Hinweis: Recherche-Vorarbeit – Nutzer prüft Seitenzahlen/Formulierungen final am Original (IU-KI-Richtlinie).

## Nächste Schritte
→ pruef-modus (Umfang „Plan-Audit"): Kapitelplan auf Kohärenz prüfen – **empfohlen** vor dem Schreiben, **Pflicht** ab > 3 Kapiteln oder eigener Vergleichsmatrix/Rubrik-Karte
→ pruef-modus (Umfang „Bereitschafts-Check"): mechanische Checkliste direkt vor dem ersten schreib-modus-Aufruf – **empfohlen**
→ danach schreib-modus: Kapitel nacheinander verfassen
```
