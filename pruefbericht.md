# Prüfbericht — Projektbericht

**Datum**: 23.07.2026 · **Geprüfter Stand**: alle Kapitel (Einleitung, Durchführung, Fazit) + Anhang · **Audit-Typ**: Re-Audit (Delta)
**Score: 100/100 — abgabereif** (die beiden einzigen Abzüge des Voll-Audits vom selben Tag — beide aus der `main.tex`-Verdrahtung — sind behoben; Textteil und Formalia waren bereits auditsauber)

**Delta-Grundlage**: Voll-Audit vom 23.07.2026 (Score 75/100). Ein Re-Audit prüft nur die FAIL-Punkte des Vorberichts gezielt nach, dazu beide Skripte und Teil-Check D, statt alle Kapitel erneut zu lesen. `PERSISTENT.md`/`MEMORY.md` gelesen — keine abweichenden Audit-Kriterien außer: Teil-Check E ist nie score-relevant (MEMORY 2026-07-19), berücksichtigt.

---

## Nachprüfung der beiden Vorbericht-FAILs

### FAIL 1 (Voll-Audit Teil-Check D, −15) — Anhang nicht eingebunden → 5 undefined references + fehlendes Lieferobjekt → **BEHOBEN**
- `main.tex:338–339`: `\appendix` und `\include{pages/appendix}` sind jetzt **einkommentiert** (Nutzer-Aktion mit einmaliger expliziter Freigabe, `main.tex` zu ändern — im Projektstatus dokumentiert).
- Alle fünf zuvor undefinierten Labels existieren real in `pages/appendix.tex` und werden durch die Einbindung aufgelöst: `tab:persona` (Z. 11), `fig:mockup_start` (Z. 31), `fig:mockup_start_bookmarks` (Z. 38), `fig:mockup_profil` (Z. 45), `fig:mockup_feed` (Z. 52).
- Die vier UI/UX-Mockups liegen als echte Bilddateien vor (`images/durchfuehrung/resteria_{startseite,startseite_bookmarks,profil,rettungsfeed}.png`) und sind per `\includegraphics` (appendix.tex Z. 33/40/47/54) eingebunden. Das geforderte Lieferobjekt erscheint damit im kompilierten Dokument.
- Statisch bestimmt: Root Cause (Anhang nicht eingebunden) entfällt, alle Ziel-Labels vorhanden, alle Bilddateien vorhanden → die fünf undefined references sind aufgelöst. Deckel −15 vollständig zurückgenommen.

### FAIL 2 (Voll-Audit Teil-Check C, −10) — Abbildungs-/Tabellenverzeichnis nicht eingebunden trotz ≥ 3 → **BEHOBEN**
- `main.tex:288–291`: `\listoffigures` inkl. `\blankpage`/`\phantomsection`/`\addcontentsline` **einkommentiert** (5 Abbildungen).
- `main.tex:295–298`: `\listoftables` analog **einkommentiert** (4 Tabellen).
- IU-Schwelle „ab 3" erfüllt; Abzug −10 zurückgenommen.

---

## Skript-Nachlauf (Regressions-Absicherung)
- `check_bib_keys.py references.bib --dir chapters/ --report-unused`: **OK (6 Keys)**, alle existieren, **keine ungenutzten Einträge**. Keine Regression.
- `check_formalia.py chapters/`: **0 FEHLER**, 11 HINWEISE (½-Seiten 03_vorgehen ~143 W.; mehrere SATZLAENGE-Treffer — davon `01_wettbewerbsanalyse`, `03_konzept`, `05_phasenplanung` teils Tabelleninhalt, bekannte False-Positive-Quelle; SATZSCHNITT 04_community/05_phasenplanung; TRIAS 05_phasenplanung). Identisches Profil wie im Voll-Audit, keine Häufung > 3 echter Verstöße in einem Kapitel → **kein Score-Abzug, keine Regression.**

## Zusätzlich erledigte Empfehlungen des Vorberichts (nicht score-relevant, aber Unschärfen beseitigt)
- Handlungsempfehlung 3: `chapters/03_fazit/02_limitationen.tex:7` nennt jetzt „**drei Plattform-Kategorien**" (zuvor „vier") — konsistent mit der Zählung in der Wettbewerbsanalyse.
- Handlungsempfehlung 4: `chapters/02_durchfuehrung/05_phasenplanung.tex:23` formuliert den Zeitpuffer jetzt „**innerhalb der \ac{MVP}-Phase**" — deckungsgleich mit `tab:phasenplanung`.
- Handlungsempfehlung 5 (UI/UX-`\ac{}`-Vereinheitlichung) bewusst ausgelassen — rein optional, keine Regelverletzung.

