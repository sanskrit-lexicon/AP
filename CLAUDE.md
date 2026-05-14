# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains tools for processing the **Apte Sanskrit-English Dictionary (1957)** as part of the [Sanskrit Lexicon project](https://github.com/sanskrit-lexicon/AP). Work is organized into numbered `issues/` subdirectories, each addressing a specific improvement to the dictionary data.

## Running the Pipeline

There is no build system. This is a Python data-processing pipeline run directly:

```bash
# Typical issue workflow (e.g., issue25)
cd issues/issue25
python step1.py          # initial extraction / prep
python step2.py          # main transformation (see Data Flow below)
python step3.py          # validation against sanhw1.txt
python step4.py          # assign permanent L-numbers
```

`redo.sh` in an issue directory re-runs the pipeline from scratch:
```bash
cd issues/issue25
bash redo.sh
```

Regenerate a local display (requires XAMPP + csl-pywork installed):
```bash
cd issues/issue10
bash redo_ap.sh <ap_file> <app_dir>
```

## Architecture

### Data Flow

```
csl-orig/v02/ap/ap.txt  (upstream source dictionary)
        ↓
    tmp_ap_0.txt         (local working copy)
        ↓  step2.py
    tmp_ap_2.txt  +  log2.tsv
        ↓  step3.py
    log3.tsv             (validation: each entry checked against sanhw1.txt)
        ↓  step4.py
    tmp_ap_4.txt  +  log4.tsv   (permanent L-numbers assigned)
        ↓  (manual correction if needed → tmp_ap_5.txt)
        ↓  git merge-file
    csl-orig/v02/ap/ap.txt  (committed upstream)
```

### Dictionary Entry Format

Each entry spans multiple lines:
```
<L>ID<pc>page<k1>headword<k2>variant<h>homonym<e>etymology
...body...
<LEND>
```

- `<k1>` = primary headword (IAST encoding)
- `<k2>` = secondary/variant form
- `<L>` / `<LEND>` delimit entries
- `{{Lbody=ID}}` cross-references a parent entry's L-number

### L-Number System

| Format | Meaning |
|--------|---------|
| `29` | Base entry |
| `29.002`, `29.004` | Sub-entries (step4.py assigns these) |
| `.XYZ` | Temporary placeholder during step2 processing |
| `.ABC` | Failed resolution — needs manual mapping |

### Key Pattern Being Processed

Issues 23 and 25 separate **hidden headwords** embedded in suffix patterns:
- Issue 23: `.{@{#-suffix#}@}` 
- Issue 25: `({@{#-suffix#}@})`

`step2.py` resolves the suffix to a full headword via `adjust_hw()` heuristics, falling back to `manually_mapped.tsv` for failures.

### Core Scripts

| Script | Role |
|--------|------|
| `step2.py` | Main transformation; resolves suffix patterns to full headwords; outputs `tmp_ap_2.txt` + `log2.tsv` |
| `step3.py` | Validates resolutions against `sanhw1.txt`; outputs `log3.tsv` with `in_sanhw1` boolean |
| `step4.py` | Replaces `.XYZ` placeholders with permanent numeric L-suffixes; outputs `tmp_ap_4.txt` |
| `parseheadline.py` | Utility: parses the `<L>...<LEND>` header line into a dict |
| `manually_mapped.tsv` | Manual fallback for entries where automatic suffix resolution failed |

### Validation Data

- **`sanhw1.txt`** — Sanskrit word list used for headword validation in step3
- **`issues/issue1/diffs/`** — Historical diff files (`diff_01_02.txt`, etc.) tracking versions of `ap.txt`

## Python Conventions

- **Encoding**: always `codecs.open(..., encoding='utf-8')` for file I/O
- **stdout**: reconfigure at script start — `sys.stdout.reconfigure(encoding='utf-8')`
- **Dependencies**: standard library only (no pip packages)
- **Log files**: tab-separated `.tsv` with a header row

## File Encoding & Line Endings

`.gitattributes` enforces LF line endings for `.tsv`, `.sh`, `.txt`, and `.yml` files. Keep files UTF-8 with IAST transliteration.

