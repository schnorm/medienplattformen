#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_quellentreue.py – gleicht jede Zitation gegen den Volltext der Quelle ab.

Prüft drei Dinge, die sonst niemand mechanisch prüft:
  1. **Wortlaut**: Wurde inhaltlich paraphrasiert oder Wort für Wort übernommen?
     Ab `--min-words` (Default 7) zusammenhängend gleichen Wörtern gilt eine
     Stelle als übernommen – außer sie ist als wörtliches Zitat gekennzeichnet.
  2. **Wörtliche Zitate**: Steht der Text in `\\enquote{}`/`blockzitat`, muss er
     **exakt** so in der Quelle stehen. Als wörtliches Zitat gilt, was dicht am
     Beleg steht – davor wie danach, denn die narrative Form (`\\textcite{k} nennt
     es \\enquote{…}`) ist genauso ein Zitat. Weiter entfernte `\\enquote{}` zählen
     nicht: An der IU ist das auch das Anführungszeichen für Begriffe, und eine
     Begriffsanführung ist kein Zitat. Für `blockzitat` gilt ein weites Fenster –
     die Umgebung ist per Definition ein Zitat, und der einleitende Satz steht
     regelmäßig einen Absatz davor. Die vom Zitierleitfaden erlaubten Eingriffe
     ([sic], eckige Ergänzungen, Hervorhebungs-Hinweise, Auslassungen mit drei
     Punkten) werden vor dem Vergleich herausgerechnet.
  3. **Seitenangabe**: Kommen die Kernbegriffe des Trägersatzes auf der
     zitierten Seite überhaupt vor? Wenn nicht, wird die wahrscheinlich
     gemeinte Seite vorgeschlagen. Lässt sich der Versatz zwischen gedruckter
     und PDF-Seite nicht bestimmen (häufig bei Artikel-PDFs), wird gegen das
     ganze Dokument geprüft und die Seitenangabe als maschinell unbestätigt
     ausgewiesen – geprüft wird trotzdem, nur eben nicht seitengenau.

**E-Books ohne Seitenzahlen** (`[Kap. X]`-Locator, IU-Vorgabe): Das `file`-Feld
darf statt eines PDFs auch ein `.epub` tragen. Statt eines Seitenversatzes wird
dann das eigene NCX-Inhaltsverzeichnis des E-Books ausgewertet – "17.2.2" im
Text wird gegen die dort hinterlegte Kapitelnummer aufgelöst, nicht gegen eine
Seite. Löst das Inhaltsverzeichnis die zitierte Unterebene nicht auf (viele
E-Books nummerieren nur die oberste Ebene), gilt dieselbe Ausweich-Logik wie
bei PDFs ohne bestimmbaren Seitenversatz: Prüfung gegen das ganze Buch, die
Stellenangabe bleibt maschinell unbestätigt statt den Lauf abzubrechen.

Was das Skript **nicht** entscheidet: ob die Aussage inhaltlich von der Quelle
gedeckt ist. Das ist der zweite Schritt und Aufgabe des Modells; das Skript
liefert dafür die Prüfpaare (Trägersatz + Seitentext) und nimmt das Urteil per
`--verdikt` entgegen.

Nutzung (vom Projekt-Root):
    python .claude/skills/_shared/scripts/check_quellentreue.py
    python .claude/skills/_shared/scripts/check_quellentreue.py --datei chapters/02_theorie
    python .claude/skills/_shared/scripts/check_quellentreue.py --alle
    python .claude/skills/_shared/scripts/check_quellentreue.py --paare 5
    python .claude/skills/_shared/scripts/check_quellentreue.py --verdikt <hash>=OK --notiz "S. 47 deckt die Aussage"
        (mehrere Urteile in einem Aufruf: je `--verdikt` ein eigenes `--notiz`
         in derselben Reihenfolge. Eine Notiz für mehrere Urteile ist ein
         Fehler und kein Kürzel – sie würde stillschweigend falsch zugeordnet.)
    python .claude/skills/_shared/scripts/check_quellentreue.py --seite <bibkey> 453
        (nur den Text der zitierten Seite ausgeben – fuer den Schreibschritt,
         der den Satz aus der Quelle heraus formuliert; kein Prueflauf. Bei
         E-Books statt der Seite die Kapitelnummer angeben, z. B. 17.2.2)
    python .claude/skills/_shared/scripts/check_quellentreue.py --offset <bibkey>=-906
        (Versatz = PDF-Seite wie im Reader minus gedruckte Seite; ein Artikel,
         der auf S. 907 beginnt und dessen PDF bei 1 anfaengt: 1 - 907 = -906.
         Gilt nur fuer PDFs -- E-Books brauchen keinen Versatz.)

Ergebnis: `quellencheck.md` (Bericht, wird pro Lauf überschrieben) und
`quellencheck-state.json` (Urteile je Zitation, überdauert Läufe – nicht von
Hand editieren).

Exit-Code 0 = keine offenen Punkte · 1 = Befunde oder ungeprüfte Zitationen
offen · 2 = Ausführungsfehler (fehlende Datei, fehlende Abhängigkeit).

