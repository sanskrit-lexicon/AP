
https://github.com/sanskrit-lexicon/AP/issues/5
  Generate new version of ap.txt to have hard-coded Devanagari
  in some ls elements.

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home

---------------------------------
* AB_table.txt
 from https://github.com/sanskrit-lexicon/AP/issues/5#issuecomment-3793831448

49 lines, text of  an ls element such as
 <ls>Bil. Ch. ({#uttarapIWikA#}) 38</ls>

Devanagari coded as {#X#}

--------------------------------------
* change_v3_v3a.txt
 
copied from 
https://github.com/sanskrit-lexicon/AP/blob/main/issues/issue3/change_v3_v3a.txt

* ======================================================================
Next, we prepare temp_ap_0.txt as latest version of csl-orig/v02/ap/ap.txt
* revised git history of ap.txt,
  so we can know the csl-orig commit for the latest change in ap.txt
cd /c/xampp/htdocs/cologne/csl-orig
 git log --follow --pretty=format:"%ad %h %an %s" --date=short -- v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/temp_ap_history.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home
wc -l temp_ap_history.txt

head -n 1 temp_ap_history.txt
2026-01-17 93e2718 funderburkjim AP: AP57_AB_v3b.txt correction Ref: https://github.com/sanskrit-lexicon/AP/issues/3

--------------
# temp_ap_0.txt
cd /c/xampp/htdocs/cologne/csl-orig
git show 93e2718:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/temp_ap_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home

* ======================================================================

* extract
python extract_changes.py change_v3_v3a.txt AB_table.txt  extract_changes.txt

49 table records
0 duplicates in AB_table.txt (49 in table)
1777 groups
SKIPPING ls=<ls>{#alaMkAraSeKara 6#}</ls>, # change recs = 0
SKIPPING ls=<ls>{#hEmaH#}</ls>, # change recs = 0
SKIPPING ls=<ls>{#mala˚ ta˚#}</ls>, # change recs = 0
SKIPPING ls=<ls>{#medinI#} 1. 65</ls>, # change recs = 0
225 lines written to extract_changes.txt

------------------------------------
cp extract_changes.txt extract_changes_1.txt
manually edit extract_changes_1.txt
  add line to each group,
   have the corresponding IAST form of each <ls>.

---------------------
extract_changes_2.txt 

transcode change.slp1 to change.deva

python extract_deva.py extract_changes_1.txt extract_changes_2.txt
315 lines written to extract_changes_2.txt

Note on transcoding.
the transcoding file slp1_deva.xml is taken from
a revised slp1_deva.xml taken from
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva.xml transcoder/slp1_deva.xml

See: https://github.com/sanskrit-lexicon/csl-websanlexicon/issues/55

devanagari abbreviation sign = ॰
---------------

# extract_changes_3.txt is a legitimate change file.

python extract_linenum.py temp_ap_0.txt extract_changes_2.txt extract_changes_3.txt
408 lines written to extract_changes_3.txt
-------------------
# temp_ap_1.txt

python updateByLine.py temp_ap_0.txt extract_changes_3.txt temp_ap_1.txt

-------------------
change_1_2.txt
 Constructed manually from AB_table_a.txt
 Based on https://github.com/sanskrit-lexicon/AP/issues/5#issuecomment-3796040622
-------------------
# temp_ap_2.txt

python updateByLine.py temp_ap_1.txt change_1_2.txt temp_ap_2.txt
5 change transactions from change_1_2.txt

------------------
# + change_ap_0_2.txt   all changes so far
python diff_to_changes_dict.py temp_ap_0.txt temp_ap_2.txt change_ap_0_2.txt
51 changes written to change_ap_0_2.txt

------------------
# diff_ap_0_2.txt
diff temp_ap_0.txt temp_ap_2.txt > diff_ap_0_2.txt

wc -l diff_ap_0_2.txt
202 diff_ap_0_2.txt

====================================
READY TO INSTALL 

# install temp_ap_2.txt in csl-orig
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home
cp temp_ap_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home

-----------------------------
# sync csl-orig to github:

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: hard-code devanagari in ls elements
Ref: https://github.com/sanskrit-lexicon/AP/issues/5"
#  1 file changed, 51 insertions(+), 51 deletions(
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home

-----------------------------
# sync csl-websanlexicon to github 

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "Devanagari Abbreviation transcoding
Ref: https://github.com/sanskrit-lexicon/csl-websanlexicon/issues/55"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home

 =====================================================

-----------------------------
# sync to Cologne, pull changed repos, redo display
---------------
cd csl-orig #pull
cd csl-websanlexicon #pull

---------------
# update displays for ap
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

=====================================================
# update this repo
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home
git pull
git add .
git commit -m "AP hard-code devanagari in ls elements
Ref: https://github.com/sanskrit-lexicon/AP/issues/5"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue5/  # home

=====================================================
THE END
