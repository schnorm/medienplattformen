# Prüfbericht – Projektbericht

**Datum**: 30.07.2026 · **Geprüfter Stand**: Delta `85c0b53..d36412e` (3 Kapiteldateien, `pages/appendix.tex`) · **Audit-Typ**: Delta-Re-Audit
**Score: 89/100 (vorläufig – Teil-Check D nicht lauffähig, Seitenumfang für den aktuellen Textstand ungeprüft)**

> **Nachtrag 30.07.2026 (nach dem Audit, auf Nutzerentscheidung):** Befund 2 und 3 sind umgesetzt, dazu eine vom Nutzer angestoßene Streichung im selben Absatz. Details am Ende des Berichts unter „Nachtrag". Offen bleibt allein Handlungsempfehlung 1 (Build).

> Einordnung vorab: Geprüft wurde der vollständige Textdiff seit dem letzten Delta-Re-Audit (100/100), alle sechs Skripte und das im Repository liegende PDF. **Inhaltlich ist der Delta ein Gewinn und trägt keinen score-relevanten Befund.** Der Punktabzug hat eine einzige Ursache: In dieser Session-Umgebung sind `lualatex`/`latexmk`/`biber` nicht installiert, und das eingecheckte `main.pdf` ist **veralteter Stand** — der Seitenumfang, ein Pflichtkriterium, ist damit für den aktuellen Text nicht gemessen. Das ist kein Textmangel, sondern ein ausstehender Build.

## Der Delta in einem Satz

Die Begründung des Verzichts auf Gruppen und Foren in `04_community_und_feedback.tex` wurde von einer Studien-Ableitung (Soma) auf drei arbeitseigene Gründe umgestellt und der Absatz dabei geteilt; `03_konzept.tex:15` und `06_evaluation_reflexion.tex:5` zogen die Vokabel nach; die vier Prompt-Zitate in `pages/appendix.tex` wurden an den tatsächlichen Wortlaut angeglichen und eine dabei zerbrochene Klammer repariert.

## Befunde

### 1 — `main.pdf` im Repository ist nicht der Build des aktuellen Textes (kein Score-Abzug, aber abgabeblockierend)

Das eingecheckte PDF stammt aus Commit `7d5bf56` und trägt den Textstand **vor** `78d0587`. Maschinell am extrahierten PDF-Text verifiziert:

| Probe | im PDF |
|---|---|
| „Die Aufgabenstellung nennt Gruppen und Foren …" (neu) | **fehlt** |
| „Chefkoch.de hat dafür einen gewachsenen …" (neu) | **fehlt** |
| „… ersetzt **Forum und Gruppen** als Anlass" (alt) | **vorhanden** |
| „Community-Zuschnitt mit **Forum und Nutzergruppen**" (alt) | **vorhanden** |
| „Den Anstoß dazu gab ein Befund von …" (alte Soma-Begründung) | **vorhanden** |

Wer dieses PDF einreicht, reicht die alte, inzwischen bewusst verworfene Begründung ein. **Vor der Abgabe zwingend neu bauen.**

### 2 — `pages/appendix.tex:53`: Anschlussformel weicht von den drei Schwesterzeilen ab (Formalia-Hinweis, kein Abzug)

Die vier `\quelle{}`-Zeilen enden nach dem Prompt-Zitat einheitlich auf `}, in weiteren Iterationsschritten verfeinert, durch Anthropic, 2026 …` — **außer** der Zeile zu `fig:mockup_feed`, die seit dem Delta `}, sowie in weiteren Iterationsschritten verfeinert …` trägt. Zwei Punkte:

- Das `sowie` steht **außerhalb** des `\enquote{}`, ist also eigener Text der Arbeit und nicht durch die Wortlauttreue des Zitats gedeckt.
- Vor `sowie` steht in einer einfachen Aufzählung kein Komma.

**Fix (ein Wort):** `}, sowie in weiteren` → `}, in weiteren`. Damit sind alle vier Zeilen wieder formgleich.

### 3 — `04_community_und_feedback.tex:9`: „vor allem" schreibt dem Verweisziel eine Rangfolge zu, die dort nicht steht (Präzisionshinweis, kein Abzug)