Buchungen (`--verdikt`, `--offset`, `--ausnahme`) geben 0 zurück, sobald sie
geschrieben sind – auch wenn danach noch etwas offen ist. Sonst sähe jede
einzelne Buchung nach einem Fehlschlag aus. Der Torwert 1 bleibt dem reinen
Prüflauf vorbehalten, der ihn in Ketten wie `check && latexmk` braucht.
"""

import argparse
import hashlib
import html
import json
import posixpath
import re
import sys
import zipfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

CITE_CMD_RE = re.compile(
    r"\\(?:[Pp]arencites?|[Cc]ites?|[Tt]extcites?|[Ff]ootcites?|[Aa]utocites?)\b"
    r"((?:\[[^\]]*\]|\{[^}]*\})*)"
)
ARG_TOKEN_RE = re.compile(r"\[([^\]]*)\]|\{([^}]*)\}")
KEY_RE = re.compile(r"\{([^}]*)\}")
# Seitenangabe im Locator. Der Zitierleitfaden (2.2.1) kennt zwei Formen, und
# beide müssen erkannt werden: zusammenhängender Bereich mit Gedankenstrich
# („S. 24--25") und nicht aufeinanderfolgende Seiten mit Komma („S. 12, 34").
# Wer nur die erste Zahl liest, prüft bei der Komma-Form gegen die falsche Seite
# und meldet eine korrekte Zitation als SEITE VERDÄCHTIG.
SEITE_RE = re.compile(
    r"S\.?\s*~?\s*(\d+(?:\s*(?:--|–|-)\s*\d+)?(?:\s*,\s*\d+(?:\s*(?:--|–|-)\s*\d+)?)*)")
SEITE_TEIL_RE = re.compile(r"(\d+)(?:\s*(?:--|–|-)\s*(\d+))?")
# Kapitel-Locator für E-Books ohne feste Seitenzahlen (IU-Vorgabe, siehe
# hard-rules-formal.md: "[Kap. X] / [Abs. X]"). Hierarchische Nummern wie
# "17.2.2" werden vollständig erfasst, nicht nur die erste Ziffer.
KAPITEL_RE = re.compile(r"Kap\.?\s*~?\s*(\d+(?:\.\d+)*)")
BIB_ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
ENQUOTE_RE = re.compile(r"\\enquote\{((?:[^{}]|\{[^{}]*\})*)\}")
BLOCKZITAT_RE = re.compile(r"\\begin\{blockzitat\}(.*?)\\end\{blockzitat\}", re.S)

# Zuordnung Anführung → Beleg. `\enquote{}` ist an der IU nicht nur das wörtliche
# Zitat, sondern das Anführungszeichen überhaupt (hard-rules-formal.md: gerade
# Anführungszeichen sind ein FEHLER). Eine großzügige Umgebungssuche erklärt
# deshalb jede Begriffsanführung im Satz zum wörtlichen Zitat – das müsste dann
# exakt in der Quelle stehen und erzeugt bei fremdsprachiger Literatur einen
# ZITAT-WEICHT-AB-Befund, der im Abgabe-Audit blockiert.
MAX_ZITAT_ABSTAND = 40   # Zeichen zwischen Anführungsende und Zitierbefehl
MIN_ZITAT_WOERTER = 5    # darunter: Kurzzitat oder Begriffsanführung – nicht entscheidbar

# Für `blockzitat` gilt ein weit größeres Fenster, und Satzenden dazwischen sind
# unschädlich. Grund: Die vom Zitierleitfaden vorgeführte Normalform lautet
# „\textcite[S. 40]{key} fasst die Entwicklung wie folgt zusammen:" + Leerzeile +
# \begin{blockzitat} – das sind weit mehr als 40 Zeichen. Mit dem engen Fenster
# wurde ausgerechnet für die langen wörtlichen Zitate KEIN Wortlautabgleich
# gefahren, also dort, wo eine Abweichung am teuersten ist. Die Sorge, die das
# enge Fenster begründet (eine Begriffsanführung als Zitat zu lesen), entfällt
# hier: Eine blockzitat-Umgebung ist per Definition ein wörtliches Zitat.
MAX_BLOCKZITAT_ABSTAND = 400

# Eingriffe, die der Zitierleitfaden im wörtlichen Zitat ausdrücklich erlaubt:
# eckige Klammern ([sic], eigene Ergänzungen, [Hervorhebung d. Verf.], der bei
# Satzbau-Anpassung weggelassene Buchstabe) und Auslassungen mit drei Punkten.
# Sie stehen naturgemäß NICHT in der Quelle. Ohne diese Bereinigung meldet der
# Vergleich jedes regelkonform bearbeitete Zitat als ZITAT WEICHT AB – ein
# Befund, der im Abgabe-Audit blockiert.
ZITAT_KLAMMER_RE = re.compile(r"\[[^\]]*\]")
ZITAT_AUSLASSUNG_RE = re.compile(r"\s*(?:\.\s*\.\s*\.|…|\\dots\b|\\ldots\b)\s*")
MIN_SEGMENT_WOERTER = 3  # kürzere Teilstücke tragen keinen Vergleich

STOPP = {
    "aber", "auch", "beim", "dabei", "damit", "dann", "dass", "dem", "den", "der",
    "des", "die", "dies", "diese", "diesem", "diesen", "dieser", "durch", "eine",
    "einem", "einen", "einer", "eines", "für", "haben", "hier", "ihre", "immer",
    "insbesondere", "ist", "jedoch", "kann", "können", "lassen", "man", "mehr",
    "mit", "muss", "nach", "nicht", "noch", "nur", "oder", "sein", "sich", "sind",
    "sowie", "über", "und", "unter", "vgl", "vom", "von", "vor", "während",
    "werden", "wird", "wobei", "zum", "zur", "zwischen",
}

STATUS_BEFUND = {"WORTLAUT", "ZITAT WEICHT AB", "SEITE VERDÄCHTIG", "CLAIM SCHÄRFER",
                 "NICHT GEFUNDEN", "SEITE AUSSERHALB", "RENTIERT NICHT"}

# „OK" heisst hier: Ein zur Textstelle passender Wortlaut wurde an der
# angegebenen Stelle gefunden. Es heisst NICHT: Die Quelle traegt die Behauptung
# in der Staerke, in der der Satz sie aufstellt. Genau dieser Unterschied ist der
# Bewertungsunterschied - in einem Schwesterprojekt fand eine Reichweitenpruefung
# an bereits mit OK quittierten Zitationen zehn Befunde. Der interne Wert bleibt
# „OK" (Kompatibilitaet mit bestehenden quellencheck-state.json und --verdikt),
# nach aussen heisst er, was er ist.
ANZEIGE_STATUS = {"OK": "FUNDSTELLE OK"}


def anzeige(status: str) -> str:
    return ANZEIGE_STATUS.get(status, status)
# „DATEI NICHT GEFUNDEN" steht bewusst hier und nicht bei den Befunden: Es ist
# kein Mangel der Arbeit, sondern eine ungeprüfte Zitation aus technischem
# Grund. Wer es als Befund führte, produzierte genau den Fehler, der zu dieser
# Klasse geführt hat – ein Punktabzug für ein Pfadproblem.
STATUS_OFFEN = {"PRÜFEN", "NICHT PRÜFBAR", "LIVE PRÜFEN", "DATEI NICHT GEFUNDEN",
                "VOLLTEXT BESCHAFFBAR", "ZUGANG PRÜFEN"}


@dataclass
class Zitation:
    datei: str
    zeile: int
    key: str
    seite: str          # "43", "43-45" oder "" (werkbezogen)
    satz: str
    woertlich: str      # Text in \enquote{}/blockzitat, sonst ""
    kapitel: str = ""   # "17.2.2" bei [Kap. X]-Locators (E-Books ohne Seitenzahlen)
    status: str = "PRÜFEN"
    befund: str = ""
    seitentext: str = ""
    notiz: str = ""
    _hash: str = field(default="", repr=False)

    @property
    def hash(self) -> str:
        if not self._hash:
            roh = f"{self.key}|{self.seite}|{self.kapitel}|{normalisiere(self.satz)}"
            self._hash = hashlib.sha1(roh.encode("utf-8")).hexdigest()[:10]
        return self._hash


def normalisiere(text: str) -> str:
    """LaTeX-Rauschen entfernen, Kleinschreibung, Wortfolge vereinheitlichen."""
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\(?:[Pp]arencites?|[Cc]ites?|[Tt]extcites?|[Ff]ootcites?"
                  r"|[Aa]utocites?)\b(?:\[[^\]]*\]|\{[^}]*\})*", " ", text)
    text = re.sub(r"\\(?:label|autoref|ref|footnote|quelle|acs?|acl?)\{[^}]*\}", " ", text)
    text = re.sub(r"\\[a-zA-Z@]+\*?", " ", text)
    text = re.sub(r"[{}~$\\]", " ", text)
    text = text.replace("\u00ad", "").replace("\u2010", "-")
    text = re.sub(r"[^\wäöüÄÖÜß\s-]", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def woerter(text: str) -> list[str]:
    return [w for w in normalisiere(text).split() if w]


# ---------------------------------------------------------------- .tex-Parsing

SATZENDE_RE = re.compile(r"(?<![A-ZÄÖÜ])(?<!\bS)(?<!\bvgl)(?<!\bz)(?<!\bB)(?<!\bu)"
                         r"(?<!\ba)(?<!\bca)(?<!\bbzw)[.!?](\s|$)")


def satz_um(text: str, pos: int) -> str:
    """Den Satz zurückgeben, in dem die Position liegt.

    Zitierbefehle werden vorher ausmaskiert: In `\\textcite[S. 59]{key}` steckt
    ein „. " mitten im Satz, und wer darauf trifft, schneidet den Trägersatz
    genau vor der Aussage ab, die belegt werden soll – der Vergleich mit der
    Quelle liefe dann gegen den falschen Text.
    """
    if in_tabelle(text, pos):
        return zellen_satz(text, pos)
    maske = list(text)
    for m in CITE_CMD_RE.finditer(text):
        for i in range(m.start(), m.end()):
            maske[i] = " "
    maskiert = "".join(maske)
    start = 0
    for m in SATZENDE_RE.finditer(maskiert[:pos]):
        start = m.end()
    rest = SATZENDE_RE.search(maskiert[pos:])
    ende = pos + rest.end() if rest else len(text)
    return ohne_struktur(text[start:ende]).strip()


# LaTeX-Struktur ohne Aussagegehalt, die sonst im Trägersatz und damit im Hash
# landet. Bewusst NICHT dabei: \caption{} und \quelle{} – dort steht Text, der
# zitiert wird („Eigene Darstellung in Anlehnung an \cite{…}"), und wer sie
# entfernt, lässt genau den Trägersatz verschwinden, den die Prüfung braucht.
STRUKTUR_RE = re.compile(
    r"\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?(?:\{[^}]*\})?"  # Umgebung, Option, Spaltenspec
    r"|\\(?:top|mid|bottom)rule(?:\[[^\]]*\])?"                # booktabs-Linien
    r"|\\label\{[^}]*\}"                                       # Anker
    r"|\\(?:hline|centering|small|footnotesize|arraybackslash)\b")


def ohne_struktur(satz: str) -> str:
    """Strukturbefehle aus dem Trägersatz entfernen (siehe STRUKTUR_RE)."""
    return re.sub(r"\s{2,}", " ", STRUKTUR_RE.sub(" ", satz))


# Argumente mitschlucken: `\begin{tabular}{ll}`, bei tabularx zusätzlich die
# Breite (`{\textwidth}{lX}`). Sonst bleibt die Spaltenspezifikation als „{ll}"
# vor dem Zeilenkopf stehen.
TABELLE_BEGIN_RE = re.compile(
    r"\\begin\{(?:tabular|tabularx|longtable)\*?\}"
    r"(?:\[[^\]]*\])?(?:\{[^{}]*\}){0,2}")
TABELLE_END_RE = re.compile(r"\\end\{(?:tabular|tabularx|longtable)\*?\}")
ZEILENENDE_RE = re.compile(r"\\\\")
ZELLENTRENNER_RE = re.compile(r"(?<!\\)&")


def in_tabelle(text: str, pos: int) -> bool:
    """Liegt `pos` innerhalb einer tabular-Umgebung?"""
    letztes_begin = max((m.start() for m in TABELLE_BEGIN_RE.finditer(text[:pos])),
                        default=-1)
    letztes_ende = max((m.start() for m in TABELLE_END_RE.finditer(text[:pos])),
                       default=-1)
    return letztes_begin > letztes_ende


def zellen_satz(text: str, pos: int) -> str:
    """Trägersatz einer Zitation in einer Tabellenzelle: die Zelle selbst.

    Eine Zelle enthält keinen Satzschlusspunkt. Die Satzgrenzen-Logik spannte
    deshalb vom letzten Punkt VOR der Tabelle bis zum ersten Punkt DANACH –
    gemessen an einem realen Projekt 1530 Zeichen, beginnend bei
    `\\begin{table}[H]` und endend mitten im Folgeabsatz. Folge: Jede Änderung
    in der Nachbarschaft der Tabelle invalidierte alle Urteile ihrer Zellen,
    obwohl kein Zeichen des zitierenden Textes berührt war – an einem Tag
    dreimal, neun Neubuchungen.

    Der Zeilenkopf (erste Zelle der Reihe) kommt als Kontext davor: Eine Zelle
    wie „Feedback und Fortschritt" allein ist für den semantischen Abgleich zu
    dünn, und der Kopf ändert sich nur, wenn die Reihe sich ändert.
    """
    # Zeilenanfang: das letzte `\\` – oder der Beginn der Tabelle, denn die
    # erste Reihe hat kein `\\` davor. Ohne diese Grenze reichte der Zeilenkopf
    # bis in den Absatz vor der Tabelle.
    start = max([m.end() for m in ZEILENENDE_RE.finditer(text[:pos])]
                + [m.end() for m in TABELLE_BEGIN_RE.finditer(text[:pos])]
                + [0])
    kandidaten = [m.start() for m in ZEILENENDE_RE.finditer(text[pos:])] \
        + [m.start() for m in TABELLE_END_RE.finditer(text[pos:])]
    ende = pos + min(kandidaten) if kandidaten else len(text)
    zeile = text[start:ende]
    rel = pos - start

    grenzen = [0] + [m.end() for m in ZELLENTRENNER_RE.finditer(zeile)] + [len(zeile)]
    zellen = [zeile[a:b].rstrip("&").strip() for a, b in zip(grenzen, grenzen[1:])]
    idx = sum(1 for g in grenzen[1:-1] if g <= rel)
    zelle = ohne_struktur(zellen[idx]).strip() if idx < len(zellen) else ""
    kopf = ohne_struktur(zellen[0]).strip() if zellen else ""
    if kopf and kopf != zelle:
        return f"{kopf} – {zelle}"
    return zelle


def spanne(text: str, muster: re.Pattern, block: bool = False) -> list[tuple[int, int, str, bool]]:
    return [(m.start(), m.end(), m.group(1), block) for m in muster.finditer(text)]


def zitat_segmente(woertlich: str) -> list[list[str]]:
    """Wörtliches Zitat in vergleichbare Teilstücke zerlegen.

    Entfernt die vom Zitierleitfaden erlaubten Klammer-Eingriffe und schneidet
    an Auslassungspunkten: Was zwischen zwei Auslassungen steht, muss in der
    Quelle zusammenhängend vorkommen – über die Auslassung hinweg naturgemäß
    nicht. Teilstücke unter MIN_SEGMENT_WOERTER Wörtern werden verworfen; sie
    bestehen aus Artikeln und Präpositionen und würden überall „gefunden".
    """
    ohne_klammern = ZITAT_KLAMMER_RE.sub(" ", woertlich)
    segmente = []
    for teil in ZITAT_AUSLASSUNG_RE.split(ohne_klammern):
        w = woerter(teil)
        if len(w) >= MIN_SEGMENT_WOERTER:
            segmente.append(w)
    return segmente


def enthaelt_folge(kurz: list[str], lang: list[str]) -> bool:
    """Kommt `kurz` als zusammenhängende Wortfolge in `lang` vor?"""
    n = len(kurz)
    if not n or n > len(lang):
        return False
    for i in range(len(lang) - n + 1):
        if lang[i:i + n] == kurz:
            return True
    return False


def seiten_liste(seite: str) -> list[tuple[int, int]]:
    """„12-13,34" → [(12, 13), (34, 34)]. Leerer String → []."""
    out: list[tuple[int, int]] = []
    for m in SEITE_TEIL_RE.finditer(seite or ""):
        von = int(m.group(1))
        bis = int(m.group(2)) if m.group(2) else von
        out.append((von, bis) if bis >= von else (von, von))
    return out


def ohne_zitattext(satz: str) -> str:
    """Als Zitat gekennzeichneten Text aus dem Trägersatz entfernen.

    Der Wortlaut-Vergleich sucht **unmarkierte** Übernahmen. Was in `\\enquote{}`
    steht, ist markiert und darf wortgleich sein – bliebe es im Vergleich, meldete
    das Skript ausgerechnet die korrekte Zitierweise als Übernahme. Der Fall trifft
    jedes Direktzitat, das nicht unmittelbar vor seinem Beleg steht.
    """
    return ENQUOTE_RE.sub(" ", satz)


def naechstes_zitat(text: str, zitate: list[tuple[int, int, str, bool]],
                    start: int, ende: int) -> str:
    """Das wörtliche Zitat, auf das sich der Zitierbefehl an [start, ende) bezieht.

    Zwei enge Bedingungen statt eines weiten Fensters (siehe MAX_ZITAT_ABSTAND):
    Die Anführung muss dicht am Beleg liegen, und dazwischen darf kein Satz enden.
    Damit bleibt `\\enquote{Zitat} \\parencite[S. 5]{k}` ein wörtliches Zitat,
    während `Der Begriff \\enquote{Resilienz} bezeichnet … \\parencite{k}` als das
    gelesen wird, was er ist: eine Begriffsanführung mit eigener Aussage.

    **Beide Richtungen zählen.** Die narrative Form – erst der Beleg, dann das
    Zitat (`\\textcite[S. 67]{k} nennt es \\enquote{…}`) – ist keine Randform,
    sondern die, zu der `hard-rules-formal.md` fürs Theorie-Kapitel ausdrücklich
    rät. Wurde sie nicht erkannt, lief für sie **kein** Wortlautabgleich: Ein
    Fehlzitat erzeugte dort keinen Befund, obwohl ZITAT WEICHT AB genau die
    Klasse ist, die im Abgabe-Audit blockiert. Nichts am deutschen Satzbau macht
    die eine Reihenfolge zum Zitat und die andere nicht.

    Der Preis der Symmetrie: Begriffsanführungen **nach** einem narrativen Beleg
    („Nach \\textcite{k} ist der Begriff \\enquote{Resilienz} zentral") werden
    miterfasst. Sie bleiben durch MIN_ZITAT_WOERTER auf ein PRÜFEN gedeckelt und
    können den blockierenden Befund nicht auslösen.

    Bei mehreren Kandidaten gewinnt der nächstgelegene, nicht der erste Fund.
    """
    beste: tuple[int, str] | None = None
    for a, b, inhalt, block in zitate:
        if a <= start <= b:                       # Beleg steht im Zitat selbst
            return inhalt
        if b <= start:                            # Anführung endet vor dem Beleg
            abstand, zwischen = start - b, text[b:start]
        elif a >= ende:                           # Anführung beginnt nach dem Beleg
            abstand, zwischen = a - ende, text[ende:a]
        else:
            continue
        if block:
            # blockzitat: großes Fenster, Satzenden dazwischen sind erlaubt
            # (der einleitende Satz endet regelmäßig vor dem Zitat).
            if abstand > MAX_BLOCKZITAT_ABSTAND:
                continue
        elif abstand > MAX_ZITAT_ABSTAND or SATZENDE_RE.search(zwischen):
            continue
        if beste is None or abstand < beste[0]:
            beste = (abstand, inhalt)
    return beste[1] if beste else ""


