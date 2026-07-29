---
name: gegenlesung
description: Liest eine fertige wissenschaftliche Arbeit mit dem Blick einer Prüferin oder eines Prüfers, die den Text zum ersten Mal sehen und den Entstehungskontext nicht kennen. Prüft ausschließlich gegen die Aufgabenstellung und den Text selbst – Kapitelplan, Projektstatus, Prüfbericht und Änderungshistorie werden bewusst nicht gelesen. Nutzen, sobald alle Kapitel FERTIG sind, vor Gesamt-Stresstest und Voll-Audit. Findet vor allem Abwesenheiten wie nicht ausgeführte Teilaufgaben, fehlende Artefakte, unbeantwortete Anforderungen und stillschweigende Verengungen – also das, was ein kontextreicher Audit strukturell übersieht.
---

# Prüfer-Gegenlesung

## Zweck

Der `pruef-modus` prüft, ob das Geschriebene den Regeln entspricht. Der `stresstest` prüft, ob die Argumente tragen. Dieser Skill prüft, **ob die Arbeit die gestellte Aufgabe erfüllt** – aus der Sicht einer Person, die nur die Aufgabenstellung und den fertigen Text vor sich hat.

Der Unterschied ist nicht die Gründlichkeit, sondern die Blickrichtung. Wer den Kapitelplan kennt, liest die Arbeit gegen den Plan und findet Abweichungen. Wer ihn nicht kennt, liest sie gegen die Aufgabenstellung und findet Lücken. Lücken sind die teureren Befunde, weil sie sich nicht durch Umformulieren beheben lassen.

## Ladevorschrift – die Inversion

**Zu lesen, ausschließlich:**
- `aufgabe.md` – der einzige Maßstab.
- alle `chapters/**/*.tex` vollständig.
- `pages/appendix.tex`, `pages/acronyms.tex` und `pages/chapters.tex` – Anhang und Einbindung gehören zur Arbeit.
- `references.bib` **vollständig, inklusive Inhalt** (Autor, Jahr, Typ, Seitenbereich) – die Angaben werden für die Locator-Achse in Prüferfrage 3 gebraucht.
- Die Volltexte in `sources/literature/` – **aber nur für die Zitationen, deren Aussage die Lesung in Zweifel zieht**, nicht als Vollprüfung aller Stellen. Der lückenlose Abgleich ist `pruef-modus` Teil-Check G; hier geht es um die einzelne Stelle, an der der Trägersatz mehr verspricht, als er einlöst.

**Ausdrücklich NICHT zu lesen, auch nicht „kurz zur Orientierung":**
- `kapitelplan.md`, `kapitelplan.draft.md`
- `pruefbericht.md`
- `AENDERUNGEN.md` (auch nicht das Erledigt-Log)
- `MEMORY.md`, `PERSISTENT.md`
- `CLAUDE.md` → „Aktueller Projektstatus" und „Aktuelle Richtung"
- **`quellencheck.md` und `quellencheck-state.json`**, und `check_quellentreue.py` wird hier **nicht ausgeführt**. Beide enthalten die Urteile früherer Läufe; wer sie liest, prüft nicht mehr, sondern bestätigt. Das ist besonders heikel, weil ein dortiges `FUNDSTELLE OK` nur besagt, dass der Wortlaut an der Stelle steht – genau die Frage, die diese Lesung *nicht* stellt.

`CLAUDE.md` wird beim Sessionstart automatisch geladen; das lässt sich nicht verhindern. **Statustabelle und „Aktuelle Richtung" sind für diesen Skill dennoch als nicht vorhanden zu behandeln** – kein Rückgriff darauf, weder für den Stand noch für die Frage, was in früheren Runden schon geprüft wurde. Was dort steht, ist die Sicht der Autorenschaft; genau die soll hier nicht wirken.

**Ausführung: standardmäßig über einen Subagenten.** `CLAUDE.md` wird in jeder Sitzung automatisch geladen, und je länger ein Projekt läuft, desto mehr Autorensicht steht darin. Eine kalte Lesung ist in der Hauptsession dann nicht mehr simulierbar – „behandle das als nicht vorhanden" ist ab einer gewissen Menge keine ausführbare Anweisung mehr. Deshalb: Auftrag per `Agent`-Tool, Brief nach der Vorlage in `_shared/gegenlesung-subagent-brief.md`. Direkt in der Hauptsession lesen ist nur zulässig, solange der Projektstatus wenige Zeilen umfasst – und auch dann nur, wenn in dieser Sitzung noch nicht geschrieben oder geprüft wurde. (Wächst der Statusabschnitt über die Zeilen der Statustabelle hinaus, ist das zugleich ein Verstoß gegen `CLAUDE.md` → „eine Komponente = eine Zeile, überschreiben, nie anhängen" und gehört behoben.)

