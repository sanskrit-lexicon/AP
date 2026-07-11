# PIPELINE_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/AP/blob/main/docs/PIPELINE_MANUAL.md)
— purpose, provenance, improvement backlog and revision history of the manual
itself (not of the pipelines it documents).

## Purpose

Give a new operator/contributor a runnable understanding of the AP `issues/`
pipeline family — above all the hidden-headword step-pipeline (issues
16/17/23/25), the L-number system it rests on, the `git merge-file` delivery
idiom, and the pattern for opening a new issue folder — without reading the
source code first, and within the org's csl-orig batched-PR delivery rule.

## Audience

- **Operators** opening a new split/correction campaign (cheat-sheet,
  new-issue walkthrough, symptom table);
- **Maintainers** touching the step scripts or `manually_mapped.tsv` files
  (L-number section, appendix invariants + traps);
- **Historians** of the AB reconciliation (issue8–8e) and the compounds
  install (issue9/10/12).

## Provenance

- Authored 11-07-2026 by Fable 5 (`claude-fable-5`) executing handoff
  [H524-Fable_AP_extraction_validation_manual_10.07.26.md](https://github.com/gasyoun/Uprava/blob/main/handoffs/H524-Fable_AP_extraction_validation_manual_10.07.26.md)
  (manual-coverage census batch H501–H531).
- Modelled on the gold-standard operator manual
  [RussianRamayana Litpam-Indexator MANUAL.md](https://github.com/gasyoun/RussianRamayana/blob/main/Litpam-Indexator/docs/indesign-pipeline/MANUAL.md).
- Source material: the 24 per-folder READMEs/notes under
  [issues/](https://github.com/sanskrit-lexicon/AP/tree/main/issues)
  (issue23/25 read directly; the rest surveyed by an Explore agent, Fable 5
  `claude-fable-5` session, 11-07-2026). Commands quoted verbatim; counts
  (8,518 / 1,900 / 79,815→88,333, resolution and validation splits) are the
  ones recorded in the executed runs' READMEs and TSV logs.
- Two defects in existing docs found and flagged rather than propagated:
  `issues/readme.txt` stale (stops at issue12);
  [CLAUDE.md](https://github.com/sanskrit-lexicon/AP/blob/main/CLAUDE.md)'s
  "typical issue workflow (e.g., issue25)" example describes issue16/23's
  4-step shape, not issue25's 2-step reality.

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Parameterize the hardcoded machine paths (`SANHW1_PATH` in issue16/23 `step3.py`, issue25 `redo.sh`'s relative csl-orig) via an env var or a small `config.py` — kills the #1 first-run failure | open |
| 2 | Rewrite [issues/readme.txt](https://github.com/sanskrit-lexicon/AP/blob/main/issues/readme.txt) from the manual's folder map (stale since issue12; lists a folder-less issue7) | open |
| 3 | Fix CLAUDE.md's issue25 example to match reality (2-step) and point its "Running the Pipeline" section at this manual | open |
| 4 | Live-verify `markup_fix/08_markup_fix.py` and issue25's `redo.sh` against current siblings and record fresh output in the manual (the only two fire-and-forget candidates) | open |
| 5 | Close the issue6 `cl.` residual gender-markup case, or record a won't-fix in that folder's notes | open |
| 6 | A short `docs/` note on when to rebuild hwnorm1/hwnorm2 sqlite DBs after headword-population changes (currently buried in issue12's readme_hwnorm1/readme_dalglob1) | open |

## Known limitations

- **Commands are transcription-verified, not re-executed.** The pipelines
  mutate the sibling csl-orig working tree, the big campaigns are commit-
  pinned and already landed ("re-running finds no patterns"), and step3
  requires a maintainer-machine path edit — so the manual quotes the in-repo
  READMEs verbatim and verifies files/paths exist instead of re-running.
  Backlog #4 upgrades the two safe candidates.
- Per-folder coverage of the issue8–8e campaign is summary-level (its
  `db_comp` review loop is semi-manual and historical); the folder readmes
  remain the authority for reviving it.
- The XAMPP/macOS path remapping guidance assumes the current flat `GitHub/`
  checkout convention.

## Related documents

- [README.md](https://github.com/sanskrit-lexicon/AP/blob/main/README.md) — repo overview, timeline, issue typology
- [CLAUDE.md](https://github.com/sanskrit-lexicon/AP/blob/main/CLAUDE.md) — code contract (data flow, entry format, conventions)
- [csl-corrections correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — the canonical csl-orig delivery procedure this manual defers to
- Sibling manuals from the same census batch: [PWK docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md), [AMAR docs/CONVERSION_MANUAL.md](https://github.com/sanskrit-lexicon/AMAR/blob/main/docs/CONVERSION_MANUAL.md)

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial manual + this metadoc authored (H524); 24 issue folders surveyed (issue23/25 first-hand + 1 Explore agent); two stale-doc defects flagged | Fable 5 (`claude-fable-5`) |

_Dr. Mārcis Gasūns_