def lies_tex(pfade: list[Path]) -> list[Zitation]:
    out: list[Zitation] = []
    for pfad in pfade:
        text = pfad.read_text(encoding="utf-8", errors="replace")
        zitate = spanne(text, ENQUOTE_RE) + spanne(text, BLOCKZITAT_RE, block=True)
        for m in CITE_CMD_RE.finditer(text):
            satz = satz_um(text, m.start())
            woertlich = naechstes_zitat(text, zitate, m.start(), m.end())
            # Argumentliste blockweise lesen: `\parencites[S. 911]{a}[S. 5]{b}`
            # gibt jedem Werk eine EIGENE Seitenangabe. Wer hier alle Optionen
            # zusammenwirft, hängt die Seite des einen Werks an das andere und
            # erzeugt lauter falsche Seitenbefunde.
            seite = ""
            kapitel = ""
            for tok in ARG_TOKEN_RE.finditer(m.group(1)):
                opt, gruppe = tok.group(1), tok.group(2)
                if opt is not None:
                    s = SEITE_RE.search(opt)
                    if s:
                        # Auf die kanonische Form „12-13,34" normalisieren –
                        # Bereiche mit Bindestrich, Einzelseiten mit Komma.
                        seite = ",".join(
                            f"{v}-{b}" if b != v else f"{v}"
                            for v, b in seiten_liste(s.group(1)))
                    else:
                        k = KAPITEL_RE.search(opt)
                        if k:
                            kapitel = k.group(1)
                    continue
                for key in (k.strip() for k in gruppe.split(",") if k.strip()):
                    out.append(Zitation(
                        datei=str(pfad).replace("\\", "/"),
                        zeile=text[:m.start()].count("\n") + 1,
                        key=key, seite=seite, satz=satz, woertlich=woertlich,
                        kapitel=kapitel))
                seite = ""     # nächster Block beginnt ohne Seitenangabe
                kapitel = ""
    return out


# ---------------------------------------------------------------- .bib-Parsing

def lies_bib(pfad: Path) -> dict[str, dict[str, str]]:
    text = pfad.read_text(encoding="utf-8", errors="replace")
    eintraege: dict[str, dict[str, str]] = {}
    starts = [(m.start(), m.group(2), m.group(1)) for m in BIB_ENTRY_RE.finditer(text)]
    for i, (pos, key, typ) in enumerate(starts):
        ende = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        block = text[pos:ende]
        # `_typ` mit Unterstrich: kein Bib-Feld, sondern der Eintragstyp aus
        # `@book{…}` – er entscheidet, ob ein fehlender Volltext eine Besorgung
        # (Buch) oder ein Zugangsproblem (Artikel) ist.
        felder = {"_typ": typ.lower()}
        for feld in ("file", "url", "doi", "title", "author", "year", "date",
                     "pages", "zugang"):
            # Feldname am Zeilenanfang verankern: sonst trifft „pages" auch
            # `numpages`, „title" auch `booktitle`/`shorttitle` und „date" auch
            # `urldate` – und der falsche Wert kippt die ganze Seitenrechnung.
            m = re.search(r"(?mi)^\s*" + feld + r"\s*=\s*[{\"](.*?)[}\"]\s*,?\s*$",
                          block, re.S)
            if m:
                felder[feld] = m.group(1).strip()
        eintraege[key] = felder
    return eintraege


def _datei_kandidaten(feld: str) -> list[str]:
    """Kandidaten-Pfade aus dem `file`-Feld, roheste Form zuerst.

    Das ganze Feld zuerst unverändert versuchen: Handisch eingetragene
    Dateinamen (z. B. von Anna's Archive) enthalten selbst oft ein ';' –
    speziell bei mehreren Autor:innen oder Verlagen im Titel –, was mit
    Zoteros Mehrfeld-Trennzeichen kollidiert. Erst wenn das ganze Feld
    keinen Treffer ergibt, wird nach der Zotero-Konvention aufgeteilt
    (mehrere Dateien durch ';' getrennt, teils mit Typ-Suffix).
    """
    out = [feld.strip()]
    out += [t.strip() for t in feld.split(";")]
    return out


# Wohin ausgewichen wird, wenn der Pfad aus dem `file`-Feld nicht auflöst.
# Zotero schreibt IMMER absolute Pfade seiner lokalen Ablage
# (/home/…/Zotero/storage/X6D69NPM/…). Auf dem Rechner, der exportiert hat,
# lösen sie auf – in jeder anderen Umgebung nie. Das trifft damit jeden
# Bib-Eintrag mit angehängtem Volltext, sobald jemand anders (oder derselbe
# Nutzer auf einem zweiten Rechner) prüft: der Normalfall, nicht die Ausnahme.
LITERATUR_ORDNER = ("sources/literature", "sources/literatur")

# Hosts, hinter denen ein Volltext in aller Regel kostenpflichtig liegt. Die
# Liste ist eine Heuristik, keine Aufzaehlung: Sie soll den teuren Fall vom
# billigen trennen, nicht die Verlagslandschaft abbilden. Frei zugaengliche
# Anbieter (MDPI, Frontiers, PLOS, digitallibrary.un.org) stehen bewusst NICHT
# darin und behalten den bisherigen Status.
BEZAHLSCHRANKE_HOSTS = (
    "onlinelibrary.wiley.com", "linkinghub.elsevier.com", "sciencedirect.com",
    "link.springer.com", "tandfonline.com", "jstor.org", "dl.acm.org",
    "ieeexplore.ieee.org", "journals.sagepub.com", "emerald.com",
)
# Eintragstypen, bei denen ein fehlender Volltext eine Besorgung ist und kein
# Zugangsproblem: Buecher gibt es zu kaufen oder auszuleihen.
BUCH_TYPEN = {"book", "inbook", "incollection", "collection", "booklet"}


def zugangsklasse(eintrag: dict) -> str:
    """Warum fehlt der Volltext – und wie teuer ist die Behebung?

    Bisher landete alles ohne auflösbaren Volltext auf zwei Sammelstatus, die
    der Score gleich behandelt hat. Darunter liegen aber Fälle, die um
    Größenordnungen auseinanderliegen: ein Buch herunterladen (halbe Stunde),
    einen Snapshot ziehen (zwei Minuten) oder eine Quelle ersetzen, weil kein
    Zugang besteht. Ein Status, der das zusammenfasst, erzeugt falsche
    Prioritäten – die billigste und die teuerste Maßnahme stehen
    ununterscheidbar nebeneinander.

    `zugang = {…}` im Bib-Eintrag schlägt die Heuristik (über Zoteros
    Extra-Feld als `tex.zugang` pflegbar). Ob Better BibTeX frei gewählte
    Feldnamen durchreicht, ist nicht verifiziert – deshalb wird das Feld nur
    gelesen, nie vorausgesetzt.
    """
    explizit = (eintrag.get("zugang") or "").strip().lower()
    if explizit.startswith("kein"):
        return "ZUGANG PRÜFEN"
    if explizit in ("beschaffbar", "bibliothek") or explizit.startswith("oa:"):
        return "VOLLTEXT BESCHAFFBAR"
    if eintrag.get("_typ", "").lower() in BUCH_TYPEN:
        return "VOLLTEXT BESCHAFFBAR"
    ziel = f"{eintrag.get('url', '')} {eintrag.get('doi', '')}".lower()
    if any(h in ziel for h in BEZAHLSCHRANKE_HOSTS):
        return "ZUGANG PRÜFEN"
    return ""


def _pfad_kandidat(teil: str, endung: str, root: Path) -> Path | None:
    """Einen Eintrag aus dem `file`-Feld zu einem existierenden Pfad machen.

    Bewusst nur exakte Dateinamen, kein unscharfer Abgleich über Autor und
    Jahr: Ein Fuzzy-Treffer prüft die Zitation gegen das falsche Werk und
    meldet dafür OK. Ein stiller Falschbefund ist teurer als der laute
    Fehlalarm, den diese Funktion beseitigt.
    """
    if not teil.lower().endswith(endung):
        return None
    p = Path(teil)
    if not p.is_absolute():
        kandidat = root / p
        if kandidat.exists():
            return kandidat
    elif p.exists():
        return p
    # Pfad zeigt ins Leere: denselben Dateinamen in der Projektablage suchen.
    for ordner in LITERATUR_ORDNER:
        kandidat = root / ordner / p.name
        if kandidat.exists():
            return kandidat
    return None


def _bereinige(teil: str, typ_muster: str) -> str:
    teil = teil.replace("\\:", ":").replace("\\\\", "\\")
    teil = re.sub(rf":(?:{typ_muster})$", "", teil, flags=re.I)
    return re.sub(r"^[^:]*:(?=[A-Za-z]:[\\/]|/)", "", teil)


def _projekt_pfad(key: str, endung: str, root: Path) -> Path | None:
    """`sources/literature/<citekey>.pdf` – der einzige rechnerunabhängige Anker.

    Der Rückfall über den Dateinamen aus dem `file`-Feld greift nur, wenn
    Zotero und Projekt zufällig denselben Namen gewählt haben: Zotero vergibt
    „Barker et al. - 2021 - What Nudge Techniques Work.pdf", das Projekt nennt
    dieselbe Datei `barkerWhatNudgeTechniques2021.pdf`. Empirisch geprüft –
    ohne diesen Weg löst auf einem zweiten Rechner keine einzige Quelle auf,
    egal was in `sources/literature/` liegt.

    Deshalb steht der Citekey VOR dem `file`-Feld: Er ist das einzige
    Bindeglied, das ein BBT-Export nicht überschreiben kann.
    """
    if not key:
        return None
    for ordner in LITERATUR_ORDNER:
        p = root / ordner / f"{key}{endung}"
        if p.exists():
            return p
    return None


def pdf_pfad(feld: str, root: Path, key: str = "") -> Path | None:
    treffer = _projekt_pfad(key, ".pdf", root)
    if treffer:
        return treffer
    for teil in _datei_kandidaten(feld):
        treffer = _pfad_kandidat(_bereinige(teil, r"application/pdf|PDF"),
                                 ".pdf", root)
        if treffer:
            return treffer
    return None


def epub_pfad(feld: str, root: Path, key: str = "") -> Path | None:
    """Wie `pdf_pfad`, nur für `.epub`."""
    treffer = _projekt_pfad(key, ".epub", root)
    if treffer:
        return treffer
    for teil in _datei_kandidaten(feld):
        treffer = _pfad_kandidat(
            _bereinige(teil, r"application/epub\+zip|EPUB"), ".epub", root)
        if treffer:
            return treffer
    return None


def gesetzte_dateipfade(feld: str) -> list[str]:
    """Die im `file`-Feld genannten Volltext-Pfade – unabhängig davon, ob sie
    auflösen. Grundlage für die Unterscheidung „kein Volltext hinterlegt" vs.
    „Pfad zeigt ins Leere"; die zweite ist ein Konfigurationsproblem von
    dreißig Sekunden, die erste ein Rechercheproblem."""
    out = []
    for teil in _datei_kandidaten(feld):
        for endung, muster in ((".pdf", r"application/pdf|PDF"),
                               (".epub", r"application/epub\+zip|EPUB")):
            sauber = _bereinige(teil, muster)
            if sauber.lower().endswith(endung) and sauber not in out:
                out.append(sauber)
    return out


# ------------------------------------------------------------------ PDF-Zugriff

def seiten_texte(pdf: Path) -> list[str]:
    import pdfplumber
    with pdfplumber.open(str(pdf)) as doc:
        return [(s.extract_text() or "") for s in doc.pages]


# ----------------------------------------------------------------- EPUB-Zugriff
#
# E-Books haben keine feste Seitenzahl – die IU sieht dafür `[Kap. X]` vor
# (hard-rules-formal.md). Statt eines PDF-Seitenversatzes wird hier die
# eigene Kapitelstruktur des E-Books ausgewertet: container.xml -> OPF ->
# NCX-Inhaltsverzeichnis liefert für jede nummerierte Überschrift ("17.2.2
# Websites benutzerorientiert optimieren…") die Zieldatei plus Anker
# ("17_002.html#u17.2.2"). Zwischen zwei aufeinanderfolgenden Ankern **in
# derselben Datei** liegt genau der Text dieses Unterkapitels – mehrere
# Unterkapitel teilen sich oft eine gemeinsame HTML-Datei. Reine Stdlib
# (zipfile/re), kein zusätzliches Pip-Paket (ebooklib ist hier nicht
# installiert und für dieses schmale Extraktionsziel auch nicht nötig).

