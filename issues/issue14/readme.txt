
Begin 04-01-2026 Activate link targs

 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home

* tempwork/ap_0.txt start with this revision of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git log | head -n 1
# commit d18d2c4dc9652c76a44f8a134fecc56893bbf673


git show d18d2c4d:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/tempwork/ap_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/


* ==========================================
* Printed abbreviations of names of works or authors:
https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/_static/ap57_vol1_frontmatter.pdf


* tempwork/tooltips_0.txt 
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork/apauth/tooltip.txt tooltips_0.txt

wc -l tempwork/tooltips_v0.txt
# 269
* tooltips_1.txt
cp tempwork/tooltips_0.txt tooltips_1.txt
manual changes to tooltips_1.txt

sort tooltips by 2nd field
sort -t $'\t' -k2,2n tooltips_1.txt > tooltips_1a.txt

* tempwork/basicadjust.php
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php tempwork/basicadjust.php

* lsextract_all.txt for pwg  find exec
/c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue94/lsextract_all.txt
@  frequency of all pwg references As of 2025-08-31
python lsextract_all.py temp_pwg_0.txt pwgbib_input.txt lsextract_all.txt
** how to find
cd /c/xampp/htdocs/sanskrit-lexicon/PWG
 find . -type f -name "*.txt" -exec grep -n "GORR" {} + > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/tempwork/temp.txt

cd /c/xampp/htdocs/sanskrit-lexicon/PWG

** find python files in some directory
 find . -type f -name "*.py"  all python files
** pwg
cd /c/xampp/htdocs/sanskrit-lexicon/PWG
 find . -type f -name "*.txt" > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/tempwork/txtfiles_pwg.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
wc -l tempwork/txtfiles_pwg.txt
# 3191 tempwork/pyfiles_pwg.txt

* lsextract_all_1.txt for ap using tooltips_1.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
python lsextract_all.py ap tempwork/ap_0.txt tooltips_1.txt lsextract_all_1.txt tempwork/lsunknowns_1.txt

269 tooltips from tooltips_1.txt
write_tips Output in  lsextract_all_1.txt
3730 unknown ls written to tempwork/lsunknowns_1.txt

* lsextract_all_2.txt for ap using tooltips_2.txt (authtips/auth_tooltips.txt)
cp authtips/auth_tooltips.txt tooltips_2.txt

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
python lsextract_all.py ap tempwork/ap_0.txt tooltips_2.txt lsextract_all_2.txt tempwork/lsunknowns_2.txt

268 tooltips from tooltips_2.txt
3314 unknown ls written to tempwork/lsunknowns_2.txt

* tooltips_1a.txt  (edits to tooltips_1.txt)
** additions:
Rv.	Ṛigveda, (Pandita Satawalekar and V. S. Mandala, Poona).
Rv. Pr.	Ṛigveda Prātiśākhya.
** deletions:
Ṛv.	Ṛgveda, (Pandita Satawalekar and V. S. Mandala, Poona).
Ṛv. Pr.	Ṛgveda Prātiśākhya.
** changes:
*** ---
old: 
T. UP.	Taittirīya Upaniṣad.
new:
T. Up.	Taittirīya Upaniṣad.
*** ---
old:
Śanti.	Śāntiśataka.
new:
Śānti.	Śāntiśataka.
*** ---
old:
Chān.	Chāṇakyaśataka.
new:
Chāṇ.	Chāṇakyaśataka.
*** ---
old:
Chat.	Chātakāṣṭaka (In two parts.)
new:
Chāt.	Chātakāṣṭaka (In two parts.)
*** ---
old:
A. L.	Ānandalaharī.
new:
Ā. L.	Ānandalaharī.

*** ---
old:
Ghat.	Ghatakarparakāvya.
new:
Ghaṭ.	Ghaṭakarparakāvya.

*** ---
old:
Bhar. Ch.	Bhāratachampū, (Bombay).
new:
Bhār. Ch.	Bhāratachampū, (Bombay).
*** ---
old:
Day.	Dayabhāga.
Day. B.	Dayabhāga.
new:
Dāy.	Dāyabhāga.
Dāy. B.	Dāyabhāga.

*** ---
old:
Bṛ. Ar. Up.	Bṛhadāraṇyakopaniṣad, (सार्थ उपनिषत्संग्रह, ह. र. भागवत, १९१४).
new:
Bṛ. Ar. Up.	Bṛhadāraṇyakopaniṣad, (सार्थ उपनिषत्संग्रह, ह. र. भागवत, १९१४).

* lsextract_all_1a.txt for ap using tooltips_1a.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
python lsextract_all.py ap tempwork/ap_0.txt tooltips_1a.txt lsextract_all_1a.txt tempwork/lsunknowns_1a.txt

269 tooltips from tooltips_1a.txt
1954 unknown ls written to tempwork/lsunknowns_1a.txt

