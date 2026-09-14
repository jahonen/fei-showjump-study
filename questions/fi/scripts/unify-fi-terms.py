#!/usr/bin/env python3
"""
Yhtenäistää suomenkielisen kysymyspankin sääntöviittaukset ja poistaa
jäljelle jääneet konekäännösjäämät.

Sääntökirjaan viitattiin kolmella eri nimityksellä ("JR:n",
"Esteratsastussääntöjen", "Kilpailusääntöjen"). Kaikki yhtenäistetään
muotoon "kilpailusääntöjen", joka vastaa virallista nimeä
Kilpailusäännöt III - Esteratsastus.

Vain kenttien STEM, OPTION_A-OPTION_D ja EXPLANATION arvoja muutetaan.
"""

import re
from pathlib import Path

ITEMS_DIR = Path(__file__).resolve().parents[1] / "items"
EDITABLE = {"STEM", "OPTION_A", "OPTION_B", "OPTION_C", "OPTION_D", "EXPLANATION"}

# Sääntökirjan nimitykset genetiivissä, joita seuraa artikla/kohta/pykälä.
BOOK_NAMES = r"(?:JR:n|Esteratsastussääntöjen|Kilpailusääntöjen)"
REFERENCE_WORDS = r"(?:artikla|artiklan|artiklassa|kohta|kohdan|kohdassa|pykälä|pykälän|pykälässä)"

# Muut korjaukset: hakusana -> korvaus.
REPLACEMENTS = [
    # Yleisnimi kirjoitetaan pienellä myös sääntökirjan nimessä, kun se on
    # osa lausetta eikä teoksen täsmällinen nimi.
    (re.compile(rf"\b{BOOK_NAMES}\s+({REFERENCE_WORDS})\b"), r"kilpailusääntöjen \1"),
    # "rangaistus" on englannin penalty; sääntökirja käyttää sanaa virhepiste.
    (re.compile(r"\brangaistuksena\b"), "virhepisteinä"),
    (re.compile(r"\brangaistus\b"), "virhepiste"),
    (re.compile(r"\brangaistuspiste(\w*)"), r"virhepiste\1"),
    # "aikataulu" on englannin schedule; sääntökirja käyttää sanaa kilpailukutsu.
    (re.compile(r"\bVerryttelyalueen aikataulu\b"), "Verryttelyalueen kilpailukutsu"),
]


def fix_value(value: str) -> str:
    for pattern, replacement in REPLACEMENTS:
        value = pattern.sub(replacement, value)
    # Virkkeen alussa sääntökirjan nimitys kirjoitetaan isolla alkukirjaimella.
    value = re.sub(r"^kilpailusääntöjen\b", "Kilpailusääntöjen", value)
    value = re.sub(r"([.!?]\s+)kilpailusääntöjen\b", r"\1Kilpailusääntöjen", value)
    return value


def process_file(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").rstrip("\n").split("\n")
    changed = False
    out = []
    for line in lines:
        key, sep, value = line.partition(": ")
        if sep and key in EDITABLE:
            new_value = fix_value(value)
            if new_value != value:
                changed = True
                line = f"{key}: {new_value}"
        out.append(line)
    if changed:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    paths = sorted(ITEMS_DIR.rglob("*.txt"))
    changed = sum(1 for p in paths if process_file(p))
    print(f"Tarkistettu {len(paths)} tiedostoa, muutettu {changed}.")


if __name__ == "__main__":
    main()
