#-*- coding:utf-8 -*-
""" tooltip_sort.py

"""
import sys,re,codecs
import sys
sys.path.append('../')
from sort_iast import sort_iast_key

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)


if __name__=="__main__":
 filein = sys.argv[1] #  lsextract_X.txt
 fileout = sys.argv[2] # lsextract_X.txt sorted by tip abbrev
 lines = read_lines(filein)
 outarr = sorted(lines, key = sort_iast_key)
 write_lines(fileout,outarr)
 
