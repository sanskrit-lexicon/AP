# AP pipelines — operator manual

_Created: 11-07-2026 · Last updated: 11-07-2026_

This is the **operator manual** for the AP repository: how the numbered
`issues/` pipelines for Apte's *Sanskrit-English Dictionary* (1957) work, how
to re-run the re-runnable ones, and how to open a new one — without reading
the source code first. The centerpiece is the **hidden-headword step-pipeline
family** (issues 16 → 17 → 23 → 25) that grew the dictionary by 8,518 + 1,900
entries, plus the **L-number system** those splits rest on.

Three documents describe this repo, with different jobs:

- **What the repo is** (timeline, issue typology, labels) —
  [README.md](https://github.com/sanskrit-lexicon/AP/blob/main/README.md);
- **Code contract for AI/code sessions** (data flow, entry format, script
  table) — [CLAUDE.md](https://github.com/sanskrit-lexicon/AP/blob/main/CLAUDE.md);
- **How to operate the pipelines** (this document) —
  [docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/AP/blob/main/docs/PIPELINE_MANUAL.md).

Commands below are quoted verbatim from the per-issue `README.md`/`readme.txt`
notes; paths and scripts were verified to exist in the tree on 11-07-2026.
The counts (1,900 / 8,518 / 79,815 → 88,333) are the ones recorded in those
notes at execution time.

## Cheat-sheet: the hidden-headword step pipeline

The canonical modern shape ([issues/issue23/](https://github.com/sanskrit-lexicon/AP/tree/main/issues/issue23);
issue25 is the trimmed 2-step variant with the cleanest `redo.sh`):

```sh
cd issues/issue23
# 0. Baseline: a commit-pinned snapshot of the upstream text
git -C <csl-orig> show <commit>:v02/ap/ap.txt > tmp_ap_0.txt

# 1-2. Split hidden headwords out of suffix patterns; resolve suffix → full headword
python3 step2.py tmp_ap_0.txt tmp_ap_2.txt log2.tsv
#   auto-resolution via adjust_hw() heuristics; fallback = manually_mapped.tsv;
#   new entries get L-placeholder ".XYZ"; unresolvable k1/k2 marked ".ABC"

# 3. Validate every resolution against the Sanskrit headword list
python3 step3.py            # log2.tsv -> log3.tsv (+ in_sanhw1 column)
#   !! edit SANHW1_PATH inside step3.py first — see Environment

# 4. Assign permanent L-numbers (.XYZ -> .002/.004/...), rewire {{Lbody=...}}
python3 step4.py            # tmp_ap_2.txt -> tmp_ap_4.txt + log4.tsv

# 5. Manual pass: copy tmp_ap_4.txt -> tmp_ap_5.txt, search ".XYZ", resolve L clashes

# 6. Deliver via three-way merge into the live upstream file
cd <csl-orig>
git merge-file v02/ap/ap.txt <issue>/tmp_ap_0.txt <issue>/tmp_ap_5.txt
grep -n ">>>>>>>" v02/ap/ap.txt      # resolve conflicts by hand (3 on the real run)
# then validate (generate_dict.sh ap + xmlchk) and deliver per the batched-PR rule
```

Expected shape of the numbers (from the executed runs):

| Run | Pattern | Split | Auto-resolved | sanhw1-validated | Entry growth |
|---|---|---|---|---|---|
| [issue16](https://github.com/sanskrit-lexicon/AP/tree/main/issues/issue16) | `.{@{#-suffix#}@}` | 8,518 | vs 383 manual mappings | 8,273 True / 245 False (manually vetted) | 79,815 → 88,333 `<L>` |
| [issue23](https://github.com/sanskrit-lexicon/AP/tree/main/issues/issue23) | + `.({@{#-suffix#}@})` | 1,900 | 1,899 (1 typo fixed at source) | 1,803 / 97 (manually vetted) | +1,900 |
| [issue25](https://github.com/sanskrit-lexicon/AP/tree/main/issues/issue25) | parenthetical `({@{#-suffix#}@})` | (2-step: `step1.py` split, `step2.py` L-resolution) | — | — | see its [README](https://github.com/sanskrit-lexicon/AP/blob/main/issues/issue25/README.md) |

**Do-not-re-run marker:** issue16/23/25's corrections are already merged into
csl-orig — re-running against the current text finds no matching patterns
(issue23 README says so explicitly). Re-run them only against their pinned
baseline commits, to reproduce; run the *pattern* against fresh text only when
opening a **new** split campaign.

## The L-number system

Everything in this repo rests on entry identity:

| Form | Meaning |
|---|---|
| `<L>29` | base entry (from the original digitization) |
| `<L>29.002`, `29.004` | sub-entries created by a split campaign — `step4.py` assigns even, incrementing suffixes, conflict-checked against the pre-existing L set |
| `.XYZ` | temporary placeholder during step2 (must be zero after step 5) |
| `.ABC` | failed auto-resolution in `<k1>`/`<k2>` — needs a `manually_mapped.tsv` row |
| `{{Lbody=ID}}` | body-side reference to a parent entry; step4 rewires these from `.XYZ` to the final numbers (401 in issue16) |

After any split campaign, **L-number monotonicity must be re-checked** — that
is exactly what [issues/issue24/](https://github.com/sanskrit-lexicon/AP/tree/main/issues/issue24)
does (`check_order.py` → reordered `tmp_ap_1.txt` + `log.tsv`).

The entry format itself (metaline `<L>ID<pc>page<k1>hw<k2>variant<h>hom<e>etym`
… body … `<LEND>`) is documented in
[CLAUDE.md § Dictionary Entry Format](https://github.com/sanskrit-lexicon/AP/blob/main/CLAUDE.md#dictionary-entry-format);
`parseheadline.py` (vendored per folder) parses it.

## Map of the issue folders

The committed index [issues/readme.txt](https://github.com/sanskrit-lexicon/AP/blob/main/issues/readme.txt)
is **stale** (stops at issue12); the live map, grouped by concern:

| Concern | Folders | Status |
|---|---|---|
| Repo bootstrap | issue1 (make `ap.txt` public in csl-orig, 28-commit history transfer) | done 07-2025 |
| Tooltips & display | issue2 (`<ab>` tooltips), issue6 (gender → `<lex>`), issue13 (verb-class TSV dump), issue14 (`<ls>` author tooltips), issue19 (`<ls>` scan link-targets + 15 print-change corrections) | done; link work continues in new issues |
| Global text corrections | issue3 (`b`→`v` Sanskrit globals, AB v3 ingest), issue4 (extended-ASCII audit), issue5 (Devanagari inside `<ls>`) | done |
| **AB reconciliation campaign** | issue8 → 8a → 8b → 8c → 8d → 8e — one linear Feb-2026 campaign reconciling Andhrabharati's `AP57_AB_v4a.txt` against CDSL `ap.txt`, one markup category at a time (`db_comp.py` options 1–18) | historical; semi-manual, not a button |
| Compounds & alternate headwords | issue9 (classify alternates) → issue10 (compound study, ScharfSandhi joins, dictcheck) → issue12 (**the big install**: `compounds.py` + `althws.py` + `meta_e.py` → +209,758/−75,650-line csl-orig commit, plus hwnorm1/hwnorm2 sqlite rebuilds) | historical |
| **Hidden-headword splits** | issue16 (8,518) → issue17 (`˚` pattern — **automation abandoned 03-06-2026**, manual from `log2.tsv`) → issue23 (1,900) → issue25 (parenthetical, 2-step) → issue24 (L-order re-check) | the live pattern for new split campaigns |
| Markup QA | [markup_fix/](https://github.com/sanskrit-lexicon/AP/tree/main/issues/markup_fix) — AP counterpart of the PWG issue174 fixer family: `python 08_markup_fix.py` (defaults to sibling csl-orig `ap.txt`; audit + auto-fix + updateByLine-style change log; `test_markup_fix.py` = 14 synthetic tests) | **re-runnable, self-contained** |

Two authorship eras explain the styles you'll see: the issue1–14/19 folders
(funderburkjim, Git-Bash/XAMPP paths, `redo_ap.sh` render loops) and the
step-pipeline folders 16/17/23/24/25 (Dhaval, macOS paths, `stepN.py` +
TSV logs).

## Environment and prerequisites

- **Python 3**, standard library only (no pip packages). Repo conventions:
  `codecs.open(..., 'utf-8')`, `sys.stdout.reconfigure(encoding='utf-8')`,
  TSV logs with header rows. Vendored in-repo where needed: `sandhi/`
  (ScharfSandhi), `dalglobpy/` (dictcheck), `transcoder/` (slp1↔deva) inside
  issue5/8/10/12.
- **Git Bash / POSIX shell** for the `redo*.sh` drivers.
- **Sibling checkouts** (expected beside this repo or under the historical
  `/c/xampp/htdocs/cologne/` layout): [csl-orig](https://github.com/sanskrit-lexicon/csl-orig)
  (`v02/ap/ap.txt` — every baseline is `git show <commit>:v02/ap/ap.txt`),
  [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork)
  (`generate_dict.sh`, `xmlchk_xampp.sh`), csl-websanlexicon + csl-apidev
  (display PHP), [hwnorm1](https://github.com/sanskrit-lexicon/hwnorm1) —
  **the home of `sanhw1.txt`** — and hwnorm2 (search DBs), PWG (borrowed
  `lsextract_all.py` + scan link-targets), `APScan/2020/` (scan images, on
  the Cologne server).
- **Hardcoded paths are the #1 porting task.** Nothing is parameterized:
  funderburkjim-era scripts assume `/c/xampp/htdocs/...`; Dhaval-era scripts
  assume `/Users/dhaval/Documents/GithubRepos/...` —
  `issues/issue16/step3.py` and `issues/issue23/step3.py` hardcode
  `SANHW1_PATH` to that Mac home, and `issues/issue25/redo.sh` reaches
  csl-orig via a fragile `../../../../sanskrit-lexicon/csl-orig` relative.
  **Edit the path constants before running anything on your machine.**
- No secrets, no network access.

## Delivery — batched PR, and the merge-file idiom

Corrections are **never pushed directly to csl-orig** by operator/agent
sessions: prepare and XML-validate locally, then deliver per the canonical
[correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md)
as one consolidated batch PR (org rule; the README states it too). The
historical direct-commit blocks in old readmes are the upstream maintainers'
pattern, not yours.

AP's distinctive delivery mechanic is **`git merge-file`** (three-way merge:
current upstream / your pinned baseline / your final temp), which lets a
campaign land cleanly even after csl-orig moved during the work — at the cost
of hand-resolving `>>>>>>>` conflict markers (three on the real issue16 and
issue23 runs). Always `grep ">>>>>>>"` before validating.

Validation before delivery is always the csl-pywork pair:

```sh
cp <final_temp> <csl-orig>/v02/ap/ap.txt
cd <csl-pywork>/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap        # expect ok
```

`redo_ap.sh <ap_file> <app_dir>` (present in issue3/5/8–8e/9/10) wraps
exactly this as a **throwaway local render**: it copies the candidate in,
builds and validates, then **`git restore`s csl-orig's `ap.txt`** — a
`redo_ap.sh` run never persists anything.

## Walkthrough — opening a NEW issue folder

1. **Create `issues/issueNN/`** matching your GitHub issue number. Copy in
   `parseheadline.py` (and `manually_mapped.tsv` as an empty-but-headered TSV
   if you'll do headword resolution) from issue23.
2. **Pin the baseline** and record the hash in your README:
   `git -C <csl-orig> show <hash>:v02/ap/ap.txt > tmp_ap_0.txt`.
   The `tmp_*`/`temp_*` files stay untracked; the committed deliverables are
   the scripts, the TSV logs, and the README with real counts.
3. **Write step scripts, not one script.** The house pattern separates
   transform (`step2.py`) / validate (`step3.py`) / finalize (`step4.py`),
   each emitting a TSV log — that separation is what made issue16's 8,518-entry
   change reviewable. Reuse `adjust_hw()` from issue23 for suffix resolution.
4. **Prefer a self-contained `redo.sh`** in the issue25 style (fetches its
   own baseline, runs the steps, round-trip-verifies the manual edits with
   `diff`/`patch`) — it is the only fully reproducible driver in the repo.
5. **Validate, then deliver** per the section above; document the actual
   `git merge-file` conflict count in the README.
6. Post-landing: re-check L-order (issue24's `check_order.py`) if you created
   sub-entries, and rebuild the hwnorm1/hwnorm2 search DBs if you changed the
   headword population (see
   [issue12's readme_hwnorm1.txt](https://github.com/sanskrit-lexicon/AP/blob/main/issues/issue12/readme_hwnorm1.txt)).

## Symptom → cause → cure

| Symptom | Cause | Cure |
|---|---|---|
| `step3.py`: `FileNotFoundError: /Users/dhaval/...` | Hardcoded `SANHW1_PATH` | Point it at your sibling [hwnorm1](https://github.com/sanskrit-lexicon/hwnorm1) checkout's `sanhw1/sanhw1.txt` (regenerate there with `sh redo.sh` if stale) |
| `issue25/redo.sh` can't find csl-orig | Fragile `../../../../sanskrit-lexicon/csl-orig` relative | Run from inside `issues/issue25/` with csl-orig at the expected depth, or edit the path |
| step2 finds **zero** matches on current `ap.txt` | The campaign already landed in csl-orig (issue16/23/25 are done) | Expected — re-run only against the pinned baseline commit; a new campaign needs a new pattern |
| `.XYZ` survives into your final file | Step 5 (manual `tmp_ap_5.txt` pass) skipped | Search `.XYZ` and `.ABC`; every one needs a manual resolution or a `manually_mapped.tsv` row, then re-run step4 |
| `git merge-file` leaves `>>>>>>>` in `ap.txt` | Upstream moved between your baseline and delivery — expected behaviour | Resolve by hand (real runs had 3), then validate; never deliver without `grep ">>>>>>>"` |
| `xmlchk` fails after your pass | Broken tag pairing or unescaped `&` | `apab_input.txt`-style inputs need XML escaping (`&c.` → `&amp;c.`, issue2); diff the failing entries named by `generate_dict.sh` |
| csl-orig dirty after a render | `redo_ap.sh` aborted before its `git restore` | `git -C <csl-orig> status` after every render; `git restore v02/ap/ap.txt` |
| Mojibake / odd glyphs (`━`, `−`, `∙²`, `¦`, `⁞`, non-BMP `U+1F784`) | AP's text uses extended-ASCII + non-BMP markers semantically (issue4/8 inventory) | UTF-8 environment only; never "normalize" a glyph without checking the issue4/8 notes for its meaning |
| `db_comp.py` output confusing | It's option-numbered (1–18 accrued across issue8–8e) and expects the human review loop (edit marked file, `'_'→''`, re-validate) | Treat issue8* as historical record; read [issues/issue8/readme.txt](https://github.com/sanskrit-lexicon/AP/blob/main/issues/issue8/readme.txt) before reviving |
| Tempted to automate the `˚` pattern | issue17 tried; abandoned 03-06-2026 for false positives | That class is manual-from-`log2.tsv` by decision — don't re-automate without new evidence |

## Glossary

| Term | Meaning here |
|---|---|
| AP | V. S. Apte, *The Practical Sanskrit-English Dictionary*, revised ed. 1957–59; dictionary code `ap` |
| hidden headword | a sub-headword the print edition tucks into a parent entry as a bare suffix (`.{@{#-SaH#}@}`); the split campaigns promote these to real entries |
| L-number | the stable entry identifier (`<L>29`, sub-entries `29.002`); see [the L-number system](#the-l-number-system) |
| `.XYZ` / `.ABC` | step2's temporary L placeholder / failed-resolution marker — both must be gone before delivery |
| `adjust_hw()` | the suffix→full-headword heuristic in step2 (sandhi-aware join of base headword + suffix) |
| `manually_mapped.tsv` | per-issue manual fallback for resolutions the heuristics miss (383 rows in issue16, 208 in issue23) |
| `sanhw1.txt` | the cross-dictionary Sanskrit headword list from the sibling [hwnorm1](https://github.com/sanskrit-lexicon/hwnorm1) repo; step3's validation reference |
| AB / Andhrabharati | Nagabhushana Rao's independent digitization (`AP57_AB_v4a.txt`), reconciled category-by-category in issue8–8e |
| `db_comp.py` | the option-numbered comparison engine of that campaign (options 1–18) |
| `redo_ap.sh` | throwaway local render+validate of a candidate `ap.txt` (always ends in `git restore`) |
| `git merge-file` | AP's three-way delivery idiom: current upstream × pinned baseline × final temp |
| ScharfSandhi / `dalglobpy` | vendored sandhi-joiner and dictionary-checker used by the compounds work (issue10/12) |

## Maintainer appendix

### Per-folder tooling is frozen, not shared

`parseheadline.py`, `manually_mapped.tsv`, `updateByLine.py`-style appliers
and the vendored `sandhi/`/`dalglobpy/`/`transcoder/` copies are duplicated
per issue folder **deliberately** — each folder is a frozen, self-contained
record of what actually ran. Fix bugs forward (in the newest folder), never
retroactively.

### Invariants

1. **Baselines are commit-pinned**: every `tmp_ap_0.txt` is
   `git show <hash>:v02/ap/ap.txt`; the hash is in the folder's README.
2. **Placeholders never ship**: `.XYZ`/`.ABC` count must be zero in the
   delivered file.
3. **Sub-entry L-numbers are even-incrementing** (`.002`, `.004`, …) and
   conflict-checked against the existing L set; `{{Lbody=}}` refs are rewired
   in the same pass.
4. **Renders are throwaway; installs are explicit** — only a `cp` + commit
   block (historically) or a batch-PR delivery (now) changes csl-orig.
5. **TSV logs are the audit trail** — `log2/3/4.tsv` carry the per-entry
   evidence for every split; they are committed even though the temps aren't.

### Known traps and observed defects

1. **`issues/readme.txt` is stale** (stops at issue12, lists a folder-less
   issue7). The [map above](#map-of-the-issue-folders) supersedes it; fixing
   the file is backlog item #2 in the metadoc.
2. **Hardcoded author-machine paths** (Mac home in step3 of 16/23; XAMPP
   roots elsewhere) — the single biggest first-run failure source.
3. **`CLAUDE.md`'s "typical issue workflow (e.g., issue25)" example is
   inaccurate**: issue25 is a 2-step pipeline (`step1.py` + `step2.py`); the
   4-step `step1..step4` prose actually describes issue16/23 (and no folder
   has a `step1.py` except issue25). Trust the per-folder READMEs.
4. **issue17 is a graveyard with live-looking scripts** — automation
   abandoned; its `log2.tsv` drives manual edits only.
5. **issue8c's Devanagari pass is explicitly NOT DONE** (`d_comp.py` there);
   the campaign endpoint is issue8e's `ap_0j_5`.
6. **`sanhw1.txt` drifts**: it is regenerated in hwnorm1 (`sh redo.sh`); a
   stale copy silently inflates step3's `False` count.
7. **issue2's XML-escaping requirement** (`&c.` → `&amp;c.` in
   `apab_input.txt`) recurs any time a tooltip input gains an ampersand.
8. **issue6 left one `cl.` case unresolved** ("not yet done" in its notes) —
   a micro-gap for a future gender-markup pass.

Improvement backlog, provenance and revision history live in the companion
metadoc:
[docs/PIPELINE_MANUAL.meta.md](https://github.com/sanskrit-lexicon/AP/blob/main/docs/PIPELINE_MANUAL.meta.md).

_Dr. Mārcis Gasūns_
