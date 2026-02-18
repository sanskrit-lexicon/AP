""" v4a_0.py
  replace some unicode characters

"""
import re,sys
import codecs
def read_lines(filein):
 lines = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   lines.append(line.strip())
 print(f'{len(lines)} read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,'w','utf-8') as f:
  for out in outarr:
   f.write("%s\n" % out)
 print(f'{len(outarr)} lines written to {fileout}')

replacements__0 = [
 # 🞄 U+1f784 BLACK SLIGHTLY SMALL CIRCLE ->
 # "▪" (U+25AA) (BLACK SMALL SQUARE) 
 ('\U0001f784', '\u25aa'),
 # 🠚  U+1f81a HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD ->
 # → u+2192 RIGHTWARDS ARROW
 ('\U0001f81a', '\u2192'),  
 ]
replacements__1 = [
 # '∙'  U+2219  BULLET OPERATOR 
 # .² --> ∙² ;;used for meaning numbers in AP57 and WIL; used for line break(?) in pwkvn_hk version
 ('.²' ,  '∙²'),
 ('.³' ,  '∙³'),  # used only in AP57
 ]
replacements = replacements__0 + replacements__1

for old,new in replacements:
 print(f'old={old}, new={new}')

def make_newlines(lines):
 newlines = []
 for line in lines:
  newline = line
  for old,new in replacements:
   newline = newline.replace(old,new)
  newlines.append(newline)
 return newlines
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 lines = read_lines(filein)
 newlines = make_newlines(lines)
 write_lines(fileout,newlines)
