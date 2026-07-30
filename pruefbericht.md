# Prüfbericht – Projektbericht

**Datum**: 30.07.2026 · **Geprüfter Stand**: alle Kapitel (Textstand nach der Cold-Read-Session, `main.pdf` in dieser Session neu gebaut) · **Audit-Typ**: Abgabe-Audit
**Score: 72/100 – Überarbeitung empfohlen**

> Einordnung vorab: Alle vier Befunde sind **mechanisch**. Keiner betrifft These, Argumentation, Aufbau oder eine Pflichtregel des Papiertyps. Drei der vier liegen außerhalb der Kapiteldateien (ein Titelblatt-Makro, zwei Zotero-Einträge), der vierte ist eine Ein-Wort-Korrektur. Der Rückgang gegenüber dem letzten 100/100 kommt nicht von neuen Textfehlern, sondern daher, dass Teil-Check F erstmals Eintrag für Eintrag gegen die Volltext-Deckblätter gelaufen ist und dass `pages/meta.tex` erstmals außerhalb der Skript-Ausnahmeliste geprüft wurde.

## Teil-Check A – Formalia

- [PASS] Zitationen – `check_bib_keys.py`: 9/9 genutzte Keys existieren. Alle stellenbezogenen Zitate tragen `[S. X]` bzw. `[Kap. X]`; kein SEITENANGABE-Fund. Narrative und parenthetische Form sauber gemischt.
- [PASS] Eigene Werke – alle 9 Floats tragen eine `\quelle{}`-Zeile, Caption jeweils vor `\label{}`, kein `\cite{}` auf Eigenwerke. KI-Abbildungen nach IU-Muster („Erstellt mit dem Prompt „…" durch Anthropic, 2026").
- [PASS] Pronomen – kein „ich/wir/man", Selbstbezug durchgehend pronomenfrei (Einzelarbeit).
- [FAIL] LaTeX-Format – **Geviertstrich im Arbeitstitel** (Befund 1).
- [PASS] Akronyme – BMLEH, MVP, SDG, SEQ alle definiert **und** verwendet (7 / 11 / 2 / 2 Fundstellen), kein verwaister Eintrag im Abkürzungsverzeichnis.
- [PASS] Cross-References & Labels – 0 undefinierte Referenzen im Build; `\autoref`-Ziele stichprobenweise **semantisch** gegengeprüft (Klick-Prototyp-Test ↔ `tab:phasenplanung`, Challenge-Rangliste ↔ `sec:community_und_feedback`, Rezeptbestand ↔ `sec:phasenplanung`) – alle treffen inhaltlich.
- [PASS] Anti-KI-Stil – 0 FEHLER im Skript. TRIAS 4× in zwei Dateien, jeweils sachlich genau drei Dinge (drei Kategorien, drei Hauptbereiche, drei Risiken). Keine Floskel-Öffner, keine rhetorischen Fragen, keine Kontrastfigur-Häufung.
- [PASS] Verständlichkeit – Fachbegriffe bei Erstnennung erklärt (Nudge, Drivers/Levers, MVP, Fairteiler, SEQ, Think-Aloud). Satzlängen siehe „Kosmetische Hinweise".
- [PASS] Offene Arbeitsmarker – kein `% TODO-QUELLE:`, kein `% UNVERIFIED:`.

## Teil-Check B – Argumentationsqualität (nur Pflicht-Punkte der Typ-Datei als FAIL)

