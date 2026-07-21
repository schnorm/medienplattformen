# Formale Hard Rules (alle Papiertypen)

Gilt für `schreib-modus` (beim Verfassen) und `pruef-modus` (Teil-Check A: Formalia). **Nicht relevant für `plan-modus`** — deshalb bewusst nicht in `CLAUDE.md`, sondern hier. Liegt zentral in `.claude/skills/_shared/` (eine einzige Kopie, keine Skill-lokalen Duplikate). Inhaltliche, papiertyp-abhängige Regeln stehen separat in `typen/<typ>.md`.

## Zitationen (APA deutsch, IU-Abweichungen)

- `\parencite[S. X]{key}` bei stellenbezogenen indirekten Zitaten (Pflicht). Ausnahme: werkbezogene Paraphrasen nur `Autor, Jahr`.
- BBT-Keys exakt aus `references.bib`, **niemals erfinden** — vor dem Schreiben mit `.claude/skills/_shared/scripts/check_bib_keys.py` validieren. Das Skript meldet auch ungenutzte Bib-Einträge (`--report-unused`).
- 2 Autoren: `&` in Klammer, „und" im Satz. 3+ Autoren: `et al.` ab erster Erwähnung.
- Mehrere Quellen, verschiedene Seiten: `\parencites[S. 12--13]{key1}[S. 5]{key2}`. Gleiche Seite: `\parencite[S. 5]{key1, key2, key3}`.
- Sekundärzitate vermeiden; nur zulässig, wenn Primärquelle nicht beschaffbar. `(Original, Jahr zitiert nach \parencite[S. 12--13]{sekundär})`. Niemals zwei `\parencite{}` kombinieren. Nur die Sekundärquelle steht im Literaturverzeichnis.
- Persönliche Kommunikation: nur im Text, nicht in `references.bib`.
- Direkte Zitate ≤ 40 Wörter: `\enquote{}`. > 40 Wörter: `\begin{blockzitat}`-Umgebung (in `main.tex` definiert: 1,27 cm links eingerückt, **ohne** Anführungszeichen; Zitat endet mit Punkt, Quellenangabe danach: `… Angebote. (S. 40)`).
- Fußnoten: nur für Randbemerkungen, Übersetzungen nicht-englischer Zitate oder Copyright-Hinweise — keine inhaltlichen Ausführungen. 10 Pt., Blocksatz, fortlaufend nummeriert, beginnen mit Großbuchstaben, enden mit Punkt.
- **Nicht als Quellen zulässig:** Vorlesungsskripte, Vorlesungsfolien, Webinars (Zitierleitfaden explizit). Bei referenzierten Inhalten daraus: auf die zitierfähige Primärquelle (Lehrbuch, Veröffentlichung) ausweichen.

## Eigene Werke / Abbildungskonvention

Eigene Abb./Tab.: „Quelle: Eigene Darstellung." in der Caption, kein `\cite{}`. Varianten: `Eigene Darstellung in Anlehnung an` · `Eigene Darstellung (geändert) in Anlehnung an` · `Eigene Darstellung auf der Basis von` · `Übernommen aus`.

**KI-generierte Abbildungen** (Zitierleitfaden 2025): mit Quellenhinweis kennzeichnen — Muster: `Erstellt mit dem Prompt „…" durch <KI-Tool>`. Gilt nicht für Fotos/Cliparts/Bilder aus Online-Datenbanken.

**Abbildungs-Layout (IU-konform):**
- **Beschriftung über der Abbildung/Tabelle** — beginnt mit „Abb. N" bzw. „Tab. N" + Titel, Caption-Block vor `\includegraphics` bzw. vor der Tabelle. Caption vor `\label{}`.
- **Quellenzeile unter der Abbildung/Tabelle** — beginnt mit „Quelle: " in 10 Pt. Bei LaTeX: `\quelle{Eigene Darstellung.}` (Makro in `main.tex`, innerhalb des Floats direkt nach Bild/Tabelle) — nicht manuell mit `\footnotesize` nachbauen.
- Eigene Abb./Tab. immer mit „Quelle: Eigene Darstellung." (oder einer der Varianten oben). Kein `\cite{}` auf eigene Werke.

