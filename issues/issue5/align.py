# coding=utf-8
""" align.py
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

if __name__=="__main__":
 filein1 = sys.argv[1] # 
 filein2 = sys.argv[2] # new.txt
 fileout = sys.argv[3] # changes.txt
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
