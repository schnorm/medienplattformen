---
name: schreib-modus
description: Verfasst Kapitel wissenschaftlicher Arbeiten an der IU als LaTeX-Subsection-Dateien, basierend auf einem bestehenden kapitelplan.md. Nutzen, wenn ein Kapitelplan vorliegt und Kapitel geschrieben werden sollen – auch über mehrere Sessions verteilt, da jedes fertige Kapitel als eigene Datei gesichert wird. Wendet Zitierregeln, Voice und Claim-Regeln papiertyp-spezifisch an.
compatibility: Benötigt kapitelplan.md im Projekt-Root und references.bib mit BBT-Keys. .claude/skills/_shared/scripts/check_bib_keys.py benötigt Python 3.
---

# Schreib-Modus: Kapitel verfassen

## Voraussetzungen

- `kapitelplan.md` im Projekt-Root per Read-Tool geladen – nicht aus dem Gesprächsverlauf annehmen, auch wenn die Plan-Session kürzlich lief. **`aufgabe.md`** (falls vorhanden) für wörtliche Leitfragen und formale Vorgaben heranziehen statt des Aufgaben-PDFs.
- **Lese-Trigger Prüfer-Steuerungen**: Taucht während des Schreibens eine Frage zu Formalia, Anforderungen oder Methodik auf (z. B. „muss das zitiert werden?", „braucht es Primärdaten?"), **zuerst** `aufgabe.md` → „## Prüfer-Steuerungen" prüfen, bevor eine Regel aus `hard-rules-formal.md` oder aus dem Gedächtnis angewendet wird – die Prüfer-Anmerkungen können die Standardregel für dieses Projekt gezielt außer Kraft setzen (siehe `CLAUDE.md` → „Erst prüfen, dann behaupten").
- `references.bib` **nicht vollständig einlesen** – bei großen Zotero-Exporten ist das ein erheblicher Kontextposten. Keys werden per `check_bib_keys.py` deterministisch validiert; wird der Inhalt eines einzelnen Eintrags gebraucht (Autor, Jahr, Titel), gezielt nach dem Key greppen. BBT-Keys exakt übernehmen, **niemals erfinden**.
- **Literatur-Abgleich vor dem ersten Kapitel, das zitieren wird**: Enthält `kapitelplan.md` → „Literaturliste" oder „Zitat-Kandidaten" Paper, vorab prüfen, ob dafür überhaupt Einträge existieren – z. B. `grep -i "<Autor-Nachname>" references.bib` für jedes gelistete Paper. Fehlen Keys (oder ist die Datei leer), **vor** dem Schreiben des betroffenen Kapitels melden und Zotero-Import/BBT-Export nachholen lassen – nicht erst beim ersten `\parencite{}`-Versuch mitten im Text bemerken.
- Papiertyp bekannt → `.claude/skills/_shared/typen/<typ>.md` für Pflichtregeln, Voice, Synthese-Fragen, Claim-Regeln laden.
- `.claude/skills/_shared/hard-rules-formal.md` laden – Zitationen, LaTeX, Pronomen, Struktur, Schreibstil, Verständlichkeit (Details, die bewusst nicht in `CLAUDE.md` stehen, um Plan-Modus-Sessions schlank zu halten). Zusätzlich `.claude/skills/_shared/stilprofil.md` laden – Positiv-/Negativ-Beispiele aus real gut bzw. schlecht bewerteten Arbeiten als Stil-Kalibrierung.
- **Nicht vorsorglich laden:** `.claude/skills/_shared/zitation-sonderfaelle.md`. Erst wenn im heutigen Kapitel ein Sonderfall konkret ansteht – Sekundärzitat, persönliche Kommunikation, eigene Erhebungsdaten, Quelle ohne Seitenzahlen, Institution als Autor:in, Gesetz/Norm/Software, Übersetzung, KI-Ausgabe. Die Datei ist dafür da, nachgeschlagen zu werden, nicht mitgeschleppt zu werden.
- **`PERSISTENT.md` + `MEMORY.md`** (falls vorhanden) lesen – `[LERNEN:stil]`, `[LERNEN:struktur]`, `[LERNEN:zitation]` und `[LERNEN:prozess]`-Einträge ohne `[ÜBERHOLT]`-Markierung berücksichtigen (z. B. bevorzugte Absatzlänge, abweichende Kapitelgerüste, Workflow-Präferenzen); bei Widerspruch gewinnt `MEMORY.md`. Konsolidierungs-Hinweis: ab ~20 Einträgen mit Nutzer durchgehen.
- **`pruefbericht.md`** (falls vorhanden) lesen, wenn Kapitel mit Status ÜBERARBEITUNG NÖTIG anstehen – die dortigen Handlungsempfehlungen sind die Arbeitsliste für die Überarbeitung, nicht aus dem Gedächtnis rekonstruieren.

## Session-Start: welche Kapitel fehlen noch?

Schreib-Sessions laufen typischerweise über mehrere Tage – nicht auf Memory verlassen, um zu wissen, welches Kapitel als Nächstes dran ist. **Nur einmal beim ersten Aufruf dieses Skills innerhalb einer Session ausführen, nicht bei jeder weiteren Nachricht wiederholen** – danach reicht der bereits bekannte Stand, bis eine neue Session beginnt oder der Nutzer explizit nach dem aktuellen Stand fragt.

