#!/usr/bin/env python3
"""
Generate a draft fi (Finnish) question bank from the verified English bank using
a best-effort domain-level article mapping.

The output files are intentionally marked as STATUS: draft and
VERIFIED_AGAINST_SOURCE: no so they are not exposed by the app until a Finnish
subject-matter expert reviews and updates the article/page references.

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
FI_ITEMS_DIR = REPO_ROOT / "fi" / "items"
DOMAIN_MAPPING_FILE = REPO_ROOT / "fi" / "domain-mapping.json"
GLOSSARY_FILE = REPO_ROOT / "fi" / "scripts" / "glossary.json"

PROJECT_ID = "showjump-study"
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"
BATCH_SIZE = 100


def get_access_token() -> str:
    return subprocess.check_output(
        ["gcloud", "auth", "print-access-token"], text=True
    ).strip()


def load_glossary() -> dict[str, str]:
    """Return a mapping of lower-cased English term -> Finnish term."""
    if GLOSSARY_FILE.exists():
        with open(GLOSSARY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {k.lower(): v for k, v in data.items()}
    return {}


def translate_texts(texts: list[str], token: str) -> list[str]:
    """Translate a list of strings from English to Finnish."""
    if not texts:
        return []

    translations: list[str] = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        body = json.dumps(
            {"q": batch, "source": "en", "target": "fi", "format": "text"}
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
    """Replace whole-word English terms with their Finnish equivalents."""
    result = text
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


def generate_fi_files() -> None:
    token = get_access_token()
    glossary = load_glossary()

    with open(DOMAIN_MAPPING_FILE, "r", encoding="utf-8") as f:
        domain_mapping = json.load(f)

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
    iterator = iter(translated)

    FI_ITEMS_DIR.mkdir(parents=True, exist_ok=True)

    for path, data in items:
        new_data = dict(data)
        en_id = new_data.get("ID", "")
        fi_id = re.sub(r"^en-", "fi-", en_id)
        new_data["ID"] = fi_id
        if "PARENT_ID" in new_data:
            new_data["PARENT_ID"] = re.sub(r"^en-", "fi-", new_data["PARENT_ID"])

        domain = new_data.get("DOMAIN", "")
        mapping = domain_mapping.get(domain, {"article": "300", "sourcePage": 5})

        new_data["EDITION_REF"] = (
            "Kilpailusäännöt III – Esteratsastus, voimassa 1.2.2026"
        )
        new_data["ARTICLE"] = mapping["article"]
        new_data["SOURCE_PAGE"] = str(mapping["sourcePage"])
        new_data["STATUS"] = "draft"
        new_data["VERIFIED_AGAINST_SOURCE"] = "no"

        new_data["STEM"] = apply_glossary(next(iterator), glossary)
        for key in ["A", "B", "C", "D"]:
            field = f"OPTION_{key}"
            if field in new_data:
                new_data[field] = apply_glossary(next(iterator), glossary)
        explanation = apply_glossary(next(iterator), glossary)
        # Replace references to the old English article number with the mapped
        # Finnish article number in the explanation text.
        explanation = re.sub(
            r"(?i)(?:article|artikla|artiklan)\s*\d+(?:\.\d+)*",
            f"Artikla {new_data['ARTICLE']}",
            explanation,
        )
        new_data["EXPLANATION"] = explanation

        rel = path.relative_to(EN_ITEMS_DIR)
        new_name = re.sub(r"^en-", "fi-", rel.name)
        new_rel = rel.with_name(new_name)
        out_path = FI_ITEMS_DIR / new_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)

        lines = []
        for key in data.keys():
            value = new_data.get(key, "")
            lines.append(f"{key}: {value}")
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(items)} draft fi item files to {FI_ITEMS_DIR}")


if __name__ == "__main__":
    generate_fi_files()
