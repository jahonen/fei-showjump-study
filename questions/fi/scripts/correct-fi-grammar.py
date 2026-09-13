#!/usr/bin/env python3
"""
Apply targeted Finnish grammar/terminology corrections to the translated
question bank .txt files under questions/fi/items.

Only values of STEM, OPTION_*, and EXPLANATION are modified.
Protected keys (ID, PARENT_ID, etc.) are never touched.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ITEMS_DIR = REPO_ROOT / "fi" / "items"

EDITABLE_KEYS = {"STEM", "OPTION_A", "OPTION_B", "OPTION_C", "OPTION_D", "EXPLANATION"}
ARTICLE_RE = re.compile(r"\b([Aa])rtikla (\d[\d.]*)(?=\s+(?:mukaan|mukainen))")
ARTICLE_ANY_RE = re.compile(r"\bArtikla\b")


def fix_value(value: str) -> str:
    """Apply corrections to a single editable value."""

    # 1. Finnish terminology fixes (literal/MT errors)
    value = value.replace("sulhasille", "tallimiehille")
    value = value.replace("taloudenhoitajan", "stewardin")
    value = value.replace("leviäminen", "leveys")
    value = value.replace("kieltäytyisivätkään", "kieltäytyisivätkin")

    # 2. Fix the one garbled "What is true" STEM
    if "Mitä on pidettävä paikkansa" in value:
        value = value.replace(
            "Mitä on pidettävä paikkansa kaikista sisään- ja uloskäynneistä hevosen ollessa kilpailualueella?",
            "Mikä seuraavista pitää paikkansa kaikkien sisään- ja uloskäyntien osalta hevosen ollessa kilpailualueella?",
        )

    # 3. Fix the one garbled "cross-reference" STEM
    if "ristiviittaukset mihin" in value:
        value = value.replace(
            "JR:n artiklan 263.4.30 ristiviittaukset mihin kilpailuareenalla käytettäviin elektronisiin laitteisiin liittyvään artikkeliin?",
            "Mihin artiklaan JR:n artikla 263.4.30 viittaa kilpailualueella käytettäviin elektronisiin laitteisiin liittyen?",
        )

    # 4. Replace indoor-riding-hall mistranslation in one option
    value = value.replace(
        "Maneesin on oltava aidattu ja sisään- ja uloskäynnit fyysisesti suljettu hevosen ollessa maneesissa kilpailun aikana.",
        "Kilpailualueen on oltava aidattu ja sisään- ja uloskäynnit fyysisesti suljettu hevosen ollessa kilpailualueella kilpailun aikana.",
    )
    value = value.replace("Mikä kilpailuareenaa koskeva väittämä", "Mikä kilpailualueeseen liittyvä väittämä")
    value = value.replace("ulkoareenoita", "ulkokenttiä")

    # 5. Cup/support wording for obstacle depth question
    value = value.replace(
        "Mikä on sallittu syvyysalue tuille (kupeille), jotka kannattelevat pylväitä ja muita esteen osia?",
        "Mikä on sallittu syvyys tuille (kupeille), jotka kannattelevat pylväitä ja muita esteen osia?",
    )

    # 6. Article grammar: use genitive before "mukaan" / "mukainen"
    def art_repl(m: re.Match) -> str:
        # m.group(1) is the original first letter (A or a)
        number = m.group(2)
        if m.start() == 0:
            return f"Artiklan {number}"
        return f"artiklan {number}"

    value = ARTICLE_RE.sub(art_repl, value)

    # 7. Lowercase remaining "Artikla" when it is not the first word of the value
    first_space = value.find(" ")
    if first_space == -1:
        return value
    first_word, rest = value[:first_space], value[first_space + 1 :]
    if first_word in ("Artikla", "Artiklan"):
        rest = ARTICLE_ANY_RE.sub("artikla", rest)
        value = f"{first_word} {rest}"
    else:
        value = ARTICLE_ANY_RE.sub("artikla", value)

    return value


def process_file(path: Path) -> bool:
    """Read a file, apply corrections, and write it back if changed.

    Returns True if the file was modified.
    """
    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    changed = False
    for line in lines:
        # Keep line endings clean
        original = line.rstrip("\n")
        if ":" in original:
            key, sep, value = original.partition(": ")
            if key in EDITABLE_KEYS:
                new_value = fix_value(value)
                if new_value != value:
                    changed = True
                    original = f"{key}: {new_value}"
        new_lines.append(original + "\n")

    if changed:
        with path.open("w", encoding="utf-8") as f:
            f.writelines(new_lines)

    return changed


def main() -> None:
    paths = sorted(ITEMS_DIR.rglob("*.txt"))
    changed_count = 0
    changed_files = []
    for p in paths:
        if process_file(p):
            changed_count += 1
            changed_files.append(str(p.relative_to(ITEMS_DIR)))

    print(f"Reviewed {len(paths)} files.")
    print(f"Changed {changed_count} files.")
    if changed_files:
        print("Changed files:")
        for name in changed_files:
            print(f"  {name}")


if __name__ == "__main__":
    main()
