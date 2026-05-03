# Issue 25: Splitting ({@{#-suffix#}@}) entries

This issue involves identifying entries that contain a suffix in parentheses like `({@{#-SaH#}@})` and splitting them into separate headword entries.

`temp_ap_0.txt` is taken as of `34263ba59be878831ab802ee52d17665695bcd5b` in `csl-orig` repository.

## Steps

### 1. Initial Split

Run `step1.py` to identify and split the entries. This script creates new entries with placeholder L-numbers ending in `.XYZ`.

```bash
python3 step1.py temp_ap_0.txt temp_ap_1.txt temp_log1.tsv
```

### 2. L-number Resolution

Run `step2.py` to resolve the `.XYZ` placeholders to permanent numeric L-numbers.

```bash
python3 step2.py temp_ap_1.txt temp_ap_2.txt temp_log2.tsv
```

### 3. Manual Mapping

Copied temp_ap_2.txt to temp_ap_3.txt and made manual corrections.

### 4. Copy temp_ap_3.txt to csl-orig repository

Manually corrected temp_ap_3.txt was copied to csl-orig/v02/ap/ap.txt and pushed at commit <https://github.com/sanskrit-lexicon/csl-orig/commit/ff787649fa396a5d2e22cb49ef6c0e58fd6db8e4>. This commit has all the diffs related to Issue 25.

## Files

- `temp_ap_0.txt`: Original dictionary file.
- `temp_ap_1.txt`: Output of Step 1 (with `.XYZ` placeholders).
- `temp_ap_2.txt`: Final output of Step 2 (with resolved L-numbers).
- `temp_log1.tsv`: Log of splits and headword resolutions.
- `temp_log2.tsv`: Log of L-number assignments.
- `manually_mapped.tsv`: Optional file for manual headword resolutions (fallback for "None" results).
- `step1.py`: The splitting script.
- `step2.py`: The L-number resolution script.
- `parseheadline.py`: Utility for parsing metalines.
- `redo.sh`: Shell script to run all steps.
