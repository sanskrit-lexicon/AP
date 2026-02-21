
02-19-2026 Explore AP57_AB_v4a.txt from Andhrabharati, continue
Continued from issue8
 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8a #home

* --------------------------------
* temp_v4a_0c.txt  Slightly edited version of AP57_AB_v4a.txt
cp ../issue8/temp_v4a_0c.txt temp_v4a_0c.txt
* TODO possible changes to temp_v4a_0c.txt
---
'= {@{#X#}@}' -> '= {#X#}'  (3 instances)
--- L=15600
'to conquer defeat' -> 'to conquer, defeat'
* -------------------------------
* Start with temp_ap_0d.txt 

(issue8 ended with temp_ap_0d.txt)
 commit 390e322496
cd /c/xampp/htdocs/cologne/csl-orig/
git show 390e322496:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8a/temp_ap_0d.txt

* --------------------------------
* TODO possible global changes in temp_ap_0e.txt
---
342 matches in 334 lines for "@} ({@"  (none in v4a_0c)
---
'--({%<ab>' -> '━{%<ab>'  (5)
---
({@



* temp_ap_0e.txt {@X@} sequences match to temp_f4a_0c.txt

sh redo_ap.sh temp_ap_0e.txt ap_0e   # validates!
----------------------------------
# option 4 is sequence of devanagari-bold text markup
** --iteration 1
python db_comp.py 4 temp_ap_0e.txt temp_v4a_0c.txt tempwork/4_work1.txt
246 records written to tempwork/4_work4.txt
marking 150 lines
339763 lines written to temp_db_comp_ap.txt

work with tempwork/4_work1.txt
edit temp_db_comp_ap.txt and change it;
When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_4_work1. # save a copy
cp temp_db_comp_ap.txt temp_ap_0e.txt # update ap_0e

** --iteration 2
python db_comp.py 4 temp_ap_0e.txt temp_v4a_0c.txt tempwork/4_work2.txt
compare_groups finds 34 problem entries
34 records written to tempwork/4_work2.txt
marking 27 lines
339763 lines written to temp_db_comp_ap.txt

work with tempwork/4_work2.txt
edit temp_db_comp_ap.txt and change it;
  When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_4_work2. # save a copy
cp temp_db_comp_ap.txt temp_ap_0e.txt # update ap_0e

** --iteration 
python db_comp.py 4 temp_ap_0e.txt temp_v4a_0c.txt tempwork/4_work3.txt
compare_groups finds 5 problem entries
5 records written to tempwork/4_work3.txt
marking 4 lines
339763 lines written to temp_db_comp_ap.txt

work with tempwork/4_work3.txt
edit temp_db_comp_ap.txt and change it;
  When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_4_work3. # save a copy
cp temp_db_comp_ap.txt temp_ap_0e.txt # update ap_0e

** --iteration 4
python db_comp.py 4 temp_ap_0e.txt temp_v4a_0c.txt tempwork/4_work4.txt
compare_groups finds 3 problem entries
3 records written to tempwork/4_work4.txt
marking 3 lines
339763 lines written to temp_db_comp_ap.txt

work with tempwork/4_work4.txt
edit temp_db_comp_ap.txt and change it;
  When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_4_work4. # save a copy
cp temp_db_comp_ap.txt temp_ap_0e.txt # update ap_0e

** --iteration 5
python db_comp.py 4 temp_ap_0e.txt temp_v4a_0c.txt tempwork/4_work5.txt
compare_groups finds 1 problem entries
1 records written to tempwork/4_work5.txt
marking 1 lines
339763 lines written to temp_db_comp_ap.txt

work with tempwork/4_work5.txt
edit temp_db_comp_ap.txt and change it;
  When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_4_work5. # save a copy
cp temp_db_comp_ap.txt temp_ap_0e.txt # update ap_0e

** --iteration 6
python db_comp.py 4 temp_ap_0e.txt temp_v4a_0c.txt tempwork/4_work6.txt
compare_groups finds 1 problem entries
1 records written to tempwork/4_work6.txt
marking 1 lines
339763 lines written to temp_db_comp_ap.txt

work with tempwork/4_work6.txt
edit temp_db_comp_ap.txt and change it;
  When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_4_work6. # save a copy
cp temp_db_comp_ap.txt temp_ap_0e.txt # update ap_0e

** --iteration 7 No problems found
python db_comp.py 4 temp_ap_0e.txt temp_v4a_0c.txt tempwork/4_work7.txt
compare_groups finds 0 problem entries
0 records written to tempwork/4_work7.txt
marking 0 lines
339763 lines written to temp_db_comp_ap.txt

* temp_ap_0f.txt '{@X@} ({@Y@}' sequences match to temp_f4a_0c.txt

# option 5 is sequence of '{@[^@]*?@} ({@[^@]@}'   (note paren)
cp temp_ap_0e.txt temp_ap_0f.txt
Revise temp_ap_0f.txt until agreement with v4a_0c
** --iteration 1
python db_comp.py 5 temp_ap_0f.txt temp_v4a_0c.txt tempwork/5_work1.txt

compare_groups finds 20 problem entries
20 records written to tempwork/5_work1.txt
marking 1 lines
339763 lines written to temp_db_comp_ap.txt

work with tempwork/5_work1.txt
edit temp_db_comp_ap.txt and change it;
When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_5_work1. # save a copy
cp temp_db_comp_ap.txt temp_ap_0f.txt # update ap_0e

** --iteration 2
python db_comp.py 5 temp_ap_0f.txt temp_v4a_0c.txt tempwork/5_work2.txt

compare_groups finds 2 problem entries
2 records written to tempwork/5_work2.txt
marking 1 lines

work with tempwork/5_work2.txt
edit temp_db_comp_ap.txt and change it;
When done, '_' -> '' and save.
sh redo_ap.sh temp_db_comp_ap.txt aptemp  # check validation
cp temp_db_comp_ap.txt tempwork/ap_5_work2. # save a copy
cp temp_db_comp_ap.txt temp_ap_0f.txt # update ap_0e

** --iteration 3  no more changes
python db_comp.py 5 temp_ap_0f.txt temp_v4a_0c.txt tempwork/5_work3.txt

0 records written to tempwork/5_work3.txt
marking 0 lines
339763 lines written to temp_db_comp_ap.txt

diff temp_ap_0f.txt temp_db_comp_ap.txt  | wc -l
#0

** x
python db_comp.py 3 temp_ap_0f.txt temp_v4a_0c.txt temp.txt

* 02-21-2026 Install temp_ap_0f.txt at Github, Cologne
------------
get change files
python diff_to_changes_dict.py temp_ap_0d.txt temp_ap_0e.txt change_ap_0d_0e.txt
574 changes written to change_ap_0d_0e.txt

python diff_to_changes_dict.py temp_ap_0e.txt temp_ap_0f.txt change_ap_0e_0f.txt
42 changes written to change_ap_0e_0f.txt

# full change from 0d to 0f
python diff_to_changes_dict.py temp_ap_0d.txt temp_ap_0f.txt change_ap_0d_0f.txt
614 changes written to change_ap_0d_0f.txt

------------
# check no intervening changes to ap.txt
cd /c/xampp/htdocs/cologne/csl-orig
git status
# On branch master
# Your branch is up to date with 'origin/master'.
# nothing to commit, working tree clean
git pull
# Already up to date.
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8a #home

------------
# install local version from temp_ap_0f.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8a #home
cp temp_ap_0f.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8a/  # home

-----------------------------
# sync csl-orig to github:

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: changes based on comparisons with  AP57_AB_v4a.txt. version 0f
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
#  1 file changed, 614 insertions(+), 614 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8a/  # home

---------------------------
sync Cologne to github
#connect to cologne.
cd csl-orig
git pull
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
sync this repo to Github
git add .
git commit -m "#8 merging AP57_AB_v4a.txt and cdsl ap.txt (ap_0f.txt)"
git push

* ==========================================
* THE END
