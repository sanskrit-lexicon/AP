"""
 ap_0i_2.py

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

def make_newlines_1(lines):
 """
 ^{#X#}, {#Y#}¦  ==>  {#X, Y#}¦
 """
 regex = r'^{#([^#]*)#}, {#([^#]*)#}¦'
 newlines = []
 nfind = 0
 for iline,line in enumerate(lines):
  newline = re.sub(regex,r'{#\1, \2#}¦',line)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_1 finds {nfind} cases')
 print(f'make_newlines_1 returns {len(newlines)} lines')
 return newlines

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 lines1 = make_newlines_1(lines)
 write_lines(fileout,lines1)
 
 
