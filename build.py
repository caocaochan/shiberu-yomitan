"""Build a Yomitan frequency dictionary from the Shiberu Korean frequency TSV.

Usage: python build.py [input.tsv] [license.txt] [output.zip]
Defaults: data/ko-frequency-2026.tsv, data/LICENSE.txt, dist/Shiberu_Korean_Frequency_2026.zip
"""
import csv
import json
import sys
import zipfile
from pathlib import Path

BANK_SIZE = 10000
ROOT = Path(__file__).resolve().parent

args = sys.argv[1:]
src = Path(args[0]) if len(args) > 0 else ROOT / "data" / "ko-frequency-2026.tsv"
license_path = Path(args[1]) if len(args) > 1 else ROOT / "data" / "LICENSE.txt"
out = Path(args[2]) if len(args) > 2 else ROOT / "dist" / "Shiberu_Korean_Frequency_2026.zip"

rows = []
seen = set()
with open(src, encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        lemma = r["lemma"].strip()
        if not lemma or lemma in seen:
            continue
        seen.add(lemma)
        rank = int(r["rank"])
        rows.append([lemma, "freq", {"value": rank, "displayValue": str(rank)}])

index = {
    "title": "Shiberu",
    "revision": "ko-frequency-2026.1",
    "format": 3,
    "sequenced": False,
    "frequencyMode": "rank-based",
    "author": "Shiberu",
    "url": "https://shiberu.app/korean-frequency-list",
    "sourceLanguage": "ko",
    "targetLanguage": "ko",
    "description": (
        "Top 80,000 Korean lemmas (dictionary forms), ranked by a blend of web pages, "
        "online comments, subtitles and Wikipedia. Rank 1 = most frequent."
    ),
    "attribution": (
        "Shiberu Korean Word Frequency List 2026 by Shiberu "
        "(https://shiberu.app/korean-frequency-list), licensed under CC BY 4.0. "
        "Sources: FineWeb-2 (ODC-By 1.0, Common Crawl); CC-100 Korean; KcBERT corpus by "
        "Junbum Lee (CC BY-SA 4.0); DC_inside_comments (Apache-2.0); NSMC by Lucy Park (CC0 1.0); "
        "OpenSubtitles v2024 from OPUS (Lison & Tiedemann 2016); Korean Wikipedia (CC BY-SA 4.0). "
        "Converted to Yomitan format."
    ),
}

out.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("index.json", json.dumps(index, ensure_ascii=False, indent=2))
    for i in range(0, len(rows), BANK_SIZE):
        z.writestr(
            f"term_meta_bank_{i // BANK_SIZE + 1}.json",
            json.dumps(rows[i : i + BANK_SIZE], ensure_ascii=False, separators=(",", ":")),
        )
    z.writestr("LICENSE.txt", license_path.read_text(encoding="utf-8"))

print(f"{len(rows)} entries -> {out}")
