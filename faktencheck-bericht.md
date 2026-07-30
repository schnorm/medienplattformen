# Faktencheck-Bericht – Unzitierte Außenweltbehauptungen

**Datum**: 30.07.2026 · **Geprüfter Stand**: alle `chapters/**/*.tex`, `pages/appendix.tex`, `pages/acronyms.tex` · **Prüftyp**: Nüchterner Subagenten-Faktencheck (kalt, isoliert, ohne Autorenkontext)

> **Was dieser Bericht ist und was nicht.** Er ist **kein** `pruef-modus`-Voll-/Delta-Audit und ersetzt keines — die formale Prüfkette bleibt bei `pruefbericht.md` (zuletzt: 89/100, vorläufig, Score-Deckel wegen fehlendem Build). Dieser Bericht schließt eine dort dokumentierte Lücke (`SKILL-ANPASSUNGEN.md` → P36): Er prüft **unzitierte** Tatsachenbehauptungen über die reale Außenwelt — Sätze, die weder ein Kernargument sind (dafür ist `stresstest` zuständig), noch eine Zitation tragen (dafür Teil-Check G), noch ein interner `\autoref` sind (dafür P35, offen). Betroffen ist praktisch nur die Wettbewerbsanalyse, die laut Prüfer-Steuerung als „eigene Sichtung, keine Zitationspflicht" läuft — genau das macht ihre Fakten für den regulären Workflow unsichtbar, ohne sie von der Wahrheitspflicht zu befreien.

**Methodik:** Ein isolierter Subagent hat den gesamten Text gelesen, **ohne** `CLAUDE.md` → Projektstatus, `pruefbericht.md`, `AENDERUNGEN.md`, `SKILL-ANPASSUNGEN.md`, `MEMORY.md`/`PERSISTENT.md` oder Git-Historie — um frühere „schon geprüft"-Urteile nicht ungeprüft zu übernehmen. Jede gefundene, überprüfbare Außenweltbehauptung wurde per gezielter Websuche einzeln verifiziert. 12 Kandidaten gefunden, 21 Websuchen, 7 zusätzliche (durchweg blockierte) Abrufversuche an Primärquellen.

## Abarbeitungsvermerk (30.07.2026, `schreib-modus`-Sitzung)

