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

**Status: OFFEN — wird zum Schluss gesondert mit dem Nutzer besprochen (2026-07-21), nicht Teil dieser Abarbeitungsrunde.**

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
| UI/UX-Lieferobjekt | **weiter offen** — Mockup-Platzhalter (Runde-1-Befund 1), hier ausgeklammert |

Insgesamt eine argumentativ solide Arbeit, deren Kern (Marktlücke → literaturgestütztes Konzept, mit vorbildlicher Trennung von Beleg und eigener Leistung) trägt. Kein Befund dieser Runde ist abgabekritisch. Der gewichtigste ist GS-1 (reale Gegen-App), weil er das tragende Kernargument berührt und billig zu schärfen ist; GS-3 (Zeitpuffer) ist ein harter, sofort nachrechenbarer Konsistenzfehler. GS-2/GS-4/GS-5/GS-6 heben Präzision und Glaubwürdigkeit. Der einzige abgabekritische Punkt bleibt außerhalb dieser Runde: die fehlenden Mockups (Runde-1-Befund 1).

**Bekannter Hinweis (kein eigener Auftrag):** Die von der Gegenlesung (Prüferfrage 7) notierte USP-/„also"-Wiederholung über die Subsections besteht weiter — beim Abarbeiten ein bis zwei Wiederholungen straffen.

### Nächster Schritt

**Abgearbeitet (2026-07-21):** GS-1 bis GS-6 vollständig umgesetzt (GS-1 nach aktiver Rückfrage: volle Aufnahme von leftovercooking als 6. Plattform, mit Web-Recherche). Runde-1-Befund 1 (UI/UX-Mockups) bleibt weiterhin bewusst offen — auf Nutzerwunsch nicht Teil dieser Abarbeitung, gesondert zu klären. `check_formalia.py` und `check_bib_keys.py` liefen fehlerfrei (0 FEHLER) auf allen betroffenen Kapiteln.

Nächster Schritt laut Fahrplan: **Voll-Audit** (`pruef-modus`), sobald Befund 1 (Mockups) geklärt ist — kein Delta-Re-Audit, da noch kein Vorbericht vorliegt.
