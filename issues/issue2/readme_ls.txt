
AP/issues/issue2/readme.txt

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2  # work directory

Install ls abbreviations.

-----------------------------------------
* AP57.list.of.sources.as.printed.txt
 start with this file.
 (ref:https://github.com/sanskrit-lexicon/AP/issues/2#issuecomment-3822507497)

Format is a X<TAB>TOOLTIP2-column file (tab-delimited)

a few comments have no tab and can be skipped

-----------------------------------------
* apls_input.txt

python make_apls.py AP57.list.of.sources.as.printed.txt apls_input.txt

==============================================================
In csl-pywork repo,  generate apauth folder:
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork
# start with a copy of ap90auth folder
cp -r ../../ap90/pywork/ap90auth apauth
cd apauth
# replace ap90 with ap in several files
sed -i 's/ap90/ap/g' readme.org
sed -i 's/ap90/ap/g' redo.sh
sed -i 's/ap90/ap/g' tooltips.sql

# copy apls_input.txt 
cp /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/apls_input.txt tooltip.txt

# test the construction
sh redo.sh

========================
modify files in csl-pywork local repo:
 modify csl_ptwork/v02/inventory.txt
old:
; -- literary sources: ap90, ben, sch, gra, bhs
; These have the simpler format ABBREV<TAB>TIP
; --------------------------------------------------------------
ben ap90 sch gra bhs:pywork/${dictlo}auth/redo.sh:CD
ben ap90 sch gra bhs:pywork/${dictlo}auth/readme.org:CD
ben ap90 sch gra bhs:pywork/${dictlo}auth/tooltip.txt:CD
ben ap90 sch gra bhs:pywork/${dictlo}auth/tooltips.sql:CD

new:
; -- literary sources: ap90, ben, sch, gra, bhs, ap
; These have the simpler format ABBREV<TAB>TIP
; --------------------------------------------------------------
ben ap90 sch gra bhs ap:pywork/${dictlo}auth/redo.sh:CD
ben ap90 sch gra bhs ap:pywork/${dictlo}auth/readme.org:CD
ben ap90 sch gra bhs ap:pywork/${dictlo}auth/tooltip.txt:CD
ben ap90 sch gra bhs ap:pywork/${dictlo}auth/tooltips.sql:CD

------------------------
cd /c/xampp/htdocs/cologne/csl-pywork
 modify csl_pywork/v02/makotemplates/pywork/redo_postxml.sh
old:
# literary source.
%if dictlo in ['mw','pw','pwg','ap90','ben','pwkvn','sch','gra','bhs']:
new:
# literary source.
%if dictlo in ['mw','pw','pwg','ap90','ben','pwkvn','sch','gra','bhs','ap']:

------------------------
modify csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
Modify in three places:
---- 1) 
old:
  }else if (in_array($dict,array('mw','ap90','ben','sch','gra','bhs'))){
   $this->dal_auth = new Dal($dict,"authtooltips");

new:
  }else if (in_array($dict,array('mw','ap90','ben','sch','gra','bhs','ap'))){
   $this->dal_auth = new Dal($dict,"authtooltips");

---- 2) 
old:
   dbgprint($dbg,"ls_matchabbr returns: cid=$cid, code=$code, title=$title, type=$type\n");
  } else if (in_array($this->dict,array('ap90','ben','sch','gra','bhs'))) {
   list($code,$text) = $rec;

new:
   dbgprint($dbg,"ls_matchabbr returns: cid=$cid, code=$code, title=$title, type=$type\n");
  } else if (in_array($this->dict,array('ap90','ben','sch','gra','bhs', 'ap'))) {
   list($code,$text) = $rec;

---- 3)
old:
 }else if (in_array($this->getParms->dict,
           array('mw','ap90','ben','sch','gra','bhs'))){
  //dbgprint(true,"before ls_callback_mw: $line\n");
new:
 }else if (in_array($this->getParms->dict,
           array('mw','ap90','ben','sch','gra','bhs','ap'))){
  //dbgprint(true,"before ls_callback_mw: $line\n");

------------------------
# modify csl-apidev
# copy files from csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02/
sh apidev_copy.sh

========================

Do a local install of ap: do ls abbreviations show tooltips?


cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

Now, in cdsl displays, tooltips are available for the literary references
<ls>X</ls> forms, supposing X starts with an abbreviation in the printed list from
scan of 'ap'.

====================================================
Installation

----------------------------------------------------
# sync csl-pywork to github 
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "ap: Activate ls tooltips 
Ref: https://github.com/sanskrit-lexicon/AP/issues/2"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

----------------------------------------------------
# sync csl-websanlexicon to github 
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "ap: Activate ls tooltips 
Ref: https://github.com/sanskrit-lexicon/AP/issues/2"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

----------------------------------------------------
# sync csl-apidev to github 
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "ap: Activate ls tooltips 
Ref: https://github.com/sanskrit-lexicon/AP/issues/2"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

-----------------------------
# sync to Cologne, pull changed repos, redo display
---------------
ssh login to Cologne
cd csl-pywork #pull
cd csl-csl-websanlexicon #pull
cd csl-apidev #pull

---------------
# update displays for ap
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

--------------
# sync this issue to github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

git pull
git add .
git commit -m "ap: Activate ls tooltips 
Ref: https://github.com/sanskrit-lexicon/AP/issues/2"
git push
======================================================

Revise apauth/tooltip.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/2#issuecomment-3827450873
    and following comment
    
Edit /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork/apauth/tooltip.txt
1. '{#' -> '',  and '#}' -> ''   (remove {#...#} tagging inside the ls tooltips)
2. "Śāraṅgdhara Samhitā" -> "Śāraṅgadhara Samhitā"  (incidentally, this is a print change

-----------------------------------------
local install of revised displays:

cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

----------------------------------------------------
# sync csl-pywork to github 
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "ap: edits to ls tooltips
Ref: https://github.com/sanskrit-lexicon/AP/issues/2#issuecomment-3827450873"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

-----------------------------
# sync to Cologne, pull changed repos, redo display
---------------
ssh login to Cologne
cd csl-pywork #pull

# update displays for ap
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

# sync this issue to github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

git pull
git add .
git commit -m "ap: Activate ls tooltips 
Ref: https://github.com/sanskrit-lexicon/AP/issues/2"
git push

