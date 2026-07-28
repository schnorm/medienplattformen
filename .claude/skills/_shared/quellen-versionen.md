# Quellen-Versionsstand – sind Vorlagen und destillierte Regeln noch aktuell?

Die `_shared`-Regeldateien sind **Destillate** aus den IU-PDFs in `sources/`. Die IU aktualisiert Richtlinien, Zitierleitfaden und Prüfungsleitfäden regelmäßig; ein veraltetes Destillat erzeugt selbstbewusst-falsche Formalia-Aussagen. Diese Datei hält fest, auf welchem Stand das Template ist und wann der Nutzer die Aktualität zuletzt bestätigt hat.

**Warum das keine Kür ist:** Die Richtlinien legen selbst fest, welche Fassung gilt – „Für die Verfassung von schriftlichen Arbeiten an der IU gilt die zum Zeitpunkt der **Abgabe des Erstversuchs** der Arbeit gültige Version der Richtlinien bzw. des Zitierleitfadens" (Richtlinien 10/2025, S. 1). Maßgeblich ist also nicht der Stand bei Projektbeginn, sondern der bei Abgabe. Bei kurzen Arbeiten liegt dazwischen oft nur wenig Zeit – bei einem Projektbericht über ein ganzes Semester dagegen durchaus ein Update.

## Versionsregister

| IU-Quelle (in `sources/`) | Version im Template | destilliert in | zuletzt vom Nutzer bestätigt |
|---|---|---|---|
| Richtlinien Gestaltung wiss. Arbeiten | 01.10.2025 | `hard-rules-formal.md` (Formalia, Struktur, Umfang, Gendern, Transkriptionsregeln Anhang F) | – |
| Zitierleitfaden | 01.10.2025 | `hard-rules-formal.md` (Zitationen), `literaturverzeichnis.md` | – |
| Prüfungsleitfaden Hausarbeit | ohne Datumsangabe | `typen/hausarbeit.md` | – |
| Prüfungsleitfaden Fallstudie | ohne Datumsangabe | `typen/fallstudie.md` | – |
| Prüfungsleitfaden Seminararbeit | ohne Datumsangabe | `typen/seminararbeit.md` | – |
| Prüfungsleitfaden Projektbericht | ohne Datumsangabe | `typen/projektbericht.md` | – |

**Die vier Prüfungsleitfäden tragen kein Versionsdatum** – anders als Richtlinien und Zitierleitfaden lässt sich hier nicht am Deckblatt ablesen, ob sich etwas geändert hat. Bei ihnen hilft nur der inhaltliche Vergleich der Punkte, die das Destillat trägt: geforderte Bestandteile, Seitenumfang, Bewertungsgewichte.

**Nicht in `sources/`, aber trotzdem geltend:** Der Leitfaden zur Vermeidung eines Plagiats und die Richtlinie zur KI-Nutzung liegen hier nicht als PDF vor. Die daraus stammenden Punkte in `hard-rules-formal.md` (Ideenplagiat, Eigenplagiat, KI-Ausgaben) sind als solche gekennzeichnet und gelten hochschulweit. Wer sie im Zweifelsfall nachschlagen will, findet beide im Prüfungs-Guide auf myCampus.

## Prüf-Prozedur (wer, wann, wie)

**Wann geprüft wird:** beim `setup-check` (immer) und **vor dem Voll-Audit** (`pruef-modus`), falls die letzte Bestätigung länger als ~3 Monate zurückliegt – kurz vor der Abgabe zählen die Formalia am meisten.

**Wie geprüft wird (Skill-Ablauf):**
1. `sources/` listen und mit dem Register abgleichen.
2. Den Nutzer aktiv fragen (per `AskUserQuestion`): „Sind das noch die aktuellen Fassungen aus dem Prüfungs-Guide auf myCampus? Bei Richtlinien und Zitierleitfaden steht das Datum auf dem Deckblatt; bei den Prüfungsleitfäden hilft nur ein Blick auf die geforderten Bestandteile und den Seitenumfang."
3. **Bestätigt aktuell** → Spalte „zuletzt bestätigt" auf das heutige Datum setzen, quittieren.
4. **Neuere Version vorhanden** → Nutzer legt die neue PDF nach `sources/` (alte ersetzen). Danach eine eigene kurze Session: neues PDF lesen und **gegen die betroffenen Destillat-Dateien diffen** – nur tatsächliche Änderungen einarbeiten, Register-Zeile aktualisieren, Änderungen sichtbar quittieren. Bei Änderungen an Format- oder Zitierregeln zusätzlich prüfen, ob `check_formalia.py` oder `check_bib_hygiene.py` betroffen sind.
5. **Nutzer unsicher / keine Zeit** → Register unverändert lassen und im Statusbericht als OFFEN führen – nicht stillschweigend als aktuell werten.

**Grundsatz:** Bei Widerspruch zwischen Destillat und aktuellem IU-Original gilt das Original; das Destillat wird nachgezogen. Formalia-Aussagen gegenüber dem Nutzer nennen im Zweifel den Versionsstand („laut Richtlinien 10/2025 …").
