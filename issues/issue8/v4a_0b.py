""" v4a_0b.py
  
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


def unused_make_newlines_1(lines):
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


replacements_1 = [
 ('<L>3260<pc>0166-2<k1>abjA<k2>abjA	{#abjA#}	¦ Born in water',
  '<L>3260<pc>0166-2<k1>abjA<k2>abjA	{#abjA#}	¦ {%〔m.〕%} <ab>Ved.</ab> ({#bjAH#} Born in water'),
 ('.{@{#-darSin, -dfzwi#}@}	⁞ {%〔m.〕%} ‘of unerring mind or view’',
  '.{@{#-darSin, -dfzwi#}@}	⁞ {%〔a.〕%} ‘of unerring mind or view’'),
 # typo
 ('{#AntarAla#}	¦ {%〔m.〕%}',
  '{#AntarAla#}	¦ {%〔a.〕%}'),
 # typo
 ('{@{#-ojas#}@}	⁞ {%〔m.〕%} ‘of excellent valour’',
  '{@{#-ojas#}@}	⁞ {%〔a.〕%} ‘of excellent valour’'),
 # MISSING DATA 
 ('.{@{#-prati(tI)kAra#}@} ({#nizprati(tI)kAra#}), {@{#-pratikriya#}@}, ({@{#-ram#}@})	⁞ {%〔ind.〕%} uninterruptedly.',
  
  '.{@{#-prati(tI)kAra#}@} ({#nizprati(tI)kAra#}), {@{#-pratikriya#}@}, ({@{#nizpratikriya#}@}) {%〔a.〕%}  ▪.²1 incurable, irremediable; {#sarvaTA nizpratIkAreyamApadupasTitA#} <ls>K. 151</ls>.  ▪.²2 unobstructed, uninterrupted. ({@{#-ram#}@})	⁞ {%〔ind.〕%} uninterruptedly.'),

 # MISSING DATA 
 ('→	▪.{@{#-saMtati#}@} ({#niHsaMtati#}), {@{#-saMtAna#}@}, {@{#-saMdigDa#}@} ({#niHsaMdigDa#}), {@{#-saMdeha#}@}, {@{#-saMDi#}@} ({#nissaMDi, niHsaMDi#})	⁞ {%〔a.〕%} having no joints perceptible, ▪ compact, firm, close.',
  
  '→	▪.{@{#-saMtati#}@} ({#niHsaMtati#}), {@{#-saMtAna#}@} ({@{#niHsaMtAna#}@}) ▪ {%〔a.〕%} childless. ▪.{@{#-saMdigDa#}@} ({#niHsaMdigDa#}), {@{#-saMdeha#}@}, ({@{#niHsaMdeha#}@}) ▪ {%〔a.〕%} see {#niHsaMSaya#}. ▪.{@{#-saMDi#}@} ({#nissaMDi, niHsaMDi#})	⁞ {%〔a.〕%} having no joints perceptible, ▪ compact, firm, close.'),
 
 ('→	▪.{@{#-janman#}@} ({#prAgjanman#}) {%〔n.〕%}, {@{#-jAtiH#}@}, {@{#-jyotizaH#}@} ({#prAgjyotizaH#})',
  '→	▪.{@{#-janman#}@} ({#prAgjanman#}) {%〔n.〕%}, {@{#-jAtiH#}@}, ({#prAgjAtiH#}) {%〔f.〕%} ▪ a former birth. {@{#-jyotizaH#}@} ({#prAgjyotizaH#})'),
 
 #('',
 # ''),
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

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 lines1 = make_newlines_1(lines)
 write_lines(fileout,lines1)