_EPUB_TAG_RE = re.compile(r"<[^>]+>")
_EPUB_NAVPOINT_RE = re.compile(
    r"<text>(.*?)</text>\s*</navLabel>\s*<content\s+src=\"([^\"]+)\"", re.S)
_EPUB_NUMMER_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\b")


def _epub_text_ohne_tags(roh: str) -> str:
    return " ".join(html.unescape(_EPUB_TAG_RE.sub(" ", roh)).split())


def epub_kapitel(epub: Path) -> tuple[list[str], dict[str, int]]:
    """Liefert (Kapiteltexte in Lesereihenfolge, Kapitelnummer -> Index).

    Wirft bei unlesbarem/unerwartet strukturiertem E-Book eine Exception –
    der Aufrufer behandelt das wie ein defektes PDF (NICHT PRÜFBAR).
    """
    with zipfile.ZipFile(str(epub)) as z:
        container = z.read("META-INF/container.xml").decode("utf-8", errors="replace")
        m = re.search(r'full-path="([^"]+)"', container)
        if not m:
            raise ValueError("kein rootfile in META-INF/container.xml")
        opf_pfad = m.group(1)
        opf_dir = posixpath.dirname(opf_pfad)
        opf = z.read(opf_pfad).decode("utf-8", errors="replace")

        ncx_href = None
        m = re.search(r'<spine[^>]*\btoc="([^"]+)"', opf)
        if m:
            mi = re.search(r'<item\b[^>]*\bid="' + re.escape(m.group(1)) +
                           r'"[^>]*\bhref="([^"]+)"', opf)
            if not mi:  # href kann vor id stehen – Attributreihenfolge ist frei
                mi = re.search(r'<item\b[^>]*\bhref="([^"]+)"[^>]*\bid="' +
                               re.escape(m.group(1)) + r'"', opf)
            ncx_href = mi.group(1) if mi else None
        if ncx_href is None:  # Fallback: erstes Manifest-Item vom NCX-Medientyp
            mi = re.search(r'<item\b[^>]*\bhref="([^"]+)"[^>]*'
                           r'\bmedia-type="application/x-dtbncx\+xml"', opf)
            ncx_href = mi.group(1) if mi else None
        if ncx_href is None:
            raise ValueError("kein NCX-Inhaltsverzeichnis im Manifest gefunden "
                             "(nur EPUB2/NCX wird unterstützt)")
        ncx_pfad = posixpath.normpath(posixpath.join(opf_dir, ncx_href))
        ncx = z.read(ncx_pfad).decode("utf-8", errors="replace")

        # (Nummer, href, Anker) in Dokument-/Lesereihenfolge – nur nummerierte
        # Einträge zählen als zitierfähiges Kapitel (Vorwort/Register o. Ä.
        # ohne führende Zahl werden übersprungen, sie tragen keine [Kap. X]-Angabe).
        eintraege: list[tuple[str, str, str]] = []
        for nm in _EPUB_NAVPOINT_RE.finditer(ncx):
            label = html.unescape(_EPUB_TAG_RE.sub(" ", nm.group(1))).strip()
            nummer_m = _EPUB_NUMMER_RE.match(label)
            if not nummer_m:
                continue
            src = nm.group(2)
            href, _, anker = src.partition("#")
            href = posixpath.normpath(posixpath.join(opf_dir, href))
            eintraege.append((nummer_m.group(1), href, anker))

        # Je Zieldatei einmal lesen, Anker-Offsets bestimmen, dazwischen slicen.
        text_je_nummer: dict[str, str] = {}
        for href in dict.fromkeys(e[1] for e in eintraege):  # Reihenfolge erhalten
            try:
                roh = z.read(href).decode("utf-8", errors="replace")
            except KeyError:
                continue
            in_datei = [(nr, anker) for nr, h, anker in eintraege if h == href]
            positionen: list[tuple[int, str]] = []
            for nr, anker in in_datei:
                if not anker:
                    positionen.append((0, nr))
                    continue
                am = re.search(r'\bid=["\']' + re.escape(anker) + r'["\']', roh)
                if am:
                    # Ab dem öffnenden Tag schneiden, nicht mitten im Attribut –
                    # sonst bleibt das Tag-Ende ("... class=\"t3\">") als
                    # nicht erkannter Rumpf-Text vor dem eigentlichen Inhalt
                    # stehen (der Tag-Anfang "<h3 " ist ja schon abgeschnitten).
                    tag_start = roh.rfind("<", 0, am.start())
                    positionen.append((tag_start if tag_start != -1 else am.start(), nr))
            positionen.sort(key=lambda p: p[0])
            for i, (start, nr) in enumerate(positionen):
                ende = positionen[i + 1][0] if i + 1 < len(positionen) else len(roh)
                text_je_nummer[nr] = _epub_text_ohne_tags(roh[start:ende])

        texte: list[str] = []
        index_von_nummer: dict[str, int] = {}
        for nummer, _, _ in eintraege:
            if nummer in index_von_nummer or nummer not in text_je_nummer:
                continue  # Dubletten/nicht auffindbare Anker überspringen
            index_von_nummer[nummer] = len(texte)
            texte.append(text_je_nummer[nummer])
        return texte, index_von_nummer


def resolve_kapitel(nummer: str, index: dict[str, int]) -> tuple[int | None, str]:
    """Exakte Kapitelnummer, sonst schrittweise zur übergeordneten Ebene
    zurückfallen ("17.2.2" -> "17.2" -> "17") – viele E-Book-Inhaltsverzeichnisse
    lösen nicht jede Unterebene einzeln auf."""
    teile = nummer.split(".")
    for n in range(len(teile), 0, -1):
        kandidat = ".".join(teile[:n])
        if kandidat in index:
            return index[kandidat], kandidat
    return None, ""


def seitenbereich(pages: str) -> tuple[int, int] | None:
    """`pages = {907--912}` → (907, 912). Artikelnummern/Einzelseiten → None."""
    m = re.match(r"\s*(\d+)\s*(?:--|–|-)\s*(\d+)\s*$", pages or "")
    if not m:
        return None
    von, bis = int(m.group(1)), int(m.group(2))
    return (von, bis) if bis >= von else None


def versatz_aus_pages(pages: str, anzahl: int) -> int | None:
    """Versatz aus dem Seitenbereich des Bib-Eintrags ableiten.

    Der zuverlässigste Weg bei Zeitschriftenartikeln: Steht im Eintrag
    `pages = {907--912}` und hat das PDF (bis auf zwei Seiten Toleranz für
    Deckblätter) genau diesen Umfang, dann ist die gedruckte Seite 907 die
    erste PDF-Seite. Das schlägt jede Fußzeilen-Heuristik, weil es aus einer
    gepflegten Metadatenquelle kommt statt aus Texterkennung.
    """
    bereich = seitenbereich(pages)
    if not bereich:
        return None
    von, bis = bereich
    if abs((bis - von + 1) - anzahl) <= 2:
        return 1 - von
    return None


def kalibriere(texte: list[str]) -> int | None:
    """Versatz zwischen gedruckter Seitenzahl und PDF-Index bestimmen.

    Sucht in den Rand-Zeilen jeder Seite eine Seitenzahl und nimmt den Versatz,
    der am häufigsten auftritt. Bei Zeitschriftenartikeln steht die Zahl selten
    allein – typisch ist „907 R. Setola et al. / Journal …" –, deshalb wird
    nicht auf eine reine Zahlenzeile bestanden, sondern die erste beziehungsweise
    letzte Zahl der Randzeile genommen. Jahreszahlen (1900–2100) fallen raus,
    sonst kalibriert jede Fußzeile mit Copyright-Jahr falsch. Weniger als drei
    übereinstimmende Fundstellen gelten als nicht kalibrierbar – dann wird nicht
    geraten, sondern auf die Dokument-Suche ausgewichen (siehe `pruefe`).
    """
    stimmen: dict[int, int] = {}
    for i, t in enumerate(texte):
        zeilen = [z.strip() for z in t.split("\n") if z.strip()]
        for kandidat in zeilen[:2] + zeilen[-2:]:
            for zahl in re.findall(r"\b(\d{1,4})\b", kandidat[:40] + " " + kandidat[-40:]):
                gedruckt = int(zahl)
                if 1900 <= gedruckt <= 2100 or not 0 < gedruckt < len(texte) + 2000:
                    continue
                stimmen[(i + 1) - gedruckt] = stimmen.get((i + 1) - gedruckt, 0) + 1
    if not stimmen:
        return None
    versatz, treffer = max(stimmen.items(), key=lambda kv: kv[1])
    return versatz if treffer >= 3 else None


# ------------------------------------------------------------------- Vergleiche

def laengste_gemeinsame_folge(a: list[str], b: list[str], mindest: int) -> list[str]:
    """Längste zusammenhängende gemeinsame Wortfolge (leer, wenn < mindest)."""
    if len(a) < mindest or len(b) < mindest:
        return []
    index: dict[tuple[str, ...], list[int]] = {}
    for i in range(len(b) - mindest + 1):
        index.setdefault(tuple(b[i:i + mindest]), []).append(i)
    beste: list[str] = []
    for i in range(len(a) - mindest + 1):
        for j in index.get(tuple(a[i:i + mindest]), []):
            k = mindest
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            if k > len(beste):
                beste = a[i:i + k]
    return beste


def kernbegriffe(satz: str, n: int = 8) -> list[str]:
    kandidaten = [w for w in woerter(satz) if len(w) >= 5 and w not in STOPP]
    gesehen, out = set(), []
    for w in sorted(kandidaten, key=len, reverse=True):
        stamm = w[:6]
        if stamm not in gesehen:
            gesehen.add(stamm)
            out.append(w)
    return out[:n]


DE_MARKER = {"der", "die", "das", "und", "nicht", "eine", "werden", "sich", "ist",
             "auch", "für", "mit", "wird", "sind", "durch"}
EN_MARKER = {"the", "and", "of", "to", "in", "is", "are", "that", "for", "with",
             "this", "which", "be", "on", "by"}


def sprache(text: str) -> str:
    """Grobe Sprachkennung über Funktionswörter – reicht für die Frage, ob
    Trägersatz und Quelle überhaupt dieselbe Sprache sprechen."""
    w = woerter(text)
    if len(w) < 12:
        return "?"
    de = sum(1 for x in w if x in DE_MARKER)
    en = sum(1 for x in w if x in EN_MARKER)
    if de > en * 1.5:
        return "de"
    if en > de * 1.5:
        return "en"
    return "?"


def sprachwechsel(satz: str, seitentext: str) -> bool:
    """Deutscher Satz, englische Quelle (oder umgekehrt)? Dann kann der
    Begriffsabgleich nichts finden – und ein Seitenbefund daraus wäre ein
    Fehlalarm. Der Fall ist bei deutschsprachigen Arbeiten mit englischer
    Fachliteratur der Normalfall, nicht die Ausnahme."""
    a, b = sprache(satz), sprache(seitentext)
    return a != "?" and b != "?" and a != b


def treffer_auf_seite(begriffe: list[str], seitentext: str) -> int:
    norm = normalisiere(seitentext)
    return sum(1 for b in begriffe if b[:6] in norm)


def beste_seite(begriffe: list[str], texte: list[str]) -> tuple[int, int]:
    werte = [(treffer_auf_seite(begriffe, t), i) for i, t in enumerate(texte)]
    treffer, idx = max(werte) if werte else (0, 0)
    return idx, treffer


# ----------------------------------------------------------------- Zustand/IO

def lies_state(pfad: Path) -> dict:
    if pfad.exists():
        try:
            return json.loads(pfad.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"WARNUNG: {pfad} unlesbar – beginne mit leerem Stand.",
                  file=sys.stderr)
    return {"urteile": {}, "versatz": {}, "ausnahmen": []}


def schreib_state(pfad: Path, state: dict) -> None:
    pfad.write_text(json.dumps(state, ensure_ascii=False, indent=1),
                    encoding="utf-8")


