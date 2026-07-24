# Prüfbericht — Projektbericht

**Datum**: 24.07.2026 · **Geprüfter Stand**: alle Kapitel nach `AENDERUNGEN.md` Runde 4 (Kürzungsrunde) · **Audit-Typ**: Delta-Re-Audit
**Score: 90/100 — abgabereif** (ein Zählwiderspruch als Kürzungs-Regression, vor Abgabe beheben; Teil-Check D Build weiterhin lokal zu bestätigen)

Delta-Umfang laut Skill-Regel: geprüft wurden die durch Runde 4 geänderten Stellen (10 Kapiteldateien, `git diff HEAD~2 HEAD -- chapters/`), beide Skripte vollständig, `check_status.py`, sowie die kapitelübergreifenden Folgen der Kürzungen (Querverweise, Begriffserklärungen, Zählangaben, Abhakliste-Abdeckung). Nicht erneut vollständig gelesen wurden unveränderte Passagen — deren Befund aus dem Voll-Audit vom 23.07.2026 (100/100) bleibt gültig.

`PERSISTENT.md`/`MEMORY.md` gelesen — keine abweichenden Audit-Kriterien; Teil-Check E bleibt score-neutral (MEMORY-Festlegung 2026-07-19).

## Teil-Check A — Formalia
- [PASS] Zitationen — `check_bib_keys.py`: alle 6 Keys valide, keine erfundenen, keine ungenutzten. Die Kürzungen haben keine `\parencite` entfernt; Barkers Beleg wandert im Fazit korrekt auf die Erinnerungsbenachrichtigung (Propagationslücke aus GS-2 geschlossen).
- [PASS] Eigene Werke — `\quelle{}`-Zeilen unverändert, alle 5 eigenen Abb./Tab. und die 4 KI-Mockups weiterhin korrekt gekennzeichnet.
- [PASS] Pronomen — `check_formalia.py` 0 FEHLER.
- [PASS] LaTeX-Format — 0 FEHLER über alle 14 Dateien.
- [PASS] Akronyme — `\ac{MVP}` unverändert korrekt.
- [PASS] Cross-References & Labels — alle `\autoref`-Ziele weiterhin definiert; kein Verweis ist durch die Kürzungen verwaist. `tab:funktionsuebersicht` hat nach Streichung des Einleitungssatzes noch genau einen Textverweis (aus `06_evaluation_reflexion.tex`) — formal ausreichend, siehe HINWEIS unter Teil-Check C.
- [PASS] Anti-KI-Stil — kein GEDANKENSTRICH-Treffer; 3× TRIAS weiterhin nur in `05_phasenplanung.tex` (echte Phasen-/Ressourcenaufzählungen), unter dem Häufungs-Deckel.
- [PASS] Verständlichkeit — 10 HINWEISE, davon 4 durch Tabelleninhalt verzerrte SATZLAENGE-Treffer (die Skript-Heuristik liest Tabellenzeilen als Sätze). Kein Kapitel überschreitet die Häufungsschwelle. Ein Einzelbefund zur entfallenen UI/UX-Erläuterung siehe HINWEIS 2 unten (nicht gehäuft, kein Abzug).
- [PASS] Keine offenen `% UNVERIFIED:`-Marker.
- [PASS] `main.tex`/`pages/cover.tex` durch Runde 4 nicht berührt.

