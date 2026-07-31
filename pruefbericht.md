# Prüfbericht – Projektbericht

**Datum**: 31.07.2026 · **Geprüfter Stand**: Delta `7d5bf56..9231986` (Chefkoch-Faktencheck-Korrekturen, 2 Kapiteldateien) + erstmals lauffähiger Build · **Audit-Typ**: Re-Audit (Delta)
**Score: 100/100 — abgabereif**

> Einordnung vorab: Dieser Lauf schließt zwei Dinge gleichzeitig ab, die in den letzten Berichten getrennt offen standen. Erstens der Textdelta seit `7d5bf56` (letzter PDF-Commit): die Chefkoch-Korrektur aus dem Faktencheck-Bericht (Befund 1, heute vom Nutzer selbst am Primärbeleg bestätigt) in `01_wettbewerbsanalyse.tex` und `01_ausgangslage_und_problem.tex`. Zweitens **Teil-Check D war in dieser Session-Umgebung erstmals lauffähig** — `lualatex`/`latexmk` sind vorhanden, und ein Build ist tatsächlich gelaufen (`git status` zeigt `main.pdf` als lokal verändert, `build/main.log`/`build/main.bbl` frisch von heute). Der seit Wochen dokumentierte Score-Deckel bei 89 entfällt damit: Der Seitenumfang ist jetzt gemessen, nicht geschätzt.

## Was sich seit dem letzten Bericht (89/100, 30.07.) geändert hat

