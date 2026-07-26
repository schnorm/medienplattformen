# Prüfbericht — Projektbericht

**Datum**: 26.07.2026 · **Geprüfter Stand**: Delta der Überarbeitung vom 26.07.2026 (Commit `1843fa8`, 9 Kapitel-/Seitendateien) · **Audit-Typ**: Delta-Re-Audit
**Score: 100/100 — abgabereif** (unter dem Vorbehalt des noch ausstehenden lokalen Builds, siehe Teil-Check D)

**Prüfumfang**: Re-Audit nach Überarbeitung, also Delta statt Vollprüfung — die fünf FAIL-Befunde des Voll-Audits vom 24.07.2026 gezielt nachgeprüft, dazu beide Skripte vollständig, `check_status.py`, Teil-Check D und die Pflichtregeln der berührten Kapitel. Nicht erneut gelesen wurden die sechs unveränderten Kapiteldateien.

**Zusätzlicher Prüfpunkt aus dem Vorbericht**: Die dortige Lehre (b) — „Kürzungsrunden können Pflicht-Schichten mitreißen, ein Delta-Re-Audit sollte die Pflichtregeln der berührten Kapitel mitprüfen" — wurde hier erstmals angewandt. Die Überarbeitung enthält genau eine Streichung (Pointen-Schlusssatz in `02_limitationen.tex`); sie ist gegen alle sieben Pflichtregeln aus `typen/projektbericht.md` gegengeprüft, kein Verlust.

**Memory-Hinweise berücksichtigt**: `MEMORY.md` — Teil-Check E fließt in keinem Umfang in den Score ein (Nutzer-Festlegung 2026-07-19). `PERSISTENT.md` — `\SubmissionDate` bewusst auf `\today`; Grundprinzip „Erst prüfen, dann behaupten" angewandt (`hard-rules-formal.md` → Zitation/Akronyme und `typen/projektbericht.md` → Pflichtregeln vor jeder Formalia-Aussage gelesen, `acronym`-Paket in `main.tex:23` verifiziert statt angenommen).

**Ausgenommen**: Befund 6.3 aus `AENDERUNGEN.md` (Plus-Button-Überlapp im Rettungs-Feed-Mockup) bleibt auf ausdrückliche Nutzer-Anweisung vom Audit ausgenommen — weder Fund noch Abzug. Der Bildaustausch in Claude Design ist weiterhin ein externer Nutzer-Schritt.

---

## Delta-Prüfung der fünf Befunde

### Befund 1 — Zitationen narrativ/parenthetisch · **BEHOBEN**

Alle elf im Vorbericht benannten Stellen sind auf `\textcite` umgestellt, die vorangestellte Namensnennung ist jeweils gestrichen — nachgezählt: `03_konzept.tex` 4× (Z. 7, 28 ×2, 30), `04_community_und_feedback.tex` 2× (Z. 5, 7), `01_kernergebnisse_und_ausblick.tex` 4× (Z. 5), `02_limitationen.tex` 1× (Z. 3) = 11. `\textcite` kommt damit von null auf elf Vorkommen.

Die fünf Klammerzitate, die laut Anweisung unverändert bleiben sollten, sind unverändert: `01_ausgangslage_und_problem.tex:5` (2×, Autorenschaft nicht Thema des Satzes) und die drei Tabellenzellen in `tab:funktionsuebersicht` (`03_konzept.tex:43`). Keine weiteren `\parencite` im Fließtext.

