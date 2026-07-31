# Autoref-Check – tragen die Verweisziele ihre Sätze noch?

Stand: 31.07.2026 · 24 Verweispaare · OK 24 · offen 0

> Erzeugt von `check_autoref.py`. Der Bericht wird pro Lauf überschrieben; die Urteile liegen in `autoref-state.json`. Statuswerte nie von Hand ändern – Urteil per `--verdikt <hash>=OK --notiz "…"` eintragen.

> **`OK` heißt: beide Achsen geprüft.** Fundstelle (steht der Inhalt dort?) *und* Reichweite (trägt die Zielstelle ihn in dieser Stärke?). Trägt sie ihn nicht mehr, lautet das Urteil `RENTIERT NICHT` – der Befund bleibt dann stehen.

## Geprüft

| Hash | Verweis | Ziel | Notiz |
|---|---|---|---|
| `d2d0b27d74` | 01_wettbewerbsanalyse.tex:3 | `tab:wettbewerbsvergleich` | Abgabe-Audit 31.07.: Zielstelle tab:wettbewerbsvergleich fuehrt Chefkoch.de bei Kommunikation & Community mit 'stark' - Wertung und verweisender Satz decken sich exakt. |
| `1c30aefc2d` | 01_wettbewerbsanalyse.tex:13 | `tab:wettbewerbsvergleich` | Abgabe-Audit 31.07.: Methodensatz zur eigenen Sichtung bezieht sich auf dieselbe Tabelle; Quellenzeile der Tabelle nennt dieselben sechs Plattformen und denselben Zeitraum Juli 2026. |
| `e90465b871` | 02_zielgruppe.tex:3 | `sec:zielsetzung_und_verengung` | Abgabe-Audit 31.07.: 02_zielsetzung_und_verengung.tex:5 begruendet die Verengung auf die nachhaltigkeitsorientierte Teilgruppe ausdruecklich - Fundstelle und Reichweite gedeckt, keine Gewichtungszuschreibung. |
| `eee8b539f4` | 02_zielgruppe.tex:9 | `tab:persona` | Abgabe-Audit 31.07.: tab:persona liegt in Anhang A und enthaelt die Persona-Skizze Mara K. samt Merkmalen; am gebauten PDF (S. 18) verifiziert. |
| `28ae7e8f30` | 03_konzept.tex:7 | `sec:phasenplanung` | Abgabe-Audit 31.07.: tab:phasenplanung fuehrt Phase 4 'Beta-Test & Feedback' (Woche 15-17); Rezeptbestand steht als Inhalt der vorgelagerten MVP-Phase - Voraussetzungsverhaeltnis stimmt. |
| `39ac026c0f` | 03_konzept.tex:7 | `sec:wettbewerbsanalyse` | Abgabe-Audit 31.07.: Marker 'allein' geprueft - Wettbewerbsanalyse:7 weist Restegourmet und BMLEH-App beide das Reste-Matching zu (Tabelle: je 'stark'), traegt den Satz also in voller Staerke. |
| `96221e15c3` | 03_konzept.tex:11 | `sec:community_und_feedback` | Abgabe-Audit 31.07.: Marker 'vor allem' geprueft - 04:7 nennt die monatliche Zero-Waste-Woche mit Rangliste; der sichtbare Vergleich der Nutzer:innen steht dort. Die Gewichtung 'vor allem' ist eigene Designsetzung, keine Zuschreibung an die Zielstelle. |
| `8d46cfb075` | 03_konzept.tex:17 | `tab:funktionsuebersicht` | Abgabe-Audit 31.07.: tab:funktionsuebersicht traegt die Spalte 'Herleitung/Bezug' fuer alle sechs Funktionen - Ankuendigung eingeloest. |
| `fab60723ce` | 03_konzept.tex:19 | `sec:wettbewerbsanalyse` | Abgabe-Audit 31.07.: Zellbezug 'schliesst die Marktluecke aus sec:wettbewerbsanalyse' - die Luecke ist dort in :36 ausformuliert. |
| `960f28779d` | 03_konzept.tex:38 | `sec:community_und_feedback` | Abgabe-Audit 31.07.: Rettungs-Feed ist Gegenstand von 04_community_und_feedback.tex:3 - Fundstelle korrekt. |
| `20d176f271` | 03_konzept.tex:38 | `fig:styletile` | Abgabe-Audit 31.07.: fig:styletile liegt in Anhang B; Bild per Read geprueft - Farbwelt, Typografie (Lora/Work Sans) und wiederkehrende Bedienelemente sind darauf abgebildet. |
| `74e4777ac0` | 03_konzept.tex:38 | `fig:mockup_start` | Abgabe-Audit 31.07.: fig:mockup_start am Bild geprueft - Reste-Eingabefeld mit Chip-Tags und Rezeptvorschlaege mit Zubereitungszeit/fehlenden Zutaten vorhanden. |
| `e43e7ff891` | 03_konzept.tex:38 | `fig:mockup_start_bookmarks` | Abgabe-Audit 31.07.: fig:mockup_start_bookmarks am Bild geprueft - Bereich 'Gespeicherte Rezepte' ist ausgeklappt dargestellt. |
| `09cceb8af2` | 03_konzept.tex:38 | `fig:mockup_feed` | Abgabe-Audit 31.07.: fig:mockup_feed am Bild geprueft - Beitraege mit Foto, Nutzername, Zutaten-Tag, Like/Kommentar sowie Challenge-Banner und Plus-Button vorhanden. |
| `aa957663b9` | 03_konzept.tex:38 | `fig:mockup_profil` | Abgabe-Audit 31.07.: fig:mockup_profil am Bild geprueft - Rettungspunkte, Reste-Level-Badge, Einsparangabe 12,4 kg und eigene Beitraege vorhanden. |
| `eb1b08c81b` | 04_community_und_feedback.tex:9 | `sec:zielgruppe` | Abgabe-Audit 31.07.: 02_zielgruppe.tex:7 nennt woertlich 'einen Ort bieten, an dem dieser Erfolg von anderen wahrgenommen wird'. Der verweisende Satz traegt seit Streichung von 'vor allem' keine Rangfolge mehr - Reichweite jetzt deckungsgleich. |
| `acc8ce8382` | 05_phasenplanung.tex:3 | `tab:phasenplanung` | Abgabe-Audit 31.07.: tab:phasenplanung zeigt Zeitrahmen- und Ressourcenspalte je Phase - Ankuendigung eingeloest. |
| `9873b19735` | 05_phasenplanung.tex:25 | `sec:zielgruppe` | Abgabe-Audit 31.07.: sec:zielgruppe definiert die Teilgruppe ueber drei Verhaltensmerkmale - Bezugspunkt fuer Repraesentativitaet korrekt. |
| `817d61716f` | 05_phasenplanung.tex:25 | `sec:konzept` | Abgabe-Audit 31.07.: 03_konzept.tex:3 fuehrt die Kooperationen mit Food-Sharing-Initiativen und Lebensmittelhaendler:innen ein - Fundstelle korrekt. |
| `6e5445d6f4` | 06_evaluation_reflexion.tex:3 | `sec:kernergebnisse_und_ausblick` | Abgabe-Audit 31.07.: 01_kernergebnisse_und_ausblick.tex:7 nennt die Kooperationen als Weg, neue Nutzer:innen zu erschliessen - genau die im verweisenden Satz gemeinte Skalierungsfunktion. |
| `11744d4cbe` | 06_evaluation_reflexion.tex:7 | `sec:community_und_feedback` | Abgabe-Audit 31.07.: 04:9 dokumentiert den Verzicht auf Gruppen und Foren zugunsten der Challenges - Kursaenderung dort belegt. |
| `d37c7c8131` | 06_evaluation_reflexion.tex:9 | `sec:iteratives_design` | Abgabe-Audit 31.07.: 07:3 beschreibt die frueh und ohne Programmieraufwand korrigierten Mockup-Runden; der Kostenvergleich des verweisenden Satzes ist damit gedeckt. |
| `b720e9b018` | 07_iteratives_design.tex:3 | `tab:phasenplanung` | Abgabe-Audit 31.07.: tab:phasenplanung weist 'Design & Prototyp' mit Woche 3-4 aus - Wochenangabe im verweisenden Satz stimmt exakt. |
| `20eca49ff0` | 07_iteratives_design.tex:3 | `sec:konzept` | Abgabe-Audit 31.07.: 03_konzept.tex:36 beschreibt die Drei-Bereiche-Navigation (Startseite, Rettungs-Feed, Profil) - Fundstelle korrekt. |