## Akronyme

`\ac{KÜRZEL}` im Text; Definition in `pages/acronyms.tex` per `\acro{KÜRZEL}{Langform}` (acronym-Paket, alphabetisch). Nur tatsächlich verwendete, nicht allgemein geläufige Abkürzungen aufnehmen — „z. B.", „u. a." usw. gehören **nicht** ins Verzeichnis. Keine Abkürzungen aus Bequemlichkeit im Text.

## LaTeX

lualatex, Arial 11, 1,5-zeilig, 2 cm Ränder, Blocksatz. Labels `sec:`/`fig:`/`tab:`/`eq:`. `\autoref{sec:label}` (mit `~` davor: `vgl.~\autoref{sec:label}`). `\enquote{}`. Float `[H]`, Caption vor `\label{}`. Tabellen `booktabs`, `\scriptsize` bei dichten Tabellen. **Kapitelstruktur (siehe auch Ordnerstruktur in `CLAUDE.md`):**
- Pro Hauptkapitel gibt es eine **Master-Datei** in `chapters/<kap>/<kap>.tex`, die mit `\section{...}\label{sec:<kap>}` (bzw. `\chapter{...}` je nach Dokumentklasse) beginnt und ihre Subsections per `\input{}` einbindet.
- **Subsection-Dateien** in `chapters/<kap>/<nn>_<slug>.tex` beginnen mit `\subsection{...}\label{sec:<slug>}` (kein Chapter-Wrapper).
- `pages/chapters.tex` bindet alle Hauptkapitel-Master per `\input{}` ein (nicht per `\include{}`).
- `\input{}` außerdem für Tabellen-Fragmente in `tables/`. Niemals `\include{}` für Subsection-Dateien (würde Seitenzwang und Header-Reset provozieren).
- Diagramme (statt Mermaid): als `tikzpicture` in der `.tex`-Datei — TikZ ist in `main.tex` geladen. **Vordefinierte Styles aus `main.tex` verwenden**: `\node[box]`, `\node[decision]`, `\draw[arr]`, `\draw[dashedarr]` — nicht pro Diagramm neu erfinden (einheitliches Layout, weniger Boilerplate). Zusätzliche Styles nur bei Bedarf lokal in der `tikzpicture`-Umgebung ergänzen. Pro Diagramm: Caption + `\label{fig:...}` darüber, `\quelle{Eigene Darstellung.}` darunter.
- Datendiagramme (Balken/Linien, z. B. Testergebnisse): `pgfplots` ist geladen — als `axis`-Umgebung in `tikzpicture`, nicht als externes Bild rendern.
- Listen: `enumitem` ist geladen — kompakte Aufzählungen per `\begin{itemize}[nosep]`.
- **Mechanische Formalia deterministisch prüfen statt lesen**: `python3 .claude/skills/_shared/scripts/check_formalia.py chapters/` (Pronomen, quote-Env, gerade Anführungszeichen, `\include`, `[H]`, Caption-Reihenfolge, `\underline`, `~\autoref`, Gedankenstrich-Häufung, Blockzitat > 40 Wörter, ½-Seiten-Heuristik, Überschriften-Dopplung, Satzlängen-Heuristik > 30 Wörter, Meta-Verben-/Nominalstil-Marker).

Abbildungen liegen in `images/<kapitel>/`, referenziert per `\includegraphics{images/<kapitel>/<datei>}` — Dateien selbst nie in `chapters/` ablegen.

**Nie ändern**: `main.tex`, `pages/cover.tex`. Projektspezifische Angaben (Titel, Papiertyp, Modul, Tutor:in, Abgabedatum, PDF-Schlagworte) stehen **ausschließlich in `pages/meta.tex`** — einmalig beim Projektstart ausfüllen. Nur `pages/meta.tex`, `pages/acronyms.tex`, `pages/appendix.tex`, `pages/chapters.tex` und `chapters/**` editieren. `references.bib` nie manuell editieren (Zotero/BBT-Auto-Export).