## Ablauf

### Schritt 1 – Erwartung vor Exposition

**Vorlauf: einmal nach Prüfkontext fragen, der nicht in `aufgabe.md` steht.** Eine `AskUserQuestion` vor der Erwartungsbildung – Abgabezeitpunkt beziehungsweise Projektwoche, bekannte Schwerpunkte der prüfenden Person, Vorgaben aus Sprechstunde. Ohne Abgabezeitpunkt existiert für jede Zeitaussage der Arbeit kein Maßstab; eine Phasenplanung, die etwas als „bevorstehend" ankündigt, während es bei Abgabe längst laufen müsste, ist ohne diese Angabe nicht als Befund erkennbar. Keine Antwort ist eine gültige Antwort. Die Antwort geht als Zusatzprämisse in den Subagenten-Brief und wird in der Runde als eigener Prüfabschnitt geführt.

**Dann zuerst nur `aufgabe.md` lesen, den Text noch nicht.** Daraus schriftlich festhalten, bevor eine einzige `.tex`-Datei geöffnet wird:

- Welche Teilaufgaben gibt es, und woran wäre jede erkennbar erfüllt?
- Welche Berichtsinhalte werden wörtlich verlangt?
- Welche Objekte müsste die fertige Arbeit enthalten (Prototyp, Erhebung, Instrument, Abbildung, Anhang)?
- Welche Bewertungskriterien nennt die Aufgabenstellung, und welche Dimensionen hat jedes?
- Welche Materialien und Literaturhinweise werden genannt?

Diese Reihenfolge ist der eigentliche Mechanismus des Skills. Wer den Text zuerst liest, übernimmt seine Struktur und prüft danach nur noch, ob das Vorgefundene in sich stimmig ist. Wer die Erwartung zuerst bildet, bemerkt, was fehlt.

### Schritt 2 – Text vollständig lesen

Alle Kapitel in Lesereihenfolge, dazu Anhang und Einbindung. Beim Lesen nichts bewerten, nur notieren, wo eine Erwartung aus Schritt 1 bedient wird.

### Schritt 3 – Soll-Ist-Tabelle

| Geforderter Inhalt (wörtlich aus `aufgabe.md`) | Erfüllung |
|---|---|

Zulässige Werte: `erfüllt` · `erfüllt, aber <Einschränkung>` · `nur ersatzweise erfüllt` · `nicht erfüllt`. Jede Zeile mit Fundstelle oder ausdrücklichem Vermerk der Abwesenheit.

### Schritt 4 – Die sieben Prüferfragen

Jede einzeln abarbeiten, auch wenn sie unergiebig scheint:

