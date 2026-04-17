#-*- coding:utf-8 -*-
""" compare_tooltips.py 

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
 #print(title)
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
 #print(outarr[1])
 return d,outarr

def compare_tooltips(d1,lines1,d2,lines2):
 outarr = []
 icase = 0
 for abbrev in d1:
  iline1 = d1[abbrev]
  line1 = lines1[iline1]
  iline2 = d2[abbrev]
  line2 = lines2[iline2]
  parts1 = line1.split('\t')
  assert parts1[0] == abbrev
  tip1 = parts1[1]
  parts2 = line2.split('\t')
  assert parts2[0] == abbrev
  tip2 = parts2[1]
  if tip1 == tip2:
   continue
  icase = icase + 1
  out = f'** ----- Case {icase}: {abbrev}'
  outarr.append(out)
  out = f'AB:   {line1}'
  outarr.append(out)
  out = f'cdsl: {line2}'
  outarr.append(out)
  out = f' TIP: {tip1}'  # final form, usu. AB's form
  outarr.append(out)
 print(f'{icase} differences')
 return outarr
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
 assert sorted(d1.keys()) == sorted(d2.keys())
 outarr = compare_tooltips(d1,lines1,d2,lines2)
 write_lines(fileout,outarr)
