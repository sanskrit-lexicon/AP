""" v4a_0c.py
  Make cdsl compatible

"""
import re,sys
import codecs
def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   lines.append(line.strip())
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

replacements_0 = [
 ('**▪' , '▪'), # 3
 ('→	.{@{#-tI#}@}	⁞' ,
  '.{@{#-tI#}@}'),
 ('→	▪ {#˚Atman, ˚indriya#}	¦' ,
  '→	▪ {#˚Atman, ˚indriya#}	⁞'),
 ('→	▪ {#˚kulaSIlasya#}	¦' ,
  '→	▪ {#˚kulaSIlasya#}	⁞'),
 ('→		⁞ ▪ (in <ab>pl.</ab>) ' ,
  ' ▪ (in <ab>pl.</ab>) '),
 ('→	▪ {#˚ayanam#}⁞' ,
  '→	▪ {#˚ayanam#}	⁞'),
 ('˚svAgatA#}	⁞',

  '˚svAgatA#}⁞'),
 
 ]
def unused_make_newlines_0(lines):
 newlines = []
 nfind = 0 # number of line changed
 for iline,line in enumerate(lines):
  newline = line
  for old,new in replacements_0:
   newline = newline.replace(old,new)
  newlines.append(newline)
  if newline != line:
   nfind = nfind + 1
 print(f'make_newlines_0 alters {nfind} lines')
 print(f'make_newlines_0 has {len(newlines)} lines')
 return newlines

def make_newlines_1(lines):
 # ⁞¦  meta-lines
 newlines = []
 n = 0 # number of unexpected lines
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   newlines.append(line)
   continue
  m = re.search(r'^(.*?)\t(.*?)\t([⁞¦])(.*)$',line)
  if m == None:
   n = n + 1
   print(f'make_newlines_1 problem at line# {iline+1}')
   newlines.append(line)
   continue
  metaline = m.group(1)
  newlines.append(metaline)
  c = m.group(2) + m.group(3) + m.group(4)
  newlines.append(c)
 print(f'make_newlines_1 has {n} problems; {len(newlines)} lines')
 return newlines

def unused_make_newlines_2(lines):
 # →	▪.{@{#aH#}@}	⁞
 regex = "^→	▪(\.[^	]*)	⁞(.*)$"
 newlines = []
 nprob = 0 # number of unexpected lines
 nfind = 0
 mark = '⁞_2'  
 for iline,line in enumerate(lines):
  m = re.search(regex,line)
  if m != None:
   # loss of information in start0!
   a = m.group(1)
   b = m.group(2)
   c = a + mark + b
   newlines.append(c)
   nfind = nfind + 1
   continue
  newlines.append(line)
 print(f'make_newlines_2 alters {nfind} lines')
 print(f'make_newlines_2 has {len(newlines)} lines')
 return newlines

def unused_make_newlines_3(lines):
 # ' ▪∙²' ' ▪∙³'
 regex = r'( ▪∙[²³])'
 nfind = 0
 newlines = []
 for iline,line in enumerate(lines):
  parts = re.split(regex,line)
  if len(parts) == 1:
   newlines.append(line)
   nfind = nfind + 1
   continue
  prev = ''
  for ipart,part in enumerate(parts):
   if not part.startswith(' ▪∙'):
    newlines.append(prev +  part)
    prev = ''
   else:
    prev = '.' + part[-1] # ²³

 print(f'make_newlines_3 alters {nfind} lines')
 print(f'make_newlines_3 has {len(newlines)} lines')
 return newlines

def make_newlines_4(lines):
 end0 = ' ▪<LEND> ▪$'
 nend0 = len(end0)
 nfind = 0
 newlines = []
 regex2 = '^(.*) ▪<LEND> ▪\$ ▪(\[Page.*?\])$'
 regex3 = '^(.*) ▪<LEND>(.*)$'
 for iline,line in enumerate(lines):
  if line.endswith(end0):
   a = line[0:-nend0]
   newlines.append(a)
   nfind = nfind + 1
   newlines.append('<LEND>')
   continue
  m = re.search(regex2,line)
  if m != None:
   a = m.group(1)
   b = m.group(2)
   newlines.append(a)
   newlines.append('<LEND>')
   newlines.append(b)
   nfind = nfind + 1
   continue
  m = re.search(regex3,line)
  if m != None:
   a = m.group(1)
   b = m.group(2)
   newlines.append(a)
   newlines.append('<LEND>')
   newlines.append(b)
   nfind = nfind + 1
   continue
  newlines.append(line)
 print(f'make_newlines_4 alters {nfind} lines')
 print(f'make_newlines_4 has {len(newlines)} lines')
 return newlines

