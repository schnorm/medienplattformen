# Prüfbericht – Projektbericht

**Datum**: 31.07.2026 · **Geprüfter Stand**: Delta `7b597b4..1e4761d` (vier Kapiteldateien) plus Arbeitsverzeichnis, neu gebautes `main.pdf` · **Audit-Typ**: **Re-Audit (Delta)** – die beiden Befunde des Abgabe-Audits vom selben Tag, alle sieben Skripte, Teil-Check D (Neubau) und Teil-Check H über die geänderten Dateien am Stück

**Score: 100/100 – abgabereif**

> **Einordnung.** Beide Befunde des Abgabe-Audits (88/100) sind umgesetzt und am Text wie am gebauten PDF verifiziert. Kein neuer Textbefund, keine Regression. Ein Fund betrifft nicht die Arbeit, sondern das Prüfwerkzeug: `check_autoref.py` hat beim Lauf der Überarbeitungssitzung fünf bereits vergebene Urteile stillschweigend gelöscht (siehe „Werkzeug-Fund"). Sie sind in diesem Lauf neu geprüft und eingetragen.

---

## Geprüfter Delta

Vier Dateien, 8 Einfügungen, 6 Löschungen – vollständig deckungsgleich mit dem Nachtrag des Vorberichts:

| Datei | Änderung | Herkunft |
|---|---|---|
| `01_wettbewerbsanalyse.tex:15` | Definition des Kriteriums „Rezept-Austausch" (+33 Wörter) | Befund 1, Variante (a) |
| `01_wettbewerbsanalyse.tex:36` | „ein Risiko **ist** das dichte Umfeld" (+1 Wort) | Handlungsempfehlung 3 |
| `06_evaluation_reflexion.tex` | Entstehungsgeschichte-Absatz vor den Kursänderungs-Absatz gezogen (±0) | Befund 2 |
| `07_iteratives_design.tex:5` | „gilt auch hier **der** Maßstab" (−1 Wort) | Handlungsempfehlung 3 |
| `03_konzept.tex:9` | Absatzteilung vor „Ergänzend plant Resteria …" (±0) | Handlungsempfehlung 3, optional |

---

## Befund 1 des Vorberichts (Struktur, −10) – **behoben, verifiziert**

`01_wettbewerbsanalyse.tex:15` trägt jetzt zwischen der Kommunikations- und der Entdeckungs-Definition: „Rezept-Austausch bezieht sich dagegen allein auf die Rezepte selbst, also darauf, ob eine Plattform sie bereitstellt und weitergibt; die Spanne reicht von der reinen Rezeptdatenbank bis zum Einstellen eigener Beiträge durch Nutzer:innen."

**Spalte „Rezept-Austausch" erneut spaltenweise gegen die neue Definition geprüft – alle sechs Wertungen liegen auf einer Achse und sind im Text gedeckt:**

| Plattform | Wertung | Deckung im Text | Position auf der Spanne |
|---|---|---|---|
| Chefkoch.de | stark | `:3` Upload eigener Rezepte, Bewerten, Kommentieren | oberes Ende (Einstellen eigener Beiträge) |
| TikTok (Food) | mittel | `:5` Rezeptvideos von Creator-Seite, keine strukturierte Rezeptablage | Mitte |
| Restegourmet | mittel | `:7` schlägt Rezepte vor, Kochbuch/Wochenplan; kein Einstellen | bereitstellen ohne Weitergabe |
| `\ac{BMLEH}`-App | mittel | `:7` umfangreiche Rezeptdatenbank | unteres Ende (reine Datenbank) |
| leftovercooking | mittel | `:9` Food-Creator:innen teilen eigene Rezepte | Mitte |
| Foodsharing.de | schwach | `:11` schlägt gar keine Rezepte vor | außerhalb der Spanne |

**Der im Vorbericht benannte Widerspruch ist damit aufgelöst.** `:36` („ohne Austausch zwischen den Nutzer:innen") und `:7` („schafft keinen Ort für Austausch") beziehen sich nach der Definition eindeutig auf die Spalte „Kommunikation \& Community", in der beide Plattformen „schwach" tragen – sie verneinen nicht mehr dasselbe Merkmal, das die Nachbarspalte mit „mittel" bewertet. `:38` (Alleinstellungsmerkmal) und `02_limitationen:7` sind unberührt, wie im Vorbericht gegengeprüft.

**Zusätzlich auf eine neue Kollision geprüft:** Die Definition macht „Rezept-Austausch" nicht deckungsgleich mit „Rezept-Entdeckung". Die beiden Spalten laufen bei drei von sechs Plattformen auseinander (Restegourmet mittel/schwach, `\ac{BMLEH}`-App mittel/stark, TikTok mittel/stark) – sie messen erkennbar Verschiedenes.

## Befund 2 des Vorberichts (Lesefluss, −2) – **behoben, verifiziert**

Neue Absatzfolge in `06_evaluation_reflexion.tex`: `:3` Spannung SDG ↔ Nische → `:5` Entstehungsgeschichte → `:7` Methodenbewertung und die zwei Kursänderungen → `:9` Lehre aus der zweiten. Am gebauten PDF gegengelesen; der Rückbezug „Aus der zweiten dieser Kursänderungen" schließt jetzt unmittelbar an ihre Nennung an.

**Ein Nebeneffekt, den der Vorbericht nicht vorhergesagt hat, fällt zugunsten des Textes aus:** `:7` beginnt mit „Die Kombination aus Wettbewerbsanalyse und literaturbasierter Herleitung …" und folgt jetzt direkt auf `:5`, das genau diese beiden Arbeitsschritte gerade aufgezählt hat („die Sichtung der sechs Plattformen … und die Literaturrecherche zu Nudges und Gamification"). Der Absatzöffner hat damit ein unmittelbares Bezugswort, das er vorher nicht hatte.

