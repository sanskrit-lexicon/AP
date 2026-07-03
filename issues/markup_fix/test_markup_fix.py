"""Synthetic tests for 08_markup_fix.py (AP)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from importlib import import_module
mod = import_module("08_markup_fix")
fix_nested_ab = mod.fix_nested_ab
fix_trim_whitespace = mod.fix_trim_whitespace

PASS = 0
FAIL = 0

def check(desc, got, want):
    global PASS, FAIL
    if got == want:
        print(f"  PASS  {desc}")
        PASS += 1
    else:
        print(f"  FAIL  {desc}")
        print(f"        got:  {got!r}")
        print(f"        want: {want!r}")
        FAIL += 1

print("=== nested <ab> fixes ===")
line, n = fix_nested_ab("<ab><ab>N.</ab> of a river</ab>")
check("prefix flattened", line, "<ab>N. of a river</ab>")
check("prefix count", n, 1)

line, n = fix_nested_ab("<ab><ab>Ns.</ab></ab>")
check("exact-dup flattened", line, "<ab>Ns.</ab>")
check("exact-dup count", n, 1)

line, n = fix_nested_ab("<ab>no nesting</ab>")
check("no-op", line, "<ab>no nesting</ab>")
check("no-op count", n, 0)

print("\n=== whitespace trims ===")
line, n = fix_trim_whitespace("<ls>MS. 12. 1. 10. </ls>")
check("<ls> trailing trim", line, "<ls>MS. 12. 1. 10.</ls>")
check("<ls> trailing count", n, 1)

line, n = fix_trim_whitespace("<ab> m. </ab>")
check("<ab> leading+trailing trim", line, "<ab>m.</ab>")
check("<ab> trim count", n >= 1, True)

line, n = fix_trim_whitespace("<ns>{#hiraqA#}</ns>")
check("<ns> clean no-op", line, "<ns>{#hiraqA#}</ns>")
check("<ns> clean count", n, 0)

line, n = fix_trim_whitespace("<lex>m.</lex>")
check("<lex> clean no-op", line, "<lex>m.</lex>")
check("<lex> clean count", n, 0)

print(f"\n{'='*40}")
print(f"Results: {PASS}/{PASS+FAIL} passed", ("✓" if FAIL == 0 else "✗"))
if FAIL:
    sys.exit(1)
