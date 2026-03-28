"""
 compounds1.py  
 combines explore1.py and parse3.py from issue10
 slight variant of compounds.py. See adjust_rec

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

def get_outlines(outrecs):
 ans = []
 for outarr in outrecs:
  for out in outarr:
   ans.append(out)
 return ans
  
class Group:
 def __init__(self,iline,metaline):
  self.iline = iline
  self.meta = metaline
  m = re.search(r'^<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',metaline)
  self.L = m.group(1)
  self.k1 = m.group(3)
  self.pc = m.group(2)
  self.comp = False #  True when there are compounds
  self.complnum = -1
  self.dbrecs = []  # list of .{@{#X#}@} AFTER '.━{@<ab>Comp.</ab>@}'

def init_groups(lines): 
 regexcpd = '^\.{@{#(.*?)#}@}'
 regexpc = '\[Page(.*?)\]'
 compstr = '.━{@<ab>Comp.</ab>@}'
 
 groups = []
 group = None
 n = 0
 ncomp = 0
 for iline,line in enumerate(lines):
  m = re.search(regexpc,line)
  if m != None:
   pc = m.group(1)
  if line.startswith('<L>'):
   group = Group(iline,line)
   pc = group.pc 
   continue
  if group == None:  # line outside of entry
   continue
  if line.startswith('<LEND>'):
   if group.comp:
    if group.dbrecs != []:
     groups.append(group)
    else:
     print(f'L={group.L},k1={group.k1} comp={group.comp},No dbrecs')
   group = None
   continue
  if line.startswith(compstr):
   # beginning of compound section of entry
   group.comp = True
   group.complnum = iline + 1
   ncomp = ncomp + 1
  if not group.comp:
   continue
  m = re.search(regexcpd,line)
  if m != None:
   # start of a new compound
   db = m.group(1)
   # get last line of group
   iline2 = None
   for i in range(1,100000):
    jline = iline + i
    linex = lines[jline]
    if re.search(regexcpd,linex) or linex.startswith('<LEND>'):
     iline2 = jline - 1
     break
   assert iline2 != None
   dbrec = (db,iline,iline2,pc)
   group.dbrecs.append(dbrec)
   n = n + 1
 print(f'# compound groups={len(groups)}')
 print(f'ncomp={ncomp}')
 return groups

def get_outrecs_2(groups):
 outrecs = []
 for group in groups:
  L = group.L
  k1 = group.k1
  outarr = []
  for dbrec in group.dbrecs:
   db,iline,iline2,pc = dbrec
   lnum = iline + 1
   lnum2 = iline2 + 1
   fields = (L,k1,f'{lnum}',f'{lnum2}',f'{pc}',db,'')
   out = fieldsep.join(fields)
   outarr.append(out)
  outrecs.append(outarr)
 return outrecs

class Rec:
 def __init__(self,line):
  self.line = line
  parts = line.split(fieldsep)
  self.status = '?'
  (self.L,self.k1,self.lnum,self.lnum2,self.pc,self.bdstr,self.k1cpdstr) = parts
  self.bds = self.bdstr.split(', ')
  self.k1cpds = []
  for bd in self.bds:
   self.k1cpds.append('')
   
 def toString(self):
  k1cpdstr = ','.join(self.k1cpds)
  parts = (self.L,self.k1,self.lnum,self.lnum2,self.pc,self.bdstr,k1cpdstr)
  newline = fieldsep.join(parts)
  return newline

def init_recs(lines):
 recs = [Rec(line) for line in lines]
 return recs

def get_reclines(recs):
 outarr = []
 for rec in recs:
  out = rec.toString()
  outarr.append(out)
 return outarr

#slp1_consonants = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh'
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
  # revision of compounds1.py
  for (old,new) in [('ss','Hs'), ('SS', 'HS'), ('zz','Hz')]:
   cpd1 = cpd1.replace(old,new)
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

def recs_by_iline(reclines):
 d = {}
 for recline in reclines:
  (L,k1,lnumstr,lnum2str,pc,bd,bdstr) = recline.split(fieldsep)
  iline = int(lnumstr) - 1
  assert iline not in d
  d[iline] = recline
 return d

def get_dmeta(lines):
 # meta line access by L
 d = {}
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  # metaline
  metaline = line
  m = re.search(r'^<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',metaline)
  L = m.group(1)
  d[L] = iline
 return d


def get_entry_indices(lines):
 entries = []
 inflag = False
 iline1 = None
 iline2 = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   iline1 = iline
   inflag = True
  elif line.startswith('<LEND>'):
   assert inflag == True
   iline2 = iline
   entry = (iline1,iline2)
   entries.append(entry)
   inflag = False
  elif not inflag:
   entry = (iline,iline)
   entries.append(entry)
 return entries

def check_compounds(d):
 e = {}
 for L in d:
  reclines_L = d[L]
  nL = 0
  for recline in reclines_L:
   (L,k1,lnumstr,lnumstr2,pc,bd,bdstr) = recline.split(fieldsep)
   cpds = bdstr.split(',')
   n = len(cpds)
   nL = nL + n
  if nL not in e:
   e[nL] = 0
  e[nL] = e[nL] + 1
 keys = e.keys()
 keys1 = sorted(keys)
 for n in keys1:
  print(f'check_compounds: {n} headwords {e[n]}')
def reclines_by_L(reclines):
 d = {}
 for recline in reclines:
  (L,k1,lnumstr,lnumstr2,pc,bd,bdstr) = recline.split(fieldsep)
  if L not in d:
   d[L] = []
  d[L].append(recline)
 if False: 
  check_compounds(d)
 return d

def get_iline_comp(iline1,iline2,lines):
 compstr = '.━{@<ab>Comp.</ab>@}'
 for iline in range(iline1,iline2+1):
  if lines[iline].startswith(compstr):
   return iline
 print(f'get_iline_comp ERROR: iline1,iline2 = {iline1},{iline2}')
 return None

def makeap1_helper_comp(reclines_L):
 section = []
 ncpds = []
 compstr = '.━{@<ab>Comp.</ab>@}'
 k1cpds = []
 for recline in reclines_L:
  (L,k1,lnumstr,lnumstr2,pc,bd,bdstr) = recline.split(fieldsep)
  cpds = bdstr.split(',')
  for cpd in cpds:
   k1cpds.append(cpd)
 ncpds = len(k1cpds)
 cpdstr0 = ', '.join(k1cpds)
 cpdstr1 = '{#' + cpdstr0 + '#}' # devanagari
 cpdstr = f'{compstr}: {cpdstr1}'
 section = [cpdstr, '<LEND>']
 return section,ncpds

def makeap1_helper_cpd(recline,lines,L1,Lincr):
 regexcpd1 = '^\.{@{#(.*?)#}@}(.*)$'
 (L1par,k1par,lnumstr,lnumstr2,pc,bd,bdstr) = recline.split(fieldsep)
 #L = float(Lstr)
 iline1 = int(lnumstr) - 1
 iline2 = int(lnumstr2) - 1
 meta0 = lines[iline1]
 cpds = bdstr.split(',')
 m = re.search(regexcpd1,meta0)
 newline1 = '{#' + k1par + '#} + {#' + m.group(1) + '#}' +'¦' + m.group(2)
 section = []
 L = L1
 for icpd,cpd in enumerate(cpds):
  cpdmeta = f'<L>{L:.3f}<pc>{pc}<k1>{cpd}<k2>{cpd}<e>2'
  Llast = L
  section.append(cpdmeta)
  if icpd == 0:
   Lpar = L
   section.append(newline1)
   for iline in range(iline1+1,iline2+1):
    line = lines[iline]
    section.append(line)
  else:
   section.append('{{Lbody=' + f'{Lpar:.3f}' + '}}')
  L = L + Lincr # for next cpd
  section.append('<LEND>')
  section.append('') # optional empty line
 return section,Llast

def makeap1_helper(iline1,iline2,lines,reclines_L,Lpstr,k1p):
 old_section = lines[iline1:iline2+1]
 regexcpd = '^\.{@{#(.*?)#}@}'
 iline_comp = get_iline_comp(iline1,iline2,lines)
 if iline_comp == None:
  return old_section
 section_parent = lines[iline1:iline_comp]
 section_comp,ncpds = makeap1_helper_comp(reclines_L)
 ilinea = iline_comp + 1
 Lp = float(Lpstr)
 Lincr = 0.002  # can refine, using ncpds
 L0 = Lp + 0.020  # (+ 0.020 (* 0.002 487)) 0.994
 subsections = []
 subsections.append(section_parent)
 subsections.append(section_comp)
 L1 = L0
 for irecline,recline in enumerate(reclines_L):
  section_cpd,L2 = makeap1_helper_cpd(recline,lines,L1,Lincr)
  L1 = L2 + Lincr
  subsections.append(section_cpd)
 #join subsections and return result
 newsection = []
 for subsection in subsections:
  for line in subsection:
   newsection.append(line)
 return newsection

def makeap1(entry_indices,lines,reclines):
 d1 = reclines_by_L(reclines)
 sections = []
 for iline1,iline2 in entry_indices:
  section = lines[iline1:iline2+1]
  if not section[0].startswith('<L>'):
   # no change to non-entry sections
   sections.append(section)
   continue
  metaline = section[0]
  m = re.search(r'^<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',metaline)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  if L not in d1:
   # No compounds in this entry section. So no change to it
   sections.append(section)
   continue
  # modify an entry with compounds
  reclines_L = d1[L]
  newsection = makeap1_helper(iline1,iline2,lines,reclines_L,L,k1)
  sections.append(newsection)
 return sections

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout1 = sys.argv[2]  # compounds.txt
 fileout2 = sys.argv[3]  #
 lines = read_lines(filein)
 groups = init_groups(lines)

 print(f'{len(groups)} entries from {filein}')
 outrecs = get_outrecs_2(groups)
 outlines = get_outlines(outrecs)
 #write_lines('tempout.txt',outlines) dbg

 recs = init_recs(outlines)
 for rec in recs:
  adjust_rec(rec)
 # status_summary(recs)
 reclines = get_reclines(recs)
 write_lines(fileout1,reclines)  # compounds.txt
 entry_indices = get_entry_indices(lines)
 apsections =  makeap1(entry_indices,lines,reclines)
 aplines = []
 for section in apsections:
  for line in section:
   aplines.append(line)

 write_lines(fileout2,aplines)
 
