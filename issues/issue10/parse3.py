"""
 parse3.py

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
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

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
  k1cpdstr = ','.join(self.k1cpds)
  parts = (self.L,self.k1,self.bdstr,k1cpdstr)
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
 #outarr1 = sorted(outarr,key=lambda out: re.sub(':*','',out))
 outarr1 = outarr
 write_lines(fileout,outarr1)
 
slp1_consonants = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh'
slp1_vowels = 'aAiIuUfFeEoO'

def get_purvapada(x):
 # Get compound form of x
 # Scharfsandhi handles many of these, but
 # some are peculiar to Apte.
 # Apte 57 convention for default masculine, neuter words
 # e.g. 'akzaH' -> 'akza', 'daRqam' -> 'daRqa'
 # exceptions to dropping final 'm' or final 'H'
 if x in ('alam','aham','itTam', 'idam', 'evam', 'kaTam',
          'kim','tUzRIm','Sam', 'svayam', 'hum',
          'uccEH',):
  return x
 if x in ('akutaH', 'agrataH', 'anyataH', 'uBayataH',):
  return x[0:-1]+'s'  # akutas, etc
 if x == 'puMs': return 'pum'
 m = re.search(f'([{slp1_vowels}])([Hm]+)$',x)
 if m != None:
  return x[0:-1] # drop ending H or m
 # other conventions will go here
 return x

def adjust_rec(rec):
 k1 = rec.k1
 for ibd,bd in enumerate(rec.bds):
  if (k1,bd) == ('agra','-nIH'):
   cpd = 'agraRIH'
   #if k1 == 'agra': print(k1,bd,cpd)
  elif re.search('^[a-zA-Z]+$',bd):
   cpd = bd
  elif bd.startswith('-'):
   purva = get_purvapada(k1)
   cpd = cpdsandhi(purva+bd)
  else:
   cpd = '?'
  # some sandhis return a word with an avagraha.
  # Current program will use these as 'k1' (key1- cdsl citation keys)
  # For this purpose, remove avagraha
  cpd1 = cpd.replace("'","")
  rec.k1cpds[ibd] = cpd1
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