---

## Teil-Check D — Build
- [ÜBERSPRUNGEN] Kompiliert fehlerfrei — `lualatex`/`latexmk`/`biber` in dieser Umgebung weiterhin nicht verfügbar. **Lokaler Build durch den Nutzer nötig.**
- [PASS — statisch bestimmt] Keine undefined references/citations — Root Cause behoben (Anhang eingebunden, alle 5 Ziel-Labels + 4 Bilddateien vorhanden). Doppelte Labels: keine (Skript meldet keine, Grep bestätigt eindeutige Labels).
- [ÜBERSPRUNGEN] Seitenumfang — ohne Build nicht messbar; Nutzer prüft Textteil (7–10 S. B.Sc.) lokal.

## Teil-Check E — Abgabe (informativ, kein Score-Abzug)
- [OFFEN] Eidesstattliche Erklärung elektronisch über myCampus abgegeben — Status laut `CLAUDE.md` → Fristen offen.
- [OFFEN] Einreichungs-Anleitung im myCampus-Kurs gelesen — nicht dokumentiert.
- [ERINNERT] Keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko).

## Claims
- Ungesicherte FACTUAL CLAIMS: keine erfundenen Belege; alle `\parencite` valide. Nivedhitha (2024) und Shen (2023) weiterhin nur per Abstract belegt — vor Abgabe am Volltext verifizieren (Nutzer-Pflicht, IU-KI-Richtlinie).
- Fehlende OWN-WORK-Markierungen: keine.
- Ungenutzte Bib-Einträge: keine.
- Offene `% UNVERIFIED:`-Marker: keine im Text.

## Punkteabzug im Detail
- Voll-Audit (23.07.): −15 (undefined refs/Lieferobjekt) + −10 (Verzeichnisse) = −25 → 75/100.
- Re-Audit: beide Root Causes behoben → beide Abzüge zurückgenommen → **Summe 0 → 100/100.**

## Bewertungsschwerpunkte (Projektbericht)
- **Qualität (25 %)**: ABGEDECKT — Konzept erfüllt die Aufgabenstellung; das zuvor im PDF fehlende UI/UX-Mockup ist jetzt eingebunden.
- **Prozess (25 %)**: ABGEDECKT — Phasenplanung, Reflexion, Lessons Learned, dreischichtige Limitationen.
- **Transfer (15 %)**: ABGEDECKT beide Dimensionen — gesellschaftlich (SDG 12.3) und wirtschaftlich (Freemium, Kooperationen).
- **Kreativität (15 %)**: ABGEDECKT — Wettbewerbsvergleich (6 Plattformen) + offensiver Zero-Waste-Innovationskern.
- **Dokumentation (10 %)**: ABGEDECKT — Entstehungs-Artefakte (Mockups, Persona) jetzt im kompilierten Anhang sichtbar; Verzeichnisse eingebunden.
- **Ressourcen (10 %)**: ABGEDECKT — Aufwands-/Ressourcenschätzung je Phase.

## Lieferobjekt-Abgleich
- [PASS] Alle Objekte im Dokument: Wettbewerbsvergleich, Funktionsübersicht, Phasenplanung (Textteil) sowie Persona-Tabelle und vier UI/UX-Mockups (jetzt eingebundener Anhang). Bilddateien real vorhanden.

## Handlungsempfehlungen (nach Priorität)
1. **[Nutzer-Aktion, verbleibender einziger echter Schritt]** Lokal kompilieren: `latexmk -lualatex main.tex`, Log auf `undefined`/`not found`/`multiply defined` prüfen. Der statische Befund sagt „aufgelöst" voraus — die Ausführung bestätigt es. (In dieser Umgebung nicht ausführbar.)
2. Seitenumfang des Textteils (7–10 S. B.Sc.) am kompilierten PDF gegenprüfen.

## Vor der Einreichung (Nutzer-Checkliste, ohne Score-Wirkung)
- `latexmk -lualatex main.tex` lokal ausführen; Log auf undefined references/citations, fehlende Bilder, doppelte Labels prüfen (bestätigt den statischen PASS von Teil-Check D).
- Seitenumfang des Textteils (7–10 S. B.Sc., ab „1 Einleitung" bis vor Literaturverzeichnis) am PDF prüfen.
- Nivedhitha (2024) und Shen (2023) am Volltext verifizieren (bislang nur Abstract).
- Eidesstattliche Erklärung elektronisch über myCampus abgeben (Voraussetzung, sonst nimmt Turnitin die Einreichung nicht an).
- Einreichungs-Anleitung im myCampus-Kurs lesen; keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko).
- LanguageTool-Durchgang (lokal) über den Gesamttext.