## Teil-Check B — Argumentationsqualität
- [PASS] These erkennbar — Leitfrage/Ziel und These durch die Kürzungen unberührt.
- [N.A.] Forschungslücke in Einleitung — laut `projektbericht.md` nur „Optional".
- [PASS] Aktualität/Zeitbezug in Einleitung — unverändert (SDG 12.3, Plattformlandschaft).
- [FAIL-nah, siehe Struktur] Gegenargumente reflektiert & entkräftet — inhaltlich weiterhin erfüllt: alle vier Einwände stehen nach wie vor im Text und werden einzeln entkräftet. Der Fehler liegt allein in der Ankündigungszahl (siehe Struktur-Verstoß 1), nicht in der Substanz.
- [PASS] Syntheseleistung pro Hauptkapitel — Verknüpfung Wettbewerbsanalyse + Verhaltensliteratur + Konzept bleibt erhalten; die Kürzung im Fazit hat die Trennung „literaturbasierte Hebel vs. eigenständige Differenzierung" beim Verschmelzen bewusst mitgenommen.
- [PASS] Limitationen dreischichtig — drei Grenzen je mit warum · Mitigation · zukünftigem Schritt; der gekürzte Schlussabsatz streicht nur die Wiederholung des Kernbefunds, nicht eine Schicht.
- [N.A.] Ergebnisse ≠ Interpretation — nur empirische Seminararbeit.
- [PASS] Typspezifisch (Projektbericht) — Phasenplanung (5 Phasen, Tabelle stimmt mit Fließtext überein), Eigendarstellungs-Quellen, Produktdokumentation, dritte Person: unverändert.
- [PASS] Leitfragen aus `aufgabe.md` beantwortet — der stark gekürzte Abgleich in `06_evaluation_reflexion.tex` benennt alle drei Teilaufgaben weiterhin mit Fundstelle und verweist für die Berichtsinhalte jetzt auf `tab:funktionsuebersicht` statt sie aufzuzählen.
- [PASS] Abhakliste-Abdeckung nachgeprüft (Grep, nicht Leseeindruck): Rezept-Uploads (`03_konzept.tex:32,44`), Kommentar-/Bewertungssystem (`:32,45`), personalisierte Empfehlungen (`:32,46`), Menüplanung/Journaling (`:34,47`), Gruppen/Foren und Event-Kalender je begründet ausgeschlossen. Kein Schlüsselbegriff ist der Kürzung zum Opfer gefallen.
- [PASS] Dimensionsabgleich — alle Bewertungsdimensionen weiterhin im Text vertreten.

## Teil-Check C — Struktur
- [PASS] ½-Seiten-Regel — kein HALBSEITE-Treffer mehr. Knappste Dateien: `02_zielsetzung_und_verengung.tex` (155 Wörter) und `03_vorgehen_und_aufbau.tex` (156 Wörter), beide über der 150-Wörter-Schwelle. Die konservativere Umsetzung von 4.4 hat hier genau richtig gebremst.
- [PASS] Max. 3 Kapitelstufen · Front-/Backmatter · Outline-Check — durch die Kürzungen unberührt; Kapitelanteile bleiben im Soll (Einleitung/Fazit lagen am oberen Rand und wurden gezielt entlastet).
- **[FAIL] Zahlenangaben gegen die zugehörige Aufzählung** — siehe Struktur-Verstoß 1.

**Roter Faden (Regressions-Stichprobe auf die geänderten Stellen):**
- [PASS] Querverweise semantisch korrekt — die neu gesetzten Verweise in `06_evaluation_reflexion.tex` treffen: iteratives Design steht tatsächlich in `sec:community_und_feedback`, die Funktionalitäten in `tab:funktionsuebersicht`, die Persona in Anhang A. Der neue Vorverweis im Fazit („nicht aus der im Folgenden beschriebenen Verhaltensliteratur") zeigt korrekt auf den Folgeabsatz.
- [PASS] Begriffserklärungen nach Kürzung — „Drivers/Levers" ist weiterhin bei Erstnennung in `03_konzept.tex:7` definiert; im Fazit wurde nur die Zweitdefinition gestrichen. „Nudge-Forschung" bleibt erklärt (verkürzt, aber vollständig).
- [PASS] Übrige Zählangaben nachgezählt: „drei weitere Kernfunktionen" = 3 · „drei Hauptbereiche" = 3 · „fünf Phasen" = 5 Tabellenzeilen · „sechs Vertreter aus drei Plattform-Kategorien, ein bis drei Vertreter" = 2+3+1 · „drei Merkmale" · „drei Grenzen" · „zwei methodische Bausteine" · „zwei Risiken" — alle stimmig. Die gestrichene Angabe „fünf Kriterien" hinterlässt keine offene Behauptung.
- [PASS] Zeitpuffer-Konsistenz Text ↔ Tabelle (innerhalb der MVP-Phase, zwei Wochen) unverändert korrekt.
- [PASS] Tabellenwertungen und Akteurskonsistenz durch die Kürzungen nicht berührt (keine Matrixzelle geändert).

### Struktur-Verstoß 1 — Zählwiderspruch (neu durch Runde 4)
`chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:34` kündigt an: „Gegen diese Einschätzung lassen sich **zwei** Einwände vorbringen." Es folgen jedoch vier: drei kurz abgehandelte („Drei naheliegende Gegenargumente greifen bei genauerem Hinsehen zu kurz: …" — Reste-Matching nicht neu, Foodsharing.de, leftovercooking) plus einer als „Gewichtiger ist der Einwand, …" (reine Community-Plattform). Der Umbau von vier ausformulierten Einwänden auf eine gestaffelte Darstellung hat den Zählsatz nicht mitgeführt.

