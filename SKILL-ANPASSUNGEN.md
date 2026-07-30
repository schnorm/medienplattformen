# SKILL-ANPASSUNGEN.md

Offene Änderungsvorschläge an Skills, Skripten und `CLAUDE.md`. **Kein Abgabebestandteil.**

Neu angelegt 2026-07-30, nachdem die vorherigen Punkte (P1–P18) übernommen und die Datei geleert wurde.

**Status:** 13 Punkte OFFEN.

---

## P31 — Der Cold-Read-Modus (P28) hat kein Session-Ende-Ritual, dadurch bleibt die Statustabelle in CLAUDE.md hinter ad-hoc-Sessions zurück

**Konkreter Fall (2026-07-30, Ende dieser Session).** Diese gesamte Session lief als freier Dialog (Cold-Reading, siehe [[P28]]), ohne einen der bestehenden Skills (`schreib-modus`, `pruef-modus` etc.) aufzurufen. Jeder dieser Skills trägt ein eigenes „Session-Ende-Ritual" (Checkpoint, Statustabelle aktualisieren, „Aktuelle Richtung" setzen, siehe `CLAUDE.md` → Session-Regeln Punkt 3) – der Cold-Read-Modus nicht. Ergebnis: Nach rund 15 Textänderungen über fünf Kapiteldateien blieb die Statustabelle in `CLAUDE.md` unangetastet, bis der Nutzer selbst danach fragte.

**Warum kein Skript/Skill das auffängt.** Die Update-Pflicht hängt bisher an einzelnen Skills (jeder Skill-Workflow endet mit seinem eigenen Ritual), nicht an die Tatsache, dass überhaupt Dateien geändert wurden. Ein freier Dialog ohne Skill-Aufruf hat keinen strukturellen Endpunkt, an dem eine Aktualisierung ausgelöst würde – und wird von keinem Skript erkannt, weil er gar nicht als Skill läuft.

**Vorschlag.** Sobald P28 (Cold-Read-Modus) formal in `CLAUDE.md` aufgenommen wird, direkt ein eigenes, minimales Session-Ende-Ritual dafür mitgeben: Nach dem letzten inhaltlichen Edit einer Cold-Read-Session von selbst vorschlagen, Statustabelle/„Aktuelle Richtung" zu aktualisieren – analog zu den bestehenden Skills, aber ausdrücklich auch für den skill-losen Dialog-Modus, nicht nur für benannte Skills. Ohne das wiederholt sich der heutige Fall: Der Nutzer muss aktiv nachfragen, statt dass es automatisch passiert.

---

## P30 — Eine Plan-Änderung in der Durchführung lässt Restatements derselben Tatsache im Fazit unbemerkt veralten

**Konkreter Fall (2026-07-30, diese Session).** Die Ergänzung eines zweiten Testpunkts (Klick-Prototyp-Test) in `07_iteratives_design.tex` machte zwei weitere, unabhängige Stellen in `03_fazit/` veraltet, jede erst durch eine eigene Nutzerfrage gefunden: (1) `01_kernergebnisse_und_ausblick.tex:7` sprach noch von „einen realen Nutzertest" (Singular) und meinte nur den Beta-Test; (2) `02_limitationen.tex:5` empfahl noch offen „ein Usability-Test mit einem funktionsfähigen Prototyp sollte folgen", obwohl genau das zu diesem Zeitpunkt bereits geplant war. Keine der beiden Stellen war über `\autoref` mit der geänderten Quelle verknüpft – anders als bei [[P27]] geht es hier nicht um eine einzelne Referenz, die von ihrem Ziel abdriftet, sondern um mehrere, lose verstreute Prosa-Restatements derselben Tatsache (der Test-Fahrplan), die bei einer Änderung an der Quelle alle einzeln nachgezogen werden müssen.

