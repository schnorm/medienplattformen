# SKILL-ANPASSUNGEN

Arbeitsdokument, kein Bestandteil der Abgabe. Sammelt Änderungsvorschläge an `CLAUDE.md`, den Skills unter `.claude/skills/` und den Prüfskripten. Die vorherige Sammlung (Session vom 2026-07-28, Fehlalarm bei nicht auflösenden Zotero-Pfaden) ist vom Nutzer abgearbeitet und wurde deshalb ersetzt.

Jeder Punkt nennt: Beobachtung → warum es kein Einzelfall ist → Zieldatei → konkreter Vorschlag → Aufwand.

> **Status: P1-1, P1-2, P2-1, P2-2 und P3-1 sind am 2026-07-29 umgesetzt** – **P2-3 ist neu und noch offen.** (`plan-modus`, `schreib-modus`, `pruef-modus`, `setup-check`, `hard-rules-formal.md`, `projektstruktur.md`, `vorlagen.md`, `check_quellentreue.py`; 98 Skript-Tests grün, `check_all.py` ohne harte Funde). Die Texte bleiben als Begründung stehen – sie erklären, warum die Regeln so lauten. **Offen ist allein die Liste „Bitte manuell prüfen" am Dateiende.**

**Thema dieser Runde: Quellenbeschaffung.** Der gemeinsame Nenner aller fünf Punkte ist eine Reihenfolge, die im Workflow falsch herum steht. Über die **Zitierfähigkeit** einer Quelle entscheidet heute Teil-Check G – ganz am Ende, unmittelbar vor der Abgabe. **Ausgewählt** wird die Quelle in Plan-Modus Schritt 1, ganz am Anfang. Dazwischen liegt der gesamte Schreibprozess. Ein Journal-Artikel hinter einer Bezahlschranke fällt deshalb genau dann als unprüfbar auf, wenn das Argument bereits auf ihm steht – der teuerste denkbare Zeitpunkt. Die Vorschläge ziehen die Entscheidung nach vorn und machen sie **quellentypabhängig**: Beim Buch ist ein fehlendes PDF eine Aufgabe, beim Journal-Artikel ohne Zugangsweg ein Ausschlussgrund.

---

## P1-1 · Beschaffbarkeits-Gate direkt nach der Consensus-Suche

**Beobachtung.** Drei Zitationen dieser Arbeit stehen ohne Volltext da: `nivedhithaHowGreenSocial2024` (Wiley), `shenInfluenceOsmosisSocial2023` (Elsevier) und die UN-Resolution. Der Delta-Re-Audit vom 28.07. hat dafür −15 gezogen und den erreichbaren Score bei 85 gedeckelt; behoben ist der Punkt bis heute nicht, weil er sich mit den Mitteln der Session nicht beheben lässt. Keine der drei Quellen war ein Recherchefehler – alle drei passen thematisch. Der Fehler liegt darin, dass **kein Schritt je gefragt hat, ob der Volltext beschaffbar ist**, bevor die Quelle in den Plan wanderte.

**Warum kein Einzelfall.** Consensus indexiert über die Metadaten; ob ein Volltext erreichbar ist, ist kein Suchkriterium. Die Regeln in Schritt 1 fragen ausschließlich nach Inhalt und Qualität – Framework, `study_types`, `sjr_max`. Der empfohlene Qualitätsfilter arbeitet dabei sogar **gegen** die Beschaffbarkeit: Je höher das Journal-Ranking, desto wahrscheinlicher die Bezahlschranke. Solange die Regel „Keine Zitation ohne prüfbaren Volltext" (`hard-rules-formal.md`) erst im Audit greift, produziert jedes Projekt mit Journal-Literatur denselben Rückstand.

**Zieldatei.** `.claude/skills/plan-modus/SKILL.md`, Schritt 1 – neuer Unterschritt nach „Nach allen Suchen synthetisieren", **vor** der Priority Reading Order.

**Vorschlag: ein Gate mit drei Urteilen**, angewandt auf jeden Kandidaten, bevor er in die Leseliste kommt. Die Routen werden in dieser Reihenfolge geprüft, es gewinnt die erste, die trägt:

