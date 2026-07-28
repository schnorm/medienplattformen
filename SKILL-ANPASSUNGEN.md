# SKILL-ANPASSUNGEN

Arbeitsdokument, kein Bestandteil der Abgabe. Sammelt Änderungsvorschläge an `CLAUDE.md`, den Skills unter `.claude/skills/` und den Prüfskripten. Die vorherige Sammlung (Session vom 2026-07-28, P1-1 bis P3-x) ist vom Nutzer abgearbeitet und wurde deshalb ersetzt.

Jeder Punkt nennt: Beobachtung → warum es kein Einzelfall ist → Zieldatei → konkreter Vorschlag → Aufwand.

---

## P1-1 · `check_quellentreue.py` meldet einen nicht auflösbaren Pfad wie ein fehlendes `file`-Feld

**Beobachtung (Delta-Re-Audit, 2026-07-28).** Das Skript meldete für `barkerWhatNudgeTechniques2021`, `somaFoodWasteReduction2020` und `vittuariHowReduceConsumer2023`:

> `kein PDF-Snapshot im file-Feld – Webquelle live prüfen: https://…`

Diese Aussage war falsch. Alle drei Einträge **hatten** ein `file`-Feld — es zeigte auf die Zotero-Ablage des Nutzers (`/home/normi/Zotero/storage/X6D69NPM/…`), die in der Session-Umgebung nicht existiert. Die Volltexte lagen zugleich als PDF unter `sources/literatur/`, also genau dort, wo das Projekt sie erwartet.

**Folgeschaden.** Der Audit übernahm die Skriptaussage und schrieb daraus einen Befund „sechs Quellen ohne Volltext-Snapshot, −15". Erst der Nutzer-Einwand („Ist der Ordner eventuell im gitignore?") führte zur Nachprüfung. Die anschließende Volltextprüfung deckte auf, was der Fehlalarm verdeckt hatte: **drei echte Fundstellen-Befunde**, darunter zwei Zitationen auf eine Seite, die es in der zitierten Publikation nicht gibt. Ein Fehlalarm, der eine ganze Quellenklasse als „ohnehin unprüfbar" abstempelt, ist damit teurer als ein übersehener Einzelfall — er schaltet die Prüfung genau dort ab, wo sie greifen würde.

**Warum kein Einzelfall.** `references.bib` wird per Zotero/BBT exportiert, und Zotero schreibt **immer** absolute Pfade seiner lokalen Ablage. Auf der Maschine des Nutzers lösen sie auf, in jeder anderen Umgebung (Container, zweiter Rechner, CI) nie. Das trifft also **jeden** Bib-Eintrag mit angehängtem PDF, bei jedem Lauf außerhalb des Nutzer-Rechners — der Normalfall, nicht die Ausnahme.

**Zieldatei.** `.claude/skills/_shared/scripts/check_quellentreue.py` (`pdf_pfad()` / `epub_pfad()` / `_datei_kandidaten()`, ca. Z. 383–430).

**Vorschlag, drei Teile:**
1. **Fallback auf `sources/literatur/`.** Löst kein Kandidat aus dem `file`-Feld auf, den **Dateinamen** (ohne Verzeichnis) zusätzlich unter `sources/literatur/` und `sources/literature/` suchen. Zusätzlich, wenn auch das scheitert, per Fuzzy-Match über Autornachname + Jahr gegen die Dateinamen dort — die Projektkonvention (`Barker2021_NudgeTechniquesFoodWasteBehaviour.pdf`) trägt beides im Namen.
2. **Ehrliche Statusmeldung.** Ein gesetztes, aber nicht auflösbares `file`-Feld darf nicht denselben Status bekommen wie ein fehlendes. Eigene Klasse, etwa `DATEI NICHT GEFUNDEN`, mit dem versuchten Pfad im Klartext: „`file`-Feld gesetzt, Datei nicht gefunden unter `/home/normi/Zotero/storage/…` — Volltext nach `sources/literatur/` kopieren oder Pfad korrigieren." Der Unterschied ist entscheidend: „keine Quelle vorhanden" ist ein Rechercheproblem des Nutzers, „Pfad zeigt ins Leere" ein Konfigurationsproblem von 30 Sekunden.
3. **Bestandsprüfung beim Start.** Einmal pro Lauf melden, welche Dateien in `sources/literatur/` liegen, ohne von einem `file`-Feld referenziert zu werden. Das hätte den Fall hier sofort sichtbar gemacht.

