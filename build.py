"""Build the Shiberu Korean frequency dictionary for Yomitan.

Usage: python build.py

Reads data/ko-frequency.tsv, data/LICENSE.txt and VERSION, and writes:
  dist/Shiberu_Korean_Frequency.zip   the dictionary to import into Yomitan
  dist/Shiberu_Korean_Frequency.json  its index.json, which Yomitan fetches to check for updates
"""
import csv
import io
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DIST = ROOT / "dist"

REPO = "caocaochan/shiberu-yomitan"
ASSET = "Shiberu_Korean_Frequency"
LATEST = f"https://github.com/{REPO}/releases/latest/download"

BANK_SIZE = 10000
MIN_ROWS = 1000


def parse_tsv(text):
    """Return [(rank, lemma)] from Shiberu's TSV text, or raise ValueError if it doesn't look right."""
    reader = csv.reader(io.StringIO(text), delimiter="\t")
    header = next(reader, None)
    if header is None or [h.strip() for h in header[:2]] != ["rank", "lemma"]:
        raise ValueError(f"unexpected header: {header!r}")
    rows, seen = [], set()
    for line in reader:
        if not line:
            continue
        rank, lemma = int(line[0]), line[1].strip()
        if lemma and lemma not in seen:
            seen.add(lemma)
            rows.append((rank, lemma))
    if len(rows) < MIN_ROWS:
        raise ValueError(f"only {len(rows)} rows")
    return rows


def make_index(revision):
    return {
        "title": "Shiberu",
        "revision": revision,
        "format": 3,
        "sequenced": False,
        "frequencyMode": "rank-based",
        "author": "Shiberu",
        "url": "https://shiberu.app/korean-frequency-list",
        "sourceLanguage": "ko",
        "targetLanguage": "ko",
        "description": (
            "Top 80,000 Korean lemmas (dictionary forms), ranked by a blend of web pages, "
            "online comments, subtitles and Wikipedia. Rank 1 = most frequent. "
            f"Yomitan build: https://github.com/{REPO}"
        ),
        "attribution": (
            "Shiberu Korean Word Frequency List by Shiberu "
            "(https://shiberu.app/korean-frequency-list), licensed under CC BY 4.0. "
            "Sources: FineWeb-2 (ODC-By 1.0, Common Crawl); CC-100 Korean; KcBERT corpus by "
            "Junbum Lee (CC BY-SA 4.0); DC_inside_comments (Apache-2.0); NSMC by Lucy Park (CC0 1.0); "
            "OpenSubtitles v2024 from OPUS (Lison & Tiedemann 2016); Korean Wikipedia (CC BY-SA 4.0). "
            "Converted to Yomitan format."
        ),
        "isUpdatable": True,
        "indexUrl": f"{LATEST}/{ASSET}.json",
        "downloadUrl": f"{LATEST}/{ASSET}.zip",
    }


def main():
    revision = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    rows = parse_tsv((DATA / "ko-frequency.tsv").read_text(encoding="utf-8"))
    index_json = json.dumps(make_index(revision), ensure_ascii=False, indent=2)
    entries = [[lemma, "freq", {"value": rank, "displayValue": str(rank)}] for rank, lemma in rows]

    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(DIST / f"{ASSET}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("index.json", index_json)
        for i in range(0, len(entries), BANK_SIZE):
            z.writestr(
                f"term_meta_bank_{i // BANK_SIZE + 1}.json",
                json.dumps(entries[i : i + BANK_SIZE], ensure_ascii=False, separators=(",", ":")),
            )
        z.writestr("LICENSE.txt", (DATA / "LICENSE.txt").read_text(encoding="utf-8"))
    (DIST / f"{ASSET}.json").write_text(index_json, encoding="utf-8")

    print(f"Built revision {revision}: {len(entries)} entries -> {DIST}")


if __name__ == "__main__":
    main()
