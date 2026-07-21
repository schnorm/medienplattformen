---
name: setup-check
description: Prüft einmalig zu Beginn eines neuen Projektordners, ob die Umgebung bereit ist — lualatex verfügbar, references.bib vorhanden und mit Einträgen befüllt, Consensus MCP verbunden. Nutzen, wenn ein neuer Projektordner mit CLAUDE.md und .claude/skills/ zum ersten Mal geöffnet wird, oder wenn unklar ist, ob alle Voraussetzungen für Plan-/Schreib-/Prüf-Modus erfüllt sind.
---

# Setup-Check: Umgebung zu Projektbeginn prüfen

Kein Ersatz für Plan-/Schreib-/Prüf-Modus — nur ein kurzer Vorab-Check, damit spätere Skills nicht an einer fehlenden Grundvoraussetzung scheitern.

## Ablauf

1. **LaTeX-Kompilierbarkeit**: prüfen, ob `main.tex` vorhanden ist und ob `lualatex` **und** `biber` als Befehle verfügbar sind (`which lualatex biber` bzw. äquivalent — biber wird für das Literaturverzeichnis und Prüf-Modus Teil-Check D gebraucht). Falls nicht verfügbar: Nutzer auf lokale Installation hinweisen, nicht versuchen, LaTeX selbst zu installieren.
2. **`references.bib`**: existiert die Datei? Enthält sie mindestens einen Eintrag? Leere oder fehlende Datei → Hinweis, dass Zotero/BBT-Auto-Export noch eingerichtet werden muss (siehe `references/bbt-setup.md`).
3. **Skripte**: kurzer Testlauf (`python3 .claude/skills/_shared/scripts/check_bib_keys.py references.bib` und `python3 .claude/skills/_shared/scripts/check_formalia.py chapters/`), nur um zu bestätigen, dass Python 3 verfügbar ist und beide Skripte laufen.
4. **Shared-Referenzen**: existieren `.claude/skills/_shared/hard-rules-formal.md`, die vier Typ-Dateien `.claude/skills/_shared/typen/<typ>.md` (hausarbeit, fallstudie, seminararbeit, projektbericht) und `.claude/skills/_shared/scripts/check_bib_keys.py`? (Zentrale Einzelkopien — Skill-lokale Duplikate von Typ-/Regel-Dateien gibt es bewusst nicht mehr; falls welche unter `*/references/` oder `*/scripts/` auftauchen — z. B. ein `<typ>.md` oder ein zweites `check_formalia.py` außerhalb von `_shared/` —, sind sie veraltet und zu melden. `setup-check/references/bbt-setup.md` ist davon ausgenommen, das ist die reguläre BBT-Setup-Anleitung.)
5. **`pages/meta.tex`**: existiert die Datei und sind die CAPS-Platzhalter (PAPIERTITEL, MODULKÜRZEL …) schon durch echte Projektangaben ersetzt? Falls nicht: Nutzer erinnern — das ist die einzige Stelle für projektspezifische Angaben (Titel, Modul, Tutor:in, Schlagworte).
6. **Aufgabenstellung + Abgabefrist**: Liegt die Aufgabenstellung (PDF/Text) vor? Ist die Abgabefrist bekannt? → Frist in `CLAUDE.md` → „Fristen" eintragen (Zeile „Abgabe: …"). Die inhaltliche Destillation nach `aufgabe.md` übernimmt später Plan-Modus Schritt 0 — hier nur sicherstellen, dass das Material da ist.
6b. **Prüfer-Anmerkungen**: existiert `sources/Anmerkungen vom Prüfer.md` (oder ähnlich benannt, z. B. `Anmerkungen*.md` in `sources/`)? Diese Datei kann bindende Steuerungen enthalten, die von der reinen Aufgabenstellung abweichen (z. B. Methodik-Sonderfälle, Zitierausnahmen) — Plan-Modus Schritt 0 destilliert sie verpflichtend mit. Falls nicht vorhanden: kein Fehler, nur im Statusbericht als FEHLT ausweisen, damit der Nutzer weiß, dass keine gesondert geprüft wurde.
7. **`PERSISTENT.md`**: noch im Seed-Zustand (Kopfzeile „Stand: —")? → Nutzer erinnern: Falls es eine frühere Arbeit gibt, deren `PERSISTENT.md` hierher kopieren (den Seed überschreiben) — sonst gehen die arbeitenübergreifenden Lernpunkte verloren.
8. **Consensus MCP**: prüfen, ob der Connector in der aktuellen Umgebung verbunden ist (Tool-Liste). Falls nicht: Hinweis, dass Plan-Modus Schritt 1 ohne Verbindung automatisch übersprungen wird, und wie er verbunden werden kann (Connectors-Einstellungen).
9. **Ordnerstruktur**: grober Abgleich mit dem in `CLAUDE.md` hinterlegten Baum — fehlen `pages/`, `chapters/`, `images/`, `logos/`, `tables/`? Falls ja: anlegen (leere Ordner) oder Nutzer fragen, ob eine andere Struktur gewünscht ist.
10. **`CLAUDE.md` → „Aktueller Projektstatus"**: prüfen, ob die Platzhalter (`sec:<slug-1>` etc.) noch unausgefüllt sind — falls ja, kurz erwähnen, dass sie nach dem ersten Plan-Modus-Durchgang durch echte `sec:<slug>`-Einträge ersetzt werden.

## Ausgabeformat

```
[SETUP-CHECK]
LaTeX (lualatex + biber): OK / FEHLT (<was fehlt>) — <Hinweis>
references.bib: OK (<N> Einträge) / FEHLT / LEER — <Hinweis>
Python 3 (für check_bib_keys.py): OK / FEHLT
Shared-Referenzen (_shared inkl. typen/): OK / FEHLT (<betroffene Dateien>)
pages/meta.tex: AUSGEFÜLLT / PLATZHALTER — <Hinweis>
Aufgabenstellung: VORHANDEN / FEHLT · Abgabefrist: <Datum, in CLAUDE.md eingetragen> / UNBEKANNT
Prüfer-Anmerkungen (sources/Anmerkungen*.md): VORHANDEN / FEHLT
PERSISTENT.md: ÜBERNOMMEN / SEED — <Hinweis auf Kopie aus Vorgängerprojekt>
Consensus MCP: VERBUNDEN / NICHT VERBUNDEN — <Hinweis>
Ordnerstruktur: VOLLSTÄNDIG / UNVOLLSTÄNDIG (<fehlende Ordner>)

Ergebnis: BEREIT / NOCH EINRICHTUNG NÖTIG
```

Bei „BEREIT": Nutzer kann direkt mit `plan-modus` starten. Bei offenen Punkten: konkrete nächste Schritte nennen, keine Schritte automatisch für den Nutzer im System ausführen (z. B. keine Softwareinstallation ohne Rückfrage).
