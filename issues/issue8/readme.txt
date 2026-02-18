
02-11-2026 Explore AP57_AB_v4a.txt from Andhrabharati
 https://github.com/sanskrit-lexicon/AP/issues/5#issuecomment-3831267121
 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8 #home

Note: discussion of extended ascii moved to readme_ea.txt.

* --------------------------------
* v4a
* -------------------------------
* temp_AP57_AB_v4a.txt  # AB original file
unzip AP57_AB_v4a.zip
 AP57_AB_v4a.txt
# Remane to temp
mv AP57_AB_v4a.txt temp_AP57_AB_v4a.txt

# number of lines
wc -l temp_AP57_AB_v4a.txt
# 85200 temp_AP57_AB_v4a.txt

* temp_v4a_0.txt  # replace unicode characters -- AB agree
python v4a_0.py temp_AP57_AB_v4a.txt temp_v4a_0.txt
old=�, new=▪
old=�, new=→
old=.², new=∙²
old=.³, new=∙³
85200 read from temp_AP57_AB_v4a.txt
85200 lines written to temp_v4a_0.txt

** ⏑  U+23D1 METRICAL BREVE
 It is encoded in the Miscellaneous Technical block
  Replace with ˘ U+02d8 BREVE ?
occurs 1 time in cdsl and v4a

** 🞄  U+1f784 BLACK SLIGHTLY SMALL CIRCLE
   Replace with "▪" (U+25AA) (BLACK SMALL SQUARE) 
The character ▪ 
** 🠚  U+1f81a HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD
   Replace  with → u+2192 RIGHTWARDS ARROW

 # 🞄 U+1f784 BLACK SLIGHTLY SMALL CIRCLE ->
 # "▪" (U+25AA) (BLACK SMALL SQUARE) 
 ('\U0001f784', '\u25aa'),
 # 🠚  U+1f81a HEAVY RIGHTWARDS ARROW WITH EQUILATERAL ARROWHEAD ->
 # → u+2192 RIGHTWARDS ARROW
 ('\U0001f81a', '\u2192'),  

* temp_v4a_0a.txt: obvious typos
python v4a_0a.py temp_v4a_0.txt temp_v4a_0a.txt

85200 read from temp_v4a_0.txt
make_newlines_1 changes 2 lines
Remove duplicate line. L=36703 at line # 85199
Remove duplicate line. L=36704 at line # 85200
make_newlines_3 finds 63 cases
85198 lines written to temp_v4a_0a.txt

--- show changes
diff temp_v4a_0.txt temp_v4a_0a.txt > diff_v4a_0a.txt

* temp_v4a_0b.txt: 7 non-obvious changes (a couple missing data restored)
python v4a_0b.py temp_v4a_0a.txt temp_v4a_0b.txt
85198 read from temp_v4a_0a.txt
make_newlines_1 changes 7 lines
85198 lines written to temp_v4a_0b.txt

diff temp_v4a_0a.txt temp_v4a_0b.txt > diff_v4a_0b.txt

* temp_v4a_0c.txt   CDSL displays compile without error.

python v4a_0c.py temp_v4a_0b.txt temp_v4a_0c.txt
85198 read from temp_v4a_0b.txt
make_newlines_1 has 0 problems; 121889 lines
make_newlines_4 alters 36691 lines
make_newlines_4 has 160257 lines
160257 lines written to temp_v4a_0c.txt


#check xml validity  of temp_v4a_0c.txt
sh redo_ap.sh temp_v4a_0c.txt apv4a_0c


* --------------------------------
* ap 
* -------------------------------
* Prepare temp_ap_0a.txt  from csl-orig
# current ap.txt from csl-orig
#  commit ec0b80a5bd60d228162dd8d948fb26a258496055
git show ec0b80a5:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issuex/temp_ap_0a.txt
* Prepare temp_ap_0b.txt  from csl-orig <<< the starting point.
cd /c/xampp/htdocs/cologne/csl-orig
git pull

# current ap.txt from csl-orig
#  commit e1e80b16a5e7340f5bcc76804c3fa420c06d0ede 
git show e1e80b16:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8/temp_ap_0b.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8/ # home
* temp_ap_0c.txt
#
python ap_0c.py temp_ap_0b.txt temp_ap_0c.txt

