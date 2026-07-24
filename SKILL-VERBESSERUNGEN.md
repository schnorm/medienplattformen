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

## Status

Alle drei Befunde sind bislang nur dokumentiert, nicht in den Skill-Dateien umgesetzt. Umsetzung würde `typen/projektbericht.md`, `plan-modus/SKILL.md`, `gegenlesung/SKILL.md` und `pruef-modus/SKILL.md` betreffen.
