"""
 ap_0g.py

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
 newlines = []
 nfind = 0
 for iline,line in enumerate(lines):
  newline = re.sub(r'--({%<lex>.*?</lex>%})',r'━\1',line)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_1 finds {nfind} cases')
 print(f'make_newlines_1 returns {len(newlines)} lines')
 return newlines

def make_newlines_2(lines):
 replacements = [
  # print change <L>1444<pc>0080-2<k1>anAgAm
 ('--{%<ab>Caus.</ab>%}' , '━{%<ab>Caus.</ab>%}') ,
 ('--{%<ab>caus.</ab>%}' , '━{%<ab>caus.</ab>%}') ,
 ('--{%<ab>Desid.</ab>%}' , '━{%<ab>Desid.</ab>%}') ,
 ('--{%<ab>desid.</ab>%}' , '━{%<ab>desid.</ab>%}') ,
 ('--{%<ab>pass.</ab>%}' , '━{%<ab>pass.</ab>%}') ,
 ('--{%<ab>Pass.</ab>%}' , '━{%<ab>Pass.</ab>%}') ,  
  ]
 newlines = []
 nfind = 0
 for iline,line in enumerate(lines):
  newline = line
  for old,new in replacements:
   newline = newline.replace(old,new)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_2 finds {nfind} cases')
 print(f'make_newlines_2 returns {len(newlines)} lines')
 return newlines
 

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 lines1 = make_newlines_1(lines)
 lines2 = make_newlines_2(lines1)
 #lines3 = make_newlines_3(lines2)
 #lines4 = make_newlines_4(lines3)
 #lines5 = make_newlines_5(lines4)
 #lines6 = make_newlines_6(lines5)
 write_lines(fileout,lines2)
 
 
