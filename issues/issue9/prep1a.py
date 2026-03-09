"""
 prep1a.py

"""
import re,sys
import codecs

fieldsep = ':'  # agrees with prep1.py
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

def write_recs(fileout,outrecs):
 with codecs.open(fileout,'w','utf-8') as f:
  for outarr in outrecs:
   for out in outarr:
    f.write("%s\n" % out)
 print(f'{len(outrecs)} records written to {fileout}')

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,'w','utf-8') as f:
  for outarr in outrecs:
   for out in outarr:
    f.write("%s\n" % out)
 print(f'{len(outrecs)} records written to {fileout}')
 
class Rec:
 def __init__(self,line):
  self.line = line
  #parts = line.split(f'{fieldsep}')
  parts = line.split(fieldsep)
  (self.status,self.ng,self.L,self.k1,self.header,self.k1alts) = parts
 def toString(self):
  parts = (self.status,self.ng,self.L,self.k1,self.header,self.k1alts)
  newline = fieldsep.join(parts)
  return newline
 
def init_recs(lines):
 recs = [Rec(line) for line in lines]
 return recs

def write_recs(fileout,recs):
 outarr = []
 for rec in recs:
  out = rec.toString()
  outarr.append(out)
 write_lines(fileout,outarr)
 
def filter_1(recsin):
 # filter:  
 recs = []
 avagraha = "'" # slp1
 for rec in recsin:
  if rec.n1 != 0:
   continue
  if rec.n2 != 0:
   continue
  if '.' in rec.L:
   continue
  k1 = rec.k1
  header = rec.header
  hparts = header.split(', ')
  if hparts[0].replace(avagraha,'')  != k1:
   continue
  flag = True
  for hpart in hparts:
   m = re.search(r"^[a-zA-Z']+$",hpart)
   if m == None:
    flag = False
    break
  if not flag:
   continue
  recs.append(rec)
 return recs


def filter_2(recsin):
 # filter:  
 recs = []
 avagraha = "'" # slp1
 for rec in recsin:
  if rec.n1 != 0:
   continue
  if rec.n2 != 0:
   continue
  if '.' in rec.L:
   continue
  k1 = rec.k1
  header = rec.header
  m = re.search(r"^[a-zA-Z()]+$",header)
  if m == None:
   continue
  if not '(' in header:
   continue
  # when (X) is removed from header, shoud have rec.k1
  header1 = re.sub(r'[(](.*?)[)]','',header)
  k1 = rec.k1
  if header1 != k1:
   print(f'filter_2 skips: {rec.line}')
   continue
  recs.append(rec)
 return recs

def get_outrecs_2_helper(header):
 """
 d = {
  'u(uM)kuRaH': '',
  'ja(jaY)jaH': '',
  'hf(hri)RIyate': 'hriRIyate',
  }
 """
 # header = A(B)C
 x = header
 while '(' in x:
  m = re.search(r'(.*?)[(](.*?)[)](.*)$', x)
  a = m.group(1)
  b = m.group(2)
  c = m.group(3)
  na = len(a)
  nb = len(b)
  a1 = a[0:-nb]+b  # works even if nb > na
  x = a1 + c
 return x
      
def get_outrecs_2(recsin):
 recs = filter_2(recsin)
 print(f'filter_2 finds {len(recs)}')
 outrecs = []
 for rec in recs:
  outarr = []
  oldparts = rec.line.split(f'{fieldsep}')
  newparts = ['P'] + oldparts
  out = f'{fieldsep}'.join(newparts)
  outarr.append(out)
  # by filter_2, header contains one or more parens
  header = rec.header
  lparens = re.findall(r'\(', header)
  nlparens = len(lparens)
  L = rec.L
  L1 = float(L)
  L2 = L1
  Lincr = 0.1
  k1 = rec.k1
  L2 = L2 + Lincr
  Lnew = '%0.1f' % L2
  header1 = get_outrecs_2_helper(header)
  outparts = ('C',L,Lnew,k1,header1)
  out = f'{fieldsep}'.join(outparts)
  outarr.append(out)
  outrecs.append(outarr)
 return outrecs

