#-*- coding:utf-8 -*-
""" read_gitlog.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

class GITLOG:
 def __init__(self,commit):
  self.commit = commit
  self.auth = None
  self.date = None
  self.datex = None
  self.comments = []
  
def init_gitlog_main(lines):
 rec = None
 for iline,line in enumerate(lines):
  m = re.search(r'^commit (.*)$',line)
  if m != None:
   commit = m.group(1)
   rec = GITLOG(commit)
   yield rec
   continue
  m = re.search(r'^Author: (.*)$',line)
  if m != None:
   rec.auth = m.group(1)
   continue
  m = re.search(r'^Date: +(.*) -([0-9]+)$',line)
  if m != None:
   rec.date = m.group(1)
   rec.datex = m.group(2)
   continue
  # otherwise line is part of comment
  rec.comments.append(line)
  
def init_gitlog(filein):
 lines = read_lines(filein)
 ans = list(init_gitlog_main(lines))
 print(len(ans),"records read from",filein)
 return ans

if __name__=="__main__": 
 filein = sys.argv[1] #  a file in format of git log
 #fileout = sys.argv[2] # output summary
 logrecs = init_gitlog(filein)
 
