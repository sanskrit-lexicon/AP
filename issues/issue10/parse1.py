"""
 parse1.py

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

def unused_write_recs(fileout,outrecs):
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
  parts = line.split(fieldsep)
  self.status = '?'
  (self.L,self.k1,self.bdstr,self.k1cpdstr) = parts
  self.bds = self.bdstr.split(', ')
  self.k1cpds = []
  for bd in self.bds:
   self.k1cpds.append('')
   
 def toString(self):
  default = f'?:{self.line}'
  ok = True
  for k1cpd in self.k1cpds:
   if k1cpd == '':
    ok = False
    break
  if ok == False:
   return default
  if self.status == '?':
   return default
  k1cpdstr = ','.join(self.k1cpds)
  parts = (self.status,self.L,self.k1,self.bdstr,k1cpdstr)
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
 outarr1 = sorted(outarr,key=lambda out: re.sub(':*','',out))
 write_lines(fileout,outarr1)
 
slp1_consonants = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh'
slp1_vowels = 'aAiIuUfFeEoO'

vowel_sandhi_d = {
 'aa':'A', 'aA':'A', 'Aa':'A', 'AA':'A',
 'ii':'I', 'iI':'I', 'Ii':'I', 'II':'I',
 'uu':'U', 'uU':'U', 'Uu':'U', 'UU':'U',
 'au':'o','Au':'o','aU':'o','AU':'o',
 'ai':'e','Ai':'e','aI':'e','AI':'e',
 }
def vowel_sandhi(v1,v2):
 a = v1+v2
 if a in vowel_sandhi_d:
  v = vowel_sandhi_d[a]
  return v
 return None

def join_cpd_aH(k1,bd):
 default = ''
 if not k1.endswith('aH'):
  return default  # empty string
 k1a = k1[0:-1] #  ends in 'a'
 if not bd.startswith('-'):
  return default
 if bd[1] in slp1_consonants:
  k1cpd = k1a + bd[1:]
  return k1cpd
 v1 = k1a[-1] # 
 k1b = k1a[0:-1]
 bd2 = bd[2:]
 v2 =  bd[1]
 if (v1+v2) in vowel_sandhi_d:
  v = vowel_sandhi_d[v1+v2]
  k1cpd = k1b + v + bd2
  return k1cpd
 return default

def join_cpd_am(k1,bd):
 default = ''
 if not k1.endswith('am'):
  return default  # empty string
 k1a = k1[0:-1] #  ends in 'a'
 if not bd.startswith('-'):
  return default
 if bd[1] in slp1_consonants:
  k1cpd = k1a + bd[1:]
  return k1cpd
 v1 = k1a[-1] # 
 k1b = k1a[0:-1]
 bd2 = bd[2:]
 v2 =  bd[1]
 if (v1+v2) in vowel_sandhi_d:
  v = vowel_sandhi_d[v1+v2]
  k1cpd = k1b + v + bd2
  return k1cpd

 return default

def join_cpd_a(k1,bd):
 default = ''
 if not k1.endswith('a'):
  return default  # empty string
 k1a = k1
 if not bd.startswith('-'):
  return default
 if bd[1] in slp1_consonants:
  k1cpd = k1a + bd[1:]
  return k1cpd
 v1 = k1a[-1] # 
 k1b = k1a[0:-1]
 bd2 = bd[2:]
 v2 =  bd[1]
 if (v1+v2) in vowel_sandhi_d:
  v = vowel_sandhi_d[v1+v2]
  k1cpd = k1b + v + bd2
  return k1cpd
 return default

def get_antyafunctions():
 antyas = ['aH','am','a']
 funcs = {}
 for antya in antyas:
  fname = f'join_cpd_{antya}'
  if fname not in globals():
   print(f'adjust_rec FUNCTION ERROR: {fname}')
   exit(1)
  f = globals()[fname]
  funcs[antya] = f
 return funcs
antyafunctions = get_antyafunctions()

def cpdsandhi(k1,bd0):
 dbg = (k1,bd0) == ('upAMSu','-vaDaH')
 if dbg: print(f'cpdsandhi {k1} + {bd0}')
 default = ('',None)
 m = re.search(f'^([a-zA-Z]+)([{slp1_vowels}])([Hm]?)$',k1)
 if m == None:
  return default
 a,v1,c = m.group(1),m.group(2),m.group(3)
 x = a + v1
 if dbg: print(f'a={a}, v1={v1}, c={c}, x={x}')
 #
 if not bd0.startswith('-'):
  return default
 bd = bd0[1:]
 if dbg: print(f'bd={bd}')
 m = re.search(f'^([{slp1_vowels}])([a-zA-Z]+)$',bd)
 if dbg: print(f'{bd} starts with vowel = {m != None}')
 if m != None:
  v2,b = m.group(1),m.group(2)
  v = vowel_sandhi(v1,v2)
  if v == None:
   return default
  z = a + v + b
  code = v1 + c
  return (z,code)
 m = re.search(f'^([{slp1_consonants}])([a-zA-Z]+)$',bd)
 if dbg: print(f'{bd} starts with consonant = {m != None}')
 if m == None:
  return default
 z = a + v1 + bd
 code = v1 + c
 return (z,code)

def adjust_rec(rec):
 k1 = rec.k1
 ok = True
 for ibd,bd in enumerate(rec.bds):
  k1cpd,code = cpdsandhi(k1,bd)
  if k1cpd == '':
   ok = False
   break
  rec.k1cpds[ibd] = k1cpd
 if ok:
  rec.status = code
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
 print(len(recs),"recs")
 for rec in recs:
  adjust_rec(rec)
 status_summary(recs)
 write_recs(fileout,recs)