**Warum kein Skript/Skill das auffängt.** Es gibt kein Werkzeug, das verfolgt, welche Fakten aus der Durchführung an anderer Stelle (insbesondere im Fazit) in eigenen Worten wiederholt werden. Ein `\autoref`-Graph ließe sich noch mechanisch prüfen (Sprungziel existiert ja), ein unverlinktes Prosa-Restatement nicht.

**Vorschlag.** Für `schreib-modus`/`gegenlesung` eine Faustregel ergänzen: Sobald ein Plan oder eine Entscheidung in der Durchführung geändert wird, gezielt das Fazit-Kapitel (Kernergebnisse/Ausblick, Limitationen) nach Restatements derselben Sache durchsuchen (Stichwortsuche auf die betroffenen Begriffe, z. B. „Nutzertest", „Prototyp", „Beta-Test") – nicht nur an Stellen mit `\autoref` prüfen, sondern auch an unverlinkten Prosa-Wiederholungen.

---

## P29 — Tabellen-/Abbildungsschrift als Seitenbudget-Hebel war nirgends im Workflow verankert, obwohl main.tex ihn schon vorbereitet hatte

**Konkreter Fall (2026-07-30, gefunden auf Nutzerfrage).** Auf die Frage „ist es erlaubt, Tabellen kleiner darzustellen?" bestätigte ein Blick in die IU-Richtlinie („Die Schrift in den Tabellen und Abbildungen kann bei Bedarf in einer kleineren Größe als 11 Pt. gestaltet werden.") die Zulässigkeit – `main.tex` trug sogar schon seit einer früheren Session einen Kommentar, der genau das vorwegnahm („passt zu `\scriptsize`-Tabelleninhalten"), aber keine einzige Tabelle nutzte das bis zu diesem Zeitpunkt. Alle vier Tabellen liefen mit voller 11-Pt.-Schrift, obwohl mehrere frühere Kürzungsrunden (siehe [[P15]]/[[P17]]) mühsam Wörter aus dem Fließtext strichen, um Seiten zu sparen.

**Warum kein Skript/Skill das auffängt.** Weder `check_umfang.py` noch `pruef-modus`s Teil-Check D prüfen, ob bereits alle formal zulässigen Layout-Hebel (Tabellenschrift, Float-Platzierung siehe P15) ausgeschöpft sind, bevor eine Kürzungsrunde am Fließtext empfohlen wird. Der Hebel stand buchstäblich im eigenen Kommentar in `main.tex`, wurde aber nie aufgegriffen.

**Vorschlag.** In `pruef-modus` Teil-Check D (Build/Seitenumfang) und in einem künftigen Kürzungs-Workflow (P17) eine feste Reihenfolge verankern, bevor inhaltlich gekürzt wird: (1) Float-Platzierung/Weißraum prüfen (P15), (2) Tabellen-/Abbildungsschrift auf `\footnotesize`/`\scriptsize` prüfen (dieser Punkt), (3) erst danach Fließtext kürzen. Layout-Hebel sind reversibel und kosten keine inhaltliche Substanz – sie sollten vor jeder Wort-Kürzung ausgeschöpft sein.

---

## P28 — Manuelles, satzweises Cold-Reading mit Claude fehlt als eigener Workflow-Schritt, obwohl es nach einem 100/100-Voll-Audit noch reale Befunde liefert

**Konkreter Fall (2026-07-30, ganze Session).** Beide Kapitel waren als FERTIG markiert, ein Voll-Audit hatte 100/100 vergeben, Gegenlesung und Gesamt-Stresstest waren mehrfach durchlaufen. Trotzdem fand ein einfaches, vom Nutzer geführtes Vorgehen – einen Absatz oder Satz zeigen, „liest sich das für einen Erstleser schlüssig?" fragen, gemeinsam durchgehen – in einer einzigen Session sechs echte Befunde: die überdehnte Forum/Nutzergruppen-Analogie (→ [[P26]]), die Teilnehmenden/Nichtteilnehmenden-Zitatverwechslung, die falsche SEQ/Think-Aloud-Reihenfolge, die fehlende Testschleife am Klick-Prototyp (ein inhaltlicher Prozess-Fund, kein Textfehler), die Partnerschaften/Kooperationen-Begriffsdrift (→ [[P27]]) und eine Kontrastfigur samt nirgends wiederverwendetem Jargon-Begriff in `06_evaluation_reflexion.tex`.

**Warum kein bestehender Skill das auffängt.** `gegenlesung` und `stresstest` laufen als ein großer, automatisierter Durchgang über das ganze Dokument und erzeugen eine Fundliste – Breite vor Tiefe. Das hier wirksame Prinzip war umgekehrt: Ein echter Leser liest langsam, satzweise, und genau an der Stelle, an der er stolpert, wird nachgehakt – Tiefe genau am Punkt der Reibung, die kein Vollscan gezielt ansteuert. Beide Modi ergänzen sich, ersetzen sich aber nicht: Ein Vollscan findet strukturelle Lücken (fehlende Artefakte, nicht abgedeckte Schlüsselbegriffe), das satzweise Cold-Reading findet die feinkörnigen Verständnis-, Konsistenz- und Anschlussfehler, die erst beim tatsächlichen Lesen auffallen.

**Vorschlag.** Diesen Modus explizit in `CLAUDE.md` (Schnellreferenz-Tabelle und/oder Workflow-Fahrplan) als eigenen, benannten Schritt aufnehmen – z. B. „Absatz/Kapitel mit Claude cold-readen" als Freitext-Einstieg, ausdrücklich **nach** `pruef-modus` bzw. auch nach einem 100/100-Ergebnis zulässig, nicht nur davor. Kein eigenes Skill-File mit Gerüst nötig, da der Modus schon als einfacher Dialog funktioniert (Nutzer zeigt Stelle → Claude liest als Erstleser → Vorschlag mit Empfehlung → Nutzer entscheidet). Wichtig ist nur die **Sichtbarkeit im Fahrplan**, damit künftige Sessions diesen Schritt nicht für überflüssig halten, nur weil der Score schon bei 100 steht.

---

## P27 — Ein `\autoref`-Rückverweis kann von der Terminologie der referenzierten Stelle abdriften, ohne dass ein Zitat-Check das auffängt

**Konkreter Fall (2026-07-30, gefunden auf Nutzerfrage).** `chapters/02_durchfuehrung/04_community_und_feedback.tex:7` schloss mit „Rettungspunkte und Reste-Level setzen den dort beobachteten Unterschied zwischen Teilnehmenden und Nichtteilnehmenden obendrauf (siehe~\autoref{sec:konzept})“ – Rückverweis auf `03_konzept.tex:11`, wo dieselbe Soma-Quelle (S. 9) tatsächlich einen Unterschied zwischen **Viel-** und **Wenigspieler:innen** (51 % vs. 39 % Abfallreduktion) belegt, nicht zwischen Teilnehmenden und Nichtteilnehmenden. Beide Soma-Gruppen waren Teilnehmende der Intervention; „Nichtteilnehmende“ behauptet einen Unterschied, den die referenzierte Stelle nicht hergibt, und ergibt auch logisch keinen Sinn (Rettungspunkte können das Verhalten von Nicht-Nutzer:innen nicht beeinflussen).

**Warum kein Skript das auffängt.** `check_quellentreue.py` prüft nur Sätze mit `\cite`/`\textcite`/`\parencite`-Befehlen gegen den Volltext. Dieser Satz zitiert nicht direkt, sondern verweist per `\autoref{sec:konzept}` auf eine andere Stelle im eigenen Dokument – ein reiner Binnen-Rückverweis, den kein Zitat-Checker prüft, obwohl er inhaltlich genauso von der Quelle abweichen kann wie ein Zitat selbst. `check_formalia.py`s `AUTOREF`-Prüfung deckt nur, ob das Sprungziel existiert, nicht ob die Paraphrase dort zutrifft.

**Vorschlag.** Für `stresstest`/`gegenlesung` ergänzen: Bei jedem `\autoref`, der eine Aussage aus einer anderen Subsection paraphrasiert (statt nur auf eine Abbildung/Tabelle zu verweisen), die Zielstelle tatsächlich aufschlagen und die dort verwendete Terminologie mit der Paraphrase am Rückverweis abgleichen.

---

## P26 — Eine gehedgte Annahme im Satz kann eine zweite, unmarkierte Annahme verdecken

**Konkreter Fall (2026-07-30, gefunden auf Nutzerfrage, kein Skill/Skill-Schritt).** In `chapters/02_durchfuehrung/04_community_und_feedback.tex:7` hatte Gegenlesung Runde 9 (Befund 9.2) bereits moniert, dass Somas Vergleichsgruppe „Präsenz-Workshops" waren, kein per se auf Diskussion angelegtes Format, und die Übertragung des Teilnahmebefunds auf Online-Formate unklar bleibt. Die Abarbeitung fügte daraufhin einen Übertragungsvorbehalt hinzu („bleibt eine Annahme dieser Arbeit") – ließ aber im selben Satz die vorgelagerte Behauptung „Forum und Nutzergruppen setzen wie die dortige Präsenzgruppe auf moderierte Gruppendiskussion" unverändert als Faktum stehen. Diese Formatgleichsetzung ist ebenso unbelegt wie die Übertragbarkeit selbst, wurde aber nicht als Annahme markiert – der Satz hedgte nur die zweite von zwei ineinandergeschachtelten Unsicherheiten.

