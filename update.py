"""Download Shiberu's latest Korean frequency list and bump VERSION if the word list changed.

Usage: python update.py

Prints "changed" or "unchanged" as its last line. VERSION becomes today's UTC date
(YYYY.MM.DD), which Yomitan compares to decide whether an update is available.
"""
import datetime
import urllib.request

from build import DATA, ROOT, parse_tsv

BASE = "https://shiberu.app/data/frequency"
FILES = {
    "ko-frequency.tsv": f"{BASE}/ko-frequency-latest.tsv",
    "shiberu-README.txt": f"{BASE}/ko-frequency-2026-README.txt",
    "LICENSE.txt": f"{BASE}/LICENSE.txt",
}
USER_AGENT = "shiberu-yomitan (+https://github.com/caocaochan/shiberu-yomitan)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8")


def next_version(current):
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d")
    if not current.startswith(today):
        return today
    # Second change on the same day: 2026.10.28 -> 2026.10.28.1 -> 2026.10.28.2
    parts = current.split(".")
    return f"{today}.{int(parts[3]) + 1 if len(parts) > 3 else 1}"


def main():
    tsv = fetch(FILES["ko-frequency.tsv"])
    parse_tsv(tsv)  # refuse to save anything that isn't a real word list

    tsv_path = DATA / "ko-frequency.tsv"
    changed = tsv_path.read_text(encoding="utf-8") != tsv
    tsv_path.write_text(tsv, encoding="utf-8", newline="")

    # Shiberu's notes and license are kept in sync too; a missing file isn't fatal.
    for name in ("shiberu-README.txt", "LICENSE.txt"):
        try:
            (DATA / name).write_text(fetch(FILES[name]), encoding="utf-8", newline="")
        except Exception as e:  # noqa: BLE001
            print(f"warning: could not refresh {name}: {e}")

    if changed:
        version_path = ROOT / "VERSION"
        new = next_version(version_path.read_text(encoding="utf-8").strip())
        version_path.write_text(new + "\n", encoding="utf-8", newline="")
        print(f"Word list changed; VERSION -> {new}")
    print("changed" if changed else "unchanged")


if __name__ == "__main__":
    main()
