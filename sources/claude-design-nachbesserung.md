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

## Anpassung 3: Rettungs-Feed — Plus-Button-Position, Foto-Platzhalter (Gegenlesung Runde 6, Befund 6.3)

Anlass: Der schwebende Plus-Button überlappt im aktuellen `resteria_rettungsfeed.png` die Aktionsleiste des ersten Beitrags und verdeckt dort teilweise das Lesezeichen-Icon. Zusätzlich tragen die Foto-Platzhalter in allen vier Mockups die Beschriftung „Foto:" mit Doppelpunkt ohne Folgetext, was wie ein abgeschnittener Platzhalter-String wirkt. Der Prüfer erlaubt KI-generierte Mockups ausdrücklich nur, sofern sie keine gestalterischen Fehler enthalten.

Folge-Prompt im bestehenden Rettungs-Feed-Screen:

> Positioniere den Plus-Button am Rettungs-Feed-Screen so, dass er die Aktionsleiste des ersten Beitrags nicht überlappt, und ersetze die Foto-Platzhalter-Beschriftung „Foto:" durch „Foto" ohne Doppelpunkt.

Die Platzhalter-Beschriftung „Foto:" betrifft alle vier Mockups gleichermaßen. Nur der Rettungs-Feed-Screen hat zusätzlich das Überlappungsproblem; die `\quelle{}`-Zeile ist dafür bereits vorbereitet (siehe unten). Werden Startseite, Bookmarks-Ansicht oder Profil ebenfalls neu exportiert, um dieselbe Platzhalter-Korrektur einzuarbeiten, müssen die jeweiligen `\quelle{}`-Zeilen in `pages/appendix.tex` um denselben Folge-Prompt ergänzt werden.

## Anpassung 4: Startseite — Zugang zu Wochenplan und Reste-Journal (2026-07-28)

Anlass: `chapters/02_durchfuehrung/03_konzept.tex:13` behauptet für die Menüplanung wörtlich „Erreichbar ist der Bereich über die Startseite, sodass die Navigation bei drei Hauptbereichen bleibt." Eine Sichtung aller vier Mockups zeigt: Weder Wochenplan noch Reste-Journal sind irgendwo abgebildet, und auf beiden Startseiten-Screens gibt es keinen Einstiegspunkt dorthin — die Tab-Leiste führt durchgehend nur Start, Rettungs-Feed und Profil. Der Text macht damit eine Aussage, die der Leser am Bild überprüfen kann und die dort widerlegt wird; das wiegt schwerer als eine bloß fehlende Funktion, da der Prüfer KI-Mockups nur ohne gestalterische Fehler zulässt.

Hintergrund: Das ist die Altlast von Gegenlesungs-Befund 5.7 („Menüplanung ohne UI-Zugang"). Der wurde seinerzeit per Option A gelöst — Textzusatz statt neuem Bild. Der Satz sollte die Lücke schließen, hat sie aber in eine überprüfbare Behauptung verwandelt.

Warum nicht stattdessen streichen: Die Kopplung von Menüplanung und Reste-Journal an die Rettungspunkte ist die erste der drei in `03_konzept.tex:32` benannten Innovationen (Kriterium Kreativität, 15 %), sie ist der einzige Beleg für den Schlüsselbegriff „Lebensmittel-Journaling/Menüplanung" aus der Aufgabenstellung, `06_evaluation_reflexion.tex:3` beruft sich in der Abdeckungsliste darauf, und das Freemium-Paket („erweitert die Menüplanung um eine Vorratsübersicht") verlöre seine Basis. Die Bildergänzung kostet dagegen null Wörter und braucht keine fünfte Abbildung.

Folge-Prompt im bestehenden Startseiten-Screen:

> Ergänze am Startseiten-Screen unterhalb der Rezeptvorschläge eine kompakte Karte „Wochenplan & Reste-Journal" mit den nächsten Wochentagen und einer Zeile zu zuletzt verwerteten Zutaten.

(Wie bei Anpassung 1 bewusst unter 40 Wörtern — der Text wird wörtlich in `\quelle{}` zitiert, und `hard-rules-formal.md` verlangt für Zitate über 40 Wörter die `blockzitat`-Umgebung, die in einer Bildquellenzeile unpassend wäre.)

Betrifft **beide** Startseiten-Screens, da die Bookmarks-Ansicht derselbe Screen mit ausgeklapptem Lesezeichen-Bereich ist. Wenn die Karte nur in einem der beiden auftaucht, entsteht ein neuer Widerspruch zwischen zwei Abbildungen desselben Bildschirms.

