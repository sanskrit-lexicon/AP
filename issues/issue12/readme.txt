
Begin 03-21-2026 Alternate headwords and compounds

 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12 #home

* ==========================================
* tempwork/ap_0.txt start with this revision of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git log | head -n 1
# commit 6b17a5a7c60579cdbeb213428fe0f1fadc583971

git show 6b17a5a7:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12/tempwork/ap_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12/
* ==========================================
* tempwork/ap_0a.txt
cp tempwork/ap_0.txt tempwork/ap_0a.txt
5 matches for ".\.{@{#" in buffer: ap_0.txt
  Revise so these bold-devanagari strings start at beginning of line
# manual edit tempwork/ap_0a.txt
python diff_to_changes_dict.py tempwork/ap_0.txt tempwork/ap_0a.txt change_ap_0_0a.txt
14 changes written to change_ap_0_0a.txt
* ==========================================
* tempwork/ap_0b.txt
cp tempwork/ap_0a.txt tempwork/ap_0b.txt

# manual edit tempwork/ap_0b.txt
python diff_to_changes_dict.py tempwork/ap_0a.txt tempwork/ap_0b.txt change_ap_0a_0b.txt
38 changes written to change_ap_0a_0b.txt

* compounds_0b.txt and tempwork/ap_1_0b.txt

python compounds.py tempwork/ap_0b.txt temp_compounds_0b.txt tempwork/ap_1_0b.txt
339763 read from tempwork/ap_0b.txt
# compound groups=4454
ncomp=4454
4454 entries from tempwork/ap_0b.txt
34182 lines written to temp_compounds_0b.txt
461675 lines written to tempwork/ap_1_0b.txt

* althws_input.txt
Construct this from ../issue9/prep1_2.txt 
python althws_input.py ../issue9/prep1_2.txt althws_input.txt

Make one manual change to althws_input.txt
  delete line '12793:kftvA:'
due to erroneous line of prep1_2.txt
yz:0,0:12793:kftvA:kftvAcintA:

prep1_2.txt format 5 fields:
code not of interest
n1n2 not of interest
L  cologne id
k1 cologne headword
header not of interest
althws_str  comma delimited list of alternate headwords 

althws_input.txt format
L
k1
althws_str
* tempwork/ap_2_0b.txt 
constructed by althws.py
python althws.py tempwork/ap_1_0b.txt althws_input.txt tempwork/ap_2_0b.txt
* ==========================================
* tempwork/ap_0c.txt
cp tempwork/ap_0b.txt tempwork/ap_0c.txt
1. Change re jawa/ so cpds based on jawA
2. -paYcASat as compound of trayas

manual edit tempwork/ap_0c.txt
diff tempwork/ap_0b.txt tempwork/ap_0c.txt > change_0b_0c_diff.txt
38 lines in diff

* compounds_0c.txt and tempwork/ap_1_0c.txt

python compounds.py tempwork/ap_0c.txt temp_compounds_0c.txt tempwork/ap_1_0c.txt
339763 read from tempwork/ap_0c.txt
# compound groups=4454
ncomp=4454
4454 entries from tempwork/ap_0c.txt
34182 lines written to temp_compounds_0c.txt
461675 lines written to tempwork/ap_1_0c.txt

* tempwork/ap_2_0c.txt
python althws.py tempwork/ap_1_0c.txt althws_input.txt tempwork/ap_2_0c.txt
* tempwork/ap_3_0c.txt
# Compounds have been marked <e>2 in metalines.
# add <e>1 to other metalines
python meta_e.py tempwork/ap_2_0c.txt tempwork/ap_3_0c.txt
* ==========================================
* procedure to regenerate ap_3_0c.txt from ap_0c.txt and althws_input.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12 #home
# make temp_compounds_0c.txt tempwork/ap_1_0c.txt
python compounds.py tempwork/ap_0c.txt temp_compounds_0c.txt tempwork/ap_1_0c.txt
# make tempwork/ap_2_0c.txt  alt headwords 
python althws.py tempwork/ap_1_0c.txt althws_input.txt tempwork/ap_2_0c.txt
# add <e>1 to other metalines
python meta_e.py tempwork/ap_2_0c.txt tempwork/ap_3_0c.txt
# generate local displays
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12 #home
cp tempwork/ap_3_0c.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12/  # home

* ==========================================
* procedure to regenerate ap_3_1_0c.txt from ap_0c.txt and althws_input.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12 #home
# make compounds_1_0c.txt  (for evaluation -- not used further)
# tempwork/ap_1_1_0c.txt   ('final' version of ap.txt)
#    uses compounds1.py (sandhi slightly different from compounds.py)
python compounds1.py tempwork/ap_0c.txt compounds_1_0c.txt tempwork/ap_1_1_0c.txt
# make tempwork/ap_2_1_0c.txt  alt headwords 
python althws.py tempwork/ap_1_1_0c.txt althws_input.txt tempwork/ap_2_1_0c.txt
# add <e>1 to other metalines
python meta_e.py tempwork/ap_2_1_0c.txt tempwork/ap_3_1_0c.txt
# generate local displays
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12 #home
cp tempwork/ap_3_1_0c.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12/  # home


* ==========================================
* INSTALL csl-orig, csl-pywork, csl-apidev at Github, in several steps
* ==========================================
* check csl-orig for pull
cd /c/xampp/htdocs/cologne/csl-orig
git status
git restore v02/ap/ap.txt
git status
# nothing to commit
git pull
# Already up to date.
# return home
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12 #home
* save zipped version of ap_0c.txt
zip ap_0c.zip tempwork/ap_0c.txt
# For potential further use If we wanted to 'revert'

* 03-28-2026 install tempwork/ap_3_1_0c.txt at Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12/  # home
cp tempwork/ap_3_1_0c.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
# 1 file changed, 209758 insertions(+), 75650 deletions(-)
git commit -m "AP: compounds and alternate headwords
Ref: https://github.com/sanskrit-lexicon/AP/issues/12"

git push
git log | head -n 1
# commit 4025ddbe9cb445b8b73cd2dac453f70bdad6d14e
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12/  # home

---------------------------
* install revised csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
# Already up to date
git add .
git commit -m "AP pywork: compounds and alternate headwords
Ref: https://github.com/sanskrit-lexicon/AP/issues/12"
#  4 files changed, 12 insertions(+), 8 deletions(-)
git push

* install revised csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git pull
# Already up to date
git add .
git commit -m "AP listhierClass.php: compounds and alternate headwords
Ref: https://github.com/sanskrit-lexicon/AP/issues/12"
# 1 file changed, 5 insertions(+), 1 deletion(-)
git push

* ==========================================
* INSTALL Cologne csl-orig, csl-pywork, csl-apidev

** sync Cologne to github for csl-orig, csl-apidev, csl-pywork
# connect to cologne.
# pull repos
cd csl-orig
git pull
cd ../csl-pywork/
git pull
cd ../csl-apidev
git pull
# regenerate displays for AP
cd ../csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
* sync this repo to Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12
git add .
git commit -m "AP: compounds and alternate headwords
Ref: https://github.com/sanskrit-lexicon/AP/issues/12"
git push

* ==========================================
* Update hwnorm1 and csl-apidev repos
# See readme_hwnorm1.txt for details
* THE END

