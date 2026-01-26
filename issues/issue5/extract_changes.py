# coding=utf-8
""" extract_changes.py
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
  assert len(lines) == 5
  self.metaline = lines[0]
  self.oldline = lines[1]
  self.semiline = lines[2]  # comment 
  self.newline = lines[3]
  self.endline = lines[4]

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
 groupsize = 5
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

def make_outarr(table_recs):
 outarr = []
 for rec in table_recs:
  ls = rec.ls
  changes = rec.changes
  if len(changes) != 1:
   print(f'SKIPPING ls={ls}, # change recs = {len(changes)}')
   continue
  change = changes[0] # the lone change
  outarr.append(change.metaline)
  outarr.append(change.oldline)
  outarr.append(f'; {ls}')
  outarr.append(change.newline)
  outarr.append(change.endline)
 return outarr

if __name__=="__main__":
 filein_change = sys.argv[1] #  change_v3_v3a.txt
 filein_table = sys.argv[2] # AB_table.txt
 fileout = sys.argv[3] # change
 change_lines = read_lines(filein_change)
 table_lines = read_lines(filein_table)
 table_recs0 = init_table(table_lines)
 ndup,table_recs = remove_table_duplicates(table_recs0)
 print(f'{ndup} duplicates in {filein_table} ({len(table_recs)} in table)')
 # from this, there are NO DUPLICATES in table
 # parse change file into table
 change_recs = init_changes(change_lines)
 update_table(table_recs,change_recs)
 outarr =  make_outarr(table_recs)
 write_lines(fileout,outarr)
 