**Warum kein Skript/Skill das auffängt.** `check_formalia.py` prüft Struktur, keine epistemische Konsistenz. Auch `gegenlesung`/`stresstest`, die den ursprünglichen Fund 9.2 lieferten, prüften die Zitatgenauigkeit, nicht ob die *Reparatur* selbst vollständig war – eine „bleibt eine Annahme dieser Arbeit"-Formulierung wurde als erledigt gebucht, ohne zu prüfen, ob im selben Satz eine strukturell gleichartige, aber unmarkierte zweite Annahme steckt.

**Vorschlag.** Als Faustregel für `stresstest`/`gegenlesung` ergänzen: Wenn ein Satz eine explizite Annahme-/Hedge-Formulierung enthält („bleibt eine Annahme", „ist nicht belegt" o. Ä.), gezielt prüfen, ob derselbe Satz eine *weitere*, unmarkierte Tatsachenbehauptung über dieselbe Vergleichsgröße enthält (hier: das Format der Vergleichsgruppe selbst). Eine gehedgte Unsicherheit lenkt den Blick leicht von einer zweiten, benachbarten ab.

---

## P25 — Deutsche Homographie bei entlehnten Fachbegriffen (Tag = Label vs. Tag = Kalendertag)

**Konkreter Fall (2026-07-30, gefunden auf Nutzerfrage).** `chapters/02_durchfuehrung/03_konzept.tex` verwendete „Reste-Tag" für das englische Lehnwort „tag" (Label/Kennzeichnung), nicht für den Kalendertag. Weil im Deutschen alle Substantive großgeschrieben werden, ist „Tag" (Label) optisch nicht von „der Tag" (Kalendertag) zu unterscheiden. An der betroffenen Stelle stand kein disambiguierendes Verb daneben (anders als an einer zweiten Fundstelle im selben Kapitel, wo „ein Tag, der die Zutat **markiert**" die Lesart klar auf „Label" festlegt) – und stand zudem im selben Satz wie eine echte zeitbasierte Funktion (Zero-Waste-**Woche**), was die Fehllesart „ein Pflicht-Kalendertag" zusätzlich begünstigte.

