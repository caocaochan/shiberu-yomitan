# Shiberu Korean frequency dictionary for Yomitan

A [Yomitan](https://github.com/yomidevs/yomitan) frequency dictionary built from the
[Shiberu Korean Word Frequency List 2026](https://shiberu.app/korean-frequency-list):
the 80,000 most common Korean words in dictionary form (있다, 공부하다), ranked from
web pages, online comments, subtitles and Wikipedia.

It shows up in Yomitan as **Shiberu**, with the word's rank (1 = most common).

## Install

1. Download [`dist/Shiberu_Korean_Frequency_2026.zip`](dist/Shiberu_Korean_Frequency_2026.zip).
2. In Yomitan, open Settings → Dictionaries → Import and pick the zip.

## Rebuild

```bash
python build.py
```

This reads `data/ko-frequency-2026.tsv` and writes `dist/Shiberu_Korean_Frequency_2026.zip`.
To use a newer list, download it from
<https://shiberu.app/data/frequency/ko-frequency-latest.tsv> and pass it as the first argument.

## Files

| Path | What it is |
| --- | --- |
| `build.py` | Converts the TSV into a Yomitan dictionary zip |
| `data/ko-frequency-2026.tsv` | The original list from Shiberu (rank, lemma, per_million) |
| `data/ko-frequency-2026-README.txt` | Shiberu's notes on how the list was made |
| `data/LICENSE.txt` | CC BY 4.0 legal code |
| `dist/Shiberu_Korean_Frequency_2026.zip` | The built Yomitan dictionary |

## Credits and license

The word list is **Shiberu Korean Word Frequency List 2026** by Shiberu
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
