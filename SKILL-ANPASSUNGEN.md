# SKILL-ANPASSUNGEN.md

Offene Änderungsvorschläge an Skills, Skripten und `CLAUDE.md`. **Kein Abgabebestandteil.**

Neu angelegt 2026-07-30, nachdem die vorherigen Punkte (P1–P18) übernommen und die Datei geleert wurde.

**Status:** 3 Punkte OFFEN

---

## P34 — Fix-Vorschläge aus dem Prüfbericht werden als abgenommene Lösung behandelt, obwohl sie nur der kleinste Eingriff sind

**Konkreter Fall (2026-07-30, Abgabe-Audit Befund 2 und die Überarbeitung danach).** Der Bericht fand in `03_konzept.tex` eine Ankündigung „**die drei** von der Aufgabenstellung genannten Zwecke", von denen der Satz nur zwei einlöst, und empfahl als Variante (a) — ausdrücklich „empfohlen", „kleinster Eingriff" — die Ersetzung durch „**zwei der drei** … Zwecke". Genau so umgesetzt, `check_all.py` 0 FEHLER, Build sauber. Erst die Rückfrage des Nutzers („ist das jetzt noch angemessen?") brachte zwei Mängel ans Licht, die der Fix erzeugt bzw. stehen gelassen hat:

1. **Die Zähl-Differenz wurde umgedreht, nicht behoben.** Nach dem Doppelpunkt folgen **drei** Glieder. Vorher passte die Zahl zur Aufzählung, aber nicht zur Sache; nachher passte sie zur Sache, aber nicht mehr zur Aufzählung. Wer nachzählt, findet in beiden Fassungen eine Differenz.
2. **Der Fix schwächte ausgerechnet die Stelle, die ein Bewertungskriterium allein trägt.** „Zwei der drei" ist eine Defizitansage in einem Satz, der mit „ist neu" öffnet — und derselbe Bericht weist diesen Absatz unter „Bewertungsschwerpunkte" als alleinigen Träger von **Kreativität (15 %)** aus.

Die tragfähige Lösung (nach `AskUserQuestion` umgesetzt) zählt gar nicht, sondern benennt: „…, wie Resteria den Zero-Waste-Fokus in die von der Aufgabenstellung genannten Zwecke **Rezept-Teilen und gegenseitige Inspiration** hineinträgt **und ihn zugleich in der täglichen Nutzung verankert**: …". Damit ist jedes der drei Glieder gedeckt, ohne dass eine Zahl im Satz steht.

**Warum das nicht durch Sorgfalt zu verhindern war.** Der Bericht **zitiert den vollständigen Satz** direkt über seiner eigenen Fix-Empfehlung — die drei Doppelpunkt-Glieder standen dem prüfenden Durchgang wörtlich vor Augen und wurden trotzdem nicht gegen die neue Zahl gehalten. Und beim Abarbeiten wirkt ein als „empfohlen" markierter, wörtlich ausformulierter Ersetzungsschnipsel wie eine abgenommene Entscheidung: Man ersetzt die genannten Wörter und liest den Satz nicht mehr als Ganzes. Zwei Skripte und ein Build bestätigen das anschließend, weil keiner von ihnen Semantik prüft.

**Vorschlag, drei Teile:**

- **`pruef-modus` → Zählangaben-Befunde:** Eine Zahl im Ankündigungssatz hat immer **zwei** Bezugsgrößen — die Sache, auf die sie sich beruft, und die syntaktisch unmittelbar folgende Aufzählung. Ein Zählbefund ist erst vollständig, wenn beide geprüft sind, und ein Fix-Vorschlag erst zulässig, wenn er beide bedient. In den Bericht gehört das als Zwei-Zeilen-Nachweis („Sache: 2 von 3 · Aufzählung: 3 Glieder"), nicht als Prosa.
- **`pruef-modus` → Form der Fix-Empfehlung:** Fix-Vorschläge, die eine Formulierung ändern, werden als **vollständiger Satz in der Zielfassung** ausgeschrieben, nicht als Ersetzungsschnipsel („X" → „Y"). Der Schnipsel verführt zum blinden Einsetzen; der Ganzsatz zwingt schon beim Schreiben des Berichts dazu, die Fassung einmal zu lesen. Zusätzlich jede Empfehlung, die einen unter „Bewertungsschwerpunkte" als alleinigen Kriteriumsträger ausgewiesenen Absatz berührt, mit `[TRÄGT: <Kriterium> <Gewicht>]` markieren — und dort ausdrücklich prüfen, ob der Fix die Aussage rhetorisch schwächt.
- **`schreib-modus` → Überarbeitung nach Prüfbericht:** Ein Fix-Vorschlag ist eine **Hypothese, keine abgenommene Lösung**. Nach jeder übernommenen Formulierungsänderung den vollständigen Satz plus Folgesatz einmal am Stück gegenlesen — dieselbe Regel, die der Skill für Streichungen bereits kennt („Nach jeder Streichung den ganzen Absatz plus den folgenden neu lesen — nicht den Diff"), gilt für aus dem Bericht übernommene Ersetzungen genauso. Als eigener Punkt in die Self-Check-Liste.

**Möglicher Skript-Anteil (schwächer, aber billig).** `check_formalia.py` meldet Zählaussagen bereits (24 Treffer in diesem Projekt) und könnte den Sonderfall „Zahlwort … Doppelpunkt" deterministisch prüfen: Steht ein Zahlwort (zwei/drei/vier/…) im Satz vor einem Doppelpunkt, die durch Komma und „und" getrennten Glieder bis zum Satzende zählen und bei Abweichung `ZAEHLUNG-LISTE` ausgeben. Fehlalarme sind zu erwarten (Aufzählungen mit Binnenkommata), deshalb als HINWEIS, nicht als FEHLER. Er hätte diesen Fall in **beiden** Fassungen gefunden — vor dem Audit wie nach dem Fix.

---

## P33 — `check_formalia.py` überspringt `pages/meta.tex` als Vorlagen-Gerüst, obwohl der Arbeitstitel darin selbst geschriebener Text ist

**Konkreter Fall (2026-07-30, Abgabe-Audit, Befund 1).** `pages/meta.tex:7` trägt im `\PaperTitle` einen **Geviertstrich** („Resteria — Konzeption einer …"), also genau das Zeichen, das `hard-rules-formal.md` → Schreibstil als FEHLER-Klasse führt (englische Konvention, Turnitin-KI-Marker). Der Titel steht auf dem Titelblatt und in den PDF-Metadaten – der sichtbarsten Stelle der ganzen Arbeit. Er hat rund zehn Audits überlebt, darunter zwei mit Score 100/100.

**Warum kein Skript das auffängt.** `check_formalia.py` führt `meta.tex` in derselben Ausnahmeliste wie `cover.tex`, `chapters.tex` und `gender.tex` („Vorlagen-Gerüst ohne eigenen Fließtext") und weist das in der Ausgabe sogar aus. Das stimmt für die anderen drei; `meta.tex` ist aber die einzige der vier Dateien, die **projektspezifischen Text** enthält – Titel, Modulname, Studiengang, Schlagworte. Für die META-PLATZHALTER-Prüfung liest das Skript die Datei bereits, wendet aber die Textprüfungen nicht darauf an.

**Vorschlag.** `pages/meta.tex` aus der pauschalen Ausnahmeliste nehmen und stattdessen selektiv prüfen: Die Werte der `\newcommand`-Definitionen (nicht die Kommentare, nicht die Makronamen) gegen die Zeichen-Prüfungen laufen lassen – Geviertstrich, gerade Anführungszeichen, `\underline`. Satzlängen-, Trias- und Absatz-Heuristiken bleiben dort sinnlos und sollen weiter übersprungen werden. Nebenbefund derselben Prüfung: Der META-PLATZHALTER-Check meldet `\ModuleCode` und `\MatrikelNr` als „noch nicht ausgefüllt", obwohl beide gefüllt sind (`DLBMIMPFS01-01`, `3210267`) – die Heuristik hält reine Großbuchstaben-/Ziffernfolgen für Platzhalter und sollte gegen die konkreten Auslieferungs-Platzhalter matchen statt gegen ein Muster.

---

## P32 — Der Artikelnummer-Check in `check_bib_hygiene.py` greift erst ab fünf Ziffern und übersieht kurze sowie e-präfigierte Nummern

**Datei:** `.claude/skills/_shared/scripts/check_bib_hygiene.py` → `ARTNO_PAGES_RE = re.compile(r"^\d{5,}$")`

**Konkreter Fall (2026-07-30, Abgabe-Audit, Befund 3).** Zwei `@article`-Einträge tragen ihre Artikelnummer im Feld `pages`: `somaFoodWasteReduction2020` mit `pages = {907}` und `nivedhithaHowGreenSocial2024` mit `pages = {e13038}`. Beides sind belegt Artikelnummern – der Soma-Volltext trägt die Kopfzeile „Sustainability 2020, 12, 907" bei interner Paginierung „1 of 19", der Nivedhitha-Volltext läuft über „N of 29" bei DOI `10.1111/ijcs.13038`. Das Skript meldete **0 Hinweise**, weil „907" nur drei Ziffern hat und „e13038" mit einem Buchstaben beginnt.

**Warum das im Ergebnis sichtbar ist.** Im gedruckten Verzeichnis stehen vier Artikel-Zeitschriften nebeneinander: **Barker** (dieselbe Zeitschrift wie Soma) rendert korrekt „Sustainability, 13(19), **Artikel 11099**", **Shen** „**Artikel 107706**" – Soma und Nivedhitha dagegen ohne den Zusatz, als wären es Seitenzahlen. Die Inkonsistenz fällt beim Lesen des Verzeichnisses sofort auf; genau deshalb verlangt Teil-Check F Punkt 2 das Lesen des **gerenderten** Verzeichnisses und nicht nur den Skriptlauf.

**Vorschlag.** Das Muster erweitern und die Entscheidung an einem zweiten Signal absichern, statt allein an der Ziffernlänge:
- Regex auf `^[eE]?\d{3,}$` erweitern (deckt „907" und „e13038"),
- zusätzlich melden, sobald `pages` **keinen** Bindestrich/Bereich enthält und der Eintrag ein `doi` hat, dessen Suffix die `pages`-Zahl enthält (bei Nivedhitha: `10.1111/ijcs.13038` ↔ `e13038`) – das ist ein starkes, fehlalarmarmes Indiz,
- und als weiche Zusatzheuristik: Tragen mehrere `@article`-Einträge derselben `journaltitle` teils `eid`, teils eine einzelne `pages`-Zahl, das als Inkonsistenz ausgeben (Barker vs. Soma wäre so aufgefallen).

**Nachtrag 2026-07-30 — zweiter, härterer Fall aus der Umsetzung desselben Befunds: `pages` UND `eid` gleichzeitig belegt.** Bei der Korrektur in Zotero wurde `tex.eid` gesetzt, das Seitenfeld aber **nicht geleert**. `style=apa` druckt daraufhin beides: „Sustainability, 12(3), **Artikel 907, 907**." und „International Journal of Consumer Studies, 48(2), **Artikel e13038, e13038**.". Das ist im gedruckten Verzeichnis sichtbar schlechter als der Ausgangszustand — vorher stand die Nummer einmal falsch da, jetzt doppelt. `check_bib_hygiene.py` meldete weiterhin **0 Hinweise**, weil es die Kombination beider Felder nicht prüft.

Das ist der **deterministisch prüfbarste** Teil des ganzen Punkts und sollte vor allen Heuristiken oben umgesetzt werden: Sind in einem Eintrag `pages` und `eid` gleichzeitig belegt, ist das ohne Ausnahme ein Fehler — als FEHLER, nicht als HINWEIS, samt Angabe beider Werte. Gilt erst recht, wenn beide denselben Wert tragen. Kein Fehlalarmrisiko, kein Ermessensspielraum.

Zwei Lehren über das Skript hinaus: Erstens ist eine Zotero-Anweisung mit zwei Teilschritten („Feld setzen **und** Seitenfeld leeren") offenbar eine, bei der der zweite Schritt verlorengeht — Handlungsempfehlungen sollten solche Schritte einzeln nummerieren statt in einem Satz verbinden. Zweitens hat erst das Lesen des **gerenderten** Verzeichnisses den Fall gezeigt, wie schon beim Körperschafts-Fehler bei Nielsen und Sauro & Lewis am 29.07. — Teil-Check F Punkt 2 verdient seinen Aufwand zum zweiten Mal.

**Bezug zu Teil-Check F Punkt 3.** In derselben Prüfung fiel ein zweiter Verzeichnis-Fehler auf, den kein Skript finden kann: Der Titel von `erlhoferWebsiteKonzeptionUndRelaunch2017` führt einen Untertitel („: Das Handbuch für die Praxis"), den weder Cover noch Titelei noch die OPF-Metadaten des vorliegenden EPUB kennen; dazu widerspricht das Impressum („1. Auflage 2018") dem Feld `date = {2017}`. Das ist genau der Fund, für den Teil-Check F die Stichprobe gegen das Deckblatt vorschreibt – der Punkt ist also **kein** Skript-Vorschlag, sondern eine Bestätigung, dass dieser manuelle Schritt seinen Aufwand trägt und nicht zugunsten des Skripts entfallen darf.