1. **Liegt der Volltext schon in `sources/literatur/`?** Das Listing dazu entsteht ohnehin am Anfang von Schritt 1.
2. **Freie Fassung über die DOI ermitteln – maschinell, nicht geschätzt.** OpenAlex, ohne Schlüssel und ohne Anmeldung:

   ```bash
   curl -s "https://api.openalex.org/works/doi:10.1016/j.chb.2023.107706" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['open_access']); [print(l['is_oa'], l['version'], l.get('pdf_url') or l.get('landing_page_url')) for l in d['locations']]"
   ```

   Am 2026-07-29 an genau den beiden offenen Journal-Quellen dieses Projekts getestet:
   - `10.1016/j.chb.2023.107706` (Shen, Elsevier) → `is_oa: true`, `oa_status: green`, Figshare-Kopie vorhanden, `version: submittedVersion`.
   - `10.1111/ijcs.13038` (Nivedhitha, Wiley) → `is_oa: false`, `oa_status: closed`, keine Repositoriumsfassung.

   Eine der beiden vermeintlich aussichtslosen Quellen hat also einen frei zugänglichen Volltext, die andere wirklich keinen. Genau diese Unterscheidung hat bisher kein Schritt getroffen – beide wurden gleich behandelt und beide blieben liegen.

   **Achtung Fassung:** `submittedVersion`/`acceptedVersion` bringen eine eigene Seitenzählung mit. Dann greift die bestehende Regel „Gelesene Fassung ≠ zitierte Fassung" – Fassung im Plan vermerken und `[Abs. X]`/`[Kap. X]` zitieren, solange die Verlagsseitenzahl nicht verifiziert ist. Sonst verwandelt die OA-Route nur einen −5-Befund in einen −8-Befund (`SEITE AUSSERHALB`), so wie bei Vittuari geschehen.
3. **IU-Bibliothek – die vergessene Normalroute.** Über myCampus stehen lizenzierte Datenbanken zur Verfügung; eine Bezahlschranke im offenen Web sagt nichts darüber aus, ob der Zugang über die Hochschullizenz besteht. Das kann ich nicht selbst prüfen, also wird es **gefragt** und nicht angenommen – per `AskUserQuestion`, mit der DOI in der Frage.
4. **Bücher und E-Books: Beschaffung durch den Nutzer.** In diesem Projekt der erprobte Regelfall – fünf der acht Volltexte in `sources/literatur/` sind so entstanden.

**Urteil je Quelle**, verbindlich im `[INSIGHT: literaturrecherche]`-Block und als eigene Spalte in der Priority Reading Order:

- **VOLLTEXT LIEGT VOR** – uneingeschränkt zitierbar.
- **BESCHAFFBAR (`<Route>`)** – Weg benannt und zugewiesen (Bibliothek · OA-URL · Nutzer-Beschaffung). Kommt in den Plan, aber mit Frist: Der Volltext liegt vor, **bevor** das Kapitel geschrieben wird, das ihn trägt. Bücher landen hier per Default, und das ist ausdrücklich **kein Blocker** – ein Buch ohne PDF ist zum Recherchezeitpunkt eine Aufgabe, kein Ausschlussgrund.
- **KEIN ZUGANG** – keine Route gefunden. **Blocker für die Auswahlentscheidung**: Die Quelle kommt nicht in die Leseliste und bekommt kein `[zitiert]` im Plan. Ersatz wird **in derselben Session** gesucht, solange der Suchkontext noch steht. Das ist der billigste Moment; zwei Monate später kostet dieselbe Entscheidung das Umschreiben einer belegten Passage.

**Aufwand.** Mittel – rund 25 Zeilen Regeltext plus das Kommandobeispiel. Keine neue Abhängigkeit, nur `curl`.

---

## P1-2 · „Kein Volltext" ist heute ein Sammelstatus – er muss die Klasse nennen

**Beobachtung.** `check_quellentreue.py` bildet alles, was keinen auflösbaren Volltext hat, auf zwei Status ab: `LIVE PRÜFEN` (URL vorhanden) und `NICHT PRÜFBAR` (nichts vorhanden). Die Score-Regel behandelt beide gleich: „Nicht prüfbare Quelle ohne Volltext, −5, Deckel −15". Darunter liegen aber drei völlig verschiedene Fälle:

| Fall | Beispiel hier | Aufwand zur Behebung |
|---|---|---|
| Buch ohne hinterlegtes PDF/EPUB | (in dieser Arbeit inzwischen alle beschafft) | eine halbe Stunde |
| Journal-Artikel hinter Bezahlschranke, keine OA-Fassung | Nivedhitha (Wiley) | nur durch Quellenersatz lösbar |
| frei zugängliche Webquelle, nur der Snapshot fehlt | UN-Resolution | zwei Minuten |

Der Bericht zeigt eine Zahl; welcher der drei Fälle dahintersteht, muss der Nutzer selbst herausfinden.

**Warum kein Einzelfall.** Das ist dasselbe Muster wie beim Fehlalarm der letzten Runde: Ein Status, der Unterschiedliches zusammenfasst, erzeugt entweder Fehlalarme oder falsche Prioritäten. Damals waren es Fehlalarme, hier sind es falsche Prioritäten – die billigste Maßnahme (Snapshot ziehen) und die teuerste (Quelle ersetzen) stehen ununterscheidbar nebeneinander, mit identischem Punktabzug.

**Zieldatei.** `.claude/skills/_shared/scripts/check_quellentreue.py` (Statusvergabe, ca. Z. 866–890) · `.claude/skills/pruef-modus/SKILL.md` (Teil-Check G, Punkt 4 und Score-Regel).

**Vorschlag, drei Teile:**

1. **Klasse aus dem Bib-Eintrag ableiten, ohne zusätzliche Pflege.** Default-Heuristik:
   - `@book`/`@inbook`/`@collection` ohne `file` → **`VOLLTEXT BESCHAFFBAR`**: „Buch – PDF/EPUB besorgen und nach `sources/literatur/` legen."
   - `@article`/`@report` ohne `file`, dessen `url`/`doi` auf einen bekannten Bezahlschranken-Host zeigt (`onlinelibrary.wiley.com`, `linkinghub.elsevier.com`, `sciencedirect.com`, `link.springer.com`, `tandfonline.com`, `jstor.org`, `dl.acm.org`, `ieeexplore.ieee.org`) → **`ZUGANG PRÜFEN`**, mit der konkreten Folgeaufgabe im Befundtext: OpenAlex-Abfrage, dann IU-Bibliothek, dann Ersatz.
   - `url` auf frei zugänglichem Host ohne `file` → `LIVE PRÜFEN` wie bisher, plus Snapshot-Pflicht.
2. **Override statt Rätselraten:** `tex.zugang: <volltext|bibliothek|oa:<url>|beschaffbar|kein-zugang>` im Zotero-Feld *Extra*. Better BibTeX exportiert `tex.`-Felder als reguläre Bib-Felder – der Mechanismus ist in diesem Projekt bereits im Einsatz (`tex.shortauthor`, `tex.eid`), es braucht also kein neues Werkzeug. Das Feld schlägt die Heuristik. Dort wird zugleich das Urteil aus P1-1 dauerhaft geparkt: Es überlebt den nächsten BBT-Export, anders als von Hand ergänzte `file`-Pfade.
3. **Score-Folge:** `VOLLTEXT BESCHAFFBAR` ist außerhalb des Abgabe-Audits **kein Abzug**, sondern ein „Vor der Einreichung"-Punkt; `ZUGANG PRÜFEN` behält die −5. **Im Abgabe-Audit blockieren beide** – dort ist eine Quelle, die niemand gelesen hat, unprüfbar, ganz gleich warum. Das hält den Druck an der richtigen Stelle und verhindert, dass ein noch nicht heruntergeladenes Buch in jedem Zwischenaudit Punkte kostet, obwohl der Mangel ein fehlender Download ist.

**Aufwand.** Klein bis mittel – Statusvergabe, eine Hostliste, drei Zeilen Score-Regel.

---

## P2-1 · Volltext-Status durch Plan und Schreib-Modus mitführen