**Warum kein Skript das auffängt.** Beide Lesarten sind orthografisch und grammatisch korrektes Deutsch – ein Rechtschreib- oder Formalia-Check kann das nicht unterscheiden, nur Sinnverständnis.

**Vorschlag.** Bei der Einführung englischer UI-/Tech-Lehnwörter ins Deutsche (schreib-modus, Konzept-Kapitel) gezielt auf Kollision mit geläufigen deutschen Substantiven prüfen (Tag/Tag ist der naheliegendste Fall, aber nicht der einzige – z. B. „Bar" als UI-Leiste vs. Lokal, „Rahmen" als Frame vs. Bilderrahmen). Entweder ein eindeutiges deutsches Äquivalent wählen (hier: „Kennzeichnung"/„Markierung") oder – falls der Lehnbegriff bleiben soll – an **jeder** Fundstelle ein disambiguierendes Verb/Kontext mitführen, nicht nur an manchen.

---

## P24 — Funktionsbeschreibungen behaupten eine Wirkung, ohne den Mechanismus zu benennen

**Konkrete Fälle, alle in derselben Session (2026-07-30) auf Nutzerfrage gefunden, keiner durch ein Skript:**
- „Diese Mechanik greift einen belegten Nudge-Typ auf" – welcher Typ, blieb unbenannt; die tatsächliche Evidenz (Barker, „Reminders") hing an einer anderen Funktion im selben Absatz.
- „Ein Wochenplan nutzt vorhandene Zutaten" – ohne Bezug dazu, *woher* diese Zutaten kommen; die naheliegende Verbindung zum bereits etablierten Reste-Matching fehlte.
- „der Titel wirkt … im Zusammenspiel mit dem Rettungs-Feed" – der Feed zeigt den Titel laut Mockup und Fließtext gar nicht; die Behauptung hing in der Luft.

