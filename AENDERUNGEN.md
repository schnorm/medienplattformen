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

---

## Runde 4 — Nutzer-Feedback / Umfangsanalyse (2026-07-24)

Anlass: gezielte Suche nach Kürzungspotenzial im Fließtext, ohne Informationsverlust. Grundlage ist eine Wortzählung über alle 14 `chapters/**/*.tex` (Tabellen-/Abbildungsumgebungen und Zitationsbefehle herausgerechnet) plus das Layout aus `main.tex` (11pt, 2 cm Ränder, `\onehalfspacing`).

### Ausgangsbefund

- **4.508 Wörter Fließtext.** Bei 17 cm Satzbreite und 11pt/1,5-zeilig entspricht das grob **8,5–9 Seiten reinem Text**, plus 3 Tabellen und 1 Abbildung im Textteil (~1,5–2 Seiten) → geschätzt **10–11 Seiten Textteil**. Vorgabe laut `aufgabe.md:18`: **7–10 Seiten**.
- Der letzte vorliegende Build (`main.pdf`, Stand 2026-07-23) hat **17 Seiten gesamt** inkl. Front-Matter, Literaturverzeichnis und Anhang. Der Textteil daraus ließ sich ohne Renderer nicht sauber isolieren.
- Kapitelanteile aktuell: Einleitung 14,3 % · Durchführung 70,8 % · Fazit 14,9 % — alle innerhalb der Vorgabe (`aufgabe.md:20`), aber Einleitung und Fazit stehen **am oberen Rand** ihrer Bänder. Kürzungen dürfen deshalb nicht ausschließlich in der Durchführung erfolgen, sonst kippen die Anteile.

**Zielkorridor dieser Runde: 600–900 Wörter (13–20 %).** Diese Menge lässt sich vollständig aus Redundanz holen; keiner der Punkte unten verlangt, eine Information aufzugeben.

### 4.0 Vorbedingung — Build vor der Umsetzung  🟢 Nutzer-Schritt

