#-*- coding:utf-8 -*-
""" compare_abbrev.py 

"""
import sys,re,codecs
import sys

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def unique_abbrevs(d1,lines1,filein1,d2):
 outarr = ['title']
 outarr.append('=================================================')
 
 keys1 = []
 for x in d1:
  if x not in d2:
   keys1.append(x)
   iline1 = d1[x]
   line1 = lines1[iline1]
   out = line1
   outarr.append(out)
 title = f'{len(keys1)} unique in {filein1}'
 outarr[0] = title
 outarr.append('')
 print(title)
 return outarr

def get_abbrevs(lines,filename):
 d = {}
 outarr = []
 outarr.append('-----------------------------------------------')
 outarr.append('title') # outarr[1]
 ndup = 0
 for iline,line in enumerate(lines):
  abbrev,tooltip = line.split('\t')
  if abbrev in d:
   ndup = ndup + 1
   out = f'duplicate abbrev {abbrev}'
   outarr.append(out)
   print(f'duplicate abbrev {abbrev} in {filename}')
  d[abbrev] = iline
 outarr[1] = f'{ndup} duplicate abbrevs in {filename}'
 print(outarr[1])
 return d,outarr
if __name__=="__main__":
 filein1 = sys.argv[1] #
 filein2 = sys.argv[2] 
 fileout = sys.argv[3] # 
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 d1,outarr1a = get_abbrevs(lines1,filein1)
 d2,outarr2a = get_abbrevs(lines2,filein2)
 outarr1b = unique_abbrevs(d1,lines1,filein1,d2)
 outarr2b = unique_abbrevs(d2,lines2,filein2,d1)
 outarr1 = outarr1a + outarr1b
 outarr2 = outarr2a + outarr2b
 outarr = outarr1 + outarr2
 write_lines(fileout,outarr)

