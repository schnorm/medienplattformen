# Prüfbericht — Projektbericht

**Datum**: 23.07.2026 · **Geprüfter Stand**: alle Kapitel (Einleitung, Durchführung, Fazit) nach Abarbeitung Gegenlesung Runde 1+3 und Gesamt-Stresstest Runde 2 · **Audit-Typ**: Voll-Audit
**Score: 100/100 — abgabereif** (Teil-Check D Build lokal zu bestätigen, siehe unten)

Vorbedingung erfüllt: Gegenlesung (Runde 1, Runde 3) und Gesamt-Stresstest (Runde 2) sind gelaufen, `AENDERUNGEN.md` → „Offen" ist leer. Prüfer-Anmerkungen (`sources/Anmerkungen vom Prüfer.md`) wurden als zusätzlicher Prüfmaßstab herangezogen (Abgleich am Ende).

`PERSISTENT.md`/`MEMORY.md` gelesen — keine abweichenden Audit-Kriterien; Teil-Check E bleibt score-neutral (MEMORY-Festlegung 2026-07-19).

## Teil-Check A — Formalia
- [PASS] Zitationen — `check_bib_keys.py`: alle 6 Keys valide, keine erfundenen, keine ungenutzten. Stellenbezogene Zitate mit `\parencite[S. X]{}` (vittuari S. 1/106, barker S. 10, soma S. 9); werkbezogene Paraphrasen ohne Seite (un = SDG-Gesamtdokument, shen, nivedhitha) korrekt.
- [PASS] Eigene Werke — `\quelle{Eigene Darstellung.}` auf allen 5 eigenen Abb./Tab. KI-Mockups mit Pflichtmuster „Erstellt mit dem Prompt „…" durch Claude Design (Claude Sonnet 5), Abbildung nachträglich manuell bearbeitet."
- [PASS] Pronomen — `check_formalia.py` 0 FEHLER; dritte Person streng („Die Projektgruppe …").
- [PASS] LaTeX-Format — 0 FEHLER; Caption vor `\label`, Floats `[H]`, `~\autoref`, `\enquote{}` durchgehend.
- [PASS] Akronyme — `\ac{MVP}` verwendet, in `pages/acronyms.tex` definiert. UI/UX bei Erstnennung ausgeschrieben und kurz erklärt (nicht als `\ac{}` geführt — geläufig, kein Verstoß).
- [PASS] Cross-References & Labels — `sec:`/`fig:`/`tab:` konsistent; alle `\autoref`-Ziele definiert.
- [PASS] Anti-KI-Stil — kein GEDANKENSTRICH-Treffer; 3× TRIAS nur in `05_phasenplanung.tex` (sachlich, echte Phasen-/Ressourcenaufzählungen), unter dem Häufungs-Deckel.
- [PASS] Verständlichkeit — SATZSCHNITT-Hinweise (community ~23, phasenplanung ~26) durch Tabelleninhalt verzerrt; Fließtext liest klar, ein Gedanke pro Satz. Nicht gehäuft.

## Teil-Check B — Argumentationsqualität (nur Pflicht-Punkte der Typ-Datei als FAIL)
- [PASS] These erkennbar — Leitfrage/Ziel (Konzeption Resteria) und These (Kombination Reste-Matching + echte Social-Community ist die Marktlücke) getrennt.
- [N.A.] Forschungslücke in Einleitung — laut `projektbericht.md` nur „Optional".
- [PASS] Aktualität/Zeitbezug in Einleitung — Pflicht: SDG 12.3, private Haushaltsverschwendung, aktuelle Plattformlandschaft als projektbezogener Anlass.
- [PASS] Gegenargumente reflektiert & entkräftet — vier Einwände gegen die USP explizit erhoben und einzeln entkräftet (`01_wettbewerbsanalyse.tex:34`).
- [PASS] Syntheseleistung pro Hauptkapitel — Durchführung verknüpft Wettbewerbsanalyse + Verhaltensliteratur + eigenes Konzept; Evaluation reflektiert Zielerreichung.
- [PASS] Limitationen dreischichtig — drei Grenzen (Nutzertest, KI-Mockup, Marktabdeckung) je mit warum · Mitigation · zukünftigem Schritt.
- [N.A.] Ergebnisse ≠ Interpretation — nur empirische Seminararbeit.
- [PASS] Typspezifisch (Projektbericht) — Phasenplanung als Tabelle vorhanden; „Quelle: Eigene Darstellung." auf jeder eigenen Abb./Tab.; Produkt sichtbar dokumentiert (Funktionslogik + 4 Mockups); dritte Person streng.
- [PASS] Leitfragen aus `aufgabe.md` beantwortet — alle drei Teilaufgaben real ausgeführt (`06_evaluation_reflexion.tex:3` prüft explizit); Feedback-Schleifen als geplantes Vorgehen (von `aufgabe.md` gedeckt); Abhakliste vollständig, Event-Kalender und Gruppen/Foren je begründet ausgeschlossen.
- [PASS] Dimensionsabgleich — jede Bewertungsdimension im Text vertreten (auch Transfer/wirtschaftlich: Freemium + Kooperationen).

## Teil-Check C — Struktur
- [PASS] ½-Seiten-Regel — `03_vorgehen_und_aufbau.tex` mit ~143 Wörtern grenzwertig (Skript-HINWEIS, kein FEHLER), enthält aber zwei vollständige Absätze (Methodik + Aufbau). Kein Stub → kein Verstoß; optional 1–2 Sätze ergänzbar.
- [PASS] Max. 3 Kapitelstufen — Body nutzt section > subsection (2 Ebenen).
- [PASS] Front-/Backmatter — Titelblatt, Inhaltsverzeichnis, Abbildungsverzeichnis (5 Abb. ≥ 3), Tabellenverzeichnis (4 Tab. ≥ 3), Abkürzungsverzeichnis, Literaturverzeichnis, Anhang A/B gekennzeichnet + Anhangsverzeichnis; je ≥ 1 Textverweis pro Anhang.
- [PASS] Outline-Check — Einleitung (10–15 %) → Durchführung inkl. Evaluation/Reflexion als Subsection (70–80 %) → Fazit (10–15 %) entspricht dem Kapitelgerüst aus `projektbericht.md`.

**Roter Faden (kapitelübergreifend, Gesamt-Stresstest Runde 2 als Vorlauf referenziert, nur Regressions-Stichprobe):**
- [PASS] Querverweise semantisch korrekt (`\autoref{sec:wettbewerbsanalyse}` aus Konzept/Fazit zeigt auf die Analyse; Persona-/Mockup-Verweise treffen Anhang A/B).
- [PASS] Zählangaben gegen eigene Tabellen nachgezählt: „vier Einwände" = 4 gelistet · „fünf Kriterien" = 5 Matrixspalten · „sechs Plattformen" = 6 Zeilen · „sechs Vertreter aus drei Kategorien, ein bis drei Vertreter" = 2+3+1 stimmig · Zeitpuffer (Text „innerhalb der MVP-Phase, zwei Wochen" ↔ Tabelle MVP Woche 8–17 „inkl. zweiwöchigem Zeitpuffer", Beta 18–20) konsistent.
- [PASS] Tabellenwertungen spaltenweise mit Kriteriendefinition vereinbar: Community-Spalte (Chefkoch stark, TikTok stark, Foodsharing stark, leftovercooking mittel) jeweils im Fließtext begründet; leftovercookings Belohnungspunkte ausdrücklich als individuelles Spar-Feedback vom sozial-interaktiven Gamification-Begriff abgegrenzt.
- [PASS] Resteria erhält keine Bestwerte-Zeile (bewusst aus der Vergleichstabelle entfernt — kein Zirkelschluss-Anschein).
- [PASS] Selbst erhobener Einwand (SDG-12.3-Breitenanspruch vs. Zielgruppen-Verengung) in `06_evaluation_reflexion.tex` benannt UND aufgelöst; Reichweitenrisiko des Feeds explizit genannt.

## Teil-Check D — Build
- [ÜBERSPRUNGEN] Kompiliert fehlerfrei — lualatex/biber/latexmk in dieser Umgebung nicht verfügbar. Statisch geprüft: keine doppelten Labels, `main.tex` bindet `pages/appendix` (Z. 339), `\listoffigures` (Z. 291) und `\listoftables` (Z. 298) ein.
- [ÜBERSPRUNGEN → statisch PASS] Keine undefined references/citations, fehlenden Bilder — alle `\autoref`-Ziele definiert (inkl. der 5 Anhang-Ziele), alle 4 Mockup-PNG unter `images/durchfuehrung/` vorhanden, alle 6 Citations valide.
- [ÜBERSPRUNGEN] Seitenumfang Textteil (Soll 7–10 S.) — ohne Kompilat nicht messbar; lokal prüfen.

## Teil-Check E — Abgabe (informativ, kein Score-Abzug)
- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben — Status laut `CLAUDE.md` → Fristen: [offen].
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen.
- [OFFEN → lokal] Umfang im Soll — Spiegel aus Teil-Check D, ohne Build nicht bestätigt.
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko).

