"""
Markup fixer + audit for ap.txt (AP).

Counterpart of pwgissues/issue174/08_markup_fix.py (PWG),
pwkissues/markup_fix/08_markup_fix.py (PWK), and siblings.

Two jobs:
  1. FIX: nested <ab> + whitespace inside all paired tags.
  2. AUDIT: everything else with line refs (no auto-modification).

AP-specific notes vs sibling dictionaries:
  - Paired tags: <ls> (68,272), <ab> (32,858), <lex> (30,182),
    <lang> (1,538), <ns> (1,309), <sab> (468), <hom> (12),
    <is> (10), <Poem> (1). All balanced.
  - One trailing-space hit in <ls> (L151977).
  - 532 adjacent </ab> <ab> pairs — mostly intentional, for review.
  - 4 <ab n="…"> with non-standard values ("Southern Maharāṣṭra",
    "Terminalia", "Names", "line") — audit only.
  - 457 {{old -> new || …}} correction records present.
  - <ns> and <sab> are AP-specific paired tags not in PWG/PWK.

Inputs:
  ../../../csl-orig/v02/ap/ap.txt      (when run from apissues/markup_fix/)
  or argv[1] (any path)

Outputs:
  ap_fixed.txt              -- repaired copy
  markup_fix_changes.txt    -- log of every auto-fix
  markup_audit.txt          -- audit findings with line refs

Usage:
  python 08_markup_fix.py            # uses default in/out paths
  python 08_markup_fix.py IN OUT     # custom paths
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent

if len(sys.argv) >= 3:
    PW_TXT = Path(sys.argv[1])
    OUT_FIX = Path(sys.argv[2])
else:
    candidates = [
        HERE.parent.parent.parent / "csl-orig" / "v02" / "ap" / "ap.txt",
        HERE / "ap.txt",
    ]
    PW_TXT = next((p for p in candidates if p.exists()), candidates[0])
    OUT_FIX = HERE / "ap_fixed.txt"

OUT_LOG = HERE / "markup_fix_changes.txt"
OUT_AUDIT = HERE / "markup_audit.txt"


NEST_RX = re.compile(
    r"<ab(?P<oa>\b[^>]*)>(?P<pre>[^<]*)<ab(?P<ia>\b[^>]*)>(?P<inner>[^<]*)</ab>(?P<post>[^<]*)</ab>"
)


def fix_nested_ab(line):
    n_fixed = 0
    while True:
        m = NEST_RX.search(line)
        if not m:
            return line, n_fixed
        oa, pre, inner, post = m.group("oa"), m.group("pre"), m.group("inner"), m.group("post")
        line = line[:m.start()] + f"<ab{oa}>{pre}{inner}{post}</ab>" + line[m.end():]
        n_fixed += 1


# Paired tags in ap.txt: ls 68,272 | ab 32,858 | lex 30,182 | lang 1,538
# ns 1,309 | sab 468 | hom 12 | is 10 | Poem 1
TRIM_TAGS = ["ls", "ab", "lex", "lang", "ns", "sab", "hom", "is", "Poem"]


def fix_trim_whitespace(line):
    n = 0
    for tag in TRIM_TAGS:
        pat = re.compile(rf"(<{tag}\b[^>]*>)(\s+)([^<]*?)(\s*)(</{tag}>)")
        def _repl(m):
            nonlocal n
            inside = m.group(3).rstrip()
            if inside != m.group(2) + m.group(3) + m.group(4):
                n += 1
            return f"{m.group(1)}{inside}{m.group(5)}"
        line = pat.sub(_repl, line)
        pat2 = re.compile(rf"(<{tag}\b[^>]*>)([^<]*?)(\s+)(</{tag}>)")
        def _repl2(m):
            nonlocal n
            inside = m.group(2).rstrip()
            n += 1
            return f"{m.group(1)}{inside}{m.group(4)}"
        line = pat2.sub(_repl2, line)
    return line, n


def _ls_nested_classify(line):
    inside, outside = [], []
    for m in re.finditer(r"<ls\b[^>]*>([^<]*<ls\b[^>]*>)", line):
        inner_offset = m.group(1).find("<ls")
        inner_open = m.start(1) + (inner_offset if inner_offset >= 0 else 0)
        prefix = line[:inner_open]
        if prefix.rfind("{{") > prefix.rfind("}}"):
            inside.append(m)
        else:
            outside.append(m)
    return outside, inside


AUDIT_CHECKS = [
    ("Adjacent </ab> <ab> — possibly intentional but worth verifying",
     re.compile(r"</ab>\s*<ab")),
    ("Nested <ls> outside a {{ … }} correction record",
     None),
    ("Nested <ls> INSIDE a {{ … }} correction record (informational)",
     None),
    ("<ab n=\"?\"> or <ab n=\"???\"> placeholder",
     re.compile(r'<ab\s+n="\?+\">')),
    ("<ab n=\"\"> empty attribute",
     re.compile(r'<ab\s+n="">')),
    ("<ab n=\"…\"> non-standard expansion value",
     re.compile(r'<ab\s+n="(?!")[^"]{2,}">')),
    ("Empty content tag",
     re.compile(r"<(ls|ab|lex|lang|ns|sab|hom|is|Poem)\b[^>]*></\1>")),
    ("{#…#} closing brace immediately followed by <ab>/<ls>/<is>",
     re.compile(r"#\}<(?:ab|ls|is)\b")),
    ("{%…%} closing brace immediately followed by <is>",
     re.compile(r"%\}<is\b")),
    ("[PageN-NNN-N] glued to preceding </ls>.",
     re.compile(r"</ls>\.\[Page\d")),
    ("Malformed tag with unescaped < inside attribute value",
     re.compile(r'<[A-Za-z][A-Za-z0-9]*\s+[A-Za-z]+="[^"]*<[^"]*"\s*[^>]*>')),
]


def main():
    print(f"Reading {PW_TXT} …", flush=True)
    lines = PW_TXT.read_text(encoding="utf-8").splitlines()
    print(f"  {len(lines):,} lines", flush=True)

    out_lines, fix_log = [], []
    tot_nested = tot_trim = 0
    audit_hits = {label: [] for label, _ in AUDIT_CHECKS}

    for lineno, line in enumerate(lines, 1):
        orig = line
        line, n1 = fix_nested_ab(line)
        line, n2 = fix_trim_whitespace(line)
        tot_nested += n1
        tot_trim += n2
        if line != orig:
            fix_log.append((lineno, orig, line))
        out_lines.append(line)

        outside_hits, inside_hits = _ls_nested_classify(orig)
        for m in outside_hits:
            s, e = max(0, m.start()-40), min(len(orig), m.end()+40)
            audit_hits["Nested <ls> outside a {{ … }} correction record"].append((lineno, orig[s:e].replace("\t"," ")))
        for m in inside_hits:
            s, e = max(0, m.start()-40), min(len(orig), m.end()+40)
            audit_hits["Nested <ls> INSIDE a {{ … }} correction record (informational)"].append((lineno, orig[s:e].replace("\t"," ")))

        for label, pat in AUDIT_CHECKS:
            if pat is None:
                continue
            for m in pat.finditer(orig):
                s, e = max(0, m.start()-40), min(len(orig), m.end()+40)
                audit_hits[label].append((lineno, orig[s:e].replace("\t"," ")))
                if len(audit_hits[label]) >= 5000:
                    break
        if lineno % 200000 == 0:
            print(f"  {lineno:,}/{len(lines):,}", flush=True)

    print(f"Total nested <ab> repairs:    {tot_nested}", flush=True)
    print(f"Total whitespace trims:       {tot_trim}", flush=True)
    print(f"Total changed lines:          {len(fix_log)}", flush=True)

    with OUT_FIX.open("w", encoding="utf-8", newline="\n") as f:
        for line in out_lines:
            f.write(line + "\n")

    with OUT_LOG.open("w", encoding="utf-8") as f:
        f.write("; markup_fix log for ap.txt\n")
        f.write(f"; nested <ab>:    {tot_nested}\n")
        f.write(f"; whitespace:     {tot_trim}\n")
        f.write(f"; changed lines:  {len(fix_log)}\n;\n")
        for lineno, old, new in fix_log:
            f.write(f"{lineno} old {old}\n")
            f.write(f"{lineno} new {new}\n")

    with OUT_AUDIT.open("w", encoding="utf-8") as f:
        f.write("AP markup audit — findings requiring a human decision\n")
        f.write("=" * 60 + "\n\n")
        f.write("Generated by 08_markup_fix.py against ap.txt.\n")
        f.write("Items below were DETECTED but NOT modified by the fixer.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT THIS FIXER AUTO-CORRECTS\n")
        f.write("------------------------------------------------------------\n")
        f.write("  - Nested <ab><ab>X</ab> Y</ab>          → <ab>X Y</ab>\n")
        f.write("  - Whitespace inside <ls>/<ab>/<lex>/<lang>/<ns>/<sab>/<hom>/<is>/<Poem>\n")
        f.write("\nOutput goes to ap_fixed.txt; change log in markup_fix_changes.txt.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT NEEDS HUMAN ATTENTION\n")
        f.write("------------------------------------------------------------\n")
        f.write("  1. Adjacent </ab> <ab> — ap.txt has 532 of these. Most are\n")
        f.write("     intentional pairs; verify rather than auto-merge.\n\n")
        f.write("  2. <ab n=\"…\"> non-standard values — 4 occurrences:\n")
        f.write("     n=\"Southern Maharāṣṭra\" (L132970), n=\"Terminalia\" (L211691),\n")
        f.write("     n=\"Names\" (L214120), n=\"line\" (L389467). Decide whether to\n")
        f.write("     standardise the format or leave as readable tooltips.\n\n")
        f.write("  3. <ns> (1,309) and <sab> (468) are AP-specific paired tags.\n")
        f.write("     Review their content for well-formedness.\n\n")
        f.write("  4. Nested <ls> guards — currently 0 outside correction records.\n")
        f.write("     457 correction records present.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nAUTOMATED CHECKS BELOW\n")
        f.write("------------------------------------------------------------\n\n")
        for label, _ in AUDIT_CHECKS:
            hits = audit_hits[label]
            f.write(f"## {label}\n")
            f.write(f"   matches: {len(hits)} (showing up to 200)\n")
            for ln, snippet in hits[:200]:
                f.write(f"   L{ln}: {snippet}\n")
            f.write("\n")

    print("DONE", flush=True)


if __name__ == "__main__":
    main()
