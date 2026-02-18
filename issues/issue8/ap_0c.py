"""
 ap_0c.py

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
 replacements = [
  # print change <L>1444<pc>0080-2<k1>anAgAm
 ('{#anAgAmin#}¦ {%<lex>m.</lex>%}' ,
  '{#anAgAmin#}¦ {%<lex>a.</lex>%}' ),
  # print change <L>3260<pc>0166-2<k1>abjA  Questionable!
 ('.{@{#-tam#}@} <ab>ind.</ab> Without obstacles, at pleasure' ,
  '.{@{#-tam#}@} {%<lex>ind.</lex>%} Without obstacles, at pleasure' ),
 ('.{@{#-SAlmaliH#}@} {%f., m.%}' ,
  '.{@{#-SAlmaliH#}@} {%<lex>f.</lex>, <lex>m.</lex>%}' ),
 #('' ,
 # '' ),
  
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
 print(f'make_newlines_1 finds {nfind} cases')
 print(f'make_newlines_1 returns {len(newlines)} lines')
 return newlines

def make_newlines_2(lines):
 replacements = [
  ('.{@{#-kumAraH, -tanayaH#}; {#sutaH#}@}' ,
   '.{@{#-kumAraH, -tanayaH, sutaH#}@}'),
 
  ('See {@{#apsaraH#}. {#-patiH#}@}' ,
  'See {#apsaraH#}. {@{#-patiH#}@}'),
  
  ('{@{#˚tA, #-kAryatA, -kftyatA#}@}' ,
   '{@{#˚tA, -kAryatA, -kftyatA#}@}'),
  
  ('.{@{#-x, t, T, d, D, n, l#}@}, and {@{#s#}. {#-rogaH#}@}' ,
   ' {#-x, t, T, d, D, n, l#}, and {#s#}. .{@{#-rogaH#}@}'),
  
  ('{@{#gArhasTya#}. {#-vayas#}@}' ,
   '{#gArhasTya#}. {@{#-vayas#}@}'),
  
  ('see {@{#nAndin#}. {#-ninAdaH, -nAdaH, -ravaH#}@}' ,
   'see {#nAndin#}. {@{#-ninAdaH, -nAdaH, -ravaH#}@}'),
  
  ('{@{#BayakAraka, -Bayakft#}. {#-kft#}@}' ,
  '{#BayakAraka, -Bayakft#}. {@{#-kft#}@}'),
  
  ('{@{#-cUqa#} ({#la#}), {#-cOla#}@}' ,
   '{@{#-cUqa(la), {#-cOla#}@}'),
  
  ('{@{#-aBisAraH#}. {#-samatA#}@}' ,
   '{#-aBisAraH#}. ▪.{@{#-samatA#}@}'),
  
  ('.{@{#(-lI)garBaH#}@} the pith of the plantain.' ,
   '.{@{#-(lI)garBaH#}@} the pith of the plantain.'),
    
  ('town in which Buddha was born. ({@{#kapilA#}@})' ,
   'town in which Buddha was born.'),
  ('.{@{#zazWI#}@} The sixth day in the dark half of {#BAdrapada#}' ,
   ' {@{#(kapilA)zazWI#}@} The sixth day in the dark half of {#BAdrapada#}'),
  
  ('.{@{#udvigna#}@}, {@{#-udvega#}@}' ,
   '.{@{#udvigna, -udvega#}@}'),
  
  ('.{@{#pUrvaH-tataH-paScAt-upari#}@} ' ,
   '{@{#pUrvaH━tataH━paScAt━upari#}@}'),
  
  ('.{@{#-ekataH--ekataH#}@}' ,
   '.{@{#ekataH━ekataH#}@}'),
  
  ('<ab>N.</ab> of the tree Pārijātaka; also' ,
   '<ab>N.</ab> of the tree Pārijātaka; also {#-˚varaH#}.'),
  
  ('.{@{#-˚varaH, -ruhA#}@} a parasitical plant.' ,
   '.{@{#ruhA#}@} a parasitical plant.'),

  ('.({@{#-pAraSvaDika#}@})',
   '.{@{#(pAraSvaDika)rAmaH#}@}'),

  ('.{@{#-rAmaH#}@} (= {#paraSurAmaH#});',
   ' (= {#paraSurAmaH#});'),

  ('{@<ab>Comp.</ab>@} a prince, the son of a king.',
   '{@<ab>Comp.</ab>@} .{@{#???#}@} a prince, the son of a king.'),

  ('.{@{#-rAjiPalA#}@}',
   '.{@{#rAjiPalA(lI)#}@}'),

  ('.({@{#-lI#}@}) a kind of cucumber (<lang>Mar.</lang>',
   ' a kind of cucumber (<lang>Mar.</lang>'),

  ('.{@{#-KaRqanam#}@} defrauding (government) of its due revenue; also',
   '.{@{#-KaRqanam#}@} defrauding (government) of its due revenue; also {#-mozaRam#}.'),

  ('.{@{#-mozaRam, -grAhaka, -grAhin#}@} {%<lex>m.</lex>%} a toll-collector.',
   '.{@{#grAhaka, -grAhin#}@} {%<lex>m.</lex>%} a toll-collector.'),

  ('.{@{#-trama#}@} [<sab>{#upa˚ sa˚#}</sab>]',
   '.{@{#-tram#}@} [<sab>{#upa˚ sa˚#}</sab>]'),
  
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

def make_newlines_3(lines):
 replacements = [
  ('{%m., f.%}' , '{%<lex>m.</lex>, <lex>f.</lex>%}'),
  ('{%m., n.%}' , '{%<lex>m.</lex>, <lex>n.</lex>%}'),
  ('{%f., n.%}' , '{%<lex>f.</lex>, <lex>n.</lex>%}'),  ]
 newlines = []
 nfind = 0
 for iline,line in enumerate(lines):
  newline = line
  for old,new in replacements:
   newline = newline.replace(old,new)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_3 finds {nfind} cases')
 print(f'make_newlines_3 returns {len(newlines)} lines')
 return newlines

def make_newlines_4(lines):
 replacements = [
  (':--' , ':−'),
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
 print(f'make_newlines_4 finds {nfind} cases')
 print(f'make_newlines_4 returns {len(newlines)} lines')
 return newlines

def make_newlines_5(lines):
 replacements = [
  ('<ab>adv.</ab>' , '<lex>adv.</lex>'),
  ('<ab>pron. a.</ab>' , '<lex>pron. a.</lex>'),
  ('<ab>pron.</ab>' , '<lex>pron.</lex>'),
  ('Pron. {%<lex>a.</lex>%}' , '{%<lex>Pron. a.</lex>%}'),
  ('<ab>num. a.</ab>' , '<lex>num. a.</lex>'),
   ('<ab>Num. a.</ab>' , '<lex>Num. a.</lex>'),
  ('<ab>subst.</ab>', '<lex>subst.</lex>'),
  ('<ab>masc.</ab>',  '<lex>masc.</lex>'),
  ('<ab>s.</ab>' , '<lex>s.</lex>'),
  ('<ab>fem.</ab>' , '<lex>fem.</lex>'),
  ('<ab>adj.</ab>' , '<lex>adj.</lex>'),
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
 print(f'make_newlines_5 changes {nfind} lines')
 print(f'make_newlines_5 returns {len(newlines)} lines')
 return newlines

def make_newlines_6(lines):
 #  {#X--Y#} -> {#X-Y#}  per v4a
 newlines = []
 nfind = 0
 def f1(m):
  old = m.group(0)  # {#X#}
  new = old.replace('--','-')
  return new
 for iline,line in enumerate(lines):
  newline = re.sub('{#(.*?)#}',f1,line)
  if newline != line:
   nfind = nfind + 1
  newlines.append(newline)
 print(f'make_newlines_6 finds {nfind} cases')
 print(f'make_newlines_6 returns {len(newlines)} lines')
 return newlines

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 lines1 = make_newlines_1(lines)
 lines2 = make_newlines_2(lines1)
 lines3 = make_newlines_3(lines2)
 lines4 = make_newlines_4(lines3)
 lines5 = make_newlines_5(lines4)
 lines6 = make_newlines_6(lines5)
 write_lines(fileout,lines6)
 
 
