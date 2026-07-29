# Projektstruktur (Referenz)

Kommentierter Baum des Projektordners. Ausgelagert aus `CLAUDE.md`, weil er nur an wenigen Stellen gebraucht wird: `setup-check` (prüft die Struktur auf Vollständigkeit) und `plan-modus` Schritt 2.5 (Dateinamen und Ordner der Kapitel festlegen). Wer nur wissen will, welche Datei welche Wahrheit trägt, findet die Kurzliste in `CLAUDE.md` → „Ordnerstruktur".

## Ordnerstruktur

```
<latex-projektordner>/
├── CLAUDE.md                    # diese Datei, immer automatisch geladen
├── handbuch.md                  # Nutzer-Handbuch (einzige Quelle; handbuch.pdf ist daraus erzeugtes Derivat – generate_handbuch_pdf.py)
├── MEMORY.md                    # Korrekturen/Lernpunkte NUR für dieses Projekt
├── PERSISTENT.md                # projektübergreifende Dauer-Präferenzen – wandert per Kopie von Projekt zu Projekt
├── aufgabe.md                   # destillierte Aufgabenstellung (Plan-Modus Schritt 0) – Single Source statt Aufgaben-PDF
├── kapitelplan.draft.md         # Zwischenstand Plan-Modus (nach Abschluss: INSIGHT-Archiv)
├── kapitelplan.md               # finaler, bestätigter Kapitelplan
├── AENDERUNGEN.md               # Änderungsaufträge in Runden (aus Gesamt-Stresstest/Review/Nutzer-Feedback): je Punkt eine konkrete Anweisung; [FREIGABE]-Punkte nur nach aktiver Rückfrage umsetzen; Abarbeitung im schreib-modus, danach leeren und Delta-Re-Audit
├── quellencheck.md              # Volltextabgleich aller Zitationen (check_quellentreue.py, pro Lauf neu)
├── quellencheck-state.json      # Urteile je Zitation – überdauert Läufe, nie von Hand editieren
├── pruefbericht.md              # letzter Audit-Bericht (Prüf-Modus überschreibt pro Lauf)
├── main.tex                     # Wurzeldokument – nicht umbauen; nur die markierten Aktivierungsblöcke schalten
│                                #   (Gender-Disclaimer, Abbildungs-/Tabellenverzeichnis, Anhang)
├── verworfen.md                 # bewusst verworfene Anforderungen: Datum, Begründung, Wiederaufnahme-Bedingung
│                                #   (Gegenlesung liest sie ERST in Schritt 6 – sonst bricht die Inversion)
├── references.bib               # BBT-Export aus Zotero – NIE manuell editieren
├── pages/
│   ├── meta.tex                 # Projektangaben – EINZIGE projektspezifische Stelle
│   ├── acronyms.tex             # Abkürzungsverzeichnis (\acro{}-Einträge)
│   ├── appendix.tex             # Anhänge – je einer als \newappendix{Titel}; Verzeichnis entsteht daraus
│   ├── appendix-setup.tex       # Anhang-Maschinerie (aus der Präambel geladen) – NIE ändern
│   ├── cover.tex                # Titelblatt (nutzt meta.tex) – NIE ändern
│   └── chapters.tex             # bindet alle Hauptkapitel-Master per \input{} ein
├── chapters/                    # Kapitel gemäß kapitelplan.md
│   └── 01_einleitung/
│       ├── einleitung.tex        # Kapitel-Master (\section), bindet Subsections per \input{}
│       └── 01_<slug>.tex         # Subsection-Dateien
├── images/<kapitel>/            # Abbildungen, gespiegelt zur Kapitelstruktur (Konvention: hard-rules-formal.md → LaTeX)
├── logos/ · tables/             # Logos bzw. Tabellen-Fragmente
├── sources/                     # IU-Leitfäden pro Papiertyp (Zweifelsfall) + optionales Anmerkungen vom Prüfer.md (Pflichtquelle, siehe plan-modus Schritt 0) Zweifelsfall lesen
│   └── literature/              # EIGENE Quellen (Ebooks, Paper) – jederzeit befüllbar, auch vor dem Setup; Anleitung in literature/README.md. Wird in plan-modus Schritt 1 VOR der Consensus-Suche gesichtet. Nicht versioniert (.gitignore)
└── .claude/skills/
    ├── _shared/                 # hard-rules-formal.md, typen/<typ>.md, aenderungen-format.md, scripts/
    ├── setup-check/             # einmaliger Umgebungscheck
    ├── plan-modus/              # Betriebsarten kompakt/ausführlich, Schritt 0–4
    ├── schreib-modus/           # Kapitel schreiben
    ├── pruef-modus/             # Audit vor Abgabe (inkl. Build- und Abgabe-Check)
    ├── gegenlesung/             # kalte Prüfer-Gegenlesung gegen aufgabe.md (alle Kapitel FERTIG)
    └── stresstest/              # Gegenargumente prüfen, jederzeit einzeln aufrufbar
```
