import re
import sys

def parse_l(l_str):
    """Converts L identifier string to a comparable numeric value."""
    try:
        return float(l_str)
    except ValueError:
        # Fallback for complex identifiers if any
        m = re.match(r'(\d+)(\.(\d+))?', l_str)
        if m:
            base = int(m.group(1))
            suffix = m.group(3)
            if suffix:
                return base + float('0.' + suffix)
            return float(base)
        return 0.0

def main():
    input_file = "tmp_ap_0.txt"
    output_file = "tmp_ap_1.txt"
    log_file = "log.tsv"
    
    header = []
    entries = []
    current_entry = None
    
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('<L>'):
                if current_entry:
                    entries.append(current_entry)
                
                m = re.search(r'<L>(.*?)<pc>', line)
                l_str = m.group(1) if m else "0"
                current_entry = {
                    'l_str': l_str,
                    'l_val': parse_l(l_str),
                    'lines': [line]
                }
            elif current_entry:
                current_entry['lines'].append(line)
            else:
                header.append(line)
        
        if current_entry:
            entries.append(current_entry)

    # Log ordering issues
    print(f"Checking order and writing {log_file}...")
    with open(log_file, 'w', encoding='utf-8') as log:
        log.write("PreviousL\tErroneousL\n")
        for i in range(1, len(entries)):
            prev = entries[i-1]
            curr = entries[i]
            if curr['l_val'] < prev['l_val']:
                log.write(f"{prev['l_str']}\t{curr['l_str']}\n")

    # Sort entries
    print("Sorting entries...")
    entries.sort(key=lambda x: x['l_val'])

    # Write sorted file
    print(f"Writing sorted entries to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as fout:
        for line in header:
            fout.write(line)
        for entry in entries:
            for line in entry['lines']:
                fout.write(line)

    print(f"Auto-correction complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
