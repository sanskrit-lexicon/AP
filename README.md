# AP — Apte Sanskrit-English Dictionary (1957)

Collaborative tools for parsing, validating, and improving the digitised Apte Sanskrit-English dictionary, as part of the [Sanskrit Lexicon project](https://github.com/sanskrit-lexicon).

The upstream dictionary lives at [csl-orig/v02/ap/ap.txt](https://github.com/sanskrit-lexicon/csl-orig). This repo contains the scripts and issue-by-issue workflow used to clean and enhance it.

---

## Project Timeline

| Period | Milestone |
|--------|-----------|
| **Jul 2025** | Project started — 28 historical diff files created, git history established (Issue 1) |
| **Jan 2026** | Tooltip activation for `<ab>` and `<ls>` elements; extended ASCII handling (Issues 2–4) |
| **Feb 2026** | `<lex>` and `<lang>` markup; Sanskrit global character corrections (Issues 3, 6) |
| **Apr 2026** | Major pipeline built for separating hidden headwords; **8,518 new entries extracted**, growing the dictionary from 79,815 → 88,333 entries (Issues 16, 23) |
| **May 2026** | Parenthetical suffix patterns handled; link targets documented (Issues 19, 25) |

---

## How It Works

Work is organised into numbered `issues/` directories. Each issue targets a specific problem in the dictionary data and follows a step-by-step Python pipeline:

```
csl-orig/v02/ap/ap.txt   ← upstream source
        ↓
    tmp_ap_0.txt          local working copy
        ↓  step2.py       main transformation
    tmp_ap_2.txt + log2.tsv
        ↓  step3.py       validate against Sanskrit word list
    log3.tsv
        ↓  step4.py       assign permanent entry numbers
    tmp_ap_4.txt
        ↓  (manual fixes if needed)
        ↓  git merge-file
    csl-orig/v02/ap/ap.txt  ← committed back upstream
```

To re-run an issue pipeline from scratch:

```bash
cd issues/issue25
bash redo.sh
```

---

## Contributors

| Contributor | Role |
|-------------|------|
| **Dr. Dhaval Patel** | Lead developer — 75 commits |
| **Jim Funderburk** (funderburkjim) | Core contributor — 49 commits |
| **Mārcis Gasūns** | Documentation |

---

## Repository Layout

```
issues/
  issue1/    Git history tracking, historical diffs of ap.txt
  issue2/    <ab> and <ls> tooltips
  issue3/    Global Sanskrit character corrections
  issue4/    Extended ASCII handling
  issue16/   Suffix separation pipeline (step2–step4)
  issue23/   Hidden headword extraction (.{@{#-suffix#}@} pattern)
  issue25/   Parenthetical suffix extraction (({@{#-suffix#}@}) pattern)
  ...
```

For technical details on the pipeline and dictionary format, see [CLAUDE.md](CLAUDE.md).