def adjust_rec_1(rec):
 # X, Y, Z where Y, Z ,etc match [a-zA-Z]+
 avagraha = "'" # slp1
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 althws = []
 for x in hparts[1:]:
  if not re.search('^[a-zA-Z]+$',x):
   return False
  althws.append(x)
 if althws == []:
  return False
 rec.k1alts = ','.join(althws)
 rec.status = '01'
 return True

def adjust_rec_2(rec):
 # XtA, -tvam
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 if len(hparts) != 2:
  return False
 m = re.search(r'^(.*?)tA$',hparts[0])
 if m == None:
  return False
 x = m.group(1)
 if hparts[1] != '-tvam':
  return False
 althw = x + 'tvam'
 rec.k1alts = althw
 rec.status = '02'
 return True

def adjust_rec_3(rec):
 # Xtvam, -tA
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 if len(hparts) != 2:
  return False
 m = re.search(r'^(.*?)tvam$',hparts[0])
 if m == None:
  return False
 x = m.group(1)
 if hparts[1] != '-tA':
  return False
 althw = x + 'tA'
 rec.k1alts = althw
 rec.status = '03'
 return True

def adjust_rec_4(rec):
 # XyiH, -yI
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 if len(hparts) != 2:
  return False
 m = re.search(r'^(.*?)(.)iH$',hparts[0])
 if m == None:
  return False
 x = m.group(1)
 c = m.group(2)
 if hparts[1] != ('-' + c + 'I'):
  return False
 althw = x + c + 'I'
 rec.k1alts = althw
 rec.status = '04'
 return True

def adjust_rec_5(rec):
 # XyaH, -yam
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 if len(hparts) != 2:
  return False
 m = re.search(r'^(.*?)(.)aH$',hparts[0])
 if m == None:
  return False
 x = m.group(1)
 c = m.group(2)
 if hparts[1] != ('-' + c + 'am'):
  return False
 althw = x + c + 'am'
 rec.k1alts = althw
 rec.status = '05'
 return True

def adjust_rec_6(rec):
 # Xyam, -yA
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 if len(hparts) != 2:
  return False
 m = re.search(r'^(.*?)(.)am$',hparts[0])
 if m == None:
  return False
 x = m.group(1)
 c = m.group(2)
 if hparts[1] != ('-' + c + 'A'):
  return False
 althw = x + c + 'A'
 rec.k1alts = althw
 rec.status = '06'
 return True

def adjust_rec_7(rec):
 # XyaH, -yA
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 if len(hparts) != 2:
  return False
 m = re.search(r'^(.*?)(.)aH$',hparts[0])
 if m == None:
  return False
 x = m.group(1)
 c = m.group(2)
 if hparts[1] != ('-' + c + 'A'):
  return False
 althw = x + c + 'A'
 rec.k1alts = althw
 rec.status = '07'
 return True

def adjust_rec_8(rec):
 # aDigamaH, -manam: -> aDigamanam
 #  
 hparts = rec.header.split(', ')
 k1chk = hparts[0]
 if k1chk != rec.k1:
  return False
 if len(hparts) != 2:
  return False
 m = re.search(r'-(.)anam$',hparts[1])
 if m == None:
  return False
 c = m.group(1)
 m = re.search(f'^(.*?){c}aH$',hparts[0])
 if m == None:
  return False
 x = m.group(1)
 althw = x + c + 'anam'
 rec.k1alts = althw
 rec.status = '08'
 return True

def adjust_rec_9(rec):
 # pari(rI)RAmaH
 # pa ri (rI) RAmaH -> parIRAmaH
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(..)[(](..)[)]([a-zA-Z]*)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 D = m.group(4)
 b1,b2 = b
 c1,c2 = c
 if b1 != c1: return False
 if b2 != c2.lower() : return False
 k1chk = A + b + D
 if k1chk != rec.k1: return False
 althw = A + c + D
 rec.k1alts = althw
 rec.status = '09'
 return True

def adjust_rec_10(rec):
 # pari(rI)RAmaH
 # pa ri (rI) RAmaH -> parIRAmaH
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(..)[(](..)[)]([a-zA-Z]*)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 D = m.group(4)
 b1,b2 = b
 c1,c2 = c
 if b1 != c1: return False
 #if b2 != c2.lower() : return False
 k1chk = A + b + D
 if k1chk != rec.k1: return False
 althw = A + c + D
 rec.k1alts = althw
 rec.status = '10'
 return True

