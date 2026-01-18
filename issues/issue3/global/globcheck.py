# coding=utf-8
""" globcheckg.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def write_recs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)
 
class Check:
 def __init__(self,old,new):
  self.old = old
  self.new = new
  self.instances = []
  self.count = 0 

def init_checks(filein):
 lines = read_lines(filein)
 regex = r'"(.*?)" +-> +"(.*?)"'
 checks = []
 for line in lines:
  # "#sba" -> "#sva"
  m = re.search(regex,line)
  if m == None:
   continue
  old = m.group(1)
  new = m.group(2)
  check = Check(old,new)
  checks.append(check)
 print(f'{len(checks)} changes from {filein}')
 return checks
def write_checks(fileout,checks):
 outarr = []
 for i,check in enumerate(checks):
  check.count = len(check.instances)
  a = (check.old,check.new,str(check.count))
  out = '\t'.join(a)
  outarr.append(out)
 write_lines(fileout,outarr)
 
def update_checks(checks,lines):
 regex = re.compile(r'{#.*?#}')
 for iline,line in enumerate(lines):
  sans = re.findall(regex,line)
  if sans == []:
   continue
  for san in sans:
   for check in checks:
    if check.old in san:
     check.instances.append(san)
     
if __name__ == "__main__":
 filein1 = sys.argv[1]  # ap_global_san.txt
 filein = sys.argv[2]  # xxx.txt
 fileout = sys.argv[3]  #
 checks = init_checks(filein1)
 lines = read_lines(filein)
 update_checks(checks,lines)
 write_checks(fileout,checks)
 
