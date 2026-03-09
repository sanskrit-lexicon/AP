"""
 prep_sort.py

"""
import re,sys
import codecs

fieldsep = ':'  # agrees with prep1.py
def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   #lines.append(line.strip()) # changed at ap_1
   lines.append(line.rstrip('\r\n'))
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

def write_recs(fileout,outrecs):
 with codecs.open(fileout,'w','utf-8') as f:
  for outarr in outrecs:
   for out in outarr:
    f.write("%s\n" % out)
 print(f'{len(outrecs)} records written to {fileout}')

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,'w','utf-8') as f:
  for outarr in outrecs:
   for out in outarr:
    f.write("%s\n" % out)
 print(f'{len(outrecs)} records written to {fileout}')
 
class Rec:
 def __init__(self,line):
  self.line = line
  #parts = line.split(f'{fieldsep}')
  parts = line.split(fieldsep)
  (self.status,self.ng,self.L,self.k1,self.header,self.k1alts) = parts
 def toString(self):
  parts = (self.status,self.ng,self.L,self.k1,self.header,self.k1alts)
  newline = fieldsep.join(parts)
  return newline
 
def init_recs(lines):
 recs = [Rec(line) for line in lines]
 return recs

def write_recs(fileout,recs):
 outarr = []
 for rec in recs:
  out = rec.toString()
  outarr.append(out)
 write_lines(fileout,outarr)

def sort_stat(recs):
 outrecs = sorted(recs,key=lambda rec: rec.status)
 return outrecs
def sort_L(recs):
 outrecs = sorted(recs,key=lambda rec: float(rec.L))
 return outrecs
if __name__=="__main__":
 opt = sys.argv[1]
 filein = sys.argv[2]
 fileout = sys.argv[3]
 lines = read_lines(filein)
 recs = init_recs(lines)
 if opt == 'stat':
  outrecs = sort_stat(recs)
 elif opt == 'L':
  outrecs = sort_L(recs)
 else:
  print(f'unknown option "{opt}"')
  exit(1)
 write_recs(fileout,outrecs)
 exit(1)