def ortsangabe(z: Zitation) -> str:
    """Seite oder – bei E-Books – Kapitelnummer für Bericht/Prüfpaare."""
    if z.seite:
        return z.seite
    if z.kapitel:
        return f"Kap. {z.kapitel}"
    return "–"


def unreferenzierte_volltexte(bib: dict, root: Path) -> list[str]:
    """Volltexte in der Projektablage, die kein `file`-Feld nennt.

    Der billigste Hinweis auf den Fall aus P1-1: Die Datei liegt da, der
    Bib-Eintrag zeigt woanders hin. Nur melden, wenn tatsächlich etwas
    übrigbleibt – eine Liste, die bei jedem Lauf erscheint, wird überblättert.
    """
    genannt = {Path(p).name.lower()
               for e in bib.values() for p in gesetzte_dateipfade(e.get("file", ""))}
    # Nach Citekey benannte Dateien gehören zu ihrem Eintrag, auch wenn das
    # `file`-Feld woanders hinzeigt – sonst meldete jede korrekt abgelegte
    # Datei sich selbst als verwaist.
    genannt |= {f"{k.lower()}{e}" for k in bib for e in (".pdf", ".epub")}
    uebrig: list[str] = []
    for ordner in LITERATUR_ORDNER:
        d = root / ordner
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if (f.suffix.lower() in (".pdf", ".epub")
                    and f.name.lower() not in genannt):
                uebrig.append(f"{ordner}/{f.name}")
    return uebrig


# Anspruchsverlauf: Wird dieselbe Quelle an einer Stelle vorsichtig und an einer
# anderen absolut gebraucht? Bewusst grobe Wortlisten - das Skript entscheidet
# nichts, es legt die Saetze nebeneinander. Ob „belegt" an einer Stelle zu stark
# ist, haengt am Studiendesign der Quelle; das kann kein Regex.
STAERKEWOERTER = re.compile(
    r"(?<![\wäöüß])(belegt|belegen|beweist|beweisen|nachgewiesen|zeigt eindeutig|"
    r"bestätigt eindeutig|erwiesen)(?![\wäöüß])", re.I)
HEDGE_WOERTER = re.compile(
    r"(?<![\wäöüß])(stützt|deutet darauf|legt nahe|spricht dafür|könnte|dürfte|"
    r"tendenziell|Hinweise darauf|nicht belegt|belegt aber nicht)(?![\wäöüß])", re.I)


def vorfassung(z: Zitation, state: dict) -> str:
    """Der Trägersatz derselben Fundstelle aus einem früheren Lauf, falls vorhanden.

    Ändert sich ein Trägersatz, ändert sich sein Hash – das alte Urteil verfällt
    und die Zitation kommt als PRÜFEN zurück. Der Bericht zeigt dann nur den
    neuen Satz. Steht die Vorfassung daneben, ist die **Richtung** der Änderung
    sichtbar (abgeschwächt oder verschärft), und genau die entscheidet, ob das
    Zitat den Satz noch trägt: Wird ein Claim abgeschwächt, kann der Beleg zu
    stark werden – die Rahmung („stützt sich auf") behauptet dann mehr als der
    Satz selbst.
    """
    for h, e in state.get("saetze", {}).items():
        if h == z.hash:
            continue
        if e.get("key") == z.key and e.get("ort") == ortsangabe(z):
            return e.get("satz", "")
    return ""


def merke_saetze(zitate: list[Zitation], state: dict) -> None:
    """Trägersätze je Hash festhalten – Grundlage für `vorfassung()`."""
    state.setdefault("saetze", {})
    for z in zitate:
        state["saetze"][z.hash] = {"key": z.key, "ort": ortsangabe(z),
                                   "satz": z.satz.strip()[:400]}


def versatz_folgen(key: str, alt: int | None, neu: int, state: dict) -> list[str]:
    """Was ein neu gesetzter Seitenversatz mit bereits gebuchten Urteilen macht.

    Ein Urteil wird gegen die Seite gefällt, die der damalige Versatz aufgelöst
    hat – und danach nie wieder angesehen (`pruefe()` überspringt jedes OK, nur
    `--alle` bricht das auf). Ändert sich der Versatz, beruht das Urteil auf
    einer Seite, die das Skript heute anders auflöst. Es ist damit nicht
    „möglicherweise veraltet", sondern ungültig. Deshalb zwei Fälle:

    * **Erstsetzung** (vorher kein Versatz): nur warnen. Diese Urteile entstanden
      gegen das ganze Dokument – Inhalt und Wortlaut sind gedeckt, allein die
      Stellenangabe war nie bestätigt. Sie zurückzusetzen vernichtete geleistete
      Prüfarbeit, ohne dass etwas daran falsch wäre.
    * **Überschreiben mit einem anderen Wert**: Urteile löschen, sie kommen im
      nächsten Lauf als PRÜFEN zurück. Die alte Begründung wird mit ausgegeben,
      damit sie nach der Neuprüfung wiederverwendbar ist statt verloren zu sein.

    Anlass: Ein gespeicherter Versatz stand auf -8 statt 0 und fiel erst auf, als
    eine *neue* Zitation dadurch als „außerhalb des PDFs" gemeldet wurde. Er
    hätte genauso gut die *alten* Urteile unbemerkt falsch validieren können.

    Grundlage ist `state["saetze"]` (Hash → Key), das `merke_saetze()` bei jedem
    Lauf fortschreibt. Fehlt der Abschnitt – Stand aus einer älteren
    Skriptfassung –, bleibt die Meldung aus; der nächste reguläre Lauf legt ihn an.
    """
    if alt == neu:
        return []
    betroffen = [h for h, e in state.get("saetze", {}).items()
                 if e.get("key") == key and h in state.get("urteile", {})]
    if not betroffen:
        return []
    if alt is None:
        return [f"  WARNUNG: {len(betroffen)} bereits gebuchte(s) Urteil(e) zu "
                f"{key} entstanden ohne Versatz, also gegen das ganze Dokument. "
                f"Inhalt und Wortlaut sind gedeckt, die Seitenangabe nicht – für "
                f"die seitengenaue Nachprüfung: --alle",
                f"  Betroffen: {', '.join(betroffen)}"]
    zeilen = [f"  {len(betroffen)} Urteil(e) zu {key} zurückgesetzt "
              f"(Versatz {alt} → {neu}): gefällt gegen eine anders aufgelöste "
              f"Seite, kommen im nächsten Lauf als PRÜFEN zurück."]
    for h in betroffen:
        notiz = state["urteile"][h].get("notiz", "").strip()
        zeilen.append(f"    {h}  {notiz or '(ohne Begründung)'}")
        del state["urteile"][h]
    return zeilen


def anspruchsverlauf(zitate: list[Zitation], nur_auffaellig: bool = True) -> list[str]:
    """Alle Trägersätze einer mehrfach zitierten Quelle nebeneinander.

    Findet eine Fehlerklasse, die keine der übrigen Prüfungen finden *kann*:
    Die Arbeit begrenzt eine Quelle bei der Erstnutzung sauber („stützt die
    Entscheidung, belegt aber nicht die Wirkung") und lässt die Begrenzung im
    Fazit fallen („die belegte Wirksamkeit"). Jede Zitation für sich besteht
    den Volltextabgleich – die Drift entsteht zwischen ihnen. Sie entsteht
    systematisch, weil Fazitkapitel zuletzt und aus der Erinnerung entstehen.

    Standardmäßig still: gemeldet wird nur, wo an einer Fundstelle ein
    Stärkewort und an einer anderen desselben Keys ein Hedge steht. Die
    vollständige Liste liefert `--verlauf`.
    """
    nach_key: dict[str, list[Zitation]] = {}
    for z in zitate:
        nach_key.setdefault(z.key, []).append(z)

    ausgabe: list[str] = []
    for key in sorted(nach_key):
        gruppe = nach_key[key]
        if len(gruppe) < 2:
            continue
        stark = [z for z in gruppe if STAERKEWOERTER.search(z.satz)]
        hedge = [z for z in gruppe if HEDGE_WOERTER.search(z.satz)]
        auffaellig = bool(stark and hedge)
        if nur_auffaellig and not auffaellig:
            continue
        kopf = (f"[ANSPRUCHSVERLAUF] `{key}` – {len(gruppe)}× zitiert"
                + (", davon mit Stärkewort und mit Hedge: Wird die Quelle an "
                   "einer Stelle absoluter gebraucht als an der anderen? Die "
                   "Erstnutzung setzt die Obergrenze." if auffaellig else ""))
        zeilen = [kopf]
        for z in gruppe:
            marke = ("  ! " if z in stark else "  ~ " if z in hedge else "    ")
            zeilen.append(f"{marke}{Path(z.datei).name}:{z.zeile} "
                          f"[{ortsangabe(z)}] {z.satz.strip()[:220]}")
        ausgabe.append("\n".join(zeilen))
    return ausgabe


MAX_DUBLETTE_ZEILEN = 12


def zitat_dubletten(zitate: list[Zitation]) -> list[str]:
    """Dieselbe Quelle mit derselben Stelle zweimal binnen weniger Zeilen.

    Nicht falsch, aber inkonsistent – und teuer: Jede Änderung am Umfeld
    invalidiert beide Urteile statt einem. Typischer Entstehungsort sind
    Tabellenzellen, die einen Beleg wiederholen, der wenige Zeilen darüber im
    Fließtext schon steht. Ein `\\autoref` auf den Abschnitt tut dasselbe.
    """
    findings: list[str] = []
    nach_stelle: dict[tuple[str, str, str], list[Zitation]] = {}
    for z in zitate:
        nach_stelle.setdefault((z.datei, z.key, ortsangabe(z)), []).append(z)
    for (datei, key, ort), gruppe in sorted(nach_stelle.items()):
        if len(gruppe) < 2:
            continue
        gruppe.sort(key=lambda x: x.zeile)
        for a, b in zip(gruppe, gruppe[1:]):
            if b.zeile - a.zeile <= MAX_DUBLETTE_ZEILEN:
                findings.append(
                    f"[HINWEIS:ZITAT-DUBLETTE] `{key}` [{ort}] steht in "
                    f"{Path(datei).name} zweimal binnen "
                    f"{b.zeile - a.zeile} Zeilen (Z. {a.zeile} und {b.zeile}). "
                    f"Nicht falsch, aber jede Änderung am Umfeld invalidiert "
                    f"beide Urteile – die zweite Nennung durch einen "
                    f"\\autoref auf den Abschnitt ersetzen.")
    return findings


def notiz_warnungen(zitate: list[Zitation], bib: dict) -> list[str]:
    """Verrutschte Urteile sichtbar machen, solange sie noch billig sind.

    Ein einmal vergebenes OK wird nie wieder angesehen: `pruefe()` überspringt
    es vollständig, der Volltext wird nicht mehr geöffnet, und nur `--alle`
    bricht das auf. Die gespeicherte Notiz ist damit die einzige Spur, die
    überlebt – und genau die verrutscht, wenn Urteile blockweise über
    `--paare N` mit copy-and-paste eingetragen werden.

    Beides sind Hinweise, keine Befunde: Sie kosten keinen Score, machen den
    Eintragungsfehler aber sichtbar, bevor er endgültig wird.
    """
    warnungen: list[str] = []

    # (1) Dieselbe Begründung bei verschiedenen Werken. Bei zwei Zitationen
    #     DESSELBEN Werks ist eine gemeinsame Notiz legitim und bleibt still.
    nach_notiz: dict[str, list[Zitation]] = {}
    for z in zitate:
        if z.notiz.strip():
            nach_notiz.setdefault(normalisiere(z.notiz), []).append(z)
    for gruppe in nach_notiz.values():
        keys = {z.key for z in gruppe}
        if len(keys) > 1:
            erste = gruppe[0]
            for z in gruppe[1:]:
                if z.key != erste.key:
                    warnungen.append(
                        f"[NOTIZ-DUBLETTE] `{z.hash}` ({z.key}) trägt dieselbe "
                        f"Begründung wie `{erste.hash}` ({erste.key}) – beim "
                        f"Eintragen verrutscht? Urteil am Volltext gegenprüfen: "
                        f"--verdikt {z.hash}=PRÜFEN")

    # (2) Ein Autorname in der Notiz, den weder der Eintrag noch der Trägersatz
    #     kennt. Reine Zeichenkettenprüfung – hätte „Soma" in einer
    #     Vittuari-Notiz sofort gezeigt.
    namen = {k: re.findall(r"[A-ZÄÖÜ][a-zäöüß]{3,}",
                           bib.get(k, {}).get("author", "")) for k in bib}
    alle_namen = {n.lower() for liste in namen.values() for n in liste}
    for z in zitate:
        if not z.notiz.strip():
            continue
        eigene = {n.lower() for n in namen.get(z.key, [])}
        satz = normalisiere(z.satz)
        for wort in re.findall(r"[A-ZÄÖÜ][a-zäöüß]{3,}", z.notiz):
            w = wort.lower()
            if w in alle_namen and w not in eigene and w not in satz:
                warnungen.append(
                    f"[NOTIZ-FREMDER-AUTOR] `{z.hash}` ({z.key}): Die Notiz nennt "
                    f"„{wort}“ – weder im Autorenfeld dieses Eintrags noch im "
                    f"Trägersatz. Vermutlich die Begründung einer anderen Quelle.")
                break
    return warnungen


