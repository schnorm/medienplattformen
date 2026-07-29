# Format `AENDERUNGEN.md` (verbindlich)

Gilt für alle Skills, die die Datei schreiben oder abarbeiten: `gegenlesung` und `stresstest` (Gesamt-Stresstest) hängen Runden an, `schreib-modus` arbeitet sie ab. Bewusst nicht in `CLAUDE.md` – dieses Format wird nur in diesen drei Session-Typen gebraucht, `CLAUDE.md` aber in jeder Session geladen.

Die Datei sammelt Änderungsaufträge in **Runden**. **Jeder Prüflauf hängt genau eine Runde an** – nicht jede Sitzung: Läuft in einer Sitzung mehr als einer (etwa eine Vollgegenlesung und danach eine zugeschnittene Runde auf Wunsch), trägt jede Runde ihren **Umfang im Titel**. Ohne das kann `schreib-modus` beim Abarbeiten nicht unterscheiden, ob eine Runde die ganze Arbeit abgedeckt hat oder einen Ausschnitt – und davon hängt ab, ob danach ein Voll-Audit oder ein Delta-Re-Audit fällig ist. Abgearbeitete Punkte wandern ins Erledigt-Log, statt gelöscht zu werden.

```markdown
# Änderungsaufträge

## Offen

### Runde <N> – <Quelle: Gegenlesung / Gesamt-Stresstest / Nutzer-Feedback> (<Datum>)
**Umfang:** vollständig | zugeschnitten auf <Thema>

#### <N>.1 <Kurztitel des Befunds>  [FREIGABE]
- **Befund**: <was steht da bzw. was fehlt – mit Datei und Stelle>
- **Warum**: <Bewertungsbezug, keine Geschmacksfrage>
- **Anweisung**: <konkret ausführbar; bei mehreren Wegen als benannte Optionen>
- **Stärke**: Stark / Mittel / Schwach   (nur bei Stresstest-Befunden)

#### <N>.2 …

#### Bitte manuell prüfen
- **<was zu prüfen ist>** – wo: <Datei, Zeile, Quelle, Seite> · woran erkennbar: <Kriterium> ·
  warum nicht durch mich: <Grund> · **wenn ungeprüft, gilt:** <die Option, die dann greift>

#### Erneut gesehen, bewusst verworfen
- <Anforderung> – verworfen am <Datum>, weil <Begründung> (siehe `verworfen.md`). Keine Anweisung.

## Erledigt

### Runde <N-1> – <Quelle> (<Datum>, abgearbeitet am <Datum>)
- <N-1>.1 <Kurztitel> – umgesetzt als: <was tatsächlich geändert wurde>
- <N-1>.2 <Kurztitel> – verworfen, weil: <Begründung des Nutzers>
```

**„Bitte manuell prüfen" ist Pflichtbestandteil jeder prüfenden Runde**, auch wenn sie nur einen Punkt enthält – `CLAUDE.md` → Grundprinzipien verlangt sie global („Unsicherheit wird zur Prüfaufgabe für den Nutzer, nicht zur Fußnote"), und ein fester Ort im Format sorgt dafür, dass `schreib-modus` sie beim Abarbeiten immer an derselben Stelle findet. Die fünfte Angabe – **was gilt, wenn die Prüfung unterbleibt** – ist der Unterschied zwischen einer Prüfaufgabe und einer offenen Frage; ohne sie steht die Überarbeitung vor zwei Wegen ohne Entscheidungsgrundlage.

**Regeln:** `[FREIGABE]` markiert alles, was These, Kernargumente, Leitfrage, Zielgruppendefinition oder eigene Rechercheergebnisse berührt – solche Punkte werden im `schreib-modus` **aktiv per `AskUserQuestion` geklärt**, nie stillschweigend übersprungen (siehe `CLAUDE.md` → Grundprinzipien). „Offen" ist leer, bevor ein Voll-Audit gefahren wird. Die Verlaufsdarstellung des Projekts steht ausschließlich im Erledigt-Log – nicht in „Aktuelle Richtung".
