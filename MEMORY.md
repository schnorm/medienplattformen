# MEMORY.md

Persistente Korrekturen und bestätigte Vorgehensweisen des Nutzers — als Datei, nicht nur im Gesprächsverlauf oder in Cowork-Memory, da beides sessionübergreifend nicht zuverlässig genug ist für harte Fakten (siehe `CLAUDE.md` → Grundprinzipien).

**Wann hier eintragen**: Wenn der Nutzer eine Vorgehensweise explizit korrigiert ("nein, mach das anders, immer so:") oder eine Abweichung vom Standard-Setup bestätigt (z. B. "Methodik-Kapitel entfällt bei uns auch empirisch"). **Sofort im Moment der Korrektur, nicht am Sessionende** — und im Chat quittieren („📝 In MEMORY.md gelernt: …"), damit Fehleinträge sofort auffallen. Nicht für beiläufige Inhalte der Arbeit selbst — die gehören in `kapitelplan.md`/`chapters/`. Nicht für einmalige Anweisungen ohne Dauergeltung („mach diesen einen Absatz kürzer") — nur für Regeln mit „immer/ab jetzt"-Charakter; im Zweifel nachfragen statt eintragen. **Projektunabhängige Dauer-Präferenzen** („gilt generell, nicht nur für diese Arbeit") gehören stattdessen in `PERSISTENT.md` — bei Widerspruch zwischen beiden gewinnt diese Datei (die projektspezifische Regel ist die speziellere).

**Format**: `[LERNEN:kategorie] Datum — Beschreibung`

Kategorien: `stil` (Formulierung/Voice) · `struktur` (Kapitelgerüst-Abweichungen) · `zitation` (Zitier-Sonderfälle) · `prozess` (Workflow-Präferenzen, z. B. Modellwahl) · `sonstiges`

## Housekeeping

- **Widerspruch statt Löschen**: Widerlegt ein neuer Eintrag einen bestehenden, wird der alte **nicht gelöscht**, sondern mit `[ÜBERHOLT von <Datum des neuen Eintrags>]` vorangestellt — so bleibt nachvollziehbar, dass sich die Vorgehensweise geändert hat, statt dass zwei widersprüchliche Einträge kommentarlos nebeneinanderstehen. Der neue Eintrag wird normal ergänzt.
- **Vor jeder Anwendung eines Eintrags prüfen**, ob er `[ÜBERHOLT]` markiert ist — überholte Einträge gelten nicht mehr, bleiben aber als Verlauf stehen.
- **Konsolidierung ab ca. 20 Einträgen**: Wird die Liste unübersichtlich, in einer eigenen Runde alle `[ÜBERHOLT]`-Einträge und erledigte `struktur`-Einträge (z. B. zu einem inzwischen fertig geschriebenen Kapitel) gemeinsam mit dem Nutzer durchgehen und tatsächlich löschen, nicht nur weiter anhäufen. Diese Konsolidierung selbst wird nicht als neuer `[LERNEN:...]`-Eintrag geloggt.

---

## Einträge

[LERNEN:prozess] 2026-07-19 — Teil-Check E (Abgabe) fließt in `pruef-modus` in keinem Audit-Umfang in den Score ein — auch nicht im Abgabe-Audit. Grund: Die Punkte betreffen reine myCampus-Verwaltungsschritte außerhalb des Textes; sie erscheinen ausschließlich als „Vor der Einreichung"-Hinweisliste am Ende des Berichts.

<!-- Beispiel (löschen, sobald der erste echte Eintrag ansteht):
[LERNEN:stil] 2026-07-16 — Nutzer bevorzugt kürzere Absätze (3–4 statt 4–6 Sätze) auch in Kapiteln, wo der Richtwert in _shared/typen/<typ>.md höher liegt.

Beispiel für eine Überholt-Markierung:
[ÜBERHOLT von 2026-08-02] [LERNEN:stil] 2026-07-16 — Nutzer bevorzugt kürzere Absätze (3–4 statt 4–6 Sätze).
[LERNEN:stil] 2026-08-02 — Korrektur: doch beim Richtwert aus _shared/typen/<typ>.md bleiben, kürzere Absätze nur in der Einleitung.
-->
