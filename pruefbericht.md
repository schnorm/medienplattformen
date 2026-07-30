# Prüfbericht – Projektbericht

**Datum**: 30.07.2026 · **Geprüfter Stand**: Delta `cf9a579..f5fa3a4` (2 Kapiteldateien, `pages/meta.tex`, `references.bib`) plus Neubau des PDF · **Audit-Typ**: Delta-Re-Audit
**Score: 100/100 – abgabereif**

> Einordnung vorab: Geprüft wurden die vier Befunde des Abgabe-Audits vom selben Tag (72/100), der vollständige Textdiff seit dem damals geprüften Stand, alle sechs Skripte, ein Neubau und das gebaute PDF. **Alle vier Befunde sind verifiziert behoben, keine Regression, kein neuer Befund.** Der Delta ist klein: zwei Absätze in `03_konzept.tex`, ein Satz in `06_evaluation_reflexion.tex`, ein Zeichen in `pages/meta.tex`, vier Felder in `references.bib`.

## Verifikation der vier Vorbefunde

| Vorbefund | Stand | Belegt am |
|---|---|---|
| **1 – Geviertstrich im `\PaperTitle`** (Formalia, −8) | **behoben** | Titelblatt (PDF-S. 1) und PDF-Metadaten `/Title` zeigen U+2013: „Resteria – Konzeption einer …". Zeichencode am extrahierten Text geprüft (`0x2013`), nicht am Augenschein. |
| **2 – „drei Zwecke" angekündigt, zwei eingelöst** (Struktur, −10) | **behoben, über die Empfehlung hinaus** | `03_konzept.tex:15` trägt keine Zählangabe mehr. Die zwei eingelösten Zwecke sind **benannt** („Rezept-Teilen und gegenseitige Inspiration"), das dritte Glied steht unter eigener Ankündigung („zugleich über die einmalige Nutzung hinaus verankert") statt fälschlich als Zweck. Der Widerspruch zum Folgesatz ist damit weg, und die Zähl-Differenz ist nicht umgedreht, sondern aufgelöst. |
| **3 – Artikelnummer als Seitenzahl** (Literaturverzeichnis, −5) | **behoben** | `references.bib`: `pages` bei Soma und Nivedhitha entfernt, `eid` gesetzt. Gerendertes Verzeichnis (PDF-S. 16): „Sustainability, 12(3), **Artikel 907**." und „48(2), **Artikel e13038**." – je einmal, formgleich mit Barker („Artikel 11099") und Shen („Artikel 107706"). Kein Doppeldruck. |
| **4 – Erlhofer weicht vom Volltext ab** (Literaturverzeichnis, −5) | **behoben** | `title = {Website-Konzeption und Relaunch}`, `date = {2018}`. Verzeichnis: „Erlhofer, S. & Brenner, D. (2018). Website-Konzeption und Relaunch. Rheinwerk Computing." In-Text auf PDF-S. 12: „laut Erlhofer und Brenner (**2018**, Kap. 17.2.2)" – die Jahresänderung ist im Kurzbeleg angekommen. |

## Teil-Check A – Formalia

- [PASS] Zitationen – `check_bib_keys.py`: alle genutzten Keys existieren, 0 FEHLER.
- [PASS] LaTeX-Format – Befund 1 behoben. Kein Geviertstrich mehr in gesetztem Text; die zwei verbliebenen in `meta.tex` stehen in `%`-Kommentarzeilen (Z. 2, Z. 15) und werden nicht gesetzt.
- [PASS] Cross-References & Labels – 0 undefinierte Referenzen/Zitationen im Build. Die vier `\autoref`-Ziele im geänderten Mockup-Satz (`03_konzept.tex:36`) lösen in aufsteigender Reihenfolge auf: Startseite = Abb. 2, Bookmarks = Abb. 3, Rettungs-Feed = Abb. 4, Profil = Abb. 5 (am PDF gegengezählt, PDF-S. 20–23).
- [PASS] Eigene Werke · Pronomen · Akronyme · Anti-KI-Stil · Verständlichkeit – `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**. Die Hinweise sind der bekannte Bestand (Satzlängen, TRIAS, ABKUERZUNG für UI/UX/KI, TITEL-DOPPLUNG) – unverändert gegenüber dem Vorbericht, keine neuen Klassen.
- [PASS] Offene Arbeitsmarker – kein `% TODO-QUELLE:`, kein `% UNVERIFIED:`.
- [PASS] `DOPPELBELEGUNG`-Hinweis des Vorberichts ist **weg**: „Startseite" beschriftet nicht länger zwei Objekte, seit der zweite Screen als „dieselbe mit ausgeklappten gespeicherten Rezepten" benannt ist.

## Teil-Check B – Argumentationsqualität

Im Delta unberührt – der Diff enthält keine These-, Argument- oder Belegänderung. Zwei Punkte wurden trotzdem gegengeprüft, weil der Diff sie streift:

- [PASS] Reichweiten-Konsistenz Einleitung ↔ Reflexion – die am 30.07. abgeschwächte Aussage in `02_zielsetzung_und_verengung.tex:5` („dürften vor allem für Menschen … oder die sich dafür zumindest interessieren") ist in `06_evaluation_reflexion.tex:3` jetzt deckungsgleich nachgezogen („vor allem bereits motivierte **oder zumindest interessierte** Personen ansprechen **dürfte**"). Die Propagationslücke aus dem Einzel-Stresstest ist geschlossen; beide Stellen stehen im selben Modus.
- [PASS] Abhakliste – der dritte Aufgaben-Zweck **Kochtipp-Austausch** ist weiterhin eingelöst und ausgewiesen: `03_konzept.tex:13` („Zubereitungstipps austauschen") und `tab:funktionsuebersicht`, Zeile „Bewertungs-/Kommentarsystem → Aufgabenstellung: Kochtipp-Austausch". Der Fix von Befund 2 hat ihn nicht mit entfernt.

## Teil-Check C – Struktur

- [PASS] Zählangaben in den geänderten Absätzen nachgezählt: `03_konzept.tex:15` macht keine Zählaussage mehr (drei Glieder nach dem Doppelpunkt, zwei benannte Zwecke plus eine eigene Ankündigung – kein Zählversprechen). `03_konzept.tex:36`: „für die drei Bereiche vier Mockups" – drei Bereiche im Vorsatz benannt (Startseite, Rettungs-Feed, Profil), vier Abbildungen aufgezählt. Stimmt.
- [PASS] Roter Faden – der Widerspruch Ankündigung ↔ Folgesatz, der Befund 2 trug, existiert nicht mehr. Der Folgesatz („übernimmt Resteria dagegen bewusst als Formate aus etablierten Rezept-Communitys") steht jetzt in sauberer Arbeitsteilung zur Innovationsaussage statt im Gegensatz zu ihr.
- [PASS] ½-Seiten-Regel – keine Datei ist durch den Delta geschrumpft; `check_umfang.py` weist 3.721 Wörter aus (Vorbericht 3.701), also netto +20.
- [PASS] Front-/Backmatter, Kapitelstufen, Outline – im Delta unberührt, am gebauten PDF gegengeprüft (Verzeichnisse auf PDF-S. 2–5, Literaturverzeichnis S. 16, Anhangsverzeichnis S. 17, Anhänge A–C S. 18–23).

## Teil-Check D – Build

- [PASS] Kompiliert fehlerfrei – `latexmk -g -lualatex main.tex`, **Exit 0**, 23 PDF-Seiten. **0 Zeilen `^!`, 0 `Overfull \hbox`, 0 `Missing character`, 0 undefinierte Referenzen/Zitationen.**
- [PASS] Seitenumfang Textteil – **10 Seiten von 7–10.** Am gebauten PDF gemessen: „1 Einleitung" auf PDF-S. 6 (gedruckt 1), letzte Textseite PDF-S. 15 (gedruckt 10), Literaturverzeichnis ab PDF-S. 16 (gedruckt 11). Die +20 Wörter des Delta haben die letzte Seite nicht gekippt.
- Weißraum-Diagnose (3a): nicht ausgelöst – der Umfang liegt innerhalb der Vorgabe.
- [PASS] Projekt-Root nach dem Lauf frei von Build-Artefakten (kein `main.aux`/`.bcf`/`.log`/`.toc`).

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [PASS] Umfang im Soll (Spiegel aus Teil-Check D): 10 von 7–10 Seiten
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen – Turnitin würde den eigenen Upload als Treffer werten
- [OFFEN] LanguageTool-Durchgang lokal über den Gesamttext

## Teil-Check F – Literaturverzeichnis

- [PASS] `check_bib_hygiene.py`: 10 Einträge, **0 Hinweise**.
- [PASS] Gerendertes Verzeichnis erneut gelesen (PDF-S. 16) – Alphabetik korrekt (Erlhofer nach Barker, Hasanbekava vor Nielsen), Sentence Case bei allen englischen Titeln, deutscher Titel korrekt großgeschrieben, keine kaputten Sonderzeichen, keine Verlagsorte, kein Abrufdatum, DOI statt URL wo vorhanden, Autorennamen als „Nachname, Initiale.". Beide Befund-3-Einträge tragen jetzt „Artikel N" wie ihre Vergleichseinträge.
- Geprüft und **kein** Befund: Im extrahierten Verzeichnistext stehen Leerzeichen vor Satzzeichen („Relaunch .", „Consumer Studies ,"). Das sind Artefakte der PDF-Textextraktion an Kursiv-/Aufrecht-Übergängen, keine Setzung – sie treten ausschließlich am Ende kursivierter Titel und Journalnamen auf.
- Beobachtung ohne Handlungsbedarf: Das Erlhofer-Autorenfeld trägt seit dem Zotero-Fix Initialen (`{Erlhofer, S and Brenner, D}`) statt ausgeschriebener Vornamen. Die APA-Ausgabe ist identisch, weil der Stil ohnehin abkürzt.

## Teil-Check G – Quellentreue (Volltextabgleich)

- [PASS] **20 Zitationen geprüft · FUNDSTELLE OK 20 · offen 0** (Details: `quellencheck.md`).
- Befunde je Klasse: **keine.** Kein WORTLAUT, kein ZITAT WEICHT AB, kein SEITE VERDÄCHTIG, kein SEITE AUSSERHALB, kein CLAIM SCHÄRFER, kein NICHT PRÜFBAR, kein RENTIERT NICHT.
- **Keine Invalidierung durch den Delta.** Der geänderte Absatz `03_konzept.tex:15` trägt selbst keine Zitation; die drei Zitationen in `:9`, die eine in `:11` und die drei in der Tabellenzelle `:25` blieben unberührt. Auch die Erlhofer-Jahresänderung hat keinen Trägersatz-Hash bewegt (der Hash hängt am Text, nicht am Bib-Feld).
- Notiz-Wächter: kein `[NOTIZ-DUBLETTE]`, kein `[NOTIZ-FREMDER-AUTOR]`. Stichprobe: Die Notiz zu `acb47aface` (`01_ausgangslage_und_problem.tex:5`) beschreibt die Zuschreibungsform „wird … zugerechnet" – der Satz im Text lautet genau so. Keine verrutschte Notiz.
- Volltexte ohne Bib-Verweis (3): Krug- und Norman-EPUBs aus der Vorarbeit sowie die Vittuari-Preprint-Fassung neben der zitierten Verlagsfassung. Alle drei unschädlich, wie im Vorbericht.

## Teil-Check H – Lesefluss

Nur der Delta gelesen, nicht alle 12 Subsections erneut (der Vorbericht desselben Tages hat sie vollständig abgedeckt und fand 0 Befunde):

- [PASS] `03_konzept.tex:15` – der neue Öffner ist eine Aussage, der Satz trägt drei parallel gebaute Glieder, keine Wortdopplung mehr („über die einmalige Nutzung hinaus" statt des zuvor mit „monatlich wiederkehrende" kollidierenden „wiederkehrenden").
- [PASS] `03_konzept.tex:36` – die Aufzählung ist nach dem Umbau eindeutig („die Startseite … dieselbe mit ausgeklappten … der Rettungs-Feed … das Profil"); jedes Glied trägt einen Artikel, kein Bezug hängt.
- [PASS] `06_evaluation_reflexion.tex:3` – Modalwechsel („dürfte") stört den Satzbau nicht, der Anschluss an den Folgesatz („Beide Aussagen passen zusammen, wenn …") hält.

## Claims

- Ungesicherte FACTUAL CLAIMS: **keine.**
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: `pexelsHasanbekavaBasket` – **kein echter Fund**, wird über `\citeauthor`/`\citeyear` in der Quellenzeile von `tab:persona` genutzt; `check_bib_keys.py` erkennt nur `\parencite`/`\textcite`/`\cite`. **Nicht entfernen.**

## Punkteabzug im Detail

- **Keiner.** Alle vier Vorbefunde behoben, keine neue Fundklasse. **100/100.**

## Kosmetische Hinweise (kein Score-Abzug, keine Regelverletzung)

1. `03_konzept.tex:15` – „die von der Aufgabenstellung genannten Zwecke Rezept-Teilen und gegenseitige Inspiration" lässt sich streng gelesen als Aufzählung **aller** genannten Zwecke verstehen, während es drei sind. Kein Befund: Der unmittelbar folgende Satz ordnet das Bewertungs- und Kommentarsystem der Gegenkategorie zu, und `tab:funktionsuebersicht` weist es ausdrücklich dem dritten Zweck (Kochtipp-Austausch) zu – die Arbeitsteilung ist im Absatz auflösbar. Eine Zahlangabe wieder einzuführen wäre der Rückschritt, den die Überarbeitung bewusst vermieden hat. **Empfehlung: nicht anfassen.**
2. Satzlängen unverändert im bekannten Rahmen: 20 Sätze über 30 Wörtern, der längste (53 W.) weiterhin in `01_kernergebnisse_und_ausblick.tex`. Kein FAIL – Aufzählungssätze mit `\parencite`-Ketten. Erster Kandidat, falls beim finalen Durchlesen etwas hakt.
3. `check_formalia.py` meldet weiterhin `META-PLATZHALTER` für `\ModuleCode` und `\MatrikelNr` – **Fehlalarm**, beide sind gefüllt (`DLBMIMPFS01-01`, `3210267`); die Heuristik hält reine Großbuchstaben-/Ziffernfolgen für Platzhalter.
4. `check_status.py`: 0 FEHLER, 15 `DATEI-OHNE-ZEILE`-Hinweise – projekttypische Konvention (die Statustabelle führt Kapitel, nicht Subsections).

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

1. **Wortlaut der zitierten Claude-Design-Folge-Prompts** | `pages/appendix.tex`, die vier `\quelle{}`-Zeilen zu `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_feed`, `fig:mockup_profil` | Stimmt, wenn der zitierte Text wortgleich dem entspricht, was im Claude-Design-Chat eingegeben wurde | Der Chatverlauf liegt außerhalb des Repositorys. Zur Einordnung: Der Zitierleitfaden verlangt nur **den** Ursprungsprompt (Singular); die Folge-Prompts sind Projektkonvention, ihr Fehlen wäre kein Regelverstoß – eine **falsch wiedergegebene** Formulierung dagegen schon.

## Bewertungsschwerpunkte (Projektbericht)

Unverändert gegenüber dem Abgabe-Audit, mit einer Aufwertung:

- **Qualität (25 %)**: [ABGEDECKT]
- **Prozess (25 %)**: [ABGEDECKT]
- **Transfer (15 %)**: [ABGEDECKT]
- **Kreativität (15 %)**: [ABGEDECKT] – **nicht mehr durch Befund 2 geschwächt.** Die Innovationsaussage benennt jetzt, welche Aufgaben-Zwecke sie einlöst, und grenzt sich sauber gegen die bewusst übernommenen Formate ab. Das war der größte Score-Hebel des Vorberichts.
- **Dokumentation (10 %)**: [ABGEDECKT]
- **Ressourcen (10 %)**: [ABGEDECKT]

## Lieferobjekt-Abgleich

Im Delta unberührt – alle sechs Lieferobjekte liegen unverändert vor, die vier Mockups und der Style Tile wurden im Abgabe-Audit desselben Tages am **Bild** geprüft (keine Text-Bild-Lücke). Der einzige Delta-Berührungspunkt ist die Aufzählung in `03_konzept.tex:36`; ihre vier `\autoref`-Ziele lösen korrekt und in aufsteigender Abbildungsnummer auf (am PDF gegengezählt).

## Handlungsempfehlungen

**Keine.** Es steht kein Arbeitsschritt am Text, an `references.bib` oder am Build aus. Die Arbeit ist textseitig abgabereif.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

- [ ] **Eidesstattliche Erklärung** elektronisch über myCampus abgeben – **vorher nimmt Turnitin die Einreichung nicht an**.
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen.
- [ ] **LanguageTool-Durchgang** lokal über den Gesamttext (3.721 Wörter). Die Sprachstichprobe des Abgabe-Audits deckte sechs Absätze ab.
- [ ] Arbeit einmal am PDF am Stück durchlesen.
- [ ] **Keine externe Plagiatssoftware vorab** – ein Voraberprüfungs-Upload erzeugt einen Turnitin-Selbsttreffer.
- [ ] Manueller Prüfpunkt: die vier zitierten Claude-Design-Folge-Prompts gegen den tatsächlichen Chatverlauf abgleichen.
- [ ] `main.pdf` in der abgegebenen Fassung ist der Build dieser Session (23 Seiten, Textteil 10) – falls vor der Abgabe noch etwas geändert wird, neu bauen und die Seitenzahl gegenprüfen. Die Reserve auf der letzten Textseite liegt bei rund zwei Zeilen.
- [ ] Namensverfügbarkeit „Resteria" (DPMA, .de-Domain) – nicht abgabekritisch, aber vor einer realen Umsetzung relevant.
