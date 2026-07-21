# Stilprofil — Kalibrierung an gut bewerteten Arbeiten

Destillat aus den von Prüfenden gut bewerteten Beispielarbeiten (`beispieldokumente/` im übergeordneten Vorlagen-Ordner; dieses Profil ersetzt die PDF-Lektüre und funktioniert auch, wenn der Projektordner einzeln kopiert wurde). Wird von `schreib-modus` und `pruef-modus` zusammen mit `hard-rules-formal.md` → Verständlichkeit genutzt. Alle Positiv-Beispiele stammen wörtlich aus real gut bewerteten Arbeiten, alle Negativ-Beispiele aus einer real schlechter bewerteten.

## Der Zielklang in einem Satz

Schreibe wie ein kompetenter Studierender, der einem interessierten Laien etwas erklärt — nicht wie ein Fachjournal, das Dichte demonstrieren will.

## So klingen die gut bewerteten Arbeiten (Positiv-Muster)

**Fachwort einführen und sofort erklären:**
> „Der Begriff Organizational Commitment beschreibt, wie stark Mitarbeitende an ihr Unternehmen gebunden sind."
> „Continuance Commitment liegt vor, wenn Mitarbeitende bleiben, weil sie glauben, bleiben zu müssen."

Muster: `<Fachbegriff> beschreibt/bezeichnet/liegt vor, wenn <Alltagssprache>`. Danach wird der Begriff konsistent weiterverwendet, ohne erneute Erklärung.

**Einfache Hauptsätze, ein Gedanke pro Satz:**
> „Motivation beschreibt die Energie, die Mitarbeitende aufbringen, um Leistung zu erbringen."
> „Dennoch sieht sich TRESOLITE einer Herausforderung gegenüber: Die Fluktuationsrate ist hoch, während gleichzeitig viele neue Stellen besetzt werden müssen."

**Leser aktiv führen (Zweck- und Übergangssätze sind erwünscht):**
> „Um dieses Ziel zu erreichen, ist es wichtig, sich auf diese Herausforderung vorzubereiten und ein Verständnis dafür zu entwickeln."
> „Um die hohe Fluktuation bei TRESOLITE zu verstehen, ist es nötig zu untersuchen, welche Faktoren das Commitment der Mitarbeitenden beeinflussen."

**Konkrete Beispiele statt Abstraktion:**
> „Dennoch passt sich McDonald's auch lokalen Gewohnheiten und Geschmäckern an, zum Beispiel Eiscreme mit Mungobohnengeschmack in China."

## So klingt der abgestrafte KI-Akademikerstil (Negativ-Muster — vermeiden)

**Gestelzte Meta-Verben für Kapitel und Vorgehen:**
> ✗ „Kapitel 3 entfaltet daraus das Plattformkonzept …" · ✗ „Kapitel 5 bündelt die Ergebnisse …" · ✗ „Ihr Modell verortet die Unwägbarkeiten kreativer Arbeit …"
> ✓ „Kapitel 3 beschreibt das Plattformkonzept …" · ✓ „Kapitel 5 fasst die Ergebnisse zusammen …"

**Elliptische Pointen und rhetorische Kontrastfiguren:**
> ✗ „Der Bedarf an einer Alternative ist damit kein hypothetischer, sondern ein aktuell dokumentierter."
> ✓ „Der Bedarf an einer Alternative ist also real und durch aktuelle Studien belegt."

**Verdichteter Nominalstil, mehrere Gedanken pro Satz:**
> ✗ „Ein abschließender Iterationsschritt setzt den Entwurf einer angenommenen Nutzerperspektive aus; da der Projektrahmen keine reale Testgruppe zuließ, ist dieser Schritt als Gedankenexperiment angelegt und als solches gekennzeichnet."
> ✓ „Im letzten Schritt prüft die Projektgruppe den Entwurf aus Sicht möglicher Nutzer. Eine echte Testgruppe war im Projektrahmen nicht möglich. Dieser Schritt ist deshalb ein Gedankenexperiment und wird auch so gekennzeichnet."