Genau dieser Fehlertyp wurde bereits in Runde 3 (Befund 3.1) korrigiert — die Kürzung hat ihn an derselben Stelle neu erzeugt. **Fix:** „zwei Einwände" durch eine Formulierung ohne Zahl ersetzen, etwa „Gegen diese Einschätzung lassen sich mehrere Einwände vorbringen." — oder auf „vier" setzen und die Staffelung als „Drei davon greifen … zu kurz" formulieren. Einzeiler, kein inhaltlicher Eingriff.

## Teil-Check D — Build
- [ÜBERSPRUNGEN] Kompiliert fehlerfrei — `latexmk`, `lualatex` und `biber` sind in dieser Umgebung weiterhin nicht installiert. Statisch geprüft: keine doppelten Labels, keine verwaisten Verweise, alle 4 Mockup-PNG unter `images/durchfuehrung/` vorhanden.
- [ÜBERSPRUNGEN → statisch PASS] Keine undefined references/citations, fehlenden Bilder.
- [ÜBERSPRUNGEN] Seitenumfang Textteil (Soll 7–10 S.) — **der zentrale offene Punkt.** Die Umfangsanalyse vom 24.07.2026 schätzte vor Runde 4 rund 4.508 Wörter ≈ 10–11 Seiten; die Kürzungen haben ca. 394 Wörter (~8,7 %) entfernt, womit rechnerisch etwa 4.114 Wörter ≈ 9–10 Seiten bleiben. Das liegt im Soll, ist aber eine Schätzung, kein Messwert — der lokale Build muss sie bestätigen.

## Teil-Check E — Abgabe (informativ, kein Score-Abzug)
- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben — Status laut `CLAUDE.md` → Fristen: [offen].
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen.
- [OFFEN → lokal] Umfang im Soll — Spiegel aus Teil-Check D.
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko).

## Claims
- Ungesicherte FACTUAL CLAIMS: keine. Die Kürzungen haben keinen neuen Fakten-Claim eingeführt; die abgeschwächten Formulierungen aus Runde 3 und der Terminologie-Korrektur bleiben erhalten.
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: keine.
- Offene `% UNVERIFIED:`-Marker: keine.

## Punkteabzug im Detail
- Struktur-Verstoß (Teil-Check C, Zählwiderspruch `01_wettbewerbsanalyse.tex:34`): **−10** (1 Vorkommen, Deckel −30).
- Alle übrigen Kategorien: 0. BBT-Keys 0 · Pflicht-Punkte Typ-Datei 0 · Formalia 0 · Anti-KI/Verständlichkeit unter Häufungsschwelle.
- Teil-Check D (Build/Seitenumfang) nicht bewertet (ÜBERSPRUNGEN — keine spekulativen Abzüge).

