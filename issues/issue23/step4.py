import re
import sys
from parseheadline import parseheadline

def parse_l(l_str):
    clean = l_str.replace('.XYZ', '')
    if '.' in clean:
        parts = clean.split('.')
        base = int(parts[0])
        decimal = int(parts[1])
        return base, decimal
    return int(clean), 0

def l_to_str(p, d):
    if d == 0:
        return str(p)
    return f"{p}.{d:03d}"

def process():
    input_file = 'tmp_ap_2.txt'
    output_file = 'tmp_ap_4.txt'
    log_file = 'log4.tsv'

    print(f"Reading {input_file}...")
    all_data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        in_entry = False
        current_entry = []
        for line in f:
            if line.startswith('<L>'):
                in_entry = True
                current_entry = [line]
            elif line.startswith('<LEND>'):
                if in_entry:
                    current_entry.append(line)
                    all_data.append({'type': 'entry', 'lines': current_entry})
                    current_entry = []
                    in_entry = False
                else:
                    all_data.append({'type': 'line', 'text': line})
            elif in_entry:
                current_entry.append(line)
            else:
                all_data.append({'type': 'line', 'text': line})
    
    # Extract entries for logic
    entries_only = [item for item in all_data if item['type'] == 'entry']
    
    # Map from index to L and XYZ status
    l_info = []
    for item in entries_only:
        metaline = item['lines'][0]
        meta = parseheadline(metaline)
        l_str = meta['L']
        l_info.append({'l_str': l_str, 'is_xyz': '.XYZ' in l_str})

    xyz_group_parent_l = {} # base_l_xyz -> new_l_for_group
    assigned_ls = [None] * len(entries_only)
    
    with open(log_file, 'w', encoding='utf-8') as flog:
        flog.write("OldL\tAssignedL\n")
        
        i = 0
        while i < len(entries_only):
            if not l_info[i]['is_xyz']:
                i += 1
                continue
            
            # Found a block of XYZ entries
            start_i = i
            while i < len(entries_only) and l_info[i]['is_xyz']:
                i += 1
            end_i = i
            
            # Find neighbors
            prev_l_str = None
            for j in range(start_i - 1, -1, -1):
                if not l_info[j]['is_xyz']:
                    prev_l_str = l_info[j]['l_str']
                    break
            
            next_l_str = None
            for j in range(end_i, len(entries_only)):
                if not l_info[j]['is_xyz']:
                    next_l_str = l_info[j]['l_str']
                    break
            
            if prev_l_str and next_l_str:
                p1, d1 = parse_l(prev_l_str)
                p2, d2 = parse_l(next_l_str)
                
                candidates = []
                if p1 == p2:
                    for d in range(d1 + 1, d2):
                        candidates.append(l_to_str(p1, d))
                elif p1 < p2:
                    for d in range(d1 + 1, 1000):
                        candidates.append(l_to_str(p1, d))
                
                # Assign candidates
                for k, entry_idx in enumerate(range(start_i, end_i)):
                    old_l = l_info[entry_idx]['l_str']
                    
                    # Check if it has Lbody
                    has_lbody = False
                    for line in entries_only[entry_idx]['lines']:
                        if '{{Lbody=' in line:
                            has_lbody = True
                            break
                    
                    if k < len(candidates):
                        new_l = candidates[k]
                        assigned_ls[entry_idx] = new_l
                        flog.write(f"{old_l}\t{new_l}\n")
                        
                        # If this was the first entry of the group (no Lbody), it's the group parent
                        if not has_lbody:
                            xyz_group_parent_l[old_l] = new_l
                    else:
                        assigned_ls[entry_idx] = old_l # stays XYZ
                        flog.write(f"{old_l}\t{old_l}\n")
            else:
                # Edge cases
                for entry_idx in range(start_i, end_i):
                    assigned_ls[entry_idx] = l_info[entry_idx]['l_str']
            
            i = end_i

    # Final Pass: Write and update Lbody
    entry_idx = 0
    with open(output_file, 'w', encoding='utf-8') as fout:
        for item in all_data:
            if item['type'] == 'line':
                fout.write(item['text'])
            else:
                # Type: entry
                old_l = l_info[entry_idx]['l_str']
                new_l = assigned_ls[entry_idx] if assigned_ls[entry_idx] else old_l
                
                # 1. Update metaline
                metaline = item['lines'][0]
                if new_l != old_l:
                    metaline = metaline.replace(f"<L>{old_l}", f"<L>{new_l}")
                fout.write(metaline)
                
                # 2. Update lines (Lbody)
                for line in item['lines'][1:]:
                    m = re.search(r'{{Lbody=(.*?\.XYZ)}}', line)
                    if m:
                        base_xyz = m.group(1)
                        if base_xyz in xyz_group_parent_l:
                            target_l = xyz_group_parent_l[base_xyz]
                            line = line.replace(f"{{{{Lbody={base_xyz}}}}}", f"{{{{Lbody={target_l}}}}}")
                    fout.write(line)
                
                entry_idx += 1

    print(f"Done. Output written to {output_file}, log to {log_file}")

if __name__ == "__main__":
    process()
