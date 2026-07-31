#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interne Querverweise: meldet Paare, bei denen sich eine Seite bewegt hat.

Aufruf (vom Projekt-Root):
    python .claude/skills/_shared/scripts/check_autoref.py
    python .claude/skills/_shared/scripts/check_autoref.py --datei chapters/02_theorie
    python .claude/skills/_shared/scripts/check_autoref.py --paare 8
    python .claude/skills/_shared/scripts/check_autoref.py --alle
    python .claude/skills/_shared/scripts/check_autoref.py --verdikt <hash>=OK --notiz "..."

**Das Problem.** Ein zitiertes PDF ändert sich nie. Das Ziel eines
`\\autoref{sec:…}` ist dagegen ein eigenes Kapitel, das laufend umgeschrieben
wird. Wird die Zielstelle beim Kürzen abgeschwächt, bleibt der darauf gestützte
Satz in einem ganz anderen Kapitel unverändert stehen – und niemand liest beim
Kürzen von Kapitel 2.2 nach, wer aus Kapitel 2.4 darauf zeigt. Teil-Check C
fragt nur, ob an der Zielstelle der behauptete Inhalt steht (Fundstelle), nicht,
ob sie ihn in der behaupteten **Stärke** trägt (Reichweite) – genau die
Unterscheidung, die Teil-Check G für externe Quellen ausdrücklich trifft.

**Was das Skript tut und was nicht.** Es entscheidet **nichts** inhaltlich. Es
hasht beide Seiten jedes Verweispaares und meldet die Paare, bei denen sich seit
dem letzten Urteil etwas geändert hat. Ob die Zielstelle den Satz noch trägt,
beurteilt der `pruef-modus` (Teil-Check C) – dieses Skript sagt nur, wo
hinzusehen ist. Damit wird aus einer Prüfung über alle Verweise eine über die
wenigen bewegten.

**Warum das Ziel-Fenster eng ist.** Gehasht wird nicht die ganze Ziel-Subsection,
sondern der Absatz mit dem `\\label` plus der folgende. Das ist die Lehre aus dem
Trägersatz-Problem in `check_quellentreue.py` (P16/P19): Ein zu breites Fenster
wird von jeder Änderung im Umfeld invalidiert, eine einzige Kürzungsrunde wirft
dann alle Verweise gleichzeitig auf PRÜFEN – und ein Check, der nach jeder
Überarbeitung zwanzig Fehlalarme produziert, wird beim zweiten Mal übersprungen.

**Warum die Identität nicht am Satztext hängt.** Das Paar wird über (Datei,
Label, laufende Nummer) identifiziert, nicht über einen Hash des verweisenden
Satzes. Sonst wäre ein geänderter Satz ein *neues* Paar, das gespeicherte Urteil
verwaiste im State, und der Bericht meldete `NEU` statt
`VERWEISENDER SATZ GEÄNDERT` – der Fall, für den das Skript gebaut ist.

**Zielarten.** `sec:`-Labels bekommen das Absatzfenster oben. `tab:`- und
`fig:`-Labels bekommen die **Float-Umgebung**, in der sie stehen: Eine geänderte
Tabellenzelle zieht die Sätze mit, die aus ihr etwas ableiten – belegt an einer
Wettbewerbsmatrix, deren Korrektur an einer Zelle drei Folgesätze nachzog.
Verweise auf eine `sec:`-Stelle in **derselben** Datei entfallen: Dort wäre der
verweisende Satz oft Teil seines eigenen Ziels. Float-Verweise in derselben
Datei bleiben – der übliche „wie \\autoref{tab:x} zeigt"-Satz vor der Tabelle
ist genau der Fall, der überwacht gehört.

Verdikte: `OK` (Fundstelle **und** Reichweite geprüft – verlangt `--notiz`) ·
`RENTIERT NICHT` (die Zielstelle trägt den Satz in dieser Stärke nicht mehr;
der Befund bleibt stehen).

Ergebnis: `autorefcheck.md` (Bericht, pro Lauf überschrieben) und
`autoref-state.json` (Urteile, überdauern Läufe – nicht von Hand editieren).

