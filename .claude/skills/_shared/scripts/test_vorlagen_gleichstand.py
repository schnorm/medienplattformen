#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Drift-Test zwischen den Vorlagen `schriftlich` und `bachelor`.

**Wozu.** Beide Vorlagen tragen dieselben Prüfskripte – `check_formalia.py` und
`check_quellentreue.py` allein sind rund 145 KB, die zweimal im Repo liegen.
Ein Fehler, der nur in einer Kopie behoben wird, fällt monatelang niemandem auf:
Die andere Vorlage läuft ja, sie läuft nur falsch. Dieser Test macht genau das
sichtbar.

**Was er prüft**, in zwei Richtungen:

1. Jede Datei in `GLEICH` muss in beiden Vorlagen **byte-identisch** sein.
2. Jede Datei, die es in beiden `_shared`-Bäumen gibt, muss in **einer** der
   beiden Listen stehen. Wer eine neue gemeinsame Datei anlegt, muss sich also
   entscheiden: gleich halten oder als bewusste Variante mit Begründung in
   `ABWEICHEND` eintragen. Ohne diese zweite Richtung wäre der Test wertlos –
   neue Dubletten entstünden weiter unbemerkt.

**Wann er nicht läuft.** Die Vorlagen werden pro Arbeit in einen eigenen
Projektordner kopiert. Dort gibt es die Schwestervorlage nicht, und der Test
überspringt sich selbst. Er greift nur im Vorlagen-Repository, also genau dort,
wo beide Kopien gepflegt werden.