Der Satz lautet „Laut~\autoref{sec:zielgruppe} sucht die Zielgruppe **vor allem** einen Ort, an dem der eigene Erfolg von anderen gesehen wird." — `02_zielgruppe.tex:7` leitet aber **zwei gleichrangige** Anforderungen ab: sichtbar machen, wie viel eine Person einspart, **und** einen Ort, an dem dieser Erfolg wahrgenommen wird. Eine Rangfolge nennt die Stelle nicht.

Der Verweis ist inhaltlich korrekt (die zweite Anforderung steht dort wörtlich), und das Argument trägt auch ohne die Rangfolge — die erste Anforderung erfüllt Resteria über Reste-Journal und Rettungspunkte, sie spricht also nicht dagegen. **Fix: „vor allem" streichen.**

### 4 — Ein neuer Skript-Hinweis durch den Delta (kein Abzug)

`check_formalia.py` meldet 47 Hinweise gegen 46 im Vor-Delta-Stand (durch Auschecken von `85c0b53` gegengemessen). Der eine neue: `[HINWEIS:META-VERB]` in `04_community_und_feedback.tex:9` — „Die Challenges **bündeln** die Beteiligung …". Einzelvorkommen; der Abzug greift laut Score-Regel erst ab mehr als drei je Kapitel. Optional: „bündeln" → „halten … zusammen".

## Zwei Korrekturen am Vorbericht (Aktenlage, keine neuen Mängel)

