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
 import string
 # lowercase = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
 # uppercase = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 all_letters = string.ascii_letters # 
 latin = 'ñĀāĪīŚśŪūḌḍḥṃṅṇṚṛṢṣṬṭ'
 ascii = f'{all_letters}'
 both = latin + ascii
 
 dreg = {
  '1':r'\.{@{#[^-].*?#}@}',
  '2':r'\.{@{#[-].*?#}@}',
  #  '3':r'\.{@{#.*?#}@}',  # all 
  '3':r'\.{@{#[^#]*#}@}',  
  # issue8a
   '4':r'{@{#.*?#}@}', # bold-deva txt with or without preceding 
   '5':r'{@[^@]*?@} \({@[^@]*?@}',
  # issue8b
   '6':r'━{@[^@]*?@}', # U+2501 Box Drawings Heavy Horizontal
   #'7':r'━{%<ab>Caus.</ab>%}',
   '7':r'━{%.*?%}',
   '8': r'━.....',
   '9': r'[∙][²³]([^ ]*)',
   '10': r'<ls.*?</ls>',
   '11': r'<lang.*?</lang>',
   '12': r'<ab.*?</ab>',
   '13': r'<is.*?</is>',
   '14': r'−', # U+2212 Minus Sign
   #'15': r'{#[^# ]*#}',  Too many diffs, due to line-breaks, 
   '15': r'^.*?¦',
   '16': r'‘.*?’',
   #'17': f'{both}*{latin}{both}*',
   '17': f'[{both}]*[{latin}][{both}]*',
   '18': f'[{ascii}]+',
  }
 regex = dreg[opt]
 #print(f'regex={regex}')
 L = None
 groups = []
 group = None
 n = 0
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
   #if n < 10:print(f'{dbrec}')
   n = n + 1
 return groups

def check_groups(groups1,groups2):
 assert len(groups1) == len(groups2)
 for igroup,group1 in enumerate(groups1):
  group2 = groups2[igroup]
  assert group1.L == group2.L
 print('check_groups1 succeeds')

def db_equal(db1,db2,equal_opt):
 if (db1 == None) or (db2 == None):
  return False
 if equal_opt == '1':
  return db1 == db2
 if equal_opt == '2':
  db1a = db1.replace(' ▪ ',' ')
  db2a = db2.replace(' ▪ ',' ')
  db1b =  db1a.replace(' ▪','')
  db2b =  db2a.replace(' ▪','')
  return db1b == db2b
 print(f'db_equal ERROR. equal_opt={equal_opt}')
 exit(1)
 
def compare_groups(groups1,groups2,equal_opt):
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
   #if db1 != db2:
   if not db_equal(db1,db2,equal_opt):
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
 fileout1 = sys.argv[5]
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 groups1 = init_db(lines1,opt)
 print(f'{len(groups1)} entries from {filein1}')
 groups2 = init_db(lines2,opt)
 print(f'{len(groups2)} entries from {filein2}')
 check_groups(groups1,groups2)
 if opt in ['16']:
  equal_opt = '2' # remove ▪
 else:
  equal_opt = '1' # strict
  
 probrecs,diffrecs = compare_groups(groups1,groups2,equal_opt)
 write_recs(fileout,probrecs)
 if True:
  # add _ at beginning of certain lines
  marklines1 = mark_lines(diffrecs,lines1)
  #write_lines('temp_db_comp_ap.txt',marklines1)
  write_lines(fileout1,marklines1)
