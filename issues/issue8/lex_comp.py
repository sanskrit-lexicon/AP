"""
 lex_comp.py

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
  self.lexes = []  # records is (iline,lex)
  
def init_lex(lines,opt):
 L = None
 groups = []
 group = None
 regexes = {1:'<lex>(.*?)</lex>',
            2:'〔(.*?)〕'
            }
 regex = regexes[opt]
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
   lex = m.group(1)
   lexrec = (iline,lex)
   group.lexes.append(lexrec)
 return groups

def check_groups(groups1,groups2):
 assert len(groups1) == len(groups2)
 for igroup,group1 in enumerate(groups1):
  group2 = groups2[igroup]
  assert group1.L == group2.L
 print('check_groups1 succeeds')

def compare_groups(groups1,groups2):
 outrecs = []
 for igroup,group1 in enumerate(groups1):
  group2 = groups2[igroup]
  L = group2.L
  lexes1 = group1.lexes
  lexes2 = group2.lexes
  n1 = len(lexes1)
  n2 = len(lexes2)
  n = max(n1,n2)
  for i in range(n):
   if (i < n1) and (i < n2):
    iline1,lex1 = lexes1[i]
    iline2,lex2 = lexes2[i]
    lnum1 = iline1 + 1
    lnum2 = iline2 + 1
   elif i < n1:
    iline1,lex1 = lexes1[i]
    iline2,lex2 = (None,None)
    lnum1 = iline1 + 1
    lnum2 = None
   elif i < n2:
    iline2,lex2 = lexes2[i]
    iline1,lex1 = (None,None)
    lnum1 = None
    lnum2 = iline2 + 1
   if lex1 != lex2:
    arr = []
    arr.append(f'* Case L={L}')
    arr.append(f'lex1 = {lex1}, lnum1={lnum1}')
    arr.append(f'lex2 = {lex2}, lnum2={lnum2}')
    arr.append(f'--------------------')
    outrecs.append(arr)
    break
 print(f'compare_groups finds {len(outrecs)} problem entries')
 return outrecs

def old_compare_groups(groups1,groups2):
 for igroup,group1 in enumerate(groups1):
  group2 = groups2[igroup]
  L = group2.L
  lexes1 = group1.lexes
  lexes2 = group2.lexes
  n1 = len(lexes1)
  n2 = len(lexes2)
  for i1 in range(n1):
   iline1,lex1 = lexes1[i1]
   if i1 < n2:
    iline2,lex2 = lexes2[i1]
    if lex1 != lex2:
     print(f'First mismatch. igroup={igroup}, L={L}, i1={i1}')
     print(f'lex1 = {lex1}, lex2 = {lex2}')
     print(f'iline1 = {iline1},  iline2 = {iline2}')
     exit(1)
   else:
     print(f'First mismatch. igroup={igroup}, L={L}, i1={i1}')
     print(f'lex1 = {lex1}, lex2 = {None}')
     exit(1)
 print(f'compare_groups succeeds! lexes same in both inputs')

 #-----------------------------------------------------
if __name__=="__main__":
 filein1 = sys.argv[1]
 filein2 = sys.argv[2]
 fileout = sys.argv[3]
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 
 groups1 = init_lex(lines1,1)  # cdsl form 
 print(f'{len(groups1)} entries from {filein1}')
 groups2 = init_lex(lines2,2)  # ab form
 print(f'{len(groups2)} entries from {filein2}')
 check_groups(groups1,groups2)
 outrecs = compare_groups(groups1,groups2)
 write_recs(fileout,outrecs)
  
