import re
import sys
from parseheadline import parseheadline

# Pattern: {#˚word1, ˚word2#} — inline compound headwords to elevate
INLINE_PATTERN = re.compile(r'\{#(˚[^#]+)#\}')


def adjust_hw(basehw, suffix, lid, manually_mapped=None):
    result = _adjust_hw_internal(basehw, suffix)
    if result is None and manually_mapped is not None:
        key = (lid, basehw, suffix)
        if key in manually_mapped:
            return manually_mapped[key]
    return result


def _adjust_hw_internal(basehw, suffix):
    """
    Resolve basehw + ˚suffix into a full headword.
    Aligning with issue16 logic: specific rules, no catch-all.
    """
    # Normalize basehw to stem
    stem = re.sub('H$', '', basehw)
    stem = re.sub('m$', '', stem)
    # issue16 normalization:
    basehw_norm = re.sub('[a][Hm]$', 'a', basehw)

    suf = suffix

    # 1. Direct match: basehw already ends with suffix
    if basehw.endswith(suf):
        return basehw

    # 2. Sandhi: a + I/i -> e
    if stem.endswith('a') and re.match(r'^[Ii]', suf):
        return stem[:-1] + 'e' + suf[1:]

    # 3. Sandhi: a + u/U -> o
    if stem.endswith('a') and re.match(r'^[Uu]', suf):
        return stem[:-1] + 'o' + suf[1:]

    # 4. Sandhi: a + a/A -> A
    if stem.endswith('a') and re.match(r'^[aA]', suf):
        return stem[:-1] + 'A' + suf[1:]

    # 5. Ported rules from issue16
    if suf == 'tA':
        return basehw_norm + 'tA'
    if suf == 'tvam':
        return basehw_norm + 'tvam'
    if re.search('^ka[HM]*$', suf):
        return basehw_norm + suf

    # 6. Specific case for line 29: vAwaH, etc.
    # If it's a simple concatenation that "looks" like a valid compound formation
    # We might want to allow some, but let's be conservative first.
    # issue16 didn't have a catch-all, so we return None here if no rule matched.

    return None