def bericht(zitate: list[Zitation], root: Path) -> str:
    offen = [z for z in zitate if z.status in STATUS_BEFUND | STATUS_OFFEN]
    ok = [z for z in zitate if z.status == "OK"]
    zeilen = [
        "# Quellencheck – Volltextabgleich aller Zitationen",
        "",
        f"Stand: {date.today():%d.%m.%Y} · {len(zitate)} Zitationen · "
        f"OK {len(ok)} · offen {len(offen)}",
        "",
        "> Erzeugt von `check_quellentreue.py`. Der Bericht wird pro Lauf "
        "überschrieben; die Urteile liegen in `quellencheck-state.json`. "
        "Statuswerte nie von Hand ändern – Urteil per "
        "`--verdikt <hash>=OK --notiz \"…\"` eintragen.",
        "",
    ]
    if offen:
        zeilen += ["## Offen", "",
                   "| Hash | Stelle | Quelle | S./Kap. | Status | Befund |",
                   "|---|---|---|---|---|---|"]
        for z in offen:
            stelle = f"{Path(z.datei).name}:{z.zeile}"
            zeilen.append(f"| `{z.hash}` | {stelle} | `{z.key}` | {ortsangabe(z)} "
                          f"| **{z.status}** | {z.befund or ''} |")
        zeilen.append("")
    if ok:
        zeilen += ["## Fundstelle geprüft", "",
                   "> **Geprüft ist hier Fundstelle und Wortlaut, nicht die "
                   "Reichweite.** Diese Zitationen stehen so in der Quelle – ob "
                   "die Quelle die Behauptung auch in der *Stärke* trägt, in der "
                   "der Satz sie aufstellt, beantwortet die Gegenlesung "
                   "(Prüferfrage 3), nicht dieser Lauf.", "",
                   "| Hash | Stelle | Quelle | S./Kap. | Notiz |", "|---|---|---|---|---|"]
        for z in ok:
            stelle = f"{Path(z.datei).name}:{z.zeile}"
            zeilen.append(f"| `{z.hash}` | {stelle} | `{z.key}` | {ortsangabe(z)} "
                          f"| {z.notiz or ''} |")
        zeilen.append("")
    return "\n".join(zeilen) + "\n"


def seite_ausserhalb_pages(seite: str, pages: str) -> tuple[int, int, int] | None:
    """Liegt eine zitierte Seite außerhalb der Spanne im `pages`-Feld?

    Reine Feldprüfung, kein Volltext nötig – greift deshalb auch bei Quellen
    ohne hinterlegtes PDF. Zielt auf einen Fehler, der sich systematisch
    einschleicht: Repositorien (White Rose, arXiv, PMC, ResearchGate) liefern
    Preprint-Fassungen, deren Zählung bei 1 beginnt, während der Bib-Eintrag
    die Verlagsseiten trägt. Wer die Seite aus dem gelesenen Preprint abschreibt,
    zitiert eine Seite, die es in der genannten Publikation nicht gibt.

    Liefert (zitierte Seite, von, bis) oder None. `pages` ohne echten Bereich
    (Artikelnummern, Einzelseiten, Bücher) ergibt nie einen Befund.
    """
    bereich = seitenbereich(pages)
    if not bereich or not seite:
        return None
    von, bis = bereich
    for v, b in seiten_liste(seite):
        for wert in {v, b}:
            if wert < von or wert > bis:
                return (wert, von, bis)
    return None


# ------------------------------------------------------------------ Hauptlauf