Stichprobe auf Umbaufolgen — die typische Fehlerquelle bei dieser Art Ersetzung: Seitenangaben sind an allen vier betroffenen Stellen erhalten (`[S. 1]`, `[S. 9]` 2×, `[S. 10]`), kein verwaister Satzrest, keine Numerus-Fehler (`\textcite{…} belegen/stützen/unterscheiden` — durchgehend Plural, korrekt für die „et al."-Quellen), und die zwei Stellen, an denen das gestrichene Klammerzitat am Satzende stand, sind sauber neu geschnitten (`03_konzept.tex:30` und `04_community_und_feedback.tex:7` setzen jetzt einen Doppelpunkt statt eines Punkts). `check_bib_keys.py`: 6/6 Keys valide, keine ungenutzten Einträge.

### Befund 2 — Drei Abkürzungen ohne Einführung · **BEHOBEN**

`pages/acronyms.tex` enthält jetzt `\acro{BMEL}{Bundesministerium für Ernährung und Landwirtschaft}` und `\acro{SDG}{Sustainable Development Goal}`, alphabetisch einsortiert, das optionale Breiten-Argument korrekt auf `[BMEL]` aktualisiert. Ein Grep über `chapters/` und `pages/` nach `BMEL|SDG|USP` außerhalb von `\ac{}` liefert nur noch die Definitionszeilen selbst — alle neun BMEL- und beide SDG-Fundstellen laufen über `\ac{}`, „USP" ist durch die Umformulierung in Befund 3 vollständig verschwunden.

Reihenfolge der Erstnennung geprüft (bei `\ac{}` entscheidet die Dokument-Reihenfolge, nicht die Dateireihenfolge): BMEL expandiert zuerst in `01_ausgangslage_und_problem.tex:7` (Kapitel 1, die tatsächliche Erstnennung), SDG in `06_evaluation_reflexion.tex:5`. Das Abkürzungsverzeichnis vor dem Text setzt die Einträge nicht auf „verwendet", die Auflösung im Fließtext greift also. Ein Nebeneffekt der Auflösung steht unter „Kosmetik".

### Befund 3 — Widerspruch an der tragenden Aussage · **BEHOBEN**

`01_wettbewerbsanalyse.tex:36` lautet jetzt: „Das Alleinstellungsmerkmal von Resteria liegt damit in der Verbindung beider Elemente um eine wechselseitige Community herum, die über das Verfolgen von Creator-Inhalten hinausgeht." Der Satz präzisiert gegen leftovercooking, statt die eigene These zu verneinen; er zeigt jetzt in dieselbe Richtung wie der Folgesatz („Die Kombination … bleibt damit die eigentliche Lücke") und wie Z. 34 („Die Stärke liegt in genau dieser Kombination"). Die vier Einwände und ihre Entkräftung sind unverändert.

Zwei Zugaben über den Auftrag hinaus, beide unschädlich: Der Kosmetik-Punkt aus dem Vorbericht („was die Hürde ist, welche die Reste-Matching-Apps bereits gelöst haben") ist mitkorrigiert („und genau diese Hürde nehmen die Reste-Matching-Apps den Nutzer:innen bereits ab"), und mit „nicht im bloßen Verbinden …, sondern in …" ist eine der fünf gezählten „nicht X, sondern Y"-Konstruktionen entfallen — der Anti-KI-Stil-Abstand zur Häufungsschwelle wächst.

Begriffskonsistenz nachgeprüft: „Alleinstellungsmerkmal" ist jetzt die einheitliche Vokabel und deckt sich mit `01_kernergebnisse_und_ausblick.tex:5` („eigenständig hergeleitetem Alleinstellungsmerkmal"). „USP" war der einzige Ausreißer.

### Befund 4 — Erste Feedback-Schleife: falscher Akteur, nicht vorhandener Klick-Prototyp · **BEHOBEN**

`07_iteratives_design.tex:3` steht im Planungsmodus: „… sollen Bedienführungs-Entscheidungen … am Klick-Prototyp geprüft werden …". Der Bericht ist nicht mehr Akteur einer künftigen Projektphase, und der Klick-Prototyp erscheint nicht mehr als vorhandenes Prüfobjekt. Im Folgeabsatz ist „im weiteren Entwicklungsprozess" zu „im Entwicklungsprozess" gekürzt; die Ausnahmelesart, die die erste Schleife von der Planungs-Kennzeichnung ausgenommen hat, entfällt damit — der Disclaimer deckt jetzt alle Schleifen einschließlich der Design-Phase.

`06_evaluation_reflexion.tex:9` ist wie angewiesen nicht angefasst worden (dort ist die real durchgeführte Mockup-Nachbesserung korrekt als Entstehungsgeschichte ausgewiesen). Ein sprachlicher Rest im ersten Satz derselben Zeile steht unter „Kosmetik".

### Befund 5 — Limitation 2 ohne Mitigations-Schicht · **BEHOBEN**

