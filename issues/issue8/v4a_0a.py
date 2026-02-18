""" v4a_0a.py
  some corrections to AP57_AB_v4a.txt

"""
import re,sys
import codecs
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir('transcoder')

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

replacements_1 = [
 ('<sab>{#na˚ bahuvrIhiH#}<sab>',
  '<sab>{#na˚ bahuvrIhiH#}</sab>'),
 ('<ls>Kau. A. (7. 13)</LS>',
  '<ls>Kau. A. (7. 13)</ls>'),
 ]

def make_newlines_1(lines):
 newlines = []
 nfind = 0
 for line in lines:
  newline = line
  for old,new in replacements_1:
   newline = newline.replace(old,new)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_1 changes {nfind} lines')
 return newlines

def make_newlines_2(lines):
 d = {'36703':False, '36704':False}
 newlines = []
 for iline,line in enumerate(lines):
  m = re.search(r'^<L>(.*?)<pc>',line)
  if m == None:
   newlines.append(line)
   continue
  L = m.group(1)
  if L not in d:
   newlines.append(line)
   continue
  # L is in d.
  if d[L] == False:
   # add first instance
   newlines.append(line)
   d[L] = True
   continue
  # L is duplicate
  print(f'Remove duplicate line. L={L} at line # {iline+1}')
 return newlines

def make_newlines_3(lines):
 newlines = []
 nfind = 0
 def f1(m):
  slp1 = m.group(1)
  deva = transcoder.transcoder_processString(slp1,'slp1','deva')
  return deva
 
 def f(m):
  old = m.group(0)
  new = re.sub('{#(.*?)#}',f1,old)
  return new
 for iline,line in enumerate(lines):
  newline = re.sub('<ls[^<]*\{#.*?</ls>',f,line)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_3 finds {nfind} cases')
 return newlines

replacements_4 = [
 ('<L>3260<pc>0166-2<k1>abjA<k2>abjA	{#abjA#}	¦ Born in water',
  '<L>3260<pc>0166-2<k1>abjA<k2>abjA	{#abjA#}	¦ {%〔m.〕%} <ab>Ved.</ab> ({#bjAH#} Born in water'),
 ('🠚	🞄.{@{#-darSin, -dfzwi#}@}	⁞ {%〔m.〕%} ‘of unerring mind or view’',
  '🠚	🞄.{@{#-darSin, -dfzwi#}@}	⁞ {%〔a.〕%} ‘of unerring mind or view’'),
 # typo
 ('{#AntarAla#}	¦ {%〔m.〕%}',
  '{#AntarAla#}	¦ {%〔a.〕%}'),
 # typo
 ('{@{#-ojas#}@}	⁞ {%〔m.〕%} ‘of excellent valour’',
  '{@{#-ojas#}@}	⁞ {%〔a.〕%} ‘of excellent valour’'),
 # MISSING DATA IN v4a
 ('.{@{#-prati(tI)kAra#}@} ({#nizprati(tI)kAra#}), {@{#-pratikriya#}@}, ({@{#-ram#}@})	⁞ {%〔ind.〕%} uninterruptedly.',
  
  '.{@{#-prati(tI)kAra#}@} ({#nizprati(tI)kAra#}), {@{#-pratikriya#}@}, ({@{#nizpratikriya#}@}) {%〔a.〕%} .²1 incurable, irremediable; {#sarvaTA nizpratIkAreyamApadupasTitA#} <ls>K. 151</ls>. .²2 unobstructed, uninterrupted. ({@{#-ram#}@})	⁞ {%〔ind.〕%} uninterruptedly.'),
 #('',
 # ''),
 #('',
 # ''),
 ]

def make_newlines_4(lines):
 newlines = []
 nfind = 0
 for line in lines:
  newline = line
  for old,new in replacements_4:
   newline = newline.replace(old,new)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_1 changes {nfind} lines')
 return newlines

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 lines1 = make_newlines_1(lines)
 lines2 = make_newlines_2(lines1)
 lines3 = make_newlines_3(lines2)
 #lines4 = make_newlines_4(lines3)
 write_lines(fileout,lines3)
