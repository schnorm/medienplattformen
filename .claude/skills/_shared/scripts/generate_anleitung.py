#!/usr/bin/env python3
"""Erzeugt workflow-anleitung.pdf im Projekt-Root (reportlab, python3 + reportlab benötigt).

VERALTET als Pflegequelle: Die inhaltliche Wahrheit ist jetzt `handbuch.md` im
Projekt-Root (Markdown lässt sich ohne diesen Generator aktuell halten). Dieses
Skript bleibt nur, um bei Bedarf ein PDF-Derivat aus `handbuch.md` zu erzeugen —
vor einem erneuten Lauf den Fließtext unten gegen `handbuch.md` abgleichen,
sonst reproduziert der Lauf einen veralteten Stand.
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

# Pfad relativ zum Skript: .claude/skills/_shared/scripts/ -> Projekt-Root
from pathlib import Path
OUT = str(Path(__file__).resolve().parents[4] / "workflow-anleitung.pdf")
ACCENT = colors.HexColor("#1a3e6e")
LIGHT = colors.HexColor("#eef2f8")
GREY = colors.HexColor("#666666")

body = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=13.5, spaceAfter=5)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=14, bulletIndent=4, spaceAfter=3)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13.5, leading=17,
                    spaceBefore=14, spaceAfter=6, textColor=ACCENT)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14,
                    spaceBefore=10, spaceAfter=4, textColor=ACCENT)
title_st = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=19, leading=24,
                          spaceAfter=4, textColor=ACCENT)
sub_st = ParagraphStyle("s", parent=body, fontSize=10.5, textColor=GREY, spaceAfter=2)
cell = ParagraphStyle("cell", parent=body, fontSize=8.5, leading=11, spaceAfter=0)
cellb = ParagraphStyle("cellb", parent=cell, fontName="Helvetica-Bold")
box_st = ParagraphStyle("box", parent=body, fontSize=9, leading=12.5,
                        backColor=LIGHT, borderPadding=6, spaceBefore=6, spaceAfter=8)

_h1n = 0
def H1(txt):
    global _h1n; _h1n += 1
    return Paragraph(f"{_h1n}&nbsp;&nbsp;{txt}", h1)

def B(txt):
    return Paragraph(txt, bullet, bulletText="•")

def T(head, rows, widths):
    data = [[Paragraph(c, cellb) for c in head]] + \
           [[Paragraph(c, cell) for c in r] for r in rows]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#b8c4d8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    t.hAlign = "LEFT"
    return t

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(2*cm, A4[1]-1.1*cm, "Workflow-Anleitung „schriftlich“ · IU wissenschaftliches Arbeiten")
    canvas.drawRightString(A4[0]-2*cm, 1.1*cm, f"Seite {doc.page}")
    canvas.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                      topMargin=1.9*cm, bottomMargin=1.8*cm, title="Workflow-Anleitung schriftlich")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=header_footer)])

W = doc.width
el = []
el.append(Paragraph("Workflow-Anleitung „schriftlich“", title_st))
el.append(Paragraph("Handbuch für wissenschaftliche Arbeiten an der IU mit Claude · Hausarbeit, Fallstudie, Seminararbeit, Projektbericht", sub_st))
el.append(Paragraph("Stand: 18.07.2026 · Quellen: CLAUDE.md, Skill-Dateien (.claude/skills/), _shared/typen/", sub_st))
el.append(Spacer(1, 8))

el.append(H1("Wozu dieses Handbuch"))
el.append(Paragraph("Der Projektordner <b>schriftlich</b> ist eine LaTeX-Vorlage plus ein geführter Claude-Workflow für kleine wissenschaftliche Arbeiten (7–10 Seiten). Der Workflow besteht aus fünf Skills in fester Reihenfolge: <b>setup-check → plan-modus → schreib-modus → pruef-modus</b>, dazu <b>stresstest</b> als jederzeit einsetzbares Werkzeug. Dieses Handbuch beschreibt die Bedienung von Projektstart bis Abgabe — inklusive der Schnellspur „Plan kompakt“, mit der der Kapitelplan in einer einzigen Session steht.", body))

el.append(H1("Schnellreferenz: So startet jede Session"))
el.append(T(["Du willst …", "Schreibe in neuer Session"], [
    ["Umgebung prüfen (einmalig zu Beginn)", "„Setup-Check“"],
    ["Kapitelplan erstellen (Standard, 1 Session)", "„Plan kompakt“"],
    ["Kapitelplan ausführlich (empirische Seminararbeit)", "„Plan ausführlich“"],
    ["Nächstes Kapitel schreiben", "„Schreib-Modus: nächstes Kapitel“"],
    ["Ein Argument prüfen lassen", "„Stresstest auf: <Argument>“"],
    ["Erstes Kapitel gegenprüfen (früh, ohne Score)", "„Audit Kapitel: <name>“"],
    ["Arbeit oder Kapitelplan prüfen", "„Audit“"],
    ["Status erfahren", "„Wo stehen wir?“"],
], [W*0.5, W*0.5]))
el.append(Paragraph("Ihr müsst nie überlegen, wie eine Session startet — die Tabelle steht auch in CLAUDE.md ganz oben.", body))

el.append(H1("Grundprinzipien (gelten immer)"))
el.append(B("<b>Dateien sind Wahrheit, nicht der Chat-Verlauf.</b> aufgabe.md, kapitelplan.md, kapitelplan.draft.md und chapters/**/*.tex gelten vor jeder Erinnerung — bei Zweifel lesen lassen, nicht annehmen."))
el.append(B("<b>Nie ändern:</b> main.tex, pages/cover.tex, references.bib (Letzteres nur über den Zotero/Better-BibTeX-Auto-Export). Projektangaben stehen ausschließlich in pages/meta.tex (einmalig beim Projektstart ausfüllen)."))
el.append(B("<b>These und Kernargumente kommen von euch.</b> Claude hinterfragt und schärft, liefert aber nicht die inhaltliche Position. Das ist zugleich die Bedingung der IU-KI-Richtlinie: Die Verantwortung liegt beim Studierenden — jede gelieferte Quelle, Zahl oder Behauptung am Original verifizieren, bevor sie in die Arbeit übernommen wird."))
el.append(B("<b>Keine personenbezogenen Daten in Sessions</b> (IU-KI-Richtlinie): Interview-Transkripte vor der Verarbeitung anonymisieren (Namen → B1, B2 …), keine vertraulichen Unternehmensdaten ohne Freigabe."))
el.append(B("<b>Checkpoints werden im Chat sichtbar quittiert</b> („✅ Checkpoint gespeichert …“). Fehlt die Quittung, nachfragen."))
el.append(B("<b>Zwei Memory-Dateien:</b> Projektspezifische Korrekturen → MEMORY.md; projektunabhängige Dauer-Präferenzen (Stil, Zitation, Prozess) → PERSISTENT.md — die einzige Datei, die ihr von Projekt zu Projekt kopiert. Bei Widerspruch gewinnt MEMORY.md. Überholte Einträge werden als [ÜBERHOLT] markiert, nicht gelöscht."))
el.append(B("<b>Nur „Pflicht“-Regeln aus typen/&lt;typ&gt;.md zählen im Audit als FAIL.</b> „Optional“/„empfohlen“ sind Hinweise; „entfällt“ wird für den Papiertyp gar nicht geprüft. Pro Papiertyp existiert genau eine Typ-Datei (_shared/typen/) mit Pflichtregeln, Bewertungsgewichten, Kapitelgerüst, Voice und Audit-Checks."))
el.append(B("<b>Verständlichkeit ist Teil der Formalia-Prüfung.</b> Maßstab: Ein Laie versteht jeden Absatz beim ersten Lesen — kein gehäufter Nominalstil, keine gestelzten Meta-Verben. Details in _shared/hard-rules-formal.md → Verständlichkeit; Kalibrier-Referenz mit Positiv-/Negativ-Beispielen in _shared/stilprofil.md."))

el.append(H1("Session-Regeln (Memory-Management)"))
el.append(Paragraph("Kern des Workflows: <b>viele kurze Sessions statt einer großen.</b> Lange Sessions verbrennen Tokens und werden gegen Ende unzuverlässig.", body))
el.append(B("<b>Start-Ritual (&lt;1 Min.):</b> Statustabelle + „Aktuelle Richtung“ in CLAUDE.md lesen → PERSISTENT.md/MEMORY.md beachten → nur die Dateien laden, die das heutige Arbeitspaket braucht."))
el.append(B("<b>Arbeitspaket-Größen:</b> Plan kompakt = 1 Session · Plan ausführlich = 1–2 · Schreiben = 1 Hauptteil-Kapitel pro Session (Ausnahme: Einleitung + Schluss gemeinsam — je ~10 %, inhaltlich zusammenhängend) · Audit = 1 Session."))
el.append(B("<b>Ende-Ritual:</b> Checkpoint → Statustabelle → „Aktuelle Richtung“ auf nächsten Schritt → Quittung im Chat."))
el.append(B("<b>Kontext fast voll oder Session driftet?</b> Nicht „noch schnell fertig machen“ — Checkpoint schreiben, Session beenden, frisch weitermachen."))

el.append(H1("Der Workflow im Überblick"))
el.append(T(["Phase", "Skill", "Wann", "Ergebnis"], [
    ["Setup", "setup-check", "Einmalig bei neuem Projektordner", "Umgebung bereit; Frist erfasst"],
    ["Planen", "plan-modus", "Aufgabenstellung liegt vor, noch kein Kapitelplan", "aufgabe.md + kapitelplan.md"],
    ["Schreiben", "schreib-modus", "kapitelplan.md existiert", "chapters/**/*.tex, Kapitel für Kapitel"],
    ["Prüfen", "pruef-modus", "Vor der Abgabe (und nach Überarbeitungen)", "pruefbericht.md mit Score 0–100"],
    ["Stresstest", "stresstest", "Jederzeit, für ein einzelnes Argument", "Gegenargumente + Stärke"],
], [W*0.13, W*0.17, W*0.38, W*0.32]))
el.append(Paragraph("<b>EMPFEHLUNG</b> — Typischer Gesamtablauf: Setup (10 min) → <b>1 Kompakt-Plan-Session</b> → 2–4 Schreib-Sessions → Prüf-Audit → gezielte Überarbeitung → erneutes Audit → Abgabe. Jeder Zwischenstand liegt in Dateien, nie nur im Chat.", box_st))

el.append(H1("Phase 0: Setup (setup-check)"))
el.append(Paragraph("Einmalig beim ersten Öffnen ausführen. Geprüft werden: lualatex + biber, references.bib, Python-Skripte, Shared-Referenzen (inkl. typen/), pages/meta.tex, <b>Aufgabenstellung + Abgabefrist</b> (Frist wird in CLAUDE.md → Fristen eingetragen), <b>PERSISTENT.md</b> (noch Seed? → Datei aus dem Vorgängerprojekt hierher kopieren), Consensus-MCP, Ordnerstruktur.", body))
el.append(B("Zotero mit Better-BibTeX-Auto-Export auf references.bib einrichten (Anleitung: setup-check/references/bbt-setup.md). Nie manuell in die .bib-Datei schreiben."))
el.append(B("Gibt es eine frühere Arbeit? Deren PERSISTENT.md jetzt hierher kopieren — sonst gehen die arbeitenübergreifenden Lernpunkte verloren."))
el.append(B("Bei „NOCH EINRICHTUNG NÖTIG“: erst die genannten Punkte beheben, dann weiter."))

el.append(H1("Phase 1: Planen (plan-modus) — zwei Betriebsarten"))
el.append(Paragraph("<b>Kompakt</b> (Default für Hausarbeit, Fallstudie, Projektbericht, Literatur-Seminararbeit): Readiness + These + Kapitelgerüst in <b>einer</b> Dialogrunde, eine Runde pro Hauptteil-Kapitel, Einleitung/Schluss ohne eigene Runde, Stresstest optional. Ziel: kapitelplan.md in einer Session. <b>Ausführlich</b> (Default nur für die empirische Seminararbeit, sonst opt-in „Plan ausführlich“): jeder Schritt einzeln, sokratische Herleitung, Pflicht-Stresstest. Checkpoints nach jedem Schritt in kapitelplan.draft.md — beide Betriebsarten sind jederzeit unterbrechbar.", body))
el.append(T(["Schritt", "Inhalt", "Euer Beitrag"], [
    ["0 — Readiness", "Aufgabenstellung einlesen und nach <b>aufgabe.md</b> destillieren (wörtliche Leitfragen, Vorgaben, Frist, Bewertungsbezüge) — spätere Sessions lesen diese Datei statt des PDFs. Papiertyp + Betriebsart festlegen; bei Seminararbeit Forschungstyp.", "Aufgabenstellung bereitstellen, Papiertyp nennen"],
    ["1 — Literatur", "Nur falls Literatur fehlt: Consensus-Recherche (PICO/SPIDER/Dekomposition), Ergebnis: Priority Reading Order + Forschungslücken", "Framework mitwählen; Papers in Zotero importieren"],
    ["2 — These", "Leitfrage ≠ These. „Diese Arbeit argumentiert ___, weil ___, basierend auf ___“; Ebenen je nach Typ-Datei", "These selbst formulieren; stärkstes Gegenargument mitdenken"],
    ["2.5 — Kapitelgerüst", "Skelett mit Wortanteilen; <b>Seitenbudget an den Bewertungsgewichten ausgerichtet</b> (z. B. Hausarbeit: Argumentation 40 % → Diskussion größtes Kapitel; Fallstudie: Analyse+Konzepte+Ergebnis 75 % → Theorie knapp); Slugs festlegen", "Skelett bestätigen oder anpassen — hier, nicht später!"],
    ["3 — Kapitel für Kapitel", "Pro Hauptteil-Kapitel: Kernfragen → Kernargument, Belege, Risiko, Subsections. Techniken: Turning Point, Literatur-Landkarte, Limitationen dreischichtig", "Jedes Kapitel einzeln bestätigen"],
    ["4 — Stresstest", "Kompakt: optional (auf Wunsch oder bei wackelndem Argument). Ausführlich: Pflicht — alle Kernargumente mit Gegenargumenten konfrontieren", "Auf starke Gegenargumente inhaltlich reagieren"],
], [W*0.16, W*0.54, W*0.30]))
el.append(B("Session-Wiedereinstieg: Existiert kapitelplan.draft.md, bietet Claude „Weitermachen bei Schritt X?“ an. Nie stillschweigend von vorn beginnen lassen."))
el.append(B("<b>Session-Schnitt nach Schritt 1:</b> Die Literaturrecherche ist der größte Kontextposten der Planung. Danach Session beenden und Schritt 2 frisch starten — alles Weiterverwendbare liegt destilliert im Draft, und für Schritt 2–4 wechselt ohnehin das Modell."))
el.append(B("Seminararbeit als Literaturarbeit: Methodik-Kapitel bleibt als „Vorgehen der Literaturanalyse“ — die IU bewertet Methodik immer mit 20 %."))
el.append(B("Nur echte Consensus-Treffer zitieren lassen — wenige Ergebnisse werden ehrlich gemeldet, nicht mit Modellwissen aufgefüllt."))

el.append(H1("Phase 2: Schreiben (schreib-modus)"))
el.append(Paragraph("Verfasst Kapitel als LaTeX-Dateien auf Basis von kapitelplan.md (+ aufgabe.md für die wörtlichen Leitfragen). Master-Datei pro Hauptkapitel, Subsections als eigene Dateien per \\input{}.", body))
el.append(B("Vor jedem \\parencite{}: Keys per check_bib_keys.py validieren — Keys werden niemals erfunden."))
el.append(B("Nach dem Speichern: check_formalia.py — deckt jetzt auch Blockzitat > 40 Wörter, ½-Seiten-Heuristik und Überschriften-Dopplung deterministisch ab."))
el.append(B("Self-Check gegen die Pflicht-Punkte aus typen/&lt;typ&gt;.md (Absatzlogik, Synthese, Gegenargumente, Limitationen dreischichtig, Anti-KI-Stil)."))
el.append(B("Strukturabweichungen sofort nachziehen lassen (kapitelplan.md per Edit), sonst ist die „Dateien sind Wahrheit“-Quelle still falsch."))
el.append(B("Überarbeitungen nach Audit entlang pruefbericht.md abarbeiten, nicht aus dem Gedächtnis."))

el.append(H1("Phase 3: Prüfen (pruef-modus)"))
el.append(Paragraph("<b>Iterationsrhythmus:</b> Skripte + Self-Check im Schreib-Modus sind das Qualitätstor pro Kapitel — kein Voll-Audit nach jedem Kapitel. Empfohlener Ablauf: nach dem <b>ersten Hauptteil-Kapitel</b> ein Kapitel-Audit („Audit Kapitel: &lt;name&gt;“, ohne Score — fängt systematische Muster, bevor sie sich in die Folgekapitel kopieren) → restliche Kapitel schreiben → Voll-Audit, wenn alles FERTIG ist → Überarbeitung in eigenen Sessions → Re-Audit als Delta (nur FAIL-Punkte + Skripte + Build) → Abgabe-Audit mit Teil-Check E als Abschluss-Hinweisliste.", box_st))
el.append(Paragraph("Einziger Einstiegspunkt für Audits. Fünf Teil-Checks: <b>A</b> Formalia (Skripte + manuelle Punkte) · <b>B</b> Argumentationsqualität (nur Pflicht-Punkte der Typ-Datei als FAIL; inkl. Abgleich mit den Leitfragen aus aufgabe.md) · <b>C</b> Struktur · <b>D</b> Build (latexmk, Seitenumfang) · <b>E</b> Abgabe (neu). Ergebnis: Score 0–100 als pruefbericht.md.", body))
el.append(Paragraph("<b>Teil-Check E — Abgabe:</b> Abgabe läuft ausschließlich über Turnitin im myCampus-Kurs, und die <b>Eidesstattliche Erklärung muss vorab elektronisch über myCampus abgegeben werden — vorher nimmt Turnitin nichts an.</b> Der Status steht in CLAUDE.md → Fristen. Außerdem: keine externe Plagiatssoftware vorab (Turnitin-Selbsttreffer-Risiko). Fließt in keinem Audit-Umfang in den Score ein (auch nicht im Abgabe-Audit) — erscheint stattdessen als „Vor der Einreichung“-Checkliste am Berichtsende.", box_st))
el.append(T(["Score", "Bedeutung", "Nächster Schritt"], [
    ["≥ 80", "Abgabereif", "Verbleibende Punkte optional nachbessern; PERSISTENT.md fürs nächste Projekt aktualisieren"],
    ["60–79", "Überarbeitung empfohlen", "Mit schreib-modus gezielt an den Kritikpunkten arbeiten"],
    ["< 60", "Nicht einreichen", "Mindestens einen weiteren Prüf-Schreib-Zyklus einplanen"],
], [W*0.12, W*0.28, W*0.60]))
el.append(B("<b>Audit und Überarbeitung trennen:</b> Nach dem Audit neue Session starten — pruefbericht.md trägt die priorisierte Arbeitsliste hinüber, und die Überarbeitung läuft mit dem günstigeren Modell (Audit: Opus · Abarbeiten: Sonnet)."))
el.append(B("Das Audit frühzeitig einsetzen — auch auf den Kapitelplan oder einzelne Kapitel, nicht erst am Abgabetag."))
el.append(B("Der Score ist ein Priorisierungs-Hilfswert, keine Zusicherung — die Entscheidung „einreichen oder nicht“ bleibt bei euch."))

el.append(H1("Modell- und Thinking-Empfehlung je Phase"))
el.append(Paragraph("Kompakte Arbeiten sind <b>Sonnet-lastig</b>: Der Umfang (7–10 Seiten, enge Aufgabenstellung) rechtfertigt Opus-Planung nur selten. Opus gezielt dort, wo wenige Tokens über die Qualität entscheiden.", body))
el.append(T(["Phase", "Modell", "Thinking", "Begründung"], [
    ["setup-check", "Haiku 4.5", "aus/niedrig", "Nur deterministische Tool-Aufrufe."],
    ["Plan kompakt (Standard)", "Sonnet 5", "hoch", "Eine gebündelte Session; hohes Thinking gleicht die knappere Dialogführung aus — Opus lohnt bei diesem Umfang selten."],
    ["Plan ausführlich, Schritt 2–4 (empirische Seminararbeit)", "Opus 4.8 / Fable 5", "hoch", "These-Ebenen, Argumentketten, Pflicht-Stresstest — höchste Denkleistung pro Token."],
    ["Plan Schritt 0–1 (Readiness, Literatur)", "Sonnet 5", "niedrig–mittel", "Extraktion und Query-Formulierung; viele Consensus-Calls."],
    ["schreib-modus", "Sonnet 5", "mittel", "Volumenphase; Regeltreue liefern die Skripte. Opus als Option für das argumentativ kritischste Kapitel."],
    ["pruef-modus (Zwischen-Audit)", "Sonnet 5", "mittel", "A/D/E weitgehend deterministisch; B auf Kapitel-Ebene gut machbar."],
    ["pruef-modus (finales Abgabe-Audit)", "Opus 4.8", "mittel–hoch", "Letzte Instanz vor Turnitin — Teil-Check B braucht echtes Urteilsvermögen."],
    ["Überarbeitung nach Prüfbericht", "Sonnet 5", "niedrig", "Abarbeiten einer konkreten Liste."],
    ["stresstest (Einzelaufruf)", "Fable 5 / Opus 4.8", "hoch", "Kürzester Input, höchste Reasoning-Dichte."],
], [W*0.26, W*0.15, W*0.13, W*0.46]))
el.append(Paragraph("Faustregel: Teures Modell und hohes Thinking dort, wo wenige Tokens über die Qualität der ganzen Arbeit entscheiden (These, Stresstest, finales Audit); Sonnet überall sonst. Eine fest gewählte Zuordnung als [LERNEN:prozess]-Eintrag in PERSISTENT.md hinterlegen lassen (gilt projektübergreifend).", body))

el.append(H1("Welche Datei ist wofür (Schnellreferenz)"))
el.append(T(["Datei", "Rolle", "Wer schreibt"], [
    ["CLAUDE.md", "Schnellreferenz, Regeln, Session-Regeln, Statustabelle, Fristen (inkl. Eidesstattliche Erklärung)", "Skills (Status), sonst fix"],
    ["aufgabe.md", "Destillierte Aufgabenstellung — Single Source statt Aufgaben-PDF", "plan-modus (Schritt 0)"],
    ["kapitelplan.draft.md", "Checkpoint-Datei des Plan-Modus; danach INSIGHT-Archiv", "plan-modus"],
    ["kapitelplan.md", "Finaler Kapitelplan — Single Source für Struktur und Argumente", "plan-modus (Output)"],
    ["chapters/**/*.tex", "Der finale Text (Master- + Subsection-Dateien)", "schreib-modus"],
    ["pruefbericht.md", "Letzter Audit-Bericht; Arbeitsliste für Überarbeitungen", "pruef-modus"],
    ["MEMORY.md", "Projektspezifische Korrekturen ([LERNEN:kategorie])", "Skills bei euren Korrekturen"],
    ["PERSISTENT.md", "Projektübergreifende Dauer-Präferenzen — wandert per Kopie ins nächste Projekt", "Skills; ihr kopiert sie weiter"],
    ["_shared/typen/<typ>.md", "Alle papiertyp-spezifischen Regeln (Pflicht, Bewertung, Gerüst, Voice, Audit)", "Fix (Vorlage)"],
    ["references.bib", "Zitationen — nur über Zotero/BBT-Auto-Export", "Zotero (nie manuell)"],
    ["pages/meta.tex", "Einzige Stelle für Projektangaben", "Ihr, einmalig beim Start"],
    ["main.tex / pages/cover.tex", "Wurzeldokument und Titelblatt", "Niemand — nie ändern"],
], [W*0.24, W*0.52, W*0.24]))
el.append(Paragraph("<b>ACHTUNG</b> — Häufige Bedienfehler: main.tex oder cover.tex anfassen lassen · references.bib von Hand editieren · Schreib-Session ohne kapitelplan.md starten · Plan-Session neu beginnen, obwohl ein Draft existiert · Checkpoints ohne Chat-Quittung durchgehen lassen · Strukturänderungen nur im Chat besprechen · Audit erst am Abgabetag · PERSISTENT.md beim Projektwechsel vergessen · Eidesstattliche Erklärung erst am Abgabetag abgeben wollen.", box_st))
el.append(Paragraph("Quellen: CLAUDE.md · setup-check/, plan-modus/, schreib-modus/, pruef-modus/, stresstest/ (SKILL.md) · _shared/hard-rules-formal.md, _shared/typen/ · MEMORY.md, PERSISTENT.md", sub_st))

doc.build(el)
print("OK:", OUT)
