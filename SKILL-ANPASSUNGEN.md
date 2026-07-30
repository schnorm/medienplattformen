# SKILL-ANPASSUNGEN.md

Offene Änderungsvorschläge an Skills, Skripten und `CLAUDE.md`. **Kein Abgabebestandteil.**

Neu angelegt 2026-07-30, nachdem die vorherigen Punkte (P1–P18) übernommen und die Datei geleert wurde.

**Status:** 4 Punkte OFFEN

---

## P35 — Interne `\autoref`-Verweise werden nur auf Fundstelle geprüft, nie auf Reichweite — und niemand merkt, wenn sich das Ziel ändert

**Konkrete Fälle (2026-07-30, Delta-Re-Audit und die Nutzer-Rückfrage danach).** Zwei Befunde in **einem** Absatz, `04_community_und_feedback.tex:9`, beide aus derselben Klasse:

1. „Laut~`\autoref{sec:zielgruppe}` sucht die Zielgruppe **vor allem** einen Ort, an dem der eigene Erfolg von anderen gesehen wird." — `02_zielgruppe.tex:7` leitet **zwei gleichrangige** Anforderungen ab und nennt keine Rangfolge. Der Inhalt steht dort, die Gewichtung nicht.
2. „…der Austausch über Rezepte ist **die Stärke** der etablierten Communitys: Chefkoch.de hat dafür einen **gewachsenen Bestand an Beiträgen** (siehe~`\autoref{sec:wettbewerbsanalyse}`)." — `01_wettbewerbsanalyse.tex:3` belegt Upload, Bewertung, Kommentar und die Einstufung „stark". „Gewachsener Bestand" ist eine Ableitung aus „etabliert", keine Aussage der Analyse.

Beide Sätze sind **nicht falsch**. Beide haben ein Delta-Re-Audit mit ausdrücklich geprüften Querverweisen passiert — ich habe Fall 2 sogar angesehen und als „innerhalb der Toleranz" durchgewinkt. Gefunden hat ihn der Nutzer beim Lesen.

**Warum das strukturell ist und nicht Sorgfalt.** Der Skill besitzt diese Unterscheidung bereits — aber nur für **externe** Quellen. Teil-Check G sagt in seinem eigenen Vorspann: „Er prüft **Fundstelle und Wortlaut** … Er prüft **nicht die Reichweite** — ob die Quelle die Behauptung in der *Stärke* trägt, in der der Satz sie aufstellt." Dafür gibt es das Verdikt `RENTIERT NICHT`, die Trägersatz-Hashes in `quellencheck-state.json`, P18 und die Prüferfrage 3 der `gegenlesung`.

Für interne Verweise existiert nichts davon. Teil-Check C fragt wörtlich nur: „Steht an der Stelle, auf die ein `\autoref` zeigt, tatsächlich der behauptete Inhalt?" — **genau die Fundstellenfrage, die Teil-Check G selbst als unzureichend ausweist.** Die Reichweitenfrage wird für interne Verweise nie gestellt.

**Der zweite, gefährlichere Teil: Ziele bewegen sich, Quellen nicht.** Ein zitiertes PDF ändert sich nie; `check_quellentreue.py` hasht den Trägersatz trotzdem und wirft die Zitation bei jeder Änderung auf `PRÜFEN` zurück (P16/P19 handeln von genau dieser Empfindlichkeit). Das Ziel eines `\autoref` ist dagegen ein **eigenes Kapitel, das laufend umgeschrieben wird** — dieses Projekt hat vier Kürzungsrunden mit über 1.000 gestrichenen Wörtern hinter sich. Würde `02_zielgruppe.tex:7` morgen gekürzt, bliebe der darauf gestützte Satz in `04` unbemerkt stehen. **Es gibt kein Skript, keinen Check und keinen Hash, der das meldet.** Betroffen sind hier **18** `\autoref{sec:…}`-Verweise über acht Dateien.

Das ist dieselbe Klasse wie die drei gebrochenen Bezüge aus P17, nur eine Ebene höher: Dort verlor ein Pronomen sein Bezugswort, hier verliert eine Behauptung ihre Stütze. Beide entstehen im Satz *davor* und überleben Audits, die den Diff prüfen.

**Vorschlag, drei Teile:**

- **`pruef-modus` → Teil-Check C:** Den Prüfpunkt „Querverweise semantisch korrekt" um die Reichweitenfrage erweitern, wortgleich zu Teil-Check G: *Trägt die Zielstelle den Satz in seiner jetzigen Stärke — oder nur einen benachbarten, schwächeren Inhalt?* Besonders auf Gewichtungs- und Absolutheitsmarker im verweisenden Satz achten (`vor allem`, `in erster Linie`, `hauptsächlich`, `die Stärke`, `der wichtigste`, `ausschließlich`, `nur`), denn genau dort entsteht die Differenz. Fundstelle und Reichweite getrennt quittieren, nicht in einem PASS zusammenfassen.
- **Neues Skript oder Erweiterung von `check_quellentreue.py` — der eigentliche Hebel.** Die bewährte Mechanik auf interne Verweise anwenden: je Paar (verweisender Satz, Ziel-Subsection) beide Seiten hashen und in einem `autoref-state.json` ablegen. Ändert sich **eine** von beiden, geht das Paar auf `PRÜFEN`. Das ist deterministisch, ohne Fehlalarmrisiko, wiederverwendet vorhandenen Code und schließt die Lücke, die kein Lesedurchgang zuverlässig schließt — denn niemand liest beim Kürzen von Kapitel 2.2 nach, wer aus Kapitel 2.4 darauf zeigt.
- **`gegenlesung` / `stresstest`:** Prüferfrage 3 (Reichweite) gilt bislang implizit nur für Zitationen. Ausdrücklich auf interne Verweise und auf Rückgriffe auf die **eigene** Analyse ausdehnen („wie die Wettbewerbsanalyse gezeigt hat", „laut Kapitel X") — die Eigenanalyse ist im Projektbericht die Hauptbelegquelle und damit die Hauptquelle für Überdehnungen.

**Zusatzbefund: Hedging-Historie ist ein Abriss-Signal, kein Politur-Signal.** PR #16 hat die alte Soma-Begründung ersetzt und das selbst so begründet: „Nach drei Hedging-Runden trug die Zitation das Argument ohnehin nicht mehr." Der **Ersatz**satz brauchte dann in derselben PR bereits eine Rücknahme („Foren sind die Stärke der etablierten Rezept-Communitys" → „der Austausch über Rezepte", weil die Analyse für Chefkoch kein Forum belegt) — und ist einen Tag später ganz entfallen. Das Muster ist damit zweimal am selben Absatz belegt. P18 kennt die Frage „rentiert sich das Zitat noch?" nur für Zitationen; sie gehört generalisiert: **Ein Satz, dessen Stütze in zwei oder mehr Runden abgeschwächt werden musste, ist ein Ersetzungs-, kein Umformulierungskandidat.** Wo die Reparaturhistorie sichtbar ist (`AENDERUNGEN.md`, Statuszeilen), gehört sie beim Befund mitzitiert, statt die nächste Abschwächung vorzuschlagen.

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
