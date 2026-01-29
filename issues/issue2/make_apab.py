# coding=utf-8
""" make_apab.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def edit_tooltip(tip):
 newtip = tip
 # these are specific alterations
 lb = '&#13;&#10;'
 if tip == 'Et cetera. denotes that the rest of the word under consideration is to be supplied; e. g. रत्नप्रभवस्य यस्य under अनन्त means अनन्तरत्न &c.':
  # add line-breaks in the long tooltip
  newtip = f'Et cetera. denotes that the rest of the word {lb}under consideration is to be supplied;{lb} e. g. रत्नप्रभवस्य यस्य under अनन्त means अनन्तरत्न &c.'
 return newtip

def edit_abbr(ab):
 # these are specific alterations
 newab = ab.replace('&','&amp;')
 return newab

def reformat(lines):
 newlines = []
 fieldsep = '\t'
 for iline,line in enumerate(lines):
  lnum = iline + 1
  # skip some lines that have wrong format
  parts = line.split(fieldsep)
  if len(parts) != 2:
   print(f'skipping line {lnum:04d}: {line}')
   continue
  abbr0,tooltip0 = parts
  tooltip = edit_tooltip(tooltip0)
  if tooltip0 != tooltip:
   print(f'Altered tooltip at line {lnum}')
   print(f'  old: {tooltip0}')
   print(f'  new: {tooltip}')
  abbr = edit_abbr(abbr0)
  if abbr0 != abbr:
   print(f'Altered abbreviation at line {lnum}')
   print(f'  old: {abbr0}')
   print(f'  new: {abbr}')
   
  newline = f'{abbr}{fieldsep}<id>{abbr}</id> <disp>{tooltip}</disp>'
  newlines.append(newline)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1] # 
 fileout = sys.argv[2] # changes.txt
 lines = read_lines(filein)
 newlines = reformat(lines)
 write_lines(fileout,newlines)
