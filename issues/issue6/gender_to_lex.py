# coding=utf-8
""" gender_to_lex.py
"""
from __future__ import print_function
import sys, re, codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

replacements = [
 ('{%m.%}','{%<lex>m.</lex>%}'),
 ('{%f.%}','{%<lex>f.</lex>%}'),
 ('{%n.%}','{%<lex>n.</lex>%}'),
 ('{%a.%}','{%<lex>a.</lex>%}'),

 ('{%ind.%}','{%<lex>ind.</lex>%}'),
 ('{%adv.%}','{%<lex>adv.</lex>%}'),
 # two genders
 ('{%m. f.%}', '{%<lex>m.</lex> <lex>f.</lex>%}'),
 ('{%m. n.%}', '{%<lex>m.</lex> <lex>n.</lex>%}'),
 ('{%f. n.%}', '{%<lex>f.</lex> <lex>n.</lex>%}'),

 ]

def get_newlines(lines):
 newlines = []
 n = 0 # number of lines with at least one string marked
 for line in lines:
  newline = line
  for old,new in replacements:
   newline = newline.replace(old,new)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print(n,'lines changed')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # old kosha
 fileout = sys.argv[2] # revised kosha
 lines = read_lines(filein)
 newlines = get_newlines(lines)
 write_lines(fileout,newlines)
 
