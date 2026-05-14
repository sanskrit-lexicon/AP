# Issue 17 — Elevating Compound Headwords (˚ Pattern)

## Overview

This issue elevates headwords identified by the inline pattern `{#˚word#}` within
dictionary entries into standalone top-level headword entries, following the same
workflow as issue16.

**Pattern**: `{#˚` — i.e. `{#˚word1, ˚word2#}` fragments embedded in entry body text.

## Example

### Input

```
<L>12240.024<pc>0571-2<k1>kinnaraH<k2>kinnaraH<e>2
{#kim#} + {#-naraH#}¦ a bad or deformed man; a mythical being with a human figure
 and the head of a horse ({#aSvamuKa#}); {#jayodAharaRaM bAhvorgApayAmAsa#}
 {#kinnarAn#} <ls>R. 4. 78</ls>; {#udgAsyatAmicCati kinnarARAM tAnapradAyitvamivopagantum#}
 <ls>Ku. 1. 8</ls>. {#˚ISaH, ˚ISvaraH#}
∙²1 an epithet of Kubera.
∙²2 a kind of musical instrument.
<LEND>
```

### Expected Output (after Step 2 + Step 4)

```
<L>12240.024<pc>0571-2<k1>kinnaraH<k2>kinnaraH<e>2
{#kim#} + {#-naraH#}¦ a bad or deformed man; a mythical being with a human figure
 and the head of a horse ({#aSvamuKa#}); {#jayodAharaRaM bAhvorgApayAmAsa#}
 {#kinnarAn#} <ls>R. 4. 78</ls>; {#udgAsyatAmicCati kinnarARAM tAnapradAyitvamivopagantum#}
 <ls>Ku. 1. 8</ls>.
<LEND>

<L>12240.025<pc>0571-2<k1>kinnareSaH<k2>kinnareSaH<e>3
{#kim#} + {#-naraH#} + {#˚ISaH, ˚ISvaraH#}¦
∙²1 an epithet of Kubera.
∙²2 a kind of musical instrument.
<LEND>

<L>12240.026<pc>0571-2<k1>kinnareSvaraH<k2>kinnareSvaraH<e>3
{{Lbody=12240.025}}
<LEND>
```

Note: After Step 2, new L numbers carry the `.XYZ` placeholder (e.g. `12240.024.XYZ`).
Step 4 resolves these to permanent incrementing values (e.g. `12240.025`, `12240.026`).

---

## Step 2

Identify entries containing `{#˚...#}` and split them.

`tmp_ap_0.txt` was taken from `csl-orig/v02/ap/ap.txt` as it stood on the commit c464962b97d34015a95ab106c10618054fa39e3d dated 14 May 2026.

```
python3 step2.py tmp_ap_0.txt tmp_ap_2.txt log2.tsv
```

### Logic

1. **Pattern detection**: Searches each entry body line for `{#˚word1, ˚word2#}`.
2. **Parent entry**: The matched `{#˚...#}` fragment is removed from its line.
   All `∙²` definition lines that follow are also removed from the parent and
   moved into the new derived entry.
3. **Headword resolution**: Each `˚suffix` is resolved to a full headword using
   the base headword (`k1`) and Sanskrit sandhi rules (e.g. `kinnara` + `ISaH` →
   `kinnareSaH` via `a + I → e` sandhi). Falls back to `manually_mapped.tsv` if
   automatic resolution fails.
4. **New entries**: One new `<L>` entry per suffix:
   - **First suffix**: full definition line (`pref + {#˚...#}¦`) plus `∙²` body lines.
   - **Subsequent suffixes**: `{{Lbody=LID.XYZ}}` pointing to the first new entry.
5. **Placeholders**:
   - Unresolved headwords: `k1`/`k2` marked `.ABC`, L number marked `.XYZ`.
   - All new L numbers marked `.XYZ` (resolved in Step 4).

`log2.tsv` — tab-separated: `Lnum`, `basehw`, `suffix`, `resolution`.
Unresolved entries show `None` in the resolution column.

### Verification

```
cat tmp_ap_2.txt | grep '.ABC' | wc -l
# should equal:
cat log2.tsv | grep 'None' | wc -l
# both should be 0 after filling manually_mapped.tsv

cat tmp_ap_2.txt | grep '<L>.*\.XYZ' | wc -l
# should equal (cat log2.tsv | wc -l) - 1 (header)

cat tmp_ap_2.txt | grep '\.XYZ' | wc -l
# = above + number of Lbody entries (multi-suffix entries)
```

---

## Step 3

Check resolved headwords against `sanhw1.txt` (list of valid Sanskrit words).

```
python3 step3.py
```

Reads `log2.tsv`, writes `log3.tsv` with an additional `in_sanhw1` column
(`True`/`False`). Also tries stripping trailing `H` or `m` before checking.

---

## Step 4

Replace `.XYZ` placeholder L numbers with permanent incrementing values and
resolve `{{Lbody=...XYZ}}` references.

```
python3 step4.py
```

Takes `tmp_ap_2.txt` → produces `tmp_ap_4.txt` and `log4.tsv`.

### Key Logic

1. **L Number Resolution**: Every `<L>` ending in `.XYZ` gets an incrementing
   even numeric suffix (`.002`, `.004`, …) that does not conflict with existing L numbers.
2. **Conflict Prevention**: Pre-scans all existing L numbers before assigning new ones.
3. **Lbody Mapping**: `{{Lbody=BASE.XYZ}}` references are updated to point to the
   numeric L assigned to the first new entry for that base.

---

## manually_mapped.tsv

A TSV file (columns: `Lnum`, `basehw`, `suffix`, `resolution`) providing manual
resolutions for cases where automatic sandhi inference fails.
Step 2 uses this as a fallback after automatic resolution returns `None`.

---

## Merger

Once `tmp_ap_4.txt` is produced, merge with `csl-orig/v02/ap/ap.txt`:

```
cd sanskrit-lexicon/csl-orig/
git merge-file v02/ap/ap.txt ../AP/issues/issue17/tmp_ap_0.txt ../AP/issues/issue17/tmp_ap_4.txt
```

Conflicts (if any) can be identified by searching for `>>>>>` and resolved manually.