## Weitere Hinweise (ohne Score-Wirkung)
1. **Unangekündigte Tabelle** — `chapters/02_durchfuehrung/03_konzept.tex:36`: Der Einleitungssatz zu `tab:funktionsuebersicht` wurde gestrichen (Runde 4). Die Tabelle steht jetzt ohne Anmoderation zwischen zwei Absätzen; ihr einziger Textverweis liegt im späteren `06_evaluation_reflexion.tex`. Formal zulässig, für den Lesefluss aber ein Bruch — ein Halbsatz am Ende des Menüplanungs-Absatzes („…, wie~\autoref{tab:funktionsuebersicht} zusammenfasst.") stellt die Führung mit vier Wörtern wieder her.
2. **UI/UX ohne Erläuterung** — `chapters/02_durchfuehrung/03_konzept.tex:53`: Die Klammer-Erklärung („also die Bildschirmaufteilung und Bedienführung") ist entfallen; die Begriffe sind bei Erstnennung nur noch ausgeschrieben. Einzelbefund, nicht gehäuft, daher kein Abzug — im Sinne der Verständlichkeitsregel („Fachbegriffe bei erster Nennung erklären") aber die schwächste der Runde-4-Kürzungen.
3. **Dangling „dabei"** — `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:13`: Der Absatz beginnt jetzt mit „\enquote{Stark} bedeutet **dabei** …", nachdem der vorangehende Satz mit dem Tabellenbezug gestrichen wurde. Das Rückbezugswort hat keinen lokalen Bezugspunkt mehr. „dabei" ersatzlos streichen genügt.
4. `check_status.py` meldet 9 HINWEISE: acht `DATEI-OHNE-ZEILE` (bekanntes Artefakt — die Statustabelle führt Kapitel, nicht einzelne Subsections) und einen `STATUS-WERT`-Hinweis auf den nicht-standardisierten Wert „ÜBERHOLT" in der Prüf-Audit-Zeile, der mit diesem Bericht aufgelöst wird.

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: [ABGEDECKT] Alle Teilaufgaben real ausgeführt; einzige Einschränkung ist der Zählwiderspruch, der einen Prüfer beim Nachzählen auffällt.
- **Prozess (25 %)**: [ABGEDECKT] Vorgehen dokumentiert und reflektiert; Reflexion durch die Kürzung gestrafft, nicht entkernt.
- **Transfer (15 %)**: gesellschaftlich [ABGEDECKT] · wirtschaftlich [ABGEDECKT] · Ansätze/Modelle begründen [ABGEDECKT].
- **Kreativität (15 %)**: [ABGEDECKT] Vergleich zu 6 Plattformen, USP als Kombination gerahmt.
- **Dokumentation (10 %)**: [ABGEDECKT] Entstehungsgeschichte lückenlos.
- **Ressourcen (10 %)**: [ABGEDECKT] Phasenplanung mit Zeitrahmen, Ressourcen, Puffer, Risiken.

## Lieferobjekt-Abgleich
- [PASS] Alle 6 Lieferobjekte unverändert vorhanden: Wettbewerbsvergleich, Persona, UI/UX-Mockups (4 PNG, inkl. der am 24.07. nachgebesserten Profil- und Feed-Screens), Plattformname, Funktionsübersicht, Phasenplanung.

## Handlungsempfehlungen (nach Priorität, größter Score-Hebel zuerst)
1. **Zählwiderspruch beheben** (`01_wettbewerbsanalyse.tex:34`, „zwei Einwände" → „mehrere Einwände"). Einziger Score-Hebel: +10 → 100/100.
2. **Lokalen Build fahren** (`latexmk -lualatex main.tex`) und **Seitenumfang messen** — jetzt mit dem gekürzten Stand. Erwartung ≈ 9–10 Seiten, damit im Soll; bestätigt zugleich Teil-Check D.
3. Optional, kosmetisch: Anmoderation für `tab:funktionsuebersicht` wieder einsetzen (Hinweis 1), „dabei" in `01_wettbewerbsanalyse.tex:13` streichen (Hinweis 3), UI/UX-Kurzerklärung wieder ergänzen (Hinweis 2) — zusammen etwa 15 Wörter, ohne den Kürzungserfolg zu gefährden.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- [ ] Handlungsempfehlung 1 umsetzen (Einzeiler, `schreib-modus` oder von Hand).
- [ ] Lokalen Build (`latexmk -lualatex main.tex`) fehlerfrei durchlaufen lassen; Log auf undefined references/citations, fehlende Bilder, doppelte Labels prüfen.
- [ ] Textteil-Seitenumfang 7–10 S. am Kompilat bestätigen.
- [ ] LanguageTool-Durchgang (lokal) über den Gesamttext — besonders wichtig nach Runde 4, weil mehrere Sätze verschmolzen und umformuliert wurden (typische Quelle verwaister Satzreste).
- [ ] Eidesstattliche Erklärung elektronisch über myCampus abgeben (Voraussetzung, bevor Turnitin die Einreichung annimmt).
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen; keine externe Plagiatssoftware vorab nutzen.
- [ ] Nutzer-Restpflichten: Namensverfügbarkeit „Resteria" (DPMA / .de-Domain); Nivedhitha/Shen bei Bedarf am Volltext gegenprüfen.
