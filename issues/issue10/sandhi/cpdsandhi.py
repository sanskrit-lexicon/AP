"""
 cpdsandhi.py
"""
from scharfsandhi import ScharfSandhi

def cpdsandhi(s):
 # example: pUrva-antya
 #s = purva + para
 sandhi = ScharfSandhi()
 sandhi.history=[] # init history.  It is modified by wrapper
 sandhi.dbg=False
 #err = sandhi.sandhioptions(ec, "N", "S", despace)
 ec = 'C' # compound sandhi
 vedic = "N"
 closeSandhi = "S" # ? 
 despace = 'Y' # relevant for compound sandhi?
 err = sandhi.sandhioptions(ec,vedic,closeSandhi, despace)
 if err != 0:
  print("cpdsandhi ERROR in options" )
  exit(1)
 ans = sandhi.sandhi(s)
 return ans

if __name__ == '__main__':
 import sys
 ec = sys.argv[1]
 despace = sys.argv[2]
 s = sys.argv[3]
 sandhi = ScharfSandhi()
 sandhi.history=[] # init history.  It is modified by wrapper
 sandhi.dbg=True
 err = sandhi.sandhioptions(ec, "N", "S", despace)
 if err != 0:
  print("ERROR: options must be E or C, Y or N, not:", ec, despace)
  exit(1)
 ans = sandhi.sandhi(s)
 for h in sandhi.history:
  print(h)
 print('ScharfSandhiArg: ans="%s"' % ans)
