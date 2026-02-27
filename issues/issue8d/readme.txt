
02-25-2026 Explore AP57_AB_v4a.txt from Andhrabharati, continue
Continued from issue8c
 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d #home

* --------------------------------
* temp_v4a_0d.txt 
cp ../issue8c/temp_v4a_0d.txt /

* TODO temp_v4a_0e misc.
---
'= {@{#X#}@}' -> '= {#X#}'  (3 instances)
--- L=15600
'to conquer defeat' -> 'to conquer, defeat'

* temp_v4a_0e.txt 
cp temp_v4a_0d.txt temp_v4a_0e.txt
manual edit temp_v4a_0e.txt  

---
{#durjanIkf [civa#}] -> {#durjanIkf [civa]#}
---
({#bAREH) -> {#)bAREH)
---
old: 
▪∙²3 of Kṛṣṇa. ▪∙²4 the number ‘seven’. ▪∙²5 a king;
new:
▪∙²3 of Kṛṣṇa. ▪∙²4 the number ‘seven’. {#˚ISvaraH, ˚rAjaH#} an epithet of the mountain Himālaya. {#˚jaH#} a tree. ▪∙²5 a king;
---
<L>314<pc>0026-1<k1>aNganam
---
<L>29941 k1=vAc  near {@{#-saMvaraH#}@}
* ==========================================
* tempwork/ap_0i_0.txt start with this revision of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
# commit 73e073a29568cab1013733f6fa64486cd0cca731
git show 73e073a29:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d/tempwork/ap_0i_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d/
* ==========================================
* tempwork/ap_0i_1.txt check 'well-formed' status of tags
cp tempwork/ap_0i_0.txt tempwork/ap_0i_1.txt
 tagpairs = [
  ('(', ')'),
  ('[', ']'),
  ('{#', '#}'),
  ]

# manual edit of tempwork/ap_0i_01.txt
python check_balance.py tempwork/ap_0i_1.txt 
Error: closing ')' at line 95397 with no matching opener

python check_balance.py tempwork/ap_0i_1.txt 
Error: mismatched close '#}' at line 152282, expected ']'

python check_balance.py tempwork/ap_0i_1.txt 
Error: mismatched close ')' at line 187086, expected '#}'

python check_balance.py tempwork/ap_0i_1.txt 
Error: closing '}' at line 146731 with no matching opener

python check_balance.py tempwork/ap_0i_1.txt 
339763 read from tempwork/ap_0i_1.txt
flag=True, count=228952, nesting=True
tagpairs = [('(', ')'), ('[', ']'), ('{#', '#}')]

flag=True, count=271847, nesting=True
tagpairs1 = [('{', '}')]


# change file
python diff_to_changes_dict.py tempwork/ap_0i_0.txt tempwork/ap_0i_1.txt change_ap_0i_0_1.txt

* ==========================================
* tempwork/ap_0i_2.txt ^{#X#}, {#Y#}¦  ==>  {#X, Y#}¦

python ap_0i_2.py tempwork/ap_0i_1.txt tempwork/ap_0i_2.txt
339763 read from tempwork/ap_0i_1.txt
make_newlines_1 finds 1512 cases
make_newlines_1 returns 339763 lines
339763 lines written to tempwork/ap_0i_2.txt


* tempwork/ap_0i_3.txt  deva seq (split at '[ ,]+'

# Agreement done in several steps (3a, 3b, ...)
** iteration tempwork/ap_0i_3a.txt 
python d_comp.py 2 tempwork/ap_0i_2.txt temp_v4a_0d.txt tempwork/3a_work1.txt tempwork/ap_0i_3a.txt 

compare_groups finds 207 problem entries
207 records written to tempwork/3a_work1.txt
marking 207 lines
339763 lines written to tempwork/ap_0i_3a.txt

work with tempwork/3a_work1.txt
edit tempwork/ap_0i_3a.txt

When done, '_' -> '' and save tempwork/ap_0i_3a.txt

sh redo_ap.sh tempwork/ap_0i_3a.txt ap  # check validation

** iteration tempwork/ap_0i_3b.txt 
python d_comp.py 2 tempwork/ap_0i_3a.txt temp_v4a_0d.txt tempwork/3b_work1.txt tempwork/ap_0i_3b.txt 

compare_groups finds 24 problem entries
24 records written to tempwork/3b_work1.txt
marking 24 lines
339763 lines written to tempwork/ap_0i_3b.txt

work with tempwork/3b_work1.txt
edit tempwork/ap_0i_3b.txt

When done, '_' -> '' and save tempwork/ap_0i_3b.txt

sh redo_ap.sh tempwork/ap_0i_3b.txt ap  # check validation 

** iteration tempwork/ap_0i_3c.txt 
python d_comp.py 2 tempwork/ap_0i_3b.txt temp_v4a_0d.txt tempwork/3c_work1.txt tempwork/ap_0i_3c.txt 

compare_groups finds 9 problem entries
9 records written to tempwork/3c_work1.txt
marking 9 lines
339763 lines written to tempwork/ap_0i_3c.txt

work with tempwork/3c_work1.txt
edit tempwork/ap_0i_3c.txt

When done, '_' -> '' and save tempwork/ap_0i_3c.txt

sh redo_ap.sh tempwork/ap_0i_3c.txt ap  # check validation 

** iteration tempwork/ap_0i_3d.txt   Using temp_v4a_0e.txt
python d_comp.py 2 tempwork/ap_0i_3c.txt temp_v4a_0e.txt tempwork/3d_work1.txt tempwork/ap_0i_3d.txt 

compare_groups finds 4 problem entries
4 records written to tempwork/3d_work1.txt
marking 4 lines
339763 lines written to tempwork/ap_0i_3d.txt

work with tempwork/3d_work1.txt
edit tempwork/ap_0i_3d.txt

When done, '_' -> '' and save tempwork/ap_0i_3d.txt

sh redo_ap.sh tempwork/ap_0i_3d.txt ap  # check validation 
** iteration tempwork/ap_0i_3e.txt   Using revised temp_v4a_0e.txt
python d_comp.py 2 tempwork/ap_0i_3d.txt temp_v4a_0e.txt tempwork/3e_work1.txt tempwork/ap_0i_3e.txt 

compare_groups finds 1 problem entries
1 records written to tempwork/3e_work1.txt
marking 1 lines
339763 lines written to tempwork/ap_0i_3e.txt

work with tempwork/3e_work1.txt
edit tempwork/ap_0i_3e.txt

When done, '_' -> '' and save tempwork/ap_0i_3e.txt

sh redo_ap.sh tempwork/ap_0i_3e.txt ap  # check validation 

** iteration tempwork/ap_0i_3e.txt   Using revised temp_v4a_0e.txt
python d_comp.py 2 tempwork/ap_0i_3d.txt temp_v4a_0e.txt tempwork/3e_work1.txt tempwork/ap_0i_3e.txt 

compare_groups finds 1 problem entries
1 records written to tempwork/3e_work1.txt
marking 1 lines
339763 lines written to tempwork/ap_0i_3e.txt

work with tempwork/3e_work1.txt
edit tempwork/ap_0i_3e.txt

When done, '_' -> '' and save tempwork/ap_0i_3e.txt

sh redo_ap.sh tempwork/ap_0i_3e.txt ap  # check validation 
** final: tempwork/ap_0i_3.txt
python d_comp.py 2 tempwork/ap_0i_3e.txt temp_v4a_0e.txt tempwork/3f_work1.txt tempwork/ap_0i_3f.txt 

compare_groups finds 0 problem entries
0 records written to tempwork/3f_work1.txt
marking 0 lines
339763 lines written to tempwork/ap_0i_3f.txt

sh redo_ap.sh tempwork/ap_0i_3f.txt ap  # check validation 

# remove unneeded
rm tempwork/3f_work1.txt tempwork/ap_0i_3f.txt 

# copy to new name
cp tempwork/ap_0i_3e.txt tempwork/ap_0i_3.txt
* ==========================================
* change files
python diff_to_changes_dict.py tempwork/ap_0i_0.txt tempwork/ap_0i_1.txt change_ap_0i_0_1.txt
4 changes written to change_ap_0i_0_1.txt

python diff_to_changes_dict.py tempwork/ap_0i_1.txt tempwork/ap_0i_2.txt change_ap_0i_1_2.txt
1512 changes written to change_ap_0i_1_2.txt

python diff_to_changes_dict.py tempwork/ap_0i_2.txt tempwork/ap_0i_3.txt change_ap_0i_2_3.txt
251 changes written to change_ap_0i_2_3.txt


* ==========================================
* INSTALLATION csl-orig
* 02-26-2026 Install tempwork/ap_0i_3.txt at Github, Cologne

** check repo(s) for pull
cd /c/xampp/htdocs/cologne/csl-orig
git status
git pull
# Already up to date.
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d #home

------------
** install local version from tempwork/ap_0i_3.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d #home
cp tempwork/ap_0i_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d/  # home

-----------------------------
** sync csl-orig to github:
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: changes based on comparisons with  AP57_AB_v4a.txt. version ap_0i_3.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
# 1 file changed, 1762 insertions(+), 1762 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d/  # home

---------------------------
** sync Cologne to github
# connect to cologne.
cd csl-orig
git pull

cd ../csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
* sync this repo to Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8d
git add .
git commit -m "#8 merging AP57_AB_v4a.txt and cdsl ap.txt (ap_0i_3.txt)"
git push

* ==========================================
* ==========================================
* THE END