1. **`DOPPELBELEGUNG` ist nicht behoben.** Der Vorbericht führte den Hinweis („Startseite" beschriftet `fig:mockup_start` und `fig:mockup_start_bookmarks`) als erledigt. Durch Auschecken von `85c0b53` und erneuten Skriptlauf verifiziert: Der Hinweis stand dort bereits und steht unverändert. **Kein Handlungsbedarf** — es ist ein Heuristik-Fehlalarm: Die Textstelle `03_konzept.tex:13` („über die Startseite erreichbar") ist ein Verweis auf den App-Screen, kein Abbildungs-Rückverweis, und die Aufzählung in `:34` unterscheidet beide Abbildungen ausdrücklich („die Startseite … dieselbe mit ausgeklappten gespeicherten Rezepten").
2. **Die Reserve auf der letzten Textseite beträgt nicht zwei Zeilen, sondern rund acht.** Vorbericht und `CLAUDE.md` nennen „37 pt ≈ 2 Zeilen". Am PDF gemessen: Die unterste Textzeile der gedruckten Seite 10 sitzt bei y = 190,6 pt, die Satzspiegel-Unterkante der dichten Seiten bei y ≈ 56,7 pt, der Zeilenabstand beträgt 16,4 pt. Freier Raum also **≈ 134 pt ≈ 8 Zeilen**. Diese Korrektur ist nicht kosmetisch: Der zu niedrige Wert lässt jede künftige Ergänzung als kürzungspflichtig erscheinen, und Kürzungsrunden sind in diesem Projekt der Arbeitsschritt mit der höchsten dokumentierten Fehlerquote (`SKILL-ANPASSUNGEN.md` → P17).

## Teil-Check A – Formalia

- [PASS] Zitationen – `check_bib_keys.py`: alle 9 genutzten Keys existieren, 0 FEHLER.
- [PASS] LaTeX-Format – **Klammerbilanz aller sechs `\quelle{}`-Zeilen in `pages/appendix.tex` maschinell geprüft: je ±0, Datei gesamt ±0.** Der Build-Bruch aus `dbfe4f7` (verschluckte schließende Klammer des inneren `\enquote{}` bei `fig:mockup_profil`) ist mit `7d5bf56` sauber repariert; die Zeile steht strukturgleich zu ihren Schwesterzeilen.
- [PASS] Eigene Werke – alle vier Mockup-Quellenzeilen tragen weiterhin Prompt, Unternehmen, Jahr, Modell und den Bearbeitungshinweis nach dem Muster des Zitierleitfadens (Kap. 2.2.5).
- [PASS] Gendersensible Sprache – die im Delta neu erscheinenden Formen „Hobbyköche" und „Resteheld" stehen **innerhalb** von `\enquote{}` und geben die tatsächliche Prompt-Eingabe wieder. Wortlauttreue geht hier vor; die Richtlinien (10/2025, S. 1) kennen ohnehin keine Genderpflicht, und der Gender-Disclaimer bleibt eingebunden. Kein Befund.
- [PASS] Cross-References & Labels – die beiden neuen `\autoref`-Ziele (`sec:zielgruppe`, `sec:wettbewerbsanalyse`) existieren und sind semantisch korrekt (siehe Teil-Check C).
- [PASS] Pronomen · Akronyme · Anti-KI-Stil · Verständlichkeit – `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**. 47 Hinweise, davon genau einer neu (Befund 4).
- [PASS] Offene Arbeitsmarker – kein `% TODO-QUELLE:`, kein `% UNVERIFIED:`.

## Teil-Check B – Argumentationsqualität

- [PASS] These und Kernargumente im Delta unberührt.
- [PASS] **Abhakliste, Eintrag „Gruppen/Foren" – durch den Delta von „adressiert" auf „ausdrücklich beantwortet" gehoben.** Am Original verifiziert (`sources/Aufgabenstellung.pdf`, PDF-S. 4): „Dazu könnten gehören: … **Gruppen und Foren für spezifische Kochinteressen oder -stile** …". Der neue Absatz gibt das als „Gruppen und Foren für bestimmte Kochinteressen als **mögliche** Funktion" wieder — Modalität („könnten gehören") korrekt mitgeführt, Paraphrase enger als das Original. Die Auslassung ist damit begründet wie schon die des Event-Kalenders.
- [PASS] **Die Umstellung beseitigt eine Überdehnung, statt eine zu schaffen.** Die alte Begründung übertrug einen Soma-Befund über *Präsenz*-Workshops auf ein *asynchrones Online*-Forum; die dokumentierten Absagegründe (Terminkonflikt, Kinderbetreuung) tragen genau diese Übertragung nicht. Die neue Begründung stützt sich auf drei Punkte, die alle im Dokument selbst belegt sind: die Anforderung aus `02_zielgruppe.tex:7`, die Wettbewerbsanalyse (`01_wettbewerbsanalyse.tex:3`, Chefkoch „stark" bei Kommunikation & Community) und das Kaltstart-Risiko (`05_phasenplanung.tex:25`, Risiko 3: „zu wenige Community-Beiträge, um den Feed zu tragen").
- [PASS] **Keine verwaiste Attribution.** Nach dem Entfernen der Soma-Zitation aus `04` steht Soma nur noch an drei Stellen (`03_konzept.tex:11`, `:25`, `01_kernergebnisse_und_ausblick.tex:5`), alle zum Gamification-Effekt, keine zur Forumsentscheidung. Grep über `chapters/` bestätigt.
- [PASS] Limitationen weiterhin dreischichtig (im Delta unberührt, am PDF-Text der gedruckten Seite 10 gegengelesen: alle drei tragen warum · Mitigation · Folgeschritt).

## Teil-Check C – Struktur

- [PASS] **Querverweise semantisch korrekt.**
  - `\autoref{sec:zielgruppe}` → `02_zielgruppe.tex:7` trägt wörtlich „einen Ort bieten, an dem dieser Erfolg von anderen wahrgenommen wird". Deckt den Verweis; zur Rangfolge siehe Befund 3.
  - `\autoref{sec:wettbewerbsanalyse}` → `01_wettbewerbsanalyse.tex:3` trägt „Nutzer:innen laden dort eigene Rezepte hoch, bewerten fremde Beiträge und kommentieren sie; dieser tatsächliche Austausch begründet die Einstufung \enquote{stark}". Deckt „der Austausch über Rezepte ist die Stärke der etablierten Communitys"; „gewachsener Bestand an Beiträgen" ist durch „etablierte … Rezept-Communities" plus „Rezeptsammlungen zu einzelnen Zutaten" getragen.
- [PASS] **Terminologie jetzt einheitlich.** „Gruppen und Foren" — die Vokabel der Aufgabenstellung — steht nach dem Delta in allen drei Kapiteln (`03_konzept.tex:15`, `04:9`, `06_evaluation_reflexion.tex:5`); die früheren Varianten „Forum und Gruppen" und „Forum und Nutzergruppen" kommen in `chapters/` nicht mehr vor (Grep). `tab:funktionsuebersicht` nennt keine Foren, kein Widerspruch.
- [PASS] **Zählaussagen nachgezählt** (Pflicht, da Text geändert). `06_evaluation_reflexion.tex:5` kündigt „Zwei Stellen erzwangen eine Kursänderung" an und liefert zwei (Community-Zuschnitt, Namenskollision) — durch den Delta nicht gekippt. Der vollständige ZAHLWORT-Block des Skripts wurde gegengeprüft; keine Angabe berührt den Delta.
- [PASS] **Keine Doppelbegründung.** `03_konzept.tex:15` schreibt der Zero-Waste-Woche den Ersatz von Gruppen und Foren als *Anlass für gegenseitige Inspiration* zu, `04:9` dem Rettungs-Feed den *Ort der Sichtbarkeit* und den Challenges die *Bündelung der Beteiligung*. Arbeitsteilung statt Widerspruch.
- [PASS] ½-Seiten-Regel – `04_community_und_feedback.tex` ist netto ±0 Wörter, keine Datei unter die Schwelle gerutscht (einziger HALBSEITE-Hinweis unverändert `03_vorgehen_und_aufbau.tex` mit 136 Wörtern, Altbestand).
- [PASS] Front-/Backmatter, Kapitelstufen, Outline – im Delta unberührt.

## Teil-Check D – Build

- [ÜBERSPRUNGEN] Kompiliert fehlerfrei – `lualatex`, `latexmk` und `biber` sind in dieser Session-Umgebung **nicht installiert** (`which` negativ). Statisch spricht nichts gegen einen sauberen Lauf: Klammerbilanz geprüft, keine neuen Labels, keine neuen Zitationen, keine neuen Bilder.
- [ÜBERSPRUNGEN] Undefined references/citations – nicht messbar. Die zwei im Delta neu gesetzten `\autoref`-Ziele existieren als `\label` (geprüft).
- [ÜBERSPRUNGEN] **Seitenumfang Textteil – für den aktuellen Text ungemessen.** `check_umfang.py` schätzt 3.721 Wörter ≈ 9,9 Seiten gegen die Vorgabe 7–10. Das Skript weist selbst darauf hin, dass „im Soll" innerhalb von ±1 Seite um eine Grenze erst nach dem Build belastbar ist — 9,9 liegt 0,1 Seiten von der Obergrenze. Deshalb gilt das Kriterium als ungeprüft und der Score ist bei 89 gedeckelt.

  **Risikoeinschätzung (nicht als Messung zu lesen):** Der Delta ist netto ±0 Wörter, kostet aber durch die Absatzteilung in `04_community_und_feedback.tex` eine angebrochene Zeile plus einen Absatzabstand, also grob 1–2 Zeilen ≈ 20–35 pt. Dem stehen die oben gemessenen **≈ 134 pt ≈ 8 Zeilen** freier Raum auf der letzten Textseite gegenüber. Ein Kippen auf 11 Seiten ist danach unwahrscheinlich — bestätigt ist es erst durch den Build.
- Weißraum-Diagnose (3a): nicht ausgelöst. Alle Seiten des Textteils laufen bis y ≈ 57–98 pt durch; die einzige große Restfläche liegt auf der letzten Textseite und ist ein Kapitelende, keine Float-Reserve.

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [OFFEN] Umfang im Soll – Spiegel aus Teil-Check D, für den aktuellen Stand ungemessen
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen – Turnitin würde den eigenen Upload als Treffer werten
- [OFFEN] LanguageTool-Durchgang lokal über den Gesamttext

## Teil-Check F – Literaturverzeichnis

- [PASS] `check_bib_hygiene.py`: 10 Einträge, **0 Hinweise**.
- Im Delta unberührt – `references.bib` wurde nicht angefasst. Das gerenderte Verzeichnis wurde zuletzt im Vorbericht vollständig gelesen; die dortigen Befunde sind erledigt.

## Teil-Check G – Quellentreue (Volltextabgleich)

- [PASS] **19 Zitationen geprüft · FUNDSTELLE OK 19 · offen 0** (Details: `quellencheck.md`).
- Befunde je Klasse: **keine.** Kein WORTLAUT, kein ZITAT WEICHT AB, kein SEITE VERDÄCHTIG, kein SEITE AUSSERHALB, kein CLAIM SCHÄRFER, kein NICHT PRÜFBAR, kein RENTIERT NICHT.
- **Der Delta hat keine Zitation invalidiert.** Der Zähler ist von 20 auf 19 gefallen, weil die Soma-Zitation `856964c7c8` (`04_community_und_feedback.tex:7`) mit dem ersetzten Absatz entfallen ist — ein sauberer Rückbau, kein offener Befund. Die verbleibende Shen-Zitation in derselben Datei (`c06e959e3b`) blieb unberührt, weil ihr Trägersatz nicht angefasst wurde.
- Bemerkenswert: Der entfallene Eintrag trug in seiner Notiz bereits den Satz „Der Trägersatz gibt das enger wieder als die Quelle" — der Delta hat damit genau die Stelle beseitigt, an der Teil-Check G zwar `FUNDSTELLE OK` meldete, die Reichweite aber angespannt war. Das ist der im Skill beschriebene Unterschied zwischen Fundstelle und Reichweite, hier zugunsten der Arbeit aufgelöst.
- Notiz-Wächter: kein `[NOTIZ-DUBLETTE]`, kein `[NOTIZ-FREMDER-AUTOR]`.
- Volltexte ohne Bib-Verweis (3): Krug- und Norman-EPUBs aus der Vorarbeit sowie die Vittuari-Preprint-Fassung neben der zitierten Verlagsfassung. Unschädlich, wie in den Vorberichten.

## Teil-Check H – Lesefluss

Nur der Delta gelesen (die Cold-Read-Session desselben Tages hat alle 12 Subsections abgedeckt):

- [PASS] Anschlüsse im neuen Absatz `04:9` lösen alle auf: „Beides" → „Gruppen und Foren" (Vorsatz), „Genau das" → „ein Ort, an dem der eigene Erfolg gesehen wird", „dafür" → „der Austausch über Rezepte", „Jeder weitere Bereich" → relativ zum Feed. Kein hängender Bezug.
- [PASS] Absatzöffner `04:9` ist eine Aussage, kein abgeschnittener Rest.
- [HINWEIS] `04:7` ist nach der Teilung ein **Ein-Satz-Absatz** (35 Wörter). Er trägt eine vollständige Aussage und führt die Challenges ein, wirkt neben dem sieben Sätze langen Folgeabsatz aber dünn. Kein Befund — die Teilung war der Zweck der Überarbeitung (Challenges vom Verzicht trennen). Falls beim finalen Durchlesen etwas hakt: erster Kandidat für einen Rückbau.

## Claims

- Ungesicherte FACTUAL CLAIMS: **keine.** Die drei neuen Begründungen sind arbeitseigene Ableitungen mit Verweis auf eigene Kapitel, keine Außenweltbehauptungen.
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: `pexelsHasanbekavaBasket` – **kein echter Fund**, wird über `\citeauthor`/`\citeyear` in der Quellenzeile von `tab:persona` genutzt. **Nicht entfernen.**

## Punkteabzug im Detail

- Seitenumfang / Teil-Check D nicht lauffähig: **Score-Deckel bei 89** statt Einzelabzug. Kein Textbefund.
- Sonst: **keiner.** Befunde 2–4 sind Hinweise ohne Score-Wirkung (Kommasetzung, Präzision, Einzelvorkommen eines Stilmarkers).

## Bewertungsschwerpunkte (Projektbericht)

- **Qualität (25 %)**: [ABGEDECKT] – die Abhakliste ist an der letzten offenen Stelle („Gruppen/Foren") jetzt ausdrücklich beantwortet.
- **Prozess (25 %)**: [ABGEDECKT] – `06_evaluation_reflexion.tex:5` führt die Kursänderung weiterhin als eine von zwei Stellen.
- **Transfer (15 %)**: [ABGEDECKT]
- **Kreativität (15 %)**: [ABGEDECKT] – `03_konzept.tex:15` unverändert tragend, Vokabel angeglichen.
- **Dokumentation (10 %)**: [ABGEDECKT] – die vier Prompt-Zitate geben jetzt den tatsächlichen Wortlaut wieder, was die Nachvollziehbarkeit der KI-Nutzung eher stärkt als schwächt.
- **Ressourcen (10 %)**: [ABGEDECKT]

## Lieferobjekt-Abgleich

- [PASS] Alle sechs Lieferobjekte liegen unverändert vor. Der Delta berührt keine Abbildung und keine Tabelle inhaltlich — nur die vier Quellenzeilen unter den Mockups, nicht die Bilder selbst. Eine erneute Bildsichtung war deshalb nicht nötig.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

1. **Seitenzahl des Textteils nach dem Neubau** | `latexmk -g -lualatex main.tex`, dann im PDF „1 Einleitung" und den Beginn des Literaturverzeichnisses suchen | Stimmt, wenn zwischen beiden höchstens 10 gedruckte Seiten liegen | `lualatex`/`latexmk`/`biber` sind in dieser Session-Umgebung nicht installiert.
2. **Wortlaut der vier zitierten Claude-Design-Prompts** | `pages/appendix.tex`, die `\quelle{}`-Zeilen zu `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_feed`, `fig:mockup_profil` | Stimmt, wenn der zitierte Text wortgleich der Eingabe im Claude-Design-Chat entspricht | Der Chatverlauf liegt außerhalb des Repositorys. **Neu zu beachten:** Die Zeile zu `fig:mockup_start_bookmarks` zitiert seit dem Delta einen Folge-Prompt („Ergänze ein …"), führt ihn aber mit „Erstellt mit dem Prompt" ein — derselben Formel, mit der die anderen drei Zeilen ihren *Ursprungs*-Prompt einleiten. Falls dort tatsächlich ein Ursprungsprompt existierte, gehört er ergänzt; falls der Screen wirklich nur aus dem Folge-Prompt entstanden ist, ist die Zeile korrekt.

## Handlungsempfehlungen (nach Priorität)

1. **Neu bauen und die gedruckte Seitenzahl gegenprüfen.** `latexmk -g -lualatex main.tex`. Das ist der einzige Punkt, der den Score bewegt: Ergibt der Textteil 10 Seiten oder weniger, steht der Bericht bei **100/100**. Das eingecheckte `main.pdf` muss dabei mit ersetzt werden — es trägt derzeit den alten Text (Befund 1).
2. **`pages/appendix.tex:53`**: `}, sowie in weiteren` → `}, in weiteren` (Befund 2, ein Wort).
3. **`04_community_und_feedback.tex:9`**: „sucht die Zielgruppe vor allem einen Ort" → „sucht die Zielgruppe einen Ort" (Befund 3, ein Wort).
4. Optional: „bündeln" ersetzen (Befund 4). Ohne Score-Wirkung.

Punkte 2–4 sind Ein-Wort-Änderungen ohne Bezug zu These, Kernargumenten oder Leitfrage und brauchen keine Freigabe. Sie lassen sich vor dem Build in einem Zug erledigen.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

- [ ] **Neu bauen** und das eingecheckte `main.pdf` ersetzen — die abgegebene Fassung darf nicht der alte Stand sein.
- [ ] **Eidesstattliche Erklärung** elektronisch über myCampus abgeben – **vorher nimmt Turnitin die Einreichung nicht an**.
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen.
- [ ] **LanguageTool-Durchgang** lokal über den Gesamttext (3.721 Wörter).
- [ ] Arbeit einmal am PDF am Stück durchlesen.
- [ ] **Keine externe Plagiatssoftware vorab** – ein Voraberprüfungs-Upload erzeugt einen Turnitin-Selbsttreffer.
- [ ] Manueller Prüfpunkt 2 oben: die vier zitierten Prompts gegen den Chatverlauf abgleichen.
- [ ] Namensverfügbarkeit „Resteria" (DPMA, .de-Domain) – nicht abgabekritisch.

---

## Nachtrag 30.07.2026 – Überarbeitung nach diesem Bericht

Umgesetzt in derselben Session auf Nutzerentscheidung. Kein neues Audit; die Punkte sind mechanisch und berühren weder These noch Kernargumente noch Leitfrage.

### Chefkoch-Vergleichssatz gestrichen (Nutzer-Anstoß, nicht aus diesem Bericht)

Der Nutzer hat gefragt, ob der mit „Hinzu kommt," beginnende Satz in `04_community_und_feedback.tex:9` entfallen kann — der zweite der drei arbeitseigenen Gründe, die PR #16 dort aufgebaut hat („der Austausch über Rezepte ist die Stärke der etablierten Communitys: Chefkoch.de hat dafür einen gewachsenen Bestand an Beiträgen, Resteria würde bei null anfangen"). **Vorab auf Beschädigung geprüft, Ergebnis: unbedenklich.**

| geprüft | Ergebnis |
|---|---|
| Verwaistes Label durch den entfallenden `\autoref{sec:wettbewerbsanalyse}`? | Nein – das Label wird an drei weiteren Stellen referenziert (`03_konzept.tex:7`, `:24`, `01_kernergebnisse_und_ausblick.tex:3`). |
| Zitation betroffen? | Nein – der Satz und der ganze Absatz tragen keine. Teil-Check G nach der Änderung erneut gefahren: **19/19 FUNDSTELLE OK**, kein Trägersatz-Hash bewegt. |
| Zählaussage im Text, die „drei Gründe" verspricht? | Nein – Grep über `chapters/` auf Grund/Gründe/erstens/zweitens/drittens: kein Treffer. Die Dreizahl steht nur in der PR-Beschreibung und in `CLAUDE.md`. |
| Prüfer-Steuerung „Entscheidungen beruhen auf der Vergleichsanalyse"? | **Weiterhin erfüllt.** `04_community_und_feedback.tex:3` verankert das Kapitel bereits an der Analyse („wodurch der Feed genau den Austausch ermöglicht, den die Wettbewerbsanalyse bei den reinen Reste-Matching-Apps vermisst hat"). Die Anbindung läuft danach über eine positive Entscheidung statt über eine Auslassung. |
| Bleibt die Austausch-Dimension gedeckt? | Ja, an zwei vorher gelesenen Stellen: `04:3` (Kommentieren und Bewerten) sowie `03_konzept.tex:13` und `tab:funktionsuebersicht` („Zubereitungstipps austauschen" → Aufgaben-Zweck Kochtipp-Austausch). Im Verzichts-Absatz selbst wird die Frage danach nur noch implizit beantwortet — das ist der einzige reale Verlust und war die bewusste Abwägung. |

Zusätzlich beseitigt die Streichung eine Halb-Redundanz: Der entfallene Satz und der behaltene („Jeder weitere Bereich müsste zudem gefüllt werden …") begründeten beide fehlende Masse — einmal als Wettbewerbsnachteil, einmal als interne Verdünnung. Der behaltene ist der spezifischere, weil er an der eigenen schmalen Zielgruppe hängt. Das „zudem" bezieht sich danach auf einen Grund statt auf zwei und bleibt korrekt.

### Befund 3 umgesetzt

`04_community_und_feedback.tex:9`: „sucht die Zielgruppe **vor allem** einen Ort" → „sucht die Zielgruppe einen Ort". Der Satz schreibt `sec:zielgruppe` damit keine Rangfolge mehr zu, die dort nicht steht.

### Befund 2 umgesetzt

`pages/appendix.tex:53`: „}, **sowie** in weiteren Iterationsschritten verfeinert" → „}, in weiteren Iterationsschritten verfeinert". Alle vier `\quelle{}`-Zeilen tragen jetzt wieder dieselbe Anschlussformel (maschinell gegengeprüft, 4/4 identisch); das Komma vor „sowie" ist mit entfallen.

### Nicht umgesetzt

Befund 4 (`META-VERB` „bündeln") bewusst gelassen – Einzelvorkommen, kein Regelverstoß, und „bündeln" ist an der Stelle das genauere Verb.

### Prüfstand nach der Überarbeitung

- `check_all.py --mit-quellen`: **alle sechs Skripte ohne harte Funde**, `check_formalia.py` 0 FEHLER (47 Hinweise, unverändert – keine neue Klasse).
- `check_quellentreue.py`: **19/19 FUNDSTELLE OK**, keine Invalidierung.
- `check_umfang.py`: **3.691 Wörter** (vorher 3.721, −30), Korridor 2.625–3.750. Die Streichung entlastet die Seitenzahl zusätzlich.
- **Weiterhin offen: der Build.** Handlungsempfehlung 1 ist unverändert der einzige score-relevante Schritt; die Session-Umgebung hat keine LaTeX-Toolchain, und `main.pdf` im Repository ist nach dieser Überarbeitung erst recht veraltet.
