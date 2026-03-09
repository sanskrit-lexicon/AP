"""
 prep1.py

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

class Entry:
 def __init__(self,iline,metaline):
  self.iline = iline
  self.meta = metaline
  m = re.search(r'^<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',metaline)
  self.L = m.group(1)
  self.k1 = m.group(3)
  self.headerraw = None  # from text before ¦ in line following metaline
  self.header = None # adjusted header
  self.headerflag = None # True if adjusted header is 'standard', else False
  self.comp = False #  True when there are compounds
  self.dbrecs = []  # (iline,{@{#X#}@},compflag)
  # self.altheader = None  # entry has alternate headwords

def getheaderadj(h):
 h1 = re.sub(r'^<hom>[0-9]+\.</hom> ',' ',h)
 h2 = re.sub(r' *{%<lex>(.*?)</lex>%} *',' ',h1)
 h3 = re.sub(r'<ab>(.*?)</ab>','',h2)
 h4 = h3.strip()
 m = re.search(r'^{#([^#]*)#}$',h4)
 if m == None:
  hadj = h4
  flag = False # non-standard
  assert '{#' in hadj
 else:
  hadj = m.group(1) # standard {# and #} removed
  flag = True
 return hadj,flag

def init_groups(lines): 
 #regex_header = '?{#(.*?)#}¦(.*)$'
 regex_headerraw = '^(.*?)¦(.*)$'
 regexbd = '{@{#(.*?)#}@}'
 compstr = '.━{@<ab>Comp.</ab>@}'
 L = None
 groups = []
 group = None
 header_problems = []
 n = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   if group != None:
    groups.append(group)
   compflag = False
   group = Entry(iline,line)
   iline_meta = iline
   continue
  if group == None:
   continue
  if line.startswith('<LEND>'):
   groups.append(group)   
   group = None
   compflag = False
   continue
  if iline == (iline_meta + 1):
   m = re.search(regex_headerraw,line)
   group.headerraw = m.group(1)
   header,headerflag= getheaderadj(group.headerraw)
   group.header = header
   group.headerflag = headerflag
  if line.startswith(compstr):
   compflag = True
   group.comp = True
  for m in re.finditer(regexbd,line):
   db = m.group(0)
   dbrec = (iline,db,compflag)
   group.dbrecs.append(dbrec)
   # if n < 10:print(f'{dbrec}')
   n = n + 1
 return groups

def check_bd(lines):
 d = {}
 bd = '{@{#'
 bdend = '#}@}'
 regex = f'(([^ ]+{bd})|( {bd}))(.*?){bdend}'
 rarepfxs = ["-" , ".━", "[" , "▪."]
 for iline,line in enumerate(lines):
  assert not line.startswith(bd)
  for m in re.finditer(regex,line):
   x = m.group(0)
   pfx = re.sub(f'{bd}.*$','',x)
   if pfx not in d:
    d[pfx] = 0
   d[pfx] = d[pfx] + 1
   if pfx in  rarepfxs:
    print(f'"{pfx}", lnum={iline+1}, line={line}')
    #print(line)
    #print(m.group(0))
    #print(m.group(1))
    #exit (1)
 pfxes = sorted(d.keys())
 n = 0
 for pfx in pfxes:
  print(f'"{pfx}" {d[pfx]}')
  n = n + d[pfx]
 print('total:',n)
 
def get_outrecs_0(groups):
 outrecs = []
 avagraha = "'"
 fieldsep = ':'
 for group in groups:
  k1 = group.k1
  header = group.header
  headerflag = group.headerflag
  if header.replace(avagraha,'') == k1:
   # no alterate headwords for this entry
   continue
  outarr = []
  L = group.L
  comp = group.comp
  n1 = 0
  n2 = 0
  for dbrec in group.dbrecs:
   (iline,db,compflag) = dbrec
   if compflag:
    n1 = n1 + 1
   else:
    n2 = n2 + 1
  ng = f'{n1},{n2}'
  if group.headerflag == False:
   status = 'man?'  # manual, not done
  else:
   status = '?'  # not manual AND not done
  k1alts = '' # 
  fields = (status,ng,L,k1,header,k1alts)
  fields_str = [str(x) for x in fields]  
  out = f'{fieldsep}'.join(fields_str)
  outarr.append(out)
  outrecs.append(outarr)
 return outrecs

def check_comps(groups):
 # if fi
 for group in groups:
  prevflag = False
  for idbrec,dbrec in enumerate(group.dbrecs):
   (iline,db,compflag) = dbrec  # compflag is Boolean
   if (prevflag == False) and compflag:
    prevflag = True
   if (prevflag == True) and (compflag == False):
    print(f'check_groups problem')
    exit(1)
#-----------------------------------------------------
if __name__=="__main__":
 opt = sys.argv[1]
 filein = sys.argv[2]
 fileout = sys.argv[3]
 lines = read_lines(filein)
 check_bd(lines)
 groups = init_groups(lines)
 check_comps(groups)

 print(f'{len(groups)} entries from {filein}')
 if opt == '0':
  outrecs = get_outrecs_0(groups)
 elif opt == '1':
  outrecs = get_outrecs_1(groups)
 else:
  print(f'unknown option="{opt}"')
  exit(1)
 write_outrecs(fileout,outrecs)
