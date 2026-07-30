# SKILL-ANPASSUNGEN.md

Offene Änderungsvorschläge an Skills, Skripten und `CLAUDE.md`. **Kein Abgabebestandteil.**

Neu angelegt 2026-07-30, nachdem die vorherigen Punkte (P1–P18) übernommen und die Datei geleert wurde.

**Status:** zwei Punkte OFFEN.

---

## P20 — Kürzungsrunden entfernen stillschweigend die einzige Erklärung eines Fachbegriffs

**Konkreter Fall (2026-07-30, gefunden auf Nutzerfrage, nicht durch ein Skript).** `chapters/02_durchfuehrung/03_konzept.tex:9` benutzt den Begriff „Nudge" fünfmal im gesamten Dokument (`03_vorgehen_und_aufbau.tex:3`, `03_konzept.tex:9` ×2 in Fließtext und Tabelle, `02_limitationen.tex:3`, `01_kernergebnisse_und_ausblick.tex:5`) — keine einzige Stelle definiert ihn. Git-Historie zeigt: Bis Commit `caa4cc9` stand dort noch „… also der Forschung zu kleinen Gestaltungsimpulsen, die Verhalten lenken, ohne Wahlmöglichkeiten einzuschränken", über `9f66281` verkürzt auf „verhaltenslenkende Gestaltungsimpulse", und im letzten Bearbeitungsdurchgang (`65c4802`) beim Umbau des Satzes auf „einen belegten Nudge-Typ" ersatzlos herausgefallen — kein bewusster Verzicht, sondern Nebeneffekt einer Satzstraffung. Der Voll-Audit vom 24.07. hatte „Nudge" noch ausdrücklich als vorbildlich erklärten Begriff gelobt; das war zu diesem Zeitpunkt zutreffend und ist es seit einer späteren Kürzungsrunde nicht mehr.

**Warum kein Skript das auffängt.** `check_formalia.py` prüft `ABKUERZUNG` nur für tatsächliche Abkürzungen (Großbuchstabenfolgen ohne `\ac{}`), nicht für ausgeschriebene Fachbegriffe wie „Nudge", „Fairteiler" oder „Drivers/Levers". Eine Definition ist zudem keine feste Struktur wie ein `\ac{}`-Eintrag, sondern ein frei formulierter Nebensatz („also …", „, den … beschreiben, …") — es gibt keinen strukturellen Marker, den ein Skript vor und nach einer Kürzung vergleichen könnte.

**Bezug zu P17** (Kürzen ist ein blinder Arbeitsschritt, kein Skill besitzt ihn): Dies ist ein konkreter Unterfall — nicht nur Bezüge zwischen Sätzen brechen bei Kürzung, sondern auch die einzige Erklärung eines Fachbegriffs kann verschwinden, während der Begriff selbst an anderen Stellen unverändert weiterverwendet wird und dadurch unbemerkt unerklärt bleibt.

**Vorschlag.** Keine vollautomatische Lösung sinnvoll (Definitionen sind nicht strukturell erkennbar). Stattdessen ein manueller Prüfschritt im Kürzungs-Workflow (sobald er existiert, siehe P17) bzw. im `pruef-modus`/Teil-Check F: für jeden mehrfach verwendeten Fachbegriff, der nicht im Abkürzungsverzeichnis steht (grobe Heuristik: ein Wort kommt ≥3× vor, ist kein Akronym, keine Alltagssprache), prüfen, ob mindestens eine Fundstelle eine erklärende Apposition oder einen Nebensatz trägt. Bei einer Kürzung an oder neben einer Stelle mit „also"/„d. h."/erklärendem Doppelpunkt gezielt nachsehen, ob dort die einzige Definition eines andernorts weiterverwendeten Begriffs stand.

---

## P19 — Korrektur an P16: Der Trägersatz einer Tabellenzelle greift in die Nachbarabsätze über

**Datei:** `.claude/skills/_shared/scripts/check_quellentreue.py` → `satz_um()`

**Achtung, das hebt die Änderung aus P16 auf.** P16 hatte als Ursache die Float-Option benannt und vorgeschlagen, vor der Hash-Bildung LaTeX-Struktur-Zeilen (`\begin{…}`, `\toprule`, `\caption{…}`) aus dem Trägersatz zu entfernen. **Das behebt das Problem nicht.** Die Beobachtung war richtig, die Diagnose zu eng.

**Tatsächliche Ursache, mechanisch nachgewiesen.** `satz_um()` schneidet den Trägersatz an Satzgrenzen (`SATZENDE_RE`). Eine Tabellenzelle enthält keinen Satzschlusspunkt. Für eine Zitation in einer Zelle spannt die Funktion deshalb vom **letzten Punkt vor der Tabelle bis zum ersten Punkt nach der Tabelle**. Gemessen an `03_konzept.tex`, Zelle „Rettungspunkte \& Reste-Level": **1530 Zeichen** — beginnend bei `\begin{table}[H]`, endend mitten im Folgeabsatz bei „… sowie einem Profilbereich mit Rettungspunkten, Reste-Level und eigenen Beiträgen."

Damit invalidiert **jede** Änderung in unmittelbarer Nachbarschaft der Tabelle alle Zitationen ihrer Zellen, obwohl kein Zeichen des zitierenden Textes berührt wurde. Am 30.07. ist das dreimal passiert, jedes Mal für dieselben drei Urteile (Barker, Nivedhitha, Soma):

| Auslöser | Änderung am zitierenden Text? |
|---|---|
| `[H]` → `[htbp]` (Weißraum-Fix) | nein |
| Tabelle hinter den Innovationsabsatz verschoben | nein |
| Folgesatz „Das User Interface (UI) folgt drei Hauptbereichen …" umgestellt | nein |

Neun Neubuchungen an einem Tag, jede mit dem Risiko einer verrutschten Notiz — genau die Fehlerklasse aus P2-3. Gegenprobe: Eine reine Zeilenverschiebung (Kommentarzeile am Dateianfang) ändert die Hashes **nicht**; es ist also kein Positions-, sondern ein Spannenproblem.

**Konkrete Änderung.** In `satz_um()` erkennen, ob die Position innerhalb einer `tabular`/`tabularx`-Umgebung liegt. Wenn ja, den Trägersatz auf die **Zelle** begrenzen: Grenzen sind `&` (unmaskiert) und `\\`, ergänzt um die Zeile davor als Kontext, falls die Zelle allein nicht aussagekräftig ist. Damit hängt der Hash am Zellentext — dem einzigen Text, den die Zitation belegt. Die in P16 vorgeschlagene Struktur-Zeilen-Filterung wird dadurch überflüssig, weil `\begin{table}[…]`, `\caption` und `\toprule` außerhalb der Zelle liegen.

**Nebenwirkung, die eingeplant sein muss.** Der Umbau ändert die Hashes aller Tabellen-Zitationen einmalig. Die bestehenden Urteile in `quellencheck-state.json` müssten migriert oder einmalig neu gebucht werden — sinnvollerweise im selben Schritt, mit einem Hinweis im Bericht, dass es sich um eine Migration und nicht um eine inhaltliche Neuprüfung handelt.
