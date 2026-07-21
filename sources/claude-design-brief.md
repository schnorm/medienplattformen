# Claude-Design-Brief: UI/UX-Mockups Resteria

Arbeitsdokument für die spätere Session in Claude Design (separate Oberfläche, nicht Teil dieses Projektordners). Kein Bestandteil des abgegebenen Berichts — dient nur dazu, die drei Screens aus Anhang B konsistent zu befüllen. Jeden Screen-Block einzeln in den Claude-Design-Chat kopieren.

## Gemeinsamer Kontext (vor jedem Screen-Prompt mitgeben)

Plattform: Resteria — Social-Media-Plattform für nachhaltigkeitsorientierte Hobbyköch:innen mit Fokus auf Resteverwertung (Zero-Waste). Kernidee: Nutzer:innen geben übrige Zutaten ein und erhalten passende Rezeptvorschläge; jede verwertete Zutat bringt einen Rettungspunkt, der zu einem Reste-Level (z. B. Titel „Resteheld:in") führt.

Zielgruppe: nachhaltigkeitsorientierte Hobbyköch:innen, die beim Kochen bereits auf Resteverwertung achten (Persona: Mara K., 29 Jahre, kocht vier- bis fünfmal pro Woche selbst, möchte Lebensmittel nicht wegwerfen, hat wenig Zeit für aufwendige Planung).

Stil: freundlicher, warmer Look mit Food-Bezug; erdige/naturnahe Farbtöne (Grün, Terracotta); mobile App-Screens im Hochformat; keine Stock-Photo-Kitsch-Ästhetik.

## Screen 1: Startseite

- **Ziel**: Zeigt die Kernfunktion — aus übrigen Zutaten wird ein Rezeptvorschlag.
- **Layout**: Mobile App-Screen, Hochformat. Oben ein Eingabefeld für Reste-Zutaten mit bereits eingegebenen Zutaten als Chip-Tags. Darunter eine Liste mit zwei bis drei Rezeptvorschlägen als Karten (Bild, Titel, Zubereitungszeit, Anzahl fehlender Zusatzzutaten). Unten eine Navigationsleiste mit Icons für Start, Profil und Rettungs-Feed.
- **Inhalt**: Beispielzutaten wie „Brokkoli-Strunk", „Karottengrün", „altes Brot"; zwei bis drei plausible Rezepttitel, z. B. „Brokkoli-Strunk-Suppe", „Knuspriges Brot-Topping".
- **Zielgruppe**: siehe gemeinsamer Kontext, Fokus auf mobile Alltagsnutzung.

## Screen 2: Profil

- **Ziel**: Macht die Gamification-Mechanik sichtbar — Rettungspunkte und Reste-Level als Fortschritt.
- **Layout**: Mobile App-Screen. Oben ein Profilbild-Platzhalter, Name und Reste-Level-Badge. Darunter ein Fortschrittsbalken oder Punktezähler für die Rettungspunkte. Darunter ein Raster mit eigenen geposteten Reste-Kreationen (vier bis sechs Foto-Platzhalter).
- **Inhalt**: Beispielwerte wie „1.240 Rettungspunkte", „Level 4 — Resteheld:in".
- **Zielgruppe**: siehe gemeinsamer Kontext, Fokus auf Fortschritt und Selbstwahrnehmung.

## Screen 3: Rettungs-Feed

- **Ziel**: Zeigt die Community-Funktion — geteilte Reste-Kreationen mit Tag zur verwendeten Zutat.
- **Layout**: Mobile App-Screen, vertikaler Feed im Stil einer Social-Media-Timeline. Jeder Beitrag mit Foto- oder Video-Vorschau, Nutzername, Tag „gerettet: [Zutat]" sowie Like- und Kommentar-Icons darunter.
- **Inhalt**: Zwei bis drei Beispielbeiträge mit unterschiedlichen geretteten Zutaten, z. B. „gerettet: Bananenschale", „gerettet: Radieschengrün".
- **Zielgruppe**: siehe gemeinsamer Kontext, Fokus auf sozialen Austausch.

## Nach der Erstellung nicht vergessen

1. Jedes fertige Mockup als Bild aus Claude Design exportieren und in `images/durchfuehrung/` ablegen.
2. In `pages/appendix.tex` die drei `tikzpicture`-Platzhalter durch `\includegraphics{images/durchfuehrung/<datei>}` ersetzen.
3. Die `\quelle{}`-Zeile je Abbildung anpassen auf: „Erstellt mit dem Prompt [tatsächlich verwendeter Prompt-Text] durch Claude Design." — Pflicht laut Zitierleitfaden für KI-generierte Abbildungen (siehe `hard-rules-formal.md`).
4. Danach `check_formalia.py` erneut laufen lassen, um die Caption-Reihenfolge und Quellenzeile mechanisch zu prüfen.
