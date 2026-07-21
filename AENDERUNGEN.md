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
