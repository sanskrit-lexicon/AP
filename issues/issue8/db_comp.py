"""
 db_comp.py

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

class Entry:
 def __init__(self,iline,metaline):
  self.iline = iline
  self.meta = metaline
  m = re.search(r'^<L>(.*?)<pc>',metaline)
  self.L = m.group(1)
  self.dbs = []  # records is (iline,db)
  
def init_db(lines,opt):
 dreg = {
  '1':r'\.{@{#[^-].*?#}@}',
  '2':r'\.{@{#[-].*?#}@}',
  '3':r'\.{@{#.*?#}@}',  # all
  }
 regex = dreg[opt]
 L = None
 groups = []
 group = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   if group != None:
    groups.append(group)
   group = Entry(iline,line)
   continue
  if group == None:
   continue
  if line.startswith('<LEND>'):
   groups.append(group)   
   group = None
   continue
  for m in re.finditer(regex,line):
   db = m.group(0)
   dbrec = (iline,db)
   group.dbs.append(dbrec)
 return groups

def check_groups(groups1,groups2):
 assert len(groups1) == len(groups2)
 for igroup,group1 in enumerate(groups1):
  group2 = groups2[igroup]
  assert group1.L == group2.L
 print('check_groups1 succeeds')

def compare_groups_version0(groups1,groups2):
 for igroup,group1 in enumerate(groups1):
  group2 = groups2[igroup]
  L = group2.L
  dbs1 = group1.dbs
  dbs2 = group2.dbs
  n1 = len(dbs1)
  n2 = len(dbs2)
  for i1 in range(n1):
   iline1,db1 = dbs1[i1]
   if i1 < n2:
    iline2,db2 = dbs2[i1]
    if db1 != db2:
     print(f'First mismatch.  L={L}, i1={i1}')
     print(f'db1 = {db1}, lnum1={iline1+1}')
     print(f'db2 = {db2}, lnum2={iline2+1}')
     print(f'iline1 = {iline1},  iline2 = {iline2}')
     exit(1)
   else:
    print(f'First mismatch. L={L}, i1={i1}')
    print(f'db1 = {db1}, lnum1={iline1+1}')
    db2 = None
    print(f'db2 = {db2}')
    exit(1)
 print(f'compare_groups succeeds! dbs same in both inputs')

def compare_groups(groups1,groups2):
 outrecs = []
 nprob = 0
 diffrecs = []
 for igroup,group1 in enumerate(groups1):
  group2 = groups2[igroup]
  L = group2.L
  dbs1 = group1.dbs
  dbs2 = group2.dbs
  n1 = len(dbs1)
  n2 = len(dbs2)
  n = max(n1,n2)
  for i in range(n):
   if (i < n1) and (i < n2):
    iline1,db1 = dbs1[i]
    iline2,db2 = dbs2[i]
    lnum1 = iline1 + 1
    lnum2 = iline2 + 1
   elif i < n1:
    iline1,db1 = dbs1[i]
    iline2,db2 = (None,None)
    lnum1 = iline1 + 1
    lnum2 = None
   elif i < n2:
    iline2,db2 = dbs2[i]
    iline1,db1 = (None,None)
    lnum1 = None
    lnum2 = iline2 + 1
   if db1 != db2:
    arr = []
    arr.append(f'* Case L={L}')
    arr.append(f'db1 = {db1}, lnum1={lnum1}')
    arr.append(f'db2 = {db2}, lnum2={lnum2}')
    arr.append(f'--------------------')
    outrecs.append(arr)
    diffrec = (L,lnum1,db1,lnum2,db2)
    diffrecs.append(diffrec)
    break
 print(f'compare_groups finds {len(outrecs)} problem entries')
 #print(f'compare_groups succeeds! dbs same in both inputs')
 return outrecs,diffrecs

def mark_lines(recs,lines):
 newlines = []
 indicator = '_'
 d = {}
 n = 0
 for rec in recs:
  (L,lnum1,db1,lnum2,db2) = rec
  if lnum1 == None:
   continue
  if lnum2 == None:
   continue
  iline1 = lnum1 - 1
  d[iline1] = True
  n = n + 1
 print(f'marking {n} lines')
 for iline,line in enumerate(lines):
  if iline in d:
   newline = indicator + line
  else:
   newline = line
  newlines.append(newline)
 return newlines
#-----------------------------------------------------
if __name__=="__main__":
 opt = sys.argv[1]
 filein1 = sys.argv[2]
 filein2 = sys.argv[3]
 fileout = sys.argv[4]
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 groups1 = init_db(lines1,opt)
 print(f'{len(groups1)} entries from {filein1}')
 groups2 = init_db(lines2,opt)
 print(f'{len(groups2)} entries from {filein2}')
 check_groups(groups1,groups2)
 probrecs,diffrecs = compare_groups(groups1,groups2)
 write_recs(fileout,probrecs)
 if True:
  marklines1 = mark_lines(diffrecs,lines1)
  write_lines('temp_db_comp_ap.txt',marklines1)

              
