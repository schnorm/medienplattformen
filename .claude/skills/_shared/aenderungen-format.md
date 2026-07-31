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
- **Mitbetroffen**: <Stellen, die derselbe Arbeitsgang mit anpassen muss – entfällt, wenn der Befund wirklich lokal ist>
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

### Cold-Reading (<Datum>)
- <Kurztitel des Funds> – umgesetzt als: <was tatsächlich geändert wurde>
- <Kurztitel des Funds> – bewusst nicht geändert, weil: <Begründung des Nutzers>
```

**„Bitte manuell prüfen" ist Pflichtbestandteil jeder prüfenden Runde**, auch wenn sie nur einen Punkt enthält – `CLAUDE.md` → Grundprinzipien verlangt sie global („Unsicherheit wird zur Prüfaufgabe für den Nutzer, nicht zur Fußnote"), und ein fester Ort im Format sorgt dafür, dass `schreib-modus` sie beim Abarbeiten immer an derselben Stelle findet. Die fünfte Angabe – **was gilt, wenn die Prüfung unterbleibt** – ist der Unterschied zwischen einer Prüfaufgabe und einer offenen Frage; ohne sie steht die Überarbeitung vor zwei Wegen ohne Entscheidungsgrundlage.

**„Mitbetroffen" bestimmt die `[FREIGABE]`, nicht der Kurztitel.** Eine Sachkorrektur an einer Wertung oder Einstufung bleibt fast nie lokal: Sie zieht den deckenden Fließtextsatz, die daraus abgeleiteten Aussagen (Lücken-Satz, Alleinstellungsmerkmal, Fazit) und meist einen **Zwilling in der Einleitung** nach sich, wo dieselbe Behauptung eine Ebene grundsätzlicher steht. Wer die Kette erst beim Umsetzen entdeckt, hat die Freigabe schon verpasst – trägt **eine** der mitbetroffenen Stellen ein Kernargument, ist der ganze Punkt `[FREIGABE]`, auch wenn der Auslöser eine harmlose Detailkorrektur war. Deshalb wird die Kette in der prüfenden Runde bestimmt, nicht in der abarbeitenden.

**Cold-Reading bekommt keine Runde, sondern nur einen Erledigt-Block** (`CLAUDE.md` → „Cold-Reading"). Es ist kein Prüflauf mit Fundliste, sondern ein Dialog, in dem sofort entschieden und geändert wird – eine „## Offen"-Runde wäre schon beim Anlegen leer. Der Block ist trotzdem Pflicht: Ohne ihn hat eine bewusst getroffene Entscheidung keine Spur, und die nächste kalte Runde meldet dieselbe Stelle erneut. Punkte, die nicht geändert wurden, gehören zusätzlich nach `verworfen.md`, damit die `gegenlesung` sie unter „Erneut gesehen, bewusst verworfen" wiederfindet.

**Regeln:** `[FREIGABE]` markiert alles, was These, Kernargumente, Leitfrage, Zielgruppendefinition oder eigene Rechercheergebnisse berührt – solche Punkte werden im `schreib-modus` **aktiv per `AskUserQuestion` geklärt**, nie stillschweigend übersprungen (siehe `CLAUDE.md` → Grundprinzipien). „Offen" ist leer, bevor ein Voll-Audit gefahren wird. Die Verlaufsdarstellung des Projekts steht ausschließlich im Erledigt-Log – nicht in „Aktuelle Richtung".