**Fachbegriffe ohne Erklärung aneinanderreihen:**
> ✗ „… die Spannung zwischen Reichweite und fachlichem Nutzen, deren Sichtbarkeit strukturell unsicher ist …"
> ✓ Jeder Fachbegriff bekommt bei der ersten Nennung einen erklärenden Halbsatz oder eine Klammer.

**Kontrastfigur in Tarnform (zweisätzig aufgespalten oder als „statt"-Dauermuster):**
> ✗ „Das Finanzierungsmodell ist kein nachgelagertes Detail. Es ist die strukturelle Bedingung dafür, dass …"
> ✓ „Das Finanzierungsmodell entscheidet darüber, ob die übrigen Funktionen ihr Versprechen halten können."

**Pointen-Schlusssatz am Absatzende:**
> ✗ „Der bewusste Verzicht auf Breite ist damit die Voraussetzung des Konzepts." (nach einem Absatz, der genau das schon gesagt hat)
> ✓ Schlusssatz streichen — der Absatz trägt die Aussage bereits.

**Staccato-Kette kurzer Sätze mit Pronomen-Anapher:**
> ✗ „Diese Beobachtung bezieht sich auf die untersuchte Stichprobe. Sie erlaubt keine Verallgemeinerung. Sie liefert aber einen Ansatzpunkt."
> ✓ „Diese Beobachtung gilt nur für die untersuchte Stichprobe und lässt sich nicht verallgemeinern; als Ansatzpunkt für das Konzept reicht sie aber aus."

## Menschliche Textur (Positiv-Muster)

Die Verbotsregeln in `hard-rules-formal.md` entfernen KI-Marker — menschlich klingt ein Text aber erst durch das, was er *tut*, nicht nur durch das, was er unterlässt:

**Narrative Zitate mischen (nicht jede Quelle in Klammern ans Satzende):**
> ✗ „Es werden drei Komponenten des Commitments unterschieden (Meyer & Allen, 1991, S. 67). Die emotionale Komponente hat den stärksten Effekt (Meyer et al., 2002, S. 33). Das Modell wurde vielfach kritisiert (Solinger et al., 2008, S. 71)."
> ✓ „Meyer und Allen (1991, S. 67) unterscheiden drei Komponenten des Commitments. Eine Metaanalyse bestätigte später, dass die emotionale Komponente den stärksten Effekt hat (Meyer et al., 2002, S. 33). Solinger et al. (2008, S. 71) halten das Modell dagegen für empirisch nicht haltbar."

LaTeX: narrative Form mit `\textcite[S. 67]{key}`, Klammer-Form mit `\parencite`. Kein festes Verhältnis — narrativ immer dann, wenn die Autorenposition selbst Thema des Satzes ist.

**Abwägung endet mit Urteil, nicht mit Symmetrie:**
> ✗ „Einerseits bietet das Modell eine klare Struktur. Andererseits ist seine empirische Basis umstritten. Beide Perspektiven haben ihre Berechtigung."
> ✓ „Das Modell bietet eine klare Struktur, seine empirische Basis ist jedoch umstritten. Für diese Arbeit überwiegt der strukturelle Nutzen: Die Kritik von Solinger et al. (2008) betrifft die Trennschärfe der Komponenten, nicht ihre Existenz — und nur Letztere wird hier vorausgesetzt."

**Dosierte Natürlichkeit** (sparsam — ein Element alle paar Absätze): ein Klammer-Einschub mit Beispiel oder Kurzerklärung, Konnektoren-Vielfalt („allerdings", „dabei", „immerhin" statt durchgehend „jedoch"/„zudem"), gelegentlich eine nachgeschobene Präzisierung („genauer gesagt: nur für Befragte unter zwei Jahren Betriebszugehörigkeit").

**Keine rhetorischen Fragen** als Einstieg oder Übergang („Doch was folgt daraus?") — die wörtlich formulierte Leitfrage ist die einzige legitime Frage im Text.

## Absatzbau — wie ein guter wissenschaftlicher Absatz aussieht

**Richtwert: 4–7 Sätze pro Absatz — als Rahmen, nicht als Raster.** Unter 3 Sätzen ist es meist kein eigenständiger Gedanke (mit dem Vorgänger-Absatz zusammenlegen), über 8 Sätzen verliert der Leser den roten Faden (aufteilen). Ausnahme: kurze Übergangs- oder Einleitungsabsätze (2–3 Sätze sind dort in Ordnung). **Wichtig: Die Längen innerhalb des Rahmens streuen** — ein Text, in dem jeder Absatz exakt fünf Sätze hat, wirkt maschinell gleichförmig, selbst wenn jeder einzelne Absatz gut gebaut ist. Ein kurzer Absatz nach zwei langen ist ein Rhythmuswechsel, kein Fehler.

### Grundmuster: Claim → Beleg → Erklärung → Einordnung

> Organizational Commitment beschreibt die emotionale, kalkulierte oder normative Bindung von Mitarbeitenden an ihr Unternehmen (Meyer & Allen, 1991, S. 67). In einer Metaanalyse über 155 Studien zeigte sich, dass vor allem die emotionale Komponente mit geringerer Fluktuationsabsicht zusammenhängt (Meyer et al., 2002, S. 33). Das bedeutet: Mitarbeitende, die sich ihrem Unternehmen emotional verbunden fühlen, denken seltener über einen Wechsel nach — selbst wenn bessere Angebote vorliegen. Für TRESOLITE ist dieser Befund relevant, weil die aktuelle Fluktuation vor allem Mitarbeitende betrifft, die weniger als zwei Jahre im Unternehmen sind und möglicherweise noch keine emotionale Bindung aufbauen konnten.

**Was diesen Absatz gut macht:**
- Erster Satz = Hauptaussage (Claim) mit Begriffserklärung
- Zweiter Satz = konkreter Beleg mit Quellenangabe
- Dritter Satz = Erklärung in eigenen Worten (kein Nachzitieren, sondern Interpretation)
- Vierter Satz = Einordnung in den konkreten Fall / die Leitfrage (Brücke zum nächsten Absatz)

### Variante: Beobachtung → Erklärung → Einschränkung

> Die Fluktuationsrate bei TRESOLITE liegt mit 23 % deutlich über dem Branchendurchschnitt von 15 % (Bundesagentur für Arbeit, 2023, S. 12). Ein möglicher Erklärungsfaktor ist die fehlende strukturierte Einarbeitung: Neue Mitarbeitende durchlaufen kein standardisiertes Onboarding, sondern werden direkt in laufende Projekte eingebunden. Allerdings kann die Fluktuation nicht allein auf das Onboarding zurückgeführt werden, da auch die Vergütungsstruktur und die Standortlage eine Rolle spielen. Diese weiteren Faktoren werden in Abschnitt 3.2 untersucht.

**Was diesen Absatz gut macht:**
- Startet mit einer konkreten, belegten Beobachtung (Zahl + Quelle)
- Bietet eine Erklärung, ohne sie als einzige Ursache darzustellen
- Benennt die Einschränkung ehrlich (keine Überinterpretation)
- Leitet zum nächsten Abschnitt über (Leserführung)

### Was NICHT gut funktioniert (Negativ-Beispiel ganzer Absatz)

> ✗ „Organizational Commitment ist ein vielschichtiges Konstrukt, das in der wissenschaftlichen Literatur intensiv diskutiert wird. Es umfasst verschiedene Dimensionen und hat weitreichende Implikationen für das Personalmanagement. Darüber hinaus zeigt die Forschung, dass Commitment einen signifikanten Einfluss auf die Mitarbeiterbindung hat. Zusammenfassend lässt sich festhalten, dass Organizational Commitment ein zentraler Faktor für den Unternehmenserfolg ist."

**Was daran schlecht ist:** Vier Sätze, null Information. Kein konkreter Beleg, keine Erklärung, kein Bezug zum eigenen Fall. Jeder Satz könnte über jedes beliebige Konzept geschrieben worden sein — das ist der typische KI-Füllabsatz.

## Übergänge zwischen Absätzen

Klischee-Übergänge („Darüber hinaus", „Zudem", „Des Weiteren") sind verboten — sie zeigen keinen logischen Bezug. Stattdessen den tatsächlichen Zusammenhang benennen:

| Logischer Bezug | Muster | Beispiel |
|---|---|---|
| **Kausal** (Absatz B folgt aus A) | „Weil X gezeigt hat, dass …" / „Aus diesem Befund ergibt sich …" | „Weil emotionales Commitment die Fluktuation stärker beeinflusst als Gehalt, konzentriert sich die folgende Analyse auf die Bindungsfaktoren im Onboarding." |
| **Konzessiv** (B schränkt A ein) | „Obwohl X zutrifft, zeigt sich bei Y …" / „Trotz dieses Befunds …" | „Obwohl Meyer und Allen drei Komponenten unterscheiden, zeigt die neuere Forschung, dass die Grenzen zwischen affektivem und normativem Commitment fließend sind." |
| **Kontrastiv** (B widerspricht A) | „X kommt jedoch zu einem anderen Ergebnis …" / „Im Gegensatz dazu …" | „Solinger et al. (2008) kommen jedoch zu dem Ergebnis, dass das Drei-Komponenten-Modell empirisch nicht haltbar ist." |
| **Spezifizierend** (B vertieft A) | „Konkret bedeutet das …" / „Ein Beispiel dafür …" | „Konkret bedeutet das für TRESOLITE, dass die Einarbeitung in den ersten 90 Tagen entscheidend ist." |
| **Temporal/methodisch** (B folgt zeitlich/im Vorgehen) | „Im nächsten Schritt …" / „Nachdem X geklärt ist, …" | „Nachdem die theoretischen Grundlagen dargelegt sind, beschreibt der folgende Abschnitt das methodische Vorgehen." |

**Faustregel:** Der erste Satz eines neuen Absatzes sollte in 2–3 Wörtern zeigen, wie er sich zum vorherigen verhält — ohne dass der Leser zurückblättern muss.

## Schnellprüfung vor dem Speichern

1. Enthält jeder Absatz höchstens vereinzelt Sätze mit mehr als ~25 Wörtern?
2. Ist jeder Fachbegriff bei der ersten Nennung erklärt?
3. Kommen „entfaltet/bündelt/verortet/adressiert" oder ähnliche Meta-Verben vor? → ersetzen.
4. Würde ein Studienanfänger den Absatz nach einmaligem Lesen wiedergeben können?
5. Endet ein Absatz mit einem verdichteten Merksatz/Aphorismus? → streichen oder entpointen.
6. Mehr als eine Kontrastkonstruktion („nicht X, sondern Y" · „kein X. Es ist Y" · „X statt Y") pro Seite? → auflösen.
7. Häufen sich Doppelpunkt-Ankündigungen („Daraus folgt: …") oder Betonungswörter („bewusst", „genau", „gezielt", „belastbar")? → reduzieren.
8. Hängt jede Quelle als Klammer am Satzende? → an geeigneten Stellen auf narrative Zitation (`\textcite`) umstellen.
9. Mehr als eine Dreier-Aufzählung („X, Y und Z") pro Seite, ohne dass es sachlich genau drei Dinge sind? → auf zwei oder vier Glieder umbauen oder auflösen.
10. Haben fast alle Absätze dieselbe Satzzahl? → Längen streuen (kurzer Übergangsabsatz, ein längerer Analyseabsatz).
11. Rhetorische Frage außerhalb der wörtlichen Leitfrage? → als Aussagesatz umformulieren.
12. Endet eine Abwägung urteilslos („beide Perspektiven haben ihre Berechtigung")? → begründet gewichten.
