# SKILL-ANPASSUNGEN

Arbeitsdokument, kein Bestandteil der Abgabe. Sammelt Änderungsvorschläge an `CLAUDE.md`, den Skills unter `.claude/skills/` und den Prüfskripten, abgeleitet aus konkreten Befunden der Session vom **2026-07-28**. Jeder Punkt nennt: Beobachtung → warum es kein Einzelfall ist → Zieldatei → konkreter Vorschlag → Aufwand.

Reihenfolge nach erwartetem Nutzen. P1 = mehrfach aufgetreten und automatisierbar, P2 = mehrfach aufgetreten, Regeländerung, P3 = Komfort.

---

## Vorbemerkung: eine frühere Sammlung ist verlorengegangen

`CLAUDE.md` hält unter dem 2026-07-24 fest, `SKILL-VERBESSERUNGEN.md` sei „um drei Workflow-Befunde erweitert" worden (kein Schritt im Fahrplan subtrahiert · Umfangsprüfung hängt allein an Teil-Check D · Redundanz zwischen Dateien ist by design blind). Die Datei existiert nirgends im Repository, auch nicht in der Git-Historie (`git log --diff-filter=A -- "*SKILL*"` ist leer). Die drei Befunde sind damit verloren; aus der Beschreibung in `CLAUDE.md` sind sie nur noch dem Titel nach rekonstruierbar.

**Konsequenz für dieses Dokument:** Es liegt im Projekt-Root, wird eingecheckt, und `CLAUDE.md` verweist darauf. **Zusätzlich:** Der Statuseintrag vom 24.07. ist zu korrigieren, er behauptet eine Datei, die es nicht gibt.

---

## P1-1 · Text-Bild-Lücken dürfen nicht per Textzusatz „geschlossen" werden

