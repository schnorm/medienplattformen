# BBT-Konfiguration (Zotero)

Einrichtung in Zotero → Better BibTeX (BBT):

- **Citation-Key-Format**: `[auth:lower]_[year][shorttitle(1,1)]` (z. B. `normanDesignEverydayThings2013`)
- **Export-Format**: BibLaTeX, Unicode ON
- **Auto-Export pro Collection**: Zielspeicher = `<latex-projektordner>/references.bib`, „Keep updated“ = ON
- **Titel-Casing abschalten** – Einstellungen → Better BibTeX → Reiter **Erweitert** → Abschnitt „Miscellaneous“: in das **Textfeld** „Titel-Casing auf Titel anwenden“ den Wert `off` eintragen. Es ist kein Häkchen, sondern ein Eingabefeld – **und die Beschriftung fehlt in manchen Installationen**, das Feld steht dann unbeschriftet da. Zu erkennen ist es an der Position: zwischen der Checkbox „Inkludiere automatische Tags in den Export“ und der Checkbox „Groß-/Kleinschreibung … indem sie Klammern beigefügt wird“ – Letztere ist eine **andere** Einstellung (Schutzklammern) und hilft hier nicht. Leer bedeutet **aktiv**: BBT schreibt englische Titel bei jedem Export in Title Case um, sodass in Zotero korrigierte Sentence-Case-Titel nie in der `.bib` ankommen. Der Wert `off` leert die Liste der Felder, auf die die Umwandlung angewandt wird.
- **Falls das Feld nicht bedienbar ist** (in manchen Installationen erscheint es als leeres Auswahlfeld ohne Optionen): den Wert direkt setzen über Zotero → Einstellungen → Erweitert → Konfigurationseditor → `extensions.zotero.translators.better-bibtex.exportTitlecase` auf `off`.
- **Manuelle Edit-Sperre**: `references.bib` nie manuell editieren – Änderungen gehen beim nächsten Auto-Export verloren.

Wirkung prüfen (nach einem Export, vom Projekt-Root):

    python .claude/skills/_shared/scripts/check_bib_hygiene.py | grep -c "Title Case"

Steht dort trotz korrigierter Zotero-Titel eine hohe Zahl, ist die Export-Umwandlung noch aktiv.

Diese Datei ist Setup-Wissen (einmalig pro Projekt) und liegt deshalb hier statt in `CLAUDE.md` – letzteres wird in jeder Session geladen.