Exit-Code 0 = keine offenen Paare · 1 = mindestens ein Paar offen.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

STATE_NAME = "autoref-state.json"
BERICHT_NAME = "autorefcheck.md"
REF_RE = re.compile(r"\\(?:autoref|ref|nameref)\{((?:sec|tab|fig):[\w:-]+)\}")
LABEL_RE = re.compile(r"\\label\{((?:sec|tab|fig):[\w:-]+)\}")
FLOAT_RE = re.compile(r"\\begin\{(table|figure|longtable)(\*?)\}.*?\\end\{\1\2\}", re.S)

# Gewichtungsmarker im verweisenden Satz: Dort entsteht die Reichweiten-Differenz.
MARKER_RE = re.compile(
    r"\b(vor allem|in erster Linie|hauptsächlich|überwiegend|primär|maßgeblich|"
    r"die Stärke|der Kern|der wichtigste|die wichtigste|das wichtigste|zentral|"
    r"ausschließlich|ausnahmslos|lediglich|einzig|allein|jede[rs]?|alle|nur|"
    r"stets|immer|belegt|beweist)\b", re.I)

# Zusatzdateien, in denen Labels stehen können. `pages/appendix.tex` ist der
# Regelfall: Ein `\autoref{tab:persona}` zeigt fast immer dorthin. Ohne diese
# Zeile meldete jeder Anhangsverweis „ZIEL FEHLT" – ein Fehlalarm, der das
# Skript unbrauchbar macht.
ZUSATZ_LABELDATEIEN = ("pages/appendix.tex",)

STATUS_OK = "OK"
STATUS_BEFUND = "RENTIERT NICHT"
VERDIKTE = (STATUS_OK, STATUS_BEFUND)


