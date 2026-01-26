# coding=utf-8
""" extract_deva.py
"""
from __future__ import print_function
import sys, re,codecs
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir('transcoder')

def convert(ls_slp1):
 m = re.search(r'<ls>(.*)</ls>',ls_slp1)
 lsbody = m.group(1)
 # change from {#X#} to <s>X</s>
 lsbody = lsbody.replace('{#','<s>')
 lsbody = lsbody.replace('#}','</s>')
 tranin = 'slp1'
 tranout = 'deva'
 tagname = 's'
 lsbody_deva = transcoder.transcoder_processElements(lsbody,tranin,tranout,tagname)
 ans = f'<ls>{lsbody_deva}</ls>'
 return ans

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
  assert len(lines) == 6
  self.metaline = lines[0]
  self.oldline = lines[1]
  self.slp1 = lines[2]  # comment  deva in {#X#} form
  self.newline = lines[3]
  self.iast = lines[4]  # the ls in iast form. used to match ap.txt
  self.endline = lines[5]
  # from matching with ap.txt
  self.ap_lnums = [] # the lnums that match lsiast
  self.ap_metalines = []  # parallel with ap_lnums
  m = re.search(r'(<ls>.*?</ls>)',self.iast)
  self.ls_iast = m.group(1)
  self.ls_deva = convert(self.slp1)
  
def update_change(change_recs):
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
    change.ap_lnums.append(lnum)
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
 groupsize = 6
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
  lnums = rec.ap_lnums
  outarr.append(rec.metaline)
  outarr.append(rec.oldline)
  outarr.append(rec.slp1)
  outarr.append(rec.newline)
  outarr.append(rec.iast)
  outarr.append(f'; {rec.ls_deva}')
  #outarr.append(f'; lnums = {lnums}')
  outarr.append(rec.endline)
 return outarr

if __name__=="__main__":
 filein_change = sys.argv[1] #  extract_change_1.txt
 fileout = sys.argv[2] # change
 change_lines = read_lines(filein_change)

 change_recs = init_changes(change_lines)
 #update_change(change_recs)
 outarr =  make_outarr(change_recs)
 write_lines(fileout,outarr)
 
