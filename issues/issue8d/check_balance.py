"""
 check_balance.py

"""
import re,sys
import codecs

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   #lines.append(line.strip()) # changed at ap_1
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

def check_balanced_version1(lines, opentag, closetag):
 # Copilot 02-25-2026
 stack = []  # will store tuples: (tag, line_number)

 for lineno, line in enumerate(lines, start=1):
  for ch in line:
   if ch == opentag:
    stack.append((opentag, lineno))
   elif ch == closetag:
    if not stack:
     print(f"Error: closing '{closetag}' at line {lineno} with no matching '{opentag}'")
     return False
    top_tag, top_line = stack.pop()
    if top_tag != opentag:
     print(f"Error: mismatched close '{closetag}' at line {lineno}")
     return False

 # After scanning all lines
 if stack:
  tag, line_opened = stack[-1]
  print(f"Error: unclosed '{opentag}' opened at line {line_opened}")
  return False

 return True

def check_balanced_2(lines, opentag, closetag):
 # Copilot 02-25-2026
 stack = []   # holds tuples: (tag, line_number)
 open_count = 0

 for lineno, line in enumerate(lines, start=1):
  for ch in line:
   if ch == opentag:
    stack.append((opentag, lineno))
    open_count += 1
   elif ch == closetag:
    if not stack:
     print(f"Error: closing '{closetag}' at line {lineno} with no matching '{opentag}'")
     return False, open_count
    top_tag, top_line = stack.pop()
    if top_tag != opentag:
     print(f"Error: mismatched close '{closetag}' at line {lineno}")
     return False, open_count

 # After scanning all lines
 if stack:
  tag, line_opened = stack[-1]
  print(f"Error: unclosed '{opentag}' opened at line {line_opened}")
  return False, open_count

 return True, open_count

def check_balanced_3(lines, opentag, closetag):
 # 02-25-2026 Copilot. Allow multi-character tags
 stack = []   # holds tuples: (tag, line_number)
 open_count = 0
 L_open = len(opentag)
 L_close = len(closetag)

 for lineno, line in enumerate(lines, start=1):
  i = 0
  while i < len(line):
   # Check for opening tag
   if line.startswith(opentag, i):
    stack.append((opentag, lineno))
    open_count += 1
    i += L_open
    continue

   # Check for closing tag
   if line.startswith(closetag, i):
    if not stack:
     print(f"Error: closing '{closetag}' at line {lineno} with no matching '{opentag}'")
     return False, open_count
    top_tag, top_line = stack.pop()
    if top_tag != opentag:
     print(f"Error: mismatched close '{closetag}' at line {lineno}")
     return False, open_count
    i += L_close
    continue

   i += 1

 # After scanning all lines
 if stack:
  tag, line_opened = stack[-1]
  print(f"Error: unclosed '{opentag}' opened at line {line_opened}")
  return False, open_count

 return True, open_count

def check_balanced_multi_1(lines, delimiter_pairs):
 # Copilot 02-25-2026
 # General multi‑delimiter validator 
 # Preprocess: map open→close and close→open
 open_to_close = {op: cl for (op, cl) in delimiter_pairs}
 close_to_open = {cl: op for (op, cl) in delimiter_pairs}

 # Sort tags by length (longest first) so multi-char tags match correctly
 all_opens = sorted(open_to_close.keys(), key=len, reverse=True)
 all_closes = sorted(close_to_open.keys(), key=len, reverse=True)

 stack = []   # holds tuples: (open_tag, line_number)
 open_count = 0

 for lineno, line in enumerate(lines, start=1):
  i = 0
  L = len(line)

  while i < L:
   # Try matching an opening tag
   matched = False
   for op in all_opens:
    if line.startswith(op, i):
     stack.append((op, lineno))
     open_count += 1
     i += len(op)
     matched = True
     break
   if matched:
    continue

   # Try matching a closing tag
   for cl in all_closes:
    if line.startswith(cl, i):
     if not stack:
      print(f"Error: closing '{cl}' at line {lineno} with no matching opener")
      return False, open_count

     top_op, top_line = stack.pop()
     expected_cl = open_to_close[top_op]

     if cl != expected_cl:
      print(f"Error: mismatched close '{cl}' at line {lineno}, expected '{expected_cl}'")
      return False, open_count

     i += len(cl)
     matched = True
     break
   if matched:
    continue

   # Otherwise, normal character
   i += 1

 # After scanning all lines
 if stack:
  op, line_opened = stack[-1]
  print(f"Error: unclosed '{op}' opened at line {line_opened}")
  return False, open_count

 return True, open_count

