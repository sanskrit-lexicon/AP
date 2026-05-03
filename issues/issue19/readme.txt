
Begin 04-18-2026 Activate link targs

 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue19 #home

* tempwork/ap.txt, pwg.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git log | head -n 1
# commit 6fff4c58b6389ef21ca5bfdcb842045fde8b5567

git show 6fff4c58:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue19/tempwork/ap.txt

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue19/

* tooltips for pwg
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt tempwork/pwgbib_input.txt
# 
#  lsextract_all.txt for pwg

python ../issue14/lsextract_all.py pwg tempwork/pwg.txt tempwork/pwgbib_input.txt tempwork/lsextract_all_pwg.txt tempwork/lsunknowns_pwg.txt

# 
cp ../issue14/lsextract_all.py .
cp ../issue14/sort_iast.py .
cp ../issue14/lextract_all_sort_iast.py .
cp ../issue14/lsdump_abbrv.py .

# add dbg statement in lsextract_all.py
# rerun
python lsextract_all.py pwg tempwork/pwg.txt tempwork/pwgbib_input.txt tempwork/lsextract_all_pwg.txt tempwork/lsunknowns_pwg.txt
2844 tooltips from tempwork/pwgbib_input.txt

python lextract_all_sort_iast.py tempwork/lsextract_all_pwg.txt tempwork/lsextract_all_pwg_sort_iast.txt
---------------------------------------------------------
AP  ../issue14/lsextract_all_6.txt -> tempwork_lsextract_all_6.txt
PWG tempwork/lsextract_all_pwg.txt -> tempwork_lsextract_all_pwg.txt

================================================
* TODO link_target_work.txt and readme_pwg_linktargets.txt
  provide description
* prepare to install
cd /c/xampp/htdocs/cologne/csl-orig/
git pull # (52 files changed) 200000+ lines changed
# already up to date
 csl-pywork, csl-websanlexicon, csl-apidev, hwnorm1, hwnorm2

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue19 #home
* ==========================================
* Note on ap90
Links have been checked for ap.txt.
basicadjust in function ls_callback_ap90_href is 
 - active for ap.txt.  
 - inactive for ap90. 
   Probably the same links will work for ap90.txt.
   But cheching ap90 links needs to be done.

* ===========================================
* installation Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue19 #home
cp basicadjust_new.php /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
cp basicadjust_new.php /c/xampp/htdocs/cologne/csl-apidev/basicadjust.php

# make local displays for ap, and check xml
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# make local displays for ap90, and check xml
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap90  ../../ap90
sh xmlchk_xampp.sh ap90
# csl-websanlexicon to github
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "AP: link targets. 
Ref: https://github.com/sanskrit-lexicon/AP/issues/19"
git push
# csl-apidev to github
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "AP: link targets. 
Ref: https://github.com/sanskrit-lexicon/AP/issues/19"
git push
* TODO installation cologne  : Cannot connect to cologne!
# connect to cologne and change to scans directory
cd csl-orig
git pull
cd ../csl-websanlexicon
git pull
cd ../csl-apidev
git pull
cd
* push this repo
