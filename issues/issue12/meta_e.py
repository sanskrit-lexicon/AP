"""
 meta_e.py

"""
import re,sys
import codecs
sys.path.append("sandhi")
from cpdsandhi import cpdsandhi

fieldsep = ':'  

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

def add_meta_e(lines):
 newlines = []
 for line in lines:
  if not line.startswith('<L>'):
   newlines.append(line)
   continue
  # meta line.
  if '<e>' in line:
   assert line.endswith('<e>2')
   newlines.append(line)
   continue
  # add <e>1 to meta line
  newline = line + '<e>1'
  newlines.append(newline)
 return newlines
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]   # old ap.txt
 fileout = sys.argv[2]   # new ap.txt
 lines = read_lines(filein)

 outarr = add_meta_e(lines)
 write_lines(fileout,outarr)
 