def make_newlines_5(lines):
 regex1 =  "^▪.━{@<ab>Comp.</ab>@}	▪(\.?[^	]+)	⁞(.*)$"
 regex2 = "^▪.━{@<ab>Comp.</ab>@} ▪(\[Page[^	]*?\])	▪(\.?[^	]+)	⁞(.*)$"
 # one case
 regex3 =  "^▪.━{@<ab>Comp.</ab>@}	([?]+)	⁞(.*)$"
 nfind = 0
 newlines = []
 mark = '⁞_5'
 for iline,line in enumerate(lines):
  m = re.search(regex1,line)
  if m != None:
   a = '.--{@<ab>Comp.</ab>@}'
   newlines.append(a)
   b1 = m.group(1)
   b2 = m.group(2)
   b = b1 + mark + b2
   newlines.append(b)
   nfind = nfind + 1
   continue
  m = re.search(regex2,line)
  if m != None:
   a = '.--{@<ab>Comp.</ab>@}'
   newlines.append(a)
   a1 = m.group(1) ## [Pagexxx]
   newlines.append(a1)
   b1 = m.group(2)
   b2 = m.group(3)
   b = b1 + mark + b2
   newlines.append(b)
   nfind = nfind + 1
   continue
  m = re.search(regex3,line)
  if m != None:
   a = '.--{@<ab>Comp.</ab>@}'
   newlines.append(a)
   b1 = m.group(1)
   b2 = m.group(2)
   b1a = '.{@{#' + b1 + '#}@}'
   b = b1a + b2
   newlines.append(b)
   nfind = nfind + 1
   continue
  newlines.append(line)
 print(f'make_newlines_5 alters {nfind} lines')
 print(f'make_newlines_5 has {len(newlines)} lines')
 return newlines

def make_newlines_6(lines):
 regex = "^→	→	⁞(.*)$"
 newlines = []
 nprob = 0 # number of unexpected lines
 nfind = 0
 mark = '⁞_6'
 for iline,line in enumerate(lines):
  m = re.search(regex,line)
  if m != None:
   # mark 
   a = m.group(1)  # append this to previous newline
   #newlines[-1] = newlines[-1] + mark + a
   if a.startswith(' ▪'):
    a = ' ' + a[2:]
   newline = mark + a
   newlines.append(newline)
   nfind = nfind + 1
   continue
  newlines.append(line)
 print(f'make_newlines_6 alters {nfind} lines')
 print(f'make_newlines_6 has {len(newlines)} lines')
 return newlines

def make_newlines_7(lines):
 # →	▪ {#˚matPalA#}	⁞
 regex = "^→	▪ (.*?)	⁞(.*)$"  #space after ▪
 newlines = []
 nfind = 0
 mark = '_7'
 for iline,line in enumerate(lines):
  m = re.search(regex,line)
  if m != None:
   a = m.group(1) 
   b = m.group(2)
   #newlines[-1] = newlines[-1] + ' ' +  mark + a + '⁞' + b
   newlines.append(mark + a + '⁞' + b)
   nfind = nfind + 1
   continue
  newlines.append(line)
 print(f'make_newlines_7 alters {nfind} lines')
 print(f'make_newlines_7 has {len(newlines)} lines')
 return newlines

def make_newlines_8(lines):
 # →	▪ {#˚matPalA#}	⁞
 regex = "^→	▪(.*?)	⁞(.*)$"  # no space after ▪
 newlines = []
 nfind = 0
 mark = '_8'
 for iline,line in enumerate(lines):
  m = re.search(regex,line)
  if m != None:
   a = m.group(1) 
   b = m.group(2)
   #newlines[-1] = newlines[-1] + mark + a + '⁞' + b
   newlines.append(mark + a + '⁞' + b)
   nfind = nfind + 1
   continue
  newlines.append(line)
 print(f'make_newlines_8 alters {nfind} lines')
 print(f'make_newlines_8 has {len(newlines)} lines')
 return newlines

def make_newlines_9(lines):
 regex = " ▪"  # 
 newlines = []
 nfind = 0
 for iline,line in enumerate(lines):
  parts = line.split(regex)
  for part in parts:
   newlines.append(part)
  if len(parts) != 1:
   nfind = nfind + 1
 print(f'make_newlines_9 alters {nfind} lines')
 print(f'make_newlines_9 has {len(newlines)} lines')
 return newlines

def check_1(lines):
 regex = "^→	▪(.*?)	⁞(.*)$"  # no space after ▪
 regex = '〔(.*?)〕'
 d = {}
 nfind = 0
 for iline,line in enumerate(lines):
  for m in re.finditer(regex,line):
   a = m.group(1)
   if a not in d:
    d[a] = 0
   d[a] = d[a] +1
 for a in d:
  print(a,d[a])

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 #newlines0 = make_newlines_0(lines)
 newlines0 = lines
 newlines1 = make_newlines_1(newlines0)
 #write_lines(fileout,newlines1)
 #exit(1)
 #newlines2 = make_newlines_2(newlines1)
 #newlines3 = make_newlines_3(newlines2)
 newlines3 = newlines1
 newlines4 = make_newlines_4(newlines3)
 write_lines(fileout,newlines4)
 exit(1)
 newlines5 = make_newlines_5(newlines4)
 newlines6 = make_newlines_6(newlines5)
 newlines7 = make_newlines_7(newlines6)
 newlines8 = make_newlines_8(newlines7)
 #newlines9 = make_newlines_9(newlines8)
 write_lines(fileout,newlines8)
 # newlines = newlines9
 # check_1(newlines)
 
