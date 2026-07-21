# PERSISTENT.md — arbeitenübergreifende Dauer-Präferenzen

**Stand:** 2026-07-21 (Skill-Optimierungsrunde P1–P6) · **Zuletzt gepflegt in:** Medienplattformen-Projektbericht

Diese Datei wandert von Projekt zu Projekt: Beim Start einer neuen Arbeit die `PERSISTENT.md` aus dem **vorherigen Projekt** hierher kopieren (diesen Seed einfach überschreiben). Sie enthält nur Präferenzen, die **unabhängig von der konkreten Arbeit** gelten — Stil, Zitier-Sonderfälle, Prozess-/Modellpräferenzen. Alles Projektspezifische gehört in `MEMORY.md`.

**Eintragsregel** (gilt für Claude): **Default ist diese Datei.** Ein `[LERNEN:...]`-Eintrag gehört nur dann nach `MEMORY.md`, wenn er sich konkret auf *diese* Arbeit bezieht (dieses Thema, dieser Papiertyp, diese Aufgabenstellung, dieses Kapitelgerüst). Alles zu Stil, Ton, Zitier-Sonderfällen, Modellwahl, Session-Führung und Reihenfolge der Arbeitsschritte ist projektübergreifend — sonst geht es beim nächsten Projekt verloren, denn nur diese eine Datei wandert mit. Format und Housekeeping (ÜBERHOLT-Markierung, Konsolidierung ab ~20 Einträgen) wie in `MEMORY.md`. Bei Widerspruch zwischen beiden Dateien gewinnt `MEMORY.md` (die projektspezifische Regel ist die speziellere). Nach jedem Eintrag die Kopfzeile (Stand/Projekt) aktualisieren.

**Format**: `[LERNEN:kategorie] Datum — Beschreibung` · Kategorien: `stil` · `zitation` · `prozess` · `sonstiges`

---

## Einträge