**Beobachtung.** Die Zitier-Klassifikation in Plan-Modus Schritt 3 unterscheidet (a) zitiert, (b) eigene Analyse, (c) unzulässig – über den Volltext zu (a) sagt sie nichts. `schreib-modus` Punkt 3b verlangt anschließend, tragende Belege **vor** dem Formulieren am Volltext zu lesen, kennt aber keinen Fall „es gibt keinen". In der Praxis wird diese Lücke still geschlossen: Der Satz entsteht dann aus dem Abstract.

**Warum kein Einzelfall.** Das Gate aus P1-1 wirkt nur, wenn sein Urteil die Session überlebt. Alles andere in diesem Workflow, was Sessions überdauert, steht in einer Datei – das Zugangsurteil bisher nicht. Es würde bei jedem Neustart neu hergeleitet oder schlicht vergessen.

**Zieldatei.** `.claude/skills/plan-modus/SKILL.md` (Zitier-Klassifikation in Schritt 3, Literaturliste im Output) · `.claude/skills/schreib-modus/SKILL.md` (Punkt 3b).

**Vorschlag.**

1. **Klassifikation um den Status erweitern:** `[zitiert: <key>, Volltext: liegt vor]` bzw. `[zitiert: <key>, Volltext: beschaffbar – Bibliothek]`. Passt in die bestehende Zeile, kostet keine neue Struktur.
2. **`kapitelplan.md` → Literaturliste bekommt zwei Spalten:** **Volltext** (liegt vor · Route · offen) und, bei Repositoriumsfassungen, **gelesene Fassung** (Verlag/Preprint). Die zweite ist der Anschluss an die bestehende `SEITE AUSSERHALB`-Regel – ohne sie wandert eine Preprint-Seitenzahl genauso ungeprüft in den Text wie zuvor bei Vittuari, nur diesmal als Folge der OA-Route, die P1-1 gerade empfiehlt.
3. **`schreib-modus` Punkt 3b um den Fehlfall ergänzen:** Fehlt der Volltext eines tragenden Belegs, wird der Satz **nicht** aus dem Abstract formuliert. Drei zulässige Wege: Volltext jetzt beschaffen · das Argument auf eine andere Quelle stellen · die Aussage auf das zurücknehmen, was ohne diesen Beleg gedeckt ist. „Aus dem Abstract geschrieben" ist der Entstehungsweg des nicht gedeckten Claims, den Teil-Check G später als `CLAIM SCHÄRFER` findet – dann aber mit fertigem Text ringsum.

**Aufwand.** Klein, drei Regelstellen.

---

## P2-2 · Zugriff ist nicht Nachweisbarkeit – Snapshot beim ersten Zugriff, nicht vor der Abgabe

**Beobachtung.** Auch wo Zugang besteht – Bibliothekslizenz, OA-Landingpage –, ist das ein vorübergehender Zustand: Die Lizenz hängt am Campus-Login, OA-Seiten ziehen um, das Audit läuft Monate später. `hard-rules-formal.md` verlangt ein lesbares PDF im `file`-Feld, aber durchgesetzt wird die Forderung erst im Audit. Der Moment, in dem die Beschaffung nichts kostet – man hat die Quelle gerade offen –, trägt keine Regel.

**Warum kein Einzelfall.** Dieselbe Klasse wie P1-1: Geprüft wird am Ende, gehandelt werden müsste am Anfang. Der Effekt ist in diesem Projekt schon sichtbar: Die drei Quellen mit Volltext haben ihn, weil sie irgendwann jemand heruntergeladen hat; die drei ohne wurden nie heruntergeladen, und kein Schritt hat daran erinnert.

**Zieldatei.** `.claude/skills/plan-modus/SKILL.md` (Zotero-Erinnerung in Schritt 1) · `.claude/skills/schreib-modus/SKILL.md` (Punkt 3b) · `.claude/skills/_shared/hard-rules-formal.md` (Zitationen).

