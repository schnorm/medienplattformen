# Zitations-Sonderfälle (Referenz)

Ausgelagert aus `hard-rules-formal.md`. Dort stehen die Regeln, die **jede** Schreib- und Prüf-Session braucht; hier die Fälle, die selten auftreten, dann aber genau nachgeschlagen werden müssen. **Laden, sobald einer dieser Fälle konkret ansteht** – nicht pauschal beim Sessionstart. Quelle: IU-Zitierleitfaden (01.10.2025), Kapitel 2.2.2–2.4.

## Der richtige Zitierbefehl – Klammern kommen vom Befehl, nicht von Hand

Am gesetzten Dokument geprüft (biblatex, `style=apa`):

| Befehl | Ausgabe | wofür |
|---|---|---|
| `\parencite[S. 225]{key}` | `(Mindermann et al., 2021, S. 225)` | Normalfall am Satzende |
| `\textcite[S. 225]{key}` | `Mindermann et al. (2021, S. 225)` | narrativ, wenn die Autorenschaft Thema des Satzes ist |
| `\cite[S. 225]{key}` | `Mindermann et al., 2021, S. 225` | **ohne Klammern** – für Stellen, die ihre Klammer schon haben |
| `\citeauthor{key}, \citeyear{key}` | `Mindermann et al., 2021` | dasselbe, wenn die Seitenzahl separat gesetzt wird |

Die letzten beiden Formen sind kein Stilmittel, sondern notwendig: In einem Sekundärzitat und in einer Abbildungs-Quellenzeile steht der Kurzbeleg **innerhalb** einer bereits gesetzten Klammer beziehungsweise ganz ohne Klammer. Ein `\parencite` erzeugt dort eine zweite, verschachtelte Klammer.

## Sekundärzitate

Vermeiden; nur zulässig, wenn die Primärquelle nicht beschaffbar ist. Im Text wird die **Primärquelle** genannt, dahinter mit „zitiert nach" die tatsächlich gelesene Sekundärquelle. Nur die Sekundärquelle steht im Literaturverzeichnis.

```latex
(Middendorff et al., 2017, zitiert nach \cite[S.~225]{mindermann2021})
```

→ `(Middendorff et al., 2017, zitiert nach Mindermann et al., 2021, S. 225)`

Niemals zwei `\parencite{}` kombinieren und **nicht** `\parencite` für die Sekundärquelle verwenden – das ergibt eine Klammer in der Klammer.

## Persönliche Kommunikation

Nur im Text, nicht in `references.bib`. Pflichtangaben: vollständiger Name der Person oder Institution, Kennzeichnung „persönliche Kommunikation", **genaues Datum**. Zusätzlich muss im Text erkennbar sein, um welche Art von Kommunikation es sich handelt (E-Mail, interner Bericht, Gespräch). Wenn möglich im Anhang dokumentieren und darauf verweisen; ist das wegen des Umfangs nicht möglich, müssen die Dokumente auf Anfrage vorgelegt werden können.

> „Die touristischen Betriebe … sind vor allem kleine und mittelständische Unternehmen" (P. Müller, persönliche Kommunikation, 20.02.2018).

**Nicht darunter fallen** Bücher und Fachartikel hinter einer Bezahlschranke – die gelten als öffentlich zugänglich, weil sie über Bibliotheken beschaffbar sind.

## Eigene Erhebungsdaten ≠ persönliche Kommunikation

Relevant vor allem bei der empirischen Seminararbeit. Systematisch erhobene Interviews sind wissenschaftliche Daten. Sie werden mit Teilnehmerkürzel und Fundstelle im Text zitiert und stehen **nicht** im Literaturverzeichnis. Beide Fundstellen-Systeme sind zulässig (Zitierleitfaden S. 17):

- **Zeitmarken** (Transkription nach Dresing & Pehl, IU-Richtlinien Anhang F): `(Experte A, Interview A3, #00:38:23-1#)`
- **Zeilennummern** (durchnummeriertes Transkript): `(B3, Interview, Z. 45–46)`

