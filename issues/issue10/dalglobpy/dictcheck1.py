"""
 dictcheck1.py

"""
import re,sys
import codecs
import sqlite3
from hwnorm1c import normalize_key

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

def init_dalglob():
 sqlitefile = 'c:/xampp/htdocs/cologne/hwnorm2/keydoc/keydoc_glob1.sqlite'
 conn = sqlite3.connect(sqlitefile) # open connection
 cursor = conn.cursor()  # prepare cursor for further use
 tabname = 'keydoc_glob1';
 parms = {'sqlitefile':sqlitefile,
          'conn':conn,
          'cursor':conn.cursor(),
          'tabname':tabname}
 return parms

def get_dalglob(dalglob,key,normkey):
 dbg = False
 # remove avagraha (slp1 = "'")
 normkey = normkey.replace("'","")
 tabname = dalglob['tabname']
 query = f"SELECT * from {tabname} WHERE key='{normkey}'"
 if dbg: print('dbg: query=',query)
 conn = dalglob['conn']
 cursor = conn.cursor()
 try:
  cursor.execute(query)
 except:
  print(f'ERROR; key={key}, normkey={normkey}')
  print(f'query=|{query}')
  exit(1)
 rows = cursor.fetchall()
 nrows = len(rows)
 assert nrows in [0,1]
 if dbg: print('dbg: rows=',rows)
 if nrows == 0:
  return False
 # row = ('agni', 'acc:ap=agniH:ap90=agniH:armh:ben:bhs:bop:bur:cae:ccs:gra:gst:ieg')
 row = rows[0]
 normkey1, dictstr = row
 assert normkey == normkey1
 fields = dictstr.split(':')
 if dbg: print('dbg: fields=',fields)
 dictsok = []
 for field in fields:
  parts = field.split('=')
  dcode = parts[0]
  if dcode in ('ap','ap90'):
   # skip
   continue
  else:
   dictsok.append(dcode)
 if len(dictsok) == 0:
  return False
 else:
  return True

regsubs = [
 ('UH$', 'U'),
 ('AH$', 'A'),
 ('IH$', 'I'),
 ('ss', 'Hs'),
 ('SS', 'HS'),
 ('zz', 'Hz'),
 ('Hk', 'sk'),
 ('HK', 'sK'),
 ('Hp', 'sp'),
 ('HP', 'sP'),
 ]
def normalize_key_alternates(normkey):
 ans = []
 for regex,sub in regsubs:
  x = re.sub(regex,sub,normkey)
  if x != normkey:
   ans.append(x)
 return ans
def check_dict(lines,dalglob):
 outarr = [] # returned
 fieldsep = ':'
 for line in lines:
  (L,k1,db,k1cpds_str) = line.split(fieldsep)
  k1cpds = k1cpds_str.split(',')
  a = []
  for key in k1cpds:
   normkey = normalize_key(key)
   found = get_dalglob(dalglob,key,normkey)
   # try some variants
   if not found:
    alternates = normalize_key_alternates(normkey)
    for normkey1 in alternates:
     found1 = get_dalglob(dalglob,key,normkey1)
     if found1:
      found = True
      break
   if found:
    a.append(key)
   else:
    a.append(key+'?')
  newfield = ','.join(a)
  outfields = (L,k1,db,newfield)
  out = fieldsep.join(outfields)
  outarr.append(out)
 return outarr

def count_missing(lines):
 no = 0
 fieldsep = ':'
 for line in lines:
  (L,k1,db,k1cpds_str) = line.split(fieldsep)
  k1cpds = k1cpds_str.split(',')
  for key in k1cpds:
   if key.endswith('?'):
    no = no + 1
 print(f'{no} keys not found')

if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 dalglob = init_dalglob()
 #test(dalglob)
 outarr = check_dict(lines,dalglob)
 conn = dalglob['conn']
 conn.close()
 write_lines(fileout,outarr)
 count_missing(outarr)
