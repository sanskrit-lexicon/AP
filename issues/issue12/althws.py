"""
 althws.py

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

class Section:
 def __init__(self,iline,line):
  self.iline = iline
  self.line = line
  self.lines = [line]
  self.entry = line.startswith('<L>')
  
def init_sections(lines):
 sections = []
 entry = False
 section = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   section = Section(iline,line)
   sections.append(section)
   entry = True
   continue
  if line.startswith('<LEND>'):
   section.lines.append(line)
   entry = False
   section = None
   continue
  if entry == True:
   section.lines.append(line)
   continue
  # line not in entry
  if section == None:
   section = Section(iline,line)
   sections.append(section)
   continue
  # another line in non-entry section
  section.lines.append(line)
 return sections

def parse_althws_input(lines):
 d = {}
 for line in lines:
  (L,k1,althws_str) = line.split(fieldsep)
  assert L not in d
  d[L] = (L,k1,althws_str)
 return d

def sections_to_outarr(sections):
 outarr = []
 for section in sections:
  for line in section.lines:
   outarr.append(line)
 return outarr

def get_next_L(sections,isection):
 Lnext = None
 nsections = len(sections)
 i1=isection + 1
 if not (i1 < nsections):
  return Lnext
 s1 = sections[i1]
 if s1.entry:
  meta1 = s1.lines[0] # meta-line
  m = re.search(r'<L>(.*?)<pc>',meta1)
  Lnext = m.group(1)
  return Lnext
 # try one more
 i2 = isection + 2
 if not (i2 < nsections):
  return Lnext
 s2 = sections[i2]
 if not s2.entry:
  return Lnext
 meta2 = s2.lines[0] # meta-line
 m = re.search(r'<L>(.*?)<pc>',meta2)
 Lnext = m.group(1)
 return Lnext

def update_sections_helper(L,Lnew,pc,althw):
 # all parms are strings
 meta = f'<L>{Lnew}<pc>{pc}<k1>{althw}<k2>{althw}'
 body = '{{Lbody=' + f'{L}' + '}}'
 lend = '<LEND>'
 section = [meta,body,lend]
 return section

def update_sections(sections,althwsd):
 comma = ',' # separator for althws
 sections1 = []
 maxalthws = 0
 for isection,section in enumerate(sections):
  if section.entry == False:
   sections1.append(section)
   continue
  
  meta = section.lines[0]
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',meta)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  if L not in althwsd:
   sections1.append(section)
   continue
  dbg = False
  #dbg = (L == '12980')
  # append the old section
  sections1.append(section)
  # construct new section for each althw
  (L1a,k1a,althws_str) = althwsd[L]
  assert L1a == L
  assert k1a == k1
  if dbg: print(f'{althwsd[L]}')
  althws = althws_str.split(comma)
  nalthws = len(althws)
  if nalthws > maxalthws:
   print(f'chk: L={L}, nalthws={nalthws}')
   maxalthws = nalthws
  if dbg: print(f'{althws}')
  Lnext = get_next_L(sections,isection)
  Lnext0 = float(Lnext)
  L0 = float(L)
  Lincr = float(0.002)
  Lnext0 = float(Lnext)
  L1 = L0
  for ialthw,althw in enumerate(althws):
   if dbg: print(f'althw#{ialthw}={althw}')
   L1 = L1 + Lincr
   if not (L1 < Lnext0):
    print('L-error at L=',L)
    continue
   Lnew = f'{L1:.03f}'
   newsectionlines  =  update_sections_helper(L,Lnew,pc,althw)
   if dbg: print(f'new section={newsectionlines}')
   iline0 = 0 # not used further
   line0 = newsectionlines[0]
   section1 = Section(iline0,line0)
   section1.lines = newsectionlines
   sections1.append(section1)
 return sections1
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]   # old ap.txt
 filein1 = sys.argv[2]   # althws_input.txt
 fileout = sys.argv[3]   # new ap.txt
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 althwsd = parse_althws_input(lines1)
 sections = init_sections(lines)
 sections1 = update_sections(sections,althwsd)
 outarr = sections_to_outarr(sections1)
 write_lines(fileout,outarr)
 
