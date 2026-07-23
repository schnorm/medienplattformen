# AENDERUNGEN.md

## Runde 1 — Gegenlesung (2026-07-21)

Kalte Prüfer-Gegenlesung gegen `aufgabe.md`. Blickrichtung: Erfüllt die Arbeit die gestellte Aufgabe? Kapitelplan, Prüfbericht und Statusdateien wurden bewusst nicht herangezogen.

### Soll-Ist-Tabelle (Schritt 3)

| Geforderter Inhalt (aus `aufgabe.md`) | Erfüllung |
|---|---|
| Teilaufgabe 1: Analyse bestehender Plattformen | erfüllt — `sec:wettbewerbsanalyse`, 5 Plattformen + Kriterienmatrix `tab:wettbewerbsvergleich` |
| Teilaufgabe 2: Konzeptentwicklung | erfüllt — `sec:konzept`, Funktionsübersicht `tab:funktionsuebersicht` |
| Teilaufgabe 3: Iteratives Design und Feedback (Beschreibung genügt) | erfüllt — `sec:community_und_feedback`, Beta-Gruppe/Sprints als geplantes Vorgehen |
| Berichtsinhalt: Zielgruppe | erfüllt — `sec:zielgruppe` + Persona `tab:persona` (Anhang A) |
| Berichtsinhalt: Funktionalitäten | erfüllt — `sec:konzept` |
| Berichtsinhalt: UI/UX | **nur ersatzweise erfüllt** — Text beschreibt 3 Bereiche, Mockups in Anhang B sind aber leere Platzhalter (siehe Befund 1) |
| Berichtsinhalt: Community-Building | erfüllt — Rettungs-Feed + Challenges, Verzicht auf Forum begründet |
| Objekt: Wettbewerbsvergleich (Tabelle) | erfüllt — `tab:wettbewerbsvergleich` |
| Objekt: Persona (Text/Abb.) | erfüllt — `tab:persona` |
| Objekt: UI/UX-Skizze/Mockup (Abb.) | **nicht erfüllt** — nur Platzhalter-Rahmen in Anhang B (Befund 1) |
| Objekt: Plattformname | erfüllt — „Resteria", hergeleitet und gegen „Restlos Glücklich" abgegrenzt |
| Objekt: Funktionsübersicht (Tab./Abb.) | erfüllt — `tab:funktionsuebersicht` |
| Objekt: Phasenplanung (Tabelle) | erfüllt — `tab:phasenplanung` mit Zeitrahmen + Ressourcen |
| Schlüsselbegriff: Rezept-Uploads (Foto/Video) | erfüllt |
| Schlüsselbegriff: Kommentar-/Bewertungssystem | erfüllt |
| Schlüsselbegriff: Personalisierte Empfehlungen | erfüllt |
| Schlüsselbegriff: Gruppen/Foren | erfüllt, aber verengt — nur „Forum" begründet ausgeschlossen, „Gruppen" nicht eigens behandelt (Befund 5) |
| Schlüsselbegriff: Event-Kalender (bei Auslassung begründen) | erfüllt — Verzicht in `sec:konzept` explizit begründet |
| Schlüsselbegriff: Lebensmittel-Journaling/Menüplanung | erfüllt — Reste-Journal, an Rettungspunkte gekoppelt |
| Verengung Zielgruppe (begründet) | erfüllt — Einleitung + `sec:zielgruppe`, argumentativ begründet |
| Materialien Hansch & Rentschler (2012), Kapoor et al. (2018) | nicht erfüllt, aber laut `aufgabe.md` nicht Pflicht (Befund 6) |

---

### Befund 1 — Die UI/UX-Mockups existieren nicht; der Text behauptet, sie lägen vor  🔴 schwer

