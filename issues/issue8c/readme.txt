
02-24-2026 Explore AP57_AB_v4a.txt from Andhrabharati, continue
Continued from issue8b
 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c #home

* --------------------------------
* TODO possible changes to temp_v4a_0c.txt
---
'= {@{#X#}@}' -> '= {#X#}'  (3 instances)
--- L=15600
'to conquer defeat' -> 'to conquer, defeat'
* temp_v4a_0d.txt 
cp ../issue8b/temp_v4a_0d.txt /

* --------------------------------
* Prepare for changes to make_xml.py
cd /c/xampp/htdocs/cologne/csl-pywork/
git log
# latest commit a5bad985df7a66226027fbc7870159eab2c103bf
cd /c/xampp/htdocs/cologne/csl-pywork/
git show a5bad985df7:v02/makotemplates/pywork/make_xml.py > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c/make_xml.py
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c/

* Prepare for changes to basicadjust.php
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git log 
# latest commit dee532bb0b71f565d9209bc4bc1a4e18fdf09ba0
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git show dee532bb0b:v02/makotemplates/web/webtc/basicadjust.php > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c/basicadjust.php
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c/


* ==========================================
* Start with version tempwork/ap_0h_0.txt  of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
# commit b728184b318ce16cd0a2ac0582e75211f9eb2825
git show b728184b:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c/tempwork/ap_0h_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c 
* ==========================================
* tempwork/ap_0h_1.txt intermediate  r'<ls.*?</ls>'
 db_comp.py option 10: r'<ls.*?</ls>'
python db_comp.py 10 tempwork/ap_0h_0.txt temp_v4a_0d.txt tempwork/10_work1.txt tempwork/ap_0h_1.txt

compare_groups finds 300 problem entries
300 records written to tempwork/10_work1.txt
marking 295 lines
339763 lines written to tempwork/ap_0h_1.txt

work with tempwork/10_work1.txt 
edit tempwork/ap_0h_1.txt
'.x</ls>' -> '</ls>.'
When done, '_' -> '' and save tempwork/ap_0h_1.txt

sh redo_ap.sh tempwork/ap_0h_1.txt ap  # check validation

* tempwork/ap_0h_2.txt final 
python db_comp.py 10 tempwork/ap_0h_1.txt temp_v4a_0d.txt tempwork/10_work2.txt tempwork/ap_0h_2.txt

compare_groups finds 27 problem entries
27 records written to tempwork/10_work2.txt
marking 27 lines
339763 lines written to tempwork/ap_0h_2.txt

work with tempwork/10_work2.txt 
edit tempwork/ap_0h_2.txt

'.x</ls>' -> '</ls>.'
When done, '_' -> '' and save tempwork/ap_0h_2.txt

sh redo_ap.sh tempwork/ap_0h_2.txt ap  # check validation

python db_comp.py 10 tempwork/ap_0h_2.txt temp_v4a_0d.txt tempwork/10_work3.txt tempwork/ap_0h_3.txt

compare_groups finds 0 problem entries

Remove unneeded files:
rm tempwork/10_work3.txt tempwork/ap_0h_3.txt

* ==========================================
* tempwork/ap_0h_3.txt final  r'<lang.*?</lang>'
 db_comp.py option 11: r'<lang.*?</lang>'
python db_comp.py 11 tempwork/ap_0h_2.txt temp_v4a_0d.txt tempwork/11_work1.txt tempwork/ap_0h_3.txt

compare_groups finds 1 problem entries
1 records written to tempwork/11_work1.txt
marking 1 lines

work with tempwork/11_work1.txt 
edit tempwork/ap_0h_3.txt

When done, '_' -> '' and save tempwork/ap_0h_3.txt

sh redo_ap.sh tempwork/ap_0h_3.txt ap  # check validation

python db_comp.py 11 tempwork/ap_0h_3.txt temp_v4a_0d.txt tempwork/11_work2.txt tempwork/ap_0h_4.txt

0 records written to tempwork/11_work2.txt

remove unneeded:
rm tempwork/11_work2.txt tempwork/ap_0h_4.txt
* ==========================================
* tempwork/ap_0h_4.txt final  r'<ab.*?</ab>'
# db_comp.py option 12: r'<ab.*?</ab>'
python db_comp.py 12 tempwork/ap_0h_3.txt temp_v4a_0d.txt tempwork/12_work1.txt tempwork/ap_0h_4.txt