**Zwischenlösung, bereits umgesetzt.** Die drei `file`-Felder tragen jetzt zusätzlich den repo-relativen Pfad, angehängt nach Zoteros Mehrdatei-Konvention (`<Zotero-Pfad>;sources/literatur/<datei>.pdf`). Der Zotero-Pfad bleibt damit auf dem Nutzer-Rechner gültig, der zweite Kandidat greift überall sonst. **Achtung:** Der nächste BBT-Export überschreibt das wieder — die Skript-Lösung oben ist die dauerhafte.

**Aufwand.** Klein bis mittel, reine Pfadauflösung, keine neue Abhängigkeit.

---

## P1-2 · Auditregel: bei „Quelle nicht auffindbar" erst im Dateisystem nachsehen, dann den Befund schreiben

**Beobachtung.** Derselbe Vorfall, andere Ebene. Der Audit hat die Skriptaussage ungeprüft übernommen und einen −15-Befund daraus gebaut, statt `ls sources/literatur/` auszuführen — ein Aufruf, der die Sache in zwei Sekunden geklärt hätte. Das Grundprinzip „Erst prüfen, dann behaupten" (`CLAUDE.md`) gilt ausdrücklich auch für **interne** Aussagen („die Quelle liegt nicht vor"), und genau dort wurde es verletzt.

**Warum kein Einzelfall.** Skriptausgaben lesen sich wie Messwerte und werden deshalb nicht hinterfragt. `SKILL.md` verstärkt das sogar: „Die Skript-Funde direkt in Teil-Check A übernehmen, diese Punkte **nicht** zusätzlich per Durchlesen prüfen." Diese Regel ist für Formalia-Funde richtig (dort ist das Skript näher an der Wahrheit als das Modell), aber sie darf nicht auf Aussagen über **Existenz** ausgedehnt werden.

**Zieldatei.** `.claude/skills/pruef-modus/SKILL.md`, Teil-Check G, Punkt 4.

**Vorschlag.** Vor Punkt 4 einfügen:

> **Bevor eine Quelle als nicht prüfbar gemeldet wird, das Dateisystem befragen** — `ls sources/literatur/` und der Abgleich der Dateinamen gegen die Bib-Keys sind billiger als jeder Befund. `NICHT PRÜFBAR` und `LIVE PRÜFEN` bedeuten nur, dass das Skript den Volltext über das `file`-Feld nicht **auflösen** konnte, nicht, dass er fehlt. Liegt die Datei da, ist der Befund kein Quellen-, sondern ein Pfadproblem — und die Prüfung wird durchgeführt, nicht aufgeschoben.

**Aufwand.** Minimal, drei Sätze.

---

## P2-1 · Vermischte Seitenzählung bei Preprint und Verlagsfassung