def check_balanced_multi(lines, delimiter_pairs, nesting):
 # Copilot 02-25-2026
 # General multi‑delimiter validator, with optional nesting
 # Preprocess: map open→close and close→open
 open_to_close = {op: cl for (op, cl) in delimiter_pairs}
 close_to_open = {cl: op for (op, cl) in delimiter_pairs}

 # Sort tags by length (longest first) so multi-char tags match correctly
 all_opens = sorted(open_to_close.keys(), key=len, reverse=True)
 all_closes = sorted(close_to_open.keys(), key=len, reverse=True)

 stack = []   # holds tuples: (open_tag, line_number)
 open_count = 0

 for lineno, line in enumerate(lines, start=1):
  i = 0
  L = len(line)

  while i < L:
   matched = False

   # Try matching an opening tag
   for op in all_opens:
    if line.startswith(op, i):
     # If nesting is False, we cannot open a new tag while one is already open
     if not nesting and stack:
      print(f"Error: nested opening '{op}' at line {lineno} not allowed")
      return False, open_count

     stack.append((op, lineno))
     open_count += 1
     i += len(op)
     matched = True
     break
   if matched:
    continue

   # Try matching a closing tag
   for cl in all_closes:
    if line.startswith(cl, i):
     if not stack:
      print(f"Error: closing '{cl}' at line {lineno} with no matching opener")
      return False, open_count

     top_op, top_line = stack.pop()
     expected_cl = open_to_close[top_op]

     if cl != expected_cl:
      print(f"Error: mismatched close '{cl}' at line {lineno}, expected '{expected_cl}'")
      return False, open_count

     i += len(cl)
     matched = True
     break
   if matched:
    continue

   # Otherwise, normal character
   i += 1

 # After scanning all lines
 if stack:
  op, line_opened = stack[-1]
  print(f"Error: unclosed '{op}' opened at line {line_opened}")
  return False, open_count

 return True, open_count
def test1():
 lines = ['a (b c ', 'd) e']
 open_tag,close_tag = ('(',')')
 newlines = merge_tagged_segments1(lines,open_tag=open_tag,close_tag=close_tag)
 print('test1')
 print(lines)
 print(newlines)

def test2():
 lines = ['xyz','a (b c ', 'd) e']
 ans = ['xyz','a (b c d)',' e']
 open_tag,close_tag = ('(',')')
 newlines = merge_tagged_segments1(lines,open_tag=open_tag,close_tag=close_tag)
 print('test2')
 print(lines)
 print(newlines)
 print(ans)
#test1()
#test2()
#exit(1)
def make_newlines_1(lines,open_tag,close_tag):
 newlines = merge_tagged_segments1(lines,open_tag=open_tag,close_tag=close_tag)
 if len(lines) != len(newlines):
  print(f'{len(lines)}, {len(newlines)}')
  return newlines
 nfind = 0
 for i,line in enumerate(lines):
  if line != newlines[i]:
   nfind = nfind + 1
 print(f'make_newlines_1 changes {nfind} lines')
 print(f'make_newlines_1 returns {len(newlines)} lines')
 return newlines


#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 lines = read_lines(filein)

 tagpairs = [
  ('(', ')'),
  ('[', ']'),
  ('{#', '#}'),
  #(),
  ]
 nesting = True
 flag,count = check_balanced_multi(lines,tagpairs,nesting)
 print(f'flag={flag}, count={count}, nesting={nesting}')
 print(f'tagpairs = {tagpairs}')

 tagpairs1 = [('{' , '}')]
 flag,count = check_balanced_multi(lines,tagpairs1,nesting)
 print(f'flag={flag}, count={count}, nesting={nesting}')
 print(f'tagpairs1 = {tagpairs1}')
              
 exit(1)
 
 flag,count = check_balanced(lines, '(', ')')
 if flag: print('( and ) ok; count=',count)
 flag,count = check_balanced(lines, '[', ']')
 if flag: print('[ and ] ok; count=',count)
 flag,count = check_balanced(lines, '{', '}')
 if flag: print('{ and } ok; count=',count)
 flag,count = check_balanced(lines, '{#', '#}')
 if flag: print('{# and #} ok; count=',count)
 
 
 