## Pronomen

„ich/wir/man" generell verboten (Ausnahme: Praxisreflexion). Forscherbezug ohne Pronomen: „Diese Arbeit zeigt …". Projektbericht: dritte Person streng.

## Struktur

½-Seiten-Regel pro Unterkapitel. Max. 2–3 Sätze zwischen Kapitel-Überschrift und erstem Unterkapitel. Keine wortgetreue Wiederholung der übergeordneten Überschrift in Unterpunkten; Kapitelüberschriften wiederholen nicht den Titel der Arbeit. Max. 3 Kapitelstufen. Inhaltsverzeichnis: nur 1. Ebene fett. Front-Matter: Titelblatt, Verzeichnisse, Literaturverzeichnis. **Mindestens 2 Unterpunkte:** Sobald ein Kapitel in Unterkapitel geteilt wird, müssen es mindestens zwei sein (kein einzelnes 1.1 ohne 1.2). Sonst nicht unterteilen.

**Roter Faden** (gilt für Schreib- und Prüf-Modus, kapitelübergreifend):
- **Kernbegriffs-Konsistenz**: Die tragenden Begriffe aus Leitfrage und These in identischer Formulierung durch alle Kapitel führen — keine Synonym-Variation bei Kernbegriffen (nicht „strukturiertes Feedback" in der Leitfrage und „kuratiertes Feedback" im Fazit). Fazit und Zwischenfazits beantworten die Leitfrage wörtlich in deren eigenen Begriffen.
- **Eingeführte Dimensionen nicht stillschweigend fallen lassen**: Wer n Kriterien/Kategorien einführt, verfolgt alle n bis zum Ende — oder begründet an der Stelle, an der eine aus der Argumentation verschwindet, in einem Halbsatz, wo sie aufgeht (z. B. „das vierte Kriterium kehrt im Konzept als Zielgruppenzuschnitt wieder").
- **Vorverweise dosieren**: Rück- und Vorverweise sind erwünschte Leserführung, aber nicht jedes Unterkapitel muss mit einem Vorverweis enden. Ein Vorverweis unmittelbar vor der Überschrift, die dasselbe ankündigt, ist redundant und entfällt. Herleitungs-Angaben (woraus sich Kriterien/Thesen ableiten) müssen zwischen Einleitung und Hauptteil übereinstimmen.

## Front-/Backmatter, Anhang, Umfang (IU-Richtlinien)

- **Abbildungsverzeichnis erst ab drei Abbildungen**, Tabellenverzeichnis erst ab drei Tabellen — darunter das jeweilige `\listof…` in `main.tex` auskommentiert lassen (Hinweis an den Nutzer, nicht selbst ändern).
- **Anhänge**: fortlaufend „Anhang A", „Anhang B" …; im Text mindestens ein Verweis pro Anhang („siehe Anhang A"); bei mehreren Anhängen ein Anhangsverzeichnis unmittelbar vor dem Anhang; arabische Seitenzahlen laufen durch den Anhang weiter.
- **Seitenumfang**: zählt ab „1 Einleitung" inkl. Abbildungen/Tabellen im Text; Titelblatt, Verzeichnisse, Literaturverzeichnis und Anhang zählen nicht. Vorgabe je Prüfungsleitfaden (Textteil B.Sc. meist 7–10 S., M.Sc. 12–15 S.); Nicht-Erfüllung kann Punktabzug bedeuten.
- **Keine Unterstreichungen**; Hervorhebungen sparsam kursiv oder fett.
- Interviews (falls vorhanden): wörtlich transkribieren (Transkriptionsregeln in den IU-Richtlinien Anhang F), Transkript in den Anhang.

## Schreibstil (Anti-KI-Muster)

Einzige Vollversion (Kurzerinnerung in `schreib-modus/SKILL.md` verweist hierher). Akademischer Text, der wie ein Erstsemester-KI-Aufsatz klingt, fällt Betreuenden auf und schadet der Glaubwürdigkeit. Deshalb explizit vermeiden:

- **Kein Gedankenstrich als Satzfüller** — nicht „Die Studie zeigt X — ein zentraler Befund." Stattdessen Komma, Semikolon oder Satz umstrukturieren.
- **Keine Floskel-Öffner**: „Es ist wichtig zu beachten, dass…", „Es lässt sich festhalten, dass…", „Zusammenfassend lässt sich sagen…" — direkt die Aussage schreiben, ohne Ankündigung.
- **Keine Klischee-Übergänge**: „Darüber hinaus", „Zudem", „Des Weiteren" als Standardverbindung zwischen praktisch jedem Absatz. Stattdessen inhaltliche Übergänge, die den logischen Bezug zeigen (kausal, konzessiv, kontrastiv — je nachdem, was tatsächlich gemeint ist).
- **Keine Absicherungsfloskeln** ohne Funktion: „könnte möglicherweise darauf hindeuten" statt einer klaren, durch Belege gedeckten Aussage. Unsicherheit nur dort markieren, wo sie inhaltlich begründet ist (z. B. bei Limitationen).
- **Aktiv statt passiv**, wo es ohne Bedeutungsverlust geht — „Diese Arbeit argumentiert…" statt „Es wird argumentiert…".
- **Kurze, klare Sätze bevorzugen** — verschachtelte Schachtelsätze mit mehreren Nebensätzen sind kein Zeichen wissenschaftlicher Tiefe.
- **Keine abstrakten Setup-Sätze als Absatz-/Kapiteleinstieg**: nicht „X galt lange als … Diese Voraussetzung hat sich verschoben." oder ähnliche These-zuerst-Konstruktionen, die eine große abstrakte Behauptung aufstellen, um sie im nächsten Satz zu kippen. Stattdessen mit einer konkreten, nachvollziehbaren Beobachtung einsteigen; Studie/Beleg folgt danach als Untermauerung, nicht als Eröffnung selbst.
- **Kontrastfiguren auch in Tarnform vermeiden**: Das Verbot rhetorischer Kontrastfiguren („nicht X, sondern Y" als Pointe) gilt genauso für ihre Ersatzformen — die zweisätzige Aufspaltung („Das Modell ist kein nachgelagertes Detail. Es ist die strukturelle Bedingung …") und „statt"-Wendungen („X statt Y") als Dauer-Argumentationsmuster. Sachliche Abgrenzungen bleiben erlaubt; Faustregel: höchstens eine ausgeprägte Kontrastkonstruktion pro Seite.
- **Doppelpunkt-Ankündigungen sparsam**: „Daraus folgt:", „Die Projektgruppe schließt daraus:", „X hat gezeigt:" höchstens vereinzelt (~1 pro Unterkapitel) — sonst als normalen dass-Satz oder die Aussage direkt schreiben. Doppelpunkte für Begriffsdefinitionen und vor Aufzählungen sind davon unberührt.
- **Keine Pointen-Schlusssätze**: Absätze nicht mit einem verdichteten Merksatz oder Aphorismus enden lassen („Der bewusste Verzicht auf Breite ist damit die Voraussetzung des Konzepts."). Sagt der Absatz die Sache schon, den Schlusssatz streichen.
- **Satzrhythmus variieren**: Keine Staccato-Ketten aus drei und mehr kurzen Hauptsätzen in Folge, besonders nicht mit gleichem Subjekt bzw. Pronomen-Anapher („Sie … Sie … Sie …"). Kurze Sätze mit mittellangen mischen — die Kurz-Satz-Regel ist eine Obergrenze, kein Zielrhythmus.
- **Signalwort-Wiederholung prüfen**: Betonungswörter wie „bewusst", „genau", „gezielt", „belastbar" pro Kapitel höchstens ein- bis zweimal; meist sind sie ersatzlos streichbar.
- **Zentrale Sätze nicht wörtlich wiederholen**: Fazit und Reflexion paraphrasieren Kernaussagen früherer Kapitel mit eigenen Worten, statt sie nahezu wortgleich zu übernehmen.

**Gendersensible Sprache:** Generisches Maskulinum ist an der IU zulässig; eine Gender-Pflicht besteht studiengangabhängig (Rücksprache mit Lehrkraft). Optional kann vor dem Hauptteil ein Gender-Disclaimer (Vorlage in den IU-Richtlinien Anhang A) auf einer separaten Seite eingebunden werden.

## Verständlichkeit (einfache Sprache — hat bei Zielkonflikten Vorrang vor „akademischem Klang")

Maßstab sind von Prüfenden gut bewertete Beispielarbeiten — destilliert in **`_shared/stilprofil.md`** (Positiv-/Negativ-Beispiele mit Originalsätzen; beim Schreiben und Prüfen zusammen mit diesem Abschnitt laden statt der PDF-Originale in `../beispieldokumente/`). Ihr gemeinsamer Nenner: **einfache, klare Sprache, die auch ein interessierter Laie beim ersten Lesen versteht** — nicht maximale akademische Dichte. Konkret:

- **Selbsttest pro Absatz**: Könnte ein Studienanfänger ohne Fachhintergrund den Absatz nach einmaligem Lesen mit eigenen Worten wiedergeben? Wenn nein: vereinfachen.
- **Ein Gedanke pro Satz.** Hauptaussage in den Hauptsatz, höchstens ein Nebensatz. Lieber zwei kurze Sätze als ein eleganter langer.
- **Verben statt Nominalstil**: „Die Arbeit untersucht X" statt „Die Untersuchung von X erfolgt". Kapitel- und Vorgehensbeschreibungen mit einfachen Verben („Kapitel 3 beschreibt/zeigt/fasst zusammen"), nicht mit gestelzten Meta-Verben („entfaltet", „bündelt", „verortet", „adressiert").
- **Das alltagsnahe Wort wählen, wenn es dasselbe sagt**: „nutzen" statt „heranziehen", „zeigt sich" statt „manifestiert sich", „wichtig" statt „von zentraler Bedeutung". Präzision geht immer vor — aber gewählt klingende Synonyme ohne inhaltlichen Mehrwert kosten Verständlichkeit und bringen nichts.
- **Fachwörter: benutzen UND erklären.** Fachbegriffe sind erwünscht und zeigen Fachkompetenz — bei der ersten Nennung aber in einem Halbsatz oder einer Klammer allgemeinverständlich erklären (z. B. „organisationales Commitment, also die Bindung der Mitarbeitenden an das Unternehmen, …"). Danach den Begriff konsistent weiterverwenden, nicht erneut erklären.
- **Konkret statt abstrakt**: Beispiele, Zahlen und greifbare Situationen einbauen, wo sie die Aussage tragen — die gut bewerteten Arbeiten veranschaulichen Konzepte regelmäßig an konkreten Fällen.
- **Leser führen ist erlaubt und erwünscht**: Einfache Zweck- und Übergangssätze („Um dieses Ziel zu erreichen, …", „Dazu gehört …", „Im nächsten Schritt wird …") sind gute Wegweiser. Die Floskel-Regel oben verbietet nur *inhaltsleere* Ankündigungen („Es ist wichtig zu beachten, dass …" ohne Aussage) — nicht Sätze, die dem Leser Orientierung geben.
- **Keine stilistische Verdichtung**: keine elliptischen Pointen-Sätze („Der Bedarf ist damit kein hypothetischer, sondern ein aktuell dokumentierter."), keine rhetorisch aufgeladenen Appositionen oder Kontrastfiguren. Solche Sätze klingen nach KI-Aufsatz und sind schwerer zu lesen, ohne mehr auszusagen.

## Lesbarkeitsregel (Zitation)

Bezieht sich der gesamte Absatz auf dieselbe Quelle, genügt eine Quellenangabe im ersten Satz; im neuen Absatz erneut zitieren. „Doppelt zitieren" nur, wenn tatsächlich auf unterschiedliche Stellen verwiesen wird.