def pruefe(zitate: list[Zitation], bib: dict, state: dict, root: Path,
           mindest: int, alle: bool) -> None:
    cache: dict[str, object] = {}
    ausnahmen = [normalisiere(a) for a in state.get("ausnahmen", [])]
    for z in zitate:
        alt = state["urteile"].get(z.hash)
        if alt and alt.get("status") == "RENTIERT NICHT":
            z.status = "RENTIERT NICHT"
            z.befund = (alt.get("notiz") or
                        "Fundstelle deckt, das Zitat trägt den Satz aber nicht mehr – "
                        "Rahmung streichen oder Beleg ersetzen.")
            continue
        if alt and not alle and alt.get("status") in ("OK", "AUSNAHME"):
            z.status, z.notiz = alt["status"], alt.get("notiz", "")
            continue
        eintrag = bib.get(z.key)
        if eintrag is None:
            z.status, z.befund = "NICHT GEFUNDEN", "Key fehlt in references.bib"
            continue

        # Vor allem anderen, weil ohne Volltext entscheidbar: Passt die
        # Seitenangabe überhaupt zu der Spanne, die der Eintrag ausweist?
        drauss = seite_ausserhalb_pages(z.seite, eintrag.get("pages", ""))
        if drauss:
            wert, von, bis = drauss
            z.status = "SEITE AUSSERHALB"
            z.befund = (f"S. {wert} liegt außerhalb der laut `pages` zitierten "
                        f"Spanne {von}–{bis} – in der genannten Publikation gibt "
                        f"es diese Seite nicht. Typisch beim Lesen einer "
                        f"Preprint-/Repositoriumsfassung mit eigener Zählung: "
                        f"maßgeblich ist die Verlagsfassung. Steht sie nicht zur "
                        f"Verfügung, [Abs. X] oder [Kap. X] statt der Seite.")
            continue

        pdf = pdf_pfad(eintrag.get("file", ""), root, z.key)
        epub = (None if pdf is not None
                else epub_pfad(eintrag.get("file", ""), root, z.key))
        if pdf is None and epub is None:
            gesetzt = gesetzte_dateipfade(eintrag.get("file", ""))
            if gesetzt:
                # Eigene Klasse: Der Volltext ist hinterlegt, nur der Pfad
                # stimmt nicht. Vorher bekam dieser Fall dieselbe Meldung wie
                # ein fehlendes file-Feld – ein Audit hat daraus einmal einen
                # −15-Befund „Quellen ohne Volltext" gebaut und damit die
                # Prüfung genau dort abgeschaltet, wo sie gegriffen hätte.
                z.status = "DATEI NICHT GEFUNDEN"
                z.befund = (
                    f"`file`-Feld gesetzt, Datei nicht gefunden: {gesetzt[0]} – "
                    f"auch nicht als {Path(gesetzt[0]).name} in "
                    f"{' oder '.join(o + '/' for o in LITERATUR_ORDNER)}. Volltext "
                    f"dorthin kopieren oder den Pfad korrigieren; nicht als "
                    f"fehlende Quelle werten.")
            elif (klasse := zugangsklasse(eintrag)) == "VOLLTEXT BESCHAFFBAR":
                z.status = klasse
                z.befund = (
                    f"Buch/Sammelband ohne hinterlegten Volltext – besorgen und "
                    f"als {LITERATUR_ORDNER[0]}/{z.key}.pdf (oder .epub) ablegen. "
                    f"Der Dateiname nach Citekey ist der einzige Bezug, den ein "
                    f"BBT-Export nicht überschreibt. Vor der Abgabe erledigen.")
            elif klasse == "ZUGANG PRÜFEN":
                z.status = klasse
                ziel = eintrag.get("doi") or eintrag.get("url", "")
                z.befund = (
                    f"Volltext hinter einer Bezahlschranke, kein Snapshot – hier "
                    f"hilft kein Download-Klick. Reihenfolge: (1) freie Fassung "
                    f"über OpenAlex suchen (api.openalex.org/works/doi:{ziel}), "
                    f"(2) IU-Bibliothek über myCampus, (3) Quelle ersetzen. Bei "
                    f"einer Preprint-Fassung die gelesene Fassung vermerken – "
                    f"deren Seitenzählung weicht von der Verlagsfassung ab.")
            elif eintrag.get("url"):
                z.status = "LIVE PRÜFEN"
                z.befund = ("kein PDF-Snapshot im file-Feld – Webquelle live "
                            f"prüfen: {eintrag['url']}")
            else:
                z.status = "NICHT PRÜFBAR"
                z.befund = "weder PDF (file) noch URL im Bib-Eintrag"
            continue

        quelle_ist_epub = pdf is None
        index_von_nummer: dict[str, int] = {}
        if quelle_ist_epub:
            try:
                cached = cache.get(str(epub))
                texte, index_von_nummer = cached if cached is not None else epub_kapitel(epub)
            except Exception as e:  # unlesbares/unerwartet strukturiertes EPUB
                z.status, z.befund = "NICHT PRÜFBAR", f"E-Book nicht lesbar ({e})"
                continue
            cache[str(epub)] = (texte, index_von_nummer)
            if not any(t.strip() for t in texte):
                z.status = "NICHT PRÜFBAR"
                z.befund = ("E-Book ohne auswertbares Inhaltsverzeichnis (nur "
                            "nummerierte NCX-Kapitel werden unterstützt)")
                continue
        else:
            try:
                texte = cache.get(str(pdf)) or seiten_texte(pdf)
            except ImportError:
                print("FEHLER: pdfplumber fehlt – 'pip install pdfplumber'.",
                      file=sys.stderr)
                raise SystemExit(2)
            except Exception as e:  # defektes/verschlüsseltes PDF
                z.status, z.befund = "NICHT PRÜFBAR", f"PDF nicht lesbar ({e})"
                continue
            cache[str(pdf)] = texte
            if not any(t.strip() for t in texte):
                z.status = "NICHT PRÜFBAR"
                z.befund = "PDF ohne Textebene (Scan) – OCR nötig oder manuell prüfen"
                continue

        ohne_versatz = False
        if quelle_ist_epub:
            # Kein Seitenversatz zu kalibrieren – die Kapitelnummer wird direkt
            # gegen das eigene Inhaltsverzeichnis des E-Books aufgelöst.
            if z.kapitel:
                idx, gefunden_nr = resolve_kapitel(z.kapitel, index_von_nummer)
                if idx is not None:
                    seitentext = texte[idx]
                    gedruckt = (f"Kap. {z.kapitel}" if gefunden_nr == z.kapitel else
                                f"Kap. {z.kapitel} (Inhaltsverzeichnis löst nur bis "
                                f"Kap. {gefunden_nr} auf)")
                else:
                    ohne_versatz = True
                    seitentext = "\n".join(texte)
                    gedruckt = f"Kap. {z.kapitel} (im Inhaltsverzeichnis nicht gefunden)"
            else:
                ohne_versatz = True
                seitentext = "\n".join(texte)
                gedruckt = ("werkbezogen" if not z.seite else
                            f"S. {z.seite} (E-Book ohne Seitenzahlen – [Kap. X] verwenden)")
        elif z.kapitel:
            # PDF, aber mit [Kap. X] statt [S. X] zitiert (z. B. eingescanntes
            # Buch ohne verlässlich erkennbare Kapitelgrenzen). Kapitelgenau
            # lässt sich das ohne TOC-Extraktion wie beim epub nicht auflösen –
            # dieselbe Ausweich-Logik wie bei unkalibrierbaren PDF-Seiten:
            # gegen das ganze Dokument prüfen, die Stelle bleibt unbestätigt.
            ohne_versatz = True
            seitentext = "\n".join(texte)
            gedruckt = f"Kap. {z.kapitel} (PDF – Kapitelgrenzen nicht bestimmbar)"
        elif not z.seite:
            seitentext = "\n".join(texte)
            gedruckt = "werkbezogen"
        else:
            versatz = state["versatz"].get(z.key)
            if versatz is None:
                # Kein `or`: Versatz 0 ist ein gültiges Ergebnis (Artikel, dessen
                # gedruckte Seite 1 die erste PDF-Seite ist) und darf nicht als
                # „nichts gefunden" durchfallen.
                versatz = versatz_aus_pages(eintrag.get("pages", ""), len(texte))
                if versatz is None:
                    versatz = kalibriere(texte)
                if versatz is not None:
                    state["versatz"][z.key] = versatz
            if versatz is None:
                # Seitenversatz unbekannt (typisch bei Artikel-PDFs ohne
                # erkennbare Paginierung). Kein Abbruch: Wortlaut und Begriffe
                # werden gegen das **ganze** Dokument geprüft – eine wörtliche
                # Übernahme bleibt eine, egal auf welcher Seite sie steht. Nur
                # die Seitenangabe selbst bleibt maschinell unbestätigt.
                ohne_versatz = True
                seitentext = "\n".join(texte)
                gedruckt = f"S. {z.seite} (Versatz unbekannt)"
            else:
                # Jede genannte Seite einzeln auflösen – auch die Komma-Form
                # „S. 12, 34" (Zitierleitfaden 2.2.1) trägt mehrere Fundstellen.
                bloecke: list[str] = []
                ausserhalb: int | None = None
                for von_g, bis_g in seiten_liste(z.seite):
                    von = von_g + versatz - 1
                    bis = bis_g + versatz - 1
                    if not (0 <= von < len(texte)):
                        ausserhalb = von_g
                        break
                    bloecke.append("\n".join(texte[von:min(bis + 1, len(texte))]))
                if ausserhalb is not None:
                    bereich = seitenbereich(eintrag.get("pages", ""))
                    zusatz = ""
                    if bereich and ausserhalb <= len(texte):
                        # Klassischer Fehler: die PDF-interne Seite zitiert statt
                        # der gedruckten. Dann ist die richtige Angabe ausrechenbar.
                        zusatz = ("; sieht nach PDF-interner Zählung aus – gedruckt "
                                  f"wäre das S. {bereich[0] + ausserhalb - 1} "
                                  f"(Artikel: S. {bereich[0]}–{bereich[1]})")
                    z.status = "SEITE VERDÄCHTIG"
                    z.befund = (f"S. {ausserhalb} liegt außerhalb des PDFs "
                                f"({len(texte)} Seiten, Versatz {versatz}){zusatz}")
                    continue
                seitentext = "\n".join(bloecke)
                gedruckt = f"S. {z.seite}"
        z.seitentext = seitentext
        stelle = z.seite or z.kapitel  # Locator-agnostischer Wahrheitswert für die Checks unten
        nummer_von_index = {v: k for k, v in index_von_nummer.items()}

        def fundstelle_label(idx: int) -> str:
            if quelle_ist_epub:
                return f"Kap. {nummer_von_index[idx]}" if idx in nummer_von_index else f"Abschnitt {idx + 1}"
            return f"S. {idx + 1 - state['versatz'].get(z.key, 0)}"

        # 1) Wörtliches Zitat muss exakt stehen – abzüglich der Eingriffe, die
        #    der Zitierleitfaden erlaubt (Klammern, Auslassungen).
        if z.woertlich:
            zitat = woerter(z.woertlich)
            quelle_w = woerter(seitentext)
            segmente = zitat_segmente(z.woertlich)
            if segmente:
                fehlend = [s for s in segmente if not enthaelt_folge(s, quelle_w)]
                gefunden_n = sum(len(s) for s in segmente if s not in fehlend)
                vollstaendig = not fehlend
            else:
                # Zu kurz oder nur Klammerinhalt – auf den alten Weg zurückfallen.
                gefunden = laengste_gemeinsame_folge(zitat, quelle_w,
                                                     min(mindest, len(zitat)))
                gefunden_n, vollstaendig = len(gefunden), len(gefunden) >= len(zitat)
            if not vollstaendig:
                if len(zitat) < MIN_ZITAT_WOERTER:
                    # Kurze Anführung dicht vor dem Beleg: Kurzzitat oder doch
                    # Begriffsanführung? Mechanisch nicht entscheidbar – und ein
                    # blockierender Befund wäre für diesen Zweifelsfall zu scharf.
                    z.status = "PRÜFEN"
                    z.befund = (f"kurze Anführung ({len(zitat)} Wörter) steht so nicht "
                                f"in {gedruckt} – Kurzzitat (dann Wortlaut oder Seite "
                                f"korrigieren) oder Begriffsanführung (dann in Ordnung)? "
                                f"Im semantischen Schritt entscheiden")
                    continue
                z.status = "ZITAT WEICHT AB"
                z.befund = (f"wörtliches Zitat ({len(zitat)} Wörter) steht so nicht "
                            f"in {gedruckt}; {gefunden_n} von {len(zitat)} Wörtern "
                            f"gefunden. Klammer-Eingriffe ([sic], Ergänzungen, "
                            f"Hervorhebungs-Hinweise) und Auslassungen sind beim "
                            f"Vergleich bereits herausgerechnet – die Abweichung "
                            f"liegt im Zitattext selbst")
                continue
            z.status = "PRÜFEN"
            z.befund = ("wörtliches Zitat exakt gefunden – Seitenangabe bestätigen"
                        + (" (Seite maschinell nicht prüfbar, Versatz unbekannt)"
                           if ohne_versatz else ""))
            continue

        # 2) Wortlautübernahme in Paraphrasen – gekennzeichnete Zitate zählen nicht mit
        folge = laengste_gemeinsame_folge(woerter(ohne_zitattext(z.satz)),
                                          woerter(seitentext), mindest)
        if folge and not any(" ".join(folge) in a for a in ausnahmen):
            z.status = "WORTLAUT"
            z.befund = (f"{len(folge)} Wörter wörtlich übernommen: "
                        f"„{' '.join(folge)}" + "“ – umformulieren oder als Zitat "
                        "kennzeichnen")
            continue

        # 3) Passt die Seitenangabe (bzw. bei E-Books: die Kapitelangabe)?
        begriffe = kernbegriffe(z.satz)
        if stelle and begriffe and sprachwechsel(z.satz, seitentext):
            # Deutscher Satz, englische Quelle: Der Begriffsabgleich kann hier
            # nichts leisten. Kein Befund erfinden – der semantische Schritt
            # entscheidet, der Sprachen vergleichen kann.
            z.status = "PRÜFEN"
            z.befund = (f"Sprachwechsel Text/Quelle – Seitenangabe {gedruckt} "
                        "maschinell nicht prüfbar, im semantischen Schritt "
                        "mitprüfen")
            continue
        if stelle and begriffe and treffer_auf_seite(begriffe, seitentext) == 0:
            if ohne_versatz:
                # Gegen das ganze Dokument geprüft: Kommt kein Kernbegriff vor,
                # ist die Aussage in dieser Quelle überhaupt nicht zu finden –
                # ein stärkerer Befund als eine bloß falsche Seitenzahl.
                z.status = "NICHT GEFUNDEN"
                z.befund = ("kein Kernbegriff des Satzes im gesamten Dokument – "
                            "Quelle oder Aussage prüfen")
                continue
            idx, treffer = beste_seite(begriffe, texte)
            hinweis = (f"; Begriffe stehen am ehesten in {fundstelle_label(idx)} "
                       f"({treffer} Treffer)") if treffer else ""
            z.status = "SEITE VERDÄCHTIG"
            z.befund = f"kein Kernbegriff des Satzes auf {gedruckt}{hinweis}"
            continue

        z.status = "PRÜFEN"
        if ohne_versatz and quelle_ist_epub:
            idx, treffer = beste_seite(begriffe, texte) if begriffe else (0, 0)
            hinweis = f" (Begriffe am ehesten in {fundstelle_label(idx)})" if treffer else ""
            z.befund = (f"inhaltlich plausibel, aber {gedruckt} maschinell nicht "
                        f"bestätigt{hinweis}. Seitenangabe im semantischen Schritt "
                        f"mitprüfen oder direkt lesen: --seite {z.key} "
                        f"{z.kapitel or '<Kap.-Nummer>'}")
        elif ohne_versatz and z.kapitel:
            # PDF mit [Kap. X]-Locator ohne bestimmbare Kapitelgrenzen (siehe oben).
            idx, treffer = beste_seite(begriffe, texte) if begriffe else (0, 0)
            hinweis = f" (Begriffe am ehesten auf PDF-Seite {idx + 1})" if treffer else ""
            z.befund = (f"inhaltlich plausibel, aber {gedruckt} maschinell nicht "
                        f"bestätigt{hinweis}. Seitenangabe im semantischen Schritt "
                        f"mitprüfen oder gezielt lesen: --seite {z.key} <Seitenzahl>")
        elif ohne_versatz:
            idx, treffer = beste_seite(begriffe, texte) if begriffe else (0, 0)
            z.befund = (f"inhaltlich plausibel, aber S. {z.seite} maschinell nicht "
                        f"bestätigt (Seitenversatz unbekannt; Begriffe am ehesten "
                        f"auf PDF-Seite {idx + 1}). Seitenangabe im semantischen "
                        f"Schritt mitprüfen oder Versatz setzen: "
                        f"--offset {z.key}=<n>")
        else:
            z.befund = f"mechanisch unauffällig – Inhaltsdeckung auf {gedruckt} prüfen"


def zeige_seite(key: str, seite: str, bib: dict, state: dict, root: Path) -> int:
    """Den Text einer zitierten Seite ausgeben – für den Schreibschritt, der
    den Satz aus der Quelle heraus formulieren soll, statt ihn hinterher zu
    prüfen. Kein Prüflauf, kein Bericht, kein Zustand wird geschrieben."""
    eintrag = bib.get(key)
    if eintrag is None:
        print(f"FEHLER: Key '{key}' fehlt in references.bib.", file=sys.stderr)
        return 2
    pdf = pdf_pfad(eintrag.get("file", ""), root, key)
    if pdf is None:
        epub = epub_pfad(eintrag.get("file", ""), root, key)
        if epub is None:
            ziel = eintrag.get("url") or "kein Volltext im Bib-Eintrag"
            print(f"Kein PDF/E-Book im file-Feld. Webquelle: {ziel}", file=sys.stderr)
            return 2
        try:
            texte, index_von_nummer = epub_kapitel(epub)
        except Exception as e:
            print(f"FEHLER: E-Book nicht lesbar ({e}).", file=sys.stderr)
            return 2
        idx, gefunden_nr = resolve_kapitel(str(seite), index_von_nummer)
        if idx is None:
            print(f"Kap. {seite} nicht im Inhaltsverzeichnis gefunden – gebe das "
                  f"ganze E-Book aus ({len(texte)} erkannte Kapitel).",
                  file=sys.stderr)
            print("\n".join(texte)[:12000])
            return 0
        hinweis = "" if gefunden_nr == str(seite) else f" (nur bis Kap. {gefunden_nr} aufgelöst)"
        print(f"=== {key} · Kap. {seite}{hinweis} ===")
        print(texte[idx])
        return 0
    try:
        texte = seiten_texte(pdf)
    except Exception as e:
        print(f"FEHLER: PDF nicht lesbar ({e}).", file=sys.stderr)
        return 2
    versatz = state["versatz"].get(key)
    if versatz is None:
        versatz = versatz_aus_pages(eintrag.get("pages", ""), len(texte))
    if versatz is None:
        versatz = kalibriere(texte)
    if versatz is None:
        print(f"Seitenversatz unbekannt – gebe das ganze Dokument aus "
              f"({len(texte)} Seiten). Für seitengenaues Lesen: "
              f"--offset {key}=<n>", file=sys.stderr)
        print("\n".join(" ".join(s.split()) for s in texte)[:12000])
        return 0
    bereiche = seiten_liste(str(seite)) or [(int(str(seite).split("-")[0]),) * 2]
    ausgegeben = 0
    for von_g, bis_g in bereiche:
        for gedruckt in range(von_g, bis_g + 1):
            i = gedruckt + versatz - 1
            if not (0 <= i < len(texte)):
                print(f"FEHLER: S. {gedruckt} liegt außerhalb des PDFs "
                      f"({len(texte)} Seiten, Versatz {versatz}).", file=sys.stderr)
                if not ausgegeben:
                    return 2
                continue
            print(f"=== {key} · gedruckte S. {gedruckt} · "
                  f"PDF-Seite {i + 1}/{len(texte)} ===")
            print(" ".join(texte[i].split()))
            ausgegeben += 1
    return 0 if ausgegeben else 2