## Claims
- Ungesicherte FACTUAL CLAIMS: keine. Marktbehauptung „wachsender Markt" (Transfer) wurde in Runde 3 zu einer nicht belegbedürftigen Annahme abgeschwächt; Verbraucherzentrale-Verweis entfernt.
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: keine (`check_bib_keys.py --report-unused`).
- Offene `% UNVERIFIED:`-Marker: keine im Text.

## Punkteabzug im Detail
- Keine Abzüge. BBT-Keys 0 · Pflicht-Punkte Typ-Datei 0 · Formalia 0 · Struktur 0 · Anti-KI/Verständlichkeit unter Häufungsschwelle.
- Teil-Check D (Build/Seitenumfang) nicht bewertet (ÜBERSPRUNGEN — keine spekulativen Abzüge), sondern in „Vor der Einreichung" ausgelagert.

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: [ABGEDECKT] Alle drei Teilaufgaben real ausgeführt, Matrix nach Runde 3 kalibriert (Chefkoch/leftovercooking-Wertungen im Text begründet), Zählfehler behoben.
- **Prozess (25 %)**: [ABGEDECKT] Vorgehen dokumentiert, reflektiert (Lessons Learned), Grenzen dreischichtig.
- **Transfer (15 %)**: gesellschaftlich [ABGEDECKT] (SDG 12.3) · wirtschaftlich [ABGEDECKT] (Freemium, Kooperationen; Marktaussage als Annahme entschärft) · Ansätze/Modelle begründen [ABGEDECKT] (Drivers/Levers, Nudges, Gamification).
- **Kreativität (15 %)**: [ABGEDECKT] Vergleich zu 6 Plattformen; USP ehrlich als Kombination gerahmt, nicht als bewiesener Marktvorteil.
- **Dokumentation (10 %)**: [ABGEDECKT] Entstehungsgeschichte lückenlos; „eigene Sichtung (Stand Juli 2026)" als Erhebungsgrundlage deklariert.
- **Ressourcen (10 %)**: [ABGEDECKT] Phasenplanung mit Zeitrahmen, Ressourcen-Spalte, Zeitpuffer, Abhängigkeiten/Risiken.

