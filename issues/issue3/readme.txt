
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
* AP57_AB_v3a1.txt  changes since
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
* AP57_AB_v3a2.txt  M + space + vowel -> m + space + vowel
cd temp_ABuploads

cp AP57_AB_v3a1.txt AP57_AB_v3a2.txt

# manually Apply changes to Sanskrit text
"M a" -> "m a" 32
"M A" -> "m A"  3
"M i" -> "m i"  5
"M I" -> "m I"  0
"M u" -> "m u"  1
"M U" -> "m U"  1
"M f" -> "m f"  3
"M F" -> "m F"  0
"M x" -> "m x"  0
"M X" -> "m X"  0
"M e" -> "m e"  2
"M E" -> "m E"  0
"M o" -> "m o"  0
"M O" -> "m O"  0
               47

# temporary display install and check
cd ../
sh redo_ap.sh temp_ABuploads/AP57_AB_v3a2.txt apABv3a2
# ok -- installs without error

# generate changes 
cd temp_ABuploads
python ../diff_to_changes_dict.py AP57_AB_v3a1.txt AP57_AB_v3a2.txt ../change_v3a1_v3a2.txt
46 changes written to ../change_v3a_v3a2.txt  (line changes)

* AP57_AB_v3b.txt  Handle '%% xxx' (remove/insert lines)
cd temp_ABuploads

cp AP57_AB_v3a2.txt AP57_AB_v3b.txt
# manually edit AP57_AB_v3b.txt and make changes:
1. delete-matching lines %%empty line (to be deleted)
 1528 lines deleted.
 There remain 4 lines containing '%%'
2. Delete two other lines = "%%" 
3. two lines: <LEND>%%insert one empty line next
   add empty line after <LEND>

# temporary display install and check
cd ../
sh redo_ap.sh temp_ABuploads/AP57_AB_v3b.txt apABv3b
# ok -- installs without error

# diff
cd temp_ABuploads
diff AP57_AB_v3a2.txt AP57_AB_v3b.txt > ../diff_v3a2_v3b.txt
wc -l ../diff_v3a2_v3b.txt
3207 (lines in diff

* =====================================================
* installation of AP57_AB_v3b.txt
# install AP57_AB_v3b.txt in csl-orig
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home
cp temp_ABuploads.txt/AP57_AB_v3b.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home
-----------------------------
# sync csl-orig to github:

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: AP57_AB_v3b.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/3"
#  1 file changed, 85280 insertions(+), 86808 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home

-----------------------------
# sync csl-pywork to github 

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "add <sab> element to one.dtd.
Ref: https://github.com/sanskrit-lexicon/AP/issues/3"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/  # home

-----------------------------
# sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
csl-pywork #pull

---------------
# update displays for ap
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

* =====================================================
* Further analysis
* global
# 
mkdir global

global/ap_global_san.txt from
https://github.com/sanskrit-lexicon/csl-corrections/blob/master/batches/20251126/dictionaries/ap/ap_global_san.txt
There are 26 change patterns (for sanskrit text) 
Added 
cd global
python globcheck.py ap_global_san.txt ../temp_ABuploads/AP57_AB_v3a1.txt globcheck_v3a1.txt

* AB doc on some changes

