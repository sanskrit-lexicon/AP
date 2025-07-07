
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

# copy first commit ap_01.txt to issue1
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue1
cp /e/ap_open/commits/ap_01.txt ap_01.txt
# push issue1 to github

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

#0a changes .gitignore of csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git add .gitignore
git commit -m "AP: change csl-orig .gitignore to track ap.
> Ref: https://github.com/sanskrit-lexicon/AP/issues/1"


#0b initialize csl-orig/v02/ap as empty directory

cd /c/xampp/htdocs/cologne/csl-orig/v02
mkdir ap

cd /c/xampp/htdocs/cologne/csl-orig/v02/ap

------------------------------------------
# ap_01.txt	(Fri Jan 24 16:13:52 2020)	initial commit
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_01.txt ap.txt
git add ap.txt
git commit -m "AP: ap_01.txt	(Fri Jan 24 16:13:52 2020)	initial commit
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_01.txt	(Fri Jan 24 16:13:52 2020)	initial commit
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_01.txt ap.txt
git add ap.txt
git commit -m "AP: ap_01.txt	(Fri Jan 24 16:13:52 2020)	initial commit
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_13.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_13.txt ap.txt
git add ap.txt
git commit -m "AP: ap_13.txt	(Tue Jun 1 16:27:23 2021)	diff_01_02.txt - diff_12_13.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_14.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_14.txt ap.txt
git add ap.txt
git commit -m "AP: ap_14.txt	(Sun Jun 13 13:25:43 2021)	diff_13_14.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_15.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_15.txt ap.txt
git add ap.txt
git commit -m "AP: ap_15.txt	(Sun Jun 13 17:10:22 2021)	diff_14_15.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_16.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_16.txt ap.txt
git add ap.txt
git commit -m "AP: ap_16.txt	(Sat Jun 19 15:44:14 2021)	diff_ap_15_16.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_17.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_17.txt ap.txt
git add ap.txt
git commit -m "AP: ap_17.txt	(Wed Jun 23 15:39:27 2021)	diff_ap_16_17.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_18.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_18.txt ap.txt
git add ap.txt
git commit -m "AP: ap_18.txt	(Sat Jul 3 20:51:45 2021)	diff_ap_17_18.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_19.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_19.txt ap.txt
git add ap.txt
git commit -m "AP: ap_19.txt	(Thu Jul 8 12:31:58 2021)	diff_ap_18_19.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# ap_28.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp /e/ap_open/commits/ap_28.txt ap.txt
git add ap.txt
git commit -m "AP: ap_28.txt	(Tue Jul 16 14:08:09 2024)	diff_ap_19_20.txt - diff_27_28.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
diff ap.txt ../temp_ap_20250701/ap.txt | wc -l
# 0 as expected
# copy ap_28.txt to issue1
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue1/
cp /e/ap_open/commits/ap_28.txt .
# commit issue1 and push to github

------------------------------------------
# copy other files from temp_ap_20250701
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
cp ../temp_ap_20250701/ap-meta2.txt .
cp ../temp_ap_20250701/ap_hwextra.txt .
cp ../temp_ap_20250701/apheader.xml  .
git add .
git commit -m "AP: ap-meta2.txt,  ap_hwextra.txt,  apheader.xml
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"

------------------------------------------
# push all commits to github
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap
git push

------------------------------------------
# save transcript
Above work done in gitbash terminal, initially reset.
select all (in terminal) and save to file readme_transcript.txt

------------------------------------------
sync csl-orig on cologne server

#login to cologne server.
# change directory to scans
cd csl-orig/v02
# rename old 'untracked' ap
mv ap temp_ap_20250701
# pull csl-orig to get revised and tracked .gitignore and 'ap'
git pull

# -----

------------------------------------------
csl-homepage
# update on local server
(see csl-homepage/readme_update.txt)
# push to github
# update on cologne server
pull
sh update_version.sh
sh redo_cologne.sh

------------------------------------------
csl-apidev/sample/dictnames.js
Add
['AP' , 'Apte Practical Sanskrit-English Dictionary, revised']

push to github

on cologne server, pull

------------------------------------------
WHAT ELSE TO DO?