- **Status: NUTZER-SCHRITT, ohne Messwert fortgesetzt (2026-07-24).** `lualatex`/`latexmk` sind in dieser Umgebung weiterhin nicht installiert. Nutzer-Entscheidung nach Rückfrage: alle Punkte 4.1–4.8 ohne Messwert umsetzen. Der tatsächliche Seitenumfang bleibt eine Nutzer-Pflicht vor Abgabe (siehe `pruefbericht.md` → „Vor der Einreichung").
- **Befund**: Der tatsächliche Textteil-Umfang ist nicht verifiziert. Die 10–11 Seiten sind eine Schätzung aus Wortzahl und Layout, kein Messwert; `pruef-modus` Teil-Check D (Build) war in allen bisherigen Läufen ÜBERSPRUNGEN, weil `lualatex`/`biber` in der Session-Umgebung fehlen.
- **Warum**: `hard-rules-formal.md:67` — Nicht-Erfüllung des Seitenumfangs kann Punktabzug bedeuten. Die Kürzungsmenge hängt direkt am Messwert.
- **Anweisung**: Vor Umsetzung dieser Runde lokal `latexmk -lualatex main.tex` fahren und den Textteil ab „1 Einleitung" bis vor das Literaturverzeichnis zählen. Ergebnis hier eintragen. **Landet der Textteil bei ≤ 9,5 Seiten, genügen die Punkte 4.1–4.4** (~500 Wörter); die restlichen Punkte sind dann optionaler Feinschliff, keine Pflicht.

---

### Befund 4.1 — Die vier Einwände am Ende der Wettbewerbsanalyse wiederholen den eigenen Fließtext  🟠 mittel · **[FREIGABE]** (berührt die Verteidigung des Kernarguments/USP)

- **Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: wie vorgeschlagen umgesetzt.** Einwände 1, 3 und 4 zu einem Satz zusammengezogen (Verweis auf die oben bereits gegebenen Belege statt Wiederholung), Einleitungssatz auf „zwei Einwände" angepasst. Einwand 2 sowie der USP-Schlusssatz („Die USP von Resteria liegt damit nicht im bloßen Verbinden …") wörtlich erhalten.
- **Befund**: `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:34` — ein Absatz von **216 Wörtern**, der größte Einzelposten der Arbeit. Drei der vier Einwände sind bereits im Fließtext desselben Kapitels abgehandelt: Einwand 1 (Reste-Matching nicht neu) in Absatz 3, Einwand 3 (Foodsharing.de) in Absatz 5, Einwand 4 (leftovercooking) in Absatz 4. Der Text gibt die Doppelung selbst zu — die Formulierung „wie oben gezeigt" steht zweimal darin. Nur Einwand 2 (eine reine Zero-Waste-Community ohne Matching-Werkzeug würde genügen) bringt ein Argument, das an keiner anderen Stelle steht.
- **Warum**: Reine Redundanz, kein Informationsverlust bei Kürzung. Zusätzlich Wirkung auf „Qualität": Ein Prüfer liest dieselbe Verteidigung dreifach als Unsicherheit, nicht als Gründlichkeit. Der Absatz ist ein sichtbares Artefakt des Gesamt-Stresstests, kein organischer Teil der Argumentation.
- **Anweisung**: Einwand 2 vollständig erhalten (er ist das einzige neue Argument). Einwände 1, 3 und 4 zu **einem** Satz zusammenziehen, der auf die bereits gegebenen Belege verweist statt sie zu wiederholen — etwa: dass Reste-Matching, Foodsharing.de und leftovercooking den Befund je aus anderer Richtung berühren, ohne die Kombination aus Matching und wechselseitiger Peer-Community zu leisten (Begründung jeweils oben). Der Schlusssatz zur USP („nicht im bloßen Verbinden beider Elemente, sondern in einer echten, wechselseitigen Social-Community obendrauf") **bleibt wörtlich erhalten** — er trägt das Kernargument.
- **Erwarteter Ertrag**: ~150 Wörter

---

### Befund 4.2 — Der Kernbefund steht fünfmal ausformuliert  🟠 mittel · **[FREIGABE]** (berührt die Darstellung des Kernarguments)

- **Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: wie vorgeschlagen umgesetzt.** Fazit-Absatz 1 und 3 verschmolzen: Marktlücke und die Feststellung, dass die Differenzierung aus der eigenen Wettbewerbsanalyse (nicht aus der Literatur) stammt, stehen jetzt in einem Absatz. Der tragende Trennungssatz („Diese Trennung zwischen literaturbasierten Hebeln und eigenständig hergeleitetem Alleinstellungsmerkmal …") wörtlich erhalten, aber ans Ende des Literatur-Absatzes verschoben, wo er inhaltlich unmittelbar auf die dort genannten Hebel folgt. Limitationen-Schlussabsatz auf die Kernaussage gekürzt, ohne die Plattformkategorien erneut aufzuzählen.
- **Befund**: Die Aussage „Community-Plattformen bieten kein Reste-Matching, Matching-Apps keine echte Community, leftovercooking kommt am nächsten, bleibt aber bei Creator-Inhalten" steht ausformuliert an fünf Stellen: `chapters/01_einleitung/01_ausgangslage_und_problem.tex:7`, `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:32`, nochmals in `:34`, `chapters/03_fazit/01_kernergebnisse_und_ausblick.tex:3` **und** ein zweites Mal in Absatz 3 derselben Datei (85 + 79 Wörter, inhaltlich stark überlappend), schließlich im Schlussabsatz von `chapters/03_fazit/02_limitationen.tex:9`.
- **Warum**: `hard-rules-formal.md:88` verlangt ausdrücklich, dass Fazit und Reflexion Kernaussagen **paraphrasieren** statt nahezu wortgleich zu übernehmen. Zugleich der wirksamste Hebel für das Fazit, das mit 14,9 % am oberen Rand seines 10–15-%-Bandes liegt.
- **Anweisung**: Die Erstnennung in der Einleitung und die Herleitung in der Wettbewerbsanalyse (`:32`) bleiben unverändert — dort gehört der Befund hin. Im Fazit **Absatz 1 und Absatz 3 zu einem Absatz verschmelzen**: Die Marktlücke einmal nennen, direkt gefolgt von der Feststellung, dass die Differenzierung aus der eigenen Wettbewerbsanalyse stammt und nicht aus der Literatur. Der Schlussabsatz der Limitationen kürzt sich auf die Kernaussage ohne erneute Aufzählung der Plattformkategorien.
- **Nicht anfassen**: Der Satz in Fazit-Absatz 3, der die Trennung zwischen literaturbasierten Hebeln und eigener Marktbeobachtung explizit macht („hält den Bericht davon ab, den gesamten Marktvorteil … als wissenschaftlich bewiesen darzustellen"), ist eine tragende Stärke laut Runde 3 und **darf nicht wegfallen** — nur seine Einbettung wird gestrafft.
- **Erwarteter Ertrag**: ~120 Wörter

---

### Befund 4.3 — `06_evaluation_reflexion.tex` beginnt mit zwei Abhaklisten  🟠 mittel

- **Status: ERLEDIGT (2026-07-24).** Absätze 1 und 2 zu einem Absatz zusammengeführt; Teilaufgaben und Berichtsinhalte laufen jetzt in einem Durchgang, mit `\autoref` statt ausformulierter Kapitelbeschreibung. Absätze 3–5 (SDG-Spannung, Prozess-Reflexion, drei Lehren) unverändert.
- **Befund**: `chapters/02_durchfuehrung/06_evaluation_reflexion.tex` — Absatz 1 (67 Wörter) hakt die drei Teilaufgaben ab, Absatz 2 (107 Wörter) hakt die vier geforderten Berichtsinhalte ab. Zusammen **174 Wörter**, die ausschließlich auf Kapitel verweisen, die der Prüfer unmittelbar zuvor gelesen hat.
- **Warum**: Die Selbstprüfung gegen die Aufgabenstellung ist sinnvoll und soll bleiben, aber zwei getrennte Listen mit identischer Funktion sind eine Verdopplung. Ein verdichteter Absatz erfüllt denselben Zweck.
- **Anweisung**: Absätze 1 und 2 zu einem Absatz zusammenführen: Teilaufgaben und Berichtsinhalte in einem Durchgang benennen, je mit `\autoref` statt ausformulierter Beschreibung des jeweiligen Kapitelinhalts.
- **Nicht anfassen**: Absatz 3 (SDG-12.3-Spannung und ihre Auflösung) und Absatz 5 (drei Lehren) sind Substanz — „Prozess" (25 %) und „Transfer" (15 %) sind zusammen 40 % der Bewertung, und die selbst erhobene und beantwortete SDG-Spannung ist laut Runde 3 eine tragende Stärke. Ebenso bleibt Absatz 4 (Reflexion des Vorgehens) unverändert.
- **Erwarteter Ertrag**: ~80 Wörter

---

### Befund 4.4 — Ankündigungs- und Meta-Text kündigt an, was der nächste Absatz ohnehin tut  🟠 mittel

- **Status: ERLEDIGT (2026-07-24), leicht abweichend von der Anweisung.** `03_vorgehen_und_aufbau.tex` Absatz 2 auf vier statt zwei Sätze gestrafft (Trichter-Logik erhalten, Subsection-für-Subsection-Aufzählung samt Funktionsnamen entfernt) — eine Kürzung auf exakt zwei Sätze hätte die Datei laut Nachkontrolle auf ~113 Wörter gedrückt und damit unter die HALBSEITE-Schwelle (150 Wörter) gezogen; mit vier Sätzen bleibt sie bei ~156 Wörtern darüber. Absatz 1 (methodische Verzahnung) unverändert. Die vier Meta-Sätze ersatzlos gestrichen: `02_zielsetzung_und_verengung.tex` („Kapitel 2 beschreibt …"), `02_zielgruppe.tex` („Dieser Abschnitt füllt …"), `03_konzept.tex` (Satz vor `tab:funktionsuebersicht`) und `01_wettbewerbsanalyse.tex` (Satz vor `tab:wettbewerbsvergleich`). `durchfuehrung.tex:3` wie angewiesen unverändert.
- **Befund**: Der Bericht beschreibt wiederholt seinen eigenen Ablauf. Konkret:
  - `chapters/01_einleitung/03_vorgehen_und_aufbau.tex:5` beschreibt den Aufbau von Kapitel 2 in **110 Wörtern**, inklusive Nennung praktisch jeder Subsection — und `chapters/02_durchfuehrung/durchfuehrung.tex:3` beschreibt denselben Aufbau direkt danach noch einmal.
  - `chapters/01_einleitung/02_zielsetzung_und_verengung.tex:3`: „Kapitel 2 beschreibt dieses Konzept im Detail; die vorliegende Einleitung benennt zunächst, wofür die Plattform steht und für wen sie gedacht ist."
  - `chapters/02_durchfuehrung/02_zielgruppe.tex:3`: „Dieser Abschnitt füllt die Zielgruppe mit konkreten Merkmalen, damit die folgenden Konzeptentscheidungen nicht abstrakt bleiben."
  - `chapters/02_durchfuehrung/03_konzept.tex:36`: „Alle Kernfunktionen mit ihrer jeweiligen Herleitung fasst~\autoref{tab:funktionsuebersicht} zusammen." — die Tabelle trägt bereits eine Caption mit derselben Aussage. Analog `01_wettbewerbsanalyse.tex:13` Satz 1.
- **Warum**: `hard-rules-formal.md:61` — „Ein Vorverweis unmittelbar vor der Überschrift, die dasselbe ankündigt, ist redundant und entfällt." Zugleich der sauberste Hebel für die Einleitung, die mit 14,3 % ihr 10–15-%-Band fast ausschöpft.
- **Anweisung**: In `03_vorgehen_und_aufbau.tex:5` die Subsection-für-Subsection-Aufzählung auf zwei Sätze reduzieren (Trichter-Logik von Marktanalyse über Konzept zu Umsetzung und Reflexion; danach Kapitel 3). Die vier oben zitierten Meta-Sätze ersatzlos streichen. `durchfuehrung.tex:3` bleibt unverändert — die Kapitel-Einleitung ist der richtige Ort dafür, die Vorwegnahme in Kapitel 1 nicht.
- **Achtung**: `03_vorgehen_und_aufbau.tex` wurde am 2026-07-23 als Prüfbericht-Handlungsempfehlung 3 **absichtlich verlängert**, weil die Datei unter die ½-Seiten-Heuristik gefallen war. Nach der Kürzung `check_formalia.py` prüfen: Bleibt die Datei über der HALBSEITE-Schwelle (~150 Wörter)? Falls nicht, weniger kürzen — Absatz 1 (methodische Verzahnung) ist inhaltlich tragend und bleibt ohnehin vollständig erhalten.
- **Erwarteter Ertrag**: ~120 Wörter

---

### Befund 4.5 — Der Vorbehalt „kein realer Nutzertest" steht an sieben Stellen  🟡 leicht · **[FREIGABE]** (berührt den Geltungsanspruch der Ergebnisse)

- **Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: umgesetzt, aber nur 3 statt 4 Stellen gekürzt.** Gekürzt: `02_zielsetzung_und_verengung.tex` (Zielgruppenannahme-Satz auf Halbsatz), `02_zielgruppe.tex` (Persona-Satz kompaktiert) und `03_fazit/01_kernergebnisse_und_ausblick.tex` (Ausblicksatz von drei auf zwei Sätze). Bewusst zusätzlich zu den beiden angewiesenen Ausnahmen (`02_limitationen.tex:3`, `04_community_und_feedback.tex:9`) unangetastet gelassen: `01_wettbewerbsanalyse.tex` („die Schwäche im fehlenden Nutzertest") ist bereits ein Halbsatz und trägt seit Runde-1-Befund 4 eine Matrixbias-Mitigation, die beim weiteren Kürzen verloren ginge; `06_evaluation_reflexion.tex` enthält den einzigen verbliebenen Nutzerdaten-Bezug innerhalb des laut Befund 4.3 explizit geschützten Prozess-Reflexions-Absatzes. Im Zweifel weniger gekürzt, wie die Grenze der Anweisung vorschreibt.
- **Befund**: Sieben Fundstellen: `01_einleitung/02_zielsetzung_und_verengung.tex:7` · `02_durchfuehrung/02_zielgruppe.tex:9` · `02_durchfuehrung/01_wettbewerbsanalyse.tex:32` („die Schwäche im fehlenden Nutzertest") · `02_durchfuehrung/04_community_und_feedback.tex:9` · `02_durchfuehrung/06_evaluation_reflexion.tex:9` · `03_fazit/01_kernergebnisse_und_ausblick.tex:9` · `03_fazit/02_limitationen.tex:3`.
- **Warum**: Der Vorbehalt selbst ist richtig und laut `aufgabe.md:45` gedeckt (Feedback-Schleifen nur als geplantes Vorgehen). Seine siebenfache Wiederholung ist reine Absicherungs-Redundanz.
- **Anweisung**: `02_limitationen.tex:3` bleibt **vollständig unverändert** — dort gehört der Vorbehalt hin und wird ausgeführt. Ebenso bleibt `04_community_und_feedback.tex:9` erhalten, weil er dort eine Aufgabenstellungs-Anforderung explizit erfüllt. Die übrigen vier Vorwegnahmen auf Halbsätze reduzieren oder streichen, wo der Kontext sie ohnehin trägt.
- **Grenze**: Es darf an keiner Stelle der Eindruck entstehen, ein Nutzertest habe stattgefunden. Im Zweifel weniger kürzen.
- **Erwarteter Ertrag**: ~100 Wörter

---

### Befund 4.6 — Doppelte und entbehrliche Erklär-Appositionen  🟡 leicht

- **Status: ERLEDIGT (2026-07-24).** Drivers/Levers-Zweitdefinition im Fazit gestrichen. Dabei zugleich eine seit Runde-2-Befund GS-2 bestehende Propagationslücke behoben: Der Fazit-Satz zu Barkers Reminders verwies noch auf „die steigenden Reste-Level" statt auf die in `03_konzept.tex` bereits umbenannte geplante Erinnerungsbenachrichtigung — an die dort korrigierte Formulierung angeglichen, damit beide Kapitel konsistent bleiben. „also die Bildschirmaufteilung und Bedienführung von Resteria" gestrichen. Nudge-Definition in `03_konzept.tex:28` auf einen Halbsatz gekürzt.
- **Befund**: Die Unterscheidung Drivers/Levers wird **zweimal** definiert: `02_durchfuehrung/03_konzept.tex:7` („also psychologischen und sozialen Einflussfaktoren … den konkret nutzbaren Hebeln …") und erneut in `03_fazit/01_kernergebnisse_und_ausblick.tex:5` („also erklärenden Einflussfaktoren und gezielt nutzbaren Hebeln"). Dazu entbehrliche Einschübe: „also die Bildschirmaufteilung und Bedienführung von Resteria" (`03_konzept.tex:55`) und die 15-Wörter-Definition von Nudge-Forschung in `03_konzept.tex:28`.
- **Warum**: Die Erstdefinition eines Fachbegriffs ist korrekt und bleibt. Die Zweitdefinition im Fazit ist überflüssig, weil der Begriff bereits eingeführt wurde.
- **Anweisung**: Im Fazit die Drivers/Levers-Apposition ersatzlos streichen (der Begriff steht dort nur noch als Rückverweis). „also die Bildschirmaufteilung und Bedienführung von Resteria" streichen — UI und UX sind unmittelbar davor ausgeschrieben. Die Nudge-Definition in `03_konzept.tex:28` auf einen knappen Halbsatz kürzen. Alle übrigen Ersteinführungen bleiben.
- **Erwarteter Ertrag**: ~70 Wörter

---

### Befund 4.7 — Die „kurze Abgrenzung" zu Foodsharing.de ist der zweitlängste Absatz des Kapitels  🟡 leicht · **[FREIGABE]** (berührt eigenes Rechercheergebnis)

- **Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: wie vorgeschlagen umgesetzt.** Von 117 auf ca. 70 Wörter gekürzt (etwas über dem Zielwert ~55, um Nutzungsszenario und Matrixwertungs-Begründung vollständig und in unter 30 Wörtern langen Sätzen zu erhalten). „Fairteiler" auf eine knappe Klammer-Apposition gekürzt.
- **Befund**: `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex:11` — **117 Wörter**, eingeleitet mit „verdient an dieser Stelle eine kurze Abgrenzung". Die Länge widerspricht der eigenen Ankündigung. Sobald Einwand 3 aus Befund 4.1 entfällt, trägt dieser Absatz die Abgrenzung allein und kann sie kompakter leisten.
- **Warum**: Die Abgrenzung ist inhaltlich nötig — sie rechtfertigt die Matrixwertung „Community stark" bei gleichzeitig fehlendem Rezeptbezug und beantwortet einen naheliegenden Prüfereinwand. Nur ihr Umfang steht in keinem Verhältnis.
- **Anweisung**: Auf ~55 Wörter kürzen. Erhalten bleiben müssen: das Nutzungsszenario (Weitergabe vor dem Verderb statt Verarbeitung in der eigenen Küche) und die ausdrückliche Begründung der Matrixwertung „stark" bei Community-Funktionen — beides ist gegen Runde-2-Befund GS-4 gezielt eingefügt worden und darf nicht wieder verschwinden. Die Erklärung des Begriffs „Fairteiler" kann auf eine knappe Apposition schrumpfen.
- **Erwarteter Ertrag**: ~60 Wörter

---

### Befund 4.8 — Die Soma-Zahlen stehen zweimal ausgeschrieben  🟢 Hinweis

- **Status: ERLEDIGT (2026-07-24), wie angewiesen umgesetzt.** Klammer in `04_community_und_feedback.tex` auf den reinen `\autoref`-Verweis reduziert. Einordnung in `03_konzept.tex:30` wörtlich unverändert.
- **Befund**: „51 Prozent bei Vielspieler:innen gegenüber 39 Prozent bei Wenigspieler:innen" steht in `chapters/02_durchfuehrung/03_konzept.tex:30` und wird in `chapters/02_durchfuehrung/04_community_und_feedback.tex:7` in Klammern wiederholt — dort bereits mit `\autoref{sec:konzept}` daneben.
- **Warum**: Der `\autoref` leistet die Verknüpfung; die Zahlenwiederholung ist überflüssig.
- **Anweisung**: In `04_community_und_feedback.tex:7` die Klammer auf den reinen Verweis reduzieren. **Die Einordnung in `03_konzept.tex:30` bleibt wörtlich unverändert** — sie trennt ausdrücklich die belegte Gamification-Wirkung von der eigenen Resteria-Mechanik und ist laut Runde 3 eine tragende Stärke, die beim Überarbeiten nicht geglättet werden darf.
- **Erwarteter Ertrag**: ~15 Wörter

---

### Nicht kürzen (geprüft und bewusst ausgenommen)

- **Freemium- und Kooperations-Absatz** (`03_konzept.tex:5`, 91 Wörter): sieht wie ein Exkurs aus, ist aber die einzige Stelle, die die **wirtschaftliche** Hälfte des Transfer-Kriteriums bedient (`aufgabe.md:39`, 15 % der Bewertung). Zudem war er die Antwort auf Runde-1-Befund 3.
- **Event-Kalender-Begründung** (`03_konzept.tex:57`): `aufgabe.md:84` verlangt bei Auslassung ausdrücklich eine explizite Begründung.
- **`02_zielgruppe.tex`** (280 Wörter) und der Fließtext von **`05_phasenplanung.tex`** (184 Wörter): bereits die dichtesten Dateien der Arbeit; `05_phasenplanung.tex` liegt nahe an der ½-Seiten-Schwelle.
- **Die drei Limitationen** (`02_limitationen.tex`, Absätze 1–3): dreischichtige Grenzziehung, direkt bewertungsrelevant für „Prozess".
- **Alle vier Punkte der Liste „Tragende Stärken" aus Runde 3** — insbesondere die vorsichtige Soma-Einordnung und die selbst aufgelöste SDG-Spannung.

### Umfangshinweis

Diese Runde ist die erste, die **ausschließlich subtrahiert**. Erwarteter Gesamtertrag aller acht Punkte: **~715 Wörter (≈ 16 %)**, verteilt auf Einleitung (~150), Durchführung (~430) und Fazit (~135) — die Kapitelanteile bleiben damit annähernd erhalten. Kein Punkt entfernt eine Information, einen Beleg oder ein Artefakt; entfernt werden ausschließlich Wiederholungen bereits getroffener Aussagen.

### Nächster Schritt

**Abgearbeitet (2026-07-24):** Alle neun Punkte (4.0–4.8) umgesetzt. 4.0 ohne Messwert (lualatex/latexmk fehlen weiterhin), Nutzer-Entscheidung: alle Punkte trotzdem umsetzen. `[FREIGABE]`-Punkte 4.1, 4.2, 4.5 und 4.7 per `AskUserQuestion` einzeln geklärt und wie vorgeschlagen umgesetzt, bei 4.5 mit einer bewusst konservativeren Abweichung (3 statt 4 Stellen gekürzt, siehe Befund-Status oben). 4.4 ebenfalls leicht abweichend (vier statt zwei Sätze in `03_vorgehen_und_aufbau.tex`, um die HALBSEITE-Schwelle nicht zu unterschreiten). `check_formalia.py`: 0 FEHLER (10 HINWEIS, überwiegend bekannte Tabellen-Satzlängen-Artefakte). `check_bib_keys.py`: alle 6 Keys valide. Tatsächlicher Wortzahl-Ertrag ca. 394 Wörter (~8,7 %) statt der geschätzten ~715 (~16 %) — geringer, weil mehrere Punkte bewusst konservativer umgesetzt wurden, um HALBSEITE-Schwelle, Matrixbias-Mitigation (Runde 1) und den geschützten Prozess-Reflexions-Absatz (Befund 4.3) nicht zu gefährden. Damit ist „Offen" wieder vollständig leer.

Nächster Schritt laut Fahrplan: **Delta-Re-Audit** (`pruef-modus`) — die Kürzungen berühren Kapitel, für die der Voll-Audit vom 2026-07-23 (Score 100/100) den alten, ungekürzten Textstand bewertet hat. Weiterhin offen (Nutzer-Schritt): lokaler Build zur Seitenumfangs-Verifikation.

---

## Runde 5 — Gegenlesung (2026-07-24)

Kalte Prüfer-Gegenlesung gegen `aufgabe.md`. Gelesen wurden ausschließlich `aufgabe.md`, alle 14 `chapters/**/*.tex`, `pages/appendix.tex`, `pages/acronyms.tex`, `pages/chapters.tex`, die vier Mockup-Bilder in `images/durchfuehrung/` sowie `references.bib` zur reinen Eintragszählung. Kapitelplan, Prüfbericht, Statustabelle und die Runden 1–4 dieser Datei wurden nicht herangezogen. Alle Punkte sind **offen**.

### Soll-Ist-Tabelle (Schritt 3)

| Geforderter Inhalt (aus `aufgabe.md`) | Erfüllung |
|---|---|
| Teilaufgabe 1: Analyse bestehender Plattformen | erfüllt, aber ohne Instagram und ohne durchgängigen Erhebungsnachweis — `sec:wettbewerbsanalyse`, 6 Plattformen, `tab:wettbewerbsvergleich` (Befunde 5.1, 5.3) |
| — Achse „Rezept-Austausch" | erfüllt — eigene Matrixspalte |
| — Achse „Rezept-Entdeckung" | erfüllt — eigene Matrixspalte |
| — Achse „Kommunikation" | erfüllt, aber umbenannt — läuft als „Community-Funktionen"; der Begriff der Aufgabenstellung fällt nie (Befund 5.4) |
| Teilaufgabe 2: Konzeptentwicklung | erfüllt — `sec:konzept`, `tab:funktionsuebersicht`, `fig:konzeptfluss` |
| Teilaufgabe 3: Iteratives Design und Feedback | erfüllt, aber ohne eigene Überschrift und nur als Feedback-Teil — 1 Absatz in `sec:community_und_feedback` (Befund 5.2) |
| Berichtsinhalt: Zielgruppe | erfüllt — `sec:zielgruppe` + `tab:persona` (Anhang A) |
| Berichtsinhalt: Funktionalitäten | erfüllt — `sec:konzept` + `tab:funktionsuebersicht` |
| Berichtsinhalt: User Interface und User Experience | erfüllt, aber eine Tabellenfunktion ohne UI-Entsprechung — vier Mockups in Anhang B (Befund 5.7) |
| Berichtsinhalt: Community-Building | erfüllt — Rettungs-Feed + Challenges; Verzicht auf Forum/Gruppen begründet |
| Objekt: Wettbewerbsvergleich (Tabelle) | erfüllt — `tab:wettbewerbsvergleich`, 6 Plattformen × 5 Kriterien |
| Objekt: Persona (Text/Abb.) | erfüllt — `tab:persona` |
| Objekt: UI/UX-Skizze/Mockup (Abb.) | erfüllt — 4 Abbildungen, KI-Herkunft je Bild ausgewiesen; eine Prompt-Zeile stimmt nicht mit dem Bild überein (Befund 5.8) |
| Objekt: Plattformname | erfüllt — „Resteria", hergeleitet in `sec:konzept` |
| Objekt: Funktionsübersicht (Tab./Abb.) | erfüllt — `tab:funktionsuebersicht` |
| Objekt: Phasenplanung (Tabelle) | erfüllt, aber Ressourcenträger der längsten Phase offen — `tab:phasenplanung` (Befund 5.10) |
| Schlüsselbegriff: Rezept-Uploads (Foto/Video) | erfüllt |
| Schlüsselbegriff: Kommentar-/Bewertungssysteme | erfüllt |
| Schlüsselbegriff: Personalisierte Empfehlungen | erfüllt |
| Schlüsselbegriff: Gruppen/Foren | erfüllt — Verzicht mit Soma et al. begründet; erzeugt aber einen Doppelmaßstab zur Wettbewerbsanalyse (Befund 5.5) |
| Schlüsselbegriff: Event-Kalender (bei Auslassung begründen) | erfüllt — `03_konzept.tex:55`, eigener Absatz |
| Schlüsselbegriff: Lebensmittel-Journaling/Menüplanung | erfüllt im Text, ohne UI-Entsprechung (Befund 5.7) |
| Verengung Zielgruppe (begründet) | erfüllt — Einleitung + `sec:zielgruppe`, Spannung zu SDG 12.3 in `sec:evaluation_reflexion` selbst aufgelöst |
| Anonymisierung personenbezogener Daten | erfüllt — keine realen Personen; Persona ausdrücklich als fiktiv gekennzeichnet |
| Struktur 10–15 / 70–80 / 10–15 % | erfüllt — 13,5 / 71,5 / 15,0 % (Wortbasis) |
| Quellen 5–10 | erfüllt — 6 Einträge in `references.bib`, alle genutzt |
| Materialien Hansch & Rentschler (2012), Kapoor et al. (2018) | nicht erfüllt — kommen nicht vor; laut `aufgabe.md:26` nicht Pflicht |

### Bewertungskriterien je Dimension (Schritt 5)

| Kriterium | Dimension | Stand |
|---|---|---|
| Qualität 25 % | Ergebnis erfüllt die Aufgabenstellung | abgedeckt — bis auf 5.1 und 5.2 |
| Prozess 25 % | Vorgehen dokumentieren | abgedeckt — `sec:vorgehen_und_aufbau`, `tab:phasenplanung` |
| Prozess 25 % | reflektieren | **schwach** — ein Absatz, „verlief weitgehend planmäßig" (Befund 5.6) |
| Prozess 25 % | Grenzen aufzeigen | abgedeckt, stark — `sec:limitationen`, dreischichtig |
| Transfer 15 % | gesellschaftliche Bedeutung | abgedeckt — SDG 12.3, Vittuari et al. |
| Transfer 15 % | wirtschaftliche Bedeutung | abgedeckt, knapp — Freemium/Kooperationen, `03_konzept.tex:5`, unbelegt („erscheint tragfähig") |
| Transfer 15 % | Ansätze/Modelle begründen | abgedeckt, stark — Drivers/Levers, Nudges, Osmose |
| Kreativität 15 % | Vergleich zu bestehendem Produkt | abgedeckt — Matrix + narrative Einordnung; Resteria selbst steht nicht in der Matrix |
| Kreativität 15 % | Innovationskraft | abgedeckt — Kombination Matching + Peer-Community |
| Dokumentation 10 % | Entstehungsgeschichte lückenlos | **schwach** — verworfene Alternativen sind dokumentiert (Event-Kalender, Forum), der Entstehungsweg selbst nicht (Befund 5.6) |
| Ressourcen 10 % | Zeit effizient | abgedeckt — 5 Phasen, Zeitrahmen, 2 Wochen Puffer |
| Ressourcen 10 % | Material effizient | **schwach** — Träger der längsten Phase offen, keine Aufwands-/Kostengröße (Befund 5.10) |

---

#### 5.1 Instagram fehlt in der Wettbewerbsanalyse vollständig  [FREIGABE]

**Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: Option B.** In `01_wettbewerbsanalyse.tex` (TikTok-Absatz) einen Halbsatz ergänzt, der TikTok stellvertretend für allgemeine Social-Media-Plattformen einschließlich Instagram setzt (vergleichbare, visuell ausgelegte Content-Logik ohne eigene Reste-Funktion). Keine neue Matrixzeile, kein Recherche-Aufwand.

- **Befund**: `aufgabe.md:10` beschreibt das Rahmenthema wörtlich als Abgrenzung „im Unterschied zu allgemeinen Plattformen wie Instagram/TikTok". Ein Grep über alle Kapitel und `pages/` ergibt für „Instagram" **keinen einzigen Treffer**. Untersucht werden Chefkoch.de, TikTok, Restegourmet, BMEL-App, leftovercooking und Foodsharing.de.
- **Warum**: Qualität (25 %) und Kreativität (15 %, „Vergleich zu bestehendem Produkt"). Die Aufgabenstellung nennt genau zwei allgemeine Plattformen namentlich; eine davon wird bearbeitet, die andere kommt nicht vor — und der Text sagt nirgends, dass das eine Entscheidung war. Für Hobbyköch:innen ist Instagram zudem die naheliegendste Bild-Plattform. Ein Prüfer, der seine eigene Formulierung im Text sucht, findet sie halb bedient.
- **Anweisung**: Drei Wege, absteigend nach Aufwand.
  - *Option A*: Instagram als siebte Zeile in `tab:wettbewerbsvergleich` (`01_wettbewerbsanalyse.tex:19–27`) aufnehmen und im Fließtext mit zwei bis drei Sätzen einordnen (eigene Sichtung, analog TikTok). Kostet Recherche und ~60 Wörter — Umfangshinweis unten beachten.
  - *Option B* (billig): In `01_wettbewerbsanalyse.tex:5` einen Halbsatz ergänzen, der TikTok ausdrücklich stellvertretend für die allgemeinen Social-Media-Plattformen einschließlich Instagram setzt, mit kurzer Begründung (vergleichbare Content-Logik, keine Reste-Funktion).
  - *Option C*: In `02_limitationen.tex:7` bei der dritten Grenze Instagram namentlich als bewusst nicht einzeln untersuchte Plattform aufführen.

#### 5.2 Teilaufgabe 3 hat keine eigene Überschrift und besteht aus einem Absatz

**Status: ERLEDIGT (2026-07-24).** Absatz aus `04_community_und_feedback.tex` herausgelöst in neue Datei `chapters/02_durchfuehrung/07_iteratives_design.tex` (`\subsection{Iteratives Design und Feedback}\label{sec:iteratives_design}`), eingebunden in `durchfuehrung.tex` zwischen 04 und 05. Um den Design-Anteil ergänzt (Mockup/Klick-Prototyp durchlaufen in Woche 5–7 eine Rückkopplungsschleife vor der MVP-Entwicklung, verzahnt mit der Abhängigkeit aus `05_phasenplanung.tex`). Verweis in `06_evaluation_reflexion.tex:3` auf `sec:iteratives_design` umgestellt. `kapitelplan.md` im Durchführungs-Block nachgezogen.

- **Befund**: `aufgabe.md:15` führt „Iteratives Design und Feedback" als dritte, gleichrangige Leitfrage. Im Text steht sie als letzter Absatz von `chapters/02_durchfuehrung/04_community_und_feedback.tex:9` unter der Überschrift „Rettungs-Feed und Challenges" — 96 Wörter. Zum Vergleich: Teilaufgabe 1 hat 794 Wörter, eigene Subsection und Tabelle; Teilaufgabe 2 hat 921 Wörter, Tabelle und Abbildung. Im Inhaltsverzeichnis erscheint die dritte Teilaufgabe überhaupt nicht. Inhaltlich beschreibt der Absatz fast ausschließlich *Feedback* (Beta-Gruppe, Fragebögen, Sprints); der *Design*-Anteil des „iterativen Designs" — Iterationen an Mockup und Klick-Prototyp — kommt nicht vor, obwohl `tab:phasenplanung` eine eigene Phase „Design & Prototyp" (Woche 5–7) kennt.
- **Warum**: Qualität (25 %). Ein Prüfer hakt die drei Leitfragen einzeln ab und sucht sie zuerst im Inhaltsverzeichnis. Eine Teilaufgabe, die dort nicht auftaucht, muss er sich selbst zusammensuchen — und wird sie im Zweifel als schwächer bearbeitet werten, als sie ist.
- **Anweisung**: Den Absatz `04_community_und_feedback.tex:9` als eigene Subsection herauslösen: neue Datei `chapters/02_durchfuehrung/07_iteratives_design.tex` mit `\subsection{Iteratives Design und Feedback}\label{sec:iteratives_design}`, eingebunden in `durchfuehrung.tex`. Inhaltlich um zwei bis drei Sätze zum Design-Anteil ergänzen: dass Mockup und Klick-Prototyp aus Woche 5–7 vor der MVP-Entwicklung eine erste Rückkopplungsschleife durchlaufen und Bedienführungs-Entscheidungen dort korrigiert werden, bevor sie in Code gegossen sind (verzahnt sich mit dem Abhängigkeitsabsatz `05_phasenplanung.tex:21`). Verweis in `06_evaluation_reflexion.tex:3` von `sec:community_und_feedback` auf das neue Label umstellen.

#### 5.3 Die Wettbewerbsanalyse trägt null Beleg, und für die Hälfte der Plattformen fehlt sogar der Sichtungsvermerk

**Status: ERLEDIGT (2026-07-24).** Einheitlichen Methodensatz vor `tab:wettbewerbsvergleich` ergänzt (eigene Sichtung aller sechs Plattformen im Juli 2026, Kriterien aus den drei Aufgabenstellungs-Achsen plus zwei nischenspezifischen abgeleitet). Die beiden Einzelvermerke „Nach eigener Sichtung (Stand: Juli 2026)" bei Restegourmet/BMEL-App und leftovercooking gestrichen — Asymmetrie beseitigt, Wörter gespart.

- **Befund**: `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex` ist mit 794 Wörtern die größte Subsection der Arbeit und enthält **kein einziges `\parencite`**. Der Erhebungsnachweis „Nach eigener Sichtung (Stand: Juli 2026)" steht nur bei Restegourmet/BMEL-App (Z. 7) und leftovercooking (Z. 9). Für Chefkoch.de (Z. 3), TikTok (Z. 5) und Foodsharing.de (Z. 11) gibt es weder Quelle noch Sichtungsvermerk noch Datum — obwohl `tab:wettbewerbsvergleich` allen dreien je fünf Einstufungen zuweist.
- **Warum**: Prozess (25 %, „Vorgehen dokumentieren") und Dokumentation (10 %). Eigene Sichtung ist eine völlig legitime Erhebungsgrundlage für Desk-Research — aber nur, wenn sie durchgängig als solche ausgewiesen ist. Halb ausgewiesen ist schlechter als gar nicht: Der Prüfer sieht den Vermerk bei drei Plattformen, sucht ihn bei den anderen drei und findet nichts.
- **Anweisung**: Nach `01_wettbewerbsanalyse.tex:13` (also unmittelbar vor der Tabelle) einen Methodensatz einfügen, der die Erhebung für alle sechs Plattformen einheitlich deklariert — Grundlage der Einstufungen ist eine eigene Sichtung der jeweiligen Web-Auftritte und Apps im Juli 2026, die Kriterien sind aus den drei in der Aufgabenstellung genannten Achsen abgeleitet und um zwei nischenspezifische ergänzt. Anschließend die beiden Einzelvermerke in Z. 7 und Z. 9 streichen: Das beseitigt die Asymmetrie und spart zugleich Wörter.

#### 5.4 Das Kriterium „Kommunikation" aus der Aufgabenstellung fällt im Text nie

**Status: ERLEDIGT (2026-07-24).** Spaltenüberschrift und alle Textverweise auf das Kriterium in `01_wettbewerbsanalyse.tex` von „Community-Funktionen" auf „Kommunikation \& Community" umgestellt (Tabellenkopf, Kriteriendefinition, drei Fließtextstellen). Einstufungen aller sechs Plattformen unverändert.

- **Befund**: `aufgabe.md:13` verlangt Stärken und Schwächen bezüglich „Rezept-Austausch, -Entdeckung und Kommunikation". `tab:wettbewerbsvergleich` führt die Spalten Rezept-Austausch, Rezept-Entdeckung, **Community-Funktionen**, Nachhaltigkeits-/Restefokus, Reste-Matching-Werkzeug. Das Wort „Kommunikation" kommt in der gesamten Arbeit genau einmal vor — als Herleitungs-Label in einer Tabellenzelle (`03_konzept.tex:45`).
- **Warum**: Qualität (25 %). Zwei der drei wörtlich verlangten Achsen sind namensgleich abgebildet, die dritte ist umbenannt. Inhaltlich deckt „Community-Funktionen" die Kommunikation ab — die Definition in Z. 13 nennt Kommentare und Gruppen ausdrücklich. Aber der Prüfer muss diese Übersetzung selbst leisten, und beim Abhaken der eigenen Leitfrage ist das genau der Moment, in dem ein Häkchen ausbleibt. Von allen Befunden dieser Runde der billigste Fix bei größter Wirkung.
- **Anweisung**: Spaltenüberschrift in `01_wettbewerbsanalyse.tex:19` von „Community-Funktionen" auf „Kommunikation \& Community" ändern und die Kriteriendefinition in Z. 13 im ersten Wort mitziehen. Die Einstufungen aller sechs Plattformen bleiben unverändert. Falls die Spaltenbreite darunter leidet, alternativ die Überschrift belassen und in Z. 13 einen Halbsatz ergänzen, der die Gleichsetzung ausspricht.

#### 5.5 Doppelmaßstab: Der Text hält Wettbewerbern fehlende Gruppen und fehlendes Folgen vor — Resteria bietet beides ebenfalls nicht  [FREIGABE]

**Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: (a) + (b) ergänzen.** (a) „Gruppen" aus der Kriteriendefinition und aus den Defizit-Nennungen bei Restegourmet/BMEL-App und leftovercooking gestrichen. (b) In `04_community_und_feedback.tex` einen Satz ergänzt, der Following über den im Rettungs-Feed bereits sichtbaren Nutzernamen einführt — bewusst an die vorhandene Mockup-Struktur (Avatar + Nutzername je Beitrag) angebunden, ohne einen im Bild nicht vorhandenen Folgen-Button zu behaupten. Kein neues Mockup nötig.

- **Befund**: `01_wettbewerbsanalyse.tex:13` definiert das Kriterium Community-Funktionen als „tatsächlicher Austausch zwischen Nutzer:innen, etwa über Kommentare, **Gruppen** oder Gamification". Z. 7 hält Restegourmet und der BMEL-App vor, „Following, **Gruppen**, Kommentar-Communities und Gamification" fehlten. Z. 9 hält leftovercooking vor, ein Austausch „etwa über Kommentare zu fremden Beiträgen, **gegenseitiges Folgen** oder **Gruppen**" sei nicht belegt. `04_community_und_feedback.tex:7` legt für Resteria dagegen fest: „Ein offenes Diskussionsforum ist dagegen ebenso wenig vorgesehen wie feste thematische oder regionale Nutzergruppen." Eine Folgen- oder Abonnier-Funktion beschreibt die Arbeit für Resteria an keiner Stelle (Grep über alle Kapitel: Treffer ausschließlich innerhalb der Wettbewerbsanalyse, dort als Fremdplattform-Merkmal).
- **Warum**: Prüferfrage nach der Ergebnisorientiertheit der eigenen Bewertung, dazu Kreativität (15 %, Vergleich zum bestehenden Produkt) und Qualität. Der Maßstab, an dem die Konkurrenz gemessen wird, wird von der eigenen Plattform an zwei von drei genannten Merkmalen selbst nicht erfüllt. Der Verzicht auf Gruppen ist gut und literaturgestützt begründet — aber diese Begründung steht drei Subsections später, während die Wettbewerbsanalyse die fehlenden Gruppen vorher als Minuspunkt gegen andere verbucht. Das ist ein Einwand, den die Arbeit selbst aufwirft und nirgends beantwortet.
- **Anweisung**: Zwei Stellschrauben, beide ohne Substanzverlust und ohne Änderung an einer einzigen Matrixzelle.
  - *(a)* In `01_wettbewerbsanalyse.tex:13` „Gruppen" aus der Kriteriendefinition streichen und durch das ersetzen, was Resteria tatsächlich bietet: Kommentare, Bewertungen und einen öffentlichen Feed. Dieselbe Bereinigung in Z. 7 und Z. 9, wo „Gruppen" als Defizit anderer aufgeführt wird.
  - *(b)* Für „Following"/„gegenseitiges Folgen" entweder **ergänzen** — ein Satz in `03_konzept.tex` (Abschnitt Rettungs-Feed/UI, Z. 53) genügt, dass Nutzer:innen anderen folgen können; das passt zum Osmose-Argument in `04_community_und_feedback.tex:5` und ist im Feed-Mockup durch die Beitragsstruktur mit Nutzernamen bereits angelegt — **oder streichen**, sodass kein Merkmal als Defizit angeführt wird, das Resteria selbst nicht hat. Ergänzen ist die stärkere Variante, weil sie den Peer-zu-Peer-Anspruch aus Z. 32 tatsächlich einlöst.

#### 5.6 Die Prozess-Reflexion nennt keine einzige Schwierigkeit

**Status: ERLEDIGT (2026-07-24).** Leerformel „Der Prozess selbst verlief weitgehend planmäßig …" in `06_evaluation_reflexion.tex` durch zwei konkrete Prozessereignisse ersetzt: Verwerfen des Forum/Gruppen-Zuschnitts nach dem Soma-Befund zugunsten der Challenges; Korrektur des Arbeitstitels nach der Namenskollision.

- **Befund**: `aufgabe.md:39` verlangt für „Prozess" — mit 25 % das höchstgewichtete Kriterium gemeinsam mit Qualität — ausdrücklich „Vorgehen dokumentieren + reflektieren + Grenzen aufzeigen". Dokumentation und Grenzen sind stark bedient. Die Reflexion selbst besteht aus einem Absatz (`06_evaluation_reflexion.tex:7`, 88 Wörter), dessen Kern lautet: „Der Prozess selbst verlief weitgehend planmäßig: Auf die Recherche folgte zügig die Konzeptentwicklung, ohne dass grundlegende Kursänderungen nötig wurden." Die einzige Selbstkritik ist, es wäre „etwas mehr Zeit für die Suche nach zusätzlichen Vergleichsplattformen sinnvoll gewesen".
- **Warum**: Prozess 25 % und Dokumentation 10 % („Entstehungsgeschichte lückenlos"). „Alles lief nach Plan" ist die schwächste mögliche Form der Reflexion und wird als Nicht-Reflexion gelesen. Bemerkenswert ist, dass der Bericht die Substanz für eine echte Reflexion bereits enthält, sie an dieser Stelle aber nicht nutzt: Der Verzicht auf Forum und Gruppen (`04_community_und_feedback.tex:7`) ist eine echte, literaturgetriebene Abkehr von der naheliegenden Standardlösung, und die Namensprüfung wird in Z. 9 nur als abstrakte Lehre erwähnt, nicht als Vorfall im Prozess.
- **Anweisung**: `06_evaluation_reflexion.tex:7` umschreiben, ohne zu verlängern. Den Satz „Der Prozess selbst verlief weitgehend planmäßig … Kursänderungen nötig wurden" durch zwei konkrete Prozessereignisse ersetzen: (i) der ursprünglich naheliegende Community-Zuschnitt mit Forum und Nutzergruppen wurde nach Auswertung des Soma-Befunds zugunsten zeitlich begrenzter Challenges verworfen; (ii) die Prüfung des Plattformnamens erzwang eine Korrektur, bevor das Konzept darauf aufbaute. Beides ist wortneutral einsetzbar und ersetzt eine Leerformel durch nachvollziehbare Prozessgeschichte.

#### 5.7 Menüplanung und Reste-Journal stehen als Kernfunktion in der Tabelle, haben aber in keinem Mockup einen Zugang

**Status: ERLEDIGT (2026-07-24), Option A (Nutzer-Entscheidung: vorsichtig planen, kein neues Mockup).** In `03_konzept.tex:53` einen Halbsatz ergänzt, der Menüplanung/Reste-Journal als Zugang der Startseite verortet — erklärt, warum die Navigation drei statt vier Hauptbereiche zeigt, ohne neues Bild.

- **Befund**: `tab:funktionsuebersicht` (`03_konzept.tex:47`) führt „Menüplanung \& Reste-Journal" als eine von sechs Kernfunktionen; `03_konzept.tex:34` widmet ihr einen eigenen Absatz und bindet sie an den Rettungspunkte-Mechanismus. Die vier Mockups in Anhang B zeigen jedoch durchgängig eine Tab-Leiste mit genau drei Einträgen: Start, Rettungs-Feed, Profil. Ein Einstiegspunkt für Menüplanung oder Reste-Journal fehlt. `03_konzept.tex:53` benennt selbst nur „drei Hauptbereiche" für UI und UX und zählt die Menüplanung dort nicht mit.
- **Warum**: Prüferfrage „Existiert, was behauptet wird?", hier in abgeschwächter Form: Der Text führt eine Kernfunktion, die das eigene UI-Konzept nicht kennt. Sowohl „Funktionalitäten" als auch „User Interface und User Experience" sind wörtlich geforderte Berichtsinhalte (`aufgabe.md:73–74`). Ein Prüfer, der Funktionsübersicht und Mockup nebeneinanderlegt, sieht die Lücke sofort — es ist derselbe Abgleich, der bei Upload-Button und Einsparangabe bereits geführt wurde.
- **Anweisung**: Zwei Wege.
  - *Option A* (ohne neues Bild, bei Umfangsdruck bevorzugt): In `03_konzept.tex:53` einen Halbsatz ergänzen, der Menüplanung und Reste-Journal ausdrücklich als Unterbereich der Startseite verortet, und damit erklären, warum die Navigation drei statt vier Hauptbereiche führt.
  - *Option B*: Ein fünftes Mockup für den Menüplan-Screen erzeugen lassen (Nutzer-Schritt, Prompt analog `sources/claude-design-nachbesserung.md`) und in Anhang B aufnehmen. Kostet Anhangsseiten, aber keine Textseiten — und schließt die Lücke sichtbar statt erklärend.

#### 5.8 Die Prompt-Quellenzeile für den Rettungs-Feed beschreibt einen Tag, den das Bild nicht zeigt

**Status: ERLEDIGT (2026-07-24).** `pages/appendix.tex` — „den Tag \enquote{gerettet: [Zutat]}" durch „einen Tag mit der geretteten Zutat" ersetzt. Rein mechanisch, kein Bildwechsel.

- **Befund**: `pages/appendix.tex:55` gibt den Erstellungs-Prompt für `fig:mockup_feed` wörtlich wieder, einschließlich „den Tag \enquote{gerettet: [Zutat]}". Das abgedruckte Mockup zeigt den Tag ohne Präfix („Bananenschale"), und `04_community_und_feedback.tex:3` beschreibt ihn ebenfalls ohne Präfix („zum Beispiel \enquote{Brokkoli-Strunk}"). Fließtext und Bild stimmen also überein — nur die zitierte Prompt-Zeile passt zu keinem von beiden.
- **Warum**: Dokumentation (10 %). Die `\quelle{}`-Zeile ist der geforderte Transparenznachweis für die KI-Erzeugung. Wenn sie beschreibt, was im Bild nachweislich nicht steht, entwertet sie genau den Nachweis, den sie leisten soll — und ist für einen Prüfer beim Blick von der Bildunterschrift aufs Bild in Sekunden auffindbar.
- **Anweisung**: In `pages/appendix.tex:55` „den Tag \enquote{gerettet: [Zutat]}" durch „einen Tag mit der geretteten Zutat" ersetzen. Rein mechanisch, keine inhaltliche Folge, keine Änderung am Bild.

#### 5.9 Die Zahlen im Profil-Mockup widersprechen der Punkte-Regel im Text

**Status: ERLEDIGT (2026-07-24).** Starre 1:1-Regel in `03_konzept.tex:28` gelockert: Rettungspunkte bemessen sich jetzt nach Menge und Art der verwerteten Zutat statt exakt einem Punkt pro Zutat. `tab:funktionsuebersicht`-Zeile entsprechend angepasst. Mockup-Zahlen (1.240 Punkte / 12,4 kg) sind damit widerspruchsfrei, kein neues Bild nötig.

- **Befund**: `03_konzept.tex:28` legt fest: „sammelt jede verwertete Reste-Zutat einen Rettungspunkt." Das Profil-Mockup (`fig:mockup_profil`) zeigt für die Persona Mara K. **1.240 Rettungspunkte** neben **„12,4 kg Lebensmittel gerettet"**. Nach der Textregel entspräche das 1.240 einzeln verwerteten Zutaten zu je exakt 10 Gramm — bei einer Persona, die laut `tab:persona` vier- bis fünfmal pro Woche kocht.
- **Warum**: Prüferfrage nach innerer Widerspruchsfreiheit. Das Mockup ist ein gefordertes Lieferobjekt und wird gelesen, nicht überblättert. Eine Zahl, die der selbst definierten Mechanik widerspricht, ist ein billiger Fund und untergräbt ausgerechnet die Gamification-Herleitung, die sonst zu den saubersten Passagen der Arbeit gehört.
- **Anweisung**: Kein neues Bild nötig. In `03_konzept.tex:28` die starre 1:1-Regel lockern — etwa: Rettungspunkte bemessen sich nach Menge und Art der verwerteten Zutat. Das macht die Mockup-Zahlen widerspruchsfrei, ist die plausiblere Mechanik und kostet kein zusätzliches Wort. Alternative (teurer, nicht empfohlen): Kennzahlen im Mockup neu erzeugen lassen.

#### 5.10 Für die längste Phase bleibt offen, wer sie leistet

**Status: ERLEDIGT (2026-07-24).** Ressourcen-Spalte in `tab:phasenplanung` für „Design \& Prototyp" (Eigenleistung) und „\ac{MVP}-Entwicklung" (Eigenleistung, ergänzt um mögliche externe Entwicklungsunterstützung) ergänzt. Nach dem Abhängigkeiten-Absatz in `05_phasenplanung.tex` einen Satz eingefügt, der benennt, welche Phasen ohne Fremdleistung auskommen und ab welcher Phase Budget nötig wird.

- **Befund**: `tab:phasenplanung` (`05_phasenplanung.tex:11–15`) nennt in der Ressourcen-Spalte viermal ausdrücklich „Eigenleistung". Für die MVP-Entwicklung (Woche 8–17, mit zehn Wochen die längste Phase) steht dagegen „Frontend-/Backend-Entwicklung; Entwicklungsframework, Datenbank, Hosting" — ohne Angabe, ob diese Entwicklung ebenfalls Eigenleistung ist oder eingekauft wird. Dieselbe Unklarheit bei „UI/UX-Design" in der Design-Phase. Eine Aufwands-, Personen- oder Kostengröße nennt die Arbeit an keiner Stelle.
- **Warum**: Ressourcen sind ein eigenes Bewertungskriterium (10 %, „Zeit/Material effizient", `aufgabe.md:39`). Die Zeitachse ist sauber geplant und mit Puffer versehen; die Ressourcenachse bleibt ausgerechnet für die teuerste Phase unbestimmt. Wer Effizienz beurteilen soll, braucht mindestens die Information, ob dort eine Person, ein Team oder ein Dienstleister arbeitet. Der Kontrast zu den vier expliziten „Eigenleistung"-Zellen macht die Auslassung sichtbar, statt sie zu kaschieren.
- **Anweisung**: In `05_phasenplanung.tex` die Ressourcen-Spalte für „Design \& Prototyp" und „MVP-Entwicklung" um den Träger ergänzen (etwa „externe Entwicklungsleistung" oder „Eigenleistung, ergänzt um …"). Zusätzlich nach Z. 21 einen Satz einfügen, der die Ressourcenlogik benennt: welche Phasen ohne Fremdleistung auskommen und ab welcher Phase Budget nötig wird. Zwei Sätze genügen und bedienen ein bislang nur zur Hälfte belegtes 10-%-Kriterium.

#### 5.11 Wiederkehrendes Satzschlussmuster über alle Kapitel

**Status: ERLEDIGT (2026-07-24).** Drei der empfohlenen Pointen-Schlusssätze gestrichen: `01_ausgangslage_und_problem.tex:3` („… statt es nur privat zu betreiben."), `03_konzept.tex:3` (Schlusssatz der Namensherleitung), `03_konzept.tex:34` („Wer plant, sieht auch, wie viel dieser Plan tatsächlich einspart."). `02_limitationen.tex:3` unangetastet gelassen wie angewiesen.

- **Befund**: Absätze enden auffällig regelmäßig mit einer antithetischen Zweiteilung nach dem Muster „X, nicht/statt Y" oder „für A gut, für B kaum". Fundstellen: `01_ausgangslage_und_problem.tex:3` („… statt es nur privat zu betreiben."), `:5` („… nicht nur zu einer Randnotiz …"), `01_wettbewerbsanalyse.tex:3` („Wer nach einem bestimmten Gericht sucht, findet …. Wer stattdessen …, muss …"), `:5` („Für Inspiration eignet sich TikTok damit gut, für strukturierte Resteverwertung kaum."), `:11` („… die Weitergabe von Lebensmitteln vor dem Verderb, nicht deren Verarbeitung in der eigenen Küche."), `02_zielgruppe.tex:7` („Für Letztere … Nebeneffekt, für die … Teilgruppe … eigenständiges Ziel."), `03_konzept.tex:3` („… nicht nur als reines Werkzeug zur Rezeptsuche."), `:7` („… statt allgemein auf Nachhaltigkeit zu setzen."), `:34` („Wer plant, sieht auch, wie viel dieser Plan tatsächlich einspart."), `02_limitationen.tex:3` („… nicht das gewählte Vorgehen, sondern die Geltung der Ergebnisse").
- **Warum**: Der Text ist sprachlich sauber und gut lesbar — das Problem ist nicht der einzelne Satz, sondern die Regelmäßigkeit. Zehn gleichgebaute Pointen-Schlüsse in vierzehn Dateien sind ein Muster, das in menschlichem Schreiben selten so gleichförmig auftritt. Bei einer Arbeit, die laut `aufgabe.md:23` ohnehin durch Plagiatssoftware läuft, ist stilistische Gleichförmigkeit das falsche Signal.
- **Anweisung**: Drei bis vier dieser Schlusssätze auflösen — entweder ersatzlos streichen (spart zugleich Umfang) oder in eine andere Satzform überführen. Empfohlen zur Streichung, weil sie den vorangehenden Absatz nur wiederholen: `01_ausgangslage_und_problem.tex:3` (Schlusssatz), `03_konzept.tex:3` (Schlusssatz der Namensherleitung), `03_konzept.tex:34` (Schlusssatz). **Nicht anfassen**: `02_limitationen.tex:3` — dort trägt die Zweiteilung eine echte inhaltliche Unterscheidung zwischen Vorgehen und Geltung.

---

### Tragende Stärken (nicht wegschreiben)

Die Überarbeitung darf an diesen Stellen nichts kürzen oder glätten — sie sind der Grund, warum die Arbeit trotz der Befunde oben gut dasteht:

- **Die selbst aufgelöste SDG-Spannung** (`06_evaluation_reflexion.tex:5`). Die Arbeit erhebt einen ernsten Einwand gegen sich selbst — gesellschaftliche Legitimation über SDG 12.3 bei gleichzeitiger Verengung auf bereits Überzeugte — und beantwortet ihn. Das ist genau der Zug, dessen Fehlen sonst Punkte kostet.
- **Die vorsichtige Einordnung der Soma-Zahl** (`03_konzept.tex:30`). Die 51 Prozent werden angeführt und im selben Atemzug gegen Übertragung auf die eigene Mechanik abgegrenzt. Diese Zurückhaltung ist selten und wird von Prüfern bemerkt.
- **Die dreischichtigen Limitationen** (`02_limitationen.tex`). Nutzertest, Mockup-Herkunft, Marktabdeckung — jede Grenze mit Konsequenz für die Geltung der Aussagen, nicht als Pflichtübung.
- **Die begründeten Verzichte**. Event-Kalender (`03_konzept.tex:55`) und Forum/Gruppen (`04_community_und_feedback.tex:7`) werden nicht ausgelassen, sondern ausgeschlossen — mit Begründung, im zweiten Fall sogar literaturgestützt. Befund 5.5 verlangt eine Bereinigung der Wettbewerbs-Kriterien, **nicht** die Rücknahme des Verzichts.
- **Die Trennung zwischen literaturbasierten Hebeln und eigener Konzeptleistung** (`01_kernergebnisse_und_ausblick.tex:5`). Der Text sagt ausdrücklich, dass das Alleinstellungsmerkmal aus eigener Marktbeobachtung stammt und nicht aus der Verhaltensliteratur.
- **Die Kapitelanteile** (13,5 / 71,5 / 15,0 %) liegen sauber im geforderten Korridor.

### Umfangshinweis

Fließtext über alle 14 Kapiteldateien inklusive Tabelleninhalte: **rund 4.250 Wörter**, geschätzt **9–10 Seiten** Textteil gegen die Vorgabe 7–10 (`aufgabe.md:18`). Die Arbeit liegt damit am oberen Rand; nach Runde 4 ist der einfache Kürzungsspielraum weitgehend ausgeschöpft.

Konsequenz für diese Runde: **Additive Befunde brauchen Kompensation.** Netto-Zugaben entstehen bei 5.2 (~40 Wörter), 5.3 (~25, davon ein Teil durch die gestrichenen Einzelvermerke gegenfinanziert), 5.7 Option A (~15), 5.10 (~35) und, falls Option A gewählt wird, 5.1 (~60). Netto-Abzüge liefern 5.11 (~40) und 5.6 (wortneutral). Ohne 5.1 Option A geht die Runde etwa auf null auf; mit ihr sollte vorher ein lokaler Build den tatsächlichen Seitenstand messen.

**Nutzer-Schritt vor der Umsetzung**: `latexmk -lualatex main.tex` laufen lassen und den Seitenumfang des Textteils ablesen. Bei ≤ 9 Seiten ist 5.1 Option A gefahrlos; bei ≥ 9,5 Seiten auf Option B oder C ausweichen.

### Gesamteinschätzung

Die Arbeit erfüllt die Aufgabenstellung in der Substanz. Alle sechs Lieferobjekte liegen vor, alle drei Teilaufgaben sind bearbeitet, alle geforderten Berichtsinhalte und Schlüsselbegriffe kommen vor, die Verengung der Zielgruppe ist begründet, und die Arbeit geht an mehreren Stellen über das Geforderte hinaus — insbesondere in der Selbstkritik. Es gibt keinen schweren Befund im Sinne eines fehlenden Artefakts oder einer unbelegten Kernbehauptung.

Die Befunde dieser Runde teilen sich in drei Gruppen. **Sichtbarkeit** (5.1, 5.2, 5.4): Geleistetes ist da, aber an der Stelle, an der ein Prüfer es sucht, nicht auffindbar — das sind die Befunde mit dem besten Verhältnis von Aufwand zu Wirkung. **Nachweisbarkeit** (5.3, 5.10, 5.6): Ein 25-%- und ein 10-%-Kriterium sind jeweils nur zur Hälfte bedient, obwohl das Material für die andere Hälfte im Text schon vorhanden ist. **Konsistenz** (5.5, 5.7, 5.8, 5.9, 5.11): kleine Widersprüche zwischen Text, Tabelle und Mockup, einzeln harmlos, in Summe der Eindruck, dass Text und Artefakte nicht letztgeprüft wurden.

Priorität, falls nur ein Teil umgesetzt wird: **5.4 und 5.2 zuerst** (billig, direkt auf Qualität 25 %), dann **5.3 und 5.6** (beide auf Prozess 25 %), dann **5.1**, dann der Rest.

### Nächster Schritt

**Abgearbeitet (2026-07-24).** Alle elf Befunde (5.1–5.11) umgesetzt. Die beiden `[FREIGABE]`-Punkte (5.1, 5.5) wurden per `AskUserQuestion` geklärt: 5.1 Option B (TikTok stellvertretend für Instagram), 5.5 (a)+(b) vollständig umgesetzt (Following ergänzt, an vorhandene Mockup-Struktur angebunden, kein neues Bild). Der lokale Build zur Seitenmessung (Umfangshinweis) blieb aus — Nutzer-Entscheidung: konservativ planen, alle wortarmen Optionen (B/A ohne neues Bild) gewählt, kein Risiko für den 7–10-Seiten-Korridor. `check_formalia.py`: 0 FEHLER, 11 HINWEIS (ausschließlich bekannte Tabellen-/Satzlängen-Artefakte). `check_bib_keys.py`: alle 5 in Kapitel 2 genutzten Keys valide. Strukturänderung (neue Subsection `sec:iteratives_design`) in `kapitelplan.md` nachgezogen.

„Offen" ist damit vollständig leer. Nächster Schritt laut Fahrplan: Gesamt-Stresstest (bei Papiertyp Projektbericht optional, siehe `CLAUDE.md` → Kompakt-Prüfkette) oder direkt Voll-Audit.

## Offen

### Runde 6 — Gegenlesung (2026-07-24)

Kalte Prüfer-Gegenlesung ausschließlich gegen `aufgabe.md` und `sources/Anmerkungen vom Prüfer.md`. Gelesen wurden nur die Aufgabenstellung, alle 15 `chapters/**/*.tex`, `pages/appendix.tex`, `pages/acronyms.tex`, `pages/chapters.tex`, `main.tex` (nur zur Prüfung, ob der Anhang tatsächlich kompiliert wird), die vier Mockup-Bilder und `references.bib` zur Zählung. Kapitelplan, Prüfbericht, Projektstatus und frühere Runden dieser Datei wurden bewusst nicht gelesen.

#### Soll-Ist-Tabelle (Schritt 3)

| Geforderter Inhalt (wörtlich aus `aufgabe.md`) | Erfüllung |
|---|---|
| Teilaufgabe 1: Analyse bestehender Plattformen, Stärken/Schwächen bzgl. Rezept-Austausch, -Entdeckung, Kommunikation | erfüllt, aber ohne jeden Quellennachweis — `01_wettbewerbsanalyse.tex:3–36`, `tab:wettbewerbsvergleich` deckt alle drei Achsen plus zwei Nischenkriterien ab (Befund 6.1) |
| Teilaufgabe 2: Konzeptentwicklung mit innovativen Funktionen für Rezept-Teilen, Kochtipp-Austausch, gegenseitige Inspiration | erfüllt, aber Innovationsanspruch nie explizit ausgewiesen — `03_konzept.tex:9–55`, `tab:funktionsuebersicht` (Befunde 6.4, 6.5) |
| Teilaufgabe 3: Beschreibung geplanter Feedback-Schleifen | erfüllt — eigene Subsection `sec:iteratives_design`, `07_iteratives_design.tex:3–5`, hypothetischer Charakter sauber gekennzeichnet |
| Berichtsinhalt Zielgruppe | erfüllt — `02_zielgruppe.tex:1–9` plus Persona `tab:persona` in Anhang A |
| Berichtsinhalt Funktionalitäten | erfüllt — `03_konzept.tex:9–55`, `tab:funktionsuebersicht` |
| Berichtsinhalt User Interface (UI) und User Experience (UX) | erfüllt, aber eine Text-Behauptung wird vom Mockup nicht gedeckt — `03_konzept.tex:53`, `fig:mockup_start` bis `fig:mockup_feed` (Befunde 6.2, 6.3) |
| Berichtsinhalt Community-Building | erfüllt — `04_community_und_feedback.tex:3–7`, Rettungs-Feed, Following, Challenges |
| Schlüsselbegriff Rezept-Uploads (Foto/Video) | erfüllt — `03_konzept.tex:32`, `tab:funktionsuebersicht` Z. 44 |
| Schlüsselbegriff Kommentar-/Bewertungssysteme | erfüllt — `03_konzept.tex:32`, `04_community_und_feedback.tex:3` |
| Schlüsselbegriff Personalisierte Empfehlungen | erfüllt — `03_konzept.tex:32`, `tab:funktionsuebersicht` Z. 46 |
| Schlüsselbegriff Gruppen/Foren | erfüllt durch begründeten Verzicht — `04_community_und_feedback.tex:7`, Begründung über Soma et al. |
| Schlüsselbegriff Event-Kalender (bei Auslassung explizit begründen) | erfüllt — ausdrücklicher, begründeter Verzicht in `03_konzept.tex:55` |
| Schlüsselbegriff Lebensmittel-Journaling/Menüplanung | erfüllt im Text, im Mockup nicht sichtbar — `03_konzept.tex:34`, `tab:funktionsuebersicht` Z. 47 (Befund 6.2) |
| Verengung der Zielgruppe explizit benennen und begründen | erfüllt — `02_zielsetzung_und_verengung.tex:5–7`, erneut aufgegriffen in `02_zielgruppe.tex:3` |
| Lieferobjekt Wettbewerbsvergleich (Tabelle) | erfüllt — `tab:wettbewerbsvergleich`, 6 Plattformen × 5 Kriterien |
| Lieferobjekt Persona | erfüllt — `tab:persona`, Anhang A, als fiktiv gekennzeichnet |
| Lieferobjekt UI/UX-Mockup, KI-Nutzung gekennzeichnet | erfüllt, aber mit gestalterischem Fehler — Anhang B, vier Abbildungen, Prompts und Nachbearbeitung in jeder `\quelle{}`-Zeile dokumentiert (Befund 6.3) |
| Lieferobjekt Plattformname | erfüllt — `03_konzept.tex:3`, Name hergeleitet |
| Lieferobjekt Funktionsübersicht | erfüllt — `tab:funktionsuebersicht` |
| Lieferobjekt Phasenplanung | erfüllt — `tab:phasenplanung`, mit Zeitrahmen, Ressourcenträger, Abhängigkeiten und zwei Risiken |
| Genannte Einstiegsliteratur (Hansch & Rentschler; Kapoor et al.) | nicht erfüllt (laut `aufgabe.md` nicht verpflichtend) — beide fehlen in `references.bib` (Befund 6.8) |
| Quellen 5–10 | erfüllt — 6 Einträge in `references.bib`, alle im Text verwendet |
| Struktur 10–15 / 70–80 / 10–15 % | erfüllt — gemessen 12,4 / 74,6 / 13,0 % des Fließtexts |
| Seitenumfang 7–10 | nicht abschließend prüfbar ohne lokalen Build — Schätzung 9–10 Seiten, siehe Umfangshinweis |
| Anonymisierung personenbezogener Daten | erfüllt — keine realen Personen, Persona ausdrücklich als fiktiv geführt |

#### 6.1 Wettbewerbsanalyse ohne eine einzige Quellenangabe  🔴 schwer  [FREIGABE]
- **Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: Option A kombiniert mit Option C.** `\quelle{}`-Zeile von `tab:wettbewerbsvergleich` um alle sechs offiziellen Web-Auftritte (chefkoch.de, tiktok.com, restegourmet.de, zugutfuerdietonne.de, leftovercooking.app, foodsharing.de) und das Sichtungsdatum Juli 2026 erweitert. Nicht überprüfbare Detailangaben abgeschwächt: „über zwanzig Food-Creator:innen" → „Mehrere Food-Creator:innen" (Z. 9), „bis zu drei übrige Zutaten" → „mehrere übrige Zutaten" (Z. 7). Nutzer-Vorbehalt „nur zitierfähige Quellen, keine Blogs" geprüft: Die Wettbewerbsanalyse ist laut ZITIERREGEL (`kapitelplan.md`) ohnehin eigene Sichtung, kein `\parencite`-Fall — die ergänzten Angaben sind ausschließlich die offiziellen Domains der sechs Plattformen selbst, keine Blogs oder Testberichte Dritter. Die BMEL-App-Domain wurde vorab per Websuche verifiziert (zugutfuerdietonne.de ist die offizielle Kampagnenseite).
- **Befund**: `chapters/02_durchfuehrung/01_wettbewerbsanalyse.tex` enthält über sechs Plattformen konkrete, nachprüfbare Tatsachenbehauptungen — „Beide nehmen bis zu drei übrige Zutaten entgegen", „die BMEL-App ergänzt das um einen Portionenrechner" (Z. 7), „Über zwanzig Food-Creator:innen teilen zusätzlich eigene Rezepte in der App" (Z. 9), Fairteiler-Mechanik von Foodsharing.de (Z. 11) — und trägt dabei keinen einzigen Beleg. Der einzige Nachweis ist der Methodensatz in Z. 15 („eigene Sichtung der jeweiligen Web-Auftritte und Apps aller sechs Plattformen im Juli 2026"). Weder im Fließtext noch in der `\quelle{}`-Zeile von `tab:wettbewerbsvergleich` (Z. 31) steht eine URL oder ein Abrufdatum.
- **Warum**: Die Prüfer-Anmerkung verlangt ausdrücklich eine „nachvollziehbare Vergleichsanalyse bereits bestehender Plattformen …, auf deren Ergebnisse dann deine weiteren Entscheidungen beruhen" (`sources/Anmerkungen vom Prüfer.md`, Antwort zu Frage 1), und Punkt 1d verlangt Belege dort, wo das Vorgehen belegt werden sollte. Dieses Kapitel trägt die gesamte Marktlücke und damit die Existenzberechtigung des Konzepts; es ist zugleich das einzige Kapitel mit Rechercheanspruch, das ohne Nachweis auskommt. Bewertungsbezug: Qualität (25 %) und Dokumentation (10 %). Die Angabe „über zwanzig Food-Creator:innen" ist für einen Prüfer schlicht nicht überprüfbar.
- **Anweisung**: Option A (empfohlen, umfangsneutral, eine Zeile): `\quelle{}`-Zeile von `tab:wettbewerbsvergleich` in `01_wettbewerbsanalyse.tex:31` erweitern zu „Eigene Darstellung auf Basis eigener Sichtung der Web-Auftritte und Apps von chefkoch.de, tiktok.com, restegourmet.de, zugutfuerdietonne.de, leftovercooking.app und foodsharing.de, Juli 2026." Option B: je Plattform eine Fußnote mit URL und Abrufdatum an der Erstnennung (Z. 3, 5, 7, 9, 11). Option C (zusätzlich zu A oder B): die nicht überprüfbaren Detailangaben „über zwanzig Food-Creator:innen" (Z. 9) und „bis zu drei übrige Zutaten" (Z. 7) auf unbestimmte Formulierungen abschwächen. Berührt eigene Rechercheergebnisse, daher Freigabe erforderlich.

#### 6.2 Startseiten-Mockup zeigt den behaupteten Zugang zu Menüplanung und Reste-Journal nicht  🟠 mittel
- **Status: ERLEDIGT (2026-07-24), Option A.** Startseiten-Beschreibung in `03_konzept.tex` um den Menüplanungs-/Reste-Journal-Zugang gekürzt; im Menüplanungs-Absatz stattdessen ein Halbsatz ergänzt, der die Funktion als Unterbereich der Startseite verortet und erklärt, warum die Navigation bei drei statt vier Hauptbereichen bleibt.
- **Befund**: `chapters/02_durchfuehrung/03_konzept.tex:53` beschreibt „einer Startseite mit Reste-Eingabefeld, Rezeptvorschlägen und einem Zugang zu Menüplanung und Reste-Journal" und verweist dafür auf `fig:mockup_start`. Das Bild `images/durchfuehrung/resteria_startseite.png` zeigt Reste-Eingabefeld, Rezeptvorschläge, Lesezeichen-Icon, Profil-Avatar und eine Drei-Tab-Navigation (Start / Rettungs-Feed / Profil). Ein Zugang zu Menüplanung oder Reste-Journal ist auf keinem der beiden Startseiten-Mockups sichtbar, auch nicht in `resteria_startseite_bookmarks.png`.
- **Warum**: Prüferfrage „Existiert, was behauptet wird?". Die Menüplanung ist keine Nebenfunktion: `tab:funktionsuebersicht` (Z. 47) führt sie als „Zero-Waste-Kernmechanismus", `06_evaluation_reflexion.tex:3` verbucht sie als Erfüllung des Aufgaben-Schlüsselbegriffs „Lebensmittel-Journaling/Menüplanung", und `03_konzept.tex:5` will sie in erweiterter Form sogar verkaufen. Ein Prüfer, der Text und Anhang B nebeneinanderlegt, findet für die einzige explizit als Startseiten-Element benannte Funktion keinen Beleg — und das ausgerechnet im UI/UX-Teil, den die Prüfer-Anmerkung als eigene Fachexpertise hervorhebt.
- **Anweisung**: Option A (kein neues Bild, umfangsneutral): Satz in `03_konzept.tex:53` an das Bild angleichen, also den Zugang zu Menüplanung/Reste-Journal aus der Startseiten-Beschreibung herausnehmen und die Funktion stattdessen im Menüplanungs-Absatz (Z. 34) verorten, ohne eine sichtbare Schaltfläche zu behaupten. Option B: Folge-Prompt an Claude Design, der auf der Startseite eine Karte oder Zeile „Wochenplan & Reste-Journal" ergänzt, Bild ersetzen und die `\quelle{}`-Zeile von `fig:mockup_start` in `pages/appendix.tex:34` um den Folge-Prompt erweitern.

#### 6.3 Gestalterischer Fehler in den Mockups: Plus-Button verdeckt ein Bedienelement  🟠 mittel
- **Status: TEILWEISE ERLEDIGT (2026-07-24) — Vorbereitung abgeschlossen, Bildaustausch bleibt Nutzer-Schritt.** Folge-Prompt („Anpassung 3") in `sources/claude-design-nachbesserung.md` ergänzt: Plus-Button-Position + Foto-Platzhalter ohne Doppelpunkt. Die `\quelle{}`-Zeile für `fig:mockup_feed` in `pages/appendix.tex` ist bereits auf den kombinierten Prompt (Runde 1 + Anpassung 1 + Anpassung 3) vorbereitet. `resteria_rettungsfeed.png` selbst ist noch der alte Stand — die Bildkorrektur läuft wie bei den vorherigen Nachbesserungsrunden über Claude Design außerhalb dieser Session.
- **Befund**: In `images/durchfuehrung/resteria_rettungsfeed.png` (eingebunden als `fig:mockup_feed`, `pages/appendix.tex:51–56`) überlagert der schwebende Terracotta-Plus-Button die Aktionsleiste des ersten Beitrags und verdeckt das dort rechts liegende Lesezeichen-Icon teilweise. Zusätzlich tragen die Foto-Platzhalter in allen vier Mockups die Beschriftung „Foto:" mit Doppelpunkt und ohne Folgetext, was wie ein abgeschnittener Platzhalter-String wirkt.
- **Warum**: Der Prüfer erlaubt KI-generierte Designvorlagen ausdrücklich nur, „sofern sie keine inhaltlichen oder gestalterischen Fehler enthält" (`sources/Anmerkungen vom Prüfer.md`, Antwort zu Frage 2). Ein Overlay, das ein Interaktionselement verdeckt, ist genau so ein Fehler und wiegt in einer Arbeit schwerer, in der UI/UX laut Prüfer-Anmerkung 1c die eigene Studienschwerpunkt-Expertise unterstreichen soll.
- **Anweisung**: Folge-Prompt an Claude Design in `sources/claude-design-nachbesserung.md` ergänzen: Plus-Button so positionieren, dass er keine Beitrags-Aktionsleiste überlappt (etwa knapp über der Tab-Bar mit Abstand zur Like-/Kommentar-/Lesezeichen-Zeile), und die Platzhalter-Beschriftung von „Foto:" auf „Foto" ohne Doppelpunkt ändern. Danach die betroffenen Bilder in `images/durchfuehrung/` ersetzen und den Nachbesserungs-Prompt in der `\quelle{}`-Zeile von `fig:mockup_feed` (`pages/appendix.tex:55`) mitführen, wie es dort für die bisherigen Folge-Prompts bereits geschieht.

#### 6.4 Innovationsanspruch wird nie explizit eingelöst  🟠 mittel
- **Status: ERLEDIGT (2026-07-24).** Zwei Sätze nach `tab:funktionsuebersicht` in `03_konzept.tex` ergänzt, die trennen, was gegenüber den untersuchten Plattformen neu ist (Kopplung Menüplanung/Reste-Journal an Rettungspunkte, verpflichtender Reste-Tag, zeitlich begrenzte Challenges) und was bewusst aus etablierten Rezept-Communitys übernommen ist (Upload, Bewertung/Kommentare, personalisierte Empfehlungen).
- **Befund**: Weder „innovativ" noch „Innovation" kommt in `chapters/` an einer einzigen Stelle vor. Teilaufgabe 2 verlangt wörtlich eine Plattform „mit innovativen Funktionen"; das Bewertungskriterium Kreativität (15 %) nennt laut `aufgabe.md:39` ausdrücklich „Vergleich zu bestehendem Produkt + Innovationskraft". Die Arbeit argumentiert die Neuheit ausschließlich implizit über die Marktlücke (`01_wettbewerbsanalyse.tex:34` und `:36`, `01_kernergebnisse_und_ausblick.tex:3`), benennt aber nirgends, welche einzelne Funktion in welcher Hinsicht neu ist und welche bewusst von bestehenden Plattformen übernommen wurde.
- **Warum**: Kreativität ist mit 15 % gewichtet und hat zwei Dimensionen. Die erste (Vergleich zum Bestand) ist über `tab:wettbewerbsvergleich` stark abgedeckt, die zweite bleibt der Interpretation des Prüfers überlassen. Genau der Fehlertyp, bei dem eine starke Dimension die schwache verdeckt.
- **Anweisung**: In `chapters/02_durchfuehrung/03_konzept.tex` unmittelbar nach `tab:funktionsuebersicht` (nach Z. 51) zwei bis drei Sätze ergänzen, die trennen, was gegenüber dem in `\autoref{sec:wettbewerbsanalyse}` untersuchten Bestand neu ist (die Kopplung von Reste-Journal und Menüplanung an die Rettungspunkte, der verpflichtende Reste-Tag bei jedem Feed-Beitrag, zeitlich begrenzte Challenges anstelle von Forum und Gruppen) und was bewusst übernommen ist (Upload, Bewertung, Kommentare, personalisierte Empfehlungen). Zugabe über Befund 6.9 gegenfinanzieren.

#### 6.5 „Kochtipp-Austausch" als wörtlich geforderte Funktion nicht wiederauffindbar  🟢 Hinweis
- **Status: ERLEDIGT (2026-07-24).** Herleitungsspalte in `tab:funktionsuebersicht` von „Aufgabenstellung: Kommunikation" zu „Aufgabenstellung: Kochtipp-Austausch" geändert. Kostet keine Zeile Umfang.
- **Befund**: Teilaufgabe 2 nennt wörtlich „Rezept-Teilen, Kochtipp-Austausch, gegenseitige Inspiration" (`aufgabe.md:14`). Der Begriff „Kochtipp" kommt in der gesamten Arbeit nicht vor; abgedeckt ist er nur als „Zubereitungstipps" in `03_konzept.tex:32`. In der Herleitungsspalte von `tab:funktionsuebersicht` steht für das Bewertungs- und Kommentarsystem (Z. 45) „Aufgabenstellung: Kommunikation", während die Nachbarzeilen die Aufgaben-Vokabeln „Rezept-Teilen" (Z. 44) und „Inspiration" (Z. 46) wörtlich führen.
- **Warum**: Reiner Sichtbarkeitsbefund, aber an der teuersten Stelle: Die Herleitungsspalte ist erkennbar als Abhakhilfe für den Prüfer gebaut, und genau dort fehlt eine der drei wörtlich geforderten Funktionen.
- **Anweisung**: In `chapters/02_durchfuehrung/03_konzept.tex:45` in der Spalte „Herleitung/Bezug" „Aufgabenstellung: Kommunikation" zu „Aufgabenstellung: Kochtipp-Austausch" ändern. Kostet keine Zeile Umfang.

#### 6.6 Freemium-Modell kollidiert mit dem eigenen Community-Konzept  🟠 mittel  [FREIGABE]
- **Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: Option B.** „exklusive Challenges" aus dem kostenpflichtigen Zusatzpaket in `03_konzept.tex` gestrichen und durch ein community-neutrales Merkmal ersetzt (erweiterte Vorratsverwaltung). Damit bleibt das einzige aktive Community-Format der Plattform vollständig kostenlos.
- **Befund**: `03_konzept.tex:5` führt „exklusive Challenges" und „erweiterte Menüplanung" als Bestandteile eines kostenpflichtigen Zusatzpakets. `04_community_und_feedback.tex:7` macht zeitlich begrenzte Challenges zum einzigen aktiven Interaktionsformat der Plattform, nachdem Forum und Nutzergruppen begründet gestrichen wurden. Die Menüplanung führt `tab:funktionsuebersicht` (Z. 47) zugleich als „Zero-Waste-Kernmechanismus". Der Text erhebt diesen Einwand gegen sich selbst nirgends und beantwortet ihn nicht.
- **Warum**: Prüferfrage nach Widersprüchen in den eigenen Festlegungen. Wenn das einzige aktive Community-Format teilweise hinter einer Bezahlschranke liegt, untergräbt das die Argumentation in `06_evaluation_reflexion.tex:5`, wonach die gesellschaftliche Wirkung mittelbar über Reichweite und Community entsteht, und ebenso den in `04_community_und_feedback.tex:5` beschriebenen Osmose-Mechanismus, der eine Mindestzahl aktiver Nutzer:innen braucht.
- **Anweisung**: Option A: In `03_konzept.tex:5` präzisieren, dass Basis-Challenges und die Basis-Menüplanung kostenlos bleiben und das Zusatzpaket nur ergänzende Formate enthält, etwa Partner-Challenges oder längere Auswertungszeiträume. Ein Halbsatz genügt. Option B: „exklusive Challenges" aus dem Zusatzpaket streichen und durch ein community-neutrales Merkmal ersetzen (z. B. erweiterte Vorratsverwaltung). Berührt eine tragende Konzeptentscheidung und die wirtschaftliche Transfer-Dimension, daher Freigabe erforderlich.

#### 6.7 Entstehungsgeschichte des Berichts nur punktuell dokumentiert  🟠 mittel
- **Status: ERLEDIGT (2026-07-24).** Vier Sätze vor dem Lessons-Learned-Absatz in `06_evaluation_reflexion.tex` ergänzt: chronologischer Ablauf von Nischenwahl über Plattform-Sichtung (Juli 2026) und Literaturrecherche zu Funktions-/Gamification-Konzept und Mockup-Erstellung; die Mockup-Nachbesserungsrunde ist als Beleg tatsächlich durchlaufener Iteration ausdrücklich genannt.
- **Befund**: `06_evaluation_reflexion.tex:7` nennt zwei Kursänderungen (Wechsel des Community-Zuschnitts nach dem Soma-Befund, Korrektur des Arbeitstitels nach einer Namenskollision) und `:9` drei Lehren. Ein zusammenhängender Ablauf der eigenen Arbeitsschritte fehlt: In welcher Reihenfolge Nischenwahl, Plattform-Sichtung, Literaturrecherche, Funktionskonzept und Mockup-Erstellung stattfanden, steht nirgends. `tab:phasenplanung` beschreibt ausschließlich die künftige Umsetzung von Resteria, nicht die Entstehung dieses Berichts.
- **Warum**: `aufgabe.md:39` nennt für das Kriterium Dokumentation (10 %) ausdrücklich „Entstehungsgeschichte lückenlos". Ein Prüfer, der dieses Kriterium abhakt, stößt zuerst auf die Phasenplanung, hält sie kurz für die Antwort und stellt dann fest, dass sie ein Zukunftsplan ist. Das Material für eine echte Entstehungsgeschichte ist vorhanden, es steht nur nicht im Text.
- **Anweisung**: In `chapters/02_durchfuehrung/06_evaluation_reflexion.tex` vor dem Lessons-Learned-Absatz (vor Z. 9) drei bis vier Sätze ergänzen, die den tatsächlichen Ablauf chronologisch benennen: Aufgabenwahl und Setzung der Zero-Waste-Nische, Sichtung der sechs Plattformen im Juli 2026, Literaturrecherche zu Nudges und Gamification, Ableitung des Funktions- und Gamification-Konzepts, Mockup-Erstellung mit anschließender Nachbesserungsrunde, abschließende Reflexion. Die Mockup-Nachbesserung ist dabei der belastbarste Beleg für tatsächlich durchlaufene Iteration und sollte ausdrücklich vorkommen. Zugabe über Befund 6.9 gegenfinanzieren.

#### 6.8 Von der Aufgabenstellung genannte Einstiegsliteratur kommt nicht vor  🟢 Hinweis
- **Status: ÜBERSPRUNGEN (2026-07-24), Option B — konsistent mit Runde 1 und Runde 3.** Beide Quellen fehlen weiterhin in `references.bib` (nur Zotero/BBT-Import zulässig, keine manuelle Bearbeitung); die Aufnahme ist laut `aufgabe.md` ausdrücklich nicht Pflicht.
- **Befund**: `references.bib` enthält sechs Einträge (Barker, Nivedhitha, Shen, Soma, UN, Vittuari), alle im Text verwendet. Die beiden in `aufgabe.md:26–28` unter „Materialien" genannten Titel — Hansch & Rentschler (2012), *Emotion@Web*, und Kapoor et al. (2018), *Advances in Social Media Research* — sind weder zitiert noch im Verzeichnis.
- **Warum**: Beide sind laut `aufgabe.md` nicht verpflichtend, die Quellenzahl liegt mit sechs im Richtwert 5–10. Ein Prüfer, der die von ihm selbst als Einstieg genannte Literatur in einer Arbeit über eine Social-Media-Plattform überhaupt nicht wiederfindet, registriert das jedoch. Kapoor et al. wäre an genau einer Stelle einschlägig: bei der Begründung, warum eine spezialisierte Plattform gegenüber allgemeinen Social-Media-Plattformen trägt.
- **Anweisung**: Option A: Kapoor et al. (2018) über Zotero/BBT in `references.bib` aufnehmen — die Datei nicht manuell editieren — und in `01_wettbewerbsanalyse.tex:5` oder `01_einleitung/01_ausgangslage_und_problem.tex:3` als einordnenden Beleg setzen. Option B: bewusst darauf verzichten; dann ist nichts zu ändern, der Verzicht ist durch die Nicht-Verpflichtung gedeckt. Bei knappem Seitenbudget ist Option B vertretbar.

#### 6.9 Kontrastfiguren als Dauermuster (KI-Marker)  🟠 mittel
- **Status: ERLEDIGT (2026-07-24).** Fünf Konstruktionen aufgelöst: `03_konzept.tex:7` („leiten sich nicht willkürlich her, sondern"), `03_konzept.tex` Menüplanungs-Absatz („nicht als isolierte Zusatzfunktion ein, sondern"), `02_limitationen.tex:3` („nicht frei erfunden, sondern"), `02_zielgruppe.tex:7` („nicht nur, ob ein Rezept schmeckt, sondern") und `01_kernergebnisse_und_ausblick.tex:3` („stammt nicht aus … sondern"). Zusätzlich eine der beiden Nennungen von „echte Social-Community" ersetzt (`01_kernergebnisse_und_ausblick.tex` → „keinen Ort für Austausch zwischen den Nutzer:innen"). `02_limitationen.tex:3`s zweite, inhaltlich tragende Zweiteilung („nicht das gewählte Vorgehen, sondern die Geltung der Ergebnisse", siehe Runde 5, Befund 5.11) blieb unangetastet.
- **Befund**: Der Text enthält zehn „nicht X, sondern Y"-Konstruktionen und sechs „statt"-Wendungen desselben Typs, verteilt über alle drei Kapitel: `01_ausgangslage_und_problem.tex:5`, `02_zielsetzung_und_verengung.tex:3`, `01_wettbewerbsanalyse.tex:36`, `02_zielgruppe.tex:7`, `03_konzept.tex:7` und `:34`, `06_evaluation_reflexion.tex:5`, `01_kernergebnisse_und_ausblick.tex:3`, `02_limitationen.tex:3` (zweimal). Bei geschätzt neun bis zehn Seiten sind das rund 1,6 pro Seite. Ergänzend wiederholt sich „echte Social-Community" als feste Formel (`01_wettbewerbsanalyse.tex:7`, `01_kernergebnisse_und_ausblick.tex:3`), das Betonungswort „genau" steht fünfmal, „echt" in seinen Formen neunmal.
- **Warum**: `hard-rules-formal.md` → Schreibstil setzt die Obergrenze ausdrücklich bei „höchstens eine ausgeprägte Kontrastkonstruktion pro Seite" und benennt genau dieses Muster samt seiner „statt"-Tarnform als KI-Marker; Signalwörter wie „genau" sollen pro Kapitel höchstens ein- bis zweimal stehen. Beim kalten Lesen fällt der gleichbleibende Antithesen-Rhythmus auf, bevor der Inhalt wirkt — und er ist das einzige durchgehende Stilmerkmal, das den sonst ruhigen, sachlichen Ton stört.
- **Anweisung**: Fünf bis sechs Konstruktionen in einfache Aussagesätze auflösen, bevorzugt dort, wo die Antithese nichts trennt, was nicht ohnehin klar ist: `03_konzept.tex:7` („leiten sich nicht willkürlich her, sondern folgen"), `03_konzept.tex:34` (Absatzschluss „bindet Menüplanung damit nicht als isolierte Zusatzfunktion ein, sondern"), `02_limitationen.tex:3` („nicht frei erfunden, sondern"), `02_zielgruppe.tex:7` („nicht nur, ob ein Rezept schmeckt, sondern") und `01_kernergebnisse_und_ausblick.tex:3` („stammt nicht aus der im Folgenden beschriebenen Verhaltensliteratur, sondern"). Zusätzlich eine der beiden Nennungen von „echte Social-Community" ersetzen. Die Auflösungen sparen je ein bis zwei Zeilen und finanzieren die Zugaben aus 6.4 und 6.7 mit.

#### 6.10 Anhangsverzeichnis erscheint nicht im Inhaltsverzeichnis  🟢 Hinweis
- **Status: ERLEDIGT (2026-07-24).** `\phantomsection` und `\addcontentsline{toc}{section}{Anhangsverzeichnis}` unmittelbar vor der Anhangsverzeichnis-Überschrift in `pages/appendix.tex` ergänzt. `main.tex` blieb unangetastet.
- **Befund**: `pages/appendix.tex:2` setzt das Anhangsverzeichnis als `\subsubsection*{Anhangsverzeichnis}` ohne `\addcontentsline`; auch die Überschriften von Anhang A (Z. 8) und Anhang B (Z. 28) sind unnummerierte Sternüberschriften ohne Eintrag im Inhaltsverzeichnis. `main.tex:337–339` bindet den Anhang ein, führt ihn im Verzeichnis aber nicht auf, während Abbildungs- und Tabellenverzeichnis (`main.tex:291`, `:298`) eingetragen sind.
- **Warum**: Der Prüfer verweist ausdrücklich darauf, Persona, Mockups und Zeitplan in den Anhang zu legen (`sources/Anmerkungen vom Prüfer.md`, Punkt 1c) — er sucht sie also im Inhaltsverzeichnis. Fünf `\autoref`-Verweise aus dem Fließtext zeigen dorthin; ohne Verzeichniseintrag findet ein Prüfer, der die PDF-Navigation nutzt, den Anhang nur durch Blättern.
- **Anweisung**: In `pages/appendix.tex` unmittelbar vor Z. 2 `\phantomsection` und `\addcontentsline{toc}{section}{Anhangsverzeichnis}` ergänzen. `main.tex` bleibt unangetastet, die Ergänzung liegt vollständig in `appendix.tex`.

#### 6.11 Resteria selbst fehlt als Vergleichszeile in der Matrix  🟢 Hinweis (optional)  [FREIGABE]
- **Status: ERLEDIGT (2026-07-24), Nutzer-Entscheidung nach Rückfrage: Option B — unverändert gelassen.** Der Fließtext ab Z. 34 leistet die Einordnung bereits; keine Textänderung.
- **Befund**: `tab:wettbewerbsvergleich` (`01_wettbewerbsanalyse.tex:17–32`) listet sechs Bestandsplattformen, aber keine Zeile für Resteria. Die tragende Aussage, dass keine Plattform Reste-Matching und echte Community kombiniert (Z. 34), muss der Prüfer selbst gegen das erst zwei Unterkapitel später beschriebene Konzept halten.
- **Warum**: Das Bewertungskriterium Kreativität nennt ausdrücklich den „Vergleich zu bestehendem Produkt". Eine Sollzeile würde die Differenzierung auf einen Blick sichtbar machen, an der Stelle, an der der Prüfer sie sucht.
- **Anweisung**: Optional. Option A: Zeile „Resteria (Konzept)" mit angestrebten Werten ergänzen und in der `\quelle{}`-Zeile oder direkt in der Zeilenbeschriftung kenntlich machen, dass es sich um Sollwerte eines Konzepts handelt, nicht um Ergebnisse derselben Sichtung. Option B: unverändert lassen, da der Fließtext ab Z. 34 die Einordnung bereits leistet und die Tabelle so methodisch sauber bleibt. Bei Option A ist der Vorbehalt zwingend mitzuschreiben, sonst entsteht der Eindruck, das eigene Konzept sei gleichrangig erhoben worden. Berührt eigene Rechercheergebnisse, daher Freigabe erforderlich.

#### Bewertungskriterien je Dimension (Schritt 5)

| Kriterium | Dimension | Beurteilung |
|---|---|---|
| Qualität (25 %) | Erfüllt das Ergebnis die Aufgabenstellung | abgedeckt — alle drei Teilaufgaben, alle vier Berichtsinhalte, alle sechs Lieferobjekte vorhanden |
| Prozess (25 %) | Vorgehen dokumentieren | schwach — Methodik je Baustein benannt (`03_vorgehen_und_aufbau.tex:3`, `01_wettbewerbsanalyse.tex:15`), aber ohne Ablauf und ohne Belege (Befunde 6.1, 6.7) |
| Prozess (25 %) | Vorgehen reflektieren | abgedeckt — `06_evaluation_reflexion.tex:7` mit zwei konkreten Kursänderungen statt Leerformel |
| Prozess (25 %) | Grenzen aufzeigen | abgedeckt — `02_limitationen.tex`, dreischichtig und selbstkritisch |
| Transfer (15 %) | Gesellschaftliche Bedeutung | abgedeckt — SDG 12.3, `01_ausgangslage_und_problem.tex:5`, in `06_evaluation_reflexion.tex:5` sauber gegen die Nischenverengung abgewogen |
| Transfer (15 %) | Wirtschaftliche Bedeutung | abgedeckt — Freemium und Kooperationen, `03_konzept.tex:5` (Spannung siehe Befund 6.6) |
| Transfer (15 %) | Ansätze/Modelle begründen | abgedeckt — Drivers/Levers-Rahmen, jede Gamification-Funktion literaturgestützt hergeleitet |
| Kreativität (15 %) | Vergleich zu bestehendem Produkt | abgedeckt — `tab:wettbewerbsvergleich`, sechs Plattformen, differenzierte Wertungen |
| Kreativität (15 %) | Innovationskraft | schwach — nur implizit über die Marktlücke (Befund 6.4) |
| Dokumentation (10 %) | Entstehungsgeschichte lückenlos | schwach — punktuell statt durchgängig (Befund 6.7) |
| Ressourcen (10 %) | Zeit und Material effizient | abgedeckt — `tab:phasenplanung` mit Zeitrahmen, Ressourcenträger je Phase, Abhängigkeiten und Zeitpuffer |

#### Umfangshinweis

Gemessener Fließtext über alle 15 Kapiteldateien: rund 4.680 Wörter einschließlich Tabellenzellen, verteilt auf 581 / 3.493 / 608 Wörter (12,4 / 74,6 / 13,0 %). Die Kapitelanteile liegen damit im Soll von 10–15 / 70–80 / 10–15 %. Bei 11 pt, 1,5-zeilig und 2 cm Rändern entspricht das grob 9 bis 10 Seiten zuzüglich zweier eingebundener Tabellen und einer TikZ-Abbildung im Fließtext — die Arbeit steht am oberen Rand der Vorgabe 7–10 Seiten. Die Runde ist deshalb bewusst so gebaut, dass sie sich selbst finanziert: Die Zugaben aus 6.4 (etwa 60 Wörter) und 6.7 (etwa 70 Wörter) werden durch die Auflösungen aus 6.9 gedeckt, die 6.1 (Option A), 6.5 und 6.10 sind umfangsneutral, und 6.2 Option A sowie 6.6 Option A kürzen leicht. Vor der Umsetzung dennoch ein lokaler Build zur Seitenmessung; liegt die Arbeit über 10 Seiten, zuerst 6.9 umsetzen und die Zugaben aus 6.4 und 6.7 auf je zwei Sätze begrenzen.

#### Gesamteinschätzung

Die Arbeit erfüllt die gestellte Aufgabe. Alle drei Teilaufgaben sind bearbeitet, alle vier wörtlich geforderten Berichtsinhalte vorhanden, alle sechs Lieferobjekte liegen vor, und die beiden Schlüsselbegriffe, auf die verzichtet wird (Event-Kalender, Gruppen/Foren), sind ausdrücklich und begründet ausgeschlossen statt stillschweigend übergangen. Kein Befund dieser Runde ist ein fehlendes Artefakt oder eine nicht ausgeführte Teilaufgabe. Der schwerste Punkt ist ein Nachweisproblem: Das Kapitel, das die Marktlücke und damit die gesamte Konzeptbegründung trägt, kommt ohne einen einzigen Beleg aus, obwohl der Prüfer die Nachvollziehbarkeit dieser Vergleichsanalyse ausdrücklich zur Bedingung gemacht hat (6.1). Danach folgen zwei Stellen, an denen Text und Anhang auseinanderlaufen (6.2, 6.3), zwei Kriteriumsdimensionen, die vorhanden, aber nicht sichtbar eingelöst sind (6.4, 6.7), ein unbeantworteter Einwand gegen die eigene Festlegung (6.6) und ein durchgehendes Stilmuster (6.9). Der Rest sind Hinweise. Mit den Befunden 6.1 bis 6.4 und 6.7 abgearbeitet ist die Arbeit aus Prüfersicht abgabereif.

#### Tragende Stärken — bei der Überarbeitung nicht anfassen

- **Die begründete Verengung.** `02_zielsetzung_und_verengung.tex:5` benennt die Einschränkung auf nachhaltigkeitsorientierte Hobbyköch:innen offen, begründet sie funktional (Gamification wirkt nur bei bereits Motivierten) und kennzeichnet sie in Z. 7 ausdrücklich als argumentative, nicht empirische Annahme. Genau die Bewegung, die eine Gegenlesung sonst als stillschweigende Verengung anstreicht.
- **Die aufgelöste Spannung zwischen SDG-Anspruch und Nischenzuschnitt.** `06_evaluation_reflexion.tex:5` erhebt den naheliegendsten Einwand gegen die eigene Arbeit selbst und beantwortet ihn, statt ihn zu umgehen. Der Absatz ist das stärkste Stück Argumentation im Bericht.
- **Die saubere Trennung von Beleg und Eigenleistung.** `03_konzept.tex:30` sagt ausdrücklich, dass die Soma-Zahl die grundsätzliche Entscheidung für Gamification stützt, nicht die konkrete Punkte-Mechanik. `01_kernergebnisse_und_ausblick.tex:5` wiederholt diese Trennung fürs Fazit. Das ist genau die Zurückhaltung, die Overclaim-Abzüge verhindert.
- **Der begründete Verzicht statt Auslassung.** Event-Kalender (`03_konzept.tex:55`) und Forum/Gruppen (`04_community_und_feedback.tex:7`) werden nicht übergangen, sondern mit Begründung ausgeschlossen, im zweiten Fall sogar literaturgestützt.
- **Die differenzierte Vergleichsmatrix.** `tab:wettbewerbsvergleich` verteilt keine Gefälligkeitswertungen: Chefkoch und Foodsharing erhalten „stark" bei Community, leftovercooking dreimal „stark" oder „mittel", und die Kriteriendefinitionen stehen offen im Text (Z. 13). Der Verdacht ergebnisorientierter Bewertung greift hier nicht.
- **Die SWOT-Einordnung im Fließtext.** `01_wettbewerbsanalyse.tex:34` liefert Stärke, Schwäche, Chancen und Risiken des eigenen Konzepts in Prosa und bedient damit genau den Vorschlag aus der Prüfer-Anmerkung, ohne Platz für ein weiteres Schema zu verbrauchen.
- **Die Anhang-Disziplin.** Persona und alle vier Mockups liegen im Anhang, nicht im Textteil, exakt wie in Prüfer-Anmerkung 1c empfohlen. Die Persona heißt Mara K., und die Mockups sprechen dieselbe Person an („HALLO MARA", „Mara K.", Level 4 Resteheld:in) — eine stille Konsistenz, die beim Lesen sofort auffällt.
- **Die Kennzeichnung der KI-Mockups.** Jede `\quelle{}`-Zeile in `pages/appendix.tex` nennt den vollständigen Prompt, das erzeugende Werkzeug und die nachträgliche manuelle Bearbeitung. Das übererfüllt die Anforderung des Prüfers.
- **Die Struktur.** Kapitel 2 folgt einem erkennbaren Trichter von Markt über Zielgruppe und Konzept zu Community, Iteration, Fahrplan und Reflexion; die Kapitelanteile liegen im vorgegebenen Rahmen.

### Nächster Schritt

**Abgearbeitet (2026-07-24).** Zehn der elf Befunde vollständig umgesetzt, einer (6.8) wie in Runde 1/3 bewusst übersprungen, einer (6.3) nur vorbereitet. Die drei `[FREIGABE]`-Punkte (6.1, 6.6, 6.11) wurden per `AskUserQuestion` geklärt: 6.1 Option A kombiniert mit Option C (Quelle-Zeile um sechs offizielle Plattform-Domains erweitert, unbelegbare Details abgeschwächt — Nutzer-Vorbehalt „keine Blogs zitieren" geprüft und durch die ZITIERREGEL bereits gedeckt), 6.6 Option B (exklusive Challenges aus dem Zusatzpaket gestrichen), 6.11 Option B (unverändert gelassen). 6.3 bleibt teilweise offen: Der Folge-Prompt liegt in `sources/claude-design-nachbesserung.md` bereit und die `\quelle{}`-Zeile ist vorbereitet, aber der tatsächliche Bildaustausch in Claude Design ist wie bei den vorherigen Nachbesserungsrunden ein Nutzer-Schritt außerhalb dieser Session — `resteria_rettungsfeed.png` zeigt bis dahin weiterhin den Plus-Button-Überlapp.

`check_formalia.py`: 0 FEHLER, 12 HINWEIS (ausschließlich bekannte Tabellen-/Satzlängen-Artefakte plus ein neuer Satzschnitt-Hinweis in einer nicht bearbeiteten Datei — kein neuer Regelverstoß). `check_bib_keys.py`: alle 6 Keys valide. Netto-Umfangsänderung dieser Runde: rund +100 bis +140 Wörter (6.4- und 6.7-Zugaben abzüglich der durch 6.9 gestrafften Sätze und der in 6.2 gekürzten Startseiten-Beschreibung) — bei einem Ausgangswert von rund 4.680 Wörtern bleibt die Arbeit im geschätzten 9–10-Seiten-Korridor, ein lokaler Build zur Bestätigung steht weiterhin aus (Nutzer-Schritt, `lualatex`/`latexmk` in dieser Umgebung nicht verfügbar).

„Offen" ist damit bis auf den ausstehenden Bildaustausch (6.3) vollständig leer. Nächster Schritt laut Fahrplan: Gesamt-Stresstest (bei Papiertyp Projektbericht optional, siehe `CLAUDE.md` → Kompakt-Prüfkette) oder direkt Voll-Audit — sobald der Mockup-Austausch für 6.3 erfolgt ist, empfiehlt sich vorher ein kurzer `check_formalia.py`-Lauf wie im Nachbesserungsdokument vermerkt.