**Befund 2: umgesetzt** — aber **nicht** mit dem hier vorgeschlagenen Wortlaut. Der Vorschlag („offenbar kleineren, community-gespeisten Rezeptbestand als der redaktionell gepflegten Datenbank") hätte eine unbelegte Behauptung durch zwei neue ersetzt: Weder „community-gespeist" für leftovercooking noch „redaktionell gepflegt" für die \ac{BMLEH}-App ist in diesem Bericht verifiziert. Umgesetzt wurde stattdessen nur, was dieser Bericht selbst als Befund festhält (leftovercooking arbeitet KI-generiert statt mit fester Rezeptdatenbank) und was im Text bereits bestätigt steht (\ac{BMLEH}-App: umfangreiche Rezeptdatenbank, Zeile 7): der Größenvergleich ist durch einen **strukturellen** Unterschied ersetzt.
`01_wettbewerbsanalyse.tex:9` — alt: „…KI-gestützte Rezeptvorschläge aus einem kleineren Rezeptbestand als dem der \ac{BMLEH}-App." · neu: „…KI-gestützte Rezeptvorschläge, statt wie die \ac{BMLEH}-App auf einen festen, durchsuchbaren Rezeptbestand zurückzugreifen."
„durchsuchbar" ist dabei bewusst gesetzt: Der gestrichene Halbsatz war die einzige Deckung für die Tabellenwertung „Rezept-Entdeckung: mittel" bei leftovercooking; die Neufassung trägt sie weiter. Kontrolle: `check_all.py --kapitel chapters/02_durchfuehrung` 0 FEHLER · `check_quellentreue.py --datei chapters/` 19/19 FUNDSTELLE OK, keine Zitation invalidiert · Umfang 3.693 Wörter (+2).

**Befund 1: bewusst nicht angefasst, bleibt offen.** Verifikation wurde in dieser Sitzung erneut versucht und kam weiter, ohne abzuschließen:
- *Neu gefunden:* Ein unabhängiger NETZWELT-Vergleichstest speziell zu Rezept-Rückwärtssuchen führt Chefkoch.de mit einer „Reste-Suche" („Bei Chefkoch kannst du einzelne Zutaten eingeben, die du noch im Kühlschrank hast, und die Plattform schlägt dir mögliche Rezepte vor"). Zusätzlich nennen Chefkoch-**eigene** App-Store-Release-Notes die Funktion beim Namen („Performance in der Ergebnisliste der Zutatensuche verbessert") — das ist Herstellertext, kein Dritt-Snippet. Die Existenz *einer* Zutatensuche ist damit deutlich besser gestützt als im Erstlauf.
- *Weiterhin ungeklärt, und daran hängt der Satz:* (a) ob **mehrere** Zutaten gleichzeitig eingegeben werden können — alle Snippets sagen „einzelne Zutaten eingeben", im Deutschen zweideutig; (b) kostenlos oder „Chefkoch Plus" — die Quellen widersprechen sich direkt.
- *Warum kein Primärzugriff:* Nicht nur chefkoch.de blockt. Die Netzwerkrichtlinie dieser Umgebung lässt keine der Primär- und Testquellen durch — `apps.apple.com`, `play.google.com`, `netzwelt.de`, `t3n.de`, `deutsche-glasfaser.de` und `web.archive.org` antworten sämtlich mit 403 (per `curl` gegengeprüft: `CONNECT tunnel failed, response 403`; der Agent-Proxy selbst meldet `recentRelayFailures: []`, der Block ist also policy-, nicht fehlerbedingt).

**Warum auch kein vorsorgliches Entschärfen des Fließtextsatzes:** Naheliegend wäre, die Absolutbehauptung („kein Werkzeug") ohne Verifikation abzuschwächen und die Tabelle zu lassen. Das ist hier **nicht** zulässig: Der Satz ist die einzige Deckung der Tabellenzelle „Reste-Matching-Werkzeug: schwach" für Chefkoch. Ein entschärfter Fließtext bei unveränderter Zelle erzeugt eine unbedeckte Wertung — einen eigenen Audit-Befund (`schreib-modus` → Self-Check, „deckt der Fließtext jede Wertung?"). Der Fehler wäre also nur ausgetauscht, nicht behoben.

**Konsequenzkette, die dieser Bericht unterschätzt.** Er stuft die Korrektur als „reine Sachkorrektur ohne Bezug zu These/Kernargumenten" ein. Für den Fließtextsatz stimmt das; die Tabellenzelle zieht aber zwei weitere Stellen nach: `01_wettbewerbsanalyse.tex:36` („die Community-Plattformen den Austausch ohne Weg von übrigen Zutaten zum Rezept") und `:38` (Alleinstellungsmerkmal = Verbindung beider Elemente). Wandert Chefkoch von „schwach" auf „mittel", sind beide Sätze mitbetroffen. Wer Befund 1 umsetzt, plant diese drei Stellen als **einen** Arbeitsgang ein — und braucht dafür eine Freigabe, weil `:38` das Kernargument trägt.

## Ergebnis in einem Satz

Der Text ist überwiegend sorgfältig recherchiert (10 von 12 Kandidaten vollständig bestätigt); **ein Fund ist potenziell ein echter Sachfehler an einer tragenden Stelle der Wettbewerbsanalyse** und braucht manuelle Nachprüfung, bevor er als Befund gilt oder verworfen wird.

## Befund 1 (Priorität: hoch, Verdacht — nicht abschließend verifiziert) — Chefkoch-Zutatensuche

**Stelle:** `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:3` und `tab:wettbewerbsvergleich`, Zeile „Chefkoch.de", Spalte „Reste-Matching-Werkzeug" (aktuell „schwach").

**Behauptung im Text:** „Für Resteverwertung bietet die Plattform zwar Rezeptsammlungen zu einzelnen Zutaten, aber kein Werkzeug, das aus mehreren vorhandenen Resten Vorschläge ableitet."

**Befund:** Fünf voneinander unabhängige Websuch-Ergebnisse — darunter ein offizieller Chefkoch-eigener TikTok-Post — deuten übereinstimmend darauf hin, dass Chefkoch eine „Zutatensuche"/„Zutatenverwertung" anbietet, bei der mehrere vorhandene Zutaten eingegeben und dafür passende Rezepte vorgeschlagen werden — exakt das Werkzeug, dessen Fehlen der Satz kategorisch behauptet. Nach den gefundenen Quellen ist die Funktion (zumindest teilweise) Teil des kostenpflichtigen „Chefkoch Plus"-Pakets, nicht der kostenlosen Basisversion — das würde die Aussage relativieren, aber nicht aufheben, da der Satz uneingeschränkt „kein Werkzeug" behauptet.

**Warum das nicht bereits als Korrektur gilt:** Ein direkter Abruf von chefkoch.de bzw. der zugehörigen App-Store-Seiten war bei jedem Versuch mit HTTP 403 blockiert (Bot-Schutz). Die Verifizierung stützt sich damit auf konvergente Sekundärquellen (Suchergebnis-Snippets, ein TikTok-Post), nicht auf eine selbst gelesene Primärquelle. Das ist nach dem eigenen Maßstab dieses Projekts (`CLAUDE.md` → „Erst prüfen, dann behaupten") nicht stark genug, um den Text direkt zu ändern.

**Warum der Fund trotzdem nicht ignoriert werden sollte:** Der Satz sitzt an der ersten und prominentesten Vergleichsplattform der ganzen Wettbewerbsanalyse und trägt direkt die Kernabgrenzung, auf der die Marktlücken-Argumentation aufbaut („Community-Plattformen bieten Austausch, aber kein Reste-Matching"). Sollte sich die Funktion bestätigen, betrifft das sowohl den Fließtextsatz als auch die Tabellenwertung „schwach" in `tab:wettbewerbsvergleich`.

**Nötiger nächster Schritt (Nutzer-Schritt, kein Skript kann das):** Direkt in der Chefkoch-App oder auf chefkoch.de nachsehen, ob eine Zutatensuche/-verwertung existiert, die aus mehreren eingegebenen Resten Rezepte vorschlägt, und ob sie kostenlos oder Teil von „Chefkoch Plus" ist.

**Formulierungsvorschlag, falls bestätigt** (nicht angewendet, nur Vorschlag): „Für Resteverwertung bietet die Plattform inzwischen eine Zutatensuche, bei der sich aus mehreren eingegebenen Resten passende Rezepte finden lassen – nach verfügbaren Quellen jedoch nur im kostenpflichtigen Chefkoch-Plus-Paket, nicht in der kostenlosen Basisversion, und ohne den in Resteria vorgesehenen Bezug zu Rettungspunkten oder Community." Bei Nichtbestätigung: kein Änderungsbedarf, Satz bleibt stehen.

## Befund 2 (Priorität: niedrig) — leftovercooking-Rezeptbestand im Vergleich zur BMLEH-App

**Stelle:** `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:9`

**Behauptung im Text:** „…KI-gestützte Rezeptvorschläge aus einem kleineren Rezeptbestand als dem der \ac{BMLEH}-App."

**Befund:** Verdikt NICHT VERIFIZIERBAR. Für die BMLEH-App ist eine konkrete Zahl bekannt (≈ 800 Rezepte), für leftovercooking (KI-generierte statt fester Rezeptdatenbank) ließ sich trotz mehrerer Suchanfragen keine vergleichbare Zahl finden. Der Vergleich ist plausibel, aber nicht belegbar.

**Formulierungsvorschlag** (optional, keine Pflicht): „…KI-gestützte Rezeptvorschläge aus einem offenbar kleineren, community-gespeisten Rezeptbestand als der redaktionell gepflegten Datenbank der \ac{BMLEH}-App."

## Vollständig bestätigte Kandidaten (kein Handlungsbedarf)

| Datei:Zeile | Behauptung (gekürzt) | Verdikt |
|---|---|---|
| `01_ausgangslage_und_problem.tex:3` | Chefkoch/TikTok als etablierte Rezept-/Content-Plattformen | BESTÄTIGT |
| `01_ausgangslage_und_problem.tex:7` | Restegourmet/BMLEH-App: Matching ohne Community | BESTÄTIGT |
| `01_wettbewerbsanalyse.tex:3` | Chefkoch: Upload, Bewertung, Kommentar | BESTÄTIGT |
| `01_wettbewerbsanalyse.tex:5` | TikTok: Kochen als Content-Kategorie, kein Zutaten-Matching | BESTÄTIGT |
| `01_wettbewerbsanalyse.tex:7` | Restegourmet/BMLEH-App: Funktionen, keine Community | BESTÄTIGT |
| `01_wettbewerbsanalyse.tex:9` | leftovercooking: Vorrat, Farbcodierung, KI-Vorschläge, Punkte in €, Creator-Community | BESTÄTIGT |
| `01_wettbewerbsanalyse.tex:11` | Foodsharing.de: Fairteiler, aktive Community, keine Rezeptvorschläge | BESTÄTIGT |
| `06_evaluation_reflexion.tex:9` | „Restlos Glücklich" e.V., Berlin, seit 2015, Zero-Waste | BESTÄTIGT |
| `pages/acronyms.tex:9` | BMLEH-Name seit Regierungswechsel 6. Mai 2025 | BESTÄTIGT |

## Einschätzung zur Wettbewerbsanalyse als Ganzes

Kein systematisches Alterungs- oder Rechercheproblem: 6 von 8 dort geprüften Kandidaten vollständig bestätigt, einer eine unbelegbare, aber plausible Detailzahl. Fünf der sechs Plattformen (TikTok, Restegourmet, BMLEH-App, leftovercooking, Foodsharing.de) sind an unabhängigen, aktuellen Quellen vollständig verifiziert. Der eine offene Punkt (Befund 1) ist inhaltlich nicht trivial, aber ein Einzelfund, kein Muster.

## Kapitel ohne Kandidaten (kein Fund, nicht „nichts geprüft")

`02_zielsetzung_und_verengung.tex`, `03_vorgehen_und_aufbau.tex`, `02_zielgruppe.tex`, `03_konzept.tex` (dort nur Zitate oder eigene Resteria-Setzungen, keine Außenweltbehauptung), `04_community_und_feedback.tex`, `05_phasenplanung.tex`, `07_iteratives_design.tex`, beide Fazit-Dateien, `pages/appendix.tex` (nur KI-Prompt-Zitate und eigene Darstellungen).

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

1. **Existiert bei Chefkoch.de/in der App eine Zutatensuche/-verwertung, die aus mehreren eingegebenen Resten Rezeptvorschläge ableitet, und ist sie kostenlos oder Teil von „Chefkoch Plus"?** | `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:3` und `tab:wettbewerbsvergleich`, Zeile Chefkoch.de, Spalte „Reste-Matching-Werkzeug" | Direkter Blick in die Chefkoch-App/-Website oder ein aktueller Chefkoch-Plus-Test mit Screenshot | WebFetch auf chefkoch.de und die App-Store-Seiten war durchgehend mit HTTP 403 blockiert; die fünf Suchergebnisse sind konvergent, aber sekundär.
2. ~~**Größenvergleich Rezeptbestand leftovercooking vs. BMLEH-App**~~ — **entfällt seit 30.07.2026.** Der Größenvergleich steht nicht mehr im Text (siehe Abarbeitungsvermerk, Befund 2); es gibt damit nichts mehr nachzuschlagen.

## Handlungsempfehlungen (nach Priorität)

1. **Befund 1 manuell an der echten Chefkoch-App/-Website verifizieren** — einziger offener Punkt dieses Berichts. Zwei Teilfragen, beide nötig: Lassen sich **mehrere** Zutaten gleichzeitig eingeben? Kostenlos oder „Chefkoch Plus"? Danach: bei Bestätigung Fließtextsatz **und** Tabellenzelle **und** die beiden Folgestellen `:36`/`:38` in einem Arbeitsgang anpassen — **mit Freigabe**, weil `:38` das Kernargument trägt (Einstufung des Erstlaufs an dieser Stelle korrigiert, siehe Abarbeitungsvermerk). Bei Widerlegung keine Änderung, der Bericht ist damit vollständig erledigt.
2. ~~**Befund 2 optional hedgen**~~ — **erledigt 30.07.2026**, mit abweichendem Wortlaut (siehe Abarbeitungsvermerk).
3. Kein weiterer Handlungsbedarf aus diesem Bericht.

## Vor der nächsten Session

Dieser Bericht ist als eigenständige Arbeitsliste für eine neue `schreib-modus`-Sitzung gedacht (Prüfer-/Autorrolle trennen, wie bei `pruef-modus` und `gegenlesung`). Nach Umsetzung von Befund 1 (falls bestätigt): `check_all.py --kapitel chapters/02_durchfuehrung` laufen lassen und die Statuszeile `sec:durchfuehrung` in `CLAUDE.md` aktualisieren. Der bestehende Score in `pruefbericht.md` (89/100, vorläufig) ist von diesem Bericht unabhängig und bleibt gültig, bis der ausstehende Build nachgeholt wird.