--- line 126587 change to make
old:
{@{#-saMyamaH#}@} ({#vAksaMyamaH#}), {@{#-saMvaraH#}@}, {@{#-saMgaH#}@} ({#vAksaMgaH#})
new:
{@{#-saMyamaH#}@} ({#vAksaMyamaH#}), {@{#-saMvaraH#}@}, ({#vAksaMvaraH#}) restraint or control of speech. {@{#-saMgaH#}@} ({#vAksaMgaH#})
---
In as, the verb is missing form homonyms, II, III. etc. but present in text.

* temp_ap_0d.txt  manual 
cp temp_ap_0c.txt temp_ap_0d.txt
# manual changes to temp_ap_0d.txt
python lex_comp.py temp_ap_0d.txt temp_v4a_0c.txt temp_lex_comp.txt
Now the sequence of <lex>X</lex> are the same

python db_comp.py 1 temp_ap_0d.txt temp_v4a_0c.txt temp_lex_comp.txt
# resolved
python db_comp.py 2 temp_ap_0d.txt temp_v4a_0c.txt temp_lex_comp.txt

cp temp_ap_0d.txt temp_ap_0d_work1.txt
cp temp_ap_0d.txt temp_ap_0d_work2.txt
--
cp temp_ap_0d.txt temp_ap_0d_work3.txt
python db_comp.py 2 temp_ap_0d_work3.txt temp_v4a_0c.txt temp_lex_comp_work3.txt
93 records written to temp_lex_comp_work3.txt
marking 57 lines
339763 lines written to temp_db_comp_ap.txt

edit temp_lex_comp_work3.txt
edit  temp_db_comp_ap.txt and change  working...
cp temp_db_comp_ap.txt temp_ap_0d.txt
cp temp_ap_0d.txt temp_ap_0d_work4.txt

sh redo_ap.sh temp_ap_0d.txt ap_0d   # validates!
----------------------------------
python db_comp.py 2 temp_ap_0d.txt temp_v4a_0c.txt temp_db_comp_work4.txt
compare_groups finds 19 problem entries
19 records written to temp_db_comp_work4.txt
marking 12 lines
339763 lines written to temp_db_comp_ap.txt
work with temp_db_comp_work4.txt
edit temp_db_comp_ap.txt and change it;
When done, '_' -> '' and save.
cp temp_db_comp_ap.txt temp_ap_0d.txt
sh redo_ap.sh temp_ap_0d.txt ap_0d   # validates!
# save a copy
cp temp_ap_0d.txt temp_ap_0d_work5.txt
------ next iteration
python db_comp.py 2 temp_ap_0d.txt temp_v4a_0c.txt temp_db_comp_work5.txt
compare_groups finds 4 problem entries
4 records written to temp_db_comp_work5.txt
marking 3 lines
339763 lines written to temp_db_comp_ap.txt
work with temp_db_comp_work5.txt
edit temp_db_comp_ap.txt and change it;
WWhen done, '_' -> '' and save.
cp temp_db_comp_ap.txt temp_ap_0d.txt
sh redo_ap.sh temp_ap_0d.txt ap_0d   # validates!
# save a copy
cp temp_ap_0d.txt temp_ap_0d_work6.txt

------ next iteration
python db_comp.py 2 temp_ap_0d.txt temp_v4a_0c.txt temp_db_comp_work6.txt
compare_groups finds 2 problem entries
2 records written to temp_db_comp_work6.txt
marking 2 lines
339763 lines written to temp_db_comp_ap.txt

work with temp_db_comp_work6.txt
edit temp_db_comp_ap.txt and change it;
When done, '_' -> '' and save.
cp temp_db_comp_ap.txt temp_ap_0d.txt
sh redo_ap.sh temp_ap_0d.txt ap_0d   # validates!
# save a copy
cp temp_ap_0d.txt temp_ap_0d_work6.txt

------ next iteration
python db_comp.py 2 temp_ap_0d.txt temp_v4a_0c.txt temp_db_comp_work7.txt
compare_groups finds 2 problem entries
2 records written to temp_db_comp_work7.txt
marking 2 lines
339763 lines written to temp_db_comp_ap.txt

work with temp_db_comp_work7.txt
edit temp_db_comp_ap.txt and change it;
When done, '_' -> '' and save.
cp temp_db_comp_ap.txt temp_ap_0d.txt
sh redo_ap.sh temp_ap_0d.txt ap_0d   # validates!
# save a copy
cp temp_ap_0d.txt temp_ap_0d_work7.txt

------ next iteration
python db_comp.py 2 temp_ap_0d.txt temp_v4a_0c.txt temp_db_comp_work8.txt
0 records written to temp_db_comp_work9.txt

FINALLY, THIS ITERATION IS COMPLETE.
Save a copy  (maybe we have another iteration to do?)
cp temp_ap_0d.txt temp_ap_0d_work9.txt

------ next iteration
python db_comp.py 2 temp_ap_0d.txt temp_v4a_0c.txt temp_db_comp_work9.txt
compare_groups finds 1 problem entries
1 records written to temp_db_comp_work8.txt
marking 1 lines
339763 lines written to temp_db_comp_ap.txt

work with temp_db_comp_work8.txt
edit temp_db_comp_ap.txt and change it;
When done, '_' -> '' and save.
cp temp_db_comp_ap.txt temp_ap_0d.txt
sh redo_ap.sh temp_ap_0d.txt ap_0d   # validates!
# save a copy
cp temp_ap_0d.txt temp_ap_0d_work9.txt

  
python db_comp.py 3 temp_ap_0d.txt temp_v4a_0c.txt temp.txt
compare_groups finds 0 problem entries

* 02-18-2026 Install temp_ap_0d.txt at Github, Cologne
------------
get change file
python diff_to_changes_dict.py temp_ap_0b.txt temp_ap_0d.txt change_ap_0d.txt
1385 changes written to change_ap_0d.txt

------------
install local version
cp temp_ap_0d.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8/  # home

-----------------------------
# sync csl-orig to github:

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: changes based on comparisons with  AP57_AB_v4a.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8/  # home

---------------------------
sync Cologne to github
connect to cologne.
cd csl-orig
git pull
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
sync this repo to Github
git add .
git commit -m "#8 first step towards merging AP57_AB_v4a.txt and cdsl ap.txt"
git push

* ==========================================
* THE END
