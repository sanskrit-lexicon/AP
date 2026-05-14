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
    Resolve basehw + ˚suffix into a full headword using Sanskrit sandhi rules.
    suffix has already had the leading ˚ stripped.
    """
    # Strip trailing inflection from basehw to get the sandhi base vowel stem
    # e.g. kinnaraH -> kinnara, kinnarAn -> kinnarA, kinnaraSam -> kinnaraS...
    base = re.sub('H$', '', basehw)   # strip trailing visarga
    base = re.sub('m$', '', base)     # strip trailing anusvara
    # Now base ends with the stem vowel (e.g. 'a' in 'kinnara')

    suf = suffix  # e.g. 'ISaH', 'ISvaraH'

    # Direct: basehw already ends with suffix (no sandhi needed)
    if basehw.endswith(suf):
        return basehw

    # Sandhi a/A + I/i -> e  (kinnara + ISaH -> kinnare + SaH = kinnareSaH)
    # The leading I/i of the suffix is consumed, replaced by 'e' fused to base
    if base.endswith('a') and re.match(r'^[Ii]', suf):
        return base[:-1] + 'e' + suf[1:]

    # Sandhi a + u/U -> o  (base 'a' + suffix 'u' -> 'o', consuming both)
    if base.endswith('a') and re.match(r'^[Uu]', suf):
        return base[:-1] + 'o' + suf[1:]

    # Sandhi a + a/A -> A  (base 'a' + suffix 'a/A' -> 'A', consuming both)
    if base.endswith('a') and re.match(r'^[aA]', suf):
        return base[:-1] + 'A' + suf[1:]

    # No sandhi: just concatenate base + suffix
    candidate = base + suf
    if candidate != basehw:
        return candidate

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

    # Parent entry output
    parent_content = before_lines + [modified_line] + extra_parent_lines + ['<LEND>']
    for line in parent_content:
        fout.write(line + '\n')

    # Extract suffixes from the matched inner text, e.g. "˚ISaH, ˚ISvaraH"
    inner = pattern_match.group(1)          # "˚ISaH, ˚ISvaraH"
    orig_match_str = pattern_match.group(0)  # "{#˚ISaH, ˚ISvaraH#}"
    raw_parts = re.split(r'[,;]\s*', inner)
    suffixes = [s.strip().lstrip('˚').strip() for s in raw_parts if s.strip()]

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