1. `chapters/` per Verzeichnis-Listing prüfen: welche `.tex`-Dateien existieren bereits (Dateiname = `sec:<slug>` aus dem Kapitelplan)?
2. Mit den Kapiteln aus `kapitelplan.md` abgleichen: welche fehlen noch? **Ist `chapters/` noch komplett leer** (allererster Aufruf für diese Arbeit): dem Nutzer den `pruef-modus`-Umfang „Bereitschafts-Check" vorschlagen, falls noch nicht gelaufen (mechanische Checkliste – BBT-Keys, Abhakliste/Lieferobjekte, offene Stark-Befunde, Namens-/Prüfer-Steuerungen, Papiertyp-Pflichtpunkte). Kein Zwang, nur ein Angebot; bei Ablehnung normal weiterschreiben.
3. Dem Nutzer die Lücke kurz nennen („Kapitel 1–2 sind vorhanden, Kapitel 3 (Diskussion) fehlt noch – damit weitermachen?") statt anzunehmen, das letzte besprochene Kapitel sei automatisch bekannt.
4. Falls eine bestehende `.tex`-Datei überarbeitet statt neu geschrieben werden soll: das explizit erfragen, nicht automatisch überschreiben.

**Strukturänderungen während des Schreibens**: Weicht die Umsetzung vom Plan ab (Kapitel zusammengelegt/geteilt, Subsection ergänzt/gestrichen – vom Nutzer bestätigt), wird `kapitelplan.md` **sofort im betroffenen Kapitelblock per Edit nachgezogen** (plus Statustabelle in `CLAUDE.md`), sichtbar quittiert. Sonst ist die „Dateien sind Wahrheit"-Quelle beim nächsten Sessionstart still falsch. Ist die Abweichung eine Dauer-Präferenz („bei uns immer ohne X"), zusätzlich `[LERNEN:struktur]` in `MEMORY.md`.

**Freigabepflichtige Punkte beim Abarbeiten von `AENDERUNGEN.md`/`pruefbericht.md`** (Runden- und Erledigt-Log-Konvention: `_shared/aenderungen-format.md` – beim Abarbeiten laden): Trägt ein Punkt einen Vorbehalt wie „nur mit expliziter Freigabe ändern" (z. B. weil er die Leitfrage oder ein Kernargument betrifft, siehe `CLAUDE.md` → Grundprinzipien), diesen **nicht** kommentarlos auslassen. Per `AskUserQuestion` noch in derselben Session aktiv nachfragen, bevor der nächste Schritt (Audit, Commit, PR) beginnt – nicht nur in der Session-Zusammenfassung erwähnen und die Entscheidung dem Nutzer überlassen, sie von sich aus nachzufragen.