`02_limitationen.tex:5` enthält jetzt alle drei Pflicht-Schichten: Grund (KI-generiert, keine Rückmeldung realer Nutzer:innen) · **Mitigation** („Diese Grenze mildert der Bericht, indem die Herkunft des Mockups transparent gekennzeichnet ist und sich die Darstellung auf die Kernfunktion Reste-Matching … beschränkt.") · zukünftiger Schritt (Usability-Test mit funktionsfähigem Prototyp). Limitation 1 und 3 sind unverändert dreischichtig.

Die Gegenfinanzierung ist wie vorgeschlagen erfolgt: Der Pointen-Schlusssatz am Kapitelende ist gestrichen. Gegen die Pflichtregeln gegengeprüft — der Satz trug keine der drei Schichten (der reale Nutzertest als nächster Schritt steht weiterhin in Limitation 1, der Ausblick in `01_kernergebnisse_und_ausblick.tex:7`), es geht also nichts verloren. Dass das Fazit nun mit der dritten Limitation endet, entspricht der im Typ-File vorgegebenen Fazit-Reihenfolge (Kernergebnisse → Ausblick → Limitationen) und ist kein Struktur-Verstoß.

---

## Skripte und Regressionskontrolle

- **`check_bib_keys.py references.bib --dir chapters/ --report-unused`**: alle 6 Keys valide, keine ungenutzten Einträge. Unverändert zum Vorbericht.
- **`check_formalia.py chapters/`**: **0 FEHLER**, 11 HINWEIS über 15 Dateien — einer weniger als vor der Überarbeitung (12). Kein einziger neuer Hinweis: acht der elf sind Tabellen-Artefakte (die Satzlängen-Heuristik zählt `tabularx`-Zeilen als Sätze), zwei sind bekannte TRIAS-Meldungen mit sachlich genau drei Elementen, einer ist der Durchschnitts-Satzschnitt in `05_phasenplanung.tex`, ebenfalls tabellengetrieben.
- **`check_status.py`**: 0 FEHLER, 10 HINWEIS. Der Hinweis auf den unzulässigen Statuswert „ÜBERHOLT" in der Prüf-Audit-Zeile ist mit diesem Audit korrigiert. Die neun `DATEI-OHNE-ZEILE`-Hinweise sind die etablierte Projektkonvention (Kapitel-Zeilen statt einer Zeile je Subsection), keine Inkonsistenz.
- **Querverweise**: alle 14 `\autoref`-Ziele haben ein existierendes `\label` (Vollabgleich über `chapters/` und `pages/`), keine doppelten Labels.
- **Zählangaben in den geänderten Stellen** nachgezählt: „sechs Vertreter aus drei Plattform-Kategorien" (6 Tabellenzeilen, 3 Kategorien ✓), „ein bis drei Vertreter" (2/3/1 ✓), „mehrere Einwände / drei naheliegende Gegenargumente" (3 + 1 gewichtigerer ✓), „drei Grenzen" implizit über drei Absätze ✓.
- **½-Seiten-Schwelle**: kleinste Datei 159 Wörter, keine HALBSEITE-Meldung — die Streichung in `02_limitationen.tex` (280 Wörter) hat keine Datei unter die Schwelle gedrückt.
- **Pflichtregeln der berührten Kapitel** (Lehre (b) aus dem Vorbericht): Limitationen dreischichtig ✓ · Aktualität/Zeitbezug in der Einleitung ✓ (unverändert, `01_ausgangslage_und_problem.tex:5`) · Syntheseleistung pro Hauptkapitel ✓ · Phasenplanung als Tabelle ✓ (nicht berührt) · Dritte Person streng ✓ (die begründete Abweichung „pronomenfreier Selbstbezug" gilt unverändert; die neuen Formulierungen „mildert der Bericht" und „sollen … geprüft werden" sind pronomenfrei) · Leitfrage ≠ These ✓ · Normative Ebene der These ✓.
- **Umfang**: 4.890 Wörter Fließtext einschließlich Tabellenzellen gegenüber 4.870 im Vorbericht — netto **+20 Wörter**. Der Mitigationssatz (+34) und die gestrichenen Namensdopplungen (−ca. 20) heben sich gegen den gestrichenen Schlusssatz (−26) weitgehend auf. Die Schätzung bleibt damit unverändert bei 9–10 Seiten.

## Teil-Check D — Build

- [ÜBERSPRUNGEN] Kompiliert fehlerfrei — `lualatex`, `latexmk`, `biber` und `pdflatex` sind in dieser Umgebung weiterhin nicht installiert (geprüft, nicht angenommen). Kein Abzug, da nicht prüfbar.
- [ÜBERSPRUNGEN] Undefined references/citations, fehlende Bilder, doppelte Labels — statisch geprüft (Label/`\autoref`-Vollabgleich, BBT-Keys, Bilddateien in `images/durchfuehrung/`), keine Auffälligkeiten. Die Laufzeitprüfung bleibt Nutzer-Schritt.
- [ÜBERSPRUNGEN] Seitenumfang — geschätzt 9–10 Seiten von 7–10, unverändert am oberen Rand. **Weiterhin der wichtigste offene Nutzer-Schritt.**

## Teil-Check E — Abgabe (informativ, kein Score-Abzug)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben — **ohne diesen Schritt nimmt Turnitin die Einreichung nicht an.**
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen.
- [PASS, unbestätigt] Umfang im Soll — Spiegel aus Teil-Check D.
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko).
- [ERINNERT] LanguageTool-Durchgang lokal über den Gesamttext.

## Punkteabzug im Detail

| Kategorie | Abzug | Vorkommen |
|---|---|---|
| Fehlender Pflicht-Punkt aus Typ-Datei | 0 | Limitationen jetzt dreischichtig |
| Struktur-Verstoß | 0 | beide Befunde behoben |
| Formalia-Verstoß | 0 | beide Befunde behoben |
| Build / Referenzen / Seitenumfang | 0 | nicht prüfbar, ausgewiesen als ÜBERSPRUNGEN |
| Anti-KI-Stil, Verständlichkeit | 0 | unter der Häufungsschwelle |
| **Summe** | **0** | **Score 100/100** |

**Zur Belastbarkeit des Scores**: 100/100 heißt hier „alle prüfbaren Kriterien erfüllt", nicht „alle Kriterien geprüft". Teil-Check D ist zum dritten Mal in Folge übersprungen, und der Seitenumfang ist ein Pflichtkriterium der Aufgabenstellung, das allein dort gemessen wird. Bei einer Schätzung von 9–10 Seiten gegen eine Vorgabe von 7–10 liegt die Arbeit am oberen Rand — der lokale Build ist deshalb kein Formalschritt, sondern die letzte offene Prüfung. Diese Lücke ist in `SKILL-VERBESSERUNGEN.md` (Befund 5) bereits als Workflow-Schwäche vermerkt.

## Kosmetik (kein Score-Abzug, freiwillig)

1. **Erstnennung von `\ac{}` im Bindestrich-Kompositum.** `01_ausgangslage_und_problem.tex:7` schreibt „die \ac{BMEL}-App"; da dies die Erstnennung ist, rendert das `acronym`-Paket „die Bundesministerium für Ernährung und Landwirtschaft (BMEL)-App" — die Langform steht unflektiert als Bestimmungswort eines Kompositums. Sauberer wäre eine Position, in der die Vollform grammatisch trägt, etwa „… oder die App \enquote{Zu gut für die Tonne!} vom \ac{BMEL}, die genau dieses Matching leisten …"; alle späteren Vorkommen rendern dann ohnehin als kurzes „BMEL-App". Derselbe Effekt trifft `\ac{MVP}` in `07_iteratives_design.tex:3` („in die Minimum Viable Product (MVP)-Entwicklung"), seit die `\input`-Reihenfolge in Runde 5 diese Subsection vor `05_phasenplanung.tex` gezogen hat. **Erst nach dem lokalen Build entscheiden — im PDF ist in einer Sekunde sichtbar, ob das stört.**
2. **Wiederholter Mitigations-Öffner.** `02_limitationen.tex:3` und `:5` beginnen ihre Mitigations-Schicht fast wortgleich („Diese Grenze mildert dieser Bericht, indem …" / „Diese Grenze mildert der Bericht, indem …"), zusätzlich mit uneinheitlichem Artikel. Ein variierter zweiter Öffner (z. B. „Abgemildert wird das dadurch, dass …") löst beides.
3. **Doppeltes „damit".** `01_wettbewerbsanalyse.tex:36` schließt mit zwei aufeinanderfolgenden „damit"-Sätzen. Die Richtung stimmt jetzt, die Wortwiederholung bleibt.
4. **Gemischte Modalität.** `07_iteratives_design.tex:3` beginnt mit „durchlaufen Mockup und Klick-Prototyp … eine erste Rückkopplungsschleife" (Indikativ Präsens), während der Folgesatz auf „sollen … geprüft werden" umgestellt ist. „sollen … durchlaufen" im ersten Satz würde den Planungsmodus des Absatzes vereinheitlichen.
5. Unverändert offen aus dem Vorbericht, jeweils bewusst nicht Auftrag der Überarbeitungssession: die unbelegte Zelle „BMEL-App / Rezept-Austausch = mittel" in `tab:wettbewerbsvergleich` · „Nudge-Forschung" für Nivedhitha et al. in `03_konzept.tex:28` (dort geht es um Green Social Network Affordances) · die MVP-Erklärung in `05_phasenplanung.tex:3` nach der Erstnennung · der offene Vergleichspunkt „als vorher" in `02_zielgruppe.tex:7`.

## Claims

- **Ungesicherte FACTUAL CLAIMS**: keine neuen. Die zwei bekannten Verifikations-Vorbehalte bestehen fort (Nivedhitha et al. 2024, Shen et al. 2023 nur über Abstract erschlossen). Die Umstellung auf `\textcite` hat beide werkbezogen und ohne Seitenangabe belassen — formal korrekt und inhaltlich weiterhin vorsichtig formuliert.
- **Fehlende OWN WORK-Markierungen**: keine.
- **Offene `% UNVERIFIED:`-Marker**: keine.
- **Ungenutzte Bib-Einträge**: keine.

## Handlungsempfehlungen

Keine score-relevanten. Alle fünf Befunde des Voll-Audits sind behoben, ein weiterer Prüf-Schreib-Zyklus ist nicht nötig.

1. **Lokalen Build fahren** — der einzige verbliebene Schritt mit Score-Potenzial (Seitenumfang, undefined references). Nutzer-Aufgabe.
2. Optional: die vier Kosmetik-Punkte, am sinnvollsten nach dem Build, wenn das PDF vorliegt. Kein Score-Effekt, Kürzungsreserve von etwa 20 Wörtern.

**Vor der Abgabe genügt kein weiteres Audit** — sofern der Build sauber durchläuft und der Umfang im Soll liegt, ist der Textstand einreichbar. Bringt der Build Funde, reicht ein erneutes Delta-Re-Audit auf die betroffenen Stellen.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

- [ ] **Lokalen Build fahren** (`latexmk -lualatex main.tex`) — in dieser Umgebung nicht möglich. Danach prüfen: keine undefined references/citations, alle vier Mockups eingebunden, keine doppelten Labels. **Neu mitprüfen**: wie die elf `\textcite`-Stellen und die zwei neuen Abkürzungen im Satz stehen (siehe Kosmetik 1).
- [ ] **Seitenumfang des Textteils bestätigen** (ab „1 Einleitung" bis vor das Literaturverzeichnis): Vorgabe 7–10 Seiten, Schätzung 9–10. Bei Überschreitung zuerst die Kosmetik-Punkte und die Redundanz zwischen `06_evaluation_reflexion.tex` und `02_limitationen.tex` nutzen.
- [ ] **Eidesstattliche Erklärung elektronisch über myCampus abgeben** — Voraussetzung dafür, dass Turnitin die Einreichung überhaupt annimmt.
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen.
- [ ] **LanguageTool-Durchgang lokal über den Gesamttext** — seit dem letzten Voll-Audit sind elf Sätze umgebaut worden.
- [ ] **Nivedhitha et al. (2024) und Shen et al. (2023) am Volltext verifizieren**, sobald zugänglich (bisher nur Abstract; IU-KI-Richtlinie verlangt die Prüfung am Original).
- [ ] **Namensverfügbarkeit „Resteria" prüfen** (DPMA, .de-Domain) — offener Punkt seit der Plan-Phase.
- [ ] **Rettungs-Feed-Mockup nachbessern** (Befund 6.3: Plus-Button-Überlapp) — Folge-Prompt liegt in `sources/claude-design-nachbesserung.md`, `\quelle{}`-Zeile ist vorbereitet. Externer Schritt in Claude Design.
- [ ] Keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko).
- [ ] **Endgültig entscheiden**: Einstiegsliteratur Hansch & Rentschler (2012) und Kapoor et al. (2018) per Zotero/BBT importieren — oder als verworfen abhaken. Laut `aufgabe.md` nicht verpflichtend; der Punkt taucht seit Runde 1 in jeder Runde erneut auf.
- [ ] Nach der Abgabe: `MEMORY.md` Eintrag für Eintrag durchgehen und projektübergreifende Punkte nach `PERSISTENT.md` übertragen. Kandidaten: (a) die Voice-Abweichung „pronomenfreier Selbstbezug statt ‚Die Projektgruppe'" bei Einzelautorenschaft, (b) die Lehre, dass Kürzungsrunden Pflicht-Schichten mitreißen können — in diesem Delta-Re-Audit erstmals als eigener Prüfschritt angewandt und dadurch belastbar geworden, (c) die Beobachtung, dass ein nie gelaufener Teil-Check D einen 100/100-Score trägt, ohne das Pflichtkriterium Seitenumfang je geprüft zu haben.
