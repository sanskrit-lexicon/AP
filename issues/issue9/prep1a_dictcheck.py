"""
 prep1s_dictcheck.py

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

def dict_hws(filein):
 lines = read_lines(filein)
 d = {}
 n = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   m = re.search(r'<k1>(.*?)<k2>',line)
   k1 = m.group(1)
   if k1 not in d:
    d[k1] = line
    n = n + 1
 print(f'{n} distinct headwords from {filein}')
 return d

def get_status_ap90(k1,ap90_d):
 if k1 in ap90_d:
  return 'yes'
 k1a=re.sub('m$','M',k1)
 if k1a in ap90_d:
  return 'yes'
 
 return 'no'
 
def get_status_mw(k1,mw_d):
 if k1 in mw_d:
  return 'yes'
 if k1.endswith('H') and  (k1[0:-1] in mw_d):
  return 'yes'
 if k1.endswith('m') and  (k1[0:-1] in mw_d):
  return 'yes'
 return 'no'

def check_dict(lines,ap90_d,mw_d):
 n1 = 0  # found ap90
 n2 = 0  # not found ap90
 m1 = 0  # found mw
 m2 = 0  # not found mw
 n = 0  # total 'C' records
 N1 = 0  # total matched by either ap90 or mw
 N2 = 0  # total not matched by either ap90 or mw
 outarr = []
 for line in lines:
  parts = line.split('\t')
  if parts[0] == 'P':
   outarr.append(line)
   continue
  [code,L,Lnew,k1,k2] = parts   # k2 is the 'new' alternate headword
  assert code == 'C'
  n = n + 1
  in_ap90 = get_status_ap90(k2,ap90_d)
  in_mw = get_status_mw(k2,mw_d)
  #if k1 == 'ikzvAlikaH':
  # print(f'check mw: {k1} -> {in_mw}')
  lastpart = f'ap90={in_ap90},mw={in_mw}' 
  parts.append(lastpart)
  out = '\t'.join(parts)
  outarr.append(out)
  # update totals
  if in_ap90 == 'yes':
   n1 = n1 + 1
  else:
   n2 = n2 + 1
  if in_mw == 'yes':
   m1 = m1 + 1
  else:
   m2 = m2 + 1
  if (in_ap90 == 'yes') or (in_mw == 'yes'):
   N1 = N1 + 1
  else:
   N2 = N2 + 1
 print(f'{n1} found in ap90, {n2} not found (out of {n})')
 print(f'{m1} found in mw  , {m2} not found (out of {n})')
 print(f'{N1} found in ap90 or mw, {N2} not found')
 return outarr

if __name__=="__main__":
 filein = sys.argv[1]
 fileap90 = sys.argv[2]  # dictionary
 filemw = sys.argv[3]
 fileout = sys.argv[4]
 lines = read_lines(filein)
 ap90_d = dict_hws(fileap90)
 mw_d = dict_hws(filemw)
 outarr = check_dict(lines,ap90_d,mw_d)
 write_lines(fileout,outarr)