**Keine vorsorgliche Entschärfung, solange der Satz eine Wertung deckt.** Ist eine Aussage zweifelhaft, aber nicht widerlegt, ist die naheliegende Reaktion, sie abzuschwächen und alles andere stehen zu lassen. Das ist genau dann **unzulässig**, wenn der Satz die einzige Deckung einer Tabellenwertung, einer Einstufung oder eines Lieferobjekts ist: Ein entschärfter Fließtext bei unveränderter Zelle erzeugt eine **unbedeckte Wertung** – und damit einen eigenen Audit-Befund (Self-Check: „deckt der Fließtext jede Wertung?", Teil-Check C: Tabellenwertung gegen Kriteriendefinition). Der Fehler wäre nur ausgetauscht, nicht behoben. Also: entweder verifizieren und beide Seiten zusammen anpassen, oder den Punkt offen lassen und in „Bitte manuell prüfen" führen – nicht halb ändern.

**Konsequenzkette vor der ersten Änderung bestimmen, dann in einem Arbeitsgang umsetzen.** Eine Sachkorrektur an einer Vergleichsmatrix oder Einstufung bleibt fast nie lokal. Vor dem ersten Edit deshalb sammeln: (1) die Zelle beziehungsweise Wertung selbst, (2) den Fließtextsatz, der sie deckt, (3) jeden Satz, der daraus etwas ableitet (Lücken-Aussage, Alleinstellungsmerkmal, Fazit), und (4) den **Zwilling in der Einleitung** – dieselbe Absolutbehauptung steht erfahrungsgemäß eine Ebene grundsätzlicher schon dort, wo die Arbeit ihre Lücke begründet. Erst dann ändern, alles zusammen. Zwei Gründe: Ein Zwischenstand, in dem Kapitel 1 der präziseren Aussage in Kapitel 2 widerspricht, ist ein Konsistenzbefund; und trägt eine der Folgestellen ein Kernargument, braucht **der ganze Gang** eine `[FREIGABE]`, nicht nur die letzte Stelle. Die Kette im Abarbeitungsvermerk festhalten, damit ein späteres Delta-Re-Audit sie nachvollziehen kann.

### Ein Kapitel = eine Subsection-Datei pro Slug; Master bindet Subsections

Pro Kapitel aus `kapitelplan.md` gibt es eine Subsection-Datei `chapters/<kap>/<nn>_<slug>.tex`, die mit `\subsection{...}\label{sec:<slug>}` beginnt. Bei Kapiteln mit **mehreren eigenständigen Unterkonzepten mit jeweils eigenem Kernargument** (typisch beim Theorie-Kapitel mit 2–3 Konzepten, siehe `typen/<typ>.md`) bekommt jedes Unterkonzept eine eigene Datei `<nn>_<slug>.tex` im selben Kapitelordner. Bei Unsicherheit, ob ein Kapitel eine oder mehrere Dateien braucht: den Kapitelplan prüfen, nicht raten – im Zweifel eine Datei, nur bei klar getrennten Unterkonzepten aufteilen. Der **Master** `chapters/<kap>/<kap>.tex` öffnet die Section und bindet die Subsection-Dateien per `\input{}` ein.

**Sichtbarkeitspflicht**: Nach jeder gespeicherten `.tex`-Datei im Chat kurz quittieren, z. B. „✅ Gespeichert: chapters/theorie/konzept-a.tex" – nicht nur den Kapiteltext im Chat zeigen und stillschweigend annehmen, dass die Datei geschrieben wurde. **Zusätzlich** die entsprechende Zeile in `CLAUDE.md` → „Aktueller Projektstatus" auf FERTIG setzen (bestehende Zeile überschreiben, nicht anhängen) und kurz mitquittieren.

## Kürzen ist ein Arbeitsschritt mit Verfahren, nicht freihändig

Kürzungen entstehen aus einem Audit-Befund („Umfang überschritten") und wurden bisher freihändig ausgeführt – kein Verfahren, keine Abnahme, keine Prüfung danach. Belegt aus einem realen Projekt: Vier Runden entfernten über 1.000 Wörter, und der Nutzer meldete anschließend „liest sich zu gekürzt". Drei gebrochene Bezüge waren jeder einer Kürzungsrunde zuzuordnen und haben **Audits mit 100/100 überlebt** – weil geprüft wird, was der Diff zeigt, und der Schaden im Satz *davor* entsteht.

**Verbindliche Reihenfolge:**

1. **Erst die Layout-Hebel ausschöpfen, dann kürzen.** Eine Seite zu viel ist häufiger ein Layout- als ein Textmengenproblem. Beide Hebel sind reversibel und kosten keine inhaltliche Substanz – sie kommen deshalb vor jeder Wort-Kürzung, in dieser Reihenfolge:
   - **Float-Platzierung und Weißraum.** `[H]` an einer großen Tabelle schiebt sie auf die nächste Seite und lässt die vorige halb leer. Gemessen wurden 389 pt und 136 pt auf zwei Seiten – zusammen mehr, als die Extraseite an Text trug. Der Prüfbericht nennt diese Reserve vor den Kürzungsstellen (`pruef-modus` → Teil-Check D).
   - **Tabellen- und Abbildungsschrift.** Die IU-Richtlinien erlauben sie ausdrücklich kleiner: „Die Schrift in den Tabellen und Abbildungen kann bei Bedarf in einer kleineren Größe als 11 Pt. gestaltet werden." Regelstufe ist `\footnotesize`; `\scriptsize` nur für wirklich dichte Tabellen – bei 11-Pt.-Grundschrift sind das rund 8 Pt., und das liest sich als gequetscht. `main.tex` setzt die **Captions** bereits auf `\footnotesize`; der **Tabelleninhalt** ist davon unberührt und muss je Tabelle gesetzt werden.
2. **Kandidaten nach Klasse ordnen, in dieser Reihenfolge abarbeiten:**
   - **Klasse 1 – inhaltliche Dubletten:** dieselbe Aussage zum zweiten und dritten Mal, wiederholte Vorbehalte, Dubletten zwischen Reflexion und Fazit.
   - **Klasse 2 – Bindungsmasse:** Übergangssätze, Absatzöffner, Ankündigungen, Rückverweise. **Zuletzt und nur, wenn Klasse 1 erschöpft ist.** Das Kriterium „sagt der Folgesatz auch" ist für Fakten richtig und für Text falsch: Anschlüsse sind *per Definition* redundant, und genau sie machen einen Absatz lesbar. Wer nach dem Kriterium allein vorgeht, entfernt bevorzugt die Bindungsmasse, weil sie es am saubersten erfüllt.
3. **Nach jeder Streichung den ganzen Absatz plus den folgenden neu lesen** – nicht den Diff. Im Diff sieht jede einzelne Streichung sauber aus.
4. **Je Streichung notieren, ob der gestrichene Satz etwas geliefert hat, das anderswo gebraucht wird** – zweierlei:
   - ein **Bezugswort** für einen späteren Anschluss mit „es", „beide", „daraus", „diese", „dort", „ebenso". `check_formalia.py` meldet absatzinitiale Anaphern als `ANAPHER` – das fängt den häufigsten Fall, ersetzt aber das Nachlesen nicht.
   - die **einzige Erklärung eines Fachbegriffs**, der anderswo weiterverwendet wird. Die Signale stehen im gestrichenen Satz selbst: „also", „d. h.", ein erklärender Doppelpunkt, ein Relativsatz direkt nach dem Begriff. Realfall: „Nudge" wurde über drei Kürzungsrunden von einer vollen Erklärung auf „einen belegten Nudge-Typ" gestrafft und stand danach an fünf Stellen unerklärt im Text – kein bewusster Verzicht, sondern der Nebeneffekt einer Satzstraffung. Ein Voll-Audit hatte den Begriff vorher ausdrücklich als vorbildlich eingeführt gelobt.

## Was beim Kürzen geschützt ist

Das Audit schlägt Kürzungen vor, sobald `check_umfang.py` über der Zielgröße meldet. Diese Liste sagt, was dabei **nicht** angetastet wird – ohne sie greift Kürzen bevorzugt die dichtesten und damit tragenden Sätze an, weil die am meisten Wörter pro Aussage binden. Belegt: Eine Kürzungsrunde riss die Mitigationsschicht aus einer Limitation und kostete im folgenden Audit −15 Punkte.

**Vor jeder Streichung oder Straffung zwei Fragen beantworten und im Abarbeitungsvermerk festhalten:**

1. **Ist dieser Satz die einzige Fundstelle?** Betroffen sind Schlüsselbegriffe aus `aufgabe.md`, Pflichtschichten (Limitation: warum · Mitigation · Ausblick), Definitionen, Lieferobjekte und beanspruchte Innovationen. Ist er es, wird ein anderer Posten gesucht – auch wenn dieser weniger Wörter bringt. Prüfen per `grep -c "<Begriff>" chapters/`.
2. **Enthält er ein Hedge, das beim Straffen wegfällt?** `oft`, `häufig`, `in der Regel`, `kann`, `deutet darauf hin`, `tendenziell`. Ein gestraffter Satz ohne das Hedge ist keine kürzere Aussage, sondern eine **stärkere** – aus einer vorsichtigen Feststellung wird eine absolute. Hedge im gekürzten Satz erhalten.

**Erste Kürzungsreserve sind stattdessen:** mehrfach ausformulierte Kernbefunde (dritte Nennung und weitere), wiederholte Vorbehalte, Ankündigungs- und Wegweisersätze, Dubletten zwischen Reflexion und Fazit.

## Text-Bild-Lücken: zwei Lösungen, nicht drei

Meldet die Gegenlesung oder das Audit „Der Text behauptet X, die Abbildung zeigt X nicht", gibt es genau **zwei** zulässige Reaktionen: die **Abbildung ergänzen** oder die **Behauptung streichen**.

Die dritte, naheliegendste Option – die Behauptung präziser formulieren und die Abbildung so lassen – ist **unzulässig**. Sie schließt die Lücke nicht, sondern verwandelt eine Auslassung in eine überprüfbare Falschaussage: Vorher fehlte etwas, nachher steht etwas Widerlegbares da, und der Prüfer sieht die Abbildung zwei Seiten später. Belegt aus einem realen Projektbericht, wo der Zusatz „Erreichbar ist der Bereich über die Startseite" vier Tage lang auf einen Zugang verwies, den kein Screen zeigte.

Wird die Abbildung erst später geliefert, bleibt der Textzusatz bis dahin **draußen** – nicht als Vorgriff hinein und später prüfen.

**Wird eine Abbildung geändert, ist die Änderung erst mit dem Text fertig.** Eine Abbildung wird an einer Stelle bearbeitet, aber an mehreren beschrieben – typischerweise in der Caption, im einleitenden Satz davor und in einem Rückverweis im Fazit. Deshalb nach jeder Bildänderung über das Label suchen und **jede** Fundstelle einzeln gegen das neue Bild lesen:

```bash
grep -rn "fig:mein-label" chapters/ pages/
```

Der Grep findet die `\ref`-Verweise; die Caption steht in derselben `figure`-Umgebung wie das Label und wird mitgeprüft. Beschreibende Sätze ohne `\ref` findet er nicht – dafür zusätzlich nach ein bis zwei charakteristischen Wörtern aus der Caption suchen. Das ist der übliche Weg, auf dem eine Abbildung stillschweigend aus dem Text herausläuft: Sie wird verbessert, und der Rückverweis zwei Kapitel später beschreibt weiter die alte Fassung.

**Umgekehrt gilt: Ein Satz über ein bestehendes Bild wird aus dem Bild formuliert, nicht aus dem Prompt.** Wer beschreibt, was eine Abbildung zeigt, erlaubt oder ermöglicht, öffnet die Datei per `Read` – auch dann, wenn der Erzeugungs-Prompt danebensteht und die Frage scheinbar beantwortet. Der Prompt beschreibt die **Absicht**, nicht zuverlässig das **Ergebnis**; generierte Abbildungen lassen regelmäßig Elemente weg, die im Prompt standen. Diese Prüfung gehört an den Schreibzeitpunkt und nicht erst in Gegenlesung oder Audit: Dort steht der Satz bereits im fertigen Absatz, und die Korrektur kostet eine Überarbeitungsrunde.

## Begriffsersetzungen sind erst mit der Einführung fertig

Ersetzt ein Punkt aus `AENDERUNGEN.md` oder `pruefbericht.md` einen Begriff durch einen anderen („Nutzer" → „Anwendende", „Effizienz" → „Bearbeitungsdauer"), wird der neue Begriff an genau der Stelle eingesetzt, die der Befund nennt – und steht danach ohne Einführung im Text. Ein Fachbegriff, der genau einmal vorkommt, wirkt wie ein Zitat aus einer anderen Arbeit.

**Nach jeder Ersetzung:**

```bash
grep -rn "<neuer Begriff>" chapters/ pages/
```

Weniger als zwei Fundstellen heißt: Der Begriff ist nicht eingeführt. Dann eine von zwei Entscheidungen treffen und im Abarbeitungsvermerk festhalten – den Begriff **bei der ersten Nennung definieren** und danach konsistent weiterverwenden, oder die **Ersetzung zurücknehmen**, wenn das Kapitel dafür keinen Platz hat. Was nicht geht, ist ihn stehen zu lassen: Das Audit liest ihn als unerklärten Fachbegriff (`hard-rules-formal.md` → „Fachwörter: benutzen UND erklären"), und für die prüfende Person ist er ein Bruch mitten im Kapitel.

Umgekehrt gilt dasselbe für den ersetzten Begriff: Steht er noch an anderen Stellen, führt die Arbeit ab sofort zwei Wörter für dieselbe Sache – auch das per Grep prüfen, bevor der Punkt als erledigt vermerkt wird.

## Eine Änderung ist erst fertig, wenn ihre Wiederholungen nachgezogen sind

Die beiden Abschnitte davor sind Sonderfälle einer Regel: Eine Aussage steht selten nur an einer Stelle. Wer sie an ihrem Ursprung ändert, hat die Arbeit halb getan – die Wiederholungen stehen weiter da und sind ab sofort falsch. Drei Formen, jede real gefunden, keine davon durch ein Skript. Die Konsequenzketten-Regel weiter oben ist das Gegenstück davor: Sie bestimmt die betroffenen Stellen **vor** dem ersten Edit, dieser Abschnitt prüft **nach** der Änderung nach.

**1. Die Reparatur eines Befunds ist halb.** Ein Fix-Vorschlag aus dem Bericht ist eine **Hypothese, keine abgenommene Lösung** – auch wenn er als „empfohlen" markiert und wörtlich ausformuliert ist. Nach dem Umsetzen eines Punktes aus `AENDERUNGEN.md` oder `pruefbericht.md` deshalb den **ganzen Satz plus den folgenden** neu lesen, nicht nur den eingefügten Halbsatz – dieselbe Regel, die dieser Skill für Streichungen schon kennt („nach jeder Streichung den ganzen Absatz plus den folgenden neu lesen"). Dabei zweierlei prüfen:

- **Blieb eine zweite, gleichartige Behauptung unmarkiert?** Realfall: Ein Befund verlangte einen Übertragungsvorbehalt, er wurde ergänzt („bleibt eine Annahme dieser Arbeit") – und im selben Satz blieb die ebenso unbelegte Gleichsetzung zweier Erhebungsformate als Faktum stehen. Eine gehedgte Unsicherheit zieht den Blick von der danebenliegenden ab. Deshalb bei „bleibt eine Annahme", „ist nicht belegt", „lässt sich nicht zeigen" den Satz **zu Ende** prüfen, nicht bis zum Hedge.
- **Hat der Fix das Problem behoben oder nur umgedreht?** Besonders bei Zahlen: Eine Zahl im Ankündigungssatz bezieht sich zugleich auf die Sache **und** auf die Aufzählung, die syntaktisch folgt. Realfall: Aus „die drei … Zwecke" wurde „zwei der drei … Zwecke" – danach stimmte die Zahl mit der Sache überein und nicht mehr mit den drei Gliedern nach dem Doppelpunkt. Wer nachzählt, findet in beiden Fassungen eine Differenz. Die tragfähige Lösung zählte gar nicht mehr, sondern benannte die Glieder.

**2. Ein `\autoref` beschreibt sein Ziel nicht mehr.** Paraphrasiert ein Rückverweis eine Aussage aus einem anderen Abschnitt – statt nur auf Abbildung oder Tabelle zu zeigen –, die Zielstelle aufschlagen und die dort verwendete **Terminologie** mit der Paraphrase abgleichen. Maschinell greift dafür `check_autoref.py`: Es meldet das Paar, sobald sich die Zielstelle bewegt hat – die Terminologie abgleichen muss aber ein Lesedurchgang, und zwar dieser hier. `check_quellentreue.py` sieht nur Sätze mit `\cite`, die `AUTOREF`-Prüfung in `check_formalia.py` nur, ob das Sprungziel überhaupt existiert. Realfall: Der Rückverweis sprach vom „Unterschied zwischen Teilnehmenden und Nichtteilnehmenden", die Zielstelle belegte einen Unterschied zwischen Viel- und Wenigspielenden.

**3. Unverlinkte Prosa-Wiederholungen veralten still.** Ändert sich ein Plan, ein Vorgehen oder eine Entscheidung, die betroffenen Begriffe über `chapters/` greppen und **jeden** Treffer lesen – Diskussion, Fazit und Limitationen als Pflichtziel:

```bash
grep -rn "Nutzertest\|Prototyp\|Vortest" chapters/
```

Solche Stellen tragen weder `\ref` noch `\autoref`; sie wiederholen die Sache in eigenen Worten und sind über die Label-Suche unauffindbar. Die Technik steht schon im Abschnitt zu geänderten Abbildungen („zusätzlich nach ein bis zwei charakteristischen Wörtern aus der Caption suchen") – hier gilt sie für Fakten statt für Bilder. Realfall: In der Durchführung kam ein zweiter Testtermin dazu; das Fazit sprach weiter von „einem realen Nutzertest", und die Limitationen empfahlen noch als Ausblick, was inzwischen geplant war.


## Ablauf pro Kapitel

1. Kapitelplan lesen – Kernargument, Belege, Wortzahl, **Slug** (`sec:<slug>`), geplante Subsections **mit Inhaltspunkten und Argumentationsfluss** aus dem Plan. Die Inhaltspunkte sind der Schreibleitfaden pro Subsection: Jeder Punkt muss im fertigen Text erkennbar vorkommen – als eigener Absatz, als Teilaussage oder als Beispiel. Reihenfolge der Punkte darf angepasst werden, keiner darf stillschweigend wegfallen. **Bereits geschriebene Kapitel nicht „zur Konsistenz" komplett laden** – die Argumentationslinie steht im Kapitelplan; für den Übergang genügt der Schlussabsatz der letzten Subsection-Datei des Vorkapitels (Read mit offset ans Dateiende).
2. **Faktenbasis prüfen:** Weist der Kapitelblock „eigene Recherche" aus und fehlt ein Rechercheprotokoll, **vor dem Schreiben** melden und die Recherche nachholen oder vom Nutzer freigeben lassen. Jede Einzelbehauptung ohne Beleg oder Protokoll bekommt im `.tex` einen Marker `% UNVERIFIED: <was genau zu prüfen ist>`. Beruht ein Kapitel auf eigener Erhebung, gehört das Protokoll als Anhang in die Arbeit – es ist ein Lieferobjekt, kein internes Arbeitspapier.
3. **Ersatzentscheidungen:** Betrifft das Kapitel eine Teilaufgabe, für die `aufgabe.md` → „Ersatzentscheidungen" einen Eintrag führt, wird die Begründung **als eigener Absatz ausgeschrieben** – die vier Angaben (Versuch, Hinderungsgrund, geprüfter Minimalersatz, Folgeschritt). Ein Nebensatz in der Einleitung genügt nicht.
3b. **Tragende Belege vor dem Formulieren am Volltext lesen – nicht erst danach prüfen.** Betroffen sind die Belege, an denen das **Kernargument** der Subsection hängt, sowie alle Fundstellen, die der Plan als `[zitiert: <key>, S. ?]` markiert (Fragezeichen = Seitenzahl war geschätzt). Für jeden davon die zitierte Seite ziehen und den Satz **aus dieser Seite heraus** formulieren:
   `python .claude/skills/_shared/scripts/check_quellentreue.py --seite <key> <seitenzahl>`
   Das sind pro Kapitel typischerweise zwei bis vier Belege, nicht alle. Für die übrigen bleibt der Lauf am Kapitelende (Schritt 8) die Absicherung. Grund für die Zweiteilung: Eine Aussage, die schärfer formuliert ist als ihre Quelle, lässt sich beim Schreiben in Sekunden vermeiden und kostet nach dem Audit eine Überarbeitungsrunde – aber jede Seite vorab zu laden, sprengt die Schreib-Session.

- **Tatsachen über die Außenwelt gehören ebenfalls vor das Formulieren – und zwar in Sichtungskapiteln.** Schreibt das heutige Kapitel über reale Produkte, Anbieter, Institutionen oder Marktlagen, ohne dafür zu zitieren (weil es die **eigene Sichtung** ist), dann wird jede überprüfbare Angabe **beim Schreiben** verifiziert, nicht im Audit. Der Grund ist der Zeitpunkt, nicht die Gründlichkeit: Wer gerade sechs Plattformen ansieht, hat sie im Browser offen; ein Audit Monate später hat das nicht mehr und verlässt sich auf das Gedächtnis. Belegte Fälle: eine Ministeriumsumbenennung nach einem Regierungswechsel und eine falsch beschriebene Konkurrenzfunktion – beide standen bis zu einem eigens angeforderten Faktencheck im Text, weil kein Teil-Check sie sehen konnte.
  **Das Kapitel als Sichtung deklarieren**, damit der Audit die Stellen wiederfindet: eine Kommentarzeile am Dateianfang, `% SICHTUNG: eigene Plattformsichtung 07/2026, keine Zitationspflicht`. `check_formalia.py` listet daraufhin die Tatsachenbehauptungen dieser Datei als AUSSENWELT-Block – und **nur** dieser Dateien: Ohne die Deklaration schweigt der Check, sonst träfe er halbe Kapitel. Zusätzlich gehört das Sichtungsdatum in den Text (Methodensatz), denn eine Sichtung ohne Datum ist nicht nachvollziehbar.

   **Fehlt der Volltext eines tragenden Belegs, wird der Satz NICHT aus dem Abstract formuliert.** Das ist der stille Weg, auf dem ein ungedeckter Claim entsteht – und genau der, den Teil-Check G später als `CLAIM SCHÄRFER` findet, dann aber mit fertigem Text ringsum. Drei zulässige Wege, je nach Lage: den **Volltext jetzt beschaffen** (das Urteil aus dem Plan nennt die Route), das **Argument auf eine andere Quelle stellen**, oder die **Aussage auf das zurücknehmen, was ohne diesen Beleg gedeckt ist**. Welcher Weg gewählt wurde, gehört in den Kapitelvermerk.
4. Subsection-Datei schreiben – beginnt mit `\subsection{...}\label{sec:<slug>}`.
5. Hard Rules aus `.claude/skills/_shared/hard-rules-formal.md` beachten (Zitationen, Eigene Darstellung, Pronomen, Akronyme, Labels, Floats).
6. **Zitier-Klassifikation aus dem Plan übernehmen**: Jede Quelle im Kapitelblock trägt ein Klassifikations-Suffix (`[zitiert]` / `[eigene Analyse]` / `[unzulässig – ersetzt durch ...]`, siehe `plan-modus` → Schritt 3). Nur `[zitiert]`-Quellen bekommen `\parencite{}`; `[eigene Analyse]`-Quellen bekommen `\quelle{Eigene Darstellung.}` bzw. eigene Beobachtung im Fließtext – **kein** `\parencite{}`, **kein** erfundener BBT-Key dafür. Fehlt die Klassifikation im Plan, vor dem Schreiben der betroffenen Stelle nachfragen statt zu raten. **Fehlt eine Quelle in `references.bib`: Platzhalter-Kommentar `% TODO-QUELLE: <was fehlt>` setzen und den Nutzer bitten, sie über Zotero zu importieren – nie einen Key raten.** `check_formalia.py` meldet beide Arbeitsmarker (`TODO-QUELLE`, `UNVERIFIED`) mit Datei und Zeile; vor der Abgabe muss jeder davon geklärt oder die Stelle gestrichen sein. Vor jedem `\parencite{}`: Key gegen `references.bib` validieren – `python .claude/skills/_shared/scripts/check_bib_keys.py references.bib <key1> <key2> ...` oder, für eine ganze Datei, `python .claude/skills/_shared/scripts/check_bib_keys.py references.bib --tex chapters/<kap>/<nn>_<slug>.tex` (vom Projekt-Root aus aufrufen).
7. Nach dem Speichern **ein** Sammelaufruf statt mehrerer Einzelläufe: `python .claude/skills/_shared/scripts/check_all.py --kapitel chapters/<kap>` – fährt Key-Validierung, Formalia und Bib-Hygiene in einem Durchgang. Mechanische Verstöße sofort fixen, statt sie dem Prüf-Modus zu überlassen. Neben den bekannten Prüfungen meldet er drei Dinge, die früher Handarbeit waren: **`\parencite` ohne Stellenangabe** (die IU verlangt sie auch bei indirekten Zitaten), **Floats ohne `\quelle{}`** und **Kapitel mit genau einem Unterpunkt**. **Wurde stattdessen eine Datei unter `pages/` geschrieben** (typisch `pages/appendix.tex`), diese gezielt prüfen: `check_formalia.py pages/appendix.tex` – auch Anhangstext ist selbst verfasster Text und läuft sonst durch keine mechanische Prüfung.
8. **Quellentreue der neuen Zitationen prüfen – Pflicht, nicht optional:** `python .claude/skills/_shared/scripts/check_quellentreue.py --datei chapters/<kap>`. Das Skript vergleicht jeden Trägersatz mit dem Volltext der zitierten Seite und meldet Wortlautübernahmen (≥ 7 Wörter am Stück), abweichende wörtliche Zitate und falsche Seitenangaben. Befunde **sofort** beheben – umformulieren, Seitenangabe korrigieren oder als `\enquote{}` kennzeichnen. Zitationen mit Status `PRÜFEN` mit `--paare 8` abrufen und inhaltlich entscheiden, ob die Seite die Aussage deckt und die Paraphrase nicht schärfer ist als die Quelle; Urteil mit `--verdikt <hash>=OK --notiz "…"` eintragen. Der Quellenausschnitt ist auf den Bereich um die Kernbegriffe gekürzt und weist das aus – reicht er für ein Urteil nicht, `--paare N --voll` oder gezielt `--seite <key> <n>` nachladen, **nicht** auf zu wenig Kontext hin mit OK quittieren. Ein Kapitel gilt erst als geschrieben, wenn dieser Lauf durch ist. Details zu Sonderfällen (Seitenversatz, Scans, Webquellen): `pruef-modus` → Teil-Check G.
9. Nach jedem Kapitel: Self-Check (siehe unten).

## LaTeX-Schreibregeln (Kurzreminder – Details in `.claude/skills/_shared/hard-rules-formal.md`)

- Pro Hauptkapitel gibt es eine **Master-Datei** (`chapters/<kap>/<kap>.tex`, öffnet die Section mit `\section{...}\label{sec:<kap>}`) und je Subsection eine eigene Datei (`chapters/<kap>/<nn>_<slug>.tex`). Die Subsection-Datei beginnt mit `\subsection{...}\label{sec:<slug>}` – **keine Chapter-Wrapper, keine `\input{}` in der Subsection-Datei selbst**. Der Master bindet die Subsections per `\input{}` ein.
- Zitation: `\parencite[S. X]{key}`. Sekundärzitate vermeiden. Direkte Zitate > 40 Wörter: `\begin{blockzitat}` (in `main.tex` definiert), nicht `\enquote{}`.
- Eigene Abb./Tab.: `\quelle{Eigene Darstellung.}` (Makro aus `main.tex`) unter Bild/Tabelle, kein `\cite{}`.
- Akronyme: `\ac{KÜRZEL}` (Definition in `pages/acronyms.tex` per `\acro{}`). Cross-Ref: `\autoref{sec:label}`. Anführungszeichen: `\enquote{}`.
- Float `[H]`, Caption vor `\label{}`. Tabellen `booktabs`. Kompakte Listen: `itemize[nosep]` (enumitem).
- Keine Änderungen an `main.tex` / `pages/cover.tex`. Projektangaben (Titel, Modul, Tutor:in …) nur in `pages/meta.tex`.
- **Diagramme**: kein Mermaid. Stattdessen direkt `tikzpicture` in der `.tex`-Datei mit den **vordefinierten Styles aus `main.tex`** (`\node[box]`, `\node[decision]`, `\draw[arr]`, `\draw[dashedarr]`) – Styles nicht pro Diagramm neu definieren. Caption + `\label{fig:...}` darüber, `\quelle{...}` darunter. Datendiagramme als `pgfplots`-`axis`.
- Wenn Subsection oder Subsubsection die halbe Seite Regel verletzt, Umsetzbarkeit als `\paragraph{}` prüfen. Wenn möglich: Trotzdem als eigene Datei wie Subsection, damit Kapitelplan mit Latex Dateistruktur konsistent bleibt. Wenn nicht möglich: User explizit fragen.

## Schreibstil

Maßgeblich sind `_shared/hard-rules-formal.md` → Schreibstil + Verständlichkeit und `_shared/stilprofil.md` – beide sind laut Voraussetzungen ohnehin geladen, die Regeln werden hier bewusst nicht dupliziert. Sie gelten zusätzlich zu den Voice-Vorgaben in `typen/<typ>.md`, nicht anstelle davon. Bei Zielkonflikten: einfache Sprache vor akademischem Klang.

## Inhaltliche Qualitätsregeln (nur die für den aktuellen Papiertyp laut `typen/<typ>.md` pflichtigen anwenden)

- **Absatzlogik (IU-Pflicht, alle Typen)**: Jeder Absatz folgt dem Muster (1) Hauptaussage identifizieren und an den Anfang stellen, (2) erläutern, diskutieren, mit Nebenaussagen ergänzen, (3) Schlüsse ziehen, die zum nächsten Absatz überleiten. Kein Absatz endet mit reiner Beschreibung oder Selbstzweck-Aufzählung.
- **These erkennbar**: Kapitel trägt die Gesamtaussage mit, nicht nur Beschreibung. Kein Kapitel endet mit reiner Aufzählung – Syntheseleistung („Diese Arbeit schließt daraus …").
- **Gegenargumente**: stärkstes Gegenargument pro zentralem Argument reflektieren und entkräften.
- **Ergebnisse ≠ Interpretation** (nur Seminararbeit, nur empirisch): Befunde zuerst rein berichten (FACTUAL, `\parencite{}` für Methodik/Instrumente), Interpretation folgt (ARGUMENTATION). Auch bei zusammengeführtem Kapitel klar getrennt.
- **Limitationen dreischichtig**: (1) warum Limitation, (2) Mitigation, (3) wie zukünftige Forschung sie überwinden kann.
- **Aktualität/Zeitbezug**: in der Einleitung, sofern laut Typ-Datei pflichtig.

## Iterationsrhythmus (Schreiben ↔ Prüfen)

Skripte + Self-Check sind das Qualitätstor **pro Kapitel** – ein Voll-Audit nach jedem Kapitel ist nicht vorgesehen (lädt jedes Mal Typ-Datei, Hard Rules und alle Kapitel neu). Stattdessen:

1. **Nach dem ersten Hauptteil-Kapitel**: dem Nutzer ein **Kapitel-Audit** vorschlagen („Audit Kapitel: <name>", siehe `pruef-modus` → Audit-Umfänge). Das erste Kapitel prägt Zitierweise, Stil und Absatzlogik – ein systematischer Fehler, der hier gefunden wird, kopiert sich sonst in alle Folgekapitel. **Einmaliges Angebot:** Ist das erste Hauptteil-Kapitel bereits vorbei (egal ob das Audit damals durchgeführt wurde oder nicht), wird es nicht erneut vorgeschlagen – sonst verdrängt es den eigentlich fälligen Schreibschritt.
2. Danach die restlichen Kapitel schreiben. Solange noch eine Komponente in der Statustabelle nicht FERTIG ist, ist der nächste Schritt immer ein Schreibschritt, kein Audit.
3. **Sind alle Kapitel FERTIG, ist der nächste Schritt die Prüfer-Gegenlesung – nicht das Voll-Audit und nicht der Stresstest.** Reihenfolge und Begründung der ganzen Prüfkette stehen in `CLAUDE.md` → Workflow-Fahrplan und Kompakt-Prüfkette; **hier bewusst nicht wiederholt**, damit sie nicht an zwei Stellen auseinanderlaufen – genau das war passiert: Diese Zeile nannte noch „beide Runden", als der Faktencheck längst dazugehörte. Für die Schreib-Sitzung zählt nur: Gegenlesung, Gesamt-Stresstest und Faktencheck sind reine Lese-Schritte, sie laufen **vor** der ersten Überarbeitung, und abgearbeitet werden alle offenen Runden gemeinsam in einer Sitzung.
4. Überarbeitung entlang `pruefbericht.md` in eigenen Sessions; danach Re-Audit als Delta (nur FAIL-Punkte), kein erneutes Voll-Audit – das kommt erst als Abgabe-Audit.

**Nächsten Schritt nie aus dem Gedächtnis nennen.** Die im Chat empfohlene nächste Aktion wird aus der Reihenfolge in `kapitelplan.md` → „Nächste Schritte" und der Statustabelle in `CLAUDE.md` abgelesen und muss mit der „Aktuellen Richtung" übereinstimmen, die dieselbe Nachricht in `CLAUDE.md` schreibt. Weicht die Empfehlung im Chat von der Datei ab, gilt die Datei – dann die Empfehlung korrigieren, nicht die Datei.

## Self-Check nach jedem Kapitel

- [ ] `check_quellentreue.py` für dieses Kapitel gelaufen, keine offenen Befunde (WORTLAUT, ZITAT WEICHT AB, SEITE VERDÄCHTIG)?
- [ ] `check_formalia.py` gelaufen und 0 FEHLER? (deckt Pronomen, Anführungszeichen, quote-Env, `[H]`, Caption-Reihenfolge, `\underline`, `\include`, Blockzitat > 40 Wörter, ½-Seiten-Heuristik, Überschriften-Dopplung sowie die Stil-Heuristiken – Satzlängen, Meta-Verben/Nominalstil, Dreier-Aufzählungen, Absatz-Gleichförmigkeit, Fragesätze, Wortdopplungen – mechanisch ab; nicht erneut manuell prüfen)
- [ ] Kernargument aus dem Kapitelplan umgesetzt?
- [ ] Alle **Inhaltspunkte** aus dem Kapitelplan für diese Subsection im Text erkennbar umgesetzt? Kein Punkt stillschweigend ausgelassen?
- [ ] Alle Belege mit korrekten `\parencite{}`, per Skript gegen `references.bib` validiert?
- [ ] Eigene Abb./Tab. mit `\quelle{Eigene Darstellung.}`?
- [ ] Max. 3 Kapitelstufen?
- [ ] Akronyme per `\ac{}`? Labels konsistent (`sec:`, `fig:`, `tab:`)?
- [ ] Absätze pro Subsection im Richtwert laut `typen/<typ>.md`?
- [ ] Hauptkapitel schließt mit eigener Syntheseleistung?
- [ ] Für den Papiertyp laut `typen/<typ>.md` → Pflichtregeln pflichtige Punkte erfüllt (Gegenargument, Limitationen dreischichtig, ggf. Ergebnisse≠Interpretation)?
- [ ] Einleitung: Forschungslücke und – falls laut Typ-Datei pflichtig – Aktualität/Zeitbezug enthalten?
- [ ] Keine Anti-KI-Stil-Verstöße (Gedankenstrich-Füller, Floskel-Öffner, Klischee-Übergänge, unbegründete Absicherungsfloskeln, Kontrastfiguren inkl. Tarnformen, Pointen-Schlusssätze, Doppelpunkt-/Signalwort-Häufung, Staccato-Ketten)?
- [ ] Verständlichkeit: Sätze kurz und klar, Fachbegriffe bei erster Nennung erklärt, kein Nominalstil/keine stilistische Verdichtung – würde ein Laie jeden Absatz beim ersten Lesen verstehen?
- [ ] Alle diesem Kapitel zugewiesenen **Lieferobjekte** existieren tatsächlich als Datei beziehungsweise als `figure`/`table`/Anhangseintrag – nicht nur im Fließtext erwähnt? **Sonderregel:** Behauptet der Text die Existenz eines Artefakts („als Prototyp diente …", „das Formular gliedert …", „die Erhebung ergab …"), muss dieses Artefakt gezeigt oder im Anhang beigelegt sein.
- [ ] Alle diesem Kapitel zugeordneten Einträge der **wörtlichen Abhakliste** kommen im Text tatsächlich vor – Schlüsselbegriffe wörtlich, Berichtsinhalte als erkennbarer zusammenhängender Ort, `[VERENGT]`-Begriffe mit ausgeschriebener Begründung?
- [ ] Bei selbst definierter Bewertungstabelle: **jede Zelle spaltenweise gegen die Rubrik-Karte geprüft** – liegen alle Zeilen eines Kriteriums auf derselben Achse, und deckt der Fließtext jede Wertung? **Gegenprobe:** Bekommt das Objekt, gegen das sich die These richtet, durchweg die schlechtesten Wertungen? Dann ausdrücklich einräumen, worin seine reale Stärke besteht.
- [ ] Erhebt das Kapitel einen Einwand gegen die eigene Position oder benennt es eine Bedingung des eigenen Gelingens: wird sie im selben oder in einem späteren Kapitel beantwortet oder ausdrücklich als Limitation geführt – statt nur genannt zu werden?
- [ ] Alle nicht-belegten Eigenrecherche-Behauptungen entweder recherchiert (Protokoll im Kapitelplan **und** im Anhang) oder mit `% UNVERIFIED:` markiert?