**Vorschlag.** Die bestehende Zotero-Erinnerung um den Volltext erweitern – bisher sagt sie ausdrücklich „auch ohne PDF, Metadaten reichen für den BBT-Key". Das stimmt für den Key und ist für die Prüfbarkeit falsch. Zusatz: **Wer eine Quelle einmal offen hat, legt sie sofort ab** – PDF nach `sources/literatur/`, Dateiname nach der Projektkonvention `<Autor><Jahr>_<Kurztitel>.pdf`; bei Webquellen der PDF-Ausdruck der Seite. Zoteros eigenes `file`-Feld genügt dafür nicht: Es zeigt auf die lokale Ablage und löst außerhalb des exportierenden Rechners nie auf (Befund der letzten Runde). Der Projektordner ist der haltbare Ort.

**Aufwand.** Minimal.

---

## P3-1 · Zwei Schreibweisen für denselben Ordner: `sources/literatur` und `sources/literature`

**Beobachtung.** Der reale Ordner heißt `sources/literatur`. Die Skills nennen durchgängig `sources/literature`: `plan-modus` (5 Fundstellen), `setup-check` (4), `pruef-modus` (3), dazu `_shared/projektstruktur.md`. Die `file`-Felder in `references.bib` zeigen auf `literatur`, und `check_quellentreue.py` akzeptiert beide Formen (`LITERATUR_ORDNER`). Zusätzlich verweisen `setup-check` und `projektstruktur.md` auf eine Anleitung `sources/literature/README.md`, die es nicht gibt.