* tooltips_2a.txt (edits to tooltips_2.txt
** additions:
P. R.	Prasannarāghava.
Rāj. T.	Rājataraṅgiṇī.
Dṛ. Ś.	Dṛstāntaśataka.
** deletions
** changes:
*** ----
old: 
Bṛi. Ār. Up.	Bṛhadāraṇyakopaniṣad, (सार्थ उपनिषत्संग्रह—ह. र. भागवत, १९१४).
Bṛi. Up.	Bṛhadāraṇyakopaniṣad, (सार्थ उपनिषत्संग्रह—ह. र. भागवत, १९१४).
new:
Bṛ. Ār. Up.	Bṛhadāraṇyakopaniṣad, (सार्थ उपनिषत्संग्रह—ह. र. भागवत, १९१४).
Bṛ. Up.	Bṛhadāraṇyakopaniṣad, (सार्थ उपनिषत्संग्रह—ह. र. भागवत, १९१४).
*** ---
old:
Subhas.	Subhāṣita.
new:
Subhāṣ	Subhāṣita.
---

*** ---
old:
Vas.	Vāsavadattā, (Nirṇaya Sāgara, 1940).
new:
Vās.	Vāsavadattā, (Nirṇaya Sāgara, 1940).
*** ---
old:
Īsop.	Īśopaniṣad,
new:
Īśop.	Īśopaniṣad,

*** ---
old:
Bhav.P.	Bhaviṣyottara Purāṇa.
new:
Bhav. P.	Bhaviṣyottara Purāṇa.

*** ---
old:
Bri. Kath.	Bṛihatkathā.
new:
Bṛ. Kath.	Bṛihatkathā.

*** ---
old:
C P.	Copper‑plates.
new:
CP.	Copper‑plates.
* lsextract_all_2a.txt for ap using tooltips_2a.txt
python lsextract_all.py ap tempwork/ap_0.txt tooltips_2a.txt lsextract_all_2a.txt tempwork/lsunknowns_2a.txt

271 tooltips from tooltips_2a.txt
2000 unknown ls written to tempwork/lsunknowns_2a.txt

** 
* tooltips_3.txt  (edits to tooltips_2a.txt) and ap_1
cp tooltips_2a.txt tooltips_3.txt
manual edit tooltips_3.txt
cp tempwork/ap_0.txt tempwork/ap_1.txt
# manual edit ap_1
See readme_tooltips_3.txt for notes on changes

* lsextract_all_3.txt for ap using tooltips_3.txt and ap_1
# write_tips Output in  lsextract_all_3.txt  sorted reverse order by counts.
python lsextract_all.py ap tempwork/ap_1.txt tooltips_3.txt lsextract_all_3.txt tempwork/lsunknowns_3.txt

270 tooltips from tooltips_3.txt
1478 unknown ls written to tempwork/lsunknowns_3.txt

# write_tips Output in  lsextract_all_3.txt sorted by tooltip
python lextract_all_sort_iast.py lsextract_all_3.txt lsextract_all_3_sort_iast.txt
* install tooltips_3.txt and ap_1.txt
** DONE local install
cp tooltips_3.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork/apauth/tooltip.txt 
cp tempwork/ap_1.txt  /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ap  ../../ap
** DONE push csl-orig to github
/c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "AP: minor ls adjustments.
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push

** DONE push csl-pywork to github
/c/xampp/htdocs/cologne/csl-pywork/
git add .
git commit -m "AP: Edits of ap ls tooltips
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push
** TODO push this repo, and make comment

* TODO  Install at Cologne
* TODO comment at https://github.com/sanskrit-lexicon/AP/issues/14

* lsdump_abbrv.py
python lsdump_abbrv.py 'Rv.' ap tempwork/ap_0.txt tooltips_1a.txt  tempwork/lsdump_1a.txt
1498 of abbrev "Rv." written to tempwork/lsdump_1a.txt

python lsdump_abbrv.py 'Rv.' ap tempwork/ap_0.txt tooltips_2.txt  tempwork/lsdump_2.txt
1492 of abbrev "Rv." written to tempwork/lsdump_2.txt

* /c/xampp/htdocs/sanskrit-lexicon-scans/_jimnotes/

* ---------------------------------------
* csl-orig git_pull  04-17-2026
 v02/ae/ae.txt   |  2 +-
 v02/ap/ap.txt   | 42 ++++++++++++++++++++++++++++++------------
 v02/lrv/lrv.txt |  2 +-
 v02/pw/pw.txt   |  2 +-
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ae  ../../ae
sh xmlchk_xampp.sh ae
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
sh generate_dict.sh lrv  ../../lrv
sh xmlchk_xampp.sh lrv
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw

# check by local install
cd csl-py
* tooltips_5.txt and change to ap.txt

BEGIN 04-15-2026  further edits re Andhrabharati comment
see ls_andhrabharati/readme.txt 
tooltips_5.txt copied from ls_andhrabharati/tooltips_5.txt

** 1 change to tempwork/ap_1.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt tempwork/ap_1.txt

 <L>16848.308<pc>0791-1<k1>trimaDu<k2
old: 
three verses of the Ṛgveda (<ls n="Ṛv.">1. 90. 6-8</ls>
new:
three verses of the Ṛgveda (<ls n="Rv.">1. 90. 6-8</ls>

* install tooltips_5.txt and tempwork/ap_1.txt at githib
** DONE local install
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home

cp tooltips_5.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork/apauth/tooltip.txt 
cp tempwork/ap_1.txt  /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok
** DONE push csl-orig to github
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "AP: change one 'Ṛv.' to 'Rv.'
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push

** DONE push csl-pywork to github
cd /c/xampp/htdocs/cologne/csl-pywork/
git add .
git commit -m "AP: Edits of ap ls tooltips. tooltips_5.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push
* DONE  Install at Cologne
* push this repo, and make comment

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
git pull
# Already up to date
git add .
git commit -m "Revise ls abbrev-tooltips by comparison with Andhrabharati version. #14"
git push

* lsextract_all_5.txt for ap using tooltips_5.txt and current ap.txt
# write_tips Output in  lsextract_all_5.txt  sorted reverse order by counts.
cp /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt tempwork/ap_2.txt
python lsextract_all.py ap tempwork/ap_2.txt tooltips_5.txt lsextract_all_5.txt lsunknowns_5.txt

270 tooltips from tooltips_5.txt
1360 unknown ls written to lsunknowns_5.txt

# write_tips Output in  lsextract_all_5.txt sorted by tooltip
python lextract_all_sort_iast.py lsextract_all_5.txt lsextract_all_5_sort_iast.txt
* push this repo
git pull
git add .
git commit -m "lsextract files using tooltips_5 #14"
git push

* 04-23-2026
* tooltips_6.txt and change to ap.txt

BEGIN 04-23-2026  
see lsunknown/readme.txt for construction of tooltips_6.txt


* install tooltips_6.txt and lsunknown/temp_ap_0.txt at githib
** DONE local install
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
cp tooltips_6.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork/apauth/tooltip.txt 
cp lsunknown/temp_ap_0.txt  /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok
** DONE push csl-orig to github
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "ap - minor changes related to tooltips_6.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push

** DONE push csl-pywork to github
cd /c/xampp/htdocs/cologne/csl-pywork/
git add .
git commit -m "AP: Edits of ap ls tooltips. tooltips_6.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push

** DONE update cologne
* lsextract_all_6.txt for ap using tooltips_6.txt and current ap.txt
# write_tips Output in  lsextract_all_6.txt  sorted reverse order by counts.
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
cp /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt tempwork/ap_3.txt
python lsextract_all.py ap tempwork/ap_3.txt tooltips_6.txt lsextract_all_6.txt lsunknowns_6.txt

352 tooltips from tooltips_6.txt
970 unknown ls written to lsunknowns_6.txt

(- 1360 970)
270 tooltips from tooltips_6.txt
1360 unknown ls written to lsunknowns_6.txt

# write_tips Output in  lsextract_all_6.txt sorted by tooltip
python lextract_all_sort_iast.py lsextract_all_6.txt lsextract_all_6_sort_iast.txt
* push this repo
git pull
git add .
git commit -m "lsextract files using tooltips_6 #14"
git push

* ----------------------------------------
* 'ch' changes 04-26-2026 tooltips_7 and change to ap.txt
mkdir chwork   Iast spelling consistency.
See chwork/readme.txt for changes made to tooltips_7.txt
 revised chwork/temp_ap_1.txt
* install tooltips_7.txt and chwork/temp_ap_1.txt at githib
** DONE local install
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
cp tooltips_7.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork/apauth/tooltip.txt 
cp chwork/temp_ap_1.txt  /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok
** DONE push csl-orig to github
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "ap - iast spelling changes,  tooltips_7.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push

** DONE push csl-pywork to github
cd /c/xampp/htdocs/cologne/csl-pywork/
git add .
git commit -m "AP: Edits of ap ls tooltips. tooltips_7.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/14"
git push

** DONE update cologne
 csl-orig, csl-pywork
 regen dictionaries ap, bor, lrv, mw

* lsextract_all_7.txt for ap using tooltips_7.txt and current ap
# write_tips Output in  lsextract_all_7.txt  sorted reverse order by counts.
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14 #home
python lsextract_all.py ap chwork/temp_ap_1.txt tooltips_7.txt lsextract_all_7.txt lsunknowns_7.txt

352 tooltips from tooltips_7.txt
970 unknown ls written to lsunknowns_7.txt


# write_tips Output in  lsextract_all_7.txt sorted by tooltip
python lextract_all_sort_iast.py lsextract_all_7.txt lsextract_all_7_sort_iast.txt
* push this repo
git pull
git add .
git commit -m "lsextract files using tooltips_7 #14"
git push

* THE END


