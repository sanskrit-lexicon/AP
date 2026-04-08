#!/usr/bin/env python3
"""
Script to extract €class and <ab> patterns from ap.txt dictionary.

For each entry (line starting with <L>), extracts:
- L: value from <L> tag
- k1: value from <k1> tag
- Classes: extracted from €N patterns (e.g., €1, €9. €10 -> [9, 10])
- ab: value from <ab>[PĀU].</ab> tag (P., U., Ā.) or None if not found
"""

import re
import sys
from pathlib import Path


def get_l_k1(line):
    """Extract L and k1 values from a line starting with <L>."""
    l_match = re.search(r'<L>(\d+(?:\.\d+)?)', line)
    k1_match = re.search(r'<k1>([^<]+)', line)
    return (
        l_match.group(1) if l_match else None,
        k1_match.group(1) if k1_match else None
    )


def extract_classes(text):
    """Extract class numbers from € patterns. Returns list of integers."""
    classes = []
    # Match € followed by digits, handling multiple classes like €9. €10
    pattern = r'€(\d+)'
    matches = re.findall(pattern, text)
    for m in matches:
        try:
            classes.append(int(m))
        except ValueError:
            pass
    return classes


def extract_ab(text):
    """Extract <ab>[PĀU].</ab> value. Returns the matched text or None."""
    match = re.search(r'<ab>[PĀU]\.</ab>', text)
    return match.group() if match else None


def process_file(filepath):
    """Process the ap.txt file and extract €class and <ab> patterns."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    current_l = None
    current_k1 = None
    results = []
    
    for i, line in enumerate(lines, 1):
        # Track current L and k1 from lines starting with <L>
        if line.startswith('<L>'):
            current_l, current_k1 = get_l_k1(line)
        
        # Look for € patterns in this line
        if '€' in line:
            classes = extract_classes(line)
            ab = extract_ab(line)
            
            if classes:  # Only process if we found €N patterns
                results.append({
                    'line_num': i,
                    'L': current_l,
                    'k1': current_k1,
                    'classes': classes,
                    'ab': ab,
                    'raw_line': line.strip()[:100]  # First 100 chars for reference
                })
    
    return results


def main():
    # Determine the path to ap.txt
    script_dir = Path(__file__).parent
    # ap.txt is in the parent repo: ../../sanskrit-lexicon/csl-orig/v02/ap/ap.txt
    ap_path = script_dir.parent.parent.parent / 'sanskrit-lexicon' / 'csl-orig' / 'v02' / 'ap' / 'ap.txt'
    
    if not ap_path.exists():
        # Try alternative path
        ap_path = Path('/Users/dhaval/Documents/GithubRepos/sanskrit-lexicon/csl-orig/v02/ap/ap.txt')
    
    if not ap_path.exists():
        print(f"Error: Could not find ap.txt at {ap_path}", file=sys.stderr)
        sys.exit(1)
    
    results = process_file(ap_path)
    
    # Print results in TSV format: L\tk1\tclasses\tab
    for r in results:
        classes_str = ','.join(str(c) for c in r['classes'])
        ab_str = r['ab'][4:-5] if r['ab'] else 'None'  # Remove <ab> and </ab> tags
        print(f"{r['L']}\t{r['k1']}\t{classes_str}\t{ab_str}")


if __name__ == '__main__':
    main()
