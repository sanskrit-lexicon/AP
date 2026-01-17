
https://github.com/sanskrit-lexicon/AP/issues/3
 "b'->'v' sanskrit global changes"


cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home

* revised git history of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig
 git log --follow --pretty=format:"%ad %h %an %s" --date=short -- v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/ap_history.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home
wc -l ap_history.txt
# 131
* temp_ABuploads from issue3 links
AP57_AB_v1.txt   Dec 22, 2025 11:58 AM Est
AP57_AB_v2.txt   Dec 24. 2-25  5:39 AM Est
AP57_AB_v3.txt   Jan 13, 2026

  v2 includes and supercedes the changes in v1
  wc -l temp_ABuploads/AP57_*.txt
  341291 temp_ABuploads/AP57_AB_v1.txt
  341291 temp_ABuploads/AP57_AB_v2.txt
  341291 temp_ABuploads/AP57_AB_v3.txt
* temp_ap_history
mkdir temp_ap_history
sh add_history.sh 20260112 107338c
341291 ap_20260112_107338c.txt

sh add_history.sh 20260110 5fb2195 
341291 ap_20260110_5fb2195.txt

sh add_history.sh 20260103 37ff01c
341291 ap_20260103_37ff01c.txt

sh add_history.sh 20260102 2f966c3 
341291 ap_20260102_2f966c3.txt

sh add_history.sh 20251217 8da03e5 # last before AB v1
341291 ap_20251217_8da03e5.txt

* git changes between 20251217 and 20260112
cd temp_ap_history
python ../diff_to_changes_dict.py ap_20251217_8da03e5.txt ap_20260112_107338c.txt ../change_20251216_20260112.txt
22 lines changed

* TODO paRqitI  where do 4/5 come from -- not in print
ap_20251217_8da03e5.txt
<L>19823<pc>0955-1<k1>paRqitI<k2>paRqitI
{#paRqitI#}¦ {%f.%} Learning; {#pratipattumiyattayA jano na kilAsIdalamasya#}
 {#paRqitIm#} <ls>Śāhendra. 2. 51.</ls> <ls>Ms. 12. 28.</ls>
.²4 Obtaining, securing.
.²5 A ttracting, captivating,
<LEND>


* AP57_AB_v3a.txt
Modification of AP57_AB_v3.txt so (local) CDSL displays are error-free.
cd temp_ABuploads

# mostly {#<ab>
python prepchg.py AP57_AB_v3.txt prepchg.txt
cp prepchg.txt prepchg_edit.txt
# manually edit prepchg_edit.txt

# mostly {#<ab>
python prepchg2.py AP57_AB_v3.txt prepchg2.txt
cp prepchg2.txt prepchg2_edit.txt
# manually edit prepchg2_edit.txt

python ../updateByLine.py AP57_AB_v3.txt prepchg_edit.txt temp_abv3a.txt
python ../updateByLine.py temp_abv3a.txt prepchg2_edit.txt temp_abv3b.txt

python v3_v3a.py temp_abv3b.txt AP57_AB_v3a.txt

cd ../
# install local displays using v3a
sh redo_ap.sh temp_ABuploads/AP57_AB_v3a.txt apABv3a

python ../diff_to_changes_dict.py AP57_AB_v3.txt AP57_AB_v3a.txt ../change_v3_v3a.txt
1777 changes written to ../change_v3_v3a.txt

* ==============================================
* AP57_AB_v3b.txt
cd temp_ABuploads

cp AP57_AB_v3a.txt AP57_AB_v3a1.txt


# manually Apply change_20251216_20260112.txt to  AP57_AB_v3a1.txt
  [these are changes made to csl-orig since the version
   prior to AB's download]
 see change_20251216_20260112_notes.txt

# temporary display install and check
cd ../
sh redo_ap.sh temp_ABuploads/AP57_AB_v3a1.txt apABv3a1
# ok -- installs without error

# generate changes 
python ../diff_to_changes_dict.py AP57_AB_v3a.txt AP57_AB_v3a1.txt ../change_v3a_v3a1.txt
9 changes written to ../change_v3a_v3a1.txt