- `chapters/01_einleitung/01_ausgangslage_und_problem.tex:7` — „bieten eine **kostenlose** Resteverwertung aber nicht" / „eine **kostenlose** Suche … nicht vorgesehen" (+2 Wörter). Grund: dieselbe Absolutbehauptung wie in der Wettbewerbsanalyse steckte auch in der zentralen Lücken-Begründung der Einleitung.
- `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex` — vier Stellen in einem Arbeitsgang: `:3` (Chefkoch-Satz: Werkzeug existiert, aber nur im kostenpflichtigen Chefkoch-Plus-Paket), Tabellenzelle Chefkoch/Reste-Matching-Werkzeug (schwach → mittel), `:36` (Lücken-Satz auf die verifizierte Ausnahme Chefkoch umgestellt), `:38` (Alleinstellungsmerkmal: „kostenlosen" ergänzt).
- Beleglage: direkter Primärbeleg des Nutzers (chefkoch.de/wochenplaner/, Zitat „Lebensmittel aufbrauchen mit der Zutatensuche" unter Chefkoch Plus) plus Screenshot der Multi-Select-Zutatenauswahl („+"-Buttons) — stärkere Evidenz als alles, was in dieser Umgebung per Websuche erreichbar war.
- `faktencheck-bericht.md` und `CLAUDE.md` (Statuszeilen `sec:einleitung`, `sec:durchfuehrung`) entsprechend aktualisiert und quittiert.

## Teil-Check D: Build — erstmals lauffähig, sauber

```
Output written on main.pdf (23 pages, 1810502 bytes).
```

- **0** `!`-Fehler, **0** Overfull \hbox, **0** Missing character, keine „undefined references/citations" nach dem letzten Durchlauf.
- Aus `build/main.toc`: „1 Einleitung" auf gedruckter Seite **1**, „Literaturverzeichnis" auf gedruckter Seite **11** → **Textteil = 10 Seiten** (1–10), Vorgabe 7–10 laut `aufgabe.md` → **im Soll, exakt auf der Obergrenze**.
- PDF-Text extrahiert und stichprobenartig gegen die heutigen Änderungen geprüft: „kostenlose Resteverwertung", „kostenpflichtigen Chefkoch-Plus-Paket", „kostenlosen Verbindung" — alle drei finden sich im gebauten PDF. Der Build spiegelt den aktuellen Textstand, kein veralteter Stand.
- **Offen (Nutzer-Schritt):** `main.pdf` im Repository ist lokal verändert, aber noch nicht committet (`git status` → `M main.pdf`). Vor der Abgabe sicherstellen, dass genau diese Fassung eingecheckt ist.

## Teil-Check A/B/C/G — keine neuen Befunde

- `check_all.py --mit-quellen`: alle sechs Skripte ohne harte Funde (0 FEHLER durchgehend).
- `check_formalia.py chapters/ pages/`: 0 FEHLER, 47 Hinweise (bekannte Satzlängen-/Meta-Verb-Artefakte, keine neuen; die beiden heute berührten Dateien tragen je einen neuen SATZLAENGE-Hinweis durch die Wortergänzung, unterhalb der Abzugsschwelle von > 3 Vorkommen je Kapitel).
- `check_bib_hygiene.py`: 10 Einträge, 0 Hinweise.
- `check_status.py`: 0 FEHLER, 15 Hinweise (ausschließlich bekannte `DATEI-OHNE-ZEILE`-Hinweise, projekttypische Konvention).
- `check_quellentreue.py --datei chapters/`: **19/19 FUNDSTELLE OK** — keine der fünf heute geänderten Stellen trägt eine Zitation (alle laufen unter „eigene Sichtung"), keine Invalidierung.
- Konsistenz-Grep über `chapters/`/`pages/` nach „Chefkoch": keine weitere Stelle behauptet noch die widerlegte Absolutaussage; die Fazit-Zeile `01_kernergebnisse_und_ausblick.tex:3“ referenziert die Lücke nur per `\autoref`, keine eigene Wiederholung der Behauptung.
- Ein bekannter Fehlalarm bleibt bestehen, ohne Score-Wirkung: `check_formalia.py` meldet `META-PLATZHALTER` bei `pages/meta.tex` (`\ModuleCode`, `\MatrikelNr`) — beide Felder sind laut vorherigem Audit tatsächlich befüllt, die Heuristik erkennt nur das Muster, nicht den Inhalt.

## Umfang

`check_umfang.py`: **3.710 Wörter**, Ziel 2.625–3.750 — im Soll. Deckt sich mit dem gemessenen Textteil von 10 Seiten (obere Grenze in beiden Maßstäben).

## Bewertungsschwerpunkte (unverändert gegenüber dem letzten Voll-Audit)

- **Transfer (15 %)**: [ABGEDECKT]
- **Kreativität (15 %)**: [ABGEDECKT] – `03_konzept.tex:15` unberührt tragend.
- **Dokumentation (10 %)**: [ABGEDECKT]
- **Ressourcen (10 %)**: [ABGEDECKT]

## Lieferobjekt-Abgleich

- [PASS] Alle sechs Lieferobjekte unverändert vorhanden. Der Delta berührt keine Abbildung/Tabelle inhaltlich, nur eine Tabellenzelle (Reste-Matching-Werkzeug: schwach → mittel) und vier Fließtextsätze.

## Bitte manuell prüfen (kann ich nicht selbst verifizieren)

1. **Wortlaut der vier zitierten Claude-Design-Prompts** | `pages/appendix.tex`, die vier `\quelle{}`-Zeilen | Stimmt, wenn der zitierte Text wortgleich der Eingabe im Claude-Design-Chat entspricht | Der Chatverlauf liegt außerhalb des Repositorys (unverändert offen aus dem letzten Bericht).

## Handlungsempfehlungen (nach Priorität)

1. **Kein Text-Handlungsbedarf.** Alle Befunde früherer Berichte sind abgearbeitet, der Faktencheck-Bericht ist vollständig erledigt, der Build ist sauber und im Soll.
2. **`main.pdf` committen** — es liegt bereits lokal aktuell vor (siehe Teil-Check D), muss nur noch eingecheckt werden.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)

- [ ] **`main.pdf` committen** (liegt bereits aktuell und sauber gebaut vor, siehe oben).
- [ ] **Eidesstattliche Erklärung** elektronisch über myCampus abgeben – vorher nimmt Turnitin die Einreichung nicht an.
- [ ] Einreichungs-Anleitung im myCampus-Kurs lesen.
- [ ] **LanguageTool-Durchgang** lokal über den Gesamttext (3.710 Wörter).
- [ ] Arbeit einmal am PDF am Stück durchlesen.
- [ ] **Keine externe Plagiatssoftware vorab** – ein Voraberprüfungs-Upload erzeugt einen Turnitin-Selbsttreffer.
- [ ] Manueller Prüfpunkt oben: die vier zitierten Prompts gegen den Chatverlauf abgleichen.
- [ ] Namensverfügbarkeit „Resteria" (DPMA, .de-Domain) – nicht abgabekritisch.

---

## Prüfstand (mechanische Skripte)

- `check_bib_keys.py`: alle genutzten Keys valide, 0 FEHLER.
- `check_formalia.py chapters/ pages/`: 0 FEHLER, 47 Hinweise.
- `check_umfang.py`: 3.710 Wörter, Ziel 2.625–3.750 Wörter.
- `check_bib_hygiene.py`: 10 Einträge, 0 Hinweise.
- `check_status.py`: 0 FEHLER, 15 Hinweise (bekannte `DATEI-OHNE-ZEILE`-Konvention).
- `check_quellentreue.py`: 19 Zitationen, 19 FUNDSTELLE OK, 0 offen.
- **Build**: `latexmk -g -lualatex main.tex` (in dieser Session-Umgebung direkt verfügbar) → 23 PDF-Seiten, Textteil 10 Seiten, 0 Fehler, 0 Overfull, 0 Missing character.
