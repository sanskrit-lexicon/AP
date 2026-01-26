# coding=utf-8
""" extract_linenum.py
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

class Change:
 def __init__(self,lines):
  assert len(lines) == 7
  self.metaline = lines[0]
  self.oldline = lines[1] # line from older ap with #{x#}
  self.slp1 = lines[2]  # the ls  in {#X#} form
  self.newline = lines[3]  # line from ap with iast
  self.iast = lines[4]  # the ls in iast
  self.deva = lines[5]  # the ls in devanagari 
  self.endline = lines[6]
  # from matching with ap.txt
  self.ap_lnums = [] # the lnums that match lsiast
  self.ap_metalines = []  # parallel with ap_lnums
  self.ap_lines = [] # parallel with ap_lnums.
  m = re.search(r'(<ls>.*?</ls>)',self.iast)
  self.ls_iast = m.group(1)

def update_change(change_recs,aplines):
 n = 0
 meta = None
 for iline,line in enumerate(aplines):
  lnum = iline + 1
  if line.startswith('<L>'):
   meta = line
   continue
  for change in change_recs:
   if change.ls_iast in line:
    change.ap_lnums.append(lnum)
    change.ap_metalines.append(meta)
    change.ap_lines.append(line)
    n = n + 1
 print(f'update_change finds {n} lnums')
   
class Table:
 def __init__(self,ilinetab,line):
  self.ls = line
  self.ilinetab = ilinetab
  self.changes = []

def init_table(lines):
 recs = []
 for iline,line in enumerate(lines):
  recs.append(Table(iline,line))
 print(f'{len(recs)} table records')
 return recs
 
def remove_table_duplicates(table_recs):
 d = {}
 newrecs = []
 ndup = 0
 for rec in table_recs:
  ls = rec.ls
  if ls in d:
   rec.count = rec.count + 1
  else:
   d[ls] = rec
   newrecs.append(rec)
 return ndup,newrecs
 
def init_changes(lines):
 groupsize = 7
 groupsize1 = groupsize - 1
 groups = []
 group = []
 for i,line in enumerate(lines):
  group.append(line)
  if (i % groupsize) == groupsize1:
   changerec = Change(group)
   groups.append(changerec)
   group = []
 print(f'{len(groups)} groups')
 return groups

def update_table(table_recs,change_recs):
 # assume no duplicates in table_recs
 for table_rec in table_recs:
  ls = table_rec.ls
  lschanges = []
  for change_rec in change_recs:
   oldline = change_rec.oldline
   if ls in oldline:
    lschanges.append(change_rec)
  table_rec.changes = lschanges

def make_outarr(change_recs):
 outarr = []
 for rec in change_recs:
  ap_lnums = rec.ap_lnums
  ap_metalines = rec.ap_metalines
  ap_lines = rec.ap_lines
  
  outarr.append(';x ' + rec.metaline)
  outarr.append(';x ' + rec.oldline)
  outarr.append(';x ' + rec.slp1)
  outarr.append(';x ' + rec.newline)
  outarr.append(';x ' + rec.iast)
  #print(rec.slp1)
  #print(rec.iast)
  # outarr.append(f'; ap_lnums = {ap_lnums}')
  if ap_lnums == []:
   print(f'no lnums for {rec.metaline}')
   continue
  # make a new change record
  # one case has two ap_lnums
  for i,ap_lnum in enumerate(ap_lnums):
   ap_metaline = ap_metalines[i]
   ap_line = ap_lines[i]
   tempold = f'{ap_lnum} old {ap_line}'
   ls_iast = rec.iast[2:] # remove '; '
   ls_deva = rec.deva[2:] # remove '; '
   tempnew = ap_line.replace(ls_iast, ls_deva)
   outarr.append(f'; {ap_metaline}')
   outarr.append(f'{ap_lnum} old {ap_line}')
   outarr.append(f'{ap_lnum} new {tempnew}')
  outarr.append(rec.endline)
    
 return outarr

if __name__=="__main__":
 filein_ap = sys.argv[1]  # ap.txt
 filein_change = sys.argv[2] #  extract_change_1.txt
 fileout = sys.argv[3] # change
 aplines = read_lines(filein_ap)
 change_lines = read_lines(filein_change)

 change_recs = init_changes(change_lines)
 update_change(change_recs,aplines)
 outarr =  make_outarr(change_recs)
 write_lines(fileout,outarr)
 
