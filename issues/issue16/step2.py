import re
import sys
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
    
    pref = ''
    for l in lines:
        if '¦' in l:
            pref = l.split('¦')[0]
            break
    
    output_lines = []
    i = 0
    new_entries = []
    
    while i < len(lines):
        line = lines[i]
        if line.startswith('.{@{#'):
            m = re.search(r'^[.]{@{#\-([^#]+)#}@}', line)
            if m:
                suffix_str = m.group(1)
                suffix_str = suffix_str.replace('- ', '-') if '- ' in suffix_str else suffix_str
                suffix_str = re.sub(r'([a-zA-Z])-([a-zA-Z])', r'\1 -\2', suffix_str)
                suffixes = [s.strip() for s in suffix_str.split(', -')]
                suffixes = [s for s in suffixes if s]
                
                def_start = i + 1
                def_end = def_start
                while def_end < len(lines):
                    if lines[def_end].startswith('.{@') or lines[def_end].startswith('<L'):
                        break
                    def_end += 1
                
                def_lines = lines[def_start:def_end]
                
                if len(suffixes) > 1:
                    num_suffixes = len(suffixes)
                    lines_per_group = len(def_lines) // num_suffixes
                    remainder = len(def_lines) % num_suffixes
                    
                    start_idx = 0
                    for sidx, suffix in enumerate(suffixes):
                        suggestion = adjust_hw(basehw, suffix, lid, manually_mapped)
                        if suggestion:
                            correct[0] += 1
                            flog.write(f'{lid}\t{basehw}\t{suffix}\t{suggestion}\n')
                        else:
                            wrong[0] += 1
                            flog.write(f'{lid}\t{basehw}\t{suffix}\tNone\n')
                        
                        entry = {}
                        entry['metaline'] = metaline
                        entry['suggestion'] = suggestion
                        entry['suffix'] = suffix
                        
                        if sidx == 0:
                            end_idx = (sidx + 1) * lines_per_group + (1 if remainder > 0 else 0)
                            entry['def_lines'] = def_lines[start_idx:end_idx]
                            start_idx = end_idx
                            if remainder > 0:
                                remainder -= 1
                        else:
                            entry['def_lines'] = def_lines[start_idx:start_idx + lines_per_group]
                            entry['has_lbody'] = True
                            start_idx += lines_per_group
                        
                        new_entries.append(entry)
                    
                    i = def_end
                else:
                    suffix = suffixes[0]
                    suggestion = adjust_hw(basehw, suffix, lid, manually_mapped)
                    if suggestion:
                        correct[0] += 1
                        flog.write(f'{lid}\t{basehw}\t{suffix}\t{suggestion}\n')
                    else:
                        wrong[0] += 1
                        flog.write(f'{lid}\t{basehw}\t{suffix}\tNone\n')
                    
                    entry = {}
                    entry['metaline'] = metaline
                    entry['suggestion'] = suggestion
                    entry['suffix'] = suffix
                    entry['def_lines'] = def_lines
                    entry['orig_line'] = line
                    new_entries.append(entry)
                    
                    i = def_end
            else:
                output_lines.append(line)
                i += 1
        else:
            output_lines.append(line)
            i += 1
    
    for entry in new_entries:
        fout.write('<LEND>\n\n')
        
        if entry['suggestion']:
            metaline1 = entry['metaline'].replace('<k1>' + basehw, '<k1>' + entry['suggestion'])
            metaline1 = metaline1.replace('<k2>' + basehw, '<k2>' + entry['suggestion'])
            metaline1 = metaline1.replace('<pc>', '.XYZ<pc>')
        else:
            metaline1 = entry['metaline'].replace('<k2>', '.ABC<k2>')
            metaline1 = metaline1.replace('<e>', '.ABC<e>')
            metaline1 = metaline1.replace('<pc>', '.XYZ<pc>')
        
        fout.write(metaline1 + '\n')
        
        if 'orig_line' in entry:
            hw_rep = pref + ' + .{@{#-' + entry['suffix'] + '#}@}¦'
            fout.write(hw_rep + '\n')
            for dl in entry['def_lines']:
                fout.write(dl + '\n')
        else:
            hw_rep = pref + ' + .{@{#-' + entry['suffix'] + '#}@}¦'
            fout.write(hw_rep + '\n')
            if entry.get('has_lbody'):
                fout.write('{{Lbody=' + lid + '.XYZ}}\n')
    
    for ol in output_lines:
        fout.write(ol + '\n')
    
    return correct, wrong


def load_manually_mapped(filepath):
    mapping = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            lid = parts[0]
            basehw = parts[1]
            suffix = parts[2]
            resolution = parts[3]
            key = (lid, basehw, suffix)
            mapping[key] = resolution
    return mapping


if __name__=="__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]

    MANUALLY_MAPPED_PATH = "manually_mapped.tsv"
    manually_mapped = load_manually_mapped(MANUALLY_MAPPED_PATH)
    print(f"Loaded {len(manually_mapped)} manual mappings")

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
                if metaline and lines:
                    process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped)
                    lines = []
                
                metaline = lin
                fout.write(lin + '\n')
            elif lin == '<LEND>':
                lines.append(lin)
                process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped)
                lines = []
            else:
                lines.append(lin)
        
        if metaline and lines:
            process_entry(metaline, lines, fout, flog, correct, wrong, manually_mapped)

    total = correct[0] + wrong[0]
    print(f'Resolved: {correct[0]}, Unresolved: {wrong[0]}, Total: {total}')
    fin.close()
    fout.close()
    flog.close()