def process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped):
    """
    lines: content lines of the entry (NOT including the <L> metaline),
           but INCLUDING the <LEND> line.
    The <L> metaline was already written to fout by the caller.
    """
    meta = parseheadline(metaline)
    lid = meta['L']
    basehw = meta['k1']

    # Find prefix (text before ¦) for building new entry definitions
    pref = ''
    for l in lines:
        if '¦' in l:
            pref = l.split('¦')[0].strip()
            break

    # Find the first line containing the {#˚...#} pattern
    pattern_line_idx = None
    pattern_match = None
    for i, line in enumerate(lines):
        if line == '<LEND>':
            continue
        m = INLINE_PATTERN.search(line)
        if m:
            pattern_line_idx = i
            pattern_match = m
            break

    if pattern_line_idx is None:
        # No pattern found — write entry body as-is
        for line in lines:
            fout.write(line + '\n')
        return correct, wrong

    # Split lines into:
    #   before_lines  : lines before the pattern line
    #   pattern_line  : the line containing {#˚...#}
    #   def_body_lines: ∙² definition lines that follow (moved to new entry)
    #   <LEND>        : always last
    before_lines = lines[:pattern_line_idx]
    pattern_line = lines[pattern_line_idx]
    after_lines = lines[pattern_line_idx + 1:]

    # Extract suffixes early so we can guard before writing anything
    inner = pattern_match.group(1)          # "˚ISaH, ˚ISvaraH"
    orig_match_str = pattern_match.group(0)  # "{#˚ISaH, ˚ISvaraH#}"
    raw_parts = re.split(r'[,;]\s*', inner)
    suffixes = [s.strip().lstrip('˚').strip() for s in raw_parts if s.strip()]

    # Guard: if any individual suffix contains a space it is a quotation
    # sentence fragment, not a compound headword — write entry unchanged and skip.
    if any(' ' in s for s in suffixes):
        for line in lines:
            fout.write(line + '\n')
        return correct, wrong

    # ∙ lines go to new entry; other non-LEND lines stay in parent
    def_body_lines = []
    extra_parent_lines = []
    for l in after_lines:
        if l == '<LEND>':
            continue
        elif l.startswith('∙'):
            def_body_lines.append(l)
        else:
            extra_parent_lines.append(l)

    # Build modified pattern line: remove {#˚...#} match
    start, end = pattern_match.start(), pattern_match.end()
    before_match = pattern_line[:start].rstrip(' ')
    after_match = pattern_line[end:].lstrip(' ')

    if after_match:
        modified_line = (before_match + ' ' + after_match).rstrip()
    else:
        modified_line = before_match.rstrip()

    # Parent entry output (with the ˚ pattern removed)
    parent_content = before_lines + [modified_line] + extra_parent_lines + ['<LEND>']
    for line in parent_content:
        fout.write(line + '\n')

    # Resolve each suffix and log
    resolved = []
    for suffix in suffixes:
        suggestion = adjust_hw(basehw, suffix, lid, manually_mapped)
        if suggestion:
            correct[0] += 1
            flog.write(f'{lid}\t{basehw}\t{suffix}\t{suggestion}\n')
        else:
            wrong[0] += 1
            flog.write(f'{lid}\t{basehw}\t{suffix}\tNone\n')
        resolved.append(suggestion)

    # Write new derived entries
    for sidx, (suffix, suggestion) in enumerate(zip(suffixes, resolved)):
        fout.write('\n')

        # Build new metaline
        if suggestion:
            metaline1 = metaline.replace('<k1>' + basehw, '<k1>' + suggestion)
            metaline1 = metaline1.replace('<k2>' + basehw, '<k2>' + suggestion)
            metaline1 = metaline1.replace('<pc>', '.XYZ<pc>')
        else:
            metaline1 = metaline.replace('<k2>', '.ABC<k2>')
            metaline1 = metaline1.replace('<e>', '.ABC<e>')
            metaline1 = metaline1.replace('<pc>', '.XYZ<pc>')

        fout.write(metaline1 + '\n')

        if sidx > 0:
            # Subsequent suffixes: refer back to the first new entry
            fout.write(f'{{{{Lbody={lid}.XYZ}}}}\n')
        else:
            # First suffix: full definition
            def_line = f"{pref} + {orig_match_str}¦"
            fout.write(def_line + '\n')
            for dl in def_body_lines:
                fout.write(dl + '\n')

        fout.write('<LEND>\n')

    return correct, wrong


def load_manually_mapped(filepath):
    mapping = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('\t')
                if len(parts) < 4:
                    continue
                key = (parts[0], parts[1], parts[2])
                mapping[key] = parts[3]
    except FileNotFoundError:
        print("Note: manually_mapped.tsv not found, skipping.")
    return mapping


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]

    manually_mapped = load_manually_mapped("manually_mapped.tsv")
    print(f"Loaded {len(manually_mapped)} manual mappings")

    fout = open(output_file, 'w', encoding='utf-8')
    flog = open(log_file, 'w', encoding='utf-8')
    flog.write('Lnum\tbasehw\tsuffix\tresolution\n')
    correct = [0]
    wrong = [0]

    with open(input_file, 'r', encoding='utf-8') as fin:
        lines = []
        metaline = None

        for lin in fin:
            lin = lin.rstrip('\n')

            if lin.startswith('<L>'):
                if metaline and lines:
                    process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped)
                    lines = []
                metaline = lin
                fout.write(lin + '\n')

            elif lin == '<LEND>':
                lines.append(lin)
                process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped)
                lines = []
                metaline = None

            else:
                lines.append(lin)

        if metaline and lines:
            process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped)

    total = correct[0] + wrong[0]
    print(f'Resolved: {correct[0]}, Unresolved: {wrong[0]}, Total: {total}')
    fout.close()
    flog.close()
