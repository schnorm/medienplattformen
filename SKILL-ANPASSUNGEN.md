# SKILL-ANPASSUNGEN.md

Offene Änderungsvorschläge an Skills, Skripten und `CLAUDE.md`. **Kein Abgabebestandteil.**

Neu angelegt 2026-07-30, nachdem die vorherigen Punkte (P1–P18) übernommen und die Datei geleert wurde.

**Status:** ein Punkt OFFEN.

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