PAAR_MIN_ZEICHEN = 1200   # Untergrenze: darunter wird nie gekürzt
PAAR_MAX_ZEICHEN = 3000   # Obergrenze auch im ungekürzten Fall
PAAR_RAND = 400           # Kontext links und rechts um den äußersten Treffer


def ausschnitt(seitentext: str, begriffe: list[str]) -> tuple[str, bool]:
    """Den Teil der Quellseite herausschneiden, der die Kernbegriffe enthält.

    Bei 40+ Zitationen ist der Seitentext der größte Einzelposten des Audits.
    Gekürzt wird aber nur, wo es sicher ist: Der Ausschnitt umspannt **alle**
    Treffer (nicht nur den besten), behält PAAR_RAND Zeichen Kontext auf beiden
    Seiten und unterschreitet PAAR_MIN_ZEICHEN nie. Ohne Treffer wird nicht
    geraten, sondern der Anfang der Seite ausgegeben.

    Rückgabe: (Text, gekuerzt?) – der Aufrufer weist die Kürzung sichtbar aus,
    damit ein Urteil nie unbemerkt auf zu wenig Kontext beruht.
    """
    text = seitentext.strip()
    if len(text) <= PAAR_MIN_ZEICHEN:
        return text, False
    tief = text.lower()
    positionen = [p for b in begriffe if (p := tief.find(b[:6])) >= 0]
    if not positionen:
        return text[:PAAR_MAX_ZEICHEN], len(text) > PAAR_MAX_ZEICHEN
    start, ende = min(positionen) - PAAR_RAND, max(positionen) + PAAR_RAND
    start, ende = max(0, start), min(len(text), ende)
    if ende - start < PAAR_MIN_ZEICHEN:            # auf die Untergrenze dehnen
        # Erst nach links, dann nach rechts – und was auf einer Seite am Rand
        # verloren geht, wird auf der anderen nachgeholt. Ohne diesen zweiten
        # Schritt blieb ein Treffer am Seitenanfang oder -ende unter der
        # Untergrenze, weil die halbe Erweiterung ins Leere lief.
        fehlt = PAAR_MIN_ZEICHEN - (ende - start)
        links = min(start, fehlt // 2)
        start -= links
        ende = min(len(text), ende + (fehlt - links))
        if ende - start < PAAR_MIN_ZEICHEN:
            start = max(0, ende - PAAR_MIN_ZEICHEN)
    ende = min(ende, start + PAAR_MAX_ZEICHEN)
    return text[start:ende], (start > 0 or ende < len(text))


def paare_ausgeben(zitate: list[Zitation], anzahl: int, voll: bool = False) -> None:
    """Prüfpaare für den semantischen Schritt (Trägersatz + Quellenausschnitt)."""
    offen = [z for z in zitate if z.status == "PRÜFEN"][:anzahl]
    for z in offen:
        print("\n" + "=" * 70)
        print(f"HASH {z.hash} · {z.datei}:{z.zeile} · {z.key} · {ortsangabe(z)}")
        print("--- Trägersatz ---")
        print(z.satz.strip()[:1200])
        if voll:
            quelle, gekuerzt = z.seitentext.strip()[:12000], False
        else:
            quelle, gekuerzt = ausschnitt(z.seitentext, kernbegriffe(z.satz))
        print("--- Quelle (zitierte Seite) ---")
        print(quelle or "(kein Text)")
        if gekuerzt:
            print(f"[gekürzt auf den Bereich um die Kernbegriffe. Reicht der "
                  f"Ausschnitt für das Urteil nicht: --paare N --voll, oder "
                  f"gezielt die ganze Stelle mit "
                  f"--seite {z.key} "
                  f"{z.seite.split(',')[0] if z.seite else (z.kapitel or '<n>')}]")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--datei", default="chapters",
                    help="Datei oder Verzeichnis (Default: chapters/)")
    ap.add_argument("--bib", default="references.bib")
    ap.add_argument("--bericht", default="quellencheck.md")
    ap.add_argument("--state", default="quellencheck-state.json")
    ap.add_argument("--min-words", type=int, default=7,
                    help="Wortlaut-Schwelle (Default 7)")
    ap.add_argument("--alle", action="store_true",
                    help="auch bereits mit OK quittierte Zitationen neu prüfen")
    ap.add_argument("--paare", type=int, default=0,
                    help="N Prüfpaare (Trägersatz + Quellenausschnitt) ausgeben")
    ap.add_argument("--voll", action="store_true",
                    help="Prüfpaare mit vollem Seitentext statt Ausschnitt "
                         "(wenn der Ausschnitt für das Urteil nicht reicht)")
    ap.add_argument("--verdikt", action="append", default=[],
                    metavar="HASH=STATUS",
                    help="Urteil setzen: OK · AUSNAHME · \"RENTIERT NICHT\" "
                         "(Fundstelle deckt, das Zitat trägt den Satz aber nicht "
                         "mehr – bleibt als Befund stehen)")
    ap.add_argument("--notiz", action="append", default=[],
                    help="Begründung zum Urteil – positionsweise zu --verdikt; "
                         "bei mehreren --verdikt genauso oft angeben")
    ap.add_argument("--offset", action="append", default=[], metavar="KEY=N",
                    help="Seitenversatz einer Quelle manuell setzen")
    ap.add_argument("--ausnahme", action="append", default=[],
                    help="Wortfolge dauerhaft vom Wortlaut-Test ausnehmen")
    ap.add_argument("--verlauf", action="store_true",
                    help="Anspruchsverlauf für ALLE mehrfach zitierten Quellen "
                         "ausgeben, nicht nur für die auffälligen")
    ap.add_argument("--seite", nargs=2, metavar=("KEY", "SEITE"),
                    help="nur den Text der zitierten Seite ausgeben (zum Lesen "
                         "beim Schreiben) – kein Prüflauf, kein Bericht. Bei "
                         "E-Books (epub) die Kapitelnummer angeben, z. B. 17.2.2")
    a = ap.parse_args()

    # `--notiz` ist positionsgebunden: Notiz i begründet Urteil i. Früher war es
    # ein Einzelwert, der für ALLE Urteile desselben Aufrufs galt – zwei
    # `--verdikt` mit zwei `--notiz` bekamen beide die zuletzt genannte
    # Begründung. Das bleibt unbemerkt, weil ein einmal vergebenes OK nie wieder
    # angesehen wird (nur `--alle` bricht das auf) und die Notiz seine einzige
    # überlebende Spur ist. Deshalb hier abbrechen statt raten: Eine gemeinsame
    # Notiz für mehrere Urteile ist nicht als Kürzel zu retten – sie ist genau
    # der Fall, der die Fehlzuordnung erzeugt hat.
    if a.verdikt and len(a.notiz) not in (0, len(a.verdikt)):
        print(f"FEHLER: {len(a.verdikt)}× --verdikt, aber {len(a.notiz)}× --notiz. "
              f"Je Urteil eine eigene Begründung angeben (oder gar keine) – eine "
              f"Notiz für mehrere Urteile würde stillschweigend falsch zugeordnet.",
              file=sys.stderr)
        return 2
    if a.notiz and not a.verdikt:
        print("FEHLER: --notiz ohne --verdikt – die Begründung hätte kein Ziel.",
              file=sys.stderr)
        return 2

    root = Path(".").resolve()
    buchung = bool(a.verdikt or a.offset or a.ausnahme)
    state_pfad = Path(a.state)
    state = lies_state(state_pfad)

    for eintrag in a.offset:
        key, _, wert = eintrag.partition("=")
        key, neu = key.strip(), int(wert)
        alt = state["versatz"].get(key)
        state["versatz"][key] = neu
        print(f"OK: Seitenversatz {key} = {neu}")
        for zeile in versatz_folgen(key, alt, neu, state):
            print(zeile)
    for wortfolge in a.ausnahme:
        state.setdefault("ausnahmen", []).append(wortfolge)
        print(f"OK: Ausnahme ergänzt – „{wortfolge}“")
    for i, eintrag in enumerate(a.verdikt):
        h, _, status = eintrag.partition("=")
        status = status.strip().upper() or "OK"
        # „RENTIERT NICHT" schliesst eine Ausdruckslücke: Die Fundstelle deckt,
        # aber das Zitat traegt den Satz nicht mehr – etwa weil der Claim
        # abgeschwaecht wurde und die Rahmung („stuetzt sich auf") jetzt mehr
        # behauptet als der Satz selbst. Ohne diesen Wert musste so ein Fall
        # zwangslaeufig als OK gebucht werden und verschwand damit.
        if status not in ("OK", "AUSNAHME", "RENTIERT NICHT"):
            print(f"FEHLER: Status '{status}' unzulässig "
                  f"(OK, AUSNAHME oder 'RENTIERT NICHT').", file=sys.stderr)
            return 2
        state["urteile"][h.strip()] = {"status": status,
                                       "notiz": a.notiz[i] if a.notiz else "",
                                       "datum": f"{date.today():%Y-%m-%d}"}
        print(f"OK: Urteil {h.strip()} = {status}")

    bib_pfad = Path(a.bib)
    if not bib_pfad.exists():
        print(f"FEHLER: {bib_pfad} nicht gefunden.", file=sys.stderr)
        return 2

    if a.seite:
        return zeige_seite(a.seite[0], a.seite[1], lies_bib(bib_pfad), state, root)
    ziel = Path(a.datei)
    pfade = sorted(ziel.rglob("*.tex")) if ziel.is_dir() else [ziel]
    if not pfade:
        print(f"FEHLER: keine .tex-Dateien unter {ziel}.", file=sys.stderr)
        return 2

    zitate = lies_tex(pfade)
    if not zitate:
        print("Keine Zitationen gefunden – nichts zu prüfen.")
        schreib_state(state_pfad, state)
        return 0
    bib = lies_bib(bib_pfad)
    pruefe(zitate, bib, state, root, a.min_words, a.alle)
    for z in zitate:
        if z.status == "PRÜFEN" and (alt := vorfassung(z, state)):
            z.befund = ((z.befund + " · ") if z.befund else "") + (
                f"**Trägersatz geändert.** Vorfassung: „{alt}“ – Richtung der "
                f"Änderung prüfen: Deckt die Fundstelle noch, **und** trägt sie "
                f"den Satz in seiner jetzigen Stärke, oder ist er inzwischen "
                f"eigene Setzung? Falls Letzteres: "
                f"--verdikt {z.hash}=\"RENTIERT NICHT\"")
    merke_saetze(zitate, state)
    schreib_state(state_pfad, state)
    Path(a.bericht).write_text(bericht(zitate, root), encoding="utf-8")

    zaehler: dict[str, int] = {}
    for z in zitate:
        zaehler[anzeige(z.status)] = zaehler.get(anzeige(z.status), 0) + 1
    print(f"\n{len(zitate)} Zitationen in {len(pfade)} Datei(en) · Bericht: {a.bericht}")
    for status in sorted(zaehler):
        print(f"  {status:<20} {zaehler[status]}")
    for block in anspruchsverlauf(zitate, nur_auffaellig=not a.verlauf):
        print(f"\n{block}")
    for w in zitat_dubletten(zitate):
        print(f"\n{w}")
    for w in notiz_warnungen(zitate, bib):
        print(f"\n{w}")
    uebrig = unreferenzierte_volltexte(bib, root)
    if uebrig:
        print(f"\nVolltexte ohne Bib-Verweis ({len(uebrig)}): "
              f"{', '.join(uebrig[:6])}{' …' if len(uebrig) > 6 else ''}\n"
              f"  Liegt hier der Volltext zu einer als DATEI NICHT GEFUNDEN "
              f"gemeldeten Quelle, ist es ein Pfad- und kein Quellenproblem.")
    if a.paare:
        paare_ausgeben(zitate, a.paare, a.voll)
    offen = sum(v for k, v in zaehler.items() if k in STATUS_BEFUND | STATUS_OFFEN)
    if offen:
        print(f"\n{offen} Zitation(en) offen – Befunde abarbeiten, "
              "Prüfpaare mit --paare abrufen, Urteile mit --verdikt eintragen.")
    if buchung:
        # Eintragen von Urteil, Versatz oder Ausnahme ist eine Buchung, kein
        # Prüflauf: Sie ist gelungen, sobald sie geschrieben wurde. Würde hier
        # der Torwert zurückgegeben, sähe jede einzelne Buchung in der
        # Oberfläche nach einem Fehlschlag aus, solange irgendetwas offen ist.
        return 0
    return 1 if offen else 0


if __name__ == "__main__":
    sys.exit(main())
