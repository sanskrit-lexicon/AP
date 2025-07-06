#-*- coding:utf-8 -*-
""" extract_commits.py
"""
import sys,re,codecs
import read_gitlog
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
 #print(len(ans),"records read from",filein)
 return ans

def make_cmd(idx,rec):
 commit = rec.commit[0:8]
 cmd = 'git show %s:ap/ap.txt > ../commits/ap_%02d.txt' %(commit,idx+1)
 return cmd
if __name__=="__main__": 
 filein = sys.argv[1] #  a file in format of git log
 fileout = sys.argv[2] # script to extract versions of ap.txt at comments
 logrecs = init_gitlog(filein)
 logrecs.reverse() # reverse ordering
 cmds = [] # list of bash commands
 cmds.append('cd orig_pdap_copy')
 for i,logrec in enumerate(logrecs):
  i1 = i+1
  cmds.append('echo ap_%02d.txt' % i1)
  cmds.append(make_cmd(i,logrec))
 # write the script
 write_lines(fileout,cmds)
 
