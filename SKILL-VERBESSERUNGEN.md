# Skill-Verbesserungen (Befunde aus dieser Session, 2026-07-24)

Reflexion über Muster in diesem Projekt, die auf Lücken im Skill-Framework selbst hindeuten — nicht projektspezifisch, sondern relevant für alle künftigen Arbeiten mit `plan-modus`/`schreib-modus`/`pruef-modus`/`gegenlesung`/`stresstest`. Noch nicht umgesetzt, nur festgehalten.

## 1. `typen/projektbericht.md` erzwingt „Projektgruppe" ohne Ausnahme

**Befund**: [`.claude/skills/_shared/typen/projektbericht.md:42`](.claude/skills/_shared/typen/projektbericht.md) schreibt hart vor: „Voice: 3. Person streng: „Die Projektgruppe …" — keine Ausnahme." Kein Zweig für Einzelarbeit. Zum Vergleich nutzen `hausarbeit.md`, `fallstudie.md` und `seminararbeit.md` bereits durchgehend pronomenfreie Formulierungen („Diese Arbeit zeigt…", „Im vorliegenden Fall…") — nur `projektbericht.md` geht unconditional von einer Gruppe aus.

**Auswirkung in diesem Projekt**: „Projektgruppe" erschien an 16 Stellen über mehrere Kapitel, obwohl es sich laut `sources/Anmerkungen vom Prüfer.md` um eine Einzelarbeit handelt („Du bist also Projektverantwortliche"). Der Fehler überlebte Plan-Modus, Schreib-Modus, Gegenlesung und sogar das Voll-Audit (Score 100/100) — weil die Skill-Datei selbst die falsche Vorgabe machte; kein Check konnte dagegen prüfen.

**Vorgeschlagener Fix**:
- `plan-modus` Schritt 0 (Readiness-Check) um eine Frage/Extraktion „Einzelarbeit oder Gruppenarbeit?" ergänzen, Ergebnis als Feld in `aufgabe.md` festhalten.
- `typen/projektbericht.md` → Voice-Regel verzweigen: Gruppe → „Die Projektgruppe…", Einzelperson → pronomenfreier Selbstbezug („diese Arbeit"/„dieser Bericht").
- Optional: `check_formalia.py` um eine Heuristik ergänzen, die bei `Autorenschaft: Einzelperson` auf „Projektgruppe"/„Team" grept.

## 2. Kein Check vergleicht Abbildungsinhalt gegen Textbehauptungen

**Befund**: `pruef-modus` Teil-Check A prüft bei Abbildungen nur Formales ([`.claude/skills/pruef-modus/SKILL.md:75`](.claude/skills/pruef-modus/SKILL.md): `\quelle{}`, kein `\cite{}`, Beschriftung über dem Bild) — nie den tatsächlichen Bildinhalt gegen Aussagen im Fließtext. `gegenlesung` kommt am nächsten (Frage 1: „Existiert, was behauptet wird?"), prüft aber nur *Existenz* des Artefakts, nicht ob es die behauptete Funktion tatsächlich *zeigt*.

**Auswirkung in diesem Projekt**: Drei Lücken zwischen Mockup und Text (fehlender Upload-Button, fehlende Einsparangabe im Profil, fehlende Challenges/Rangliste im Feed) waren bereits vor Gegenlesung und Voll-Audit im Text vorhanden. Keiner der beiden Checks fand sie, weil keiner das Bild tatsächlich liest — die Lücken kamen erst durch gezielte Nachfrage im Chat ans Licht.

**Vorgeschlagener Fix**:
- `gegenlesung/SKILL.md` Frage 1 erweitern: „Bei Abbildungen: zeigt das Bild tatsächlich, was der Text behauptet — nicht nur, ob die Datei existiert" (per `Read`-Tool aufs Bild selbst, nicht nur die Caption).
- `pruef-modus` Teil-Check A um denselben Punkt als Pflicht ergänzen, wenn Mockups laut Typ-Datei ein Lieferobjekt sind (bei Projektbericht der Fall).

## 3. Feinkörnige Wirkungsbehauptungen werden nirgends geprüft

**Befund**: Zwei Formulierungen im Text behaupteten mehr, als der beschriebene Mechanismus tatsächlich trägt — „ein solcher Fokus wäre eher ein Hindernis als ein Mehrwert" (Prämisse trug nur „kein Mehrwert") und „das Reste-Level macht sichtbar, wie viele Zutaten gerettet wurden" (tatsächlich zeigt das der Rettungspunkte-Zähler, nicht das Level). Genau dieses Muster prüft `stresstest`. Laut `CLAUDE.md` → „Kompakt-Prüfkette" ist der Gesamt-Stresstest bei Projektbericht aber standardmäßig übersprungen, und `gegenlesung` prüft laut eigener Beschreibung „vor allem Abwesenheiten", nicht die Präzision einzelner Wirkungsaussagen.

