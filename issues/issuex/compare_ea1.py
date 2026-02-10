""" compare_ea1.py 
Compare two extended ascii files
"""

import re,sys
import codecs, unicodedata


def make_combining_chars():
 chars = [
  r'\u0300', # combining grave accent
  r'\u0301', # combining acute accent
  r'\u0302', # combining circumflex accent
  r'\u0303', # combining tilde
  r'\u0304', # combining macron
 ]
 ans = []
 for x in chars:
  # ref: //stackoverflow.com/questions/2828284/conversion-of-strings-like-uxxxx-in-python
  # y = x.decode('unicode-escape')
  # AttributeError: 'str' object has no attribute 'decode'
  y = bytes(x,"ascii").decode('unicode-escape')
  ans.append(y)
 if False:
  for key in ans:
   ords = [r"\u%04x" % ord(c) for c in key]
   ordstr = '.'.join(ords)
   names = [unicodedata.name(c) for c in key]
   namestr = ' + '.join(names)
   out = "%s  (%s)  := %s" %(key,ordstr,namestr)
   print(out.encode('utf-8'))
  exit(0)
 return ans

combining_chars = make_combining_chars() # a list 




def update_asdict(line,asdict):
 if line == '':
  return
 parts = []
 prev = None
 for ic,c in enumerate(line):
  if ic == 0:
   prev = c
  elif c in combining_chars:
   prev = prev + c
  else:
   # not a combining character and not the first character
   parts.append(prev)
   prev = c
  if ord(c) == 8206: # \u200e left-to-right mark:
   print('left-to-right-mark at character position',ic+1,'in line\n' ,line)
   print(len(line))
   atemp =[]
   for jc in range(ic-5,ic+5):
    xc = line[jc]
    if jc == ic:
     atemp.append('**'+xc+'**')
    else:
     atemp.append(xc)
   atempx = ' '.join(atemp)
   print(atempx)
   print()
 parts.append(prev)
 #print 'line=',line.encode('utf-8')
 for ic,c in enumerate(parts):
  #print ic,c
  if (len(c) == 1) and (ord(c) <= 127):
   # skip ascii character character
   continue
  if c not in asdict:
   asdict[c] = 0
  asdict[c] = asdict[c] + 1
 #exit(0)

def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   lines.append(line.strip())
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

def check_ea(filein,fileout):
# set up regex callback 'repl' with access to dictionary asdict
 asdict = {}
 # read the lines of the file
 f = codecs.open(filein,encoding='utf-8',mode='r')
 n = 0
 for line in f:
  line = line.rstrip()
  n = n + 1
  update_asdict(line,asdict)
  
 f.close()
 keys = asdict.keys()
 print(n,"lines in",filein)
 print(len(keys),"extended ascii codes found in",filein)

 keys = sorted(keys)
 print( len(keys))
 outlines = []
 for key in keys:
  asobj = asdict[key]
  #key1=convert(key)
  # key is a string
  # ords = ["\u%04x" % ord(c) for c in key]
  ords = []
  for c in key:
   try:
    uval = r"\u%04x" % ord(c)
   except:
    print('WARNING: Cannot convert: c=%s, ord(c)=%s' % (c,ord(c)))
    uval = "???"
   ords.append(uval)
  ordstr = ''.join(ords)
  names = [unicodedata.name(c) for c in key]
  namestr = ' + '.join(names)
  #out = "%s  (\\u%04x) %5d := %s" %(key,ord(key),asobj,namestr)
  out = "%s  (%s) %5d := %s" %(key,ordstr,asobj,namestr)
  outlines.append(out)
 fout = codecs.open(fileout,'w','utf-8')
 for out in outlines:
  fout.write("%s\n" % out)
 fout.close()

def parse_lines(lines):
 d = {}
 for line in lines:
  linea,namestr = line.split(' := ')
  c,ucode,countstr = re.split(r' +',linea)
  count = int(countstr)
  d[c] = (ucode,count,namestr)
 return d

def merge_asdict(d1,d2):
 d = {}
 for c in d1:
  ucode,count1,namestr = d1[c]
  counts = [count1,0]
  d[c] = (ucode,namestr,counts)
 for c in d2:
  ucode2,count2,namestr2 = d2[c]
  if c in d:
   ucode1,namestr1,counts1 = d[c]
   assert ucode1 == ucode2
   assert namestr1 == namestr2
   assert counts1[1] == 0
   count1 = counts1[0]
   counts2 = [count1,count2]
   d[c] = (ucode1,namestr2,counts2)
  else: # c not in d:
   counts2 = [0,count2]
   d[c] = (ucode2,namestr2,counts2)
 return d

def make_outlines(d,parm):
 keys = d.keys()
 keys = sorted(keys)
 name1,name2 = parm.split(',')
 outarr = []
 titlevals = ['char'.ljust(5),
              'ucode'.ljust(8),
              name1.rjust(5),
              name2.rjust(5),
              'diff'.rjust(5),
              '  uname']
 title = ' : '.join(titlevals)
 outarr.append(title)
 for c in keys:
  (ucode,namestr,counts) = d[c]
  n1,n2 = counts
  ndiff = n2 - n1
  values = [c.ljust(5),
            ucode.ljust(8),
            str(n1).rjust(5),
            str(n2).rjust(5),
            str(ndiff).rjust(5),'  '+namestr]
  out = ' : '.join(values)
  outarr.append(out)
 return outarr
#-----------------------------------------------------
if __name__=="__main__":
 param = sys.argv[1]
 filein1 = sys.argv[2]
 filein2 = sys.argv[3]
 fileout = sys.argv[4]
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 asdict1 = parse_lines(lines1)
 asdict2 = parse_lines(lines2)
 asdict = merge_asdict(asdict1,asdict2)
 outlines = make_outlines(asdict,param)
 write_lines(fileout,outlines)
