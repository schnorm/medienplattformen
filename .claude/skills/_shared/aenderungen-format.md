# Format `AENDERUNGEN.md` (verbindlich)

Gilt für alle Skills, die die Datei schreiben oder abarbeiten: `gegenlesung` und `stresstest` (Gesamt-Stresstest) hängen Runden an, `schreib-modus` arbeitet sie ab. Bewusst nicht in `CLAUDE.md` — dieses Format wird nur in diesen drei Session-Typen gebraucht, `CLAUDE.md` aber in jeder Session geladen.

Die Datei sammelt Änderungsaufträge in **Runden**. Jede prüfende Sitzung hängt genau eine neue Runde an; abgearbeitete Punkte wandern ins Erledigt-Log, statt gelöscht zu werden.

```markdown
# Änderungsaufträge

## Offen

### Runde <N> — <Quelle: Gegenlesung / Gesamt-Stresstest / Nutzer-Feedback> (<Datum>)

#### <N>.1 <Kurztitel des Befunds>  [FREIGABE]
- **Befund**: <was steht da bzw. was fehlt — mit Datei und Stelle>
- **Warum**: <Bewertungsbezug, keine Geschmacksfrage>
- **Anweisung**: <konkret ausführbar; bei mehreren Wegen als benannte Optionen>
- **Stärke**: Stark / Mittel / Schwach   (nur bei Stresstest-Befunden)

#### <N>.2 …

## Erledigt

### Runde <N-1> — <Quelle> (<Datum>, abgearbeitet am <Datum>)
- <N-1>.1 <Kurztitel> — umgesetzt als: <was tatsächlich geändert wurde>
- <N-1>.2 <Kurztitel> — verworfen, weil: <Begründung des Nutzers>
```

**Regeln:** `[FREIGABE]` markiert alles, was These, Kernargumente, Leitfrage, Zielgruppendefinition oder eigene Rechercheergebnisse berührt — solche Punkte werden im `schreib-modus` **aktiv per `AskUserQuestion` geklärt**, nie stillschweigend übersprungen (siehe `CLAUDE.md` → Grundprinzipien). „Offen" ist leer, bevor ein Voll-Audit gefahren wird. Die Verlaufsdarstellung des Projekts steht ausschließlich im Erledigt-Log — nicht in „Aktuelle Richtung".
