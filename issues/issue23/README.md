_Created: 20-04-2026 · Last updated: 05-09-2026_

# Issue 23: Separating Hidden Headwords from `.{@{#-suffix#}@}` Patterns

## Overview

This issue focuses on identifying and separating "hidden" headwords located within entries using the pattern `.{@{#-suffix#}@}` or `.({@{#-suffix#}@})`.

These suffixes are extracted, resolved into full headwords, and converted into independent entries with their own `L` identifiers.

## Initial Statistics

Input file: `tmp_ap_0.txt` (taken from `csl-orig` repository).

The processing focused on 1,900 specific instances based on patterns `.{@{#-suffix#}@}` or `.({@{#-suffix#}@})` into individual headword and entries.

---

## Step 2: Identification and Separation

`python3 step2.py tmp_ap_0.txt tmp_ap_2.txt log2.tsv`

- **Input**: `tmp_ap_0.txt`
- **Output**: `tmp_ap_2.txt` (Text file with new entries)
- **Log**: `log2.tsv` (Tab-separated mapping of Lid, basehw, suffix, and resolution)

### Statistics (log2.tsv)

- **Total entries separated**: 1,900
- **Automatically resolved**: 1,899
- **Unresolved (None)**: 1 (Lid 32337). This was a typo and was corrected in the base data ap.txt itself.

### Key Logic

1. **Resolution**: The script uses a set of heuristic rules in `adjust_hw()` to combine the base headword with the suffix.

2. **Fallback**: If automatic resolution fails, it looks up the entry in `manually_mapped.tsv`.

3. **Placeholders**:
   - New entries are assigned a temporary `L` number ending in `.XYZ` (e.g., `29.XYZ`).
   - Unresolved entries are marked with `.ABC` in `<k1>` and `<k2>` tags.

---

## Step 3: Validation

`python3 step3.py`

- **Input**: `log2.tsv`
- **Output**: `log3.tsv`
- **Logic**: Checks the `resolution` column against `sanhw1.txt` (a list of valid Sanskrit words).
- **Statistics (log3.tsv)**:
  - **Total entries**: 1,900
  - **Found in sanhw1 (True)**: 1,803
  - **Not found in sanhw1 (False)**: 97
  These 97 entries are manually validated and are valid headwords.

---

## Step 4: Permanent L Number Assignment

`python3 step4.py`

- **Input**: `tmp_ap_2.txt`
- **Output**: `tmp_ap_4.txt`
- **Log**: `log4.tsv`

### Statistics (log4.tsv)

- **Total L numbers mapped**: 1,900

### Key Logic

1. **L Number Resolution**: Replaces `.XYZ` placeholders with unique, incrementing permanent `L` numbers (e.g., `29.002`, `29.004`).

2. **Sequential Assignment**: New `L` numbers are assigned numerically based on surrounding entries.

3. **Lbody Mapping**: Updates `{{Lbody=...}}` references from placeholder `.XYZ` form to the new numeric `L` values.

---

## Manual Resolution (`tmp_ap_5.txt`)

`tmp_ap_5.txt` was created by copying `tmp_ap_4.txt` and performing manual edits to resolve any remaining `L` number clashes.

## Supporting Files

### `manually_mapped.tsv`

Contains 208 manual resolutions (as of current state) where automatic logic failed.

### `parseheadline.py`

Utility used by `step2.py` and `step4.py` to handle header metadata.

---

## How to Update

This is not required to be re-run. The corrections have been made to csl-orig/v02/ap/ap.txt file and therefore, if you redo this work, there will not be any matching patterns.

1. Update `manually_mapped.tsv` with new resolutions.
2. Run `step2.py tmp_ap_0.txt tmp_ap_2.txt log2.tsv`.
3. Run `step3.py` for verification.
4. Run `step4.py` for finalizing `L` numbers.
5. Copy `tmp_ap_4.txt` and as `tmp_ap_5.txt` and manually resolve the cases where code could not give Lid properly i.e. search for '.XYZ' placeholder and make manual adjustment.
6. `tmp_ap_5.txt` was merged into csl-orig/v02/ap/ap.txt by `cd /path/to/csl-orig` and `git merge-file v02/ap/ap.txt /path/to/issue23/tmp_ap_0.txt /path/to/issue23/tmp_ap_5.txt`. This will generate a new v02/ap/ap.txt file.
7. Manually resolve git conflicts if any by searching for '>>>>>>>'. There were three such cases on my run.

_Dr. Mārcis Gasūns_