1. **Existiert, was behauptet wird?** Jede Textstelle, die ein Artefakt behauptet („als Prototyp diente …", „das Formular gliedert …", „die Erhebung ergab …"), gegen den tatsächlichen Bestand prüfen. Grep-Ansatz: `Prototyp`, `Formular`, `Skizze`, `Erhebung`, `Anhang`. Behauptete und nicht beiliegende Artefakte sind schwere Befunde – sie schwächen die Aussage, statt sie zu stützen.

   **Und bei gestalteten Artefakten: zeigt das Bild, was der Text behauptet?** Existenz genügt hier nicht. Wenn die Arbeit ein Mockup, eine Konzeptskizze, einen Prototyp oder ein Interface beschreibt („der Upload-Button …", „im Profil erscheint die Einsparung …", „die Rangliste zeigt …"), muss die Abbildung diese Elemente tatsächlich enthalten. Text und Entwurf driften beim Überarbeiten auseinander: Der Text wird geschärft, das Bild bleibt stehen.
   - Bei `tikzpicture` und `pgfplots` ist der Bildinhalt Quelltext – gratis lesbar, einfach mitprüfen.
   - Bei `\includegraphics` die Bilddatei per `Read`-Tool ansehen. **Nur dort, wo es um ein gestaltetes Artefakt geht** – nicht bei Diagrammen, die aus den eigenen Daten erzeugt wurden, und nicht bei übernommenen Abbildungen aus Quellen. Sonst zahlt diese ohnehin teure Session für jede Abbildung Tokens ohne Ertrag.
   - Je Abweichung notieren, welches im Text genannte Element im Bild fehlt. **Als Anweisung immer eine von zwei Optionen nennen – Abbildung ergänzen oder Behauptung streichen.** Die Behauptung nur umzuformulieren ist keine Lösung: Sie macht aus einer Auslassung eine widerlegbare Aussage (`schreib-modus` → Text-Bild-Lücken). Das ist ein inhaltlicher Befund, kein Formfehler: Die Arbeit beschreibt etwas, das sie nicht vorlegt.
2. **Wurde eine Teilaufgabe ersetzt statt ausgeführt?** Falls ja: Steht die Begründung im Text, und beantwortet sie die naheliegende Rückfrage nach dem billigsten realen Ersatz? Saubere Kennzeichnung des hypothetischen Charakters ist nicht dasselbe wie eine Begründung.
3. **Ist jede Behauptung nachprüfbar – und trägt jede Quelle die Rolle, die der Satz ihr zuweist?** Kapitel mit Recherche- oder Analysecharakter ohne eine einzige Quellenangabe oder dokumentierte Erhebungsgrundlage sind ein Befund, unabhängig davon, wie plausibel der Inhalt wirkt. Eigenleistung entbindet nicht von Nachvollziehbarkeit.

   Der zweite Teil ist eine **andere** Frage als die des Volltextabgleichs in Teil-Check G: Der prüft, ob der Wortlaut auf der genannten Seite steht. Diese hier prüft, ob die Quelle die Behauptung in ihrer **Stärke** trägt – und sie kann nur ein kalter Leser stellen, weil sie am Absatz hängt und nicht an der Zitatzeile. Ein bestandener Teil-Check G ist dafür ausdrücklich kein Ersatz.

   Sieben Achsen, je Zitation durchgehen, die inhaltlich trägt:
   - **Deckung** – sagt die Quelle das überhaupt?
   - **Richtung** – sagt sie es in dieselbe Richtung? Der Klassiker ist die von der Studie **verworfene** Hypothese, die als Beleg benutzt wird. Das findet keine Wortlautprüfung, weil der Wortlaut ja dasteht.
   - **Reichweite** – ist die Textaussage weiter als die Quelle (Quantoren, Absolutformulierungen, „belegt" statt „stützt")?
   - **Locator** – steht es auf der genannten Seite, und passt die Seite zum `pages`-Bereich des Bib-Eintrags?
   - **Ankündigung ↔ Einlösung** – „zwei Befunde", „mehrere Studien": kommt so viel, wie angekündigt war?
   - **Attribution** – Autorname im Fließtext ohne Zitation oder umgekehrt.
   - **Anspruchsverlauf** – jede mehrfach zitierte Quelle über **alle** Fundstellen hinweg vergleichen: Ist eine spätere Behauptung stärker als eine frühere? **Die Erstnutzung setzt die Obergrenze**; Fazit und Tabellen dürfen sie nicht überschreiten. Diese Drift entsteht systematisch, weil Fazitkapitel zuletzt und aus der Erinnerung entstehen, und keine Einzelprüfung kann sie sehen – beide Stellen bestehen für sich. Vorarbeit dafür: `check_quellentreue.py --verlauf` legt die Trägersätze je Key nebeneinander (das Skript bewertet nichts, es sortiert).

   Dazu die Tabellenregel: **Eine Zitation in einer Tabellenzelle deckt nur das zuletzt genannte Element**, sofern die Zelle nichts anderes sagt. Steht davor ein zweiter Mechanismus, braucht er einen eigenen Beleg oder die Kennzeichnung als eigene Gestaltung – im Fließtext fiele das auf, in einer Zelle liest es niemand als Behauptung.

   Für die Prüfung dürfen die Volltexte in `sources/literature/` geöffnet werden, **aber nur für die Stellen, die diese Lesung in Zweifel zieht**. Keine Vollprüfung – die ist Teil-Check G.
4. **Wird ein Zentralbegriff der Aufgabenstellung stillschweigend verengt?** Verengung ist legitim, unbegründete Verengung nicht.
5. **Widerspricht sich die Arbeit in ihren eigenen Festlegungen?** Besonders bei Rollen, Zugängen und Ausschließlichkeitsformulierungen. Und: Erhebt die Arbeit einen Einwand gegen sich selbst, den sie nirgends beantwortet?
6. **Wirkt eine eigene Bewertung ergebnisorientiert?** Bekommt das Objekt, gegen das die These sich richtet, durchweg die schlechtesten Werte, ohne dass der Text diesen Anschein entkräftet?
7. **Hätte das so ein Mensch geschrieben?** Liest sich der Text wie ein KI-Aufsatz, ist das ein Befund – nicht weil KI schlecht wäre, sondern weil die Eigenständigkeitserklärung eine eigene Autorenschaft versichert und Prüfende auf genau dieses Muster achten. Anhaltspunkte: generische Formulierungen, wiederkehrende Satzbaumuster, verdichtete Pointen-Schlusssätze, fehlende eigene Reflexion. Verdächtige Stellen mit Fundstelle notieren und gegen `hard-rules-formal.md` → Schreibstil abgleichen.

   **Stilmuster werden gezählt, nicht empfunden.** Vorkommen ermitteln, um Tabellenzellen und legitime Fälle bereinigen, gegen den Richtwert in `hard-rules-formal.md` stellen und **beide Zahlen im Befund nennen** („30 Vorkommen, davon 3 in Tabellenzellen und 4 legitime Aufzählungsdoppelpunkte, bleiben 23 gegen einen Richtwert von 12"). Ein Stilbefund ohne Zahl ist eine Geschmacksäußerung, und die Überarbeitung kann nicht erkennen, wann sie fertig ist.

### Schritt 5 – Bewertungskriterien je Dimension

Jedes Kriterium aus `aufgabe.md` in seine Dimensionen zerlegen und einzeln beurteilen: `abgedeckt` · `schwach` · `fehlt`. Zwei starke Dimensionen erzeugen leicht den Eindruck, das Kriterium sei erfüllt – die dritte auszulassen ist der wahrscheinlichste Fehler.

### Schritt 6 – Ausgabe

Befunde als **neue Runde in `AENDERUNGEN.md`**, Format: `_shared/aenderungen-format.md` (jetzt laden). Je Befund:

- **Befund** – was steht da beziehungsweise was fehlt, mit Fundstelle
- **Warum ein Prüfer das anstreicht** – der Bewertungsbezug, nicht die Geschmacksfrage
- **Anweisung** – konkret, ausführbar, mit Datei und Stelle; bei mehreren gangbaren Wegen als benannte Optionen
- **`[FREIGABE]`** bei allem, was These, Kernargumente, Leitfrage, Zielgruppendefinition oder eigene Rechercheergebnisse berührt

Zusätzlich in die Runde: die Soll-Ist-Tabelle aus Schritt 3, eine nüchterne Gesamteinschätzung und ein **Umfangshinweis auf den Gesamtstand nach dieser Runde** – nicht auf das Delta.

**Datengrundlage des Umfangshinweises ist die gedruckte Seitenzahl des letzten Builds, nicht `check_umfang.py`.** Das Skript liefert die Wortzahl und damit das Delta dieser Runde; seine Seitenangabe ist erklärtermaßen eine Schätzung und liegt systematisch zu niedrig, weil sie Abbildungen, Tabellen und Float-Umbrüche nicht kennt (bis zu +1,5 Seiten). Ist der letzte Build älter als der aktuelle Textstand, gehört genau dieser Umstand in den Umfangshinweis, statt die Schätzung als Stand auszugeben. Maßstab ist die Zielgröße aus `kapitelplan.md`. Der Unterschied ist nicht akademisch – ein Hinweis „diese Runde erzwingt keine Kürzungen" kann zutreffen, während die Arbeit insgesamt längst über der Vorgabe liegt. Liegt der Gesamtstand darüber, gehört in die Runde ein eigener Punkt „Kürzen", mit konkretem Vorschlag: mehrfach ausformulierte Kernbefunde sind die erste Reserve, nicht die Belege.

**Bitte manuell prüfen – eigene Sektion am Ende der Runde**, auch wenn sie nur einen Punkt enthält. Eine Gegenlesung produziert systematisch Punkte, die sie nicht selbst entscheiden kann: die Volltextlage einer Quelle, eine gedruckte Seitenzahl, der reale Entstehungsweg einer Abbildung. Stehen sie nur als Nebensatz in einer Anweisung („am Volltext prüfen, ob …"), liest die Schreib-Session sie als eine von zwei gleichwertigen Optionen und wirft eine Münze. Je Punkt **fünf** Angaben:

1. was zu prüfen ist,
2. wo – Datei, Zeile, Quelle, Seite,
3. woran erkennbar ist, dass es stimmt,
4. warum die Gegenlesung es nicht konnte,
5. **welche Option gilt, wenn die Prüfung unterbleibt.**

Angabe (5) ist der Unterschied zwischen einer Prüfaufgabe und einer offenen Frage. Ohne sie steht die Überarbeitung vor zwei Wegen ohne Entscheidungsgrundlage.

**Rollentrennung bei der Übergabe.** Läuft die Lesung über einen Subagenten – der Regelfall –, schreibt der seinen vollständigen Bericht in eine Scratchpad-Datei und **nicht** in `AENDERUNGEN.md`: Die Datei steht auf seiner Verbotsliste, und Rundennummer wie Einhängepunkt kann nur kennen, wer sie lesen darf. Die Hauptsession überträgt den Bericht anschließend als neue Runde, **ohne Befunde zu entschärfen oder zusammenzufassen – sie ist Schreiber, nicht zweite Instanz.** Der letzte Halbsatz ist der wichtige: Die Hauptsession kennt den Entstehungskontext und ist damit die Instanz, die am ehesten geneigt ist, einen Befund „einzuordnen", der sich gegen eine Entscheidung richtet, die sie selbst getroffen hat.

**Ehrlichkeitspflicht:** Auch benennen, was gut ist – aber nicht als Trostpflaster, sondern damit die Überarbeitung weiß, was sie nicht anfassen darf. Eine Gegenlesung, die nur Mängel listet, verleitet dazu, tragende Stärken wegzuschreiben. **Jede Stilregel, die geprüft wurde und eingehalten ist, bekommt dabei einen eigenen Eintrag – mit Zahl und dem ausdrücklichen Hinweis, dass hier nichts zu tun ist.** Sonst prüft die nächste kalte Runde dieselbe Regel erneut und meldet sie als neuen Befund, und die Überarbeitung repariert etwas, das in Ordnung war.

**Erneut gesehen, bewusst verworfen** – eigene Überschrift, ohne Nummer und ohne Anweisung. Bewusst verworfene Anforderungen aus `aufgabe.md` schlagen in jeder kalten Runde erneut auf; das ist keine Schwäche der Lesung, sondern die zwangsläufige Folge ihres Designs, denn die Entscheidung liegt in `AENDERUNGEN.md` und im Projektstatus, beides Leseverbot. Deshalb: **erst hier in Schritt 6**, nach Erwartungsbildung und Textlesung, die Datei `verworfen.md` im Projekt-Root lesen (eine Zeile je verworfener Anforderung, mit Datum, Begründung und der Bedingung, unter der die Entscheidung wieder aufzumachen wäre). Was dort steht, wandert unter diese Überschrift statt in die Befundliste. So bleibt die Inversion unbeschädigt – die Lesung findet den Punkt weiterhin kalt. **Gegenprobe:** Trägt die Begründung inzwischen nicht mehr (Beispiel: „übersprungen, weil die Quelle nicht in `references.bib` steht", und sie steht inzwischen dort), wird der Punkt **doch** als Befund geführt.

### Schritt 7 – keine Umsetzung in derselben Sitzung

Prüfer- und Autorrolle trennen, wie beim Audit. Umsetzung in frischer Sitzung: „Schreib-Modus: AENDERUNGEN.md abarbeiten". Der Nutzer entscheidet über jeden Befund; nichts wird eigenmächtig umgesetzt.

## Abgrenzung zu den Nachbar-Skills

| Skill | Maßstab | Kennt den Entstehungskontext | Findet typischerweise |
|---|---|---|---|
| `gegenlesung` | `aufgabe.md` | nein (Leseverbot) | Abwesenheiten, nicht erfüllte Anforderungen |
| `stresstest` (Gesamt) | Argumentation | ja | schwache Argumente, Overclaims, Inkonsistenzen |
| `pruef-modus` | Regelwerk, Typ-Datei | ja | Formalia, Pflichtpunkte, Struktur, Build |

Keiner ersetzt einen anderen. Die Reihenfolge ist Gegenlesung → Gesamt-Stresstest → Voll-Audit, weil die Gegenlesung die kältesten Augen braucht und die strukturellsten Befunde liefert.
