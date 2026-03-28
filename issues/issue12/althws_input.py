"""
 althws_input.py  
 extract fields from issue9/prep1_2.txt

"""
import re,sys
import codecs

fieldsep = ':'  

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

def extract_fields(line):
 parts = line.split(fieldsep)
 fields = (parts[2], # L
           parts[3], # k1
           parts[5], # althws_str
           )
 outline = fieldsep.join(fields)
 return outline
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1] # ../issue9/prep1_2.txt
 fileout= sys.argv[2]  
 lines = read_lines(filein)
 outarr = []
 for line in lines:
  newline = extract_fields(line)
  outarr.append(newline)
 write_lines(fileout,outarr)
 
 