- [PASS] These erkennbar – Leitfrage (Konzeption einer spezialisierten Plattform) und These (die Lücke zwischen Reste-Matching und echter Community lässt sich durch deren Verbindung schließen) sind getrennt; normative Ebene vorhanden.
- [N.A.] Forschungslücke in Einleitung – laut `typen/projektbericht.md` optional; die Marktlücke ist trotzdem ausformuliert.
- [PASS] Aktualität/Zeitbezug in Einleitung – SDG 12.3 mit Zielhorizont 2030.
- [PASS] Gegenargumente reflektiert & entkräftet – `01_wettbewerbsanalyse.tex:34` (reine Community-Plattform würde genügen) samt Entkräftung; `03_konzept.tex:11` grenzt die Soma-Evidenz gegen die eigene Mechanik ab.
- [PASS] Syntheseleistung pro Hauptkapitel – Einleitung schließt mit der Lücke, Durchführung mit `06_evaluation_reflexion`, Fazit mit Kernergebnissen und Grenzen.
- [PASS] Limitationen dreischichtig – alle drei nachgezählt: warum · Mitigation · Folgeschritt jeweils vorhanden und benannt.
- [N.A.] Ergebnisse ≠ Interpretation – nur empirische Seminararbeit.
- [PASS] Typspezifisch – dritte Person streng ✓ · „Quelle: Eigene Darstellung." auf jeder eigenen Abb./Tab. ✓ · Produkt sichtbar dokumentiert ✓ · **Phasenplanung als Tabelle** ✓ · Reflexion + Theorie-Praxis-Bezug ✓ · 9 zitierte Werke + 1 Bildquelle, im Richtwert 5–10 ✓
- [PASS] Leitfragen aus `aufgabe.md` beantwortet – alle drei Teilaufgaben real ausgeführt und mit eigener Subsection sichtbar (`sec:wettbewerbsanalyse`, `sec:konzept`, `sec:iteratives_design`).
- [PASS] Abhakliste vollständig – Rezept-Upload, Bewertungs-/Kommentarsystem, personalisierte Empfehlungen, Menüplanung/Reste-Journal im Konzept; Gruppen/Foren und Event-Kalender jeweils **begründet** ausgelassen; die `[VERENGT]`-Zielgruppe ist in `02_zielsetzung_und_verengung.tex` begründet.
- [PASS] Dimensionsabgleich gegen die Abdeckungs-Tabelle in `kapitelplan.md:162` – alle sechs Kriterien mit je allen Dimensionen im Text auffindbar (siehe „Bewertungsschwerpunkte").

## Teil-Check C – Struktur

- [PASS] ½-Seiten-Regel – Minimum 136 Wörter (`03_vorgehen_und_aufbau.tex`), knapp unter der 150-Wort-Heuristik. Bewusst so: Die Datei wurde in Runde 4 gezielt gegen ein Unterschreiten geschützt und füllt gesetzt rund eine halbe Seite. Kein FAIL.
- [PASS] Max. 3 Kapitelstufen – zwei Stufen, mindestens zwei Unterpunkte je Kapitel (3 / 7 / 2).
- [PASS] Front-/Backmatter – Titelblatt, Inhalts-, Abbildungs- (5 Einträge), Tabellen- (4), Abkürzungs-, Literatur- und Anhangsverzeichnis (3 Anhänge). Je Anhang mindestens ein wörtlicher Textverweis ✓.
- [PASS] Outline-Check – Einleitung (Umfeld/Problem/Ziel/Vorgehen) → Hauptteil (Analyse, Konzept, Community, Iteration, Phasen, Evaluation) → Fazit (Kernergebnisse, Limitationen); deckungsgleich mit dem Gerüst aus `typen/projektbericht.md`.
- [FAIL] Roter Faden – **Ankündigung „die drei von der Aufgabenstellung genannten Zwecke" wird nur zweifach eingelöst** (Befund 2).
- [PASS] Zählangaben – alle 24 vom Skript gemeldeten Zählaussagen nachgezählt (sechs Plattformen, drei Kategorien, drei Vertreter, drei Merkmale, zwei Anforderungen, fünf Phasen, drei Risiken, vier Mockups, drei Hauptbereiche, sechs Vertreter, ein bis drei Vertreter je Kategorie). Alle stimmen.
- [PASS] Tabellenwertungen spaltenweise – „Kommunikation \& Community" folgt exakt der eigenen Definition in `01_wettbewerbsanalyse.tex:13` (Creator-Following zählt abgeschwächt → leftovercooking „mittel"; reine Bewertungsfunktion zählt nicht → Restegourmet „schwach"). Kein Maßstabsbruch, kein Kriterium ist ein Gesamturteil.
- [PASS] Akteurskonsistenz – die Freemium-Trennlinie („nur Komfortfunktionen kostenpflichtig; Reste-Matching, Rettungs-Feed und Challenges kostenlos") wird an keiner späteren Stelle unterlaufen.
- [PASS] Offene Einwände – jeder selbst erhobene Einwand wird beantwortet oder als Limitation ausgewiesen; der Vorbehalt „keine Primärdaten" landet als Limitation 1.
- [PASS] Redundanz – Marktlücke: Erstnennung (Einleitung, Behauptungsebene) → Beleg (Wettbewerbsanalyse) → Wiederaufnahme (Fazit). Regelkonform. Reflexion (Vorgehen) und Fazit (Ergebnis/Grenzen) sind sauber getrennt.
- [PASS] Wirkungsaussagen – „sichtbar machen, wie viel eine Person einspart" ist durch die Kennzahl „12,4 kg Lebensmittel gerettet" im Profil-Mockup gedeckt; „Reste-Journal protokolliert die verwerteten Zutaten im Profilbereich" durch den Bereich „Reste-Journal" mit Datums-, Punkte- und Zutaten-Tags im selben Screen. Beides am Bild geprüft, nicht am Text.

## Teil-Check D – Build

- [PASS] Kompiliert fehlerfrei – `latexmk -g -lualatex main.tex`, Exit 0, 23 PDF-Seiten. **0 Zeilen `^!`/`Error`, 0 `Overfull \hbox`, 0 `Missing character`.**
- [PASS] Keine undefinierten Referenzen/Zitationen, keine fehlenden Bilder, keine doppelten Labels.
- [PASS] Seitenumfang Textteil – **10 Seiten von 7–10** (gedruckt 1–10 = PDF-Seite 6–15; Literaturverzeichnis ab gedruckt 11 = PDF-Seite 16). Am gebauten PDF gemessen, nicht geschätzt. `check_umfang.py`: 3.701 Wörter im Zielkorridor 2.625–3.750.
- Weißraum-Diagnose (Teil-Check D 3a): nicht ausgelöst, weil der Umfang **innerhalb** der Vorgabe liegt. Zur Einordnung für spätere Ergänzungen: Die Reserve auf der letzten Textseite lag zuletzt bei rund 37 pt (≈ 2 Zeilen); jede Zugabe braucht eine Gegenfinanzierung.
- Projekt-Root nach dem Lauf frei von Build-Artefakten (kein `main.aux`/`.bcf`/`.log`/`.toc` im Root) ✓.

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [PASS] Umfang im Soll (Spiegel aus Teil-Check D): 10 von 7–10 Seiten
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen – Turnitin würde den eigenen Upload als Treffer werten
- [OFFEN] LanguageTool-Durchgang lokal über den Gesamttext – die Sprachstichprobe unten ersetzt keine Vollprüfung

## Teil-Check F – Literaturverzeichnis

- [PASS] `check_bib_hygiene.py`: 10 Einträge, 0 Hinweise.
- [PASS] Gerendertes Verzeichnis gelesen (PDF-Seite 16): Alphabetik korrekt, Sentence Case bei allen englischen Titeln, deutscher Titel korrekt großgeschrieben, keine kaputten Sonderzeichen, keine Verlagsorte, kein Abrufdatum, DOI statt URL wo vorhanden, Autorennamen korrekt als „Nachname, Initiale." – der im Vorbericht behobene Körperschafts-Fehler bei Nielsen und Sauro & Lewis ist verifiziert weg.
- [FAIL] **Artikelnummer als Seitenzahl** bei zwei Einträgen (Befund 3).
- [FAIL] **Erlhofer-Eintrag weicht vom Volltext ab** (Befund 4).

## Teil-Check G – Quellentreue (Volltextabgleich)

- [PASS] **20 Zitationen geprüft · FUNDSTELLE OK 20 · offen 0** (Details: `quellencheck.md`)
- Befunde je Klasse: **keine.** Kein WORTLAUT, kein ZITAT WEICHT AB, kein SEITE AUSSERHALB, kein CLAIM SCHÄRFER, kein NICHT PRÜFBAR, kein RENTIERT NICHT.
- In diesem Lauf **neu am Volltext verifiziert** (nicht aus dem Erledigt-Stand übernommen):
  - **Soma S. 10–12** → S. 11 nennt 9/56 Workshop-Teilnehmende (16 %) und die Absagegründe, S. 12 fasst zusammen: „participation rates in the Information group were high, in the Community group they were very low, and they were relatively high in the Game group". Der Trägersatz gibt das **enger** wieder als die Quelle. Rentabilität nach der Cold-Read-Änderung geprüft: Die Rahmung „Den Anstoß dazu gab" bleibt schwach genug für den zwei Sätze später stehenden Übertragungsvorbehalt.
  - **Erlhofer Kap. 17.2.2** → Praxistipp „Fünf Test-User reichen meist" deckt „schwerwiegende, mehrfach auftretende Bedienhürden" exakt.
  - **Nielsen Kap. 6.8** (gedruckte S. 195) → „identify the users' major misconceptions" plus die ausdrückliche Abgrenzung gegen „performance measurement" – deckt beide Hälften des Trägersatzes.
  - **Sauro & Lewis Kap. 8** (gedruckte S. 218) → „the SEQ simply asks participants to assess the overall ease of completing a task … we recommend using the 7-point version". Die Erfolgsschwelle „Mittelwert ≥ 5" steht im Text ausdrücklich als **eigene Festlegung** – am Volltext gegengeprüft, dort existiert keine solche Regel.
- **Tooling-Korrektur in diesem Lauf, kein Textbefund**: Für `nivedhithaHowGreenSocial2024` war ein Seitenversatz von **+9** gespeichert; das Skript prüfte deshalb PDF-Seite 23 (das Literaturverzeichnis der Quelle) statt der zitierten S. 14. Am PDF verifiziert, dass gedruckte S. 14 = PDF-Seite 14 ist (Kopfzeile „14 of 29") und dort wörtlich steht: „the direct effect of green self-identification on PEB is insignificant, as the 95 % CI includes 0, thus rejecting H1" sowie der signifikante Pfad über *collective intention* (0,246, p < .05). Versatz auf 0 gesetzt. **Die drei Nivedhitha-Zitationen waren inhaltlich richtig – geprüft wurde nur die falsche Seite.**
- **Migration, kein inhaltlicher Neubefund**: Die drei Zitationen in der Zelle „Rettungspunkte \& Reste-Level" (`03_konzept.tex:25`) kamen erstmals mit dem neuen Trägersatz-Zuschnitt (Zeilenkopf + Zelle statt 1.530 Zeichen Umfeld) zurück. Zellentext inhaltlich unverändert; die drei zitierten Seiten sind in diesem Lauf an je zwei weiteren Fundstellen am Volltext bestätigt. Der `SEITE VERDÄCHTIG`-Status war dort ein Heuristik-Fehlalarm – die deutschen Stichworte der Zelle haben keine Begriffsüberschneidung mit dem englischen Volltext.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

> **Punkt 1 ist am 30.07.2026 in der Überarbeitungs-Session aufgelöst worden** – siehe „Nachtrag zur Überarbeitung" am Dateiende. Ergebnis: Erscheinungsjahr **2018**, Titel ohne Untertitel, beides am DNB-Katalogisat belegt. Der Punkt bleibt nur als Historie stehen.

1. ~~**Erscheinungsjahr Erlhofer & Brenner**~~ **ERLEDIGT (30.07.2026)** | `references.bib` → `erlhoferWebsiteKonzeptionUndRelaunch2017`, Feld `date` | Aufgelöst über die SRU-Schnittstelle der Deutschen Nationalbibliothek (`services.dnb.de/sru/dnb`, ISBN 9783836245579): MARC 250 „1. Auflage", MARC 264 „Bonn : Rheinwerk Verlag : 2018". Das Impressum des E-Books („1. Auflage 2018") ist damit die richtige Angabe, die OPF-Metadaten (`2017-11-07`) sind es nicht. **Der Eintrag muss auf 2018.**
2. **Wortlaut der zitierten Claude-Design-Folge-Prompts** | `pages/appendix.tex`, die vier `\quelle{}`-Zeilen zu `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_feed`, `fig:mockup_profil` | Stimmt, wenn der zitierte Text wortgleich dem entspricht, was im Claude-Design-Chat eingegeben wurde | Der Chatverlauf liegt außerhalb des Repositorys. Zur Einordnung: Der Zitierleitfaden verlangt nur **den** Ursprungsprompt (Singular); die Folge-Prompts sind Projektkonvention, ihr Fehlen wäre kein Regelverstoß – eine **falsch wiedergegebene** Formulierung dagegen schon.

## Claims

- Ungesicherte FACTUAL CLAIMS: **keine.** Jede Außenweltaussage ist entweder belegt (20/20 Zitationen am Volltext geprüft) oder als eigene Sichtung ausgewiesen (Methodensatz `01_wettbewerbsanalyse.tex:13` mit Erhebungszeitraum Juli 2026 und `\quelle{}`-Zeile unter `tab:wettbewerbsvergleich`).
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: `pexelsHasanbekavaBasket` – **kein echter Fund**. Der Eintrag wird über `\citeauthor`/`\citeyear` in der Quellenzeile von `tab:persona` genutzt; `check_bib_keys.py` erkennt nur `\parencite`/`\textcite`/`\cite`. **Nicht entfernen.**
- Volltexte ohne Bib-Verweis (3): die beiden EPUBs von Krug und Norman (aus der Vorarbeit, hier nicht zitiert) und `Vittuari2023_DriversLeversFoodWaste.pdf` (Preprint-Fassung neben der zitierten Verlagsfassung). Alle drei unschädlich.

## Punkteabzug im Detail

- Formalia-Verstoß (Teil-Check A): −8 (1 Vorkommen, gedeckelt bei −32)
- Struktur-Verstoß (Teil-Check C): −10 (1 Vorkommen, gedeckelt bei −30)
- Literaturverzeichnis-Verstoß (Teil-Check F): −10 (2 Regelverstoß-Klassen à −5, gedeckelt bei −15)
- **Summe: −28 → 72/100**

## Befunde im Detail

### Befund 1 – Geviertstrich im Arbeitstitel (Formalia, −8)

`pages/meta.tex:7`:

```
\newcommand{\PaperTitle}{Resteria — Konzeption einer Social-Media-Plattform für nachhaltigkeitsorientierte Hobbyköch:innen}
```

Das Zeichen zwischen „Resteria" und „Konzeption" ist U+2014 (Geviertstrich), nicht U+2013 (Halbgeviertstrich). `hard-rules-formal.md` → Schreibstil führt den Geviertstrich als **FEHLER**-Klasse: englische Konvention, im Deutschen unüblich, und ein von Turnitin ausgewertetes KI-Erkennungsmerkmal. Der Titel steht auf dem Titelblatt und in den PDF-Metadaten – an der sichtbarsten Stelle der ganzen Arbeit.

Warum das bisher niemand gefunden hat: `check_formalia.py` überspringt `pages/meta.tex` als Vorlagen-Gerüst und weist das in der Ausgabe sogar aus. Der Titel ist aber selbst geschriebener Text, kein Gerüst.

**Fix**: das Zeichen durch „–" ersetzen. Ein Zeichen, keine inhaltliche Änderung, keine Auswirkung auf den Seitenumfang. `meta.tex` ist ausdrücklich editierbar.

### Befund 2 – Ankündigung „drei Zwecke", eingelöst werden zwei (Struktur, −10)

`chapters/02_durchfuehrung/03_konzept.tex:16`:

> Gegenüber den untersuchten Plattformen ist neu, wie Resteria **die drei von der Aufgabenstellung genannten Zwecke** mit dem Zero-Waste-Fokus verbindet: Die verpflichtende Zutaten-Kennzeichnung macht das **Rezept-Teilen** selbst zur Verwertungshandlung, die monatlich wiederkehrende Zero-Waste-Woche ersetzt Forum und Gruppen als Anlass für **gegenseitige Inspiration**, und die Kopplung von Menüplanung und Reste-Journal an die Rettungspunkte verankert den Zero-Waste-Kern in der täglichen Nutzung.

Die Aufgabenstellung nennt drei Zwecke: Rezept-Teilen, **Kochtipp-Austausch**, gegenseitige Inspiration (`aufgabe.md:15`). Der Satz löst Rezept-Teilen und gegenseitige Inspiration ein; das dritte Glied betrifft Menüplanung und Reste-Journal – keinen der drei Zwecke. Der Kochtipp-Austausch wird im **unmittelbar folgenden Satz** ausdrücklich der Gegenkategorie zugeschlagen („Rezept-Upload, Bewertungs- und Kommentarsystem sowie personalisierte Empfehlungen übernimmt Resteria dagegen bewusst als Formate aus etablierten Rezept-Communitys"). Die Ankündigung widerspricht damit dem eigenen Folgesatz.

Das wiegt schwerer als eine gewöhnliche Zahlendrift, weil dieser Absatz die einzige zusammenhängende Innovationsaussage der Arbeit ist und damit das Bewertungskriterium **Kreativität (15 %)** allein trägt. Wer die drei Zwecke gegenzählt, findet an der prominentesten Stelle eine Ankündigung, die der nächste Satz zurücknimmt.

**Fix (eine Zeile, ±0 bis +2 Wörter, drei Varianten):**
- **(a) empfohlen** – „…, wie Resteria **zwei der drei** von der Aufgabenstellung genannten Zwecke mit dem Zero-Waste-Fokus verbindet": kleinster Eingriff, macht die Arbeitsteilung mit dem Folgesatz explizit.
- (b) „…, wie Resteria **die von der Aufgabenstellung genannten Zwecke** mit dem Zero-Waste-Fokus verbindet": lässt die Zahl weg, ein Wort weniger.
- (c) das dritte Glied auf den Kochtipp-Austausch umschreiben: inhaltlich der stärkste Weg, aber der teuerste – er verlangt eine Innovationsaussage über das Bewertungs-/Kommentarsystem, die der Folgesatz derzeit ausdrücklich verneint. **Nicht ohne Änderung des Folgesatzes.**

### Befund 3 – Artikelnummer als Seitenzahl (Literaturverzeichnis, −5)

Zwei `@article`-Einträge tragen ihre Artikelnummer im Feld `pages` statt in `eid`:

| Eintrag | ist | soll | rendert derzeit |
|---|---|---|---|
| `somaFoodWasteReduction2020` | `pages = {907}` | `eid = {907}`, `pages` leer | „Sustainability, 12(3), 907." |
| `nivedhithaHowGreenSocial2024` | `pages = {e13038}` | `eid = {e13038}`, `pages` leer | „International Journal of Consumer Studies, 48(2), e13038." |

Beide Zahlen sind belegt Artikelnummern, keine Seiten: Der Soma-Volltext trägt die Kopfzeile „Sustainability 2020, 12, 907" bei einer internen Paginierung „1 of 19"; der Nivedhitha-Volltext läuft über „N of 29" bei der DOI `10.1111/ijcs.13038`. Die Inkonsistenz ist im gedruckten Verzeichnis unmittelbar sichtbar: **Barker** steht in derselben Zeitschrift wie Soma und rendert korrekt „Sustainability, 13(19), **Artikel 11099**", **Shen** ebenso „**Artikel 107706**" – Soma und Nivedhitha dagegen ohne den Zusatz, als wären es Seitenzahlen.

Warum kein Skript das gemeldet hat: `check_bib_hygiene.py` erkennt Artikelnummern über `^\d{5,}$`, also erst ab fünf Ziffern. „907" hat drei, „e13038" beginnt mit einem Buchstaben. Beide fallen durch das Raster (als Skript-Punkt in `SKILL-ANPASSUNGEN.md` notiert).

**Fix (Zotero, nicht `references.bib`)**: je Eintrag Extra-Feld `tex.eid: 907` bzw. `tex.eid: e13038` setzen, Seitenfeld leeren, BBT neu exportieren, einmal bauen. Die In-Text-Zitationen (`[S. 9]`, `[S. 14]`) bleiben unberührt – sie zählen die interne Paginierung des Artikels und sind korrekt.

### Befund 4 – Erlhofer-Eintrag weicht vom Volltext ab (Literaturverzeichnis, −5)

`references.bib` → `erlhoferWebsiteKonzeptionUndRelaunch2017`:

```
title = {Website-Konzeption und Relaunch: Das Handbuch für die Praxis},
date  = {2017},
```

Am vorliegenden EPUB geprüft (Titelei, Coverbild und OPF-Metadaten):

- **Untertitel** – der Titel lautet an allen drei Stellen schlicht **„Website-Konzeption und Relaunch"**. Die Titelei (`OEBPS/title.html`) zeigt „Sebastian Erlhofer, Dorothea Brenner · Website-Konzeption und Relaunch", das Cover ebenso, `<dc:title>` im OPF ebenfalls. Der Zusatz „: Das Handbuch für die Praxis" ist im Buch nirgends belegt und steht im gedruckten Literaturverzeichnis dennoch.
- **Jahr** – das Impressum nennt „ISBN 978-3-8362-4559-3, **1. Auflage 2018**, © Rheinwerk Verlag GmbH, Bonn 2018", die OPF-Metadaten dagegen `2017-11-07`. Siehe „Bitte manuell prüfen", Punkt 1.

Der Untertitel allein trägt den Befund, unabhängig davon, wie sich das Jahr auflöst. Ein Verzeichniseintrag mit einem Titelzusatz, den das zitierte Werk nicht führt, ist genau der Fund, den Teil-Check F Punkt 3 sucht – und er stammt vermutlich aus einem Datenbank-Import, nicht aus dem Buch.

**Fix (Zotero)**: Titel auf „Website-Konzeption und Relaunch" kürzen; Jahr erst nach der manuellen Prüfung setzen. **Achtung**: Ändert sich das Jahr auf 2018, ändert sich auch der Kurzbeleg im Text („Erlhofer & Brenner, 2018"). Der Citekey ist gepinnt und bleibt – er trägt dann eine Jahreszahl, die nicht mehr zum Feld passt; das ist kosmetisch und für die Ausgabe folgenlos.

## Kosmetische Hinweise (kein Score-Abzug, keine Regelverletzung)

1. `03_konzept.tex:34` kündigt „für die **drei Bereiche** Mockups" an und zählt dann vier Abbildungen auf – die zweite ist eine Variante der Startseite. `check_formalia.py` meldet dazu passend `DOPPELBELEGUNG` („Startseite" beschriftet zwei Objekte). Glättung, falls gewünscht: „…liegen Mockups in Anhang C vor: die Startseite in \autoref{fig:mockup_start}, dieselbe mit ausgeklappten gespeicherten Rezepten in \autoref{fig:mockup_start_bookmarks}, …".
2. `check_formalia.py` meldet `META-PLATZHALTER` für `\ModuleCode` und `\MatrikelNr`. **Fehlalarm** – beide sind gefüllt (`DLBMIMPFS01-01`, `3210267`); die Heuristik hält reine Großbuchstaben-/Ziffernfolgen für Platzhalter.
3. Satzlängen: 20 Sätze über 30 Wörtern, davon 4 über 40 (`03_konzept.tex` 43 und 58 Wörter, `06_evaluation_reflexion.tex` 50, `01_kernergebnisse_und_ausblick.tex` 53). Drei Dateien liegen im Schnitt über 22 Wörtern. Kein FAIL – es sind Aufzählungssätze mit `\parencite`-Ketten. Der längste Satz der Arbeit steht aber im Fazit und wäre der erste Kandidat, falls beim Durchlesen etwas hakt.
4. `main.tex:342` trägt einen Vorlagenrest `% Appendix % TODO: Add Appendix?` – reiner Kommentar, wird nicht gesetzt. Nicht anfassen (`main.tex` bleibt unangetastet).
5. Der Anhang wird über `\section*{Anhang~A: …}` plus eine handgepflegte Tabelle in `main.tex:336–340` gesetzt statt über das inzwischen vorgesehene `\newappendix{}`/`\listofappendices`. Rendert korrekt, aber jede künftige Änderung an der Anhangsreihenfolge muss weiterhin an zwei Stellen nachgezogen werden.
6. Gendersensible Sprache: Die Arbeit gendert durchgehend mit Doppelpunkt („Hobbyköch:innen", „Nutzer:innen"), was der Rangfolge in `hard-rules-formal.md` (Punkt 3: nicht gendern) widerspricht. **Kein Befund**, aus drei Gründen: Die IU-Richtlinie verbietet Gendern nicht, die Aufgabenstellung selbst schreibt „Hobbyköch:innen", und der Gender-Disclaimer ist konsequenterweise deaktiviert (`main.tex:282`) – er würde „überwiegend das generische Maskulinum" behaupten, was hier falsch wäre. Der Zustand ist in sich stimmig; nur die Projektregel und der Text gehen auseinander.

## Sprachstichprobe (Abgabe-Audit, zwei Absätze je Hauptkapitel)

Gelesen wurden je zwei Absätze aus Einleitung, Durchführung und Fazit ausschließlich auf Rechtschreibung, Grammatik, Kommasetzung, Bezugsfehler und Satzreste nach Umbauten. **Kein Sprachfehler gefunden.** Geprüft und für korrekt befunden wurden insbesondere die Stellen, an denen die Cold-Read-Session zuletzt eingegriffen hat:

- `01_kernergebnisse_und_ausblick.tex:5`, „Nur die Funktionen sind literaturgestützt, die Differenzierung selbst bleibt unbelegte Marktbeobachtung." – Komma zwischen zwei unverbundenen Hauptsätzen ist zulässig (§ 72 amtl. Regelung); ein Semikolon läse sich ruhiger, ist aber keine Korrektur.
- `02_zielsetzung_und_verengung.tex:5`, „…, denen Nachhaltigkeit beim Kochen bereits wichtig ist oder die sich dafür zumindest interessieren." – Kasuswechsel „denen"/„die" ist korrekt, beide Relativsätze verlangen unterschiedliche Fälle.
- `06_evaluation_reflexion.tex:9`, „Aus der zweiten dieser Kursänderungen…" – zeigt korrekt auf die Namenskollision, die als zweite genannt ist.
- `04_community_und_feedback.tex:7`, „Forum und Nutzergruppen erfordern wie diese Präsenzgruppe aktiven Gruppenaustausch." – Bezug eindeutig, seit die Vergleichsgruppe zwei Sätze davor benannt ist.

`check_formalia.py` meldet keinen `DOPPELWORT`- und keinen `ANAPHER`-Treffer. Die flächige Prüfung bleibt der LanguageTool-Durchgang.

## Teil-Check H – Lesefluss (max. −5)

**Keine Befunde, 0 Abzug.** Jede der 12 Subsections einmal am Stück gelesen:

- **Anschlüsse**: Alle satzinternen „es / beide / diese / daraus / dort / letztere" haben ein Bezugswort, und es zeigt auf das Richtige. Die drei am Vormittag reparierten Stellen (`03_vorgehen_und_aufbau.tex:5`, `04_community_und_feedback.tex:7`, `06_evaluation_reflexion.tex:9`) halten.
- **Absatzöffner**: Jeder Absatz öffnet mit einer Aussage, keiner mit einem abgeschnittenen Rest.
- **Absatzlänge**: Keine Zwei-Satz-Kürzungsnarbe. Die Absatzzahl je Subsection liegt bei 3–9; den Richtwert 4–8 überschreitet nur `01_wettbewerbsanalyse.tex` (9 Absätze plus Tabelle) – bei sechs einzeln vorgestellten Plattformen sachlich begründet.

## Bewertungsschwerpunkte (Projektbericht)

- **Qualität (25 %)**: **je Dimension** [ABGEDECKT] – alle drei Teilaufgaben ausgeführt, alle sechs Lieferobjekte vorhanden, Abhakliste vollständig; Zielerreichung explizit in `06_evaluation_reflexion.tex:3`.
- **Prozess (25 %)**: [ABGEDECKT] – Vorgehen dokumentiert (`03_vorgehen_und_aufbau`, `06_evaluation_reflexion`), zwei konkrete Kursänderungen statt Leerformel, Grenzen dreischichtig im Fazit.
- **Transfer (15 %)**: [ABGEDECKT] – gesellschaftliche Bedeutung (SDG 12.3) und wirtschaftliche Bedeutung (Freemium plus Kooperationen) beide benannt; vier Modelle explizit begründet eingesetzt (Drivers/Levers, Nudge, Green Social Network Affordances, Influence by Osmosis).
- **Kreativität (15 %)**: [ABGEDECKT, durch Befund 2 geschwächt] – der Vergleich zu bestehenden Produkten trägt (sechs Plattformen, fünf Kriterien, Abgrenzung gegen leftovercooking als engsten Wettbewerber); die Innovationsaussage steht, nur ihre Ankündigung stimmt nicht. Hier liegt der größte Score-Hebel.
- **Dokumentation (10 %)**: [ABGEDECKT] – Entstehungsgeschichte als Abfolge in `06_evaluation_reflexion.tex:7`, Iterationsrunden in `07_iteratives_design.tex:3`, KI-Nutzung in allen fünf Bild-Quellenzeilen transparent.
- **Ressourcen (10 %)**: [ABGEDECKT] – Ressourcenspalte je Phase inklusive Daten, Zeitpuffer, Budgetgrenze für die MVP-Entwicklung, drei Risiken mit Gegenmaßnahmen.

## Lieferobjekt-Abgleich

- [PASS] Alle sechs Lieferobjekte aus `aufgabe.md:52` liegen vor: Wettbewerbsvergleich (`tab:wettbewerbsvergleich`), Persona (`tab:persona` mit Portraitfoto), UI/UX-Mockups (`fig:mockup_start`, `…_bookmarks`, `…_feed`, `…_profil`), Plattformname (`03_konzept.tex:3`), Funktionsübersicht (`tab:funktionsuebersicht`), Phasenplanung (`tab:phasenplanung`).
- [PASS] **Gestaltete Artefakte am Bild geprüft, nicht an der Existenz.** Alle vier Mockups und der Style Tile wurden geöffnet und gegen die Textaussagen gehalten. Im Bild belegt: Wochenplan-Banner auf beiden Startseiten-Screens · Reste-Eingabe als Chip-Tags · Rezeptkarten mit Zubereitungszeit und fehlenden Zutaten · ausgeklappter Bereich „Gespeicherte Rezepte" · Challenge-Banner „Zero-Waste-Woche · Rangliste · Platz 4" · frei stehender Plus-Button ohne Überlapp · Tag mit geretteter Zutat, Like- und Kommentar-Icon, sichtbarer Nutzername · Level-Badge „Level 4 — Resteheld:in" · Rettungspunkte-Fortschrittsbalken · Kennzahl „12,4 kg Lebensmittel gerettet" · Bereich „Reste-Journal" mit Datum, Punkten und Zutaten-Tags · Style Tile mit Farbwelt, Typografie, Layout-Maßen, Icons und Komponenten. **Keine Text-Bild-Lücke.**
- [PASS] `pages/appendix.tex` enthält Inhalt, alle drei Anhänge sind im Fließtext wörtlich verwiesen.

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)

1. **Befund 2 – `03_konzept.tex:16`** (+10): „die drei von der Aufgabenstellung genannten Zwecke" → „zwei der drei von der Aufgabenstellung genannten Zwecke". Ein Wort. Danach `check_all.py --kapitel chapters/02_durchfuehrung`.
2. **Befund 1 – `pages/meta.tex:7`** (+8): Geviertstrich „—" durch Halbgeviertstrich „–" ersetzen. Ein Zeichen.
3. **Befund 3 – Zotero** (+5): `tex.eid: 907` bei Soma, `tex.eid: e13038` bei Nivedhitha, Seitenfeld jeweils leeren, BBT-Export.
4. **Befund 4 – Zotero** (+5): Erlhofer-Titel auf „Website-Konzeption und Relaunch" kürzen; Jahr erst nach dem manuellen Prüfpunkt 1 setzen.
5. Danach **einmal bauen** und die gedruckte Seitenzahl gegenprüfen. Befund 1 und 2 kosten null bis zwei Wörter, die Zotero-Fixes ändern nur das Literaturverzeichnis – der Textteil sollte bei 10 Seiten bleiben, aber die Reserve auf der letzten Textseite beträgt nur rund zwei Zeilen.
6. Anschließend genügt ein **Delta-Re-Audit**, kein neuer Voll-Audit. Erwarteter Score nach vollständiger Umsetzung: **100/100**.

Nicht in dieser Session weiterarbeiten – neue Session, „Schreib-Modus: Überarbeitung nach Prüfbericht".

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

- [ ] **Eidesstattliche Erklärung** elektronisch über myCampus abgeben – **vorher nimmt Turnitin die Einreichung nicht an**.
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen.
- [ ] **LanguageTool-Durchgang** lokal über den Gesamttext. Die Sprachstichprobe oben hat sechs Absätze abgedeckt, nicht 3.701 Wörter.
- [ ] Arbeit einmal am PDF am Stück durchlesen.
- [ ] **Keine externe Plagiatssoftware vorab** – ein Voraberprüfungs-Upload erzeugt einen Turnitin-Selbsttreffer.
- [x] ~~Manueller Prüfpunkt 1: Erscheinungsjahr Erlhofer & Brenner~~ – am 30.07.2026 über das DNB-Katalogisat geklärt: **2018**.
- [ ] Manueller Prüfpunkt 2: die vier zitierten Claude-Design-Folge-Prompts gegen den tatsächlichen Chatverlauf abgleichen.
- [ ] Namensverfügbarkeit „Resteria" (DPMA, .de-Domain) – nicht abgabekritisch, aber vor einer realen Umsetzung relevant.

## Nachtrag zur Überarbeitung (30.07.2026, eigene Session)

**Befund 1 und 2 umgesetzt, Befund 3 und 4 sachlich vollständig geklärt, Umsetzung bleibt Zotero-Schritt.**

- **Befund 2** – zunächst nach Variante (a) gefixt („zwei der drei … Zwecke"), auf Nutzer-Rückfrage dann **über den Prüfbericht hinaus** gelöst. Variante (a) hatte den Widerspruch zum Folgesatz behoben, aber zwei Mängel hinterlassen: Nach dem Doppelpunkt standen weiterhin **drei** Glieder, die Ankündigung nannte zwei — die Zähl-Differenz war nur umgedreht, nicht weg; und „zwei der drei" ist eine Defizitansage an der einzigen Stelle, die das Kriterium **Kreativität (15 %)** trägt. Nach `AskUserQuestion` auf eine Fassung ohne Zahl umgestellt: „…, wie Resteria den Zero-Waste-Fokus in die von der Aufgabenstellung genannten Zwecke **Rezept-Teilen und gegenseitige Inspiration** hineinträgt **und ihn zugleich in der täglichen Nutzung verankert**: …". Die zwei eingelösten Zwecke sind damit benannt statt gezählt, und das dritte Glied steht unter einer eigenen Ankündigung, statt fälschlich als Zweck zu gelten. Das Schlussglied endete in der beschlossenen Fassung wortgleich wie die neue Rahmung — umformuliert, um die Dopplung innerhalb eines Satzes zu vermeiden.

  **Faktenprüfung desselben Absatzes auf Nutzerwunsch, ein Overclaim behoben (Frequenzanspruch „täglich").** Drei der vier Aussagen sind am eigenen Text belegt: die verpflichtende Zutaten-Kennzeichnung (`03_konzept.tex:13`, „Pflichtangabe der verwendeten Reste-Zutat"), die monatliche Zero-Waste-Woche als Ersatz für Forum und Gruppen (`04_community_und_feedback.tex:7` wörtlich) und die Kopplung an die Rettungspunkte (`:13`). **Nicht belegt war „tägliche Nutzung"/„tägliche Routine":** Der beschriebene Mechanismus ist ein **Wochen**plan (`:13` „verteilt die Rezepte über die Woche"; `tab:funktionsuebersicht` „Wochenplan"), die Challenges sind monatlich, und die Erinnerungsbenachrichtigung feuert ausdrücklich erst, „wenn längere Zeit keine Zutat eingetragen wurde" — also gerade nicht täglich. Die Arbeit formuliert ihr eigenes Ziel in `:9` als „aus einmaliger Nutzung **wiederkehrendes** Verhalten zu machen". „Täglich" kam im gesamten `chapters/` nur an dieser einen Stelle vor. **Herkunft:** Der Anspruch stand bereits vor der Neufassung im Text („verankert den Zero-Waste-Kern in der täglichen Nutzung") — die Neufassung hatte ihn verdoppelt, nicht eingeführt. Jetzt „in der **wiederkehrenden** Nutzung verankert" (Vokabel aus `:9`) und „**bindet die Reste-Verwertung in die Wochenplanung ein**" (Mechanismus aus `:13`/`tab:funktionsuebersicht`).

  Netto +10 Wörter gegenüber dem Audit-Stand (3.712).

  **Nebenbefund ohne Handlungsbedarf, der Variante (c) des Berichts erledigt:** Der dritte Zweck der Aufgabenstellung — Kochtipp-Austausch — **ist** eingelöst. `03_konzept.tex:13` nennt beim Bewertungs- und Kommentarsystem ausdrücklich das Austauschen von „Zubereitungstipps". Er steht nur bewusst in der Kategorie „übernommenes Format" statt „Innovation", und genau diese Arbeitsteilung bildet der Satz jetzt ab. Die im Bericht als „inhaltlich stärkster, aber teuerster Weg" bezeichnete Variante (c) hätte also eine Innovationsaussage für etwas verlangt, das der Text schon korrekt als nicht-innovativ einordnet.
- **Befund 1** – `pages/meta.tex:7`: U+2014 → U+2013. Am gebauten PDF verifiziert, Titelblatt zeigt „Resteria – Konzeption einer …". Nebenbefund ohne Handlungsbedarf: `meta.tex` enthält zwei weitere Geviertstriche, beide in `%`-Kommentarzeilen (Z. 2, Z. 15) – sie werden nicht gesetzt.
- **Build nachgezogen** (Handlungsempfehlung 5, auf ausdrückliche Nutzeranweisung selbst gefahren): `latexmk -g -lualatex main.tex`, Exit 0, 23 PDF-Seiten, **0 Overfull \hbox, 0 Missing character, 0 `!`-Fehler**. **Textteil unverändert 10 Seiten** von 7–10 (gedruckt 1–10 = PDF-Seite 6–15, Literaturverzeichnis ab PDF-Seite 16). Die +2 Wörter haben die letzte Seite nicht gekippt.
- `check_all.py --kapitel chapters/02_durchfuehrung`: 0 FEHLER · `check_quellentreue.py --datei chapters/`: **20/20 FUNDSTELLE OK**, keine Zitation invalidiert · `check_umfang.py`: **3.711 Wörter** im Korridor 2.625–3.750.
- **Zweiter Build nach der Neufassung des Innovationssatzes**: Exit 0, 0 Overfull, 0 Missing character, 0 `!`-Fehler, **Textteil weiterhin 10 Seiten** (gedruckt 1–10 = PDF-Seite 6–15). Die +9 Wörter haben die Reserve auf der letzten Textseite nicht gesprengt.

**Befund 4 am DNB-Katalogisat entschieden.** Über die SRU-Schnittstelle der Deutschen Nationalbibliothek (`services.dnb.de/sru/dnb`, Suche `num=9783836245579`, Schema MARC21-xml):

| MARC-Feld | Inhalt |
|---|---|
| 020 | 9783836245579 / 3836245574 |
| 245 | „Website-Konzeption und Relaunch / Sebastian Erlhofer, Dorothea Brenner" – **kein Untertitelfeld** |
| 250 | „1. Auflage" |
| 264 | „Bonn : Rheinwerk Verlag : 2018" |

Damit sind **beide Hälften des Befunds bestätigt**: Der Untertitel „: Das Handbuch für die Praxis" gehört nicht zum katalogisierten Titel (er stammt aus der Buchhandels-Marketingzeile – AbeBooks führt ihn als „Das Handbuch für die Praxis. Website-Konzepte entwickeln, Webseiten optimieren, Besucher begeistern", der Verlag selbst nennt für die 2. Auflage wiederum „Planung, Optimierung, Usability"; drei verschiedene Zusätze, keiner davon im Buch). Und das **Erscheinungsjahr ist 2018**, nicht 2017 – die OPF-Metadaten des EPUBs (`2017-11-07`) geben ein Produktions-, kein Erscheinungsdatum wieder; das Impressum („1. Auflage 2018") und das DNB-Katalogisat stimmen überein.

**Folge für den Text**: Der Kurzbeleg an den beiden Fundstellen in `07_iteratives_design.tex` rendert nach dem Zotero-Fix als „Erlhofer & Brenner, 2018". Der gepinnte Citekey behält die 2017 im Namen – kosmetisch, für die Ausgabe folgenlos (so schon in Befund 4 vermerkt).