**Beobachtung.** Gegenlesungs-Befund 5.7 („Menüplanung ohne UI-Zugang") wurde am 24.07. mit Option A gelöst: Statt das Mockup zu ergänzen, kam der Satz „Erreichbar ist der Bereich über die Startseite" in `03_konzept.tex`. Heute zeigte die Bildsichtung, dass auf beiden Startseiten-Screens kein solcher Zugang existierte. Der Textzusatz hatte die Lücke nicht geschlossen, sondern in eine **überprüfbare Falschaussage** verwandelt — schlechter als der Ausgangszustand, weil der Prüfer KI-Mockups nur ohne gestalterische Fehler zulässt und die Behauptung zwei Seiten später widerlegt wird.

**Kein Einzelfall.** Dieselbe Mechanik drohte heute erneut, als das Reste-Journal ins Profil verlagert wurde; nur die vorherige Bildkontrolle verhinderte, dass die Aussage wieder ins Leere zeigt.

**Ziel:** `.claude/skills/gegenlesung/SKILL.md` und `.claude/skills/schreib-modus/SKILL.md`.

**Vorschlag.** Regel aufnehmen: *Ein Befund „Text behauptet X, Abbildung zeigt X nicht" hat genau zwei zulässige Lösungen — Abbildung ergänzen oder Behauptung streichen. Eine dritte Option, die Behauptung präziser zu formulieren, ohne die Abbildung zu ändern, ist unzulässig, weil sie eine Auslassung in eine widerlegbare Aussage verwandelt.* Wird die Abbildung erst später geliefert, bleibt der Textzusatz bis dahin draußen.

**Aufwand:** klein (Regeltext).

---

## P1-2 · Vor jeder Aussage über eine eigene Abbildung: Bild ansehen

**Beobachtung.** Die Lücke aus P1-1 bestand seit dem 24.07. und überlebte zwei Gegenlesungen, einen Gesamt-Stresstest, zwei Voll-Audits und ein Delta-Re-Audit. Gefunden wurde sie erst, als die vier PNG heute tatsächlich per Read-Tool geöffnet wurden. Beim selben Durchgang fielen zwei weitere Abweichungen auf, die kein Skript sieht: die Singular-/Plural-Drift in `02_limitationen.tex` und die überholte Mitigation „Beschränkung auf die Kernfunktion Reste-Matching", obwohl die Mockups längst Profil, gespeicherte Rezepte und Feed zeigen.

**Ziel:** `.claude/skills/pruef-modus/SKILL.md`, Teil-Check C (Struktur).

**Vorschlag.** Neuer Prüfpunkt **„Abbildungsabgleich"**: Im Voll- und Abgabe-Audit jede Abbildung aus `pages/appendix.tex` und `chapters/` öffnen und gegen alle Textstellen prüfen, die per `\autoref` darauf verweisen oder sie beschreiben. Konkret zu vergleichen sind Anzahl (Singular/Plural), benannte Bedienelemente, behauptete Zugangswege und Zahlenwerte. Aufwand pro Abbildung gering, weil die Verweisstellen über `grep` auf das Label auffindbar sind.

**Aufwand:** mittel (Prüfschritt + Beispiel im Skill).

---

## P1-3 · Ersetzungen aus `AENDERUNGEN.md` werden nicht propagiert

**Beobachtung.** Runde 6, Befund 6.6 ersetzte die „exklusiven Challenges" im Freemium-Paket durch eine „erweiterte Vorratsverwaltung". Der Ersatzbegriff wurde eingesetzt — aber nie in `03_konzept.tex` erklärt, nie in `tab:funktionsuebersicht` aufgenommen, nie in einem Mockup gezeigt. Er stand vier Tage lang als undefinierter Posten im Erlösmodell, und „erweitert" verwies auf eine Basisversion, die es nicht gab.

**Kein Einzelfall.** Runde 4 hinterließ denselben Fehlertyp (Fazit verwies auf „steigende Reste-Level", während `03_konzept.tex` längst „Erinnerungsbenachrichtigung" sagte).

**Ziel:** `.claude/skills/schreib-modus/SKILL.md`, Abschnitt „AENDERUNGEN.md abarbeiten".

**Vorschlag.** Pflichtschritt nach jedem Befund, der einen Begriff **ersetzt oder neu einführt**: `grep -rn "<neuer Begriff>" chapters/ pages/` ausführen. Bei weniger als zwei Fundstellen gilt der Begriff als nicht eingeführt — dann entweder definieren und in die zuständige Tabelle aufnehmen oder den Ersatz verwerfen. Ergebnis im Abarbeitungsvermerk festhalten.

**Aufwand:** klein (ein Befehl, eine Regelzeile).

---

## P1-4 · Zähl- und Numerusangaben systematisch nachziehen

**Beobachtung heute.** „das UI/UX-Mockup" (Singular, es sind vier) in `02_limitationen.tex`; „Eine erste Rückkopplungsschleife" in `07_iteratives_design.tex`, obwohl es inzwischen mehrere sind; dazu die Angleichung von „Eine erste Nachbesserungsrunde" in `06_evaluation_reflexion.tex`.

**Kein Einzelfall.** Derselbe Fehlertyp war Befund 3.1 (Runde 3), erneut FAIL im Delta-Re-Audit vom 24.07. („zwei Einwände", es waren vier), und noch einmal beim Streichen der dritten „Lehre" in der Kürzungsrunde. Fünfter Auftritt in vier Wochen.

**Ziel:** `.claude/skills/_shared/scripts/check_formalia.py`.

**Vorschlag.** Neue Heuristik **ZAHLWORT**: Alle Vorkommen von `ein/eine/erste/zwei/drei/vier/fünf/sechs/mehrere` unmittelbar vor einem Substantiv als Hinweisliste ausgeben, gruppiert nach Substantiv. Kein FEHLER, nur HINWEIS — die Prüfung, ob die Zahl stimmt, bleibt menschlich, aber die Fundstellen müssen nicht mehr erinnert werden. Ergänzend im `pruef-modus` Teil-Check C: Liste einmal komplett durchgehen.

**Aufwand:** mittel (Regex + Test), hoher Ertrag wegen der Wiederholungsrate.

---

## P2-1 · Anhangsverzeichnis: `main.tex`-Sperre blockiert eine Routineänderung

**Beobachtung.** Der Anhangsverzeichnis-Block steht in `main.tex:336–339`. Ein neuer Anhang C erforderte deshalb heute eine **zweite** ausdrückliche Einzelfreigabe des Nutzers (die erste am 23.07. für die Aktivierungsblöcke). Die Alternative wäre ein unvollständig ausgewiesener Anhang gewesen — ein Abgabefehler.

**Zusatzbefund.** `check_formalia.py` prüft laut Quelltext (Z. 116–121, 716 ff.), *ob* ein Anhangsverzeichnis existiert und ob je Anhang ein Textverweis vorliegt. Es prüft **nicht**, ob die Tabellenzeilen mit den tatsächlich vorhandenen `\section*{Anhang~X}` übereinstimmen. Ein Anhang ohne Zeile fällt also durch beide Netze.

**Ziel:** `CLAUDE.md` → Grundprinzipien; `check_formalia.py`.

**Vorschlag.**
1. Regelergänzung: Neben den Aktivierungsblöcken ist **eine** weitere Änderung an `main.tex` freigabefrei — das Pflegen der Anhangsverzeichnis-Tabelle, wenn ein Anhang hinzukommt oder wegfällt. Begründung: Das ist Nachführen eines Verzeichnisses, kein Umbau, und die Alternative ist ein Abgabefehler.
2. Neue Prüfung **ANHANG-ZEILE**: Menge der `\section*{Anhang~X: …}` in `pages/appendix.tex` gegen die Zeilen der Anhangsverzeichnis-Tabelle in `main.tex` abgleichen, Abweichung als FEHLER.

**Aufwand:** klein (Regel) + mittel (Skript).

---

## P2-2 · Zitierregel für iterativ erzeugte KI-Abbildungen fehlt

**Beobachtung.** Beim vierten Mockup-Durchgang war unklar, was bei einem chatbasiert-iterativen Werkzeug überhaupt zu zitieren ist — alle Prompts? nur der erste? Die Antwort musste im Original-PDF nachgeschlagen werden (**Zitierleitfaden S. 20**: „den verwendeten Prompt und das Unternehmen … angeben"; ausdrücklich mit dem Hinweis, dass es „noch keine Standard-Vorgehensweise" gibt). Die KI-Richtlinie v1.0 verweist für Abbildungen zurück auf den Zitierleitfaden und fordert kein Prompt-Protokoll.

**Ziel:** `.claude/skills/_shared/hard-rules-formal.md`, Abschnitt „Eigene Werke / Abbildungskonvention".

**Vorschlag.** Vier Sätze aufnehmen:
1. Zu zitieren sind der Ursprungs-Prompt und die **inhaltlich prägenden** Folge-Prompts, nicht jede Verfeinerung; unbenannte Iterationen werden mit einem Zusatz wie „und in weiteren Iterationsschritten verfeinert" transparent gemacht.
2. Eine Prompt-Angabe ist ein **Zitat der Eingabe**, nicht eine Beschreibung des Ergebnisses. Weicht das Bild vom Prompt ab, bleibt der Prompt trotzdem korrekt zitiert.
3. Prompt-Text **nicht glätten** — auch grammatische Unebenheiten der Eingabe bleiben stehen.
4. Eine `\quelle{}`-Zeile wird **nie im Voraus** für einen noch nicht ausgeführten Prompt geschrieben; sonst enthält das Dokument eine Quellenangabe für einen Vorgang, den es nicht gab.

**Aufwand:** klein.

---

## P2-3 · Kürzen greift bevorzugt tragende Sätze an

**Beobachtung.** Zur Gegenfinanzierung des Rezeptbestand-Satzes wurde heute der Menüplanungs-Satz um sieben Wörter gestrafft — ausgerechnet die einzige Definition des Reste-Journals, das zugleich einzige Beleg für den Schlüsselbegriff „Lebensmittel-Journaling/Menüplanung" und eine der drei beanspruchten Innovationen ist. Im selben Zug fiel beim Straffen der Namensherleitung das Hedge „oft" weg und machte aus einer vorsichtigen eine absolute sprachliche Behauptung; beides wurde erst beim Gegenlesen bemerkt.

**Kein Einzelfall.** Die Kürzungsrunde 4 riss die Mitigationsschicht aus Limitation 2 mit — im Voll-Audit vom 24.07. ein −15-FAIL.

**Ziel:** `.claude/skills/schreib-modus/SKILL.md`, Kürzungs-/Gegenfinanzierungsteil.

**Vorschlag.** Vor jeder Streichung oder Straffung zwei Fragen beantworten und im Vermerk festhalten: (a) Ist dieser Satz die **einzige** Fundstelle eines Abhakliste-Schlüsselbegriffs, einer Pflichtschicht oder eines Lieferobjekts? (b) Enthält er ein Hedge (`oft`, `häufig`, `kann`, `deutet darauf hin`), das bei der Straffung wegfällt? Bei (a) ja: anderen Posten suchen. Bei (b) ja: Hedge im gekürzten Satz erhalten.

Ergänzend automatisierbar: `check_formalia.py` kann Schlüsselbegriffe aus `aufgabe.md` zählen und die mit **genau einer** Fundstelle als HINWEIS ausweisen („einzige Belegstelle — beim Kürzen schützen").

**Aufwand:** klein (Regel), mittel (Skriptteil).

---

## P2-4 · Umfangs-Heuristik wird zu leicht für eine Messung gehalten

**Beobachtung.** `check_umfang.py` schätzte am 28.07. früh 12,5 Seiten; der Build ergab 14. Heute schätzt es 9,9 Seiten bei zuletzt gemessenen 10 — die Richtung stimmt, die Genauigkeit reicht aber nicht, um an der Obergrenze zu entscheiden. Die Abweichung entsteht durch Abbildungen, Tabellen und Seitenumbrüche, die die Wortzahl-Heuristik nicht kennt.

**Zusatz:** Die Warnzeile des Skripts vergleicht Wörter mit Seiten („3.709 > 10") und liest sich wie ein Fehlalarm.

**Ziel:** `check_umfang.py`, `.claude/skills/pruef-modus/SKILL.md`.

**Vorschlag.** (1) Ausgabe umformulieren: gemessene Wortzahl, geschätzte Seiten **mit Angabe der beobachteten Abweichung** (bislang bis +1,5 Seiten), und der Hinweis, dass bei verfügbarem `lualatex` der Build maßgeblich ist. (2) Im Skill festhalten: Liegt die Schätzung im Bereich ±1 Seite um eine Grenze der Vorgabe, ist die Aussage „im Soll" **nur nach Build** zulässig.

**Aufwand:** klein.

---

## P3-1 · Ankündigungssätze als eigene Stilregel

**Beobachtung.** „Auch das Vorgehen selbst verdient einen Blick." war der einzige inhaltsleere Absatzöffner in `06_evaluation_reflexion.tex`, während alle vier übrigen Absätze mit einer belastbaren Aussage beginnen. Die Kürzungsrunde hatte solche Wegweiser-Absätze in den Kapitel-Mastern entfernt, innerhalb der Subsections aber nicht gesucht.

**Ziel:** `.claude/skills/_shared/hard-rules-formal.md`, Abschnitt „Schreibstil (Anti-KI-Muster)".

**Vorschlag.** Regel: *Ein Absatz öffnet mit einer Aussage, nicht mit einer Ankündigung.* Dazu eine Skript-Heuristik auf Formulierungen wie „verdient einen Blick", „sei ein Blick gewidmet", „im Folgenden wird", „soll nun betrachtet werden" als HINWEIS.

**Aufwand:** klein.

---

## P3-2 · Terminologie-Doppelbelegung früher erkennen

**Beobachtung.** „Skizze" bezeichnete gleichzeitig die Persona-Skizze in Anhang A und — über „Mockup-Skizze" und ein verkürztes „Die Skizze" — die vier Mockups. Zwei verschiedene Anhang-Artefakte unter einem Wort.

**Ziel:** `check_formalia.py` oder Teil-Check C.

**Vorschlag.** Für alle Bezeichner, die in einer `\caption{}` vorkommen, prüfen, ob sie im Fließtext auch für ein anderes Objekt verwendet werden — mindestens als Hinweisliste „Begriff X erscheint in Captions zu zwei verschiedenen Labels". Alternativ günstiger: im Prüf-Modus eine Liste aller Caption-Substantive ausgeben und einmal auf Doppelbelegung sichten.

**Aufwand:** mittel.

---

## P3-3 · Rückfragen erst nach Dateiprüfung stellen

**Beobachtung.** Ich habe gefragt, ob der Rezeptbestandsaufbau in Phase 3 oder Phase 1–2 gehört. Die Antwort stand bereits in `05_phasenplanung.tex:3`: Phase 1 und die Mockups aus Phase 2 sind „mit diesem Bericht bereits erbracht", ein dort einsortierter Bestandsaufbau wäre damit als erledigt deklariert worden. Die Frage war aus den Projektdateien entscheidbar und hat eine Antwortrunde gekostet.

**Ziel:** `CLAUDE.md` → Grundprinzipien (bei „Freigabepflichtige Punkte aktiv klären").

**Vorschlag.** Ergänzen: *Vor einer Rückfrage prüfen, ob die Antwort aus `aufgabe.md`, `kapitelplan.md` oder den Kapiteldateien folgt. Rückfragen sind für Entscheidungen reserviert, die der Nutzer treffen muss — nicht für solche, die die Projektdateien bereits treffen.* Das ergänzt die bestehende Regel, die das Gegenteil absichert (Freigabepflichtiges nicht stillschweigend übergehen).

**Aufwand:** klein.

---

## Nicht übernommen

- **Eigener „Kürzungs-Modus" als Skill.** Die Kürzungsarbeit ist inzwischen zweimal im `schreib-modus` gelaufen und hat dort funktioniert; die Fehler entstanden nicht aus fehlender Anleitung, sondern aus fehlender Schutzliste (siehe P2-3). Ein weiterer Skill erhöht nur die Zahl der Einstiegspunkte.
- **Automatische Prüfung, ob Textaussagen zu Bildinhalten passen.** Nicht mechanisierbar; deshalb der manuelle Prüfschritt in P1-2.