---

## Teil-Check A – Formalia

- [PASS] **`check_formalia.py` über `chapters/` + `pages/`: 0 FEHLER**, 49 Hinweise – ausschließlich bekannte Klassen (SATZLAENGE, SATZSCHNITT, TRIAS, ABKUERZUNG für UI/UX/KI, TITEL-DOPPLUNG), keine neue Klasse durch den Delta.
- [PASS] **Zitationen** – `check_bib_keys.py`: alle 9 im Text genutzten Keys existieren in `references.bib`. Keine Zitation im Delta hinzugefügt, entfernt oder verschoben; die Absatzteilung in `03_konzept.tex` lässt beide Hälften mit je eigenen Belegen zurück (`:9` Barker S. 2; `:11` Barker S. 10 und Nivedhitha S. 14).
- [PASS] **Verständlichkeit** – am Fließtext **ohne Tabellenmarkup** neu gemessen: `01_wettbewerbsanalyse.tex` 25,0 (vorher 25,1), `03_konzept.tex` 22,9 (vorher 22,7), alle übrigen 13 Dateien zwischen 10,5 und 21,9. Der neue Definitionssatz (32 Wörter) hat den Durchschnitt seiner Datei nicht erhöht, weil er zugleich die Satzzahl anhebt. Unveränderte Einordnung des Vorberichts: kein gehäufter Verständlichkeitsverstoß, kein Abzug.
- [PASS] **Offene Arbeitsmarker** – kein `% TODO-QUELLE:`, kein `% UNVERIFIED:`.
- [PASS] **`main.tex`/`cover.tex` unverändert**; der Delta berührt ausschließlich `chapters/`.

## Teil-Check B – Argumentationsqualität

Im Delta-Umfang geprüft, nicht neu erhoben. Keine der fünf Änderungen berührt These, Kernargumente, Leitfrage oder einen Pflicht-Punkt aus `typen/projektbericht.md`. Zwei Pflicht-Punkte lagen dennoch im Änderungsumfeld und wurden gegengelesen:

- [PASS] **Limitationen dreischichtig** – `02_limitationen.tex` unverändert, alle drei Grenzen nachgezählt weiterhin vollständig (warum · Mitigation · Folgeschritt).
- [PASS] **Syntheseleistung Durchführung** – `sec:evaluation_reflexion` trägt nach der Umstellung dieselben vier Bausteine (Zielerreichung, Entstehungsgeschichte, Methodenbewertung, Lehre); keiner ist entfallen.