**Auswirkung in diesem Projekt**: Beide Fehler fielen nur auf, weil im Chat zufällig gezielt nachgefragt wurde — kein Skill-Schritt hätte sie strukturell gefunden.

**Vorgeschlagener Fix** (bewusst vorsichtig, da er die absichtliche Kompakt-Architektur berührt statt sie zu ersetzen): `pruef-modus` Teil-Check B um einen gezielten, günstigen Punkt ergänzen: „Für jede Kausal-/Wirkungsaussage (,X macht sichtbar/bewirkt/zeigt Y'): Liefert der beschriebene Mechanismus tatsächlich Y, oder eine benachbarte, nicht deckungsgleiche Eigenschaft?" — kein voller Gesamt-Stresstest, aber ein gezielter Blick auf genau dieses Fehlermuster.

## 4. Der Workflow kennt keinen Schritt, dessen Ergebnis negativ ist

**Befund**: Jede Station des Fahrplans in `CLAUDE.md` produziert **Zugaben**. `gegenlesung` findet laut eigener Beschreibung „vor allem Abwesenheiten" — also Dinge, die fehlen und ergänzt werden müssen. `stresstest` erzeugt Gegenargumente, die im Text vorweggenommen und entkräftet werden. `pruef-modus` liefert Handlungsempfehlungen, die fast durchweg auf Präzisieren und Ergänzen hinauslaufen. Kein einziger Schritt hat als definiertes Ergebnis: „Dieser Absatz kann weg."

Das ist einzeln jeweils richtig — in Summe entsteht ein einseitiger Prozess. In diesem Projekt haben drei Qualitätsrunden (Gegenlesung, Gesamt-Stresstest, Prüfbericht) über den Textstand hinweg rund 700 Wörter defensive Redundanz aufgebaut: derselbe Kernbefund fünfmal ausformuliert, der „kein Nutzertest"-Vorbehalt an sieben Stellen, ein 216-Wörter-Absatz mit vier Einwänden, von denen drei den eigenen Fließtext desselben Kapitels wiederholen und dies mit „wie oben gezeigt" sogar selbst zugeben. Jede dieser Stellen ist einzeln als Reaktion auf einen berechtigten Befund entstanden. Keine Instanz hat je den akkumulierten Stand angeschaut.

**Der schärfste Beleg**: `gegenlesung/SKILL.md:83` verlangt „einen Umfangshinweis, falls Zugaben Kürzungen erzwingen". Der Hinweis blickt also ausschließlich auf das, was *diese Runde* hinzufügt. Entsprechend steht am Ende von Runde 3 in `AENDERUNGEN.md`: „Bei 7–10 Seiten Zielkorridor entsteht **kein Kürzungsdruck**." Das war für die Zugaben dieser Runde korrekt und für die Arbeit insgesamt falsch — der Textteil lag zu diesem Zeitpunkt bereits schätzungsweise bei 10–11 Seiten.

**Vorgeschlagener Fix**: Kein neuer Modus. Zwei kleine Eingriffe genügen:
- `gegenlesung/SKILL.md:83` umformulieren: Der Umfangshinweis bezieht sich auf den **Gesamtumfang nach der Runde**, nicht auf das Delta. Datengrundlage ist die Gesamt-Wortzahl aus `check_formalia.py` (siehe Befund 5), nicht eine Schätzung.
- `pruef-modus` Teil-Check B: Der Redundanz-Check existiert dort bereits, aber zu eng (`pruef-modus/SKILL.md:133` prüft ausschließlich „Redundanz zwischen Reflexion und Fazit"). Auf den ganzen Text ausweiten: „Steht ein zentraler Befund an mehr als zwei Stellen ausformuliert? Erstnennung und Fazit-Paraphrase sind zulässig, alles darüber ist Kürzungsreserve." `hard-rules-formal.md:88` formuliert die Regel bereits — sie hat nur keinen Prüfschritt, der auf sie zeigt.

## 5. Die Umfangsprüfung hängt vollständig am Build — der hier nie lief

**Befund**: Der Seitenumfang wird an genau einer Stelle geprüft: `pruef-modus/SKILL.md:141`, Teil-Check D, und zwar aus dem gerenderten PDF. Teil-Check D war in **jedem** Lauf dieses Projekts ÜBERSPRUNGEN, weil `lualatex`/`biber` in der Session-Umgebung fehlen. Ergebnis: Der Voll-Audit vom 2026-07-23 vergab **Score 100/100 mit dem Vermerk „abgabereif"**, obwohl das einzige Kriterium, das laut `hard-rules-formal.md:67` Punktabzug nach sich ziehen kann, gar nicht geprüft wurde.

Zwei getrennte Probleme stecken darin:

1. **Kein Fallback ohne Build.** Eine Wortzählung über `chapters/**/*.tex` plus die Layout-Parameter aus `main.tex` (11pt, Randbreite, `\onehalfspacing`) liefert eine brauchbare Schätzung — in diesem Projekt ~10–11 Seiten. Das ist kein Messwert, aber es hätte gereicht, um das Thema überhaupt aufzuwerfen.
2. **Ein übersprungener Check darf keinen vollen Score erlauben.** „ÜBERSPRUNGEN" wird derzeit wie „bestanden" behandelt. Ein Audit mit ungeprüftem Pflichtkriterium sollte den Score deckeln oder ihn ausdrücklich als vorläufig kennzeichnen — sonst liest der Nutzer „100/100 abgabereif" und hört auf zu prüfen. Genau das ist hier passiert.

**Vorgeschlagener Fix**:
- `check_formalia.py` um eine Gesamt-Wortzahl mit Seitenschätzung erweitern. **Architektonisch fast gratis**: Das Skript sammelt in `main()` bereits alle Dateien und führt in `check_title_duplication` schon einen dateiübergreifenden Durchgang über `metas` mit einem vorhandenen `word_count` je Datei aus (`check_formalia.py:316`, `:102`). Es fehlt nur die Summe plus ein Divisor. Auffällig ist die aktuelle Asymmetrie: Das Skript warnt, wenn eine Subsection **zu kurz** ist (HALBSEITE, < 150 Wörter), aber nie, wenn die Arbeit insgesamt zu lang ist.
- `pruef-modus` Teil-Check D: Bei fehlendem `lualatex` die Schätzung als `[UNGEPRÜFT — Schätzung: N Seiten]` ausgeben statt den Punkt kommentarlos zu überspringen, und die Score-Regel entsprechend anpassen.
- Ergänzend `plan-modus`: Aus der Seitenvorgabe in `aufgabe.md` ein **Wortbudget je Kapitel** ableiten und in `kapitelplan.md` mitführen. Der Schreib-Modus hat aktuell keinerlei Zielgröße, gegen die er schreiben könnte — er kennt Prozentanteile („Einleitung 10–15 %"), aber nie einen absoluten Wert.

## 6. Redundanzvermeidung beim Schreiben: teilweise vorhanden, aber blind für Nachbardateien

**Befund**: `hard-rules-formal.md` enthält die richtigen Regeln bereits — `:61` (Vorverweise dosieren, „ein Vorverweis unmittelbar vor der Überschrift, die dasselbe ankündigt, entfällt"), `:87` (Signalwort-Wiederholung), `:88` (zentrale Sätze nicht wörtlich wiederholen). Diese Regeln wurden in diesem Projekt **trotzdem** an mehreren Stellen verletzt: Die Einleitung kündigt den Kapitelaufbau in 110 Wörtern an, die Kapitel-Einleitung der Durchführung wiederholt ihn direkt danach.

Die Ursache ist struktureller Natur, nicht mangelnde Regeltreue: `schreib-modus` schreibt **ein Kapitel pro Session** (so vorgesehen und richtig, siehe `CLAUDE.md` → Session-Regeln), und `check_formalia.py` arbeitet im Kern dateiweise. Weder Schreiber noch Prüfskript sieht beim Verfassen von Kapitel 2, was Kapitel 1 bereits gesagt hat. Redundanz zwischen Dateien ist damit ein blinder Fleck **by design**.

**Vorgeschlagener Fix** (bewusst minimal, die Ein-Kapitel-pro-Session-Architektur soll bleiben):
- `schreib-modus` Schritt „Stand ermitteln": Beim Schreiben eines Kapitels die **erste und letzte Textzeile jeder bereits fertigen Subsection-Datei** mitlesen — nicht die ganzen Kapitel, das würde den Token-Vorteil zerstören. Absatzanfänge verraten Themenwiederholung zuverlässig und kosten fast nichts.
- `check_formalia.py` um eine Heuristik für kapitelübergreifende Wiederholung ergänzen: Sätze, die sich über Dateigrenzen hinweg um mehr als X % im Wortbestand überlappen, als `[HINWEIS:WIEDERHOLUNG]` melden. Der dateiübergreifende Durchgang ist wie in Befund 5 bereits vorhanden.

## Einschätzung: Braucht es einen eigenen „Kürzungs-Modus"?

**Nein.** Ein eigener Skill wäre die falsche Antwort, aus drei Gründen:

1. **Der Fahrplan hat bereits sieben Stationen.** Eine achte kostet eine weitere Session und wird bei kleinen Arbeiten (7–10 Seiten) genauso übersprungen wie der Gesamt-Stresstest laut Kompakt-Prüfkette — also gerade bei den Arbeiten, wo der Umfangsdruck am größten ist.
2. **Das Wissen sitzt schon an der richtigen Stelle.** `pruef-modus` Teil-Check B hat einen Redundanz-Punkt (`:133`), er ist nur auf Reflexion↔Fazit verengt. `hard-rules-formal.md:88` hat die Regel, ihr fehlt nur ein Prüfschritt. Ein neuer Modus würde Bestehendes duplizieren statt reparieren.
3. **Kürzen braucht den Gesamtblick, den nur der Prüf-Modus ohnehin schon hat.** Ein separater Skill müsste alle Kapitel neu einlesen — genau der teure Kontext, den `pruef-modus` bereits geladen hat.

**Und: nicht von Anfang an redundanzfrei schreiben zu wollen.** Das ist der intuitive Reflex, aber er zielt an der Ursache vorbei. Die Redundanz stammt nicht aus dem ersten Entwurf — die Erstfassungen der Kapitel waren angemessen dicht. Sie ist in den **Überarbeitungsrunden** entstanden, jedes Mal als korrekte Reaktion auf einen korrekten Befund. Eine schärfere Schreibregel im `schreib-modus` hätte daran nichts geändert; sie hätte höchstens den ersten Entwurf verknappt und damit den späteren Zuwachs erst recht kaschiert. Zudem ist ein gewisses Maß an Wiederaufnahme in wissenschaftlichen Texten **gewollt** — Einleitung, Hauptteil und Fazit sollen sich aufeinander beziehen. Eine Regel „schreibe nie zweimal dasselbe" wäre schlechter als der Ist-Zustand.

**Der eigentliche Hebel liegt am Ende, nicht am Anfang:** Der Prozess braucht keine strengere Schreibregel, sondern eine Stelle, die den **kumulierten** Stand betrachtet statt nur das jeweilige Delta. Konkret in dieser Reihenfolge:

| Priorität | Eingriff | Aufwand | Wirkung |
|---|---|---|---|
| 1 | `check_formalia.py`: Gesamt-Wortzahl + Seitenschätzung ausgeben | sehr gering (Mehrdatei-Durchgang und `word_count` existieren) | macht Umfang in **jeder** Session sichtbar, unabhängig vom Build |
| 2 | `pruef-modus` Teil-Check B `:133`: Redundanz-Check vom Reflexion↔Fazit-Paar auf den ganzen Text ausweiten | gering (ein Checklistenpunkt) | findet genau das Muster dieses Projekts |
| 3 | `pruef-modus` Teil-Check D: übersprungener Umfangs-Check deckelt den Score bzw. markiert ihn vorläufig | gering | verhindert „100/100 abgabereif" bei ungeprüftem Pflichtkriterium |
| 4 | `gegenlesung/SKILL.md:83`: Umfangshinweis auf Gesamtstand statt Delta beziehen | sehr gering | schließt die Lücke, die in Runde 3 zur Fehleinschätzung führte |
| 5 | `plan-modus`: Wortbudget je Kapitel aus der Seitenvorgabe ableiten, in `kapitelplan.md` mitführen | mittel | gibt dem Schreib-Modus erstmals eine absolute Zielgröße |
| 6 | `schreib-modus`: Absatzanfänge fertiger Nachbarkapitel mitlesen | mittel (Token-Kosten abwägen) | mildert die Ein-Kapitel-pro-Session-Blindheit |

Die Punkte 1–4 sind zusammen unter einer Stunde Arbeit und hätten in diesem Projekt gereicht. Punkte 5 und 6 sind optional und berühren die Session-Architektur — dort würde ich erst nach dem nächsten Projekt entscheiden.

## Status

Alle sechs Befunde sind bislang nur dokumentiert, nicht in den Skill-Dateien umgesetzt. Umsetzung würde `typen/projektbericht.md`, `plan-modus/SKILL.md`, `schreib-modus/SKILL.md`, `gegenlesung/SKILL.md`, `pruef-modus/SKILL.md`, `_shared/hard-rules-formal.md` und `_shared/scripts/check_formalia.py` betreffen.

**Empfohlene Reihenfolge insgesamt**: zuerst Befund 5 Punkt 1 (Wortzahl im Skript — billigste Maßnahme mit der breitesten Wirkung), dann Befund 1 (falsche Voice-Vorgabe für Einzelarbeiten — der einzige Befund, bei dem eine Skill-Datei aktiv etwas Falsches vorschreibt), danach die Checklistenpunkte aus Befund 4 und 5.