**Warum kein Einzelfall.** Solange nur das Skript beide Schreibweisen kennt, fällt nichts auf. Jede Anweisung an den Nutzer („legen Sie die Datei nach `sources/literature/`") erzeugt aber einen zweiten Ordner – und der Volltext liegt danach dort, wo niemand sucht. Der Fehlalarm der letzten Runde hing an genau einer Pfadangabe, die nicht auflöste; das hier ist dieselbe Fehlerquelle, nur mit dem Nutzer als ausführender Instanz. Die Vorschläge P1-1, P1-2 und P2-2 verschärfen das, weil sie den Ordner alle drei aktiv als Ablageziel benennen.

**Zieldatei.** Eine Schreibweise festlegen – Vorschlag `sources/literatur`, weil die Dateien und die `file`-Felder schon dorthin zeigen –, `plan-modus`, `setup-check`, `pruef-modus` und `projektstruktur.md` nachziehen, `LITERATUR_ORDNER` als Rückfall stehen lassen. Das `README.md` entweder anlegen oder die Verweise darauf streichen.

**Aufwand.** Minimal (Suchen/Ersetzen) – aber vor der nächsten Nutzeranweisung erledigen, sonst entsteht der zweite Ordner.

---

## P2-3 · Ein OK-Urteil wird nie wieder angesehen – auch dann nicht, wenn seine Begründung offensichtlich nicht passt

**Beobachtung (2026-07-29).** Zwei Vittuari-Zitationen (`bdf041cb6b`, `b7402f55c9`) trugen in `quellencheck-state.json` als Begründung wortwörtlich den **Soma**-Prüftext aus derselben Sitzung vom 28.07. – inklusive Seitenangaben und Prozentwerten, die mit Vittuari nichts zu tun haben. Beim Eintragen mehrerer `--verdikt`-Aufrufe hintereinander war dieselbe `--notiz` mehrfach mitgegeben worden. Die Urteile selbst waren korrekt (am Volltext nachgeprüft: Kap. 1, Abs. 3 trägt sowohl den Haushalts-Claim als auch die Drivers/Levers-Definition), aber das war der Datei nicht anzusehen.

**Warum kein Einzelfall.** `pruefe()` überspringt jede Zitation mit Status OK oder AUSNAHME vollständig – der Volltext wird nicht geöffnet, die gespeicherte Notiz unbesehen durchgereicht (`if alt and not alle and alt.get("status") in ("OK","AUSNAHME"): … continue`). Nur `--alle` bricht das auf, und kein Audit-Umfang ruft das automatisch. Teil-Check G weist zudem nur an, offene `PRÜFEN`-Paare zu entscheiden; die OK-Tabelle liest niemand gegen. Ein einmal vergebenes OK ist damit **endgültig**, und seine Begründung ist die einzige Spur, die überlebt. Genau darauf ist die Inkrementalität ausgelegt – sie macht die Vollprüfung bezahlbar –, aber sie hat als Preis, dass ein Eintragungsfehler nie mehr auffällt. Das Muster „mehrere Urteile in einem Rutsch mit derselben Notiz" entsteht dabei nicht aus Nachlässigkeit, sondern weil die Urteile blockweise über `--paare N` abgearbeitet werden.

**Zieldatei.** `.claude/skills/_shared/scripts/check_quellentreue.py` (Verdikt-Eintragung und Bericht).

**Vorschlag, zwei kleine Wächter – beide deterministisch, kein Modellurteil:**
1. **Notiz-Dublette melden.** Taucht derselbe Notiztext bei Zitationen mit **verschiedenen** Bib-Keys auf, im Bericht als Hinweis ausgeben („Notiz identisch mit `<hash>` (`<anderer key>`) – beim Eintragen verrutscht?"). Fängt genau diesen Fehler, ohne je einen echten Fall zu blockieren: Dieselbe Begründung für zwei Zitationen **derselben** Quelle ist legitim und bleibt still.
2. **Key-Nennung in der Notiz gegenprüfen.** Nennt eine Notiz einen Autornamen, der weder im `author`-Feld des zitierten Eintrags noch im Trägersatz vorkommt, ebenfalls als Hinweis melden. Reine Zeichenkettenprüfung; hätte den Fall hier sofort gezeigt („Soma" in einer Vittuari-Notiz).

Beides sind Hinweise, keine Befunde – sie kosten keinen Score, machen den Eintragungsfehler aber sichtbar, solange er noch billig zu beheben ist.

**Aufwand.** Klein, zwei Schleifen über die bereits geladenen Urteile.

---

## Bitte manuell prüfen

1. **Figshare-Fassung von Shen et al. (2023).** Wo: `https://figshare.com/articles/journal_contribution/Influence_by_osmosis_Social_media_green_communities_and_pro-environmental_behavior/27570216`. Woran erkennbar, dass es passt: Der Eintrag muss den **Volltext** enthalten (PDF mit Fließtext), nicht nur Metadaten oder Zusatzmaterial; laut OpenAlex ist es die `submittedVersion`, die Seitenzählung weicht also von der Verlagsfassung ab. Warum nicht durch mich: Ich habe den OpenAlex-Datensatz abgefragt, nicht die Datei geöffnet – ob dort ein lesbares PDF hängt, ist damit nicht belegt.
2. **Zugang zu Wiley und Elsevier über die IU-Bibliothek.** Wo: myCampus → Bibliothek/Datenbanken, mit den DOIs `10.1111/ijcs.13038` und `10.1016/j.chb.2023.107706`. Woran erkennbar: Der Volltext öffnet sich nach Campus-Login ohne Kaufaufforderung. Warum nicht durch mich: Der Zugang hängt an einem persönlichen Login; ich kann weder prüfen, welche Lizenzpakete die IU hält, noch mich anmelden. Die Route in P1-1 Schritt 3 ist deshalb bewusst als Nutzer-Schritt formuliert und **nicht** als gesicherte Aussage über den Lizenzbestand.
3. **`tex.zugang` als BBT-Exportfeld.** Wo: Zotero-Eintrag → Feld *Extra*, danach `references.bib` nach dem Re-Export. Woran erkennbar: Im exportierten Eintrag steht eine Zeile `zugang = {…}`. Warum nicht durch mich: Ich habe den Mechanismus aus den im Projekt bereits genutzten Feldern `tex.shortauthor` und `tex.eid` abgeleitet, aber keinen Export mit einem neuen, frei gewählten Feldnamen laufen lassen. Falls BBT nur bekannte Felder durchreicht, wäre der Rückfall ein Präfix im `note`-Feld.
4. **Bezahlschranken-Hostliste aus P1-2.** Wo: `check_quellentreue.py` nach der Umsetzung, gegen die eigenen Bib-Einträge. Woran erkennbar: Kein frei zugänglicher Eintrag (MDPI, Frontiers, PLOS, `digitallibrary.un.org`) darf `ZUGANG PRÜFEN` bekommen. Warum nicht durch mich: Die Liste beruht auf den in diesem Projekt vorkommenden Verlagen plus den geläufigen Datenbanken – sie ist eine Heuristik, keine vollständige Aufzählung.
