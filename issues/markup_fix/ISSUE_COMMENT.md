### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `ap.txt`.

I ran the same two-job recipe over `csl-orig/v02/ap/ap.txt`: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `issues/markup_fix/` folder on the branch `markup-fix-audit`.

@funderburkjim @Andhrabharati — would value a look at the 528 within-line adjacent `</ab> <ab>` cases and the 4 `<ab n="…">` non-standard attribute values.

## Markup fixer + audit for `ap.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>N.</ab> of a river</ab>` | `<ab>N. of a river</ab>` |
| `<ab n=X><ab>Ns.</ab></ab>` | `<ab n=X>Ns.</ab>` |
| `<ls>MS. 12. 1. 10. </ls>` | `<ls>MS. 12. 1. 10.</ls>` |
| `<ab> m. </ab>` | `<ab>m.</ab>` |

Whitespace trimming applies to all 9 paired tags that actually occur in `ap.txt`: `<ls>`, `<ab>`, `<lex>`, `<lang>`, `<ns>`, `<sab>`, `<hom>`, `<is>`, `<Poem>`. The original file is never modified — output goes to `ap_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format).

### Closing-tag inventory in current `ap.txt`

| Tag | Count |
|---|---:|
| `</ls>` | 68,272 |
| `</ab>` | 32,858 |
| `</lex>` | 30,182 |
| `</lang>` | 1,538 |
| `</ns>` | 1,309 |
| `</sab>` | 468 |
| `</hom>` | 12 |
| `</is>` | 10 |
| `</Poem>` | 1 |

No self-closing tags. All paired tags are balanced. `<ns>` and `<sab>` are AP-specific paired tags not found in PWG/PWK/WIL.

### What it found in current `ap.txt`

- **0** nested `<ab>` — clean.
- **1** whitespace trim — applied: L151977, trailing space in `<ls>MS. 12. 1. 10. </ls>` → `<ls>MS. 12. 1. 10.</ls>`.
- **4** `<ab n="…">` attributes with non-standard values:
  - L132970 — `<ab n="Southern Maharāṣṭra">S. M.</ab>`
  - L211691 — `<ab n="Terminalia">T.</ab>`
  - L214120 — `<ab n="Names">Ns.</ab>`
  - L389467 — `<ab n="line">l.</ab>`
- **0** nested `<ls>` — clean outside and inside correction records. (457 `{{old → new || …}}` correction records present.)
- **0** boundary collisions — clean on all collision patterns.
- **528** within-line adjacent `</ab> <ab>` — listed in `markup_audit.txt` for verification (532 total when matching across line boundaries). Spot checks show mostly intentional pairs; verify rather than auto-merge.

### Broader cleanup checklist (in `markup_audit.txt`)

1. **Adjacent `</ab> <ab>`** (528 within-line) — verify each pair is intentional.
2. **`<ab n="…">` non-standard values** (4 occurrences) — decide whether to standardise or leave as readable tooltips.
3. **`<ns>` tag** (1,309 occurrences) — AP-specific; review content for well-formedness (`grep -n '<ns>' ap.txt | head`).
4. **`<sab>` tag** (468 occurrences) — AP-specific; review similarly.
5. **Nested `<ab>` / `<ls>` guards** — both 0; retained for re-run safety.

### Usage

```
cd issues/markup_fix
python 08_markup_fix.py                        # uses csl-orig/v02/ap/ap.txt by default
python 08_markup_fix.py IN.txt OUT.txt         # custom paths
```

Outputs: `ap_fixed.txt`, `markup_fix_changes.txt`, `markup_audit.txt`.

### Summary

`ap.txt` uses 9 paired tag types, all balanced. One auto-fix applied (L151977 trailing space in `<ls>`). Non-trivial findings: 528 within-line adjacent `</ab> <ab>` pairs and 4 `<ab n="…">` non-standard attribute values for human review. Zero boundary collisions and zero nested tags.

### Severity

`minor`