def adjust_rec_11(rec):
 # aBisA(SA)ntv
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(..)[(](..)[)]([a-zA-Z]*)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 D = m.group(4)
 b1,b2 = b
 c1,c2 = c
 if b2 != c2: return False
 #if b2 != c2.lower() : return False
 k1chk = A + b + D
 if k1chk != rec.k1: return False
 althw = A + c + D
 rec.k1alts = althw
 rec.status = '11'
 return True

def adjust_rec_12(rec):
 # avacCa(cCA)daH
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(...)[(](...)[)]([a-zA-Z]*)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 D = m.group(4)
 b1,b2,b3 = b
 c1,c2,c3 = c
 if (b1+b2) != (c1+c2): return False
 k1chk = A + b + D
 if k1chk != rec.k1: return False
 althw = A + c + D
 rec.k1alts = althw
 rec.status = '12'
 return True

def adjust_rec_13(rec):
 # aBizya(sya)ndaH
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(...)[(](...)[)]([a-zA-Z]*)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 D = m.group(4)
 b1,b2,b3 = b
 c1,c2,c3 = c
 if (b2+b3) != (c2+c3): return False
 k1chk = A + b + D
 if k1chk != rec.k1: return False
 althw = A + c + D
 rec.k1alts = althw
 rec.status = '13'
 return True

def adjust_rec_14(rec):
 # indukaH(kuH)
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(...)[(](...)[)]([a-zA-Z]*)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 D = m.group(4)
 b1,b2,b3 = b
 c1,c2,c3 = c
 if (b1+b3) != (c1+c3): return False
 k1chk = A + b + D
 if k1chk != rec.k1: return False
 althw = A + c + D
 rec.k1alts = althw
 rec.status = '14'
 return True

def adjust_rec_15(rec):
 # :akava, -vA
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(..), -(..)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 b1,b2 = b
 c1,c2 = c
 if b1 != c1: return False
 k1chk = A + b
 if k1chk != rec.k1: return False
 althw = A + c
 rec.k1alts = althw
 rec.status = '15'
 return True

def adjust_rec_16(rec):
 # :akava, -vA
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(..), -(..)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 b1,b2 = b
 c1,c2 = c
 if b2 != c2: return False
 k1chk = A + b
 if k1chk != rec.k1: return False
 althw = A + c
 rec.k1alts = althw
 rec.status = '16'
 return True

def adjust_rec_17(rec):
 # :kuWAraH, -rI
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(...), -(..)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 b1,b2,b3 = b
 c1,c2 = c
 if b1 != c1: return False
 k1chk = A + b
 if k1chk != rec.k1: return False
 althw = A + c
 rec.k1alts = althw
 rec.status = '17'
 return True

def adjust_rec_18(rec):
 # anavekza, -kzA
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(...), -(...)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 b1,b2,b3 = b
 c1,c2,c3 = c
 if (b1+b2) != (c1+c2): return False
 k1chk = A + b
 if k1chk != rec.k1: return False
 althw = A + c
 rec.k1alts = althw
 rec.status = '18'
 return True

def adjust_rec_19(rec):
 # anuprapAtam, -dam
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(...), -(...)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 b1,b2,b3 = b
 c1,c2,c3 = c
 if (b2+b3) != (c2+c3): return False
 k1chk = A + b
 if k1chk != rec.k1: return False
 althw = A + c
 rec.k1alts = althw
 rec.status = '19'
 return True

def adjust_rec_20(rec):
 # kayADuH, -DUH
 header = rec.header
 m = re.search(r'^([a-zA-Z]*)(...), -(...)$',header)
 if m == None: return False
 A = m.group(1)
 b = m.group(2)
 c = m.group(3)
 b1,b2,b3 = b
 c1,c2,c3 = c
 if (b1+b3) != (c1+c3): return False
 k1chk = A + b
 if k1chk != rec.k1: return False
 althw = A + c
 rec.k1alts = althw
 rec.status = '20'
 return True

