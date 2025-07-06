
sanskrit-lexicon/AP/issues/issue1/readme.txt
Begin 07-06-2025

===========================================
The history of AP has been tracked in a private (secret) repository maintained
on cologne server.  In the following comments, this repo is called 'orig_ap'.
In local file system, we make a new directory (ap_open)
and put a copy of orig_ap in that directory.


mkdir ap_open
cd ap_open
cp -r /c/xampp/htdocs/cologne/orig_ap orig_ap_copy

==========================================
We save the 'git log' in a file.  There are 28 commits to the repo.
cd orig_ap_copy
git log > ../orig_ap_log.txt
cd ../
grep -E '^commit ' orig_ap_log.txt | wc -l
# 28  total number of commits

----
# we write a program to parse orig_ap_log.txt into an array of 28 objects.
cd /e/ap_open
# the commits are in reverse order by date.
# read_gitlog.py parses the log file, constructing a list of GITLOG objects
python read_gitlog.py orig_ap_log.txt

---  We will rename the versions of ap.txt at these commits
  as ap_01.txt, ..., ap_28.txt.
  ap_01.txt is the oldest, at commit date Jan 24, 2020
  ap_28.txt is the newest, at commit date Jul 16, 2024
     ap_28.txt is the one currently used in Cologne displays.

commits_dates.txt has the commit date for each version.
python commit_dates.py  orig_ap_log.txt commit_dates.txt

======================================================
We aim to transfer the history of ap.txt to csl-orig repo
Each file size is approx. 12MB  (* 12 28) = 336 mb.

We extract ap_nn.txt for each of the 28 commits
mkdir commits  # ap_nn.txt  
python extract_commits.py orig_ap_log.txt extract_commits.sh
# run the extract script
# makes commits/ap_nn.txt  nn = 01 (oldest) to 28 (newest)
sh extract_commits.sh
# check the latest one
diff commits/ap_28.txt orig_ap_copy/ap/ap.txt | wc -l
# 0  these two files are the same, as expected
--------
# confirm that commits/ap_28.txt is the 'current' ap.txt of csl-orig
# Recall: csl-orig/v02/ap/ is current version of ap.txt, and other files.
# but it has NOT been tracked by git in csl-orig.
# Locally, I have moved to csl-orig/v02/temp_ap_20250701

diff commits/ap_28.txt /c/xampp/htdocs/cologne/csl-orig/v02/temp_ap_20250701/ap.txt | wc -l
0

======================================================
# diff analysis
mkdir diffs
# compute 27 files:
  diffs/diff_01_02.txt , diffs/diff_27_28.txt
# compute temp_difflog.txt which has counts of each diff_xx_yy.txt file
# Example: diff_18_19.txt   32576

python init_diffs.py temp_difflog.txt
cp temp_difflog.txt difflog.txt
# manually edit difflog.txt, adding <TAB>brief comment 
# Example: diff_18_19.txt   32576	remove ‡; misc. <ls>

======================================================
# temporary comments to ignore for now.
#----- move currently untracked csl-orig/v02/ap
cd /c/xampp/htdocs/cologne/csl-orig/v02
mv ap temp_ap_20250701

#----- remove ap from .gitignore (so git will track ap kosha)
cd /c/xampp/htdocs/cologne/csl-orig/
# edit .gitignore :  remove v02/
git add .
git commit -m "comment out v02/ap/*  in .gitignore, so git will track v02/ap"
git push
#----- 

#----- make new repo:  sanskrit-lexicon/AP for work on ap57
cd /c/xampp/htdocs/sanskrit-lexicon
git clone git@github.com:sanskrit-lexicon/AP.git
#---  get usual .gitignore
cp AP90/.gitignore AP/



# ap_01.txt	(Fri Jan 24 16:13:52 2020)	initial commit
cp commits/ap_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