[LERNEN:prozess] 2026-07-21 — Nutzer möchte `pages/meta.tex` → `\SubmissionDate` bewusst dauerhaft auf `\today` gesetzt haben, entgegen der Template-Warnung („NIE \today — ändert sich bei jedem Kompilieren"). Auf den Zielkonflikt hingewiesen (Deckblatt zeigt dann Kompilierdatum statt echtem Abgabedatum), Nutzer hat sich informiert dafür entschieden. Gilt projektübergreifend, nicht nur für dieses Projekt.

[LERNEN:prozess] 2026-07-21 — Kompakt-Plan-Stresstest (plan-modus Schritt 4) ist jetzt ein **Pflicht-Minimalpass**, nicht mehr optional. Anlass: kompakt geplant, Stresstest übersprungen („nichts wirkte wacklig") — ein nachgeholter Einzel-Stresstest fand trotzdem einen Stark-Befund im finalen Plan. Der Selbst-Check „wackelt hier etwas?" ist strukturell blind, weil der Autor der schlechteste Richter über die eigenen Schwächen ist. Skill entsprechend geändert (`plan-modus/SKILL.md` Betriebsarten + Schritt 4).

[LERNEN:prozess] 2026-07-21 — Stresstest hat jetzt ein **Verifikations-Gate**: Behauptungen über die Außenwelt (Marktlage, Konkurrenzprodukte, „keine Plattform tut X") werden erst recherchiert, dann bewertet. Anlass: ein „Stark: das gibt es schon"-Befund kippte nach Web-Recherche komplett (niemand kombinierte die Features → USP hielt doch). Ohne Recherche produziert der Stresstest selbstbewusst-falsche Ratings. Skill geändert (`stresstest/SKILL.md`).

[LERNEN:prozess] 2026-07-21 — Produkt-/Plattform-/Konzeptnamen vor finaler Übernahme in den Plan einmal auf **Namenskollision** prüfen (eine Suche): schon belegt als Marke/App/Verein im selben Feld? Anlass: Arbeitstitel „Restlos" kollidierte mit „Restlos Glücklich" e.V./App (identisches Zero-Waste-Feld), erst im Stresstest entdeckt. Untergräbt Eigenständigkeits-/Innovationsanspruch + markenrechtlich heikel. Als Pflicht-Check ins Namens-Gate aufgenommen (`plan-modus/SKILL.md` Schritt 0, Faustregel Konzeptarbeiten). DPMA/Domain-Verfügbarkeit bleibt Nutzer-Pflicht.

[LERNEN:prozess] 2026-07-21 — Grundprinzip **„Erst prüfen, dann behaupten"** gilt jetzt projektübergreifend für jeden Skill, nicht nur für den Stresstest: Vor jeder belastbaren Außenwelt-Aussage (Markt, Konkurrenz, Zahlen) **oder** internen Regel-/Blocker-Aussage („das ist ein Blocker", „so darf man nicht zitieren") erst die maßgebliche Quelle konsultieren (Web bzw. Projektdatei — `aufgabe.md`, `sources/Anmerkungen vom Prüfer.md`, `hard-rules-formal.md`, `typen/<typ>.md`), nicht aus dem Gedächtnis behaupten. Anlass: ein interner Blocker-Befund („references.bib fehlt Keys") wurde behauptet, bevor `sources/Anmerkungen vom Prüfer.md` gelesen war, wo die Antwort längst stand. In `CLAUDE.md` → Grundprinzipien verankert.

[LERNEN:prozess] 2026-07-21 — `sources/Anmerkungen vom Prüfer.md` (falls vorhanden) ist jetzt eine **Pflichtquelle**, kein Zufallsfund: `setup-check` weist ihre Existenz aus, `plan-modus` Schritt 0 destilliert bindende Steuerungen verpflichtend nach `aufgabe.md` → „## Prüfer-Steuerungen", `schreib-modus`/`pruef-modus` prüfen diesen Abschnitt zuerst, bevor eine Formalia-/Methodik-Frage aus der Standardregel beantwortet wird. Anlass: Die Datei enthielt bindende Abweichungen (Wettbewerbsanalyse = eigene Analyse, keine Primärdaten nötig), wurde aber nur gefunden, weil der Nutzer aktiv darauf zeigte.

[LERNEN:prozess] 2026-07-21 — Vor dem ersten `schreib-modus`-Aufruf gibt es jetzt einen **Plan-Audit** als eigenen Umfang in `pruef-modus` (empfohlen bei jeder Arbeit, Pflicht ab > 3 Kapiteln oder eigener Vergleichsmatrix): prüft `kapitelplan.md` auf roten Faden, Waisen-Inhaltspunkte, Redundanz/Widerspruch zwischen Subsections, Flughöhe, Abdeckungs-Re-Verify gegen `aufgabe.md` und Budget-Realismus — kein Score, reine Fundliste. Grund: Strukturprobleme im Plan fielen bisher erst nach investierten Schreib-Sessions auf, weil kein Schritt den fertigen Plan als Ganzes prüfte.

[LERNEN:prozess] 2026-07-21 — `plan-modus`-Output bekommt vor Fertigstellung einen **Pflicht-Integritätscheck**: jede bestätigte Draft-Entscheidung (Abhakliste, Lieferobjekte, bestätigte Feature-Ideen) muss im finalen `kapitelplan.md` einen Ort haben, sonst gilt sie als verloren. Anlass: „Journaling/Menüplanung" fiel bei der Konsolidierung Draft → Output still heraus, obwohl im Draft zugeordnet.

[LERNEN:prozess] 2026-07-21 — Jede im Plan genannte Quelle bekommt jetzt eine **Zitier-Klassifikation**: (a) zitiert → `\parencite` + BBT-Key Pflicht, (b) eigene Analyse/Sichtung → `\quelle{Eigene Darstellung.}`, kein Cite, nicht in `references.bib`, (c) unzulässig → auf Primärquelle ausweichen. Anlass: Plattformen/Webquellen standen im Plan unter „Belege" und hätten `schreib-modus` beinahe zu `\parencite` mit erfundenem Key verleitet — nur eine manuelle Sonderregel in derselben Session verhinderte es. Jetzt strukturell in `plan-modus` Schritt 3, `schreib-modus` und `hard-rules-formal.md` verankert.

[LERNEN:prozess] 2026-07-21 — Vor dem allerersten `schreib-modus`-Aufruf gibt es jetzt einen **Bereitschafts-Check** als eigenen, rein mechanischen Umfang in `pruef-modus` (Nutzer-Entscheidung: Heimat `pruef-modus`, nicht `schreib-modus`-Eingangsritual — konsistent mit „Audits nur in pruef-modus"): BBT-Keys für alle `[zitiert]`-Quellen, Abhakliste/Lieferobjekte vollständig zugeordnet, kein offener Stark-Stresstest-Befund, Namens-/Prüfer-Steuerungen berücksichtigt, Papiertyp-Pflichtpunkte je einem Kapitel zugeordnet. Kein Score, keine Textbewertung — reiner Dateiabgleich. Anlass: eine Bereitschaftseinschätzung enthielt einen falschen Blocker („Zotero nötig"), weil sie geschätzt statt geprüft war. `schreib-modus` bietet den Check beim allerersten Aufruf (leeres `chapters/`) unverbindlich an.

<!-- Beispiel:
[LERNEN:stil] 2026-07-18 — Nutzer bevorzugt generell kürzere Absätze (3–4 Sätze), unabhängig vom Papiertyp.
[LERNEN:prozess] 2026-07-18 — Kapitel-Entwürfe immer erst als Gliederungs-Stichpunkte zeigen, dann ausformulieren.
-->
