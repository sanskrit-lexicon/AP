#-*- coding:utf-8 -*-
""" check_L_unique.py
    Usage: python check_L_unique.py <path-to-{dict}.txt>
       Checks NUMERIC uniqueness of all L-values .
"""
import sys,re,codecs

def check_L(lines):
 metaline = None
 d = {}
 dups = []
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   m = re.search(r'^<L>(.*?)<',line)
   L0 = m.group(1)
   L = float(L0)
   if L not in d:
    d[L] = iline
   else:
    # duplicate
    ilineold = d[L]
    dup = (L0,L,ilineold,iline)
    dups.append(dup)
 if dups == []:
  print('ok')
  return
 for dup in dups:
  (L0,L,ilineold,iline) = dup
  print(f'line {iline} same (float) L {L} as at line {ilineold}. L0={L0}')

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 
 check_L(lines)
 
