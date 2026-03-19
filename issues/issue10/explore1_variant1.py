"""
 explore1_variant1.py

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
  self.comp = False #  True when there are compounds
  self.complnum = -1
  self.dbrecs = []  # list of .{@{#X#}@} AFTER '.━{@<ab>Comp.</ab>@}'

def init_groups(lines): 
 regexcpd = '^\.{@{#(.*?)#}@}'
 compstr = '.━{@<ab>Comp.</ab>@}'
 groups = []
 group = None
 n = 0
 ncomp = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   group = Entry(iline,line)
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
   group.comp = True
   group.complnum = iline + 1
   ncomp = ncomp + 1
  if group.comp:
   m = re.search(regexcpd,line)
   if m != None:
    db = m.group(1)
    dbrec = (db,iline)
    #
    group.dbrecs.append(dbrec)
    # if n < 10:print(f'{dbrec}')
    n = n + 1
 print(f'# compound groups={len(groups)}')
 print(f'ncomp={ncomp}')
 return groups

def get_outrecs_1(groups):
 outrecs = []
 fieldsep = ':'
 for group in groups:
  L = group.L
  k1 = group.k1
  outarr = []
  ncomp = len(group.dbrecs)
  fields = (L,k1,str(ncomp))
  # fields = [str(group.complnum)] dbg with write_L_comps
  out = fieldsep.join(fields)
  outarr.append(out)
  outrecs.append(outarr)
 return outrecs

def get_outrecs_2(groups):
 outrecs = []
 fieldsep = ':'
 for group in groups:
  L = group.L
  k1 = group.k1
  outarr = []
  for dbrec in group.dbrecs:
   db,iline = dbrec
   fields = (L,k1,db,'')  
   out = fieldsep.join(fields)
   outarr.append(out)
  outrecs.append(outarr)
 return outrecs

def write_L_comps(fileout,lines):
 # for debugging.
 compstr = '.━{@<ab>Comp.</ab>@}'
 group = None
 n = 0
 ncomp = 0
 outarr = []
 fieldsep = ':'
 for iline,line in enumerate(lines):
  if line.startswith(compstr):
   outarr.append(str(iline+1))
 write_lines(fileout,outarr)

def temp_prep_ap_0c(fileout,lines,groups):
 d = {}
 for group in groups:
  for dbrec in group.dbrecs:
   db,iline = dbrec
   if '(' in db:
    d[iline] = True
 outarr = []
 for iline,line in enumerate(lines):
  if iline in d:
   outarr.append('_'+line) # '_' is not in any line
  else:
   outarr.append(line)
 write_lines(fileout,outarr)
 
#-----------------------------------------------------
if __name__=="__main__":
 opt = sys.argv[1]
 filein = sys.argv[2]
 fileout = sys.argv[3]
 fileout1 = sys.argv[4]
 lines = read_lines(filein)
 #check_bd(lines)
 groups = init_groups(lines)

 print(f'{len(groups)} entries from {filein}')
 if opt == '1':
  outrecs = get_outrecs_1(groups)
 elif opt == '2':
  outrecs = get_outrecs_2(groups)
 else:
  print(f'unknown option="{opt}"')
  exit(1)
 write_outrecs(fileout,outrecs)
 # write_L_comps('temp_L_comp.txt',lines)  # debugging done
 if (opt == '2') and True:
  temp_prep_ap_0c(fileout1,lines,groups)
