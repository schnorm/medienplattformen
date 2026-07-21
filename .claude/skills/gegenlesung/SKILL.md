---
name: gegenlesung
description: Liest eine fertige wissenschaftliche Arbeit mit dem Blick einer Prüferin oder eines Prüfers, die den Text zum ersten Mal sehen und den Entstehungskontext nicht kennen. Prüft ausschließlich gegen die Aufgabenstellung und den Text selbst — Kapitelplan, Projektstatus, Prüfbericht und Änderungshistorie werden bewusst nicht gelesen. Nutzen, sobald alle Kapitel FERTIG sind, vor Gesamt-Stresstest und Voll-Audit. Findet vor allem Abwesenheiten: nicht ausgeführte Teilaufgaben, fehlende Artefakte, unbeantwortete Anforderungen, stillschweigende Verengungen — also das, was ein kontextreicher Audit strukturell übersieht.
---

# Prüfer-Gegenlesung

## Zweck

Der `pruef-modus` prüft, ob das Geschriebene den Regeln entspricht. Der `stresstest` prüft, ob die Argumente tragen. Dieser Skill prüft, **ob die Arbeit die gestellte Aufgabe erfüllt** — aus der Sicht einer Person, die nur die Aufgabenstellung und den fertigen Text vor sich hat.

Der Unterschied ist nicht die Gründlichkeit, sondern die Blickrichtung. Wer den Kapitelplan kennt, liest die Arbeit gegen den Plan und findet Abweichungen. Wer ihn nicht kennt, liest sie gegen die Aufgabenstellung und findet Lücken. Lücken sind die teureren Befunde, weil sie sich nicht durch Umformulieren beheben lassen.

## Ladevorschrift — die Inversion

**Zu lesen, ausschließlich:**
- `aufgabe.md` — der einzige Maßstab.
- alle `chapters/**/*.tex` vollständig.
- `pages/appendix.tex`, `pages/acronyms.tex` und `pages/chapters.tex` — Anhang und Einbindung gehören zur Arbeit.
- `references.bib` nur zur Zählung der Einträge (per Grep auf `^@`), nicht inhaltlich.

**Ausdrücklich NICHT zu lesen, auch nicht „kurz zur Orientierung":**
- `kapitelplan.md`, `kapitelplan.draft.md`
- `pruefbericht.md`
- `AENDERUNGEN.md` (auch nicht das Erledigt-Log)
- `MEMORY.md`, `PERSISTENT.md`
- `CLAUDE.md` → „Aktueller Projektstatus" und „Aktuelle Richtung"

`CLAUDE.md` wird beim Sessionstart automatisch geladen; das lässt sich nicht verhindern. **Statustabelle und „Aktuelle Richtung" sind für diesen Skill dennoch als nicht vorhanden zu behandeln** — kein Rückgriff darauf, weder für den Stand noch für die Frage, was in früheren Runden schon geprüft wurde. Was dort steht, ist die Sicht der Autorenschaft; genau die soll hier nicht wirken.

**Wenn die Sitzung bereits Kontext zur Arbeit trägt** — etwa weil vorher geschrieben oder geprüft wurde —, ist die Gegenlesung in dieser Sitzung nicht mehr durchführbar. Dann dem Nutzer eine frische Sitzung vorschlagen, statt eine kalte Lesung zu simulieren, die keine ist. Alternativ per `Agent`-Tool an einen Subagenten übergeben, der die Ladevorschrift oben als Auftrag erhält.

## Ablauf

### Schritt 1 — Erwartung vor Exposition

**Zuerst nur `aufgabe.md` lesen, den Text noch nicht.** Daraus schriftlich festhalten, bevor eine einzige `.tex`-Datei geöffnet wird:

- Welche Teilaufgaben gibt es, und woran wäre jede erkennbar erfüllt?
- Welche Berichtsinhalte werden wörtlich verlangt?
- Welche Objekte müsste die fertige Arbeit enthalten (Prototyp, Erhebung, Instrument, Abbildung, Anhang)?
- Welche Bewertungskriterien nennt die Aufgabenstellung, und welche Dimensionen hat jedes?
- Welche Materialien und Literaturhinweise werden genannt?

Diese Reihenfolge ist der eigentliche Mechanismus des Skills. Wer den Text zuerst liest, übernimmt seine Struktur und prüft danach nur noch, ob das Vorgefundene in sich stimmig ist. Wer die Erwartung zuerst bildet, bemerkt, was fehlt.

### Schritt 2 — Text vollständig lesen

Alle Kapitel in Lesereihenfolge, dazu Anhang und Einbindung. Beim Lesen nichts bewerten, nur notieren, wo eine Erwartung aus Schritt 1 bedient wird.

### Schritt 3 — Soll-Ist-Tabelle

| Geforderter Inhalt (wörtlich aus `aufgabe.md`) | Erfüllung |
|---|---|

Zulässige Werte: `erfüllt` · `erfüllt, aber <Einschränkung>` · `nur ersatzweise erfüllt` · `nicht erfüllt`. Jede Zeile mit Fundstelle oder ausdrücklichem Vermerk der Abwesenheit.

### Schritt 4 — Die sieben Prüferfragen

Jede einzeln abarbeiten, auch wenn sie unergiebig scheint:

1. **Existiert, was behauptet wird?** Jede Textstelle, die ein Artefakt behauptet („als Prototyp diente …", „das Formular gliedert …", „die Erhebung ergab …"), gegen den tatsächlichen Bestand prüfen. Grep-Ansatz: `Prototyp`, `Formular`, `Skizze`, `Erhebung`, `Anhang`. Behauptete und nicht beiliegende Artefakte sind schwere Befunde — sie schwächen die Aussage, statt sie zu stützen.
2. **Wurde eine Teilaufgabe ersetzt statt ausgeführt?** Falls ja: Steht die Begründung im Text, und beantwortet sie die naheliegende Rückfrage nach dem billigsten realen Ersatz? Saubere Kennzeichnung des hypothetischen Charakters ist nicht dasselbe wie eine Begründung.
3. **Ist jede Behauptung nachprüfbar?** Kapitel mit Recherche- oder Analysecharakter ohne eine einzige Quellenangabe oder dokumentierte Erhebungsgrundlage sind ein Befund, unabhängig davon, wie plausibel der Inhalt wirkt. Eigenleistung entbindet nicht von Nachvollziehbarkeit.
4. **Wird ein Zentralbegriff der Aufgabenstellung stillschweigend verengt?** Verengung ist legitim, unbegründete Verengung nicht.
5. **Widerspricht sich die Arbeit in ihren eigenen Festlegungen?** Besonders bei Rollen, Zugängen und Ausschließlichkeitsformulierungen. Und: Erhebt die Arbeit einen Einwand gegen sich selbst, den sie nirgends beantwortet?
6. **Wirkt eine eigene Bewertung ergebnisorientiert?** Bekommt das Objekt, gegen das die These sich richtet, durchweg die schlechtesten Werte, ohne dass der Text diesen Anschein entkräftet?
7. **Hätte das so ein Mensch geschrieben, oder wirkt es wie ein KI-Text?** Wenn letzteres, ist das ein Befund — nicht, weil KI schlecht ist, sondern weil die Aufgabenstellung eine menschliche Autorenschaft verlangt. Achte darauf, dass die Arbeit nicht nur inhaltlich, sondern auch stilistisch wie ein menschlicher Text wirkt. KI-typische Muster (z. B. übermäßige Wiederholungen, generische Formulierungen, fehlende persönliche Reflexion) sind zu notieren. Gleiche die Muster mit `hard-rules-formal.md` ab, um zu prüfen, ob sie gegen die formalen Anforderungen verstoßen. Wenn du den Eindruck hast, dass KI-Text vorliegt, markiere die entsprechenden Stelle und schlage dem User vor, diese zu überarbeiten, um den menschlichen Schreibstil zu gewährleisten.

### Schritt 5 — Bewertungskriterien je Dimension

Jedes Kriterium aus `aufgabe.md` in seine Dimensionen zerlegen und einzeln beurteilen: `abgedeckt` · `schwach` · `fehlt`. Zwei starke Dimensionen erzeugen leicht den Eindruck, das Kriterium sei erfüllt — die dritte auszulassen ist der wahrscheinlichste Fehler.

### Schritt 6 — Ausgabe

Befunde als **neue Runde in `AENDERUNGEN.md`**, Konvention wie in `CLAUDE.md` → Ordnerstruktur. Je Befund:

- **Befund** — was steht da beziehungsweise was fehlt, mit Fundstelle
- **Warum ein Prüfer das anstreicht** — der Bewertungsbezug, nicht die Geschmacksfrage
- **Anweisung** — konkret, ausführbar, mit Datei und Stelle; bei mehreren gangbaren Wegen als benannte Optionen
- **`[FREIGABE]`** bei allem, was These, Kernargumente, Leitfrage, Zielgruppendefinition oder eigene Rechercheergebnisse berührt

Zusätzlich in die Runde: die Soll-Ist-Tabelle aus Schritt 3, eine nüchterne Gesamteinschätzung und ein Umfangshinweis, falls Zugaben Kürzungen erzwingen.

**Ehrlichkeitspflicht:** Auch benennen, was gut ist — aber nicht als Trostpflaster, sondern damit die Überarbeitung weiß, was sie nicht anfassen darf. Eine Gegenlesung, die nur Mängel listet, verleitet dazu, tragende Stärken wegzuschreiben.

### Schritt 7 — keine Umsetzung in derselben Sitzung

Prüfer- und Autorrolle trennen, wie beim Audit. Umsetzung in frischer Sitzung: „Schreib-Modus: AENDERUNGEN.md abarbeiten". Der Nutzer entscheidet über jeden Befund; nichts wird eigenmächtig umgesetzt.

## Abgrenzung zu den Nachbar-Skills

| Skill | Maßstab | Kennt den Entstehungskontext | Findet typischerweise |
|---|---|---|---|
| `gegenlesung` | `aufgabe.md` | nein (Leseverbot) | Abwesenheiten, nicht erfüllte Anforderungen |
| `stresstest` (Gesamt) | Argumentation | ja | schwache Argumente, Overclaims, Inkonsistenzen |
| `pruef-modus` | Regelwerk, Typ-Datei | ja | Formalia, Pflichtpunkte, Struktur, Build |

Keiner ersetzt einen anderen. Die Reihenfolge ist Gegenlesung → Gesamt-Stresstest → Voll-Audit, weil die Gegenlesung die kältesten Augen braucht und die strukturellsten Befunde liefert.