**Status: ERLEDIGT (2026-07-23).** Nutzer hat vier echte Mockup-Screenshots geliefert (Startseite, Startseite mit ausgeklappten „Gespeicherte Rezepte", Profil, Rettungs-Feed) unter `images/durchfuehrung/`. Alle drei Platzhalter in `pages/appendix.tex` durch `\includegraphics` ersetzt, ein viertes Mockup (Bookmarks) neu ergänzt und im Fließtext (`03_konzept.tex`) nach Rückfrage referenziert. `\quelle{}`-Zeilen folgen dem Pflichtmuster „Erstellt mit dem Prompt [...] durch Claude Design (Claude Sonnet 5)", mit Zusatz „, Abbildung nachträglich manuell bearbeitet." nach Prüfung von `sources/Zitierleitfaden.pdf` Kap. 2.2.5. `check_formalia.py` 0 FEHLER auf `03_konzept.tex` und `appendix.tex`.

**Befund:** Anhang B (`pages/appendix.tex`, `fig:mockup_start`, `fig:mockup_profil`, `fig:mockup_feed`) enthält drei leere gestrichelte Rahmen mit dem Text „Platzhalter für KI-generiertes Mockup … vor Abgabe durch tatsächliches Mockup ersetzen". Der Fließtext behauptet dagegen an drei Stellen, das Mockup existiere und sei fertig:
- `chapters/02_durchfuehrung/03_konzept.tex:53`: „Für alle drei Bereiche liegt je eine grafische Mockup-Skizze in Anhang B vor … Die Mockups sind als KI-generierte Darstellung gekennzeichnet, wie es der IU-Zitierleitfaden … vorsieht."
- `chapters/03_fazit/02_limitationen.tex:5`: „Die Skizze ist KI-generiert und beruht nicht auf einer Rückmeldung realer Nutzer:innen … Erstens ist die Herkunft des Mockups transparent gekennzeichnet".
- `chapters/02_durchfuehrung/06_evaluation_reflexion.tex:5`: „Der Bereich User Interface und User Experience ist mit … dem Mockup im Anhang abgedeckt."

**Warum ein Prüfer das anstreicht:** Die UI/UX-Skizze ist ein wörtlich gefordertes Lieferobjekt (`aufgabe.md`, Lieferobjekte + Berichtsinhalt UI/UX). Ein Prüfer, der Anhang B aufschlägt, findet nichts als eine TODO-Notiz an sich selbst — und einen Fließtext, der die Existenz des Artefakts behauptet. Das trifft gleich zwei Kriterien: Qualität (das geforderte Ergebnis fehlt) und Dokumentation/Redlichkeit (der Text sagt aus, was nicht stimmt). Ein behauptetes, aber nicht beiliegendes Artefakt schwächt die Aussage, statt sie zu stützen. In der aktuellen Form ist die Arbeit nicht abgabefähig.

**Anweisung:** Vor jeder weiteren Runde die drei Platzhalter in `pages/appendix.tex` durch echte KI-generierte Mockups ersetzen und die `\quelle{}`-Zeile nach dem hinterlegten Muster („Erstellt mit dem Prompt […] durch […]") ausfüllen. Erst wenn die Bilder tatsächlich vorliegen, decken sich Text und Anhang. Solange sie fehlen, dürfen `03_konzept.tex:53`, `02_limitationen.tex:5` und `06_evaluation_reflexion.tex:5` die Existenz nicht im Präsens behaupten. (Diese Arbeit — die Mockups selbst — liegt beim Nutzer, nicht bei mir.)

### Befund 2 — Wettbewerbsanalyse stützt sich auf einen unbelegten „App-Test der Verbraucherzentrale"  🟠 mittel

**Status: ERLEDIGT (2026-07-21).** Named-Reference auf die Verbraucherzentrale entfernt (deckungsgleich mit der bereits geltenden ZITIERREGEL im Kapitelplan — Wettbewerbsanalyse ist eigene Sichtung, kein `\parencite`), Aussage in `01_wettbewerbsanalyse.tex:7` läuft jetzt rein als „Nach eigener Sichtung (Stand: Juli 2026)". Unbelegte Zahl „mehr als 800 Rezepte" durch „eine umfangreiche Rezeptdatenbank" ersetzt.

**Befund:** `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:7`: „Nach eigener Sichtung, gestützt durch einen unabhängigen App-Test der Verbraucherzentrale (Stand: Juli 2026)…". Für diesen App-Test gibt es keinen Eintrag in `references.bib` (nur 6 Quellen: barker, nivedhitha, shen, soma, un, vittuari). Auch die Angabe „mehr als 800 Rezepte" für die BMEL-App ist ohne Beleg.

**Warum ein Prüfer das anstreicht:** Ein Kapitel mit Analysecharakter, das eine externe Quelle namentlich als Stütze anführt, muss sie nachprüfbar machen (Nachvollziehbarkeit). Eine Quelle beim Namen zu nennen und dann nicht zu zitieren, wirkt schwächer, als sie gar nicht zu erwähnen — der Prüfer sieht die Lücke.

**Anweisung:** Entweder den Verbraucherzentrale-App-Test als Quelle in Zotero/BBT aufnehmen und in `01_wettbewerbsanalyse.tex:7` per `\parencite` belegen (bevorzugt), oder — falls kein zitierfähiger Test vorliegt — den Verweis streichen und die Plattformbewertung ausschließlich als „eigene Sichtung (Stand: Juli 2026)" deklarieren. Für „mehr als 800 Rezepte" entweder Beleg ergänzen oder die konkrete Zahl entschärfen.

### Befund 3 — Transfer-Kriterium: wirtschaftliche Bedeutung bleibt dünn  🟠 mittel

**Status: ERLEDIGT (2026-07-21).** Kompakter Absatz zu Freemium-Modell, Kooperationen (Food-Sharing-Initiativen, Lebensmittelhändler:innen) und Marktrelevanz des Zero-Waste-Segments in `03_konzept.tex` nach der Namensherleitung ergänzt.

**Befund:** Die gesellschaftliche Bedeutung (Lebensmittelverschwendung, SDG 12.3) ist gut ausgeführt (`01_ausgangslage_und_problem.tex`). Die *wirtschaftliche* Seite, die `aufgabe.md` unter Transfer ausdrücklich nennt („Technologie ↔ gesellschaftliche/wirtschaftliche Bedeutung"), erscheint nur als Halbsatz: „kommerziell gedachtes Plattformkonzept" (`03_konzept.tex:3`). Geschäftsmodell, Finanzierung, Marktgröße oder Monetarisierung fehlen.

**Warum ein Prüfer das anstreicht:** Transfer zählt 15 % und hat laut Aufgabenstellung zwei Dimensionen. Zwei starke Dimensionen (hier: gesellschaftlich, technisch) verdecken leicht, dass die dritte (wirtschaftlich) ausgelassen ist — genau das ist der wahrscheinlichste Punktverlust.

**Anweisung:** Einen kompakten Absatz zur wirtschaftlichen Einordnung ergänzen, am besten in `03_konzept.tex` (nach der Namensherleitung) oder in der Reflexion `06_evaluation_reflexion.tex`. Genügend wären: grobes Monetarisierungsmodell (z. B. Freemium, Partnerschaften), Marktrelevanz des Zero-Waste-Segments, ggf. Bezug zu bereits erwähnten Kooperationen. Kein volles Business-Modell nötig, aber die Dimension muss sichtbar bedient werden.

### Befund 4 — Vergleichsmatrix: Resteria erhält durchweg Bestwerte  🟡 leicht (teilweise entschärft)

**Status: ERLEDIGT (2026-07-21), abweichend von der ursprünglichen Anweisung — Nutzer-Entscheidung nach Rückfrage.** Statt einzelne Zelle abzuschwächen: Resteria-Zeile komplett aus `tab:wettbewerbsvergleich` entfernt (Tabelle heißt „Vergleich bestehender Plattformen" — Resteria ist kein bestehendes Produkt). Quelle-Zeile bereinigt. Folgesatz „Die Tabelle macht die Lücke sichtbar …" trägt die Differenzierung weiterhin im Fließtext. Nebenbefund behoben: „vier Plattformen" in `06_evaluation_reflexion.tex:3` auf „fünf Plattformen" korrigiert (entsprach nicht der tatsächlichen Anzahl in der Wettbewerbsanalyse).

**Befund:** In `tab:wettbewerbsvergleich` (`01_wettbewerbsanalyse.tex:24`) bekommt Resteria in allen vier Kriterien „stark", während jede Konkurrenzplattform mindestens eine Schwäche hat. Das ist das klassische Muster einer ergebnisorientierten Eigenbewertung.

**Warum ein Prüfer das anstreicht:** Eine Matrix, in der das eigene Konzept auf ganzer Linie gewinnt, weckt Verdacht auf Zirkelschluss — die Kriterien scheinen so gewählt, dass Resteria gewinnt. Kreativität (Vergleich zu Bestehendem) verliert an Überzeugungskraft, wenn der Vergleich zu freundlich mit sich selbst ist.

**Entschärfung, die schon da ist (nicht anfassen):** Die Quellenzeile der Tabelle und der Fließtext (`:30`, „Schwäche im fehlenden Nutzertest") kennzeichnen den Konzeptstatus ausdrücklich und benennen die eigene Schwäche. Das mildert den Befund erheblich.

**Anweisung (optional, zur Absicherung):** Erwägen, Resteria bei einem Kriterium bewusst *nicht* auf „stark" zu setzen, solange kein Nutzertest vorliegt — z. B. „Reste-Matching-Werkzeug: mittel (Konzept, noch nicht erprobt)". Das erhöht die Glaubwürdigkeit der Matrix stärker als jede Fußnote. Kein Muss, aber ein billiger Gewinn.

### Befund 5 — Schlüsselbegriff „Gruppen/Foren": nur „Forum" wird begründet ausgeschlossen  🟡 leicht

**Status: ERLEDIGT (2026-07-21).** `04_community_und_feedback.tex` schließt jetzt Gruppen ausdrücklich mit derselben Soma-et-al.-Begründung aus wie das Forum.

**Befund:** `aufgabe.md` listet „Gruppen/Foren" als Schlüsselbegriff. Der Text schließt in `04_community_und_feedback.tex:7` ein „offenes Diskussionsforum" begründet aus (Soma et al.). „Gruppen" als eigene Funktion (z. B. thematische oder regionale Nutzergruppen) werden dabei nicht getrennt betrachtet — sie fallen stillschweigend mit dem Forum weg.

**Warum ein Prüfer das anstreicht:** Der Begriff nennt zwei Dinge; die Begründung deckt nur eines ab. Ein aufmerksamer Prüfer fragt, ob „Gruppen" bewusst oder versehentlich fehlen.

**Anweisung:** In `04_community_und_feedback.tex` den Ausschluss auf beide Begriffe beziehen — entweder Gruppen ebenfalls begründet ausschließen (die Challenges/der Feed ersetzen sie), oder eine leichte Gruppenfunktion andeuten. Ein Satz genügt.

### Befund 6 — Genannte Einstiegsliteratur (Hansch & Rentschler; Kapoor et al.) nicht aufgegriffen  🟢 Hinweis

**Status: ÜBERSPRUNGEN (2026-07-21).** Beide Quellen fehlen noch in `references.bib` (nur 6 Keys vorhanden, keiner der beiden). Da der Befund selbst als „nicht Pflicht, nur wenn es sich natürlich fügt" markiert ist und ein Einbau einen vorherigen Zotero-Import erfordern würde, bewusst nicht erzwungen.

**Befund:** Die beiden in `aufgabe.md` genannten Materialien tauchen weder in `references.bib` noch im Text auf.

**Warum ein Prüfer das anstreicht:** `aufgabe.md` markiert sie ausdrücklich als „nicht Pflicht, aber sinnvoller Einstieg" — also **kein FAIL**. Manche Prüfer werten es dennoch positiv, wenn die ausdrücklich empfohlene Literatur wenigstens gestreift wird.

**Anweisung (optional):** Falls beim nächsten Durchgang inhaltlich passend, eine der beiden Quellen an einer Stelle einbauen (Kapoor et al. z. B. bei Social-Media-Funktionen, Hansch & Rentschler bei UI/UX-Emotionalität). Nur wenn es sich natürlich fügt — nicht erzwingen.

---

### Die sieben Prüferfragen (Schritt 4)

1. **Existiert, was behauptet wird?** → Nein bei den Mockups (Befund 1). Alle Tabellen (Wettbewerb, Funktionen, Persona, Phasen) und die Funktionslogik-Abbildung existieren real.
2. **Teilaufgabe ersetzt statt ausgeführt?** → Feedback-Schleifen sauber als „geplantes Vorgehen" gekennzeichnet (von `aufgabe.md` gedeckt). Der fehlende Nutzertest ist ebenfalls gedeckt. Einziger echter Ersatz ohne Deckung: der Platzhalter statt Mockup (Befund 1).
3. **Jede Behauptung nachprüfbar?** → Überwiegend ja; Lücke beim Verbraucherzentrale-Test und der 800-Rezepte-Zahl (Befund 2).
4. **Zentralbegriff stillschweigend verengt?** → Zielgruppen-Verengung ist explizit begründet (legitim). „Gruppen/Foren" leicht verengt (Befund 5).
5. **Widerspruch in eigenen Festlegungen?** → Ja: Text behauptet fertiges Mockup, Anhang zeigt Platzhalter (Befund 1). Sonst konsistent.
6. **Eigene Bewertung ergebnisorientiert?** → Ansatzweise in der Vergleichsmatrix, aber durch Kennzeichnung des Konzeptstatus entschärft (Befund 4).
7. **Wirkt es wie ein KI-Text?** → Überwiegend menschlich und fachlich sauber. Mild auffällig: das USP-Motiv (Reste-Matching + Community) wird in fast jeder Subsection nahezu wortgleich wiederholt, und die „also"-Einschübe zur Begriffserklärung häufen sich. Kein Regelverstoß, aber beim Überarbeiten könnten ein bis zwei der USP-Wiederholungen (Einleitung → Wettbewerb → Konzept → Fazit) gestrafft werden, damit es weniger schablonenhaft klingt. **Kein eigener Änderungsauftrag — nur Hinweis fürs Straffen.**

---

### Gesamteinschätzung

Inhaltlich eine tragfähige, in sich schlüssige Arbeit: Die Marktlücke ist sauber hergeleitet, die Funktionen sind aus Literatur begründet und — vorbildlich — von den eigenen Konzeptentscheidungen abgegrenzt (`03_konzept.tex:28`, die vorsichtige Einordnung der Soma-Zahl ist stark und **darf nicht wegredigiert werden**). Struktur, Reflexion und Limitationen erfüllen die Prozess-Anforderungen gut. Der Verzicht auf Event-Kalender und Forum ist begründet, die Zielgruppen-Verengung ordentlich gerechtfertigt.

Der eine Befund, der alles andere überlagert, ist Befund 1: Solange die Mockups Platzhalter sind, fehlt ein gefordertes Lieferobjekt und der Text behauptet dessen Existenz. Das ist der einzige **abgabekritische** Punkt. Befunde 2 und 3 heben die Qualität spürbar, sind aber überschaubarer Aufwand. Befunde 4–6 sind Feinschliff.

**Umfangshinweis:** Die Zugaben aus Befund 2 (Beleg/Streichung) und Befund 3 (wirtschaftlicher Absatz, ~5–8 Zeilen) sind klein. Das Einsetzen echter Mockups (Befund 1) ersetzt nur Platzhalter, kostet also kaum Seitenumfang. Bei 7–10 Seiten Zielkorridor entsteht durch die Runde kein Kürzungsdruck.

**Freigabepflichtig:** Keiner der Befunde berührt These, Kernargumente, Leitfrage, Zielgruppendefinition oder eigene Rechercheergebnisse in einer Weise, die eine `[FREIGABE]` erzwingt. Befund 4 (Matrix-Bewertung ändern) berührt eine eigene Bewertung — daher als **optional** markiert, Entscheidung liegt beim Nutzer.

### Nächster Schritt

Umsetzung **nicht in dieser Sitzung** (Prüfer- und Autorrolle getrennt). In frischer Sitzung: „Schreib-Modus: AENDERUNGEN.md abarbeiten". Der Nutzer entscheidet über jeden Befund einzeln.

---

## Runde 2 — Gesamt-Stresstest (2026-07-21)

Inhaltliche Prüfung der ganzen Arbeit gegen ihre eigene Argumentation und gegen `aufgabe.md`. Alle Kapitel FERTIG. Mockup-Platzhalter (Runde-1-Befund 1) auf Nutzerwunsch ausgeklammert — bleibt separat offen. Doppelbefunde der Gegenlesung nicht erneut aufgeführt. Verifikations-Gate für die Markt-Nichtexistenzbehauptung ausgeführt (Websuche).

### Befund GS-1 — USP-Behauptung durch reale App widerlegbar: „Leftovercooking"  🟠 mittel · **[FREIGABE]** (berührt Kernargument/Marktlücke + eigene Recherche)

**Status: ERLEDIGT (2026-07-21).** Nutzer-Entscheidung nach Rückfrage: volle Aufnahme, mit gründlicher Online-Recherche (Verbraucherzentrale-Test 2024 + leftovercooking.app). leftovercooking als 6. Plattform in `01_wettbewerbsanalyse.tex` aufgenommen (eigener Absatz + Tabellenzeile: Rezept-Austausch mittel, Community mittel, Nachhaltigkeitsfokus stark, Reste-Matching stark), viertes Gegenargument im Fließtext ergänzt, Lücken-Absatz präzisiert. Recherche-Nachweis in `kapitelplan.md` → Rechercheprotokoll ergänzt. Folgeanpassungen „fünf" → „sechs Plattformen" in `06_evaluation_reflexion.tex`, `01_kernergebnisse_und_ausblick.tex`, `02_limitationen.tex` (dort auch „drei" → „vier Plattform-Kategorien").

**Befund:** Das tragende Kernargument lautet, keine breit genutzte Plattform kombiniere Reste-Matching mit einer echten Social-Community (`01_wettbewerbsanalyse.tex:29`, `03_konzept.tex:9`, Fazit `01_kernergebnisse_und_ausblick.tex:3,7`). Die Websuche (Verifikations-Gate) fördert mit **Leftovercooking** (leftovercooking.app, von der Verbraucherzentrale getestet) eine reale App zutage, die Zutaten-Matching mit einer Creator-/Community-Ebene (Kurzprofile von Food-Creator:innen und Hobbyköch:innen, community-basierte Rezepte) und Zero-Waste-Tipps verbindet — also näher an Resterias Pitch liegt als die fünf untersuchten Plattformen. Brisanz: Genau dieser Verbraucherzentrale-Test war ursprünglich als Quelle im Text (Runde-1-Befund 2, entfernt) — die App war der Projektgruppe bekannt und fehlt dennoch in der Analyse.

**Warum ein Prüfer das anstreicht:** Ein Prüfer, der eine bekannte Reste-App kennt, die die behauptete Lücke teilweise schon füllt, liest die USP als zu selbstbewusst. Die strikte Formulierung („keine der **untersuchten** Plattformen", Fazit „keine der **fünf** untersuchten") ist durch die Scoping-Wortwahl formal gedeckt und die Limitationen (`02_limitationen.tex:7`) räumen die Nicht-Vollständigkeit ausdrücklich ein — der Befund bricht die These also nicht. Aber die konkrete, prominente Gegen-App ausgerechnet auszulassen, obwohl sie schon im eigenen Entwurf stand, ist der wahrscheinlichste Angriffspunkt auf Kreativität (Vergleich zu Bestehendem) und Qualität.

**Anweisung (Nutzerentscheidung, [FREIGABE]):** Bevorzugt Leftovercooking als sechste Plattform in `01_wettbewerbsanalyse.tex` + `tab:wettbewerbsvergleich` aufnehmen und einordnen — mutmaßlich Rezept-Austausch/Community „mittel", Reste-Matching „stark", womit die USP (Matching **plus voll ausgebaute** Social-Community mit Feed/Gamification/Challenges) geschärft, nicht widerlegt wird. Mindestvariante: Leftovercooking in `02_limitationen.tex:7` als konkretes Beispiel der „weiteren, kleineren Reste-Matching-Apps" namentlich nennen, damit die Auslassung bewusst und begründet wirkt statt übersehen. Die Entscheidung, ob und wie tief die App aufgenommen wird, liegt beim Nutzer (Kernargument + eigene Recherche).

### Befund GS-2 — Barker-„Reminders" trägt die Reste-Level-Herleitung nur bedingt  🟠 mittel

**Status: ERLEDIGT (2026-07-21).** Reste-Level in `03_konzept.tex` als Feedback-/Fortschritts-Mechanik umformuliert; echter Reminder als geplante Erinnerungsbenachrichtigung („Deine Reste warten") ergänzt, die den Barker-Beleg jetzt sauber trägt. `tab:funktionsuebersicht`-Zelle entsprechend angepasst.

**Befund:** `03_konzept.tex:28` (und `tab:funktionsuebersicht:45`, Fazit `01_kernergebnisse_und_ausblick.tex:5`) leitet die Rettungspunkt-/Reste-Level-Mechanik u. a. aus Barkers Nudge-Typ „Reminders" ab: „das steigende Reste-Level erinnert Nutzer:innen implizit daran, weiterzumachen." Ein passiver Fortschritts-/Statusbalken ist aber kein Reminder im Sinne der Nudge-Literatur — Reminders sind aktive, wiederkehrende Anstöße (Push-Nachricht, E-Mail). Ein sichtbares Level ist funktional näher an Feedback/Zielgradient/Belohnung.

**Warum ein Prüfer das anstreicht:** Die Arbeit macht ihre Sorgfalt gerade daran fest, Funktionen sauber aus Hebeln herzuleiten (`06_evaluation_reflexion.tex:9`, „bewusste Trennung zwischen literaturbasierten Hebeln und eigenen Konzeptentscheidungen"). Eine schiefe Zuordnung (Level = Reminder) unterläuft genau diesen Anspruch und ist leicht zu bemerken.

**Anweisung:** Entweder die Zuordnung präzisieren — das Level als Feedback-/Zielgradient-Mechanik ausweisen und den echten „Reminder" an die Stelle setzen, an die er gehört (z. B. eine geplante Erinnerungs-Benachrichtigung „Deine Reste warten"), was Barker sauber trägt — oder den Reminder-Bezug am Level abschwächen zu „stützt sich u. a. auf". Ein bis zwei Sätze, keine Struktur­änderung.

### Befund GS-3 — Zeitpuffer behauptet, in der Phasentabelle nicht sichtbar  🟠 mittel

**Status: ERLEDIGT (2026-07-21).** `tab:phasenplanung` angepasst: MVP-Entwicklung Woche 8–17 (inklusive zweiwöchigem Puffer), Beta-Test Woche 18–20, Launch ab Woche 21. Fließtext-Aussage (Zeitpuffer von zwei Wochen) jetzt durch die Tabelle gedeckt.

**Befund:** `05_phasenplanung.tex:23` nennt als Risikopuffer „einen Zeitpuffer von zwei Wochen zwischen \ac{MVP}-Entwicklung und Beta-Test". Die Phasentabelle `tab:phasenplanung` (`:13`–`:14`) führt \ac{MVP}-Entwicklung in Woche 8–15 und Beta-Test in Woche 16–18 — lückenlos aneinander, kein Puffer. Text und eigene Tabelle widersprechen sich.

**Warum ein Prüfer das anstreicht:** Zählungen/Zeitangaben gegen die eigene Tabelle sind der klassische Konsistenz-Check. Ein Prüfer, der die Wochen nachrechnet, findet den fehlenden Puffer sofort — das trifft Dokumentation und Prozess-Reflexion.

**Anweisung:** Eines von beiden angleichen. Entweder den Puffer in die Tabelle einbauen (\ac{MVP} bis Woche 15, Beta ab Woche 18, Wochen 16–17 als Puffer/Stabilisierung ausweisen; Launch-Wochen entsprechend verschieben) oder die Puffer-Aussage in `:23` als „innerhalb der \ac{MVP}-Phase eingeplant" umformulieren, sodass sie nicht mehr eine Lücke zwischen zwei Tabellenzeilen behauptet, die dort nicht steht.

### Befund GS-4 — Foodsharing.de: Tabellenwertung „Community stark" gegen die eigene Abgrenzung im Fließtext  🟡 leicht

**Status: ERLEDIGT (2026-07-21).** Halbsatz in `01_wettbewerbsanalyse.tex` ergänzt: Mitglieder-Community rund um Fairteiler/Abholungen ist aktiv und real (rechtfertigt „stark"), bezieht sich aber auf die Weitergabe-Organisation, nicht auf Rezeptaustausch. Chefkoch-Wertung geprüft, nicht geändert (Anweisung: „nur prüfen, nicht zwingend ändern").

**Befund:** `tab:wettbewerbsvergleich` gibt Foodsharing.de „Community-Funktionen: stark". Der Fließtext (`01_wettbewerbsanalyse.tex:9`) spricht der Plattform aber „eine Rezept-Community im engeren Sinn" ausdrücklich ab und grenzt sie als „anderes Nutzungsszenario" (Weitergabe vor dem Verderb) ab. Ein Prüfer, der Zelle und Absatz nebeneinanderlegt, sieht die Spannung: entweder ist Foodsharings Community stark (dann ein näherer Wettbewerber als zugegeben) oder nicht (dann Zelle zu großzügig). Nebenbei: Chefkoch „Nachhaltigkeits-/Restefokus: mittel" wirkt für eine Plattform, die laut Text nur „einzelne Rezeptsammlungen zu bestimmten Zutaten" bietet, ebenfalls eher großzügig.

**Warum ein Prüfer das anstreicht:** Die Kriteriendefinition (`:11`) macht Community an „tatsächlichem Austausch zwischen Nutzer:innen" fest — für Foodsharing verteidigbar (Abhol-Koordination, Mitglieder). Der Konflikt ist daher mild, aber sichtbar, weil der Fließtext die Community-Qualität selbst relativiert.

**Anweisung:** Einen Halbsatz in `:9` ergänzen, der die Tabellenwertung deckt — z. B. dass Foodsharing zwar eine aktive Mitglieder-Community (daher „stark") hat, diese aber der Lebensmittel-Weitergabe und nicht dem Rezept-Austausch dient. Damit lesen Zelle und Text konsistent. Chefkoch-Wertung nur prüfen, nicht zwingend ändern.

### Befund GS-5 — Verengung auf bereits Überzeugte gegen den gesellschaftlichen Wirkungsanspruch (SDG 12.3) + kritische Masse  🟠 mittel

**Status: ERLEDIGT (2026-07-21).** Neuer Absatz in `06_evaluation_reflexion.tex` (nach dem Berichtsinhalte-Abgleich, vor der Methoden-Reflexion): löst die Zange auf, indem Resteria als Vertiefungs-/Bindungsangebot für eine realistische Nische statt als Werkzeug für die Gesamtbevölkerung gerahmt wird, Breitenwirkung als mittelbare, partnerschaftsabhängige Perspektive erklärt und das Reichweitenrisiko des Feeds explizit benannt wird. Limitationen-Struktur (3 Schichten) unverändert gelassen, kein 4. Limitationspunkt.

**Befund:** Die Einleitung begründet die gesellschaftliche Relevanz über SDG 12.3, die Halbierung der Lebensmittelverschwendung „auf Handels- und Verbraucherebene" (`01_ausgangslage_und_problem.tex:5`). Zugleich verengt der Bericht die Zielgruppe bewusst auf **bereits** nachhaltigkeitsorientierte Hobbyköch:innen (`02_zielsetzung_und_verengung.tex:5`) — mit der Begründung, Gamification wirke nur für ohnehin Motivierte. Beides zusammen erzeugt eine Zange: Die breite Wirkung, mit der die Arbeit ihre Relevanz begründet, erfordert Verhaltensänderung bei den Nicht-Überzeugten, während das Konzept ausdrücklich nur die Überzeugten adressiert. Verstärkend ruht die Community-Mechanik (Osmosis/Feed, `04_community_und_feedback.tex:5`) auf Sichtbarkeit vieler Beiträge — sie braucht also kritische Masse, gerade in einer engen Nische. Die Phasenplanung adressiert Beta-Repräsentativität und \ac{MVP}-Verzug (`05_phasenplanung.tex:23`), aber nicht dieses Adoptions-/Reichweitenrisiko.

**Warum ein Prüfer das anstreicht:** Die Arbeit nennt eine Bedingung ihres eigenen Gelingens (Breitenwirkung bzw. genügend aktive Nutzer:innen), ohne sie mit der selbst gewählten Verengung zu versöhnen. Das ist ein klassischer selbst erhobener, unbeantworteter Einwand — Transfer (gesellschaftliche Bedeutung) und Qualität sind betroffen.

**Anweisung (Nutzerentscheidung bei These-Nähe — hier aber ohne [FREIGABE], weil die Verengung nicht geändert, nur ihr Verhältnis zum Wirkungsanspruch geklärt wird):** Einen kurzen Absatz — am ehesten in `06_evaluation_reflexion.tex` oder als vierte Limitation — der die Zange benennt und auflöst: Resteria zielt auf Vertiefung/Bindung bei bereits Motivierten (realistische Nische), nicht auf die Gesamtbevölkerung; Breitenwirkung Richtung SDG 12.3 ist eine mittelbare, skalierungs- und partnerschaftsabhängige Perspektive (Anknüpfung an die bereits genannten Kooperationen im Ausblick, `01_kernergebnisse_und_ausblick.tex:11`). Das entschärft den Einwand, ohne die Verengung anzutasten. Alternativ das SDG-12.3-Framing in der Einleitung eine Spur bescheidener an die Nische koppeln.

### Befund GS-6 — Soma selektiv: „passive Informationsgruppe ebenso wirksam" lädt zur Rückfrage nach der Gamification-Notwendigkeit ein  🟡 leicht

**Status: ERLEDIGT (2026-07-21).** Satz in `04_community_und_feedback.tex` ergänzt: Rettungs-Feed = passiver Osmosis-Kanal aus der Studie, Rettungspunkte/Reste-Level setzen den belegten Dosis-Effekt obendrauf statt zu ersetzen.

**Befund:** `04_community_und_feedback.tex:7` stützt den Verzicht auf Forum/Gruppen darauf, dass bei Soma et al. „sowohl eine passive Informationsgruppe als auch eine Gamification-Gruppe deutlich höhere Teilnahme" erreichten als die Diskussionsgruppe. Dieselbe Studie trägt in `03_konzept.tex:30` die Gamification-Entscheidung. Ein kritischer Leser kann `:7` gegen `:30` wenden: Wenn die **passive** Gruppe ebenso gut abschnitt, warum dann der ganze Rettungspunkt-/Level-Apparat? (Die Arbeit hat de facto eine gute Antwort — der Rettungs-Feed **ist** der passive Osmosis-Kanal, Gamification liefert zusätzlich den Dosis-Effekt Vielspieler 51 % vs. Wenigspieler 39 % —, macht sie an dieser Stelle aber nicht sichtbar.)

**Warum ein Prüfer das anstreicht:** Zwei Aussagen aus einer Quelle, die sich auf den ersten Blick gegenseitig relativieren, ohne dass der Text die Auflösung ausspricht — das lädt zur genau dieser Nachfrage ein.

**Anweisung:** Einen halben Satz in `04_community_und_feedback.tex` ergänzen, der beide Soma-Nutzungen verklammert: Resterias Feed nimmt den wirksamen passiven Kanal auf, die Gamification setzt obendrauf (Dosis-Effekt aus derselben Studie). Damit liest sich die doppelte Berufung als kohärent statt widersprüchlich.

---

### Gesamteinschätzung (Anforderung → Argument-Robustheit)

| Anforderung aus `aufgabe.md` | Argumentativ tragfähig? |
|---|---|
| Teilaufgabe 1: Analyse bestehender Plattformen | ja, aber USP-Behauptung durch reale Gegen-App angreifbar (GS-1); Tabellenwertung vs. Text bei Foodsharing (GS-4) |
| Teilaufgabe 2: Konzeptentwicklung | ja; Herleitung überwiegend sauber, eine schiefe Nudge-Zuordnung (GS-2) |
| Teilaufgabe 3: Iteratives Design/Feedback | ja, als geplantes Vorgehen sauber gekennzeichnet; Zeitpuffer-Widerspruch (GS-3) |
| Transfer (gesellschaftlich ↔ wirtschaftlich) | wirtschaftlich seit Runde 1 bedient; gesellschaftlicher Anspruch in Spannung zur Verengung (GS-5) |
| Community-Building | ja; Verzicht auf Forum/Gruppen begründet, Soma-Doppelnutzung präzisierbar (GS-6) |
| UI/UX-Lieferobjekt | erledigt (2026-07-23) — echte Mockups eingebunden (Runde-1-Befund 1) |

Insgesamt eine argumentativ solide Arbeit, deren Kern (Marktlücke → literaturgestütztes Konzept, mit vorbildlicher Trennung von Beleg und eigener Leistung) trägt. Kein Befund dieser Runde ist abgabekritisch. Der gewichtigste ist GS-1 (reale Gegen-App), weil er das tragende Kernargument berührt und billig zu schärfen ist; GS-3 (Zeitpuffer) ist ein harter, sofort nachrechenbarer Konsistenzfehler. GS-2/GS-4/GS-5/GS-6 heben Präzision und Glaubwürdigkeit. Der zuvor einzige abgabekritische Punkt (fehlende Mockups, Runde-1-Befund 1) ist seit 2026-07-23 ebenfalls erledigt.

**Bekannter Hinweis (kein eigener Auftrag):** Die von der Gegenlesung (Prüferfrage 7) notierte USP-/„also"-Wiederholung über die Subsections besteht weiter — beim Abarbeiten ein bis zwei Wiederholungen straffen.

### Nächster Schritt

**Abgearbeitet (2026-07-21):** GS-1 bis GS-6 vollständig umgesetzt (GS-1 nach aktiver Rückfrage: volle Aufnahme von leftovercooking als 6. Plattform, mit Web-Recherche). `check_formalia.py` und `check_bib_keys.py` liefen fehlerfrei (0 FEHLER) auf allen betroffenen Kapiteln.

**Abgearbeitet (2026-07-23):** Runde-1-Befund 1 (UI/UX-Mockups) ebenfalls erledigt — vier echte Mockups eingebunden (siehe Befund-1-Status oben). Damit ist „Offen" jetzt vollständig leer.

Nächster Schritt laut Fahrplan: **Voll-Audit** (`pruef-modus`) — kein Delta-Re-Audit, da noch kein Vorbericht vorliegt.

---

## Runde 3 — Gegenlesung (2026-07-23)

Zweite kalte Prüfer-Gegenlesung gegen `aufgabe.md`, unabhängig durchgeführt: Erwartung erst aus `aufgabe.md` gebildet, dann Text + Anhang + Einbindung gelesen, erst danach diese Datei geöffnet. Kapitelplan, Prüfbericht, Projektstatus und Änderungshistorie wurden nicht als Maßstab herangezogen. Befunde sind gegen den **aktuellen Text** geprüft; wo ein Punkt Bereiche berührt, die frühere Runden bereits ansahen, steht er nur, weil er im aktuellen Text noch **lebt**.

### Soll-Ist-Tabelle (Schritt 3)

| Geforderter Inhalt (wörtlich aus `aufgabe.md`) | Erfüllung |
|---|---|
| Teilaufgabe 1: Analyse bestehender Plattformen (Stärken/Schwächen: Rezept-Austausch, **-Entdeckung**, Kommunikation) | erfüllt, aber „Rezept-Entdeckung" nicht als eigene Vergleichsdimension geführt (3.5); Matrix-Kalibrierung bei Chefkoch/leftovercooking fraglich (3.2, 3.3) — `sec:wettbewerbsanalyse`, `tab:wettbewerbsvergleich` (6 Plattformen) |
| Teilaufgabe 2: Konzeptentwicklung (Rezept-Teilen, Kochtipp-Austausch, gegenseitige Inspiration) | erfüllt — `sec:konzept`, `tab:funktionsuebersicht` |
| Teilaufgabe 3: Iteratives Design/Feedback (Beschreibung genügt) | erfüllt — `sec:community_und_feedback`, Beta-Gruppe/Sprints als geplantes Vorgehen |
| Berichtsinhalt: Zielgruppe | erfüllt — `sec:zielgruppe` + Persona `tab:persona` (Anhang A) |
| Berichtsinhalt: Funktionalitäten | erfüllt — `sec:konzept` |
| Berichtsinhalt: UI/UX | erfüllt — `sec:konzept` (3 Bereiche) + 4 Mockups Anhang B; alle 4 PNG real unter `images/durchfuehrung/`; Einbindung ins Gesamtdokument nicht aus zulässigen Dateien prüfbar (3.8) |
| Berichtsinhalt: Community-Building | erfüllt — Rettungs-Feed + Challenges; Forum/Gruppen begründet ausgeschlossen |
| Objekt: Wettbewerbsvergleich (Tabelle) | erfüllt — `tab:wettbewerbsvergleich` |
| Objekt: Persona (Text/Abb.) | erfüllt — `tab:persona` |
| Objekt: UI/UX-Mockup (ggf. KI-generiert, gekennzeichnet) | erfüllt — 4 PNG, KI-Kennzeichnung im Pflichtmuster |
| Objekt: Plattformname | erfüllt — „Resteria", hergeleitet, gegen „Restlos Glücklich" abgegrenzt |
| Objekt: Funktionsübersicht | erfüllt — `tab:funktionsuebersicht` |
| Objekt: Phasenplanung (Tabelle) | erfüllt — `tab:phasenplanung` mit Zeitrahmen + Ressourcen |
| Schlüsselbegriff: Rezept-Uploads (Foto/Video) | erfüllt |
| Schlüsselbegriff: Kommentar-/Bewertungssystem | erfüllt |
| Schlüsselbegriff: Personalisierte Empfehlungen | erfüllt |
| Schlüsselbegriff: Gruppen/Foren | erfüllt — beide begründet ausgeschlossen (Soma et al.) |
| Schlüsselbegriff: Event-Kalender (bei Auslassung begründen) | erfüllt — Verzicht in `sec:konzept` begründet |
| Schlüsselbegriff: Lebensmittel-Journaling/Menüplanung | erfüllt — Reste-Journal an Rettungspunkte gekoppelt |
| Verengung Zielgruppe (begründet) | erfüllt — Einleitung + `sec:zielgruppe`, argumentativ |
| Nachprüfbarkeit der Wettbewerbsanalyse | erfüllt, aber „App-Test der Verbraucherzentrale" namentlich genannt, ohne `\parencite`/Bib-Eintrag (3.4); Marktbehauptung unbelegt (3.6) |
| Materialien Hansch & Rentschler (2012); Kapoor et al. (2018) | nicht erfüllt — fehlen in Text und `references.bib`; laut `aufgabe.md` nicht Pflicht (3.7) |
| Formal: 5–10 Quellen | erfüllt — 6 Einträge in `references.bib` |
| Formal: 7–10 Seiten / Struktur-% | nicht aus dem Text prüfbar (Build/`pruef-modus`) |

---

### Befund 3.1 — Zähl-/Aufzählungsdrift nach Aufnahme der sechsten Plattform  🔴 hart

- **Status: ERLEDIGT (2026-07-23).** „drei Einwände" → „vier Einwände" in `01_wettbewerbsanalyse.tex:34`; „ein bis zwei Vertretern" → „ein bis drei Vertretern" in `02_limitationen.tex:7`. Rein mechanisch, keine inhaltliche Änderung.
- **Befund**: Zwei Zählangaben stimmen nach der Aufnahme von leftovercooking nicht mehr mit dem eigenen Text überein:
  - `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:34`: „Gegen diese Einschätzung lassen sich **drei** Einwände vorbringen." — aufgezählt werden aber **vier** (Erstens / Zweitens / Drittens / **Viertens** = leftovercooking).
  - `chapters/03_fazit/02_limitationen.tex:7`: „sechs Vertreter aus drei Plattform-Kategorien … bei der **jede Kategorie mit ein bis zwei Vertretern** belegt ist." Die Reste-Matching-Kategorie hat jedoch **drei** Vertreter (Restegourmet, BMEL-App, leftovercooking).
- **Warum ein Prüfer das anstreicht**: Zählangaben gegen den eigenen Text sind der billigste Konsistenz-Check überhaupt. „Drei" unmittelbar vor vier sichtbar nummerierten Punkten ist ein harter, sofort auffallender Fehler; er trifft Qualität (Sorgfalt) und Dokumentation und wirkt wie ein nicht nachgezogener Editierstand.
- **Anweisung**: In `01_wettbewerbsanalyse.tex:34` „drei Einwände" → „vier Einwände". In `02_limitationen.tex:7` „ein bis zwei Vertretern" → „ein bis drei Vertretern" (oder Satz so umformulieren, dass die Reste-Matching-Kategorie mit drei Vertretern gedeckt ist). Rein mechanisch, keine inhaltliche Änderung.

### Befund 3.2 — Chefkoch: Prosa „aktiver Austausch" gegen Matrix-Wertung „Community mittel"  🟠 mittel  [FREIGABE]

- **Status: ERLEDIGT (2026-07-23), Nutzer-Entscheidung nach Rückfrage: Option (a) mit Web-Faktencheck.** Websuche zu Chefkoch.de-Community bestätigt aktiven Austausch über Kommentare, Bewertungen und Tipp-Weitergabe zwischen Nutzer:innen (mehrere unabhängige App-Reviews). Zelle in `tab:wettbewerbsvergleich` auf „stark" gehoben; in `01_wettbewerbsanalyse.tex:3` ein Satz ergänzt, der die Einstufung explizit an das Matrix-Kriterium bindet.
- **Befund**: `01_wettbewerbsanalyse.tex:3` beschreibt Chefkoch.de so, dass Nutzer:innen „bewerten fremde Beiträge und kommentieren sie, wodurch ein **aktiver Austausch** rund um einzelne Gerichte entsteht." `tab:wettbewerbsvergleich` (`:21`) wertet Chefkoch bei Community-Funktionen jedoch nur **„mittel"**. Die Kriteriendefinition (`:13`) macht „stark" an „tatsächlichem Austausch zwischen Nutzer:innen, etwa über Kommentare" fest — genau das schreibt die Prosa Chefkoch zu.
- **Warum ein Prüfer das anstreicht**: Fazit und Kreativitäts-Bewertung (Vergleich zu Bestehendem) ruhen auf der Matrix. Wer die als „aktiv" beschriebene Chefkoch-Community neben die „mittel"-Zelle legt, liest die Wertung als ergebnisorientiert: Die Community-Plattformen werden tendenziell heruntergestuft, damit die USP-Lücke größer erscheint. Das ist der klassische Verdacht der Selbstbewertung zum eigenen Vorteil.
- **Anweisung**: Optionen — **(a)** Chefkoch Community-Funktionen auf „stark" heben und im Fließtext klarstellen, warum Chefkoch die Lücke dennoch nicht schließt (kein Reste-Matching-Werkzeug); **(b)** im Chefkoch-Absatz präzisieren, warum der Austausch trotz Aktivität nur „mittel" trägt (z. B. rezept- statt reste-fokussiert, keine Gamification), sodass Prosa und Zelle konsistent lesen. Berührt eine eigene Bewertung → **[FREIGABE]**.

### Befund 3.3 — leftovercooking: die USP-tragende Community-Zelle „mittel" gegen das eigene Kriterium  🟠 mittel  [FREIGABE]

- **Status: ERLEDIGT (2026-07-23), Nutzer-Entscheidung nach Rückfrage: Halbsatz zur Abgrenzung.** In `01_wettbewerbsanalyse.tex:9` ergänzt: Das Belohnungspunkte-System ist individuelles Spar-Feedback ohne Bezug zu anderen Nutzer:innen und zählt damit nicht als die im Kriterium gemeinte, sozial-interaktive Gamification. Zelle „mittel" bleibt unverändert, jetzt aber begründet.
- **Befund**: `01_wettbewerbsanalyse.tex:9` schreibt leftovercooking „ein **Belohnungspunkte-System**" zu (= Gamification). Das Matrix-Kriterium (`:13`) zählt „Gamification" ausdrücklich als Merkmal, das Community-„stark" begründet. Dennoch erhält leftovercooking Community **„mittel"** (`:25`) — und genau diese eine Zelle trägt die gesamte USP-Behauptung („leftovercooking kommt am nächsten, bleibt aber auf Creator-Inhalte beschränkt", `:32`, Fazit `01_kernergebnisse_und_ausblick.tex:7`).
- **Warum ein Prüfer das anstreicht**: Das tragende Kernargument (Reste-Matching **plus** echte Social-Community sei einzigartig) steht und fällt mit dieser Wertung. Solange nicht ausdrücklich steht, warum leftovercookings Punktesystem **nicht** die vom Kriterium gemeinte „Gamification" ist, wirkt die entscheidende Zelle zu bequem für die eigene These. Kreativität und Qualität sind betroffen.
- **Anweisung**: In `01_wettbewerbsanalyse.tex` einen Halbsatz ergänzen, der leftovercookings Belohnungspunkte als **individuelles Spar-Feedback** (Anzeige gesparter Geldbeträge, kein Austausch zwischen Nutzer:innen) vom kriterienrelevanten, **sozial-interaktiven** Gamification-Begriff abgrenzt — dann trägt „mittel". Alternativ die Kriteriendefinition (`:13`) so schärfen, dass „Gamification" nur zählt, wenn sie interaktiv zwischen Nutzer:innen wirkt. Berührt Kernargument + eigene Recherche → **[FREIGABE]**.

### Befund 3.4 — „App-Test der Verbraucherzentrale" namentlich, aber unbelegt  🟠 mittel  [FREIGABE]

- **Status: ERLEDIGT (2026-07-23), Nutzer-Entscheidung nach Rückfrage: Verweis streichen.** „gestützt durch einen unabhängigen App-Test der Verbraucherzentrale" aus `01_wettbewerbsanalyse.tex:9` entfernt; leftovercooking-Bewertung läuft jetzt durchgängig als „eigene Sichtung (Stand: Juli 2026)". Folgesatz „im Test" auf „dabei" angepasst, damit kein Testbezug mehr suggeriert wird.
- **Befund**: `01_wettbewerbsanalyse.tex:9`: „Nach eigener Sichtung (Stand: Juli 2026), **gestützt durch einen unabhängigen App-Test der Verbraucherzentrale**, erfasst leftovercooking …". Auf diesen Test stützen sich konkrete Tatsachenangaben (über zwanzig Food-Creator:innen, Belohnungspunkte-System, kein belegter Peer-Austausch). `references.bib` enthält dazu keinen Eintrag (nur 6 Keys: barker, nivedhitha, shen, soma, un, vittuari).
- **Warum ein Prüfer das anstreicht**: Eine namentlich genannte externe Quelle ohne `\parencite` ist nicht nachprüfbar — das wirkt schwächer, als sie gar nicht zu nennen. Trifft Nachvollziehbarkeit/Dokumentation, zusätzlich verschärft, weil die konkrete Einordnung der wichtigsten Gegen-App (leftovercooking) auf diesem Test beruht.
- **Anweisung**: Entweder den Verbraucherzentrale-App-Test in Zotero/BBT aufnehmen und in `01_wettbewerbsanalyse.tex:9` per `\parencite` belegen (bevorzugt), **oder** — falls kein zitierfähiger Test greifbar ist — den namentlichen Verweis streichen und die leftovercooking-Bewertung ausschließlich als „eigene Sichtung (Stand: Juli 2026)" führen. Berührt eigene Recherche → **[FREIGABE]**.

### Befund 3.5 — „Rezept-Entdeckung" fehlt als eigene Vergleichsdimension  🟠 mittel  [FREIGABE]

- **Status: ERLEDIGT (2026-07-23), Nutzer-Entscheidung nach Rückfrage: neue Matrixspalte.** `tab:wettbewerbsvergleich` um die Spalte „Rezept-Entdeckung" erweitert (fünf statt vier Kriterien) und je Plattform bewertet; Kriterien-Absatz in `01_wettbewerbsanalyse.tex:13` um eine Definition ergänzt, die Rezept-Entdeckung (allgemeine Auffindbarkeit) vom bestehenden Kriterium Reste-Matching-Werkzeug (reste-spezifische Suche) abgrenzt.
- **Befund**: Teilaufgabe 1 verlangt wörtlich Stärken/Schwächen bzgl. „Rezept-Austausch, **-Entdeckung** und Kommunikation" (`aufgabe.md`). `tab:wettbewerbsvergleich` führt die vier Achsen Rezept-Austausch, Community-Funktionen, Nachhaltigkeits-/Restefokus, Reste-Matching-Werkzeug — „Rezept-Entdeckung" ist **keine eigene Achse**. Im Prosatext wird Suche/Auffindbarkeit je Plattform gestreift („Wer nach einem bestimmten Gericht sucht, findet auf Chefkoch.de schnell Ergebnisse"), aber nicht systematisch verglichen.
- **Warum ein Prüfer das anstreicht**: Qualität misst u. a. Vollständigkeit gegen die wörtliche Aufgabenstellung. Eine der drei ausdrücklich genannten Analyse-Achsen taucht nicht als Vergleichskriterium auf; ein Prüfer, der die Aufgabe neben die Matrix legt, sieht die Auslassung sofort.
- **Anweisung**: Optionen — **(a)** eine Spalte „Rezept-Entdeckung/Auffindbarkeit" in `tab:wettbewerbsvergleich` ergänzen und je Plattform bewerten; **(b)** im Fließtext je Plattform-Kategorie einen Satz ergänzen, der die Auffindbarkeit ausdrücklich als eine der drei geforderten Achsen adressiert und benennt, dass „Reste-Matching-Werkzeug" die reste-spezifische Entdeckung abbildet. Berührt die Wettbewerbsmatrix (eigene Recherche) → **[FREIGABE]**.

### Befund 3.6 — Unbelegte Marktbehauptung stützt die wirtschaftliche Transfer-Dimension  🟡 leicht

- **Status: ERLEDIGT (2026-07-23).** „Der wachsende Markt für Zero-Waste-Produkte und -Dienstleistungen macht dieses kommerzielle Umfeld tragfähig" in `03_konzept.tex:5` zu „Angesichts der steigenden gesellschaftlichen Aufmerksamkeit für Nachhaltigkeit und Zero-Waste erscheint dieses kommerzielle Umfeld tragfähig" abgeschwächt — keine belegbedürftige Tatsachenbehauptung mehr.
- **Befund**: `03_konzept.tex:5`: „Der **wachsende Markt** für Zero-Waste-Produkte und -Dienstleistungen macht dieses kommerzielle Umfeld tragfähig." Diese Marktaussage trägt die wirtschaftliche Seite des Transfer-Kriteriums, ist aber ohne Quelle.
- **Warum ein Prüfer das anstreicht**: Transfer (15 %) verlangt eine begründete wirtschaftliche Einordnung. Eine unbelegte Marktwachstums-Behauptung ist die schwächste Stelle einer sonst sauber belegten Argumentation und lädt zur Rückfrage „woher?" ein.
- **Anweisung**: Entweder mit einer Quelle (Marktstudie/Branchenzahl) belegen, **oder** vorsichtiger als Annahme formulieren („angesichts der steigenden Aufmerksamkeit für Nachhaltigkeit …"), sodass keine belegbedürftige Tatsachenbehauptung stehen bleibt. Ein Satz genügt.

### Befund 3.7 — Genannte Einstiegsliteratur (Hansch & Rentschler; Kapoor et al.) nicht aufgegriffen  🟢 Hinweis (optional)

- **Status: ÜBERSPRUNGEN (2026-07-23).** Beide Quellen fehlen weiterhin in `references.bib` (geprüft per grep). Da der Befund ausdrücklich als „nicht Pflicht" markiert ist und ein Einbau einen vorherigen Zotero-Import erfordern würde, bewusst nicht erzwungen — identisch zur Entscheidung bei Runde-1-Befund 6.
- **Befund**: Beide in `aufgabe.md` genannten Materialien (Hansch & Rentschler 2012 — Emotion@Web; Kapoor et al. 2018 — Advances in Social Media Research) tauchen weder in `references.bib` noch im Text auf.
- **Warum ein Prüfer das anstreicht**: `aufgabe.md` markiert sie ausdrücklich als „nicht Pflicht, aber sinnvoller Einstieg" — also **kein FAIL**. Manche Prüfer werten es dennoch positiv, wenn die selbst empfohlene Einstiegsliteratur wenigstens gestreift wird.
- **Anweisung (optional)**: Falls beim Abarbeiten inhaltlich passend, eine der beiden Quellen einbauen (Kapoor et al. bei den Social-Media-Funktionen, Hansch & Rentschler bei der UI/UX-Emotionalität). Nur wenn es sich natürlich fügt — nicht erzwingen.

### Befund 3.8 — Anhang-Einbindung nicht aus zulässigen Dateien verifizierbar  🟢 Grenzvermerk

- **Status: KEIN TEXTAUFTRAG — an Voll-Audit weitergereicht.** `main.tex` bindet Anhang und Verzeichnisse laut Projektstatus (`CLAUDE.md`) bereits seit 2026-07-23 ein; der Teil-Check D (Build) im `pruef-modus` prüft das verbindlich, sobald der Nutzer lokal kompiliert.
- **Befund**: `pages/chapters.tex` bindet ausschließlich die drei Kapitel ein; `pages/appendix.tex` (Persona + 4 Mockups) wird dort **nicht** referenziert. Fünf `\autoref`-Ziele — `tab:persona`, `fig:mockup_start`, `fig:mockup_start_bookmarks`, `fig:mockup_profil`, `fig:mockup_feed` — liegen in `appendix.tex`. Ob der Anhang ins kompilierte Dokument gelangt, wird in `main.tex` entschieden; `main.tex` liegt laut Auftrag **außerhalb meines Lesebereichs**, daher kalt nicht abschließend prüfbar.
- **Warum ein Prüfer das anstreicht**: Wären Anhang und Mockups nicht eingebunden, blieben fünf `\autoref` unaufgelöst und ein wörtlich gefordertes Lieferobjekt (UI/UX) fehlte im PDF, obwohl die Dateien vorhanden sind. Kalt gelesen ist das ein offener Punkt.
- **Anweisung**: Grenzvermerk, kein Textänderungsauftrag. Im Voll-Audit (`pruef-modus`, Build-Check) bzw. beim lokalen Kompilieren sicherstellen, dass `main.tex` den Anhang einbindet und die fünf Anhang-`\autoref` sauber auflösen.

---

### Die sieben Prüferfragen (Schritt 4)

1. **Existiert, was behauptet wird?** → Ja. Alle vier Mockup-PNG liegen real unter `images/durchfuehrung/`, alle Tabellen (Wettbewerb, Funktionen, Persona, Phasen) und die Funktionslogik-Abbildung existieren. Offen bleibt nur die **Einbindung** des Anhangs ins Gesamtdokument (3.8, Grenzvermerk).
2. **Teilaufgabe ersetzt statt ausgeführt?** → Nein. Feedback-Schleifen sauber als „geplantes Vorgehen" gekennzeichnet (von `aufgabe.md` gedeckt), fehlender Nutzertest ebenfalls gedeckt und offen als Limitation benannt.
3. **Jede Behauptung nachprüfbar?** → Verhaltensliteratur durchweg mit `\parencite` + Seitenzahlen. Lücken: Verbraucherzentrale-App-Test namentlich, aber unbelegt (3.4); Marktbehauptung „wachsender Markt" unbelegt (3.6).
4. **Zentralbegriff stillschweigend verengt?** → Zielgruppen-Verengung explizit benannt und begründet (legitim). „Rezept-Entdeckung" als Analyse-Achse still absorbiert statt ausgewiesen (3.5).
5. **Widerspruch in eigenen Festlegungen?** → „drei Einwände" + vier gelistet, „ein bis zwei Vertreter" trotz drei Reste-Apps (3.1); Chefkoch „aktiver Austausch" (Prosa) vs. „mittel" (Matrix, 3.2). Die SDG-12.3-vs-Verengung-Spannung wird dagegen **selbst erhoben und beantwortet** (`sec:evaluation_reflexion`) — das ist eine Stärke, kein Befund.
6. **Eigene Bewertung ergebnisorientiert?** → Die beiden Community-Wertungen, auf denen die USP ruht, laden dazu ein: Chefkoch „mittel" trotz Prosa „aktiver Austausch" (3.2) und leftovercooking „mittel" trotz eigenem Gamification-Kriterium (3.3). Kein Beweis für Ergebnisorientierung, aber der wahrscheinlichste Angriffspunkt.
7. **Wirkt es wie ein KI-Text?** → Überwiegend menschlich, mit echter Reflexion (Lessons Learned, Auflösung der SDG-Spannung, vorsichtige Einordnung der Soma-Zahl). Mild auffällig: durchgängig triadische „Erstens/Zweitens/Drittens"-Gerüste (Zielgruppe, Limitationen, Lessons Learned, Einwände). Der „drei Einwände/vier"-Bruch (3.1) ist zugleich ein Editier-Artefakt genau dieses Musters. Kein Regelverstoß gegen `hard-rules-formal.md`.

---

### Bewertungskriterien je Dimension (Schritt 5)

| Kriterium (Gewicht) | Dimension | Urteil |
|---|---|---|
| Qualität (25 %) | Vollständigkeit der Teilaufgaben | abgedeckt |
| | Inhaltliche Richtigkeit | schwach — Matrix-Kalibrierung (3.2, 3.3), Zählfehler (3.1) |
| | Zielerreichung | abgedeckt (`sec:evaluation_reflexion` prüft explizit) |
| Prozess (25 %) | Vorgehen dokumentiert | abgedeckt |
| | Reflektiert | abgedeckt |
| | Grenzen aufgezeigt | abgedeckt (dreischichtige Limitationen) |
| Transfer (15 %) | Gesellschaftliche Bedeutung | abgedeckt (SDG 12.3, Haushaltsabfall) |
| | Wirtschaftliche Bedeutung | schwach — Freemium/Kooperationen da, aber unbelegte Marktbehauptung (3.6) |
| | Ansätze/Modelle begründen | abgedeckt (Drivers/Levers, Nudges, Gamification) |
| Kreativität (15 %) | Vergleich zu bestehendem Produkt | abgedeckt (6 Plattformen) — Überzeugungskraft leidet unter 3.2/3.3 |
| | Innovationskraft | abgedeckt (Kombination als USP, ehrlich als inkrementell gerahmt) |
| Dokumentation (10 %) | Entstehungsgeschichte | abgedeckt |
| | Lückenlosigkeit/Nachvollziehbarkeit | schwach — unbelegter Verbraucherzentrale-Test (3.4), „eigene Sichtung" ohne dokumentierte Grundlage |
| Ressourcen (10 %) | Zeiteinsatz | abgedeckt (Phasenplanung, Zeitpuffer) |
| | Materialeinsatz | abgedeckt (Ressourcen-Spalte) |

---

### Tragende Stärken (Ehrlichkeitspflicht — beim Überarbeiten nicht wegschreiben)

- **Trennung von Beleg und Eigenleistung**: `03_konzept.tex:30` ordnet die Soma-Zahl (51 % vs. 39 %) ausdrücklich nur der grundsätzlichen Gamification-Wirkung zu, nicht der konkreten Resteria-Mechanik. Diese Vorsicht ist ein Qualitätsmerkmal und **darf nicht geglättet werden**.
- **Selbst erhobener, beantworteter Einwand**: Die Spannung zwischen SDG-12.3-Breitenanspruch und der Verengung auf bereits Motivierte wird in `sec:evaluation_reflexion` benannt **und** aufgelöst (Nische → mittelbare Breitenwirkung über Partnerschaften). Das nimmt einem Prüfer den naheliegendsten Angriff vorweg.
- **Begründete Auslassungen statt stiller Lücken**: Event-Kalender und Forum/Gruppen werden aktiv und mit Beleg (Soma et al.) ausgeschlossen, nicht übergangen.
- **Verengung sauber deklariert**, Verhaltensliteratur durchgehend belegt, Limitationen dreischichtig, Phasenplanung mit Abhängigkeiten und Risiken — die Prozess-Dimension ist durchweg stark.

---

### Gesamteinschätzung

Eine inhaltlich tragfähige, formal weit gediehene Arbeit, die alle drei Teilaufgaben und alle wörtlich geforderten Berichtsinhalte mit **real vorhandenen** Artefakten bedient. **Kein Befund dieser Runde ist abgabekritisch.** Die gewichtigsten Punkte konzentrieren sich auf die Wettbewerbsmatrix — den Kern der eigenen Recherche und damit den wahrscheinlichsten Angriffspunkt auf Qualität und Kreativität: der harte Zählfehler (3.1) sowie die Kalibrierung der beiden Community-Wertungen, auf denen die USP ruht (3.2 Chefkoch, 3.3 leftovercooking), plus die unbelegte Stütze der leftovercooking-Einordnung (3.4). **3.1 ist der einzige harte Fehler und rein mechanisch zu beheben.** 3.5 (fehlende Entdeckungs-Achse) betrifft die wörtliche Erfüllung der Aufgabe. 3.6–3.8 sind Feinschliff bzw. ein Build-Grenzvermerk.

**Umfangshinweis**: Alle Zugaben sind klein — Halbsätze (3.2, 3.3, 3.4, 3.6), ein bis zwei geänderte Zahlwörter (3.1), optional eine zusätzliche Matrixspalte (3.5), optional ein Bib-Eintrag (3.4/3.7). Bei 7–10 Seiten Zielkorridor entsteht **kein Kürzungsdruck**; eine zusätzliche Matrixspalte verbreitert nur die bestehende Tabelle.

**Freigabepflichtig**: 3.2, 3.3, 3.4 und 3.5 berühren die eigene Wettbewerbsbewertung, das Kernargument bzw. eigene Rechercheergebnisse und sind daher **[FREIGABE]** — im `schreib-modus` aktiv per `AskUserQuestion` klären, nicht stillschweigend umsetzen. 3.1, 3.6, 3.7, 3.8 sind ohne Freigabe umsetzbar (Zahlkorrektur, Belegformulierung, optionaler Einbau, Build-Check).

### Nächster Schritt

**Abgearbeitet (2026-07-23):** Alle acht Befunde (3.1–3.8) bearbeitet. 3.1, 3.6 mechanisch ohne Freigabe umgesetzt. 3.2–3.5 (`[FREIGABE]`) per `AskUserQuestion` einzeln geklärt: 3.2 Chefkoch-Zelle auf „stark" gehoben (mit Web-Faktencheck zur Community-Aktivität), 3.3 Halbsatz zur Gamification-Abgrenzung bei leftovercooking, 3.4 unbelegter Verbraucherzentrale-Verweis gestrichen, 3.5 neue Matrixspalte „Rezept-Entdeckung" ergänzt. 3.7 (optionale Literatur) übersprungen wie in Runde 1. 3.8 ist ein reiner Build-Grenzvermerk ohne Textauftrag. `check_formalia.py` (0 FEHLER, nur bekannte Satzlängen-Hinweise) und `check_bib_keys.py` (alle 6 Keys valide) auf allen betroffenen Dateien bestätigt. Damit ist „Offen" wieder vollständig leer.

Nächster Schritt laut Fahrplan: **Voll-Audit** (`pruef-modus`) — prüft insbesondere die neue Matrixspalte, die veränderten Chefkoch-/leftovercooking-Wertungen und Teil-Check D (Build/Anhang-Einbindung, Befund 3.8).
