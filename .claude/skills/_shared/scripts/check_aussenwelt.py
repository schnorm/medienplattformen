#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unzitierte Behauptungen über die reale Außenwelt einsammeln.

Die Lücke, die dieses Skript schließt: **Ein Satz ohne Zitation existiert für
keinen anderen Prüfschritt.** `check_quellentreue.py` (Teil-Check G) sieht nur
Sätze mit `\\cite`; der `stresstest` prüft nur Kernargumente, und sein
Verifikations-Gate greift erst, wenn ein Argument auf einer Außenweltbehauptung
ruht; `check_autoref.py` prüft nur interne Verweise. Eine Tatsachenbehauptung
über ein reales Produkt, eine Institution oder eine Zahl, die ohne Beleg
danebensteht, fällt durch alle drei Netze.

Betroffen sind vor allem beschreibende Textklassen, die legitim ohne Zitation
auskommen (Marktüberblick, Wettbewerbs- und Produktanalyse, Werkzeug- und
Systembeschreibung, Praxiskontext einer Fallorganisation). Genau ihre
Zitationsfreiheit macht ihre Fakten unsichtbar – ohne sie von der
Wahrheitspflicht zu befreien. Erschwerend:
Die Welt bewegt sich, der Text nicht. Ministerien werden umbenannt, Produkte
bekommen Funktionen, die der Text ihnen abspricht; ein Satz, der beim Schreiben
stimmte, kann bei der Abgabe falsch sein, ohne dass sich ein Zeichen geändert
hat.

Was das Skript **nicht** tut: recherchieren oder urteilen. Es sammelt Kandidaten
ein und merkt sich, welche schon beurteilt wurden. Die Verifikation macht der
`faktencheck`-Skill in einer eigenen, kalten Sitzung – ein Skript kann nicht ins
Web sehen, und ein Modell mit Projektkontext übernimmt zu leicht das „schon
geprüft" früherer Runden.

## Warum der Filter am Absatz hängt, nicht am Satz

Der teuerste reale Fund dieser Klasse lautete: „Für Resteverwertung bietet die
Plattform zwar Rezeptsammlungen zu einzelnen Zutaten, aber **kein Werkzeug**,
das aus mehreren vorhandenen Resten Vorschläge ableitet." Dieser Satz enthält
keinen Eigennamen, keine Zahl, keine Domain – nur „die Plattform". Ein reiner
Satzfilter hätte ihn verfehlt, und er war es, der die Kernabgrenzung der ganzen
Arbeit trug.

Deshalb zwei Ebenen: **Träger** ist der Absatz, **Kandidat** ist der Satz.
Nennt ein Absatz irgendwo eine reale Entität (Domain, Produktname in
Binnenmajuskel, Rechtsform, Behörden-/Institutionswort), gelten **alle** seine
unzitierten Sätze als Kandidaten – auch die anaphorischen. Außerhalb solcher
Absätze wird ein Satz nur bei einem eigenen, harten Signal zum Kandidaten
(Prozent-, Jahres- oder Mengenangabe, Domain, Binnenmajuskel).

Sätze **mit** Zitation werden übersprungen: Für die ist Teil-Check G zuständig,
und doppelte Zuständigkeit erzeugt doppelte Arbeit ohne zusätzlichen Fund.
Ebenso ausgenommen ist zitierter Fremdtext (`\\enquote{}`, `blockzitat`) – dort
steht die Formulierung der Quelle, nicht die des Verfassers.

## Warum der Zustand mitgeführt wird

Ohne State-Datei wäre der Check bei jedem Audit gleich teuer und würde bald
übersprungen – genau das ist dem optionalen Gesamt-Stresstest schon passiert.
Ein einmal beurteilter Satz bleibt still, bis er sich ändert. Das Verdikt
`EIGENE SETZUNG` sorgt dafür, dass eigene Konzept- und Produktnamen (die wie
Entitäten aussehen, aber keine Außenweltbehauptung sind) dauerhaft ruhig
bleiben, statt jede Runde neu aufzuschlagen.

Nutzung (vom Projekt-Root):
    python .claude/skills/_shared/scripts/check_aussenwelt.py
    python .claude/skills/_shared/scripts/check_aussenwelt.py --datei chapters/02_haupt
    python .claude/skills/_shared/scripts/check_aussenwelt.py --alle
    python .claude/skills/_shared/scripts/check_aussenwelt.py \
        --verdikt <hash>=BESTÄTIGT --notiz "chefkoch.de/wochenplaner, Stand 31.07.2026"