**Beobachtung.** `vittuariHowReduceConsumer2023` wird an drei Stellen zitiert, mit zwei unvereinbaren Zählungen: `[S. 106]` folgt der Verlagsfassung (*Sustainable Production and Consumption* 38, S. 104–114), `[S. 1]` folgt der White-Rose-Preprint-Fassung, deren Fließtext bei 1 beginnt. Der Bib-Eintrag weist ausschließlich die Verlagsseiten aus — wer `[S. 1]` nachschlägt, findet in der zitierten Publikation nichts. Das Skript hat den Widerspruch sichtbar gemacht, aber nur halb: `[S. 106]` meldete es als `SEITE VERDÄCHTIG` („liegt außerhalb des PDFs, 23 Seiten"), weil das hinterlegte PDF der Preprint ist.

**Warum kein Einzelfall.** Frei zugängliche Repositorien (White Rose, arXiv, PubMed Central, ResearchGate) liefern durchweg Fassungen mit eigener Zählung, während der Bib-Eintrag aus der Verlagsdatenbank stammt. Wer den Volltext über das Repositorium liest und die Seite von dort abschreibt, erzeugt diesen Fehler systematisch — und keine der bisherigen Prüfungen fand ihn, weil `check_formalia.py` nur die **Existenz** einer Stellenangabe prüft, nicht ihre Plausibilität gegen `pages`.

**Zieldatei.** `.claude/skills/_shared/scripts/check_quellentreue.py` **und** `.claude/skills/_shared/hard-rules-formal.md`.

**Vorschlag.**
1. **Deterministischer Check:** Jede numerische Stellenangabe gegen das `pages`-Feld des Eintrags halten. Liegt `[S. X]` außerhalb des dort genannten Bereichs, als eigene Klasse melden — etwa `SEITE AUSSERHALB` mit dem Text „`[S. 1]` liegt außerhalb der laut `pages` zitierten Spanne 104–114 — vermutlich Preprint-Zählung." Das ist eine reine Feldprüfung ohne Volltext und fängt den Fehler auch dann, wenn gar kein PDF vorliegt.
2. **Regel:** In `hard-rules-formal.md` unter Zitationen festhalten: Wird ein Volltext aus einem Repositorium gelesen, die Verlagsfassung aber zitiert, sind die Seitenangaben der **Verlagsfassung** maßgeblich. Steht sie nicht zur Verfügung, `[Abs. X]` oder `[Kap. X]` statt einer Seitenzahl verwenden — eine unauffindbare Seitenzahl ist schlechter als keine.

**Aufwand.** Klein (Check), minimal (Regel).

---

## P2-2 · Teil-Check D braucht einen Weg ohne lokale TeX-Installation

**Beobachtung.** Die Session-Umgebung hatte am Vormittag `lualatex`/`latexmk`/`biber`, am Abend nicht mehr. Teil-Check D wäre damit erneut ÜBERSPRUNGEN gewesen — und mit ihm der Seitenumfang, das einzige Kriterium, dessen Nichterfüllung laut IU-Richtlinien ausdrücklich Punkte kostet. Der Ausweg lief über das eingecheckte `main.pdf`: Seitenzahl, Verzeichnisse und aufgelöste Referenzen ließen sich daraus vollständig ablesen, nachdem vier Textproben aus dem letzten Commit die Aktualität des PDFs belegt hatten.

**Warum kein Einzelfall.** Die Umgebung ist nicht stabil, und `check_umfang.py` schätzt nachweislich zu niedrig (9,8 geschätzte gegen 11 gemessene Seiten — die Heuristik ignoriert Abbildungen, Tabellen und Float-Umbrüche). Ein Score, der bei 89 gedeckelt wird, weil niemand nachsehen konnte, ist die schlechtere Antwort, wenn das gebaute PDF danebenliegt.

**Zieldatei.** `.claude/skills/pruef-modus/SKILL.md`, Teil-Check D, Punkt 4.

**Vorschlag.** Punkt 4 ersetzen:

> **Fehlt `lualatex`/`biber`, zuerst nach einem gebauten PDF sehen** (`main.pdf` im Root, `build/main.pdf`). Ist eines vorhanden, seine **Aktualität belegen**, bevor es ausgewertet wird: drei bis vier kurze Textproben aus dem jüngsten Commit, der `chapters/` berührt hat, im PDF suchen und zusätzlich prüfen, dass die jeweils ersetzten Vorgängerformulierungen **nicht** mehr darin stehen. Erst dann Seitenumfang, Verzeichnisse und aufgelöste Referenzen daraus ablesen und im Bericht als „aus vorhandenem PDF, Aktualität verifiziert" ausweisen. Kein aktuelles PDF und kein TeX: dann ÜBERSPRUNGEN und Score-Deckel 89 wie bisher.

**Aufwand.** Klein, Regeltext plus die bereits erprobte Vorgehensweise.

---

## P3-1 · Zwei bekannte Fehlalarme in `check_formalia.py`

Beide erzeugen jedes Mal Rauschen, das im Bericht einzeln entkräftet werden muss.

1. **Anhangszählung scheitert am geschützten Leerzeichen.** Meldung „`main.tex`: Anhangsverzeichnis aktiv bei 0 Anhang", während `pages/appendix.tex` drei Anhänge enthält. Die Zählung erkennt `\section*{Anhang~A: …}` nicht, weil zwischen „Anhang" und dem Buchstaben ein `~` steht — das die IU-Formatierung dort gerade verlangt. Fix: `~` und geschütztes Leerzeichen im Suchmuster als Trenner zulassen.
2. **`LOCATOR_RE` erkennt `[Kap.~8]` nicht.** Bereits am 28.07. gefunden, hier nur zur Vollständigkeit: Stellenangaben mit `~` vor der Ziffer werden als fehlend gemeldet. Gleiche Ursache, gleicher Fix.

**Zieldatei.** `.claude/skills/_shared/scripts/check_formalia.py`.
**Aufwand.** Je eine Regex-Zeile.