Das Methodik-Kapitel muss transparent nennen: verwendetes Transkriptionssystem, Bezeichnungsschema der Befragten (B1, B2 … oder „Experte A") und wie die Fundstellen auffindbar sind. Klarnamen nur mit **gesondert eingeholter** Zustimmung; ohne sie ein anonymisierter Name.

## Quellen ohne Seitenzahlen

Websites, EPUBs, Vorab-Onlinepublikationen: per Kapitel, Absatz oder Abschnittsname zitieren – Hauptsache, das Merkmal ändert sich nicht und macht die Stelle auffindbar.

- `(Müller, 2017, Kap. 2.1)` · `(Müller, 2017, Kap. 2.1, Abs. 4)`
- `(IU Internationale Hochschule, 2025, Abschnitt „Lange direkte Zitate")`
- Multimedia mit Zeitstempel (z. B. „2:13")

**EPUBs werden mitgeprüft.** Liegt im `file`-Feld des Bib-Eintrags eine `.epub`-Datei, löst `check_quellentreue.py` den `[Kap. X]`-Locator gegen das Inhaltsverzeichnis des E-Books auf und vergleicht die Aussage mit genau diesem Kapitel – wie sonst mit einer PDF-Seite. Hierarchische Nummern (`Kap. 17.2.2`) funktionieren; löst das Verzeichnis die Unterebene nicht auf, fällt die Prüfung auf die nächsthöhere Ebene und zuletzt auf das ganze Buch zurück und weist die Stelle als maschinell unbestätigt aus. Zum Nachlesen beim Schreiben: `check_quellentreue.py --seite <bibkey> 17.2.2`.

## Mehrdeutigkeit auflösen

- Mehrere Werke derselben Autorenschaft im selben Jahr → Suffix a, b, c (bei unbekanntem Jahr „n.d.-a"); die Zuordnung folgt der Reihenfolge im Literaturverzeichnis.
- Gleiche Nachnamen verschiedener Personen → abgekürzter Vorname („A. Klein, 2014"). Mehrere gleichnamige Autor:innen **am selben Werk** brauchen das nicht.
- Gleiche zwei Erstautoren im selben Jahr → so viele Autoren nennen, wie zur Unterscheidung nötig; der Rest ab dem fünften mit „et al.".
- Nachnamen mit „von", „van", „de": An der IU dürfen sie als Bestandteil des Familiennamens behandelt werden (auch für die alphabetische Sortierung). Groß-/Kleinschreibung wie in der Quelle, außer am Satzanfang.

## Institution als Autor:in

Kein persönlicher Autor auffindbar → Institution laut Impressum beziehungsweise Website-Name. Abkürzung beim **ersten** Zitat in eckigen Klammern, danach nur noch die Abkürzung; im Literaturverzeichnis immer ausgeschrieben.

> Erstzitat: `(United Nations World Tourism Organization [UNWTO], 2017)` · weitere: `(UNWTO, 2017)`

**Nicht von Hand einführen** – das erledigt biblatex-apa: Zotero-Feld *Extra* → `tex.shortauthor: UNWTO`. Ein zusätzlich in den Fließtext geschriebener Einführungssatz erzeugt die Abkürzung doppelt.

## Internetquellen

Kurzbeleg wie bei Büchern; Titel und URL nie in den Fließtext. **Kein Abrufdatum** (explizite IU-Abweichung von APA). Allgemeiner Hinweis auf eine Website ohne konkreten Inhalt → gar kein Quellenverweis, sondern Name im Text und URL in Klammern („… mithilfe des Umfragetools von Unipark (www.unipark.de)"). Mehrere Unterseiten derselben Site → getrennte Einträge (n.d.-a, n.d.-b). Statista/Destatis: die dort hinterlegte **Originalquelle** als Autor:in angeben.

## Direktzitat-Details

- Buchstäbliche Genauigkeit. Fehler im Original mit `[sic]` **nach** dem Fehler kennzeichnen.
- Der erste Buchstabe darf groß oder klein gesetzt und die Zeichensetzung am Zitatende angepasst werden – das ist keine Abweichung.
- Auslassung eines oder mehrerer Wörter mit drei Punkten; **nicht** nötig, wenn das Zitat mitten im Satz beginnt oder endet.
- Eigene Ergänzungen in eckige Klammern.
- Weggelassene Hervorhebungen des Originals mit „[Hervorhebung weggelassen]", eigene mit „[Hervorhebung d. Verf.]" direkt dahinter.
- Muss aus Satzbaugründen ein Buchstabe entfallen, steht er in eckigen Klammern: „prozessorientierte[n] Ausrichtung".
- Zitat im Zitat mit einfachen Anführungszeichen (`\enquote{… \enquote{…} …}` erzeugt das automatisch).
- Fremdsprachige wörtliche Zitate im Original übernehmen und in der Fußnote übersetzen; **englische Zitate müssen nicht übersetzt werden**.
- Keine dekorativen Zitate und keine Zitate, die sich keiner Textstelle zuordnen lassen.

`check_quellentreue.py` toleriert Klammer-Einschübe und Auslassungspunkte beim Wortlautvergleich – ein regelkonform bearbeitetes Zitat erzeugt keinen Befund.

## Gesetze, Urteile, Normen

- **Gesetze**: nur im Text, nie im Literaturverzeichnis. Zuerst Paragraf, dann Absatz, ggf. Satz, zuletzt die Gesetzes-Abkürzung – eine Schreibweise wählen und durchhalten: „§ 48 Absatz 1 HGB" · „§ 48 Abs. 1 HGB" · „§ 48 I HGB". Auf die aktuelle Fassung braucht es kein Datum; für eine ältere „§ 127 AktG idF v. 1937". Verwendete Abkürzungen ins Abkürzungsverzeichnis.
- **Gerichtsentscheidungen**: ebenfalls nur im Text, in Klammern, mit Gericht, Verkündungsdatum, Aktenzeichen und **einer** Fundstelle: `(BAG, 20.10.2015, 9 AZR 224/14, NZA, 2016, S. 159)` bzw. aus einer Datenbank `(OVG Berlin-Brandenburg, 19.12.2018, 3 S 98/18, BeckRS 2018, 33732 Rn. 10)`.
- **Kommentare und juristische Lehrbücher** dagegen ganz normal nach APA, mit Verzeichnis-Eintrag; bei Loseblatt- und Online-Kommentaren statt des Jahres den Stand angeben.
- **Normen (ISO/DIN)**: mit Literaturverzeichnis-Eintrag, Standard-Nummer in Klammern hinter dem Titel.

## Software, Tools und Spiele (Zitierleitfaden 2.3.9)

Für einen Projektbericht über ein selbst gebautes Artefakt und für jede Arbeit, die ein Werkzeug untersucht, ist das der praktisch wichtigste Sonderfall – dort der Regelfall, nicht die Ausnahme:

- **Ins Literaturverzeichnis**, wenn die Software in der Arbeit **untersucht** wird oder daraus zitiert wird – ebenso, wenn im Text wenig bekannte Software genannt wird.
- **Nicht** ins Verzeichnis: übliche, weit verbreitete Software, die nur erwähnt wird (Word, Excel, Zotero, VS Code als Arbeitsmittel).
- Format: `Entwickler:in oder Studio. (Jahr der verwendeten Version). Titel (Version) [Art der Software oder Plattform]. Produktionsfirma oder App Store. URL`
  > Corporation for Digital Scholarship. (2024). Zotero (Version 7.0.11) [Computer Software, Windows]. https://…
- Physische Spiele wie Monografien, mit Art des Spiels nach dem Titel.

## Übersetzte Werke

Übersetzer:in im Literaturverzeichnis nennen, dazu „(Original veröffentlicht JJJJ)". Im Kurzbeleg steht **nur das Jahr der verwendeten Ausgabe** – die APA-Doppelform „(Frankfurt, 2006/2024, S. 5)" ist an der IU ausdrücklich nicht vorgesehen.

## Eigene frühere Prüfungsleistungen

Grundsätzlich nicht zitierwürdig. Ausnahme: **eigene empirische Ergebnisse** daraus, zitierbar mit dem Zusatz „[unveröffentlichte Arbeit]. IU Internationale Hochschule." Das ist zugleich die praktische Seite der Eigenplagiat-Regel (`hard-rules-formal.md` → Zitationen): Bei vielen kleinen Arbeiten im selben Studiengang ist die unbelegte Wiederverwendung eigener Vorarbeit der wahrscheinlichste Plagiatsfall überhaupt – im Zweifel die eigene Arbeit regulär zitieren.

## KI-Ausgaben

Drei Nutzungsarten, drei verschiedene Antworten (Zitierleitfaden 2.2.1):

- **Als Hilfsmittel** (Übersetzen, Umformulieren, Strukturieren): weder zitierpflichtig noch zitierfähig – es wird nichts aus einer Quelle übernommen. **Ausnahme Bilder**: KI-erzeugte Abbildungen brauchen den Quellenhinweis (`hard-rules-formal.md` → Eigene Werke / Abbildungskonvention).
- **Als Informationsquelle**: nicht zitierfähig. KI-Tools sind keine natürlichen Personen, die Herkunft der Information ist nicht nachvollziehbar, und es sind nie Originalveröffentlichungen. Inhalt am Original verifizieren und **die Originalquelle** zitieren.
- **Als Untersuchungsgegenstand**: zitierfähig. Autor ist das Softwareunternehmen, nicht die KI („OpenAI. (2025). ChatGPT (Version …) [Large Language Model]"). Die untersuchten KI-Outputs gehören dokumentiert in den Anhang.
