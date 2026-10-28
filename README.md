# Shiberu Korean frequency dictionary for Yomitan

A [Yomitan](https://github.com/yomidevs/yomitan) frequency dictionary built from the
[Shiberu Korean Word Frequency List](https://shiberu.app/korean-frequency-list):
the 80,000 most common Korean words in dictionary form (있다, 공부하다), ranked from
web pages, online comments, subtitles and Wikipedia.

It shows up in Yomitan as **Shiberu**, with the word's rank (1 = most common).

## Install

1. Download **[Shiberu_Korean_Frequency.zip](https://github.com/caocaochan/shiberu-yomitan/releases/latest/download/Shiberu_Korean_Frequency.zip)**
   from the [latest release](https://github.com/caocaochan/shiberu-yomitan/releases/latest).
2. In Yomitan, open Settings → Dictionaries → Import and pick the zip.

## Updates

The dictionary can be updated from inside Yomitan: in Settings → Dictionaries, click
**Check for updates**. If there's a newer revision, Yomitan shows an update button and
downloads it from the latest release here.

Every Monday a GitHub Actions job checks shiberu.app for a new word list. If the list
changed, it commits the new data, sets `VERSION` to that day's date (for example
`2026.10.28`), and publishes a release. Yomitan compares that revision to the one you
have installed.

## Build it yourself

```bash
python build.py
```

This reads `data/ko-frequency.tsv` and `VERSION`, and writes two files to `dist/`:
the dictionary zip and its index JSON (the file Yomitan fetches to check for updates).

```bash
python update.py
```

This downloads the latest list from shiberu.app and bumps `VERSION` if the words changed.

## How releases work

| Event | What the workflow does |
| --- | --- |
| Push to `main` | Builds the dictionary. Publishes a release if `VERSION` has no release yet. |
| Monday schedule, or **Run workflow** in the Actions tab | Checks shiberu.app first, commits any new list, then builds and releases as above. |

To ship a change to `build.py` without new data, bump `VERSION` (for example
`2026.10.28` → `2026.10.28.1`) and push.

## Files

| Path | What it is |
| --- | --- |
| `build.py` | Converts the TSV into a Yomitan dictionary zip and index |
| `update.py` | Pulls the latest list from shiberu.app and bumps `VERSION` |
| `VERSION` | The dictionary revision Yomitan uses to detect updates |
| `data/ko-frequency.tsv` | The original list from Shiberu (rank, lemma, per_million) |
| `data/shiberu-README.txt` | Shiberu's notes on how the list was made |
| `data/LICENSE.txt` | CC BY 4.0 legal code |
| `.github/workflows/build.yml` | Builds, checks for new data, and publishes releases |

## Credits and license

The word list is **Shiberu Korean Word Frequency List** by Shiberu
(<https://shiberu.app/korean-frequency-list>), licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This repo converts it to
Yomitan's format; the words and ranks are unchanged.

Source credits from the original list:

- Contains information from FineWeb-2 (Hugging Face), made available under the Open Data Commons Attribution License (ODC-By) v1.0, built from Common Crawl.
- CC-100 Korean (Conneau et al. 2020, "Unsupervised Cross-lingual Representation Learning at Scale"; Wenzek et al. 2020, "CCNet"), built from Common Crawl.
- KcBERT pre-training corpus (Korean news comments) by Junbum Lee (Beomi), CC BY-SA 4.0.
- DC_inside_comments dataset (Hugging Face: Dasool/DC_inside_comments), Apache License 2.0.
- Naver Sentiment Movie Corpus (NSMC) by Lucy Park (https://github.com/e9t/nsmc), CC0 1.0.
- OpenSubtitles v2024 from OPUS (http://www.opensubtitles.org/; P. Lison and J. Tiedemann, 2016, "OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles", LREC 2016).
- Korean Wikipedia (Wikimedia dump 20231101.ko), CC BY-SA 4.0.