**Muster:** Ein Verb wie „wirkt", „nutzt", „verbindet", „greift … auf" suggeriert einen kausalen Mechanismus, ohne einen zu nennen. Das liest sich flüssig und plausibel, hält aber einer Nachfrage „wie genau?" nicht stand – in allen drei Fällen brauchte es eine Nutzerfrage, keine automatische Prüfung deckte es auf.

**Warum kein Skript das auffängt.** Das ist eine inhaltliche, keine strukturelle Prüfung – reine Textanalyse, die kein Regex/Formalia-Check leisten kann.

**Vorschlag.** Als Faustregel für `schreib-modus` beim Verfassen von Funktionsbeschreibungen: Zu jedem Wirkverb prüfen, ob ein *konkretes, bereits eingeführtes* Element als Subjekt/Objekt benannt ist (nicht nur ein abstraktes Label). Ebenfalls als Frage für `stresstest`/`gegenlesung` ergänzen: „Nennt der Satz einen Mechanismus, oder nur eine Wirkung?"

---

## P23 — Text-Mockup-Abgleich ist kein routinemäßiger Prüfschritt, obwohl er fast in jeder Session Funde produziert

**Wiederkehrendes Muster über mehrere Sessions:** Menüplanungs-Zugang nicht im Mockup sichtbar (Befund 5.7/6.2), Plus-Button-Überlappung (6.3), fehlendes Wochenplan-Banner (Anpassung 4), Prompt-Text ≠ tatsächliches Bild (5.8) – und **heute zwei weitere**, beide auf Nutzerfrage, keine durch ein Skript: der „sichtbare Titel" wirkt laut Text „im Zusammenspiel mit dem Rettungs-Feed", aber der Feed-Mockup zeigt gar keinen Titel/Level-Badge; die Folgen-Funktion über den Nutzernamen hat im Mockup kein sichtbares Interaktionselement (was sich hier als bewusste, bereits früher getroffene Entscheidung herausstellte – aber nur, weil nachgefragt wurde).

**Warum kein Skript das auffängt.** Bild-Text-Abgleich ist inhärent visuell/semantisch; `check_formalia.py` und Verwandte arbeiten nur auf dem `.tex`-Text.

