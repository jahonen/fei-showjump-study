#!/usr/bin/env python3
"""
Generate the el (Hellenic/Greek) question bank from the verified English bank.

The script:
  1. Reads the verified en item files.
  2. Translates stems, options and explanations using the Google Cloud Translation
     API (source en -> target el).
  3. Applies a glossary of FEI jumping terms extracted from the Greek rulebook so
     official terminology is preferred over generic translations.
  4. Rewrites IDs with the el prefix and updates edition/source metadata to point
     at the Greek PDF.

Requirements:
  - pypdf installed
  - Active gcloud authentication with access to translate.googleapis.com
  - X-Goog-User-Project header set to the billing project
"""

import json
import re
import subprocess
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EN_ITEMS_DIR = REPO_ROOT / "en" / "items"
EL_ITEMS_DIR = REPO_ROOT / "el" / "items"
ARTICLE_PAGES_FILE = REPO_ROOT / "el" / "article-pages.json"
GLOSSARY_FILE = REPO_ROOT / "el" / "scripts" / "glossary.json"

PROJECT_ID = "showjump-study"
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"
BATCH_SIZE = 100


def get_access_token() -> str:
    return subprocess.check_output(
        ["gcloud", "auth", "print-access-token"], text=True
    ).strip()


def load_glossary() -> dict[str, str]:
    """Return a mapping of lower-cased English term -> Greek term."""
    if GLOSSARY_FILE.exists():
        with open(GLOSSARY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {k.lower(): v for k, v in data.items()}
    return {}


def translate_texts(texts: list[str], token: str) -> list[str]:
    """Translate a list of strings from English to Greek."""
    if not texts:
        return []

    translations: list[str] = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        body = json.dumps(
            {"q": batch, "source": "en", "target": "el", "format": "text"}
        ).encode("utf-8")
        req = urllib.request.Request(
            TRANSLATE_URL,
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "X-Goog-User-Project": PROJECT_ID,
            },
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        translations.extend(
            t["translatedText"] for t in payload["data"]["translations"]
        )
    return translations


def apply_glossary(text: str, glossary: dict[str, str]) -> str:
    """Replace whole-word English terms with their Greek equivalents."""
    result = text
    # Sort by length descending so longer phrases are matched first.
    for en_term in sorted(glossary, key=len, reverse=True):
        pattern = re.compile(re.escape(en_term), re.IGNORECASE)
        result = pattern.sub(lambda m: glossary[en_term], result)
    return result


def parse_item(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in text.split("\n"):
        line = raw_line.rstrip()
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def article_page(article: str, page_map: dict[str, int]) -> int:
    base = article.split(".")[0]
    return page_map.get(base, 0)


def generate_el_files() -> None:
    token = get_access_token()
    glossary = load_glossary()

    with open(ARTICLE_PAGES_FILE, "r", encoding="utf-8") as f:
        article_pages = json.load(f)["articlePages"]

    # Collect all en files and the text strings that need translation.
    files = sorted(EN_ITEMS_DIR.rglob("*.txt"))
    items: list[tuple[Path, dict[str, str]]] = []
    strings_to_translate: list[str] = []

    for path in files:
        data = parse_item(path.read_text(encoding="utf-8"))
        if data.get("STATUS") != "verified":
            continue
        items.append((path, data))
        strings_to_translate.append(data.get("STEM", ""))
        for key in ["A", "B", "C", "D"]:
            field = f"OPTION_{key}"
            if field in data:
                strings_to_translate.append(data[field])
        strings_to_translate.append(data.get("EXPLANATION", ""))

    print(f"Translating {len(strings_to_translate)} strings from {len(items)} items...")
    translated = translate_texts(strings_to_translate, token)

    # Apply glossary replacements and map translations back.
    iterator = iter(translated)

    EL_ITEMS_DIR.mkdir(parents=True, exist_ok=True)

    for path, data in items:
        new_data = dict(data)
        en_id = new_data.get("ID", "")
        el_id = re.sub(r"^en-", "el-", en_id)
        new_data["ID"] = el_id
        if "PARENT_ID" in new_data:
            new_data["PARENT_ID"] = re.sub(r"^en-", "el-", new_data["PARENT_ID"])

        new_data["EDITION_REF"] = (
            "Κανονισμός Αγώνων Υπερπήδησης Εμποδίων, 25η έκδοση (Ενημέρωση 2017)"
        )
        new_data["SOURCE_PAGE"] = str(article_page(new_data.get("ARTICLE", ""), article_pages))

        new_data["STEM"] = apply_glossary(next(iterator), glossary)
        for key in ["A", "B", "C", "D"]:
            field = f"OPTION_{key}"
            if field in new_data:
                new_data[field] = apply_glossary(next(iterator), glossary)
        new_data["EXPLANATION"] = apply_glossary(next(iterator), glossary)

        # Reconstruct the file path with the el prefix.
        rel = path.relative_to(EN_ITEMS_DIR)
        new_name = re.sub(r"^en-", "el-", rel.name)
        new_rel = rel.with_name(new_name)
        out_path = EL_ITEMS_DIR / new_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)

        lines = []
        for key in data.keys():
            value = new_data.get(key, "")
            lines.append(f"{key}: {value}")
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(items)} el item files to {EL_ITEMS_DIR}")


if __name__ == "__main__":
    generate_el_files()
