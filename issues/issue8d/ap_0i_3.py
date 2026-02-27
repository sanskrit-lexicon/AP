"""
 ap_0i_3.py

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

def merge_tagged_segments1(lines, open_tag='(', close_tag=')'):
 out = [""] * len(lines)
 inside = False
 buf = ""
 start_line = None

 for idx, line in enumerate(lines):
  i = 0
  while i < len(line):
   ch = line[i]

   if ch == open_tag and not inside:
    inside = True
    start_line = idx
    buf += ch
   elif ch == close_tag and inside:
    buf += ch
    inside = False
    out[start_line] += buf
    buf = ""
   else:
    if inside:
     buf += ch
    else:
     out[idx] += ch

   i += 1

 # If tag never closed, flush buffer into its start line
 if inside and start_line is not None:
  out[start_line] += buf

 return out

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
def make_newlines_1(lines):
 open_tag = '['
 close_tag = ']'
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
 fileout = sys.argv[2]
 lines = read_lines(filein)
 lines1 = make_newlines_1(lines)
 write_lines(fileout,lines1)
 
 
 