**Vorschlag.** Einen expliziten Prüfschritt in `pruef-modus` (Teil-Check, z. B. Ergänzung zu Teil-Check F) und in `gegenlesung` verankern: Für jeden Satz, der behauptet, was ein Mockup zeigt/erlaubt/ermöglicht, das referenzierte Bild tatsächlich per Read-Tool ansehen – nicht nur den Claude-Design-Prompt lesen (der beschreibt die Absicht, nicht zuverlässig das Ergebnis). Nicht erst am Ende (Voll-Audit), sondern schon in `schreib-modus`, sobald ein UI-Verhaltens-Satz geschrieben wird, der sich auf ein bereits existierendes Mockup bezieht.

---

## P22 — Seitenversatz-Korrektur in `check_quellentreue.py` prüft nicht rückwirkend gegen bereits gebuchte Zitationen derselben Quelle

**Konkreter Fall (2026-07-30).** Der gespeicherte Seitenversatz für `barkerWhatNudgeTechniques2021` stand auf `-8`. Korrekt ist `0` (gedruckte Artikel-Seite = PDF-Index + 1, verifiziert an der bereits validierten „S. 10"-Zitation). Der falsche Wert fiel erst auf, als eine **neue** Zitation (S. 2) dadurch fälschlich als „außerhalb des PDFs" gemeldet wurde – er hätte aber genauso gut die **alte** S.-10-Zitation unbemerkt falsch validieren oder invalidieren können, wenn die zufällige Kombination aus Artikellänge und Seitenzahl das zugelassen hätte. Es ist reiner Zufall, dass der Fehler hier auffiel statt sich weiter unbemerkt fortzupflanzen.

**Warum kein Skript das auffängt.** `--offset KEY=N` setzt den Wert und prüft nur die aktuell übergebene Seite (falls per `--seite` getestet), nicht automatisch alle anderen bereits mit diesem Key gebuchten Urteile.

**Vorschlag.** Beim Setzen/Ändern eines Seitenversatzes automatisch alle bereits mit `OK` quittierten Zitationen desselben Bib-Keys erneut auflösen und warnen, falls sich der aufgelöste Text ändert oder eine davon nun außerhalb des PDFs läge. Das macht sowohl einen fehlerhaft gesetzten Versatz sofort sichtbar als auch eine spätere Regression durch einen erneuten `--offset`-Aufruf.

---

## P21 — `--notiz` in `check_quellentreue.py` ist kein Listenparameter: mehrere `--verdikt` in einem Aufruf teilen sich dieselbe (letzte) Notiz

**Konkreter Fall (2026-07-30), live reproduziert.** Aufruf mit zwei `--verdikt <hash>=OK` und zwei `--notiz "…"` in derselben Kommandozeile: Beide Urteile bekamen die **gleiche, letzte** Notiz zugewiesen – die Barker-Zitation trug hinterher den Nivedhitha-Text. Ursache mechanisch bestätigt: `--verdikt` ist `action="append"`, `--notiz` ist `default=""` (einzelner Wert, kein Listenparameter) und gilt global für alle `--verdikt` desselben Aufrufs.

**Zur Ehre des Skripts:** Die bereits vorhandenen Wächter (`NOTIZ-DUBLETTE`, `NOTIZ-FREMDER-AUTOR`, siehe P2-3) haben den Fehler sofort nach dem Schreiben erkannt und gemeldet – der Fehlerzustand wurde also nicht unbemerkt persistiert. Trotzdem musste der Fehler manuell durch zwei separate Neuaufrufe korrigiert werden.

**Vorschlag.** `--notiz` ebenfalls als `action="append"` definieren und mit `--verdikt` positionsweise zippen; bei ungleicher Anzahl (`len(a.notiz) != len(a.verdikt)`, sofern mehr als ein `--verdikt` übergeben wurde) einen Fehler statt einer stillen Fehlzuordnung ausgeben. Damit wird der Fall, den die Wächter heute nur nachträglich abfangen, von vornherein unmöglich.

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