Verdikte: `BESTÄTIGT` (an einer Quelle verifiziert) · `WIDERLEGT` (Befund –
der Text stimmt nicht) · `NICHT VERIFIZIERBAR` (recherchiert, keine belastbare
Quelle; bleibt sichtbar und gehört in „Bitte manuell prüfen") · `EIGENE SETZUNG`
(keine Außenweltbehauptung, sondern eigene Definition/Benennung).
`BESTÄTIGT` verlangt `--notiz` mit dem Beleg: Ein Häkchen ohne Fundstelle ist
beim nächsten Lauf wertlos.

Ergebnis: `faktencheck-state.json` (Urteile, überdauern Läufe – nicht von Hand
editieren). Den Bericht schreibt der `faktencheck`-Skill, nicht dieses Skript.

Exit-Code 0 = keine offenen Kandidaten · 1 = offene Kandidaten oder Befunde ·
2 = Ausführungsfehler. Buchungen (`--verdikt`) geben 0 zurück.
"""

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

# Eine Definition von „Satz" und „normalisiert" im ganzen Skriptsatz – siehe
# check_autoref.py für die Begründung.
try:
    from check_quellentreue import (CITE_CMD_RE, SATZENDE_RE, normalisiere,
                                    ohne_struktur)
except ImportError:  # pragma: no cover
    print("FEHLER: check_quellentreue.py nicht neben diesem Skript gefunden.",
          file=sys.stderr)
    raise SystemExit(2)

# Gliederungsbefehle gehoeren nicht in den Kandidatensatz - sonst steht die
# Ueberschrift im Bericht und im Hash, und ein umbenanntes Kapitel setzt
# jedes Urteil darin zurueck.
GLIEDERUNG_RE = re.compile(r"\\(?:sub)*section\*?{[^}]*}")
ENQUOTE_RE = re.compile(r"\\enquote\{((?:[^{}]|\{[^{}]*\})*)\}")
BLOCKZITAT_RE = re.compile(r"\\begin\{blockzitat\}.*?\\end\{blockzitat\}", re.S)
KOMMENTAR_RE = re.compile(r"(?<!\\)%.*")

# `% SICHTUNG: …` – die Selbstdeklaration aus `schreib-modus`. Sie ist hier
# **kein Tor, sondern eine Rangfolge**: Ein Kapitel, das sich als eigene Sichtung
# deklariert, hat besonders viele unbelegte Aussenweltaussagen und wird zuerst
# geprueft. Der Filter laeuft trotzdem ueber alle Kapitel – genau die Datei, an
# die niemand gedacht hat, ist der Fall, fuer den P36 ueberhaupt entstanden ist.
# `check_formalia.py` wertet denselben Marker aus (dort: check_sichtungskapitel),
# meldet aber nur die Saetze; die Verifikation und der Zustand liegen hier.
SICHTUNG_RE = re.compile(r"%[ \t]*SICHTUNG\b:?[ \t]*(.*)")   # kein \s: das fraesse den Zeilenumbruch

# --------------------------------------------------------------- Signalklassen
# „Stark" heißt: benennt eine reale, nachschlagbare Entität. Diese Signale
# machen den ganzen Absatz zum Träger.
DOMAIN_RE = re.compile(
    r"\b[a-z0-9][\w-]*\.(?:de|com|app|org|net|eu|io|gov|edu|at|ch)\b", re.I)
# Binnenmajuskel: TikTok, YouTube, SuperCook, LinkedIn, foodsharing→Foodsharing.
# Trifft keine normalen deutschen Substantive, weil die nur vorn groß sind.
BINNENMAJUSKEL_RE = re.compile(r"\b[A-ZÄÖÜ][a-zäöüß]+[A-ZÄÖÜ][a-zA-ZäöüßÄÖÜ]+\b")
RECHTSFORM_RE = re.compile(
    r"(?:\be\.\s?V\.|\bGmbH\b|\bAG\b|\bSE\b|\bKG\b|\bmbH\b|\bInc\.|\bLtd\.)")
INSTITUTION_RE = re.compile(
    r"\b(?:Bundes(?:ministerium|amt|anstalt|behörde)\w*|Ministerium\w*|"
    r"Kommission|Verband|Verein|Institut|Stiftung|Universität|Hochschule|"
    r"Bundesregierung|Europäische[nrs]?\s+Union|Vereinte[nr]?\s+Nationen)\b")

# „Hart" heißt: nachprüfbare Größe, unabhängig vom Absatz.
PROZENT_RE = re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:%|Prozent)\b")
JAHR_RE = re.compile(r"\b(?:19|20)\d{2}\b")
MENGE_RE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s*(?:Mio\.|Mrd\.|Millionen|Milliarden|Tsd\.|Tausend|"
    r"Euro|EUR|€|Dollar|USD)\b")

STARKE_SIGNALE = {
    "DOMAIN": DOMAIN_RE,
    "PRODUKTNAME": BINNENMAJUSKEL_RE,
    "RECHTSFORM": RECHTSFORM_RE,
    "INSTITUTION": INSTITUTION_RE,
}
HARTE_SIGNALE = {
    "PROZENT": PROZENT_RE,
    "JAHRESZAHL": JAHR_RE,
    "MENGE": MENGE_RE,
}

# Absolutheits- und Verneinungsmarker. Allein kein Signal – ein Satz wird
# dadurch nicht zum Kandidaten. Sie werden nur mitgemeldet, weil sie die
# Behauptung angreifbar machen: „bietet kein X" ist widerlegt, sobald es
# irgendwo ein X gibt, während „bietet wenig X" kaum je falsch ist.
ABSOLUT_RE = re.compile(
    r"(?<![\wäöüß])(kein|keine|keinen|keiner|keinem|nicht|nie|niemals|"
    r"ausschließlich|einzig|einzige[rsnm]?|erstmals|als erste[rs]?|"
    r"vollständig|sämtliche)(?![\wäöüß])", re.I)

STATUS_BEFUND = {"WIDERLEGT"}
STATUS_OFFEN = {"NEU", "PRÜFEN", "NICHT VERIFIZIERBAR"}
STATUS_ERLEDIGT = {"BESTÄTIGT", "EIGENE SETZUNG"}
VERDIKTE = STATUS_BEFUND | STATUS_ERLEDIGT | {"NICHT VERIFIZIERBAR"}

# Dateien, die selbst geschriebenen, bewerteten Text enthalten. `acronyms.tex`
# steht bewusst dabei: Die Langform eines Akronyms ist eine Tatsachenbehauptung
# über eine reale Institution – die Umbenennung eines Ministeriums schlägt genau
# dort auf, und niemand liest das Abkürzungsverzeichnis noch einmal.
ZUSATZ_DATEIEN = ("pages/appendix.tex", "pages/acronyms.tex",
                  "pages/abstract.tex")


@dataclass
class Kandidat:
    datei: str
    zeile: int
    satz: str
    signale: list[str]
    absolut: list[str]
    sichtung: str = ""
    status: str = "NEU"
    notiz: str = ""

    @property
    def hash(self) -> str:
        return hashlib.sha1(
            normalisiere(self.satz).encode("utf-8")).hexdigest()[:10]


def maskiere(text: str) -> str:
    """Zitierten Fremdtext und Kommentare durch Leerzeichen ersetzen.

    Länge und damit alle Positionen bleiben erhalten – sonst zeigten die
    Zeilennummern ins Leere.
    """
    def leer(m: re.Match) -> str:
        return " " * (m.end() - m.start())
    text = KOMMENTAR_RE.sub(leer, text)
    text = BLOCKZITAT_RE.sub(leer, text)
    return ENQUOTE_RE.sub(leer, text)


def absaetze(text: str) -> list[tuple[int, int]]:
    """Absatzgrenzen als (start, ende). Leerzeile trennt, wie in LaTeX."""
    grenzen, start = [], 0
    for m in re.finditer(r"\n[ \t]*\n", text):
        grenzen.append((start, m.start()))
        start = m.end()
    grenzen.append((start, len(text)))
    return [(a, b) for a, b in grenzen if text[a:b].strip()]


def saetze_in(text: str, von: int, bis: int) -> list[tuple[int, str]]:
    """(Startposition, Satz) für einen Bereich. Zitierbefehle sind maskiert."""
    ausschnitt = text[von:bis]
    treffer, start = [], 0
    for m in SATZENDE_RE.finditer(ausschnitt):
        treffer.append((von + start, ausschnitt[start:m.end()].strip()))
        start = m.end()
    if ausschnitt[start:].strip():
        treffer.append((von + start, ausschnitt[start:].strip()))
    return [(p, s) for p, s in treffer if s]


def signale_in(text: str, muster: dict[str, re.Pattern]) -> list[str]:
    return sorted(name for name, r in muster.items() if r.search(text))


def zeile_von(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def tex_dateien(wurzel: Path, ziel: str) -> list[Path]:
    pfad = wurzel / ziel
    if pfad.is_file():
        return [pfad]
    if not pfad.is_dir():
        return []
    return sorted(p for p in pfad.rglob("*.tex"))


def sammle(wurzel: Path, ziel: str) -> tuple[list[Kandidat], list[str]]:
    """Kandidaten und die Liste der Dateien **ohne** Kandidaten.

    Die zweite Liste ist kein Beiwerk: „kein Fund" und „nicht geprüft" sind
    verschiedene Aussagen, und nur die erste darf im Bericht als Entlastung
    stehen.
    """
    kandidaten: list[Kandidat] = []
    ohne: list[str] = []
    pfade = list(tex_dateien(wurzel, ziel))
    for rel in ZUSATZ_DATEIEN:
        p = wurzel / rel
        if p.is_file() and p not in pfade:
            pfade.append(p)

    for pfad in pfade:
        try:
            roh = pfad.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        text = maskiere(roh)
        rel = pfad.relative_to(wurzel).as_posix()
        m = SICHTUNG_RE.search(roh)
        sichtung = (m.group(1).strip() or "deklariert") if m else ""
        vorher = len(kandidaten)
        for von, bis in absaetze(text):
            absatz = text[von:bis]
            traeger = signale_in(absatz, STARKE_SIGNALE)
            for pos, satz in saetze_in(text, von, bis):
                # Sätze mit Zitation gehören Teil-Check G.
                if CITE_CMD_RE.search(satz):
                    continue
                eigen = signale_in(satz, STARKE_SIGNALE) + \
                    signale_in(satz, HARTE_SIGNALE)
                # Außerhalb eines Träger-Absatzes zählt nur ein eigenes Signal.
                if not eigen and not traeger:
                    continue
                # Geerbte Signale mit „~" kennzeichnen: Der Satz selbst nennt
                # nichts Nachschlagbares, der Absatz schon – das ist der Fall
                # „die Plattform bietet kein Werkzeug".
                signale = eigen or [f"~{s}" for s in traeger]
                # Strukturbefehle raus: In einer Float-Umgebung steht kein
                # Satzschlusspunkt, der ganze Block gilt also als ein Satz.
                # Ohne die Bereinigung liest der Bericht sich als LaTeX-Dump.
                kandidaten.append(Kandidat(
                    rel, zeile_von(text, pos),
                    " ".join(ohne_struktur(GLIEDERUNG_RE.sub(" ", satz)).split()),
                    signale,
                    sorted({a.lower() for a in ABSOLUT_RE.findall(satz)}),
                    sichtung))
        if len(kandidaten) == vorher:
            ohne.append(rel)
    # Ein Satz kann in mehreren Läufen identisch auftauchen (Wiederholung im
    # Fazit): einmal führen, sonst wird derselbe Fakt doppelt recherchiert.
    einmalig: dict[str, Kandidat] = {}
    for k in kandidaten:
        einmalig.setdefault(k.hash, k)
    # Deklarierte Sichtungskapitel zuerst – dort sitzt die hoechste Trefferdichte.
    return (sorted(einmalig.values(),
                   key=lambda k: (not k.sichtung, k.datei, k.zeile)), ohne)


def lies_state(pfad: Path) -> dict:
    if pfad.exists():
        try:
            return json.loads(pfad.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"WARNUNG: {pfad} unlesbar – beginne mit leerem Stand.",
                  file=sys.stderr)
    return {"urteile": {}}


def schreib_state(pfad: Path, state: dict) -> None:
    pfad.write_text(json.dumps(state, ensure_ascii=False, indent=1),
                    encoding="utf-8")


def bewerte(kandidaten: list[Kandidat], state: dict) -> None:
    urteile = state.setdefault("urteile", {})
    for k in kandidaten:
        eintrag = urteile.get(k.hash)
        if not eintrag:
            k.status = "NEU"
            continue
        k.status = eintrag.get("status", "NEU")
        k.notiz = eintrag.get("notiz", "")


def buche(state: dict, kandidaten: list[Kandidat], vorgaben: list[str],
          notiz: str) -> int:
    nach_hash = {k.hash: k for k in kandidaten}
    fehler = 0
    for vorgabe in vorgaben:
        if "=" not in vorgabe:
            print(f"FEHLER: --verdikt erwartet <hash>=<URTEIL>, bekam "
                  f"'{vorgabe}'.", file=sys.stderr)
            fehler += 1
            continue
        h, urteil = (t.strip() for t in vorgabe.split("=", 1))
        urteil = urteil.upper()
        if urteil not in VERDIKTE:
            print(f"FEHLER: '{urteil}' ist kein Verdikt "
                  f"({', '.join(sorted(VERDIKTE))}).", file=sys.stderr)
            fehler += 1
            continue
        k = nach_hash.get(h)
        if not k:
            print(f"FEHLER: kein Kandidat mit Hash '{h}' im aktuellen Lauf.",
                  file=sys.stderr)
            fehler += 1
            continue
        # Ein BESTÄTIGT ohne Beleg ist die Behauptung, recherchiert zu haben.
        # Beim nächsten Lauf steht dann nichts da, woran sich das nachprüfen
        # ließe – und genau dieses „schon geprüft" hat die realen Fehler
        # überleben lassen.
        if urteil == "BESTÄTIGT" and not notiz.strip():
            print(f"FEHLER: '{h}=BESTÄTIGT' braucht --notiz mit dem Beleg "
                  f"(Quelle, Stand).", file=sys.stderr)
            fehler += 1
            continue
        state.setdefault("urteile", {})[h] = {
            "status": urteil,
            "notiz": notiz.strip(),
            "stelle": f"{k.datei}:{k.zeile}",
            "satz": k.satz[:200],
            "datum": f"{date.today():%Y-%m-%d}",
        }
        print(f"gebucht: {h} = {urteil}"
              + (f" – {notiz.strip()}" if notiz.strip() else ""))
    return fehler


def aufraeumen(state: dict, kandidaten: list[Kandidat]) -> int:
    lebend = {k.hash for k in kandidaten}
    urteile = state.setdefault("urteile", {})
    tot = [h for h in urteile if h not in lebend]
    for h in tot:
        del urteile[h]
    return len(tot)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Unzitierte Außenweltbehauptungen einsammeln (kein Urteil).")
    ap.add_argument("--datei", default="chapters",
                    help="Datei oder Ordner; pages/appendix.tex und "
                         "pages/acronyms.tex kommen immer dazu")
    ap.add_argument("--state", default="faktencheck-state.json")
    ap.add_argument("--alle", action="store_true",
                    help="auch bereits beurteilte Kandidaten auflisten")
    ap.add_argument("--verdikt", action="append", default=[],
                    metavar="HASH=URTEIL",
                    help=f"Urteil buchen ({', '.join(sorted(VERDIKTE))})")
    ap.add_argument("--notiz", default="", help="Beleg zum Urteil")
    args = ap.parse_args()

    wurzel = Path.cwd()
    kandidaten, ohne = sammle(wurzel, args.datei)
    state_pfad = wurzel / args.state
    state = lies_state(state_pfad)

    if args.verdikt:
        bewerte(kandidaten, state)
        fehler = buche(state, kandidaten, args.verdikt, args.notiz)
        schreib_state(state_pfad, state)
        return 2 if fehler else 0

    bewerte(kandidaten, state)
    entfernt = aufraeumen(state, kandidaten)
    # Keine Kandidaten und nichts gespeichert heisst: nichts zu merken. Ohne
    # diese Bedingung legte jeder Probelauf in einer frischen Vorlage eine leere
    # State-Datei an, die dann als Projektartefakt mitgeschleppt wird.
    if kandidaten or state.get("urteile") or state_pfad.exists():
        schreib_state(state_pfad, state)

    offen = [k for k in kandidaten if k.status in STATUS_OFFEN]
    befunde = [k for k in kandidaten if k.status in STATUS_BEFUND]
    fertig = [k for k in kandidaten if k.status in STATUS_ERLEDIGT]

    print(f"{len(kandidaten)} Kandidaten · offen {len(offen)} · "
          f"Befunde {len(befunde)} · beurteilt {len(fertig)}")
    if entfernt:
        print(f"{entfernt} Urteil(e) zu entfallenen Sätzen aufgeräumt.")
    for k in befunde + offen:
        marker = f" [absolut: {', '.join(k.absolut)}]" if k.absolut else ""
        vorrang = f"  [SICHTUNG: {k.sichtung}]" if k.sichtung else ""
        print(f"\n  {k.status:<20} {k.hash}  {k.datei}:{k.zeile}{vorrang}")
        print(f"    Signale: {', '.join(k.signale)}{marker}")
        print(f"    {k.satz[:300]}")
        if k.notiz:
            print(f"    Notiz: {k.notiz}")
    if args.alle:
        for k in fertig:
            print(f"\n  {k.status:<20} {k.hash}  {k.datei}:{k.zeile}")
            print(f"    {k.satz[:200]}")
            if k.notiz:
                print(f"    Beleg: {k.notiz}")
    if ohne:
        print("\nDateien ohne Kandidaten (kein Fund, nicht „nichts geprüft“): "
              + ", ".join(ohne))
    if offen or befunde:
        print("\nVerifikation ist Sache des `faktencheck`-Skills (kalte "
              "Sitzung, Websuche je Kandidat). Urteil buchen mit "
              "--verdikt <hash>=BESTÄTIGT --notiz \"…\"")
        return 1
    print("\nAlle Kandidaten beurteilt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