Aufruf: python -m unittest test_vorlagen_gleichstand
"""

import unittest
from pathlib import Path

VORLAGEN = ("schriftlich", "bachelor")

# Byte-identisch zu halten. Wer hier etwas ändert, ändert es in beiden Vorlagen.
GLEICH = (
    "stilprofil.md",
    "literaturverzeichnis.md",
    "scripts/check_all.py",
    "scripts/check_autoref.py",
    "scripts/check_aussenwelt.py",
    "scripts/check_bib_hygiene.py",
    "scripts/check_bib_keys.py",
    "scripts/check_formalia.py",
    "scripts/check_quellentreue.py",
    "scripts/generate_handbuch_pdf.py",
    "scripts/test_check_autoref.py",
    "scripts/test_check_aussenwelt.py",
    "scripts/test_check_bib_hygiene.py",
    "scripts/test_check_bib_keys.py",
    "scripts/test_check_formalia.py",
    "scripts/test_check_quellentreue.py",
    "scripts/test_vorlagen_gleichstand.py",
)

# Bewusste Varianten – je Datei der Grund, warum sie auseinanderlaufen DARF.
ABWEICHEND = {
    "aenderungen-format.md":
        "Thesis kennt zusätzlich die Zeile „Kolloquiumsfrage“ und Betreuer-Feedback als Rundenquelle.",
    "faktencheck-subagent-brief.md":
        "Textklassen ohne Zitationspflicht und die Verbotsliste unterscheiden sich: aufgabe.md und Pruefer-Steuerungen hier, expose.md und thesis-plan.md in der Thesis.",
    "gegenlesung-subagent-brief.md":
        "Maßstab der Gegenlesung: aufgabe.md hier, expose.md in der Thesis.",
    "hard-rules-formal.md":
        "Umfangsvorgabe, Aktivierungsblöcke und Pronomen-Regel sind papiertyp- bzw. thesisspezifisch.",
    "modell-empfehlung.md":
        "Andere Phasen (Exposé, Erhebung, Auswertung, Kolloquium) und andere Opus/Sonnet-Grenze.",
    "projektstruktur.md":
        "Unterschiedlicher Dateibestand (auswertung/, prozess-status.md, typen/).",
    "quellen-versionen.md":
        "Andere IU-Quellen im Register (Thesis-Handbuch, FAQ, Checkliste).",
    "zitation-sonderfaelle.md":
        "Eigene Erhebungsdaten, Software-Sonderfall und frühere Prüfungsleistungen sind je Vorlage anders gewichtet.",
    "scripts/check_status.py":
        "Thesis-Fassung rechnet zusätzlich den Zeitplan gegen das Abgabedatum ([ZEITPLAN]).",
    "scripts/check_umfang.py":
        "Diese Vorlage misst Wortbudgets, die Thesis Seitenbudgets (36–44-Seiten-Korridor).",
    "scripts/test_check_status.py":
        "Testet die jeweilige Fassung von check_status.py.",
    "scripts/test_check_umfang.py":
        "Testet die jeweilige Fassung von check_umfang.py.",
    "scripts/export_pdf.py":
        "Thesis-Fassung kann zusätzlich das Exposé im Layout der IU-Mustervorlage rendern.",
}


def _repo_wurzel() -> Path | None:
    """Verzeichnis suchen, das beide Vorlagen enthält – sonst None."""
    for kandidat in Path(__file__).resolve().parents:
        if all((kandidat / v / ".claude" / "skills" / "_shared").is_dir() for v in VORLAGEN):
            return kandidat
    return None


WURZEL = _repo_wurzel()


def _shared(vorlage: str) -> Path:
    return WURZEL / vorlage / ".claude" / "skills" / "_shared"


def _dateien(vorlage: str) -> set[str]:
    basis = _shared(vorlage)
    return {p.relative_to(basis).as_posix() for p in basis.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts}


@unittest.skipIf(WURZEL is None,
                 "Nur im Vorlagen-Repository sinnvoll – in einem Projektordner "
                 "gibt es die Schwestervorlage nicht.")
class TestVorlagenGleichstand(unittest.TestCase):

    def test_gemeinsame_dateien_sind_identisch(self):
        for rel in GLEICH:
            with self.subTest(datei=rel):
                a, b = (_shared(v) / rel for v in VORLAGEN)
                self.assertTrue(a.is_file(), f"fehlt in {VORLAGEN[0]}: {rel}")
                self.assertTrue(b.is_file(), f"fehlt in {VORLAGEN[1]}: {rel}")
                self.assertEqual(
                    a.read_bytes(), b.read_bytes(),
                    f"{rel} ist auseinandergelaufen. Entweder die Änderung in beide "
                    f"Vorlagen übernehmen oder die Datei mit Begründung nach "
                    f"ABWEICHEND verschieben.")

    def test_jede_gemeinsame_datei_ist_eingeordnet(self):
        gemeinsam = _dateien(VORLAGEN[0]) & _dateien(VORLAGEN[1])
        eingeordnet = set(GLEICH) | set(ABWEICHEND)
        offen = sorted(gemeinsam - eingeordnet)
        self.assertEqual(
            offen, [],
            "Diese Dateien gibt es in beiden Vorlagen, aber in keiner Liste: "
            f"{offen}. Entscheiden und in GLEICH oder ABWEICHEND (mit Grund) "
            "eintragen – sonst driften sie unbemerkt auseinander.")

    def test_listen_nennen_nur_existierende_dateien(self):
        gemeinsam = _dateien(VORLAGEN[0]) & _dateien(VORLAGEN[1])
        veraltet = sorted((set(GLEICH) | set(ABWEICHEND)) - gemeinsam)
        self.assertEqual(
            veraltet, [],
            f"Diese Einträge zeigen auf Dateien, die es nicht (mehr) in beiden "
            f"Vorlagen gibt: {veraltet}. Aus der Liste entfernen.")

    def test_abweichende_dateien_haben_eine_begruendung(self):
        for rel, grund in ABWEICHEND.items():
            with self.subTest(datei=rel):
                self.assertGreater(
                    len(grund.strip()), 20,
                    f"{rel}: Der Grund muss erklären, WARUM die Fassungen "
                    "auseinanderlaufen dürfen – ein Stichwort reicht nicht.")


if __name__ == "__main__":
    unittest.main()