compare_groups finds 24 problem entries
24 records written to tempwork/12_work1.txt
marking 12 lines
339763 lines written to tempwork/ap_0h_4.txt

work with tempwork/12_work1.txt 
edit tempwork/ap_0h_4.txt

When done, '_' -> '' and save tempwork/ap_0h_4.txt

sh redo_ap.sh tempwork/ap_0h_4.txt ap  # check validation

python db_comp.py 12 tempwork/ap_0h_4.txt temp_v4a_0d.txt tempwork/12_work2.txt tempwork/ap_0h_5.txt
compare_groups finds 0 problem entries

Remove unneeded
rm tempwork/12_work2.txt tempwork/ap_0h_5.txt

0 records written to tempwork/11_work2.txt

remove unneeded:
rm tempwork/11_work2.txt tempwork/ap_0h_4.txt
* ==========================================
* tempwork/ap_0h_5.txt = temp_ap_0h_4.txt  r'<is.*?</is>'
# db_comp.py option 13: r'<is.*?</is>'
python db_comp.py 13 tempwork/ap_0h_4.txt temp_v4a_0d.txt tempwork/13_work1.txt tempwork/ap_0h_5.txt

compare_groups finds 0 problem entries

diff tempwork/ap_0h_5.txt tempwork/ap_0h_4.txt
* ==========================================
* tempwork/ap_0h_6.txt final  '14': r'−', # U+2212 Minus Sign
 db_comp.py option '14': r'−', # U+2212 Minus Sign
python db_comp.py 14 tempwork/ap_0h_5.txt temp_v4a_0d.txt tempwork/14_work1.txt tempwork/ap_0h_6.txt

compare_groups finds 87 problem entries
87 records written to tempwork/14_work1.txt
marking 23 lines
339763 lines written to tempwork/ap_0h_6.txt

work with tempwork/14_work1.txt 
edit tempwork/ap_0h_6.txt

When done, '_' -> '' and save tempwork/ap_0h_6.txt

sh redo_ap.sh tempwork/ap_0h_6.txt ap  # check validation

python db_comp.py 14 tempwork/ap_0h_6.txt temp_v4a_0d.txt tempwork/14_work2.txt tempwork/ap_0h_7.txt
0 records written to tempwork/14_work2.txt

remove unneeded:
rm tempwork/14_work2.txt tempwork/ap_0h_7.txt
* ==========================================
* ==========================================
* ==========================================
* ==========================================
* change file
python diff_to_changes_dict.py tempwork/ap_0h_0.txt tempwork/ap_0h_6.txt change_ap_0h_0_6.txt
355 changes written to change_ap_0h_0_6.txt

* ==========================================
* INSTALLATION csl-orig
* 02-24-2026 Install tempwork/ap_0h_6.txt at Github, Cologne

** check repo(s) for pull
cd /c/xampp/htdocs/cologne/csl-orig
git status
git pull
# Already up to date.
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c #home

------------
** install local version from tempwork/ap_0h_6.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c #home
cp tempwork/ap_0h_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c/  # home

-----------------------------
** sync csl-orig to github:
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: changes based on comparisons with  AP57_AB_v4a.txt. version ap_0h_6.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
# 1 file changed, 355 insertions(+), 355 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c/  # home

---------------------------
** sync Cologne to github
# connect to cologne.
cd csl-orig
git pull

cd ../csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
* sync this repo to Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8c
git add .
git commit -m "#8 merging AP57_AB_v4a.txt and cdsl ap.txt (ap_0h_6.txt)"
git push

* ==========================================
* NOT DONE !! tempwork/ap_0h_7.txt devanagari sequence  
python d_comp.py tempwork/ap_0h_6.txt temp_v4a_0d.txt tempwork/d_work1.txt tempwork/ap_0h_7.txt

compare_groups finds 2137 problem entries
2137 records written to tempwork/d_work1.txt
marking 2137 lines
339763 lines written to tempwork/ap_0h_7.txt

work with tempwork/15_work1.txt 
edit tempwork/ap_0h_7.txt

When done, '_' -> '' and save tempwork/ap_0h_7.txt

sh redo_ap.sh tempwork/ap_0h_7.txt ap  # check validation

python db_comp.py 14 tempwork/ap_0h_7.txt temp_v4a_0d.txt tempwork/14_work2.txt tempwork/ap_0h_8.txt


remove unneeded:
rm tempwork/14_work2.txt tempwork/ap_0h_7.txt
* ==========================================
* THE END

