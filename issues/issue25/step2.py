import re
import sys
from parseheadline import parseheadline

def get_existing_ls(input_file):
    existing = set()
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('<L>'):
                # Handle both normal and XYZ lines
                l_part = line.split('<pc>')[0].replace('<L>', '').strip()
                if '.XYZ' in l_part:
                    existing.add(l_part.replace('.XYZ', ''))
                else:
                    existing.add(l_part)
    return existing

def resolve_l(orig_l, existing_ls):
    if '.XYZ' not in orig_l:
        return orig_l
    
    base_l = orig_l.replace('.XYZ', '')
    
    # Try incrementing by exactly one step
    if '.' in base_l:
        parts = base_l.split('.')
        prefix = parts[0]
        suffix = parts[1]
        try:
            val = int(suffix)
            val += 1
            candidate = f"{prefix}.{val:0{len(suffix)}d}"
            if candidate not in existing_ls:
                existing_ls.add(candidate)
                return candidate
            else:
                return "None"
        except ValueError:
            pass
    
    # Generic fallback if no suffix (e.g. 100 -> 100.001)
    candidate = f"{base_l}.001"
    if candidate not in existing_ls:
        existing_ls.add(candidate)
        return candidate
    
    return "None"

def process():
    if len(sys.argv) < 3:
        print("Usage: python3 step2.py <input_file> <output_file> <log_file>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]

    print(f"Reading {input_file} to collect existing L numbers...")
    existing_ls = get_existing_ls(input_file)
    print(f"Found {len(existing_ls)} existing L numbers.")
    
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8') as fout, \
         open(log_file, 'w', encoding='utf-8') as flog:
        
        flog.write("OrigL\tAssignedL\n")
        
        entry_lines = []
        current_empty_parent = None
        in_entry = False
        
        for line in fin:
            line_str = line.rstrip('\n')
            if line_str.startswith('<L>'):
                entry_lines = [line_str]
                in_entry = True
            elif line_str == '<LEND>':
                entry_lines.append(line_str)
                in_entry = False
                
                meta = parseheadline(entry_lines[0])
                orig_l = meta['L']
                is_child = '.XYZ' in orig_l
                base_l = orig_l.replace('.XYZ', '')
                
                # Check for empty definition after ¦
                full_text = "\n".join(entry_lines)
                is_empty = False
                if '¦' in full_text:
                    after_bar = full_text.split('¦', 1)[1]
                    content_after_bar = after_bar.replace('<LEND>', '').strip()
                    if not content_after_bar:
                        is_empty = True
                
                if not is_child:
                    # Flush pending parent if any (shouldn't happen if data is well-formed)
                    if current_empty_parent:
                        for el in current_empty_parent['entry_lines']:
                            fout.write(el + '\n')
                        current_empty_parent = None
                        
                    if is_empty:
                        print(f"Empty definition found in Lnum: {orig_l}. Will attempt body swap with child.")
                        # Save for later
                        current_empty_parent = {
                            'orig_l': orig_l,
                            'entry_lines': entry_lines
                        }
                    else:
                        # Write normally
                        for el in entry_lines:
                            fout.write(el + '\n')
                            
                else: # is_child
                    if current_empty_parent and current_empty_parent['orig_l'] == base_l:
                        # Swap bodies
                        parent_orig_l = current_empty_parent['orig_l']
                        
                        # Child body becomes parent body
                        child_body_lines = entry_lines[1:-1]
                        parent_lines = current_empty_parent['entry_lines']
                        parent_lines = [parent_lines[0]] + child_body_lines + [parent_lines[-1]]
                        
                        # Child body becomes Lbody
                        entry_lines = [entry_lines[0], f"{{{{Lbody={parent_orig_l}}}}}", entry_lines[-1]]
                        
                        # Write parent
                        for el in parent_lines:
                            fout.write(el + '\n')
                            
                        current_empty_parent = None
                    
                    # Resolve L for child
                    assigned_l = resolve_l(orig_l, existing_ls)
                    entry_lines[0] = entry_lines[0].replace(f"<L>{orig_l}", f"<L>{assigned_l}")
                    flog.write(f"{orig_l}\t{assigned_l}\n")
                    
                    # Write child
                    for el in entry_lines:
                        fout.write(el + '\n')
                
                entry_lines = []
            else:
                if in_entry:
                    entry_lines.append(line_str)
                else:
                    fout.write(line_str + '\n')
                
        # Flush at EOF if needed
        if current_empty_parent:
            for el in current_empty_parent['entry_lines']:
                fout.write(el + '\n')
    
    print(f"Done. Output written to {output_file}, log to {log_file}")

if __name__ == "__main__":
    process()
