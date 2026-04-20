import re
import sys
from parseheadline import parseheadline

def get_existing_ls(input_file):
    existing = set()
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('<L>'):
                meta = parseheadline(line.strip())
                existing.add(meta['L'])
    return existing

def process():
    input_file = 'tmp_ap_2.txt'
    output_file = 'tmp_ap_4.txt'
    log_file = 'log4.tsv'

    print(f"Reading {input_file} to collect existing L numbers...")
    existing_ls = get_existing_ls(input_file)
    print(f"Found {len(existing_ls)} existing L numbers.")
    
    current_xyz_group_parent = {} # base_l_str -> assigned_l_str

    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8') as fout, \
         open(log_file, 'w', encoding='utf-8') as flog:
        
        flog.write("BaseL\tAssignedL\n")
        
        entry_lines = []
        in_entry = False
        metaline = None

        for line in fin:
            if line.startswith('<L>'):
                metaline = line.strip()
                entry_lines = [line]
                in_entry = True
            elif line.startswith('<LEND>'):
                entry_lines.append(line)
                
                meta = parseheadline(metaline)
                orig_l = meta['L']
                
                if '.XYZ' in orig_l:
                    base_l_str = orig_l.split('.')[0]
                    
                    # Logic to find next available L
                    suffix = 2
                    while True:
                        candidate_l = f"{base_l_str}.{suffix:03d}"
                        if candidate_l not in existing_ls:
                            break
                        suffix += 2
                    
                    assigned_l = candidate_l
                    existing_ls.add(assigned_l)
                    
                    flog.write(f"{orig_l}\t{assigned_l}\n")
                    
                    # Replace in metaline
                    new_metaline = metaline.replace(f"<L>{orig_l}", f"<L>{assigned_l}")
                    entry_lines[0] = new_metaline + '\n'
                    
                    # Check for Lbody in lines
                    has_lbody = False
                    for i in range(len(entry_lines)):
                        # Look for {{Lbody=BASE.XYZ}}
                        m = re.search(r'{{Lbody=' + re.escape(base_l_str) + r'\.XYZ}}', entry_lines[i])
                        if m:
                            if base_l_str in current_xyz_group_parent:
                                replaced_l = current_xyz_group_parent[base_l_str]
                                entry_lines[i] = entry_lines[i].replace(f"{{{{Lbody={base_l_str}.XYZ}}}}", f"{{{{Lbody={replaced_l}}}}}")
                                flog.write(f"Lbody:{base_l_str}.XYZ\tLbody:{replaced_l}\n")
                                has_lbody = True
                    
                    # If this entry didn't have Lbody, it's the parent for this group
                    if not has_lbody:
                        current_xyz_group_parent[base_l_str] = assigned_l
                
                for el in entry_lines:
                    fout.write(el)
                
                in_entry = False
                entry_lines = []
                metaline = None
            elif in_entry:
                entry_lines.append(line)
            else:
                fout.write(line)

    print(f"Done. Output written to {output_file}, log to {log_file}")

if __name__ == "__main__":
    process()
