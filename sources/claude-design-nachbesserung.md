# Claude-Design-Nachbesserung: UI/UX-Mockups Resteria (Runde 2)

Arbeitsdokument für eine Folge-Session in Claude Design, aufbauend auf `claude-design-brief.md` (Runde 1, bereits umgesetzt und in `images/durchfuehrung/` abgelegt). Kein Bestandteil des abgegebenen Berichts.

Claude Design arbeitet chatbasiert-iterativ: Beschreibung → erste Version → Verfeinerung per Chat/Inline-Kommentar, kein Einmal-Prompt wie bei klassischen Bildgeneratoren (Quelle: [claude.com/product/design](https://claude.com/product/design)). Die Anpassungen unten lassen sich deshalb als **Folgeanweisungen im selben Projekt/Chat** geben, in dem die Runde-1-Mockups entstanden sind — kein Neuaufbau der Screens nötig.

## Anlass

Beim Abgleich von `chapters/02_durchfuehrung/02_zielgruppe.tex`, `03_konzept.tex` und `04_community_und_feedback.tex` gegen die vier bestehenden Mockups sind drei Lücken zwischen Textanspruch und Bild aufgefallen:

1. **Rezept-Upload nicht sichtbar**: `03_konzept.tex` und die Funktionsübersicht-Tabelle (`tab:funktionsuebersicht`) nennen den Foto-/Video-Upload eigener Reste-Kreationen als eigene Kernfunktion (von der Aufgabenstellung explizit gefordert). In keinem der vier Mockups gibt es einen sichtbaren „Beitrag erstellen"-Button.
2. **Einsparangabe fehlt**: `02_zielgruppe.tex` verlangt, dass die Plattform sichtbar macht, „wie viel eine Person durch Resteverwertung tatsächlich einspart". Das Profil-Mockup zeigt bisher nur abstrakte Rettungspunkte/Level, keine konkrete Mengenangabe.
3. **Challenges/Rangliste fehlen im Feed**: `04_community_und_feedback.tex` beschreibt die zeitlich begrenzte „Zero-Waste-Woche"-Challenge mit Rangliste als zentrales, studienbasiert begründetes Interaktionsformat. Im Rettungs-Feed-Mockup ist davon nichts zu sehen.

Hinweis zum Tag-Format: Der Text nannte ursprünglich als Beispiel „gerettet: Brokkoli-Strunk", das Mockup zeigt am Beitrag aber nur die Zutat ohne das Präfix „gerettet:". Das ist bewusst **nicht** als Bild-Anpassung aufgenommen — stattdessen wurde der Text an das bestehende, schlankere Mockup angeglichen (Nutzerentscheidung: Präfix wirkt auf dem kleinen Screen überladen, der Kontext „Rettungs-Feed" macht es ohnehin klar).

## Anpassung 1: Rettungs-Feed — Beitrag-Button, Challenge-Banner

Folge-Prompt im bestehenden Rettungs-Feed-Screen (beide Punkte können in einer Nachricht gegeben werden, da derselbe Screen betroffen ist):

> Ergänze am Rettungs-Feed-Screen einen schwebenden Terracotta-Plus-Button unten rechts zum Beitrag-Erstellen sowie ein schmales Challenge-Banner oben für die „Zero-Waste-Woche"-Rangliste.

(Bewusst unter 40 Wörtern gehalten — der Prompt-Text wird wörtlich in `\quelle{}` zitiert, und `hard-rules-formal.md` verlangt für Zitate > 40 Wörter die `blockzitat`-Umgebung statt `\enquote{}`, was in einer Bildquellenzeile unpassend wäre.)

## Anpassung 2: Profil — konkrete Einsparangabe

Folge-Prompt im bestehenden Profil-Screen:

> Ergänze unterhalb des Rettungspunkte-Fortschrittsbalkens eine zweite, kleinere Kennzahl mit einer konkreten Mengenangabe, z.\,B. „12,4 kg Lebensmittel gerettet", die die Rettungspunkte in eine greifbare Einsparung übersetzt. Layout und Farben sonst unverändert lassen.

## Nach der Erstellung nicht vergessen

1. Beide aktualisierten Screens exportieren und die bestehenden Dateien in `images/durchfuehrung/` überschreiben (`resteria_rettungsfeed.png`, `resteria_profil.png`).
2. Die `\quelle{}`-Zeilen in `pages/appendix.tex` sind bereits auf die kombinierten Prompts (Runde 1 + diese Anpassung) vorbereitet — nach dem Bild-Austausch nur noch prüfen, ob der zitierte Prompt-Text exakt der tatsächlich verwendeten Folgeanweisung entspricht, und bei Abweichung nachziehen.
3. Danach `check_formalia.py` erneut laufen lassen.