## Teil-Check C – Struktur

- [PASS] **Tabellenwertungen gegen die eigene Kriteriendefinition** – siehe Befund 1 oben. Der einzige FAIL des Vorberichts ist geschlossen.
- [PASS] **Querverweise – Fundstelle *und* Reichweite.** `check_autoref.py`: **29 Verweise · 27 Labels · 29 quittiert, 0 offen.** Fünf Paare mussten in diesem Lauf neu beurteilt werden (siehe „Werkzeug-Fund"); alle fünf einzeln gegen ihre Zielstelle gelesen und mit Begründung in `autoref-state.json` eingetragen:

  | Verweis | Ziel | Ergebnis |
  |---|---|---|
  | `01_kernergebnisse:3` | `sec:wettbewerbsanalyse` | OK – `:36` formuliert die Lücke wörtlich; der weitergehende Anspruch wird in `:5` selbst als „unbelegte Marktbeobachtung" begrenzt |
  | `01_kernergebnisse:7` | `sec:phasenplanung` | OK – Phase 2 (Klick-Prototyp, Woche 3–4) und Phase 4 (Beta-Test, Woche 15–17) liegen beide vor Phase 5 (Launch, ab Woche 18). Marker „vor allem" steht in der Eigenaussage, nicht in der Zuschreibung – keine Reichweiten-Differenz |
  | `01_kernergebnisse:7` | `sec:konzept` | OK – `03_konzept:3` legt die Kooperationen als Teil des Erlösmodells an; die Wachstumsaussage steht im Konjunktiv und wird der Zielstelle nicht zugeschrieben |
  | `02_limitationen:3` | `sec:phasenplanung` | OK – Phase 4 mit Zeitrahmen und Beta-Gruppe; der Limitationssatz bleibt hinter der Zielstelle zurück |
  | `02_limitationen:5` | `sec:iteratives_design` | OK – `07:3` beschreibt die Prüfung von Bedienführungs-Entscheidungen mit externen Testpersonen vor der `\ac{MVP}`-Entwicklung wörtlich |

- [PASS] **Zahlenangaben** – der Delta führt keine neue Zählaussage ein und verändert keine bestehende. Die im Änderungsumfeld liegenden zwei geprüft: „Zwei Stellen erzwangen eine Kursänderung" (`06:7`) steht weiterhin unmittelbar vor „Aus der zweiten dieser Kursänderungen" (`06:9`); „drei Bereiche vier Mockups" (`03:38`) unberührt.
- [PASS] **Front-/Backmatter, Kapitelstufen, Outline** – vom Delta nicht berührt, im Build bestätigt.

## Teil-Check D – Build

- [PASS] **Neubau aus leerem Zustand** (`build/` und `main.pdf` vorher gelöscht), `latexmk main.tex` über die projekteigene `.latexmkrc`, **Exit-Code 0**.
- [PASS] **Log sauber:** 0 Fehler (`^!`), 0 undefinierte Referenzen, 0 undefinierte Zitationen, 0 doppelte Labels, 0 fehlende Dateien, **0 Overfull \hbox**, **0 Overfull \vbox**, **0 Missing character**. 11 Underfull \hbox, sämtlich in schmalen Tabellenspalten – kein Randüberstand, kein Formfehler.
- [PASS] **Projekt-Root sauber** – nach dem Lauf keine `.aux`, `.bcf`, `.log`, `.out`, `.run.xml`, `.toc`, `.bbl`, `.blg` im Root; alle Hilfsdateien in `build/`.
- [PASS] **Seitenumfang Textteil: 10 Seiten von 7–10.** „1 Einleitung" auf PDF-Seite 6 (gedruckt 1), Literaturverzeichnis auf PDF-Seite 16 (gedruckt 11); letzte Textseite ist PDF-Seite 15 = gedruckt 10. 23 PDF-Seiten gesamt. **Die +33 Wörter haben die Seite nicht gekippt.** `check_umfang.py`: 3.743 Wörter gegen das Ziel 2.625–3.750 (Einleitung 496 / Durchführung 2.854 / Fazit 393).
- **Weißraum neu gemessen:** unterste Fließtextzeile der letzten Textseite bei y ≈ 188,4 pt, Satzspiegel-Unterkante bei y ≈ 56,7 pt, Zeilenabstand 16,4 pt → **≈ 132 pt ≈ 8 freie Zeilen**. Der Vorbericht maß ≈ 173 pt ≈ 10 Zeilen; die Überarbeitung hat rund zwei Zeilen gekostet, die Prognose des Vorberichts („netto rund eine Zeile") lag knapp zu niedrig.
- [PASS] **PDF-Aktualität, dreifach abgeglichen.** Der Neubau ist über alle 23 Seiten **textidentisch** mit dem vorher im Arbeitsverzeichnis liegenden `main.pdf` **und** mit der abgabefertig benannten Kopie `20260731_Pelz_Sascha_3210267_DLBMIMPFS01-01.pdf`. Beide tragen die vier Textänderungen (per Phrasensuche im extrahierten Text belegt). Es besteht kein Aktualitätsproblem – nur der Versionierungsschritt steht aus.

## Teil-Check E – Abgabe (informativ, **kein** Score-Abzug – Festlegung `MEMORY.md` 19.07.2026)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben.
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen.
- [PASS] Umfang im Soll – Spiegel aus Teil-Check D (10 von 7–10 Seiten).
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko).
- [OFFEN] LanguageTool-Durchgang lokal über den Gesamttext.

## Teil-Check F – Literaturverzeichnis

- [PASS] `check_bib_hygiene.py`: 10 Einträge, **0 Fehler, 0 Hinweise**. `references.bib` liegt außerhalb des Deltas – die Vollprüfung des Abgabe-Audits (gerendertes Verzeichnis, Stichprobe über vier Einträge gegen die Titelei) bleibt gültig und wurde nicht wiederholt.

## Teil-Check G – Quellentreue

- [PASS] **19 Zitationen in 15 Dateien · 19× FUNDSTELLE OK · 0 offen** (`quellencheck.md`).
- **Keine Invalidierung durch den Delta.** Weder die Absatzteilung in `03_konzept.tex` noch die Absatzverschiebung in `06_evaluation_reflexion.tex` hat einen Trägersatz verändert – Trägersätze sind Sätze, keine Absätze, und kein Satz mit Zitation wurde angefasst. Keine Befunde der Klassen WORTLAUT, ZITAT WEICHT AB, SEITE VERDÄCHTIG, SEITE AUSSERHALB, NICHT GEFUNDEN, CLAIM SCHÄRFER, RENTIERT NICHT; kein `[NOTIZ-DUBLETTE]`, kein `[NOTIZ-FREMDER-AUTOR]`.

> **Grenze dieses Checks, unverändert:** Teil-Check G prüft Fundstelle und Wortlaut, **nicht die Reichweite**. Die Reichweitenprüfung über alle 19 Zitationen hat die Gegenlesung Runde 9 (29.07.) geleistet; ihre Befunde sind abgearbeitet. Der Delta hat keinen zitierenden Satz berührt.

## Teil-Check H – Lesefluss (geänderte Dateien am Stück gelesen, nicht am Diff)

Alle vier geänderten Subsections vollständig am Stück gelesen, wie es der Re-Audit-Umfang ausdrücklich verlangt.

- [PASS] **Anschlüsse** – `06:9` „Aus der zweiten dieser Kursänderungen" zeigt nach der Verschiebung auf den unmittelbar vorangehenden Absatz. `06:5` „Der Weg zu diesem Konzept" hat sein Bezugswort im Kapitelkontext. `03:11` „Ergänzend" schließt an den Punktezähler-Satz an. `07:5` „gilt auch hier **der** Maßstab" ist selbsttragend, weil der Satz die Zahl („von fünf Testpersonen") selbst nennt – die vollständige Zitation steht im Vorabsatz. Kein ANAPHER-Hinweis des Skripts, keine satzinterne Ausnahme gefunden.
- [PASS] **Absatzöffner** – alle fünf berührten Absätze beginnen mit einer Aussage.
- [PASS] **Absatzlänge und Rhythmus** – die Teilung in `03_konzept.tex` entschärft den dichtesten Absatz der Arbeit (vorher sieben Sätze, vier Belege) auf zwei Hälften mit je eigenem Belegbestand.

---

## Werkzeug-Fund (kein Textbefund, kein Score-Abzug)

**`check_autoref.py` löscht bei einem eingegrenzten Lauf die Urteile außerhalb der Eingrenzung.** Die Funktion `aufraeumen()` entfernt jedes Urteil, dessen Paar im aktuellen Lauf nicht vorkommt – bei `--datei`/`--kapitel` sind das alle Paare der übrigen Kapitel. Die Überarbeitungssitzung hat `check_all.py --kapitel chapters/02_durchfuehrung --mit-quellen` gefahren; dabei sind die **fünf Urteile der Fazit-Verweise** aus `autoref-state.json` verschwunden. Nachweis: Die im Commit `1e4761d` eingecheckte Zustandsdatei enthält 24 Einträge, sämtlich aus `chapters/02_durchfuehrung/`, keinen einzigen aus `chapters/03_fazit/`.

**Folge für den Vorbericht:** Dessen Aussage „Alle **29** internen Verweise einzeln gegen ihre Zielstelle gelesen und in `autorefcheck.md` mit Begründung quittiert" war zum Zeitpunkt des Schreibens zutreffend, ließ sich aber nicht mehr belegen – die fünf Fazit-Begründungen waren gelöscht. Sie sind in diesem Lauf **neu am Text geprüft** und mit eigener Begründung eingetragen (Tabelle in Teil-Check C). Der Prüfstand ist damit wiederhergestellt, nicht nur der Zähler.

**Warum das mehr ist als Buchführung:** Der Nutzen des Skripts liegt darin, dass ein einmal quittiertes Paar nie wieder gelesen werden muss und ein bewegtes Ziel automatisch auffällt. Ein stiller Urteilsverlust kehrt beides um – die Arbeit war getan, die Spur weg, und beim nächsten Lauf sieht der Fund wie ein neuer Verweis aus. Als **P37** in `SKILL-ANPASSUNGEN.md` aufgenommen (Vorschlag: `aufraeumen()` nur beim ungefilterten Lauf ausführen).

---

## Kosmetische Hinweise (kein Score-Abzug, kein Handlungsdruck)

- **`06_evaluation_reflexion.tex:5`** bleibt ein Ein-Satz-Absatz von 50 Wörtern zwischen zwei mehrsätzigen Absätzen. Der Vorbericht hatte das als zweite Hälfte von Befund 2 mitgenannt, seine eigene Fix-Empfehlung („`:7` vor `:5` ziehen, ±0 Wörter") aber bewusst darauf beschränkt, die Unterbrechung aufzulösen. Das ist eingetreten: Der Absatz trägt die Erzählung jetzt, statt sie zu unterbrechen – die inhaltliche Begründung des Abzugs entfällt damit. Der lange Satz ist eine geordnete „zuerst/dann/anschließend"-Kette und beim ersten Lesen verständlich. **Kein Abzug.**
- **Geviertstriche in den KI-Mockups** (Style Tile „Salbeigrün — Primär", Profil „Level 4 — Resteheld:in") – im Bild, nicht im Text, von der Geviertstrich-Regel nicht erfasst. Eine Korrektur hieße neue Mockup-Runde.
- **`check_aussenwelt.py`-Zustandsdatei** – 14 Kandidaten stehen unquittiert auf „NEU", obwohl `faktencheck-bericht.md` sie inhaltlich abgearbeitet hat. Reine Buchführung.
- **`check_status.py`** – 0 Fehler, 15 `DATEI-OHNE-ZEILE`-Hinweise. Projektkonvention: Die Statustabelle führt Hauptkomponenten, nicht jede Subsection-Datei.
- **`SKILL-ANPASSUNGEN.md` führt „2 Punkte OFFEN"** (P35, P36), obwohl beide erkennbar umgesetzt sind – `check_autoref.py` samt `autoref-state.json` (P35) und `check_aussenwelt.py` samt `faktencheck`-Skill und `faktencheck-state.json` (P36) existieren und laufen. Statuszeile veraltet.

---

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

1. **Wortlaut der zitierten Claude-Design-Prompts** | `pages/appendix.tex`, Zeilen 30, 39, 46, 53, 60 (`\quelle{}`-Zeilen der fünf Abbildungen) | Stimmt der zitierte Prompt-Text wörtlich mit der Eingabe im Claude-Design-Chat überein, einschließlich der Folge-Prompts bei Rettungs-Feed und Profil? | Der Chatverlauf liegt außerhalb des Repositorys; ich kann nur prüfen, dass die Zitate formal korrekt gesetzt und in sich geschlossen sind. **Zur Entlastung:** Der Zitierleitfaden (Kap. 2.2.5) verlangt nur „den verwendeten Prompt" im Singular – ein fehlender Folge-Prompt wäre kein Regelverstoß, ein falsch wiedergegebener schon.
2. **Aktualität der IU-Leitfäden zum Abgabezeitpunkt** | `sources/Zitierleitfaden.pdf` und `sources/Richtlinien für die Gestaltung wissenschaftlicher Arbeiten.pdf` (Datumszeile auf der Impressumsseite) gegen den Prüfungs-Guide auf myCampus; Register `_shared/quellen-versionen.md` | Tragen beide dort ebenfalls den Stand 01.10.2025? | Die Spalte „zuletzt vom Nutzer bestätigt" ist im Register für alle Zeilen leer. Die PDFs wurden am 25.07.2026 ausgetauscht und das Destillat am 28.07.2026 dagegen geprüft – die Regeln sind mit hoher Wahrscheinlichkeit aktuell, formal bestätigt ist es nicht. Laut Richtlinien gilt die zum Abgabezeitpunkt gültige Fassung. myCampus kann ich nicht abrufen.
3. **Namensverfügbarkeit „Resteria"** | DPMA-Markenregister und `.de`-Domain | keine eingetragene Marke und keine aktive Domain im selben Themenfeld | Nutzer-Restpflicht seit Projektbeginn; nicht abgabekritisch.

---

## Claims

- **Ungesicherte FACTUAL CLAIMS**: keine. Der Delta führt keine neue Außenweltbehauptung ein – die Definition in `:15` ist eine methodische Setzung dieser Arbeit, keine Aussage über eine Plattform. `faktencheck-bericht.md` (30./31.07.) bleibt vollständig abgearbeitet.
- **Fehlende OWN WORK-Markierungen**: keine.
- **Ungenutzte Bib-Einträge (Aufräumhinweis)**: `pexelsHasanbekavaBasket` – Fehlalarm durch den Prüfumfang, der Eintrag wird in `pages/appendix.tex:21` über `\citeauthor`/`\citeyear` genutzt, das Skript scannt nur `chapters/`. Am gerenderten Verzeichnis verifiziert.
- **Volltexte ohne Bib-Verweis (Aufräumhinweis)**: drei Dateien in `sources/literatur/` – Krug und Norman (bewusst nicht zitiert) sowie die Preprint-Fassung von Vittuari (durch die Verlagsfassung ersetzt).

---

## Punkteabzug im Detail

| Kategorie | Abzug | Begründung |
|---|---|---|
| Struktur-Verstoß (Teil-Check C) | **0** | Befund 1 des Vorberichts behoben und spaltenweise gegengeprüft |
| Lesefluss-Befund (Teil-Check H) | **0** | Befund 2 des Vorberichts behoben, am PDF gegengelesen |
| **Summe** | **0** | **Score 100/100 – abgabereif** |

Keine Abzüge in den Kategorien BBT-Keys, Pflicht-Punkte der Typ-Datei, Formalia, Build, undefinierte Referenzen, Seitenumfang, Literaturverzeichnis, Anti-KI-Stil, Verständlichkeit, Quellentreue.

**Zur Belastbarkeit dieses Scores:** Teil-Check D ist gelaufen und hat den Seitenumfang **gemessen** (nicht geschätzt); der Score-Deckel von 89 für einen übersprungenen Build greift nicht. Teil-Check F wurde im Delta-Umfang nur über das Skript geführt – die Vollprüfung des Abgabe-Audits vom selben Tag bleibt gültig, weil `references.bib` außerhalb des Deltas liegt.

---

## Bewertungsschwerpunkte (Projektbericht) – Änderungen gegenüber dem Abgabe-Audit

| Kriterium | Gewicht | Status | Änderung durch die Überarbeitung |
|---|---|---|---|
| **Qualität** | 25 % | ABGEDECKT | unverändert |
| **Prozess** | 25 % | ABGEDECKT | unverändert |
| **Transfer** | 15 % | ABGEDECKT | unverändert |
| **Kreativität** | 15 % | ABGEDECKT | **Einschränkung entfällt** – der Vergleichsteil trägt die Wertungen jetzt vollständig im Text |
| **Dokumentation** | 10 % | ABGEDECKT | **Einschränkung entfällt** – die Entstehungsgeschichte eröffnet die Reflexion, statt sie zu unterbrechen |
| **Ressourcen** | 10 % | ABGEDECKT | unverändert |

---

## Lieferobjekt-Abgleich

Vom Delta nicht berührt; der Abgleich des Abgabe-Audits (alle sechs Lieferobjekte vorhanden, alle fünf Bilddateien einzeln per `Read` gesichtet, jede im Text behauptete Oberflächen-Eigenschaft am Bild belegt) bleibt gültig. Der einzige berührte Punkt ist `tab:wettbewerbsvergleich` – dort ist keine Zelle geändert, nur die zugehörige Kriteriendefinition ergänzt worden.

---

## Handlungsempfehlungen

**Am Text ist nichts mehr offen.** Es bleiben zwei Versionierungsschritte und die Nutzer-Checkliste.

1. **`main.pdf` einchecken.** `git status` meldet `M main.pdf` (der Neubau dieses Audits). Das eingecheckte PDF aus Commit `1e4761d` ist inhaltlich identisch – es geht um die Versionierung, nicht um Aktualität.
2. **Abgabekopie prüfen, nicht neu erzeugen.** `20260731_Pelz_Sascha_3210267_DLBMIMPFS01-01.pdf` liegt untracked im Root und ist über alle 23 Seiten textidentisch mit dem Neubau. Sie trägt die vier Textänderungen bereits. Nur falls nach diesem Audit noch etwas geändert wird, muss sie ersetzt werden.
3. **Optional, ohne Score-Wirkung:** die fünf kosmetischen Punkte oben – keiner davon berührt die Bewertung.

Ein weiteres Audit ist nicht nötig. Wird der Text nicht mehr angefasst, ist dieser Stand der Abgabestand.

---

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

1. **Eidesstattliche Erklärung elektronisch über myCampus abgeben** – ohne sie nimmt Turnitin die Einreichung nicht an. Das Fristfeld in `CLAUDE.md` steht auf `[offen]`.
2. **Einreichungs-Anleitung im myCampus-Kurs lesen.**
3. **LanguageTool-Durchgang lokal über den Gesamttext** (3.743 Wörter). Die Sprachstichprobe des Abgabe-Audits hat zwei Absätze je Hauptkapitel geprüft und ersetzt keine Vollprüfung.
4. **Die Arbeit einmal am fertigen PDF am Stück durchlesen.**
5. **Keine externe Plagiatssoftware vorab** – Selbsttreffer-Risiko bei Turnitin.
6. **Prompt-Wortlaut der fünf Abbildungen gegen den Claude-Design-Chatverlauf abgleichen** (siehe „Bitte manuell prüfen", Punkt 1).
7. **Auf myCampus prüfen, ob Zitierleitfaden und Gestaltungsrichtlinien noch den Stand 01.10.2025 tragen** (Punkt 2). Danach in `_shared/quellen-versionen.md` die Spalte „zuletzt vom Nutzer bestätigt" setzen.
8. **Namensverfügbarkeit „Resteria"** (DPMA, `.de`-Domain) – nicht abgabekritisch, aber offen.
9. **Das eingereichte PDF muss aus dem letzten Build stammen.** Wird nach diesem Audit noch etwas geändert: neu bauen, Seitenzahl gegen 7–10 prüfen (Reserve auf der letzten Textseite ≈ 8 Zeilen), Abgabekopie neu erzeugen.
