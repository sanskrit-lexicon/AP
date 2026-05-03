import re
import sys
import os
from parseheadline import parseheadline

def adjust_hw(basehw, suffix, lid, manually_mapped=None):
    result = _adjust_hw_internal(basehw, suffix, lid)
    if result is None and manually_mapped is not None:
        key = (lid, basehw, suffix)
        if key in manually_mapped:
            return manually_mapped[key]
    return result

def _adjust_hw_internal(basehw, suffix, lid):
    basehw = re.sub('[a][Hm]$', 'a', basehw)
    suffix = suffix.lstrip('[-˚]')
    if (basehw.endswith('a') and suffix.endswith('am')) and ((basehw + 'm').endswith(suffix)):
        return basehw + 'm'
    elif (basehw.endswith('a') and suffix.endswith('aH')) and ((basehw + 'H').endswith(suffix)):
        return basehw + 'H'
    elif (basehw.endswith('a') and suffix.endswith('A')) and ((basehw[:-1] + 'A').endswith(suffix)):
        return basehw[:-1] + 'A'
    elif (basehw.endswith('a') and suffix.endswith('I')) and ((basehw[:-1] + 'I').endswith(suffix)):
        return basehw[:-1] + 'I'
    elif basehw.endswith(suffix):
        return basehw
    elif basehw.endswith(suffix.rstrip('[mH]')):
        return basehw + suffix[-1]
    elif (basehw+'I').endswith(suffix):
        return basehw + 'I'
    elif (basehw[:-1]+'RI').endswith(suffix):
        return basehw[:-1] + 'RI'
    elif re.sub('A$', 'a', basehw).endswith(re.sub('a[Hm]*$', 'a', suffix)):
        return basehw[:-2] + suffix
    elif re.sub('a$', 'AH', basehw).endswith(suffix):
        return basehw[:-2] + suffix
    elif re.sub('i$', 'I', basehw).endswith(suffix):
        return basehw[:-1] + 'I'
    elif re.sub('Yc$', 'k', basehw).endswith(suffix):
        return basehw[:-2] + 'k'
    elif re.sub('aka$', 'ikA', basehw).endswith(suffix):
        return re.sub('aka$', 'ikA', basehw)
    elif basehw == 'janman' and not re.search('^[aAiIuUfFxeEoO]', suffix):
        return 'janma' + suffix
    elif basehw.endswith('c') and suffix == 'k':
        return basehw[:-1] + 'k'
    elif re.sub('a$', 'O', basehw).endswith(suffix):
        return re.sub('a$', 'O', basehw)
    elif re.sub('iH$', 'I', basehw).endswith(suffix):
        return re.sub('iH$', 'I', basehw)
    elif re.sub('a$', 'e', basehw).endswith(suffix):
        return re.sub('a$', 'e', basehw)
    elif suffix == 'tA':
        return basehw + 'tA'
    elif suffix == 'tvam':
        return basehw + 'tvam'
    elif re.search('^ka[HM]*$', suffix):
        return basehw + suffix
    elif basehw.endswith('H') and re.sub('iH$', 'i', basehw).endswith(suffix):
        return basehw[:-1]
    elif basehw.endswith('H') and re.sub('uH$', 'u', basehw).endswith(suffix):
        return basehw[:-1]
    return None

def process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped):
    meta = parseheadline(metaline)
    lid = meta['L']
    basehw = meta['k1']
    
    full_text = "\n".join(lines)
    
    if '¦' not in full_text:
        fout.write(metaline + '\n')
        fout.write(full_text + '\n')
        fout.write('<LEND>\n')
        return
            
    before_bar, after_bar = full_text.split('¦', 1)
    
    # Prefix for new entries (part before the first broken bar)
    pref = before_bar.strip()
    
    # Pattern to find the suffix part including parentheses
    pattern = r'(\s*\(\s*\{@\{#\-([^#]+)#\}@\}[^)]*\))'
    
    matches = list(re.finditer(pattern, after_bar))
    
    if not matches:
        fout.write(metaline + '\n')
        fout.write(full_text + '\n')
        fout.write('<LEND>\n')
        return

    # Original entry gets everything up to the first suffix split
    first_match = matches[0]
    before_suffix = after_bar[:first_match.start()]
    
    fout.write(metaline + '\n')
    fout.write(f"{before_bar}¦{before_suffix.rstrip()}\n")
    fout.write('<LEND>\n')
    
    # Process each match to create new entries
    for i, m in enumerate(matches):
        full_match = m.group(1)
        suffix_str = m.group(2)
        
        # Text after this suffix until the next suffix or end of entry
        if i + 1 < len(matches):
            after_suffix = after_bar[m.end():matches[i+1].start()]
        else:
            after_suffix = after_bar[m.end():]
            
        suffixes = [s.strip() for s in suffix_str.split(', -')]
        
        for sidx, suffix in enumerate(suffixes):
            suggestion = adjust_hw(basehw, suffix, lid, manually_mapped)
            if suggestion:
                correct[0] += 1
                flog.write(f'{lid}\t{basehw}\t{suffix}\t{suggestion}\n')
            else:
                wrong[0] += 1
                flog.write(f'{lid}\t{basehw}\t{suffix}\tNone\n')
            
            suffix_part = full_match.strip()
            
            # Use original metaline but mark L and adjust headwords
            metaline1 = metaline.replace('<L>' + lid, '<L>' + lid + '.XYZ')
            if suggestion:
                metaline1 = metaline1.replace('<k1>' + basehw, '<k1>' + suggestion)
                metaline1 = metaline1.replace('<k2>' + basehw, '<k2>' + suggestion)
            else:
                metaline1 = metaline1.replace('<k1>' + basehw, '<k1>.ABC' + basehw)
                metaline1 = metaline1.replace('<k2>' + basehw, '<k2>' + basehw)
            
            fout.write('\n' + metaline1 + '\n')
            # The body starts with prefix + suffix part + ¦
            # We preserve the whitespace of after_suffix to keep multi-line structure
            fout.write(f"{pref} + {suffix_part}¦{after_suffix}\n")
            fout.write('<LEND>\n')

def load_manually_mapped(filepath):
    mapping = {}
    if not filepath or not os.path.exists(filepath):
        return mapping
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) < 4: continue
            lid = parts[0]
            basehw = parts[1]
            suffix = parts[2]
            resolution = parts[3]
            key = (lid, basehw, suffix)
            mapping[key] = resolution
    return mapping

if __name__=="__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 step1.py <input_file> <output_file> <log_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]

    MANUALLY_MAPPED_PATH = "manually_mapped.tsv"
    manually_mapped = load_manually_mapped(MANUALLY_MAPPED_PATH)

    fout = open(output_file, 'w')
    flog = open(log_file, 'w')
    flog.write('Lnum\tbasehw\tsuffix\tresolution\n')
    correct = [0]
    wrong = [0]

    with open(input_file, 'r') as fin:
        lines = []
        metaline = None
        
        for lin in fin:
            lin = lin.rstrip('\n')
            
            if lin.startswith('<L>'):
                metaline = lin
                lines = []
            elif lin == '<LEND>':
                process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped)
                metaline = None
                lines = []
            else:
                lines.append(lin)

    total = correct[0] + wrong[0]
    print(f'Resolved: {correct[0]}, Unresolved: {wrong[0]}, Total: {total}')
    fin.close()
    fout.close()
    flog.close()
