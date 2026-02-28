
02-26-2026 Explore AP57_AB_v4a.txt from Andhrabharati, continue
Continued from issue8d
 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e #home

* --------------------------------
* temp_v4a_0e.txt 
cp ../issue8d/temp_v4a_0e.txt /

* temp_v4a_0f.txt  
cp temp_v4a_0e.txt temp_v4a_0f.txt 
# manual edit temp_v4a_0f.txt 

---
<L>441<pc>0032-2<k1>ajita<k2>ajita
old:
→	▪ {#˚Atman, ˚indriya#}	¦
new:
→	▪ {#˚Atman, ˚indriya#}	⁞

---
<L>465<pc>0034-1<k1>ajYAta<k2>ajYAta
old:
→	▪ {#˚kulaSIlasya#}	¦
→	▪ {#˚kulaSIlasya#}	⁞


diff temp_v4a_0e.txt temp_v4a_0f.txt > diff_v4a_0e_0f.txt
 wc -l diff_v4a_0e_0f.txt
8 diff_v4a_0e_0f.txt

* ==========================================
* tempwork/ap_0j_0.txt start with this revision of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
# commit 5020bdb27ca46425451b0a7c83efee1d09243510
git show 5020bdb27:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e/tempwork/ap_0j_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e/
* ==========================================
* tempwork/ap_0j_1.txt entry header sequence r'^.*?¦
sequences r'^.*?¦
** iteration tempwork/ap_0j_1a.txt 
python db_comp.py 15 tempwork/ap_0j_0.txt temp_v4a_0e.txt tempwork/1a_work.txt tempwork/ap_0j_1a.txt 

compare_groups finds 84 problem entries
84 records written to tempwork/1a_work.txt
marking 82 lines
339763 lines written to tempwork/ap_0j_1a.txt

work with tempwork/1a_work.txt
edit tempwork/ap_0j_1a.txt

When done, '_' -> '' and save tempwork/ap_0j_1a.txt

sh redo_ap.sh tempwork/ap_0j_1a.txt ap  # check validation

** iteration tempwork/ap_0j_1b.txt 
python db_comp.py 15 tempwork/ap_0j_1a.txt temp_v4a_0f.txt tempwork/1b_work.txt tempwork/ap_0j_1b.txt 

compare_groups finds 4 problem entries
4 records written to tempwork/1b_work.txt
marking 4 lines
339763 lines written to tempwork/ap_0j_1b.txt

work with tempwork/1b_work.txt
edit tempwork/ap_0j_1b.txt

When done, '_' -> '' and save tempwork/ap_0j_1b.txt

sh redo_ap.sh tempwork/ap_0j_1b.txt ap  # check validation

** finish tempwork/ap_0j_1.txt 
python db_comp.py 15 tempwork/ap_0j_1b.txt temp_v4a_0f.txt tempwork/1c_work.txt tempwork/ap_0j_1c.txt 

compare_groups finds 0 problem entries
0 records written to tempwork/1c_work.txt
marking 0 lines

diff tempwork/ap_0j_1b.txt tempwork/ap_0j_1c.txt | wc -l
#0  
# remove unneeded files
rm tempwork/1c_work.txt tempwork/ap_0j_1c.txt 

** tempwork/ap_0j_1.txt
# get final file under new name tempwork/ap_0j_1.txt
cp tempwork/ap_0j_1b.txt tempwork/ap_0j_1.txt

sh redo_ap.sh tempwork/ap_0j_1.txt ap  # check validation

* ==========================================
* tempwork/ap_0j_2.txt  metaline sequence r'^<L>.*$'
r'^<L>.*$'
meta1 = <L>8895<pc>0419-1<k1>udan<k2>udan<h>1
meta2 = <L>8895<pc>0419-1<k1>udan<k2>1. udan

** iteration tempwork/ap_0j_2a.txt 
python metaline_comp.py tempwork/ap_0j_1.txt temp_v4a_0e.txt tempwork/2a_work.txt tempwork/ap_0j_2a.txt 

compare_groups finds 24 problem entries
24 records written to tempwork/2a_work.txt
marking 24 lines
339763 lines written to tempwork/ap_0j_2a.txt

work with tempwork/2a_work.txt
edit tempwork/ap_0j_2a.txt

When done, '_' -> '' and save tempwork/ap_0j_2a.txt

sh redo_ap.sh tempwork/ap_0j_2a.txt ap  # check validation

** iteration tempwork/ap_0j_2b.txt 
python metaline_comp.py tempwork/ap_0j_2a.txt temp_v4a_0e.txt tempwork/2b_work.txt tempwork/ap_0j_2b.txt 

compare_groups finds 0 problem entries
0 records written to tempwork/2b_work.txt
marking 0 lines
339763 lines written to tempwork/ap_0j_2b.txt

diff tempwork/ap_0j_2a.txt tempwork/ap_0j_2b.txt | wc -l
#0  
# remove unneeded files
rm tempwork/2b_work.txt tempwork/ap_0j_2b.txt 

** tempwork/ap_0j_2.txt
# get final file under new name tempwork/ap_0j_2.txt
cp tempwork/ap_0j_2a.txt tempwork/ap_0j_2.txt

sh redo_ap.sh tempwork/ap_0j_2.txt ap  # check validation

* ==========================================
* tempwork/ap_0j_3.txt  sequence r'‘.*?’'
r'‘.*?’'

** tempwork/ap_0j_3a.txt  merge lines '‘' , '’'
python merge_lines.py 1 tempwork/ap_0j_2.txt tempwork/ap_0j_3a.txt
339763 read from tempwork/ap_0j_2.txt
make_newlines_1 changes 787 lines
make_newlines_1 returns 339763 lines
339763 lines written to tempwork/ap_0j_3a.txt

** iteration tempwork/ap_0j_3b.txt 

python db_comp.py 16 tempwork/ap_0j_3a.txt temp_v4a_0f.txt tempwork/3b_work.txt tempwork/ap_0j_3b.txt 

compare_groups finds 115 problem entries
115 records written to tempwork/3b_work.txt
marking 101 lines
339763 lines written to tempwork/ap_0j_3b.txt

work with tempwork/3b_work.txt
edit tempwork/ap_0j_3b.txt

When done, '_' -> '' and save tempwork/ap_0j_3b.txt

sh redo_ap.sh tempwork/ap_0j_3b.txt ap  # check validation

** iteration tempwork/ap_0j_3c.txt 

python db_comp.py 16 tempwork/ap_0j_3b.txt temp_v4a_0f.txt tempwork/3c_work.txt tempwork/ap_0j_3c.txt 

compare_groups finds 10 problem entries
10 records written to tempwork/3c_work.txt
marking 5 lines
339763 lines written to tempwork/ap_0j_3c.txt


work with tempwork/3c_work.txt
edit tempwork/ap_0j_3c.txt

When done, '_' -> '' and save tempwork/ap_0j_3c.txt

sh redo_ap.sh tempwork/ap_0j_3c.txt ap  # check validation
** final iteration tempwork/ap_0j_3d.txt 

python db_comp.py 16 tempwork/ap_0j_3c.txt temp_v4a_0f.txt tempwork/3d_work.txt tempwork/ap_0j_3d.txt 

compare_groups finds 0 problem entries
0 records written to tempwork/3d_work.txt
marking 0 lines
339763 lines written to tempwork/ap_0j_3d.txt

diff tempwork/ap_0j_3c.txt tempwork/ap_0j_3d.txt | wc -l
# 0

sh redo_ap.sh tempwork/ap_0j_3d.txt ap  # check validation

# discard unneded files
rm tempwork/3d_work.txt tempwork/ap_0j_3d.txt 
** tempwork/ap_0j_3.txt
# get final file under new name tempwork/ap_0j_3.txt
cp tempwork/ap_0j_3c.txt tempwork/ap_0j_3.txt

sh redo_ap.sh tempwork/ap_0j_3.txt ap  # check validation

* ==========================================
* temp_v4a_0g.txt
cp temp_v4a_0f.txt temp_v4a_0g.txt
manual edit:
# Śaṅkarāchārya -> Śaṅkarācārya 13 times
# Śukrāchārya -> Śukrācārya  4 times
# Āchārya -> Ācārya 3 times
# chārya -> cārya
# Gunjā -> Guñjā 8 times
# Gunja -> Guñja 2 times
# billion -> trillion  11 times
# severalty -> severally (1)

diff temp_v4a_0f.txt temp_v4a_0g.txt > diff_v4a_0f_0g.txt
wc -l diff_v4a_0f_0g.txt
# 244
* tempwork/ap_0j_4.txt  letter sequence with latin letter
** iteration tempwork/ap_0j_4a.txt 

python db_comp.py 17 tempwork/ap_0j_3.txt temp_v4a_0f.txt tempwork/4a_work.txt tempwork/ap_0j_4a.txt 

work with tempwork/4a_work.txt
edit tempwork/ap_0j_4a.txt

When done, '_' -> '' and save tempwork/ap_0j_4a.txt

sh redo_ap.sh tempwork/ap_0j_4a.txt ap  # check validation

** iteration tempwork/ap_0j_4b.txt and temp_v4a_0g.txt

python db_comp.py 17 tempwork/ap_0j_4a.txt temp_v4a_0g.txt tempwork/4b_work.txt tempwork/ap_0j_4b.txt 

compare_groups finds 8 problem entries
8 records written to tempwork/4b_work.txt
marking 7 lines
339763 lines written to tempwork/ap_0j_4b.txt


work with tempwork/4b_work.txt
edit tempwork/ap_0j_4b.txt

When done, '_' -> '' and save tempwork/ap_0j_4b.txt

sh redo_ap.sh tempwork/ap_0j_4b.txt ap  # check validation

** iteration tempwork/ap_0j_4c.txt and temp_v4a_0g.txt
** final iteration tempwork/ap_0j_4d.txt and temp_v4a_0g.txt

python db_comp.py 17 tempwork/ap_0j_4c.txt temp_v4a_0g.txt tempwork/4d_work.txt tempwork/ap_0j_4d.txt 

compare_groups finds 0 problem entries
0 records written to tempwork/4d_work.txt
marking 0 lines
339763 lines written to tempwork/ap_0j_4d.txt

When done, '_' -> '' and save tempwork/ap_0j_4d.txt

sh redo_ap.sh tempwork/ap_0j_4d.txt ap  # check validation

diff tempwork/ap_0j_4c.txt tempwork/ap_0j_4d.txt | wc -l
# 0
# remove unneeded
rm tempwork/4d_work.txt tempwork/ap_0j_4d.txt 

** tempwork/ap_0j_4.txt
cp tempwork/ap_0j_4c.txt tempwork/ap_0j_4.txt
* ==========================================
* tempwork/ap_0j_5.txt  letter sequence a-zA-Z

** iteration tempwork/ap_0j_5a.txt 

python db_comp.py 18 tempwork/ap_0j_4.txt temp_v4a_0g.txt tempwork/5a_work.txt tempwork/ap_0j_5a.txt 

compare_groups finds 33 problem entries
33 records written to tempwork/5a_work.txt
marking 33 lines
339763 lines written to tempwork/ap_0j_5a.txt

work with tempwork/5a_work.txt
edit tempwork/ap_0j_5a.txt

When done, '_' -> '' and save tempwork/ap_0j_5a.txt

sh redo_ap.sh tempwork/ap_0j_5a.txt ap  # check validation

** iteration tempwork/ap_0j_5b.txt 

python db_comp.py 18 tempwork/ap_0j_5a.txt temp_v4a_0g.txt tempwork/5b_work.txt tempwork/ap_0j_5b.txt 

compare_groups finds 3 problem entries
3 records written to tempwork/5b_work.txt
marking 3 lines
339763 lines written to tempwork/ap_0j_5b.txt

work with tempwork/5b_work.txt
edit tempwork/ap_0j_5b.txt

When done, '_' -> '' and save tempwork/ap_0j_5b.txt

sh redo_ap.sh tempwork/ap_0j_5b.txt ap  # check validation
** final tempwork/ap_0j_5.txt 

python db_comp.py 18 tempwork/ap_0j_5b.txt temp_v4a_0g.txt tempwork/5c_work.txt tempwork/ap_0j_5c.txt 

compare_groups finds 0 problem entries

cp tempwork/ap_0j_5b.txt tempwork/ap_0j_5.txt
# remove unneeded files
rm tempwork/5c_work.txt tempwork/ap_0j_5c.txt 

sh redo_ap.sh tempwork/ap_0j_5c.txt ap  # check validation

* ==========================================
* change files
python diff_to_changes_dict.py tempwork/ap_0j_0.txt tempwork/ap_0j_1.txt change_ap_0j_0_1.txt
84 changes written to change_ap_0j_0_1.txt

python diff_to_changes_dict.py tempwork/ap_0j_1.txt tempwork/ap_0j_2.txt change_ap_0j_1_2.txt
24 changes written to change_ap_0j_1_2.txt

python diff_to_changes_dict.py tempwork/ap_0j_2.txt tempwork/ap_0j_3.txt change_ap_0j_2_3.txt
820 changes written to change_ap_0j_2_3.txt

python diff_to_changes_dict.py tempwork/ap_0j_3.txt tempwork/ap_0j_4.txt change_ap_0j_3_4.txt
54 changes written to change_ap_0j_3_4.txt

python diff_to_changes_dict.py tempwork/ap_0j_4.txt tempwork/ap_0j_5.txt change_ap_0j_4_5.txt
30 changes written to change_ap_0j_4_5.txt

* ==========================================
* INSTALLATION csl-orig
* 02-28-2026 Install tempwork/ap_0j_5.txt at Github, Cologne

** check repo(s) for pull
cd /c/xampp/htdocs/cologne/csl-orig
git status
git pull
# Already up to date.
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e #home

------------
** install local displays from tempwork/ap_0j_5.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e #home
cp tempwork/ap_0j_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e/  # home

-----------------------------
** sync csl-orig to github:
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: changes based on comparisons with  AP57_AB_v4a.txt. version ap_0j_5.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
# 1 file changed, 1009 insertions(+), 1009 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e/  # home

---------------------------
** sync Cologne to github
# connect to cologne.
cd csl-orig
git pull

cd ../csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
* sync this repo to Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8e
git add .
git commit -m "#8 merging AP57_AB_v4a.txt and cdsl ap.txt (ap_0j_5.txt)"
git push

* ==========================================
* THE END