def kommentare_weg(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def normalisieren(text: str) -> str:
    """Whitespace vereinheitlichen – sonst ändert jede Umformatierung den Hash."""
    return re.sub(r"\s+", " ", text).strip()


def kurz_hash(*teile: str) -> str:
    h = hashlib.sha1("\x00".join(teile).encode("utf-8"))
    return h.hexdigest()[:10]


def saetze(absatz: str) -> list[str]:
    """Grobe Satztrennung. Genauigkeit ist zweitrangig: Entscheidend ist, dass
    dieselbe Eingabe immer dieselbe Zerlegung ergibt (Hash-Stabilität)."""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", absatz) if s.strip()]


def absaetze_mit_position(text: str) -> list[tuple[int, str]]:
    """(Startoffset, Absatztext) – Absätze sind durch Leerzeilen getrennt."""
    aus, pos = [], 0
    for teil in re.split(r"\n\s*\n", text):
        aus.append((pos, teil))
        pos += len(teil) + 2
    return aus


def float_spannen(text: str) -> list[tuple[int, int, str]]:
    return [(m.start(), m.end(), m.group(0)) for m in FLOAT_RE.finditer(text)]


def sammle_labels(dateien: list[Path], wurzel: Path) -> dict[str, tuple[str, str, str]]:
    """label -> (Datei, Art, Ziel-Fenster).

    Art ist „Subsection" (Fenster = Absatz mit dem `\\label` + der folgende) oder
    „Float" (Fenster = die ganze table/figure-Umgebung). Doppelt vergebene Labels
    gewinnt das zuletzt gelesene – wie in LaTeX auch.
    """
    ziele: dict[str, tuple[str, str, str]] = {}
    for p in dateien:
        text = kommentare_weg(p.read_text(encoding="utf-8", errors="replace"))
        rel = p.relative_to(wurzel).as_posix()
        floats = float_spannen(text)
        absaetze = absaetze_mit_position(text)
        for m in LABEL_RE.finditer(text):
            label = m.group(1)
            umgebend = next((f for f in floats if f[0] <= m.start() < f[1]), None)
            if umgebend:
                ziele[label] = (rel, "Float", normalisieren(umgebend[2]))
                continue
            for i, (off, absatz) in enumerate(absaetze):
                if off <= m.start() < off + len(absatz) + 2:
                    fenster = absatz
                    if i + 1 < len(absaetze):
                        fenster += "\n\n" + absaetze[i + 1][1]
                    ziele[label] = (rel, "Subsection", normalisieren(fenster))
                    break
    return ziele


# Gliederungsbefehle gehören nicht in den Trägersatz: Sonst hängt der Hash an der
# Überschrift, und ein umbenanntes Kapitel invalidiert jeden Verweis darin.
GLIEDERUNG_RE = re.compile(r"\\(?:sub)*section\*?\{[^}]*\}|\\label\{[^}]*\}")


def sammle_verweise(dateien: list[Path], wurzel: Path,
                    ziele: dict[str, tuple[str, str, str]] | None = None) -> list[dict]:
    """Je Verweis: Datei, Zeile, Label, verweisender Satz, laufende Nummer.

    Die laufende Nummer je (Datei, Label) bildet zusammen mit beiden die
    **Identität** des Paares – siehe Modul-Docstring.
    """
    ziele = ziele or {}
    aus = []
    for p in dateien:
        text = kommentare_weg(p.read_text(encoding="utf-8", errors="replace"))
        rel = p.relative_to(wurzel).as_posix()
        zaehler: dict[str, int] = {}
        for offset, absatz in absaetze_mit_position(text):
            if not REF_RE.search(absatz):
                continue
            for satz in saetze(absatz):
                labels = REF_RE.findall(satz)
                if not labels:
                    continue
                zeile = text[:offset].count("\n") + 1
                traeger = normalisieren(GLIEDERUNG_RE.sub(" ", satz))
                for label in labels:
                    ziel = ziele.get(label)
                    # Selbstverweis auf die eigene Subsection: Der verweisende
                    # Satz wäre Teil seines eigenen Ziels, jede Änderung an der
                    # Datei invalidierte das Paar ohne Erkenntnisgewinn.
                    if ziel and ziel[1] == "Subsection" and ziel[0] == rel:
                        continue
                    zaehler[label] = zaehler.get(label, 0) + 1
                    aus.append({"datei": rel, "zeile": zeile, "label": label,
                                "nr": zaehler[label], "satz": traeger})
    return aus


def lade_state(pfad: Path) -> dict:
    if not pfad.is_file():
        return {}
    try:
        return json.loads(pfad.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print(f"HINWEIS: {pfad.name} nicht lesbar – wird neu angelegt.", file=sys.stderr)
        return {}


def schreibe_state(pfad: Path, state: dict) -> None:
    pfad.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")


def paare_bilden(verweise: list[dict],
                 ziele: dict[str, tuple[str, str, str]]) -> list[dict]:
    paare = []
    for v in verweise:
        ident = kurz_hash(v["datei"], v["label"], str(v["nr"]))
        ziel = ziele.get(v["label"])
        if ziel is None:
            paare.append({**v, "status": "ZIEL FEHLT", "hash": ident,
                          "zieldatei": None, "zielart": None,
                          "quelle_hash": kurz_hash(v["satz"]), "ziel_hash": ""})
            continue
        zieldatei, art, fenster = ziel
        paare.append({**v, "zieldatei": zieldatei, "zielart": art,
                      "quelle_hash": kurz_hash(v["satz"]),
                      "ziel_hash": kurz_hash(fenster),
                      "hash": ident, "status": None})
    return paare


def bewerte(paare: list[dict], state: dict, alle: bool) -> None:
    for p in paare:
        if p["status"] == "ZIEL FEHLT":
            continue
        alt = state.get(p["hash"])
        if alt is None:
            p["status"] = "NEU"
        elif alle:
            p["status"] = "PRÜFEN (erzwungen)"
        elif alt.get("quelle_hash") != p["quelle_hash"] and alt.get("ziel_hash") != p["ziel_hash"]:
            p["status"] = "BEIDE SEITEN GEÄNDERT"
        elif alt.get("quelle_hash") != p["quelle_hash"]:
            p["status"] = "VERWEISENDER SATZ GEÄNDERT"
        elif alt.get("ziel_hash") != p["ziel_hash"]:
            p["status"] = "ZIELSTELLE GEÄNDERT"
        else:
            p["status"] = alt.get("verdikt") or "PRÜFEN"
        p["notiz"] = (alt or {}).get("notiz", "")


def aufraeumen(state: dict, paare: list[dict]) -> int:
    """Urteile zu Paaren entfernen, die es nicht mehr gibt."""
    lebend = {p["hash"] for p in paare}
    tot = [h for h in state if h not in lebend]
    for h in tot:
        del state[h]
    return len(tot)


def marker_von(satz: str) -> list[str]:
    return sorted({m.lower() for m in MARKER_RE.findall(satz)})


def bericht(paare: list[dict]) -> str:
    offen = [p for p in paare if p["status"] != STATUS_OK]
    ok = [p for p in paare if p["status"] == STATUS_OK]
    z = [
        "# Autoref-Check – tragen die Verweisziele ihre Sätze noch?",
        "",
        f"Stand: {date.today():%d.%m.%Y} · {len(paare)} Verweispaare · "
        f"OK {len(ok)} · offen {len(offen)}",
        "",
        "> Erzeugt von `check_autoref.py`. Der Bericht wird pro Lauf überschrieben; "
        "die Urteile liegen in `autoref-state.json`. Statuswerte nie von Hand ändern – "
        "Urteil per `--verdikt <hash>=OK --notiz \"…\"` eintragen.",
        "",
        "> **`OK` heißt: beide Achsen geprüft.** Fundstelle (steht der Inhalt dort?) "
        "*und* Reichweite (trägt die Zielstelle ihn in dieser Stärke?). Trägt sie ihn "
        "nicht mehr, lautet das Urteil `RENTIERT NICHT` – der Befund bleibt dann stehen.",
        "",
    ]
    if offen:
        z += ["## Offen", "",
              "| Hash | Verweis | Ziel | Status | Marker |", "|---|---|---|---|---|"]
        for p in offen:
            ziel = (f"`{p['label']}` ({p['zielart']})" if p["zielart"]
                    else f"`{p['label']}` (fehlt)")
            z.append(f"| `{p['hash']}` | {Path(p['datei']).name}:{p['zeile']} | {ziel} "
                     f"| **{p['status']}** | {', '.join(marker_von(p['satz'])) or '–'} |")
        z.append("")
    if ok:
        z += ["## Geprüft", "", "| Hash | Verweis | Ziel | Notiz |", "|---|---|---|---|"]
        for p in ok:
            z.append(f"| `{p['hash']}` | {Path(p['datei']).name}:{p['zeile']} "
                     f"| `{p['label']}` | {p.get('notiz', '')} |")
        z.append("")
    return "\n".join(z) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Interne Querverweise auf Reichweite vorsortieren")
    ap.add_argument("--datei", help="nur diese Datei/dieses Verzeichnis als Verweisquelle")
    ap.add_argument("--paare", type=int, default=0, help="höchstens N offene Paare ausgeben")
    ap.add_argument("--alle", action="store_true", help="auch bereits mit OK quittierte erneut prüfen")
    ap.add_argument("--bericht", default=BERICHT_NAME)
    ap.add_argument("--verdikt", help=f"<hash>=<URTEIL> ({' bzw. '.join(VERDIKTE)})")
    ap.add_argument("--notiz", default="", help="Begründung zum Verdikt")
    args = ap.parse_args()

    wurzel = Path(".").resolve()
    state_pfad = wurzel / STATE_NAME
    state = lade_state(state_pfad)

    # Ziele immer über den GESAMTEN Bestand suchen: Ein Verweis aus Kapitel 2
    # kann auf ein Label in Kapitel 5 oder im Anhang zeigen.
    alle_tex = sorted((wurzel / "chapters").rglob("*.tex")) if (wurzel / "chapters").is_dir() else []
    for extra in ZUSATZ_LABELDATEIEN:
        if (wurzel / extra).is_file():
            alle_tex.append(wurzel / extra)
    if not alle_tex:
        print("Keine Kapiteldateien gefunden – noch nichts zu prüfen.")
        return 0

    ziele = sammle_labels(alle_tex, wurzel)

    quellen = alle_tex
    if args.datei:
        ziel = wurzel / args.datei
        quellen = ([p for p in alle_tex if str(p).startswith(str(ziel))]
                   if ziel.is_dir() else [ziel] if ziel.is_file() else [])
        if not quellen:
            print(f"FEHLER: {args.datei} enthält keine .tex-Dateien.", file=sys.stderr)
            return 1

    paare = paare_bilden(sammle_verweise(quellen, wurzel, ziele), ziele)

    if args.verdikt:
        if "=" not in args.verdikt:
            print("FEHLER: --verdikt braucht die Form <hash>=OK.", file=sys.stderr)
            return 2
        h, urteil = args.verdikt.split("=", 1)
        urteil = urteil.strip()
        if urteil not in VERDIKTE:
            print(f"FEHLER: '{urteil}' ist kein Verdikt ({', '.join(VERDIKTE)}).",
                  file=sys.stderr)
            return 2
        treffer = [p for p in paare if p["hash"] == h]
        if not treffer:
            print(f"FEHLER: kein Paar mit Hash {h}.", file=sys.stderr)
            return 2
        # Ein OK ohne Begründung behauptet die getrennte Prüfung beider Achsen,
        # statt sie zu belegen. Beim nächsten GEÄNDERT steht dann nichts da,
        # woran sich ablesen ließe, was damals eigentlich geprüft wurde.
        if urteil == STATUS_OK and not args.notiz.strip():
            print(f"FEHLER: '{h}=OK' braucht --notiz (worauf stützt sich das Urteil – "
                  f"Fundstelle und Reichweite).", file=sys.stderr)
            return 2
        p = treffer[0]
        state[h] = {"verdikt": urteil, "notiz": args.notiz.strip(),
                    "quelle_hash": p["quelle_hash"], "ziel_hash": p["ziel_hash"],
                    "label": p["label"], "datei": p["datei"],
                    "datum": f"{date.today():%Y-%m-%d}"}
        schreibe_state(state_pfad, state)
        print(f"OK: Urteil „{urteil}\" für {h} gespeichert ({p['datei']} → {p['label']}).")
        return 0

    bewerte(paare, state, args.alle)
    entfernt = aufraeumen(state, paare)
    schreibe_state(state_pfad, state)
    (wurzel / args.bericht).write_text(bericht(paare), encoding="utf-8")

    offen = [p for p in paare if p["status"] != STATUS_OK]
    print(f"{len(paare)} interne Verweise · {len(ziele)} Labels · "
          f"{len(offen)} zu prüfen, {len(paare) - len(offen)} unverändert quittiert")
    if entfernt:
        print(f"{entfernt} Urteil(e) zu entfallenen Verweisen aufgeräumt.")

    if not offen:
        print("\nAlle Verweispaare unverändert seit dem letzten Urteil.")
        return 0

    gezeigt = offen[:args.paare] if args.paare else offen
    print()
    for p in gezeigt:
        marker = marker_von(p["satz"])
        print(f"[{p['status']}] {p['datei']}:{p['zeile']} → {p['label']}  (hash {p['hash']})")
        print(f"    verweisender Satz: {p['satz'][:300]}")
        if p["status"] == "ZIEL FEHLT":
            print("    ZIEL: kein \\label mit diesem Namen im Textbestand – "
                  "Tippfehler oder gelöschtes Kapitel.")
        else:
            print(f"    Zielstelle: {p['zieldatei']} ({p['zielart']})")
        if marker:
            print(f"    Gewichtungsmarker im Satz: {', '.join(marker)} – "
                  f"genau hier entsteht die Reichweiten-Differenz.")
        print()

    if args.paare and len(offen) > args.paare:
        print(f"… und {len(offen) - args.paare} weitere. Nächster Block: --paare {args.paare}\n")

    print(f"Bericht: {args.bericht}")
    print("Urteil eintragen: --verdikt <hash>=OK --notiz \"<Begründung>\"")
    print("Trägt die Zielstelle den Satz nicht mehr in seiner Stärke: "
          "--verdikt <hash>=\"RENTIERT NICHT\" – der Befund bleibt dann stehen.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
