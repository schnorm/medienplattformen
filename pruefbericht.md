# Prüfbericht – Projektbericht

**Datum**: 30.07.2026 · **Geprüfter Stand**: Delta `1b8660f..3848ace` (PR #17, 2 Kapiteldateien + `pages/appendix.tex`) · **Audit-Typ**: Re-Audit (Delta)
**Score: 89/100 (vorläufig – Teil-Check D nicht lauffähig, Seitenumfang für den aktuellen Textstand ungeprüft)**

> Einordnung vorab: Geprüft wurden die beiden im letzten Bericht offenen Ein-Wort-Befunde (2, 3) und die vom Nutzer angestoßene Streichung des Chefkoch-Vergleichssatzes — alle drei sind jetzt am Text verifiziert umgesetzt. **Kein neuer score-relevanter Befund.** Der Abzug hat dieselbe einzige Ursache wie im Vorbericht: `lualatex`/`latexmk`/`biber` sind in dieser Session-Umgebung weiterhin nicht installiert, und das eingecheckte `main.pdf` ist **weiterhin veralteter Stand** — jetzt sogar um zwei Pull Requests (#16 und #17) veraltet, nicht mehr nur um einen.

## Was sich seit dem letzten Bericht geändert hat

- `04_community_und_feedback.tex:9` — „vor allem" gestrichen (Befund 3 des Vorberichts).
- `pages/appendix.tex:53` — „}, sowie in weiteren" → „}, in weiteren" (Befund 2 des Vorberichts); alle vier `\quelle{}`-Zeilen wieder formgleich.
- `04_community_und_feedback.tex:9` — der Chefkoch-Vergleichssatz („Hinzu kommt, …") entfällt (Nutzer-Anstoß, nicht aus dem Vorbericht). Vorab gegen vier Beschädigungskriterien geprüft (verwaistes Label, betroffene Zitation, Zählaussage, Prüfer-Steuerung) — alle vier negativ, siehe Commit `fd4c690`.
- `SKILL-ANPASSUNGEN.md` — neuer Punkt P35 (Skill-Prozessdatei, kein Bestandteil der Arbeit selbst, nicht Gegenstand dieses Audits).

## Befunde

### 1 — `main.pdf` im Repository ist weiterhin nicht der Build des aktuellen Textes (kein Score-Abzug, aber abgabeblockierend)

Der letzte Commit, der `main.pdf` verändert hat, ist `7d5bf56`. Per Ancestry-Prüfung bestätigt: `7d5bf56` liegt **vor** `78d0587` (Neufassung der Gruppen/Foren-Begründung, PR #16) **und vor** `fd4c690` (Chefkoch-Streichung + Befund 2/3, PR #17):

```
git merge-base --is-ancestor 7d5bf56 78d0587  → ja
git merge-base --is-ancestor 7d5bf56 fd4c690  → ja
```

Das eingecheckte PDF trägt also weder die aktuelle Gruppen/Foren-Begründung noch die drei jüngsten Korrekturen. Wer dieses PDF einreicht, reicht einen zweifach überholten Textstand ein. **Vor der Abgabe zwingend neu bauen und das PDF ersetzen** — unverändert der einzige Punkt, der den Score bewegt.

### 2 und 3 des Vorberichts — behoben, am Text verifiziert

- `pages/appendix.tex`: alle vier `\quelle{}`-Zeilen enden jetzt identisch auf „…, in weiteren Iterationsschritten verfeinert, durch Anthropic, 2026 …" (per Grep gegengeprüft, 4/4 Treffer).
- `04_community_und_feedback.tex:9`: „Laut~\autoref{sec:zielgruppe} sucht die Zielgruppe einen Ort, an dem der eigene Erfolg von anderen gesehen wird." — keine Rangfolge mehr behauptet, die `sec:zielgruppe` nicht stützt.

### 4 des Vorberichts — bewusst nicht umgesetzt (kein Abzug)

`META-VERB` „bündeln" (`04_community_und_feedback.tex:9`, „Die Challenges bündeln die Beteiligung …") steht unverändert. Einzelvorkommen, Abzug greift laut Score-Regel erst ab mehr als drei je Kapitel; keine Handlungspflicht.

### 5 — Chefkoch-Vergleichssatz gestrichen: Nachprüfung ohne neuen Fund

Der Absatz `04_community_und_feedback.tex:9` liest sich nach der Streichung durchgehend: Aufgabenstellung nennt Gruppen/Foren als mögliche Funktion → Grund 1 (Rettungs-Feed deckt die Sichtbarkeits-Anforderung aus `sec:zielgruppe`) → „zudem" leitet zu Grund 2 (Verdünnungsrisiko bei geteilter Zielgruppe) über. Eigene Nachprüfung bestätigt die vier bereits im Commit dokumentierten Punkte:

- `\autoref{sec:wettbewerbsanalyse}` bleibt an drei weiteren Stellen referenziert (`03_konzept.tex:7`, `:24`, `01_kernergebnisse_und_ausblick.tex:3`) — kein verwaistes Label.
- Grep über `chapters/` auf „drei Gründe/erstens/zweitens/drittens" im Umfeld des Kapitels: kein Treffer, der eine Dreizahl verspricht.
- `check_quellentreue.py`: weiterhin 19/19 FUNDSTELLE OK, kein Trägersatz-Hash der Datei bewegt.

Kein neuer Befund.

### 6 — Falscher Positiv-Fund im Skript-Lauf: `META-PLATZHALTER` bei `pages/meta.tex` (kein Fund)

`check_formalia.py` meldet `\ModuleCode`, `\MatrikelNr` als „noch nicht ausgefüllt". Am Volltext geprüft: Beide Felder tragen echte Werte (`\ModuleCode{DLBMIMPFS01-01}`, `\MatrikelNr{3210267}`) — die Heuristik prüft nur, ob der Wert komplett aus Großbuchstaben/Ziffern besteht, und ein echter Modulcode bzw. eine Matrikelnummer erfüllen dieses Muster zufällig genauso wie ein Platzhalter. **Kein Handlungsbedarf.**

## Teil-Check A – Formalia

- [PASS] Zitationen – `check_bib_keys.py`: alle 9 genutzten Keys existieren, 0 FEHLER.
- [PASS] LaTeX-Format – `check_formalia.py` über `chapters/` + `pages/`: **0 FEHLER**, 47 Hinweise (unverändert gegenüber dem Vorbericht, keine neue Klasse).
- [PASS] Eigene Werke – alle vier Mockup-Quellenzeilen tragen Prompt, Unternehmen, Jahr, Modell, Bearbeitungshinweis; jetzt zusätzlich untereinander formgleich (Befund 2 behoben).
- [PASS] Cross-References & Labels – `sec:zielgruppe`, `sec:wettbewerbsanalyse` weiterhin gültig und mehrfach referenziert.
- [PASS] Pronomen · Akronyme · Anti-KI-Stil · Verständlichkeit – keine neuen Funde.
- [PASS] Offene Arbeitsmarker – kein `% TODO-QUELLE:`, kein `% UNVERIFIED:`.
- [Kein Fund] `META-PLATZHALTER` bei `pages/meta.tex` — Heuristik-Fehlalarm, siehe Befund 6.

## Teil-Check B – Argumentationsqualität

- [PASS] These und Kernargumente im Delta unberührt.
- [PASS] Abhakliste „Gruppen/Foren" weiterhin „ausdrücklich beantwortet" (unverändert seit PR #16).
- [PASS] Prüfer-Steuerung „Entscheidungen beruhen auf der Vergleichsanalyse" bleibt erfüllt — `04_community_und_feedback.tex:3` verankert das Kapitel weiterhin an der Wettbewerbsanalyse, unabhängig vom gestrichenen Chefkoch-Satz.
- [PASS] Limitationen weiterhin dreischichtig (im Delta unberührt).

## Teil-Check C – Struktur

- [PASS] Querverweise semantisch korrekt (siehe Befund 5).
- [PASS] Keine Doppelbegründung / Redundanz durch die Streichung — im Gegenteil: eine Halb-Redundanz zum verbleibenden Satz „Jeder weitere Bereich müsste zudem gefüllt werden" ist entfallen.
- [PASS] Zählaussagen weiterhin stimmig (`06_evaluation_reflexion.tex:5` „Zwei Stellen" unberührt).
- [PASS] ½-Seiten-Regel — keine Datei unter die Schwelle gerutscht.

## Teil-Check D – Build

- [ÜBERSPRUNGEN] Kompiliert fehlerfrei – `lualatex`/`latexmk`/`biber`/`pdflatex`/`tectonic` explizit geprüft: **keines in dieser Session-Umgebung installiert.**
- [ÜBERSPRUNGEN] Undefined references/citations – nicht messbar; statisch keine neuen Labels oder Zitationen im Delta.
- [ÜBERSPRUNGEN] **Seitenumfang Textteil – für den aktuellen Text weiterhin ungemessen.** `check_umfang.py`: **3.691 Wörter ≈ 9,8 Seiten** gegen die Vorgabe 7–10 (unverändert zum Vorbericht, das Delta ist netto ±0 Wörter — die Streichung des Chefkoch-Satzes und die zwei Ein-Wort-Fixes gleichen sich mit vorherigen +30 Wörtern der Chefkoch-Streichung selbst nahezu aus; siehe „Prüfstand" unten). Die Heuristik kennt Tabellen/Floats nicht (beobachtete Abweichung bis zu +1,5 Seiten) — das Kriterium bleibt ungeprüft, Score-Deckel bei 89 greift unverändert.

## Teil-Check E – Abgabe (informativ, kein Score-Abzug)

- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen
- [OFFEN] Umfang im Soll – Spiegel aus Teil-Check D, für den aktuellen Stand ungemessen
- [ERINNERT] Keine externe Plagiatssoftware vorab nutzen
- [OFFEN] LanguageTool-Durchgang lokal über den Gesamttext

## Teil-Check F – Literaturverzeichnis

- [PASS] `check_bib_hygiene.py`: 10 Einträge, **0 Hinweise**. Im Delta unberührt.

## Teil-Check G – Quellentreue (Volltextabgleich)

- [PASS] **19 Zitationen geprüft · FUNDSTELLE OK 19 · offen 0** (Details: `quellencheck.md`).
- Kein WORTLAUT, kein ZITAT WEICHT AB, kein SEITE VERDÄCHTIG, kein SEITE AUSSERHALB, kein CLAIM SCHÄRFER, kein NICHT PRÜFBAR, kein RENTIERT NICHT.
- Der Chefkoch-Satz trug keine eigene Zitation; die Streichung hat keinen Trägersatz-Hash bewegt (verifiziert per erneutem Lauf nach dem Commit).
- Notiz-Wächter: kein `[NOTIZ-DUBLETTE]`, kein `[NOTIZ-FREMDER-AUTOR]`.
- Volltexte ohne Bib-Verweis (3): Krug- und Norman-EPUBs aus der Vorarbeit sowie die Vittuari-Preprint-Fassung neben der zitierten Verlagsfassung — unschädlich, unverändert.

## Teil-Check H – Lesefluss

- [PASS] Datei vollständig gelesen (siehe „Was sich geändert hat"). Anschlüsse lösen auf: „Beides" → „Gruppen und Foren", „Genau das" → Sichtbarkeits-Anforderung, „Jeder weitere Bereich" → relativ zum Feed, „zudem" bezieht sich nach der Streichung jetzt korrekt auf einen vorangegangenen Grund statt zwei. Kein hängender Bezug, kein abgeschnittener Absatzöffner.

## Claims

- Ungesicherte FACTUAL CLAIMS: keine.
- Fehlende OWN WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: `pexelsHasanbekavaBasket` — kein echter Fund, wird über `\citeauthor`/`\citeyear` genutzt. Nicht entfernen.

## Punkteabzug im Detail

- Seitenumfang / Teil-Check D nicht lauffähig: **Score-Deckel bei 89** statt Einzelabzug. Kein Textbefund.
- Sonst: **keiner.**

## Bewertungsschwerpunkte (Projektbericht)

- **Qualität (25 %)**: [ABGEDECKT]
- **Prozess (25 %)**: [ABGEDECKT] – Kursänderung weiterhin als eine von zwei Stellen in `06_evaluation_reflexion.tex:5` geführt.
- **Transfer (15 %)**: [ABGEDECKT]
- **Kreativität (15 %)**: [ABGEDECKT] – `03_konzept.tex:15` unberührt tragend.
- **Dokumentation (10 %)**: [ABGEDECKT]
- **Ressourcen (10 %)**: [ABGEDECKT]

## Lieferobjekt-Abgleich

- [PASS] Alle sechs Lieferobjekte unverändert vorhanden. Der Delta berührt keine Abbildung/Tabelle inhaltlich, nur eine Quellenzeilen-Formulierung und einen Fließtextsatz.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

1. **Seitenzahl des Textteils nach dem Neubau** | `latexmk -g -lualatex main.tex`, dann im PDF „1 Einleitung" und den Beginn des Literaturverzeichnisses suchen | Stimmt, wenn zwischen beiden höchstens 10 gedruckte Seiten liegen | `lualatex`/`latexmk`/`biber` sind in dieser Session-Umgebung nicht installiert.
2. **Wortlaut der vier zitierten Claude-Design-Prompts** | `pages/appendix.tex`, die vier `\quelle{}`-Zeilen | Stimmt, wenn der zitierte Text wortgleich der Eingabe im Claude-Design-Chat entspricht | Der Chatverlauf liegt außerhalb des Repositorys (unverändert offen aus dem Vorbericht).

## Handlungsempfehlungen (nach Priorität)

1. **Neu bauen und das eingecheckte `main.pdf` ersetzen.** `latexmk -g -lualatex main.tex`. Einziger Punkt mit Score-Wirkung: Ergibt der Textteil 10 Seiten oder weniger, steht der Bericht bei **100/100**. Ohne Neubau bleibt das PDF zweifach veraltet (Befund 1).
2. Kein weiterer Text-Handlungsbedarf. Optional: „bündeln" (Befund 4) ersetzen — ohne Score-Wirkung.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

- [ ] **Neu bauen** und das eingecheckte `main.pdf` ersetzen — die abgegebene Fassung darf nicht der alte Stand sein.
- [ ] **Eidesstattliche Erklärung** elektronisch über myCampus abgeben – vorher nimmt Turnitin die Einreichung nicht an.
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen.
- [ ] **LanguageTool-Durchgang** lokal über den Gesamttext (3.691 Wörter).
- [ ] Arbeit einmal am PDF am Stück durchlesen.
- [ ] **Keine externe Plagiatssoftware vorab** – ein Voraberprüfungs-Upload erzeugt einen Turnitin-Selbsttreffer.
- [ ] Manueller Prüfpunkt 2 oben: die vier zitierten Prompts gegen den Chatverlauf abgleichen.
- [ ] Namensverfügbarkeit „Resteria" (DPMA, .de-Domain) – nicht abgabekritisch.

---

## Prüfstand (mechanische Skripte)

- `check_bib_keys.py`: 9/9 Keys valide, 0 FEHLER.
- `check_formalia.py chapters/ pages/`: 0 FEHLER, 47 Hinweise (unverändert).
- `check_umfang.py`: 3.691 Wörter, Ziel 2.625–3.750 Wörter, ≈ 9,8 Seiten geschätzt.
- `check_bib_hygiene.py`: 10 Einträge, 0 Hinweise.
- `check_status.py`: 0 FEHLER, 15 Hinweise (ausschließlich bekannte `DATEI-OHNE-ZEILE`-Hinweise, projekttypische Konvention — jede Kapiteldatei hat ihre eigene Zeile in der übergeordneten `sec:`-Statuszeile in `CLAUDE.md`, nicht in einer Datei-zu-Datei-Abbildung).
- `check_quellentreue.py`: 19 Zitationen, 19 FUNDSTELLE OK, 0 offen.