def adjust_rec_21(rec):
 # anasUya, -yaka
 header = rec.header
 m = re.search(r'^([a-zA-Z]+), -(.+)ka$',header)
 if m == None: return False
 A = m.group(1)
 B = m.group(2)
 C = 'ka'
 if not A.endswith(B): return False
 k1chk = A
 if k1chk != rec.k1: return False
 althw = A + C
 rec.k1alts = althw
 rec.status = '21'
 return True

def adjust_rec_22(rec):
 # anulepaH, -lepanam
 # anulepaka, -lepin:   
 header = rec.header
 m = re.search(r'^([a-zA-Z]+), -([a-zA-Z][a-zA-Z][a-zA-Z])([a-zA-Z]+)$',header)
 if m == None: return False
 A = m.group(1)
 B = m.group(2)
 C = m.group(3)
 if A != rec.k1: return False
 x = re.findall(B,A)
 if len(x) != 1: return False
 A1 = re.sub(f'{B}.*$','',A)
 althw = A1 + B + C
 rec.k1alts = althw
 rec.status = '22'
 return True

def adjust_rec_23(rec):
 # anulepaH, -lepanam
 # anulepaka, -lepin:   
 header = rec.header
 m = re.search(r'^([a-zA-Z]+), -([a-zA-Z][a-zA-Z])([a-zA-Z]+)$',header)
 if m == None: return False
 A = m.group(1)
 B = m.group(2)
 C = m.group(3)
 if A != rec.k1: return False
 x = re.findall(B,A)
 if len(x) != 1: return False
 A1 = re.sub(f'{B}.*$','',A)
 althw = A1 + B + C
 rec.k1alts = althw
 rec.status = '23'
 return True

def adjust_rec_24(rec):
 # anulepaH, -lepanam
 # anulepaka, -lepin:   
 header = rec.header
 m = re.search(r'^([a-zA-Z]+), -([a-zA-Z])([a-zA-Z]+)$',header)
 if m == None: return False
 A = m.group(1)
 B = m.group(2)
 C = m.group(3)
 if A != rec.k1: return False
 x = re.findall(B,A)
 if len(x) != 1: return False
 A1 = re.sub(f'{B}.*$','',A)
 althw = A1 + B + C
 rec.k1alts = althw
 rec.status = '24'
 return True

def adjust_rec(rec):
 if rec.status.startswith('man'):
  return
 if rec.status != '?':
  return # already done
 if adjust_rec_1(rec): return
 if adjust_rec_2(rec): return
 if adjust_rec_3(rec): return
 if adjust_rec_4(rec): return
 if adjust_rec_5(rec): return
 if adjust_rec_6(rec): return
 if adjust_rec_7(rec): return
 if adjust_rec_8(rec): return
 if adjust_rec_9(rec): return
 if adjust_rec_10(rec): return
 if adjust_rec_11(rec): return
 if adjust_rec_12(rec): return
 if adjust_rec_13(rec): return
 if adjust_rec_14(rec): return
 if adjust_rec_15(rec): return
 if adjust_rec_16(rec): return
 if adjust_rec_17(rec): return
 if adjust_rec_18(rec): return
 if adjust_rec_19(rec): return
 if adjust_rec_20(rec): return
 if adjust_rec_21(rec): return
 if adjust_rec_22(rec): return
 if adjust_rec_23(rec): return
 if adjust_rec_24(rec): return
 return

def status_summary(recs):
 d ={}
 for rec in recs:
  if rec.status not in d:
   d[rec.status] = 0
  d[rec.status] = d[rec.status] + 1
 keys = sorted(d.keys())
 ntot = 0
 for key in keys:
  n = d[key]
  ntot = ntot + n
  print(f'{key} {n}')
 print(f'Total {ntot}')
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 recs = init_recs(lines)
 for rec in recs:
  adjust_rec(rec)
 status_summary(recs)
 write_recs(fileout,recs)
 exit(1)
 if opt == '1':
  outrecs = get_outrecs_1(recs)
 elif opt == '2':
  outrecs = get_outrecs_2(recs)
 else:
  print(f'unknown option="{opt}"')
  exit(1)
 write_outrecs(fileout,outrecs)
