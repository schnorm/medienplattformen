---
name: setup-check
description: Prüft einmalig zu Beginn eines neuen Projektordners, ob die Umgebung bereit ist – lualatex verfügbar, references.bib vorhanden und mit Einträgen befüllt, Consensus MCP verbunden. Nutzen, wenn ein neuer Projektordner mit CLAUDE.md und .claude/skills/ zum ersten Mal geöffnet wird, oder wenn unklar ist, ob alle Voraussetzungen für Plan-/Schreib-/Prüf-Modus erfüllt sind.
---

# Setup-Check: Umgebung zu Projektbeginn prüfen

Kein Ersatz für Plan-/Schreib-/Prüf-Modus – nur ein kurzer Vorab-Check, damit spätere Skills nicht an einer fehlenden Grundvoraussetzung scheitern.

## Ablauf

1. **LaTeX-Kompilierbarkeit**: prüfen, ob `main.tex` vorhanden ist und ob `lualatex` **und** `biber` als Befehle verfügbar sind (`which lualatex biber` bzw. äquivalent – biber wird für das Literaturverzeichnis und Prüf-Modus Teil-Check D gebraucht). Falls nicht verfügbar: Nutzer auf lokale Installation hinweisen, nicht versuchen, LaTeX selbst zu installieren.
2. **`references.bib`**: existiert die Datei? Enthält sie mindestens einen Eintrag? Leere oder fehlende Datei → Hinweis, dass Zotero/BBT-Auto-Export noch eingerichtet werden muss (siehe `references/bbt-setup.md`). **Unabhängig davon, ob die Datei existiert, einmal die BBT-Exporteinstellungen gegen `references/bbt-setup.md` prüfen** – insbesondere das Title-Casing. Enthält `references.bib` bereits Einträge, liefert `python .claude/skills/_shared/scripts/check_bib_hygiene.py | grep -c "Title Case"` den Beweis: Eine hohe Zahl bei englischen Quellen bedeutet, dass BBT die Titel beim Export umschreibt – dann `bbt-setup.md` laden und die Einstellung mit dem Nutzer korrigieren. Das ist kein Randfall: Die Voreinstellung ist aktiv, und der Effekt fällt sonst erst im Abgabe-Audit auf, wo jede Korrektur in Zotero wirkungslos bleibt.
3. **Skripte**: kurzer Testlauf beider Skripte (`.claude/skills/_shared/scripts/check_bib_keys.py references.bib` und `.claude/skills/_shared/scripts/check_formalia.py chapters/`), nur um zu bestätigen, dass Python 3 verfügbar ist und beide Skripte laufen.
   **Interpreter zuerst bestimmen und im Statusbericht festhalten** – der Aufruf ist plattformabhängig: Unter Windows ist `python3` in aller Regel der Microsoft-Store-Platzhalter, der *nicht* funktioniert („Python wurde nicht gefunden"), während `python` das echte Python ist; unter macOS/Linux ist es meist umgekehrt. Deshalb einmalig `python --version` und `python3 --version` prüfen, den funktionierenden Befehl merken und **in allen Folgeaufrufen dieser und späterer Sessions genau diesen verwenden**. Schlägt ein Skriptaufruf in einem anderen Skill mit „Python wurde nicht gefunden" fehl, ist das die Ursache – dann auf den anderen Befehl wechseln, nicht das Skript für defekt halten.
4. **Shared-Referenzen**: existieren `.claude/skills/_shared/hard-rules-formal.md`, `_shared/literaturverzeichnis.md`, `_shared/stilprofil.md`, `_shared/projektstruktur.md`, `_shared/aenderungen-format.md`, `_shared/modell-empfehlung.md`, `_shared/quellen-versionen.md`, die vier Typ-Dateien `.claude/skills/_shared/typen/<typ>.md` (hausarbeit, fallstudie, seminararbeit, projektbericht) sowie sämtliche Skripte unter `.claude/skills/_shared/scripts/` (`check_all.py`, `check_bib_keys.py`, `check_formalia.py`, `check_umfang.py`, `check_bib_hygiene.py`, `check_status.py`, `check_quellentreue.py` – Letzteres braucht `pdfplumber`, `pip install pdfplumber`; ohne das Paket fällt der Volltextabgleich aller Zitationen aus, der in jedem Audit Pflicht ist)? **Die Liste ist vollständig zu prüfen** – `stilprofil.md` etwa lädt jede Schreib- und Prüf-Session, ihr Fehlen fiele sonst erst dort auf. (Zentrale Einzelkopien – Skill-lokale Duplikate von Typ-/Regel-Dateien gibt es bewusst nicht mehr; falls welche unter `*/references/` oder `*/scripts/` auftauchen – z. B. ein `<typ>.md` oder ein zweites `check_formalia.py` außerhalb von `_shared/` –, sind sie veraltet und zu melden. `setup-check/references/bbt-setup.md` ist davon ausgenommen, das ist die reguläre BBT-Setup-Anleitung.)
5. **`pages/meta.tex` – Metadaten aktiv abfragen und eintragen** (nicht nur erinnern): Datei lesen und prüfen, welche CAPS-Platzhalter noch stehen. Sind welche offen, die fehlenden Angaben **per `AskUserQuestion` im Dialog erheben und anschließend selbst per Edit in `pages/meta.tex` eintragen** – `meta.tex` ist ausdrücklich editierbar (im Gegensatz zu `main.tex` und `cover.tex`) und die einzige projektspezifische Stelle; `cover.tex` und die PDF-Metadaten ziehen sich alles von dort. Unbekannte Felder bleiben Platzhalter und werden als OFFEN gemeldet – `check_formalia.py chapters/ pages/` listet jeden verbliebenen im Audit namentlich (META-PLATZHALTER).

   Abzufragende Felder: `\PaperTitle` · `\PaperType` (Hausarbeit/Fallstudie/Seminararbeit/Projektbericht) · `\StudyProgram` · `\ModuleCode` · `\ModuleName` · `\AuthorName` · `\MatrikelNr` · `\TutorName` · `\SubmissionDate` · `\PaperKeywords`. `\StudyProgram` aktiv im Dialog erfragen (nicht vorbelegen; z. B. „Wirtschaftsinformatik (B. Sc.)").

   **Regeln dabei:**
   - Mehrere Felder pro Frage bündeln (Titel+Typ+Modul in einer Runde, Person+Matrikelnummer in der nächsten), nicht neun Einzelfragen stellen.
   - **Unbekannte Felder bleiben Platzhalter**, werden nicht geraten und im Statusbericht als OFFEN gelistet. Typische Fälle zu Projektbeginn: Abgabedatum und Tutor:in stehen vor der Kurszuteilung noch nicht fest.
   - `\SubmissionDate` als **festes Datum** eintragen (z. B. `31.03.2026`), niemals `\today` – das änderte sich bei jedem Kompilieren.
   - Ist das Abgabedatum bekannt, zusätzlich in `CLAUDE.md` → „Fristen" eintragen (deckt sich mit Schritt 6).
   - Jedes tatsächlich geschriebene Feld im Chat sichtbar quittieren („✅ In pages/meta.tex eingetragen: …").
6. **Aufgabenstellung + Abgabefrist**: Liegt die Aufgabenstellung (PDF/Text) vor? Ist die Abgabefrist bekannt? → Frist in `CLAUDE.md` → „Fristen" eintragen (Zeile „Abgabe: …"). Die inhaltliche Destillation nach `aufgabe.md` übernimmt später Plan-Modus Schritt 0 – hier nur sicherstellen, dass das Material da ist.
6b. **Prüfer-Anmerkungen**: existiert `sources/Anmerkungen vom Prüfer.md` (oder ähnlich benannt, z. B. `Anmerkungen*.md` in `sources/`)? Diese Datei kann bindende Steuerungen enthalten, die von der reinen Aufgabenstellung abweichen (z. B. Methodik-Sonderfälle, Zitierausnahmen) – Plan-Modus Schritt 0 destilliert sie verpflichtend mit. Falls nicht vorhanden: kein Fehler, nur im Statusbericht als FEHLT ausweisen, damit der Nutzer weiß, dass keine gesondert geprüft wurde.
6c. **`sources/literatur/` – eigene Literatur inventarisieren**: Verzeichnis-Listing von `sources/literatur/`. Dieser Ordner ist die Ablage, in die der Nutzer **schon vor dem Setup** eigene Quellen legen darf (Ebooks, Paper, Buchkapitel, PDF-Snapshots von Webquellen); Namenskonvention `<Autor><Jahr>_<Kurztitel>.pdf`. **Schreibweise beachten:** deutsch `literatur/`, nicht `literature/` – `check_quellentreue.py` akzeptiert zwar beide, aber zwei Ordner nebeneinander sind der sichere Weg zu einem Volltext, den später niemand findet. Ergebnis: Anzahl + Dateinamen im Statusbericht ausweisen, damit sichtbar ist, worauf Plan-Modus Schritt 1 aufsetzen kann. Dateien **nicht inhaltlich einlesen** – das ist Aufgabe des Literaturschritts, nicht des Setups.
   **Zotero-Abgleich (der eigentliche Zweck des Checks):** Je gefundene Datei anhand von Autor und Jahr im Dateinamen per Grep gegen `references.bib` prüfen, ob ein passender BBT-Eintrag existiert. Fehlt einer, als Hinweis listen – ohne Zotero-Eintrag gibt es keinen BBT-Key, und `schreib-modus` darf laut eigener Regel keinen erfinden; das Werk wäre also lesbar, aber nicht zitierbar. Kein Fehler, nur ein Hinweis: Der Abgleich über den Dateinamen ist eine Heuristik, keine Gewissheit.
   Leerer Ordner ist **kein Fehler** – dann nur erwähnen, dass die Ablage existiert und jederzeit befüllt werden kann.
7. **`PERSISTENT.md`**: noch im Seed-Zustand (Kopfzeile „Stand: –")? → Nutzer erinnern: Falls es eine frühere Arbeit gibt, deren `PERSISTENT.md` hierher kopieren (den Seed überschreiben) – sonst gehen die arbeitenübergreifenden Lernpunkte verloren.
8. **Consensus MCP**: prüfen, ob der Connector in der aktuellen Umgebung verbunden ist (Tool-Liste). Falls nicht: Hinweis, dass Plan-Modus Schritt 1 ohne Verbindung automatisch übersprungen wird, und wie er verbunden werden kann (Connectors-Einstellungen).
9. **Ordnerstruktur**: Abgleich mit dem kommentierten Baum in `_shared/projektstruktur.md` (**jetzt laden** – er nennt auch Zweck und Versionierungsstatus der Ordner) – fehlen `pages/`, `chapters/`, `images/`, `logos/`, `tables/`? Falls ja: anlegen (leere Ordner) oder Nutzer fragen, ob eine andere Struktur gewünscht ist.
9b. **Quellen-Aktualität prüfen** (`_shared/quellen-versionen.md` laden und der dortigen Prüf-Prozedur folgen): `sources/` listen, Register abgleichen, den Nutzer per `AskUserQuestion` fragen, ob Richtlinien, Zitierleitfaden und der Prüfungsleitfaden des Papiertyps noch dem Stand im myCampus-Prüfungs-Guide entsprechen. Bestätigt → „zuletzt bestätigt"-Spalte auf heute setzen. Neuere Version gemeldet → neue PDF nach `sources/`, eigene Abgleich-Session vorschlagen. Unklar → als OFFEN in den Statusbericht, nicht stillschweigend als aktuell werten. Hintergrund: Laut Richtlinien gilt die zum **Abgabezeitpunkt** gültige Fassung, nicht die bei Projektbeginn.
10. **`CLAUDE.md` → „Aktueller Projektstatus"**: `python .claude/skills/_shared/scripts/check_status.py` laufen lassen – gleicht die Statustabelle deterministisch gegen das Dateisystem ab (FERTIG ohne Datei = FEHLER, Kapiteldatei ohne Tabellenzeile = HINWEIS). Zusätzlich prüfen, ob die Platzhalter (`sec:<slug-1>` etc.) noch unausgefüllt sind – falls ja, kurz erwähnen, dass sie nach dem ersten Plan-Modus-Durchgang durch echte `sec:<slug>`-Einträge ersetzt werden.

## Ausgabeformat

```
[SETUP-CHECK]
LaTeX (lualatex + biber): OK / FEHLT (<was fehlt>) – <Hinweis>
references.bib: OK (<N> Einträge) / FEHLT / LEER – <Hinweis>
Python 3: OK (Befehl: <python | python3>) / FEHLT
Shared-Referenzen (_shared inkl. typen/): OK / FEHLT (<betroffene Dateien>)
pages/meta.tex: AUSGEFÜLLT / TEILWEISE (offen: <Felder>) / PLATZHALTER – <was eingetragen wurde>
Aufgabenstellung: VORHANDEN / FEHLT · Abgabefrist: <Datum, in CLAUDE.md eingetragen> / UNBEKANNT
Prüfer-Anmerkungen (sources/Anmerkungen*.md): VORHANDEN / FEHLT
Eigene Literatur (sources/literatur/): <N> Datei(en) / LEER – <ohne Zotero-Eintrag: ...>
PERSISTENT.md: ÜBERNOMMEN / SEED – <Hinweis auf Kopie aus Vorgängerprojekt>
Consensus MCP: VERBUNDEN / NICHT VERBUNDEN – <Hinweis>
Ordnerstruktur: VOLLSTÄNDIG / UNVOLLSTÄNDIG (<fehlende Ordner>)
Quellen-Aktualität: BESTÄTIGT <Datum> / OFFEN / UPDATE NÖTIG (<Quelle>) – siehe _shared/quellen-versionen.md

Ergebnis: BEREIT / NOCH EINRICHTUNG NÖTIG
```

Bei „BEREIT": Nutzer kann direkt mit `plan-modus` starten. Bei offenen Punkten: konkrete nächste Schritte nennen, keine Schritte automatisch für den Nutzer im System ausführen (z. B. keine Softwareinstallation ohne Rückfrage).