## Lieferobjekt-Abgleich
- [PASS] Alle 6 Lieferobjekte real vorhanden: Wettbewerbsvergleich (`tab:wettbewerbsvergleich`), Persona (`tab:persona`), UI/UX-Mockup (4 PNG), Plattformname (Resteria), Funktionsübersicht (`tab:funktionsuebersicht`), Phasenplanung (`tab:phasenplanung`). `pages/appendix.tex` mit echtem Inhalt; visuelle Konzeptdarstellung (Funktionslogik + Mockups) vorhanden; kein behauptetes, aber fehlendes Artefakt.

## Prüfer-Anmerkungen-Abgleich (`sources/Anmerkungen vom Prüfer.md`)
- [ERFÜLLT] Eigenständigkeit/Kreativität in Auswahl & Argumentation — selektive, begründete Plattform- und Funktionsauswahl.
- [ERFÜLLT] 7–10-Seiten-Projektvorschlag mit bewusster Schwerpunktsetzung — Visuals + Persona in den Anhang ausgelagert (Seitenbudget geschont).
- [ERFÜLLT] Vergleichsanalyse mit SWOT-Charakter, auf der die weiteren Entscheidungen beruhen — SWOT-Einordnung Resterias (Stärke/Schwäche/Chancen/Risiko) in `01_wettbewerbsanalyse.tex:32`; Konzept leitet sich explizit aus der Marktlücke ab.
- [ERFÜLLT] Zielgruppe ohne Primärdaten, argumentativ begründet.
- [ERFÜLLT] KI-Mockup zulässig, transparent gekennzeichnet + manuelle Weiterbearbeitung angegeben — Pflichtmuster im Anhang B erfüllt genau die Prüfer-Vorgabe.
- [ERFÜLLT] Literatur zur Objektivierung der Vorschläge (nicht zur UX-Definition) — 6 Quellen belegen Verhaltens-Hebel, UX selbst wird nicht mit Quellen „erklärt".

## Handlungsempfehlungen (nach Priorität)
1. **Lokalen Build fahren** (`latexmk -lualatex main.tex`) und Log auf `undefined`/`multiply defined`/`not found` prüfen — der einzige Punkt, der maschinell hier nicht abschließbar war. Erwartung nach statischer Prüfung: sauber.
2. **Seitenumfang des Textteils** (ab „1 Einleitung" bis vor Literaturverzeichnis, inkl. Abb./Tab. im Text) gegen 7–10 Seiten halten. Anhang, Verzeichnisse, Literatur zählen nicht.
3. Optional: `03_vorgehen_und_aufbau.tex` um 1–2 Sätze verlängern (grenzwertige ½-Seite) — kosmetisch.
4. Optional: eine der Einstiegsquellen (Kapoor et al. / Hansch & Rentschler) einbauen, falls sich beim Feinschliff eine natürliche Stelle ergibt — laut `aufgabe.md` nicht Pflicht.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- [ ] Lokalen Build (`latexmk -lualatex main.tex`) fehlerfrei durchlaufen lassen; Log auf undefined references/citations, fehlende Bilder, doppelte Labels prüfen.
- [ ] Textteil-Seitenumfang 7–10 S. bestätigen.
- [ ] LanguageTool-Durchgang (lokal) über den Gesamttext (Sprache zählt in die Bewertung; das Voll-Audit ersetzt keine Vollprüfung).
- [ ] Eidesstattliche Erklärung elektronisch über myCampus abgeben (Voraussetzung, bevor Turnitin die Einreichung annimmt).
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen; keine externe Plagiatssoftware vorab nutzen (Turnitin-Selbsttreffer-Risiko).
- [ ] Nutzer-Restpflichten: Namensverfügbarkeit „Resteria" (DPMA / .de-Domain); Nivedhitha/Shen bei Bedarf am Volltext gegenprüfen.
