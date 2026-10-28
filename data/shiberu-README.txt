Shiberu Korean Word Frequency List 2026
=======================================

https://shiberu.app/korean-frequency-list

The 80,000 most frequent Korean words (lemmas, dictionary forms), most
frequent first, counted by Shiberu with its own analyzer.

Files
-----

  ko-frequency-2026.tsv         UTF-8, tab-separated, one header row
  ko-frequency-2026.tsv.gz      the same file, gzip-compressed
  ko-frequency-2026-README.txt  this file
  LICENSE.txt                   Creative Commons Attribution 4.0 legal code

Stable links to the newest version: https://shiberu.app/data/frequency/ko-frequency-latest.tsv
and https://shiberu.app/data/frequency/ko-frequency-latest.tsv.gz

Columns
-------

  rank         1 = most frequent
  lemma        the word in its dictionary form
  per_million  blended occurrences per million word tokens

How it was made
---------------

Sources (share of the blend):

  - FineWeb-2 (kor_Hang) (web pages, 17.5%): ODC-By 1.0; Common Crawl terms of use. https://huggingface.co/datasets/HuggingFaceFW/fineweb-2
  - CC-100 Korean (web pages, 17.5%): No claims on the preparation; Common Crawl terms of use. https://data.statmt.org/cc-100/
  - Naver news comments (KcBERT corpus), DC Inside comments, NSMC movie reviews (online comments, 25%): CC BY-SA 4.0; Apache-2.0; CC0 1.0. https://www.kaggle.com/datasets/junbumlee/kcbert-pretraining-corpus-korean-news-comments
  - OpenSubtitles v2024 (OPUS) (film and TV subtitles, 25%): OPUS: credit opensubtitles.org and cite Lison & Tiedemann 2016. https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles
  - Korean Wikipedia (encyclopedia, 15%): CC BY-SA 4.0. https://ko.wikipedia.org/

Every text was run through Shiberu's Korean analyzer (kiwipiepy with the
same eojeol grouping and headword rule the Shiberu Reader and dictionary
popup use), so each key is a dictionary form as Shiberu shows it:
있는 -> 있다, 교무실에서 -> 교무실, 공부했어요 -> 공부하다.

Each corpus gives a per-million rate for every lemma. The blend is a
weighted median: a lemma's score is the highest rate that corpora holding
at least half of the weight reach, so the written side (web + Wikipedia)
or the informal side (comments + subtitles) can carry a word, but no single
corpus can lift its own oddities. A lemma must occur in at least two
corpora. per_million is that blended rate.

Left out: numbers and anything with a digit, Latin- or hanja-only tokens,
anything with a bare jamo (ㅋㅋ, ㅎㅎ, ㅠㅠ), and particles that
punctuation cut off their noun.

Only counts are published: no text from any source is in these files.

Licence
-------

CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); the legal code is in LICENSE.txt.
You may copy, share and adapt the list for any purpose, including
commercially, as long as you give credit. Please credit it as:

  Shiberu Korean Word Frequency List 2026 by Shiberu (https://shiberu.app/korean-frequency-list), licensed under CC BY 4.0.

Source credits (please keep them with redistributed copies):

  - Contains information from FineWeb-2 (Hugging Face), made available under the Open Data Commons Attribution License (ODC-By) v1.0, built from Common Crawl.
  - CC-100 Korean (Conneau et al. 2020, "Unsupervised Cross-lingual Representation Learning at Scale"; Wenzek et al. 2020, "CCNet"), built from Common Crawl.
  - KcBERT pre-training corpus (Korean news comments) by Junbum Lee (Beomi), CC BY-SA 4.0.
  - DC_inside_comments dataset (Hugging Face: Dasool/DC_inside_comments), Apache License 2.0.
  - Naver Sentiment Movie Corpus (NSMC) by Lucy Park (https://github.com/e9t/nsmc), CC0 1.0.
  - OpenSubtitles v2024 from OPUS (http://www.opensubtitles.org/; P. Lison and J. Tiedemann, 2016, "OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles", LREC 2016).
  - Korean Wikipedia (Wikimedia dump 20231101.ko), CC BY-SA 4.0.

The sources are credited as their licences and terms ask. The list holds
statistics about the texts (which words occur and how often), not the texts.

Questions and corrections: support@shiberu.app