Da ohnehin beide Startseiten neu exportiert werden, lässt sich die noch offene Platzhalter-Korrektur aus Anpassung 3 („Foto:" → „Foto") im selben Zug miterledigen; dann bleibt sie nur noch im Profil-Screen offen.

### Stand Anpassung 4: umgesetzt am 2026-07-28

Beide Startseiten-Screens tragen jetzt identisch das Banner „Wochenplan · Heute: Brokkoli-Suppe" unterhalb des Headers; die Tab-Leiste bleibt bei drei Einträgen. Die Aussage in `03_konzept.tex:13` ist damit am Bild belegt. `\quelle{}`-Zeilen für `fig:mockup_start` und `fig:mockup_start_bookmarks` entsprechend ergänzt.

Zwei Punkte bewusst so belassen: Das Banner nennt nur den Wochenplan, nicht das Reste-Journal — der Text führt das Journal als „begleitend" zum Wochenplan, es liegt also hinter demselben Einstieg; belegt ist es nicht, widerlegt aber auch nicht. Und der Prompt beschreibt eine Karte unterhalb der Rezeptvorschläge, entstanden ist ein Banner oben: Der Zitierleitfaden (S. 20) verlangt „den verwendeten Prompt", also die Eingabe, nicht eine Beschreibung des Ergebnisses; der Zusatz „und in weiteren Iterationsschritten verfeinert" hält die Abweichung transparent, ohne ein Prompt-Protokoll zu behaupten.

## Stand Anpassung 3 (Befund 6.3), geprüft am 2026-07-28

Am Rettungs-Feed **erledigt**: Der Plus-Button überlappt die Aktionsleiste nicht mehr, das Lesezeichen-Icon des ersten Beitrags ist frei, und der Foto-Platzhalter trägt dort keinen Doppelpunkt mehr. Die Beschriftung „Foto:" steht aber weiterhin in `resteria_startseite.png`, `resteria_startseite_bookmarks.png` und `resteria_profil.png` — Anpassung 3 galt ausdrücklich für alle vier Screens.

## Nach der Erstellung nicht vergessen

1. Den aktualisierten Rettungs-Feed-Screen exportieren und die bestehende Datei in `images/durchfuehrung/` überschreiben (`resteria_rettungsfeed.png`).
2. Die `\quelle{}`-Zeile für `fig:mockup_feed` in `pages/appendix.tex` ist bereits auf die kombinierten Prompts (Runde 1 + Anpassung 1 + Anpassung 3) vorbereitet — nach dem Bild-Austausch nur noch prüfen, ob der zitierte Prompt-Text exakt der tatsächlich verwendeten Folgeanweisung entspricht, und bei Abweichung nachziehen.
3. Danach `check_formalia.py` erneut laufen lassen.

### Zusätzlich für Anpassung 4

4. `resteria_startseite.png` und `resteria_startseite_bookmarks.png` neu exportieren und die bestehenden Dateien in `images/durchfuehrung/` überschreiben.
5. Die `\quelle{}`-Zeilen für `fig:mockup_start` (`pages/appendix.tex:27`) und `fig:mockup_start_bookmarks` (Z. 34) um den Folge-Prompt ergänzen — Muster wie bei `fig:mockup_profil`: nach dem Ursprungs-Prompt `, ergänzt um den Folge-Prompt \enquote{…}` einfügen, davor den schließenden Teil `durch Anthropic, 2026 (Claude Design, Modell Claude Sonnet 5). Abbildung nachträglich manuell bearbeitet.` unverändert stehen lassen. Die Anführungszeichen im Prompt (`\enquote{Wochenplan \& Reste-Journal}`) verschachtelt setzen und das `&` als `\&` maskieren.
6. **Erst nach dem Bildaustausch** zitieren: Die `\quelle{}`-Zeilen wurden bewusst noch nicht vorbereitet. Stünde dort ein Prompt, der nie ausgeführt wurde, enthielte das abgegebene Dokument eine falsche Quellenangabe — und der Satz in `03_konzept.tex:13` bliebe zusätzlich unbelegt.
7. Wird die Runde **nicht** gefahren, stattdessen den Fallback setzen: In `03_konzept.tex:13` „Erreichbar ist der Bereich über die Startseite, sodass die Navigation bei drei Hauptbereichen bleibt." durch eine Formulierung ohne überprüfbare Zugangsbehauptung ersetzen, etwa „Der Bereich ergänzt die drei Hauptbereiche, ohne die Navigation zu erweitern." (±0 Wörter).
