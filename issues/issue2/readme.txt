
AP/issues/issue2/readme.txt

Install abbreviations.

* AP57.printed.abbrs.txt
 start with this file.
 (ref: https://github.com/sanskrit-lexicon/AP/issues/2#issuecomment-3793826888)

* apab_input.txt
use ap90ab_input.txt as a model
Most cdsl koshas have their input file to have the ap90ab format.
We'll use that for apab. Each line has form:
X<TAB><id>X</id> <disp>TOOLTIP</disp>
The AP57.printed.abbrs.txt file has format
X<TAB>TOOLTIP

# A small program generates apab_input.txt from  AP57.printed.abbrs.txt
# &#13;&#10;  for a line break in the tip

Abbreviation '&c.' is changed to '&amp;c.'
   
Because oif xml rules about '&',
 make_xml.py changes
  <ab>&c.</ab> in ap.txt to
 <ab>&amp;c.</ab> in ap.xml.
Thus apab_input.txt must use '&amp;c.' in place of '&c.'

python make_apab.py AP57.printed.abbrs.txt apab_input.txt

93 read from AP57.printed.abbrs.txt
skipping line 0001: Abbreviations and Symbols [1]
skipping line 0002: ------------------------------------------
skipping line 0003:
Altered tooltip at line 81
  old: Et cetera. denotes that the rest of the word under consideration is to be
 supplied; e. g. रत्नप्रभवस्य यस्य under अनन्त means अनन्तरत्न &c.
  new: Et cetera. denotes that the rest of the word &#13;&#10;under consideratio
n is to be supplied;&#13;&#10; e. g. रत्नप्रभवस्य यस्य under अनन्त means अनन्तरत
न &c.
Altered abbreviation at line 81
  old: &c.
  new: &amp;c.
skipping line 0082:
skipping line 0083:
skipping line 0084: A Supplementary List [2]
skipping line 0085: ------------------------------------------
skipping line 0086:
85 lines written to apab_input.txt

==============================================================
In csl-pywork repo,  generate apab folder:
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/ap/pywork
# start with a copy of ap90ab folder
cp -r ../../ap90/pywork/ap90ab apab
cd apab
mv ap90ab.sql apab.sql
mv redo_ap90ab.sh redo_apab.sh
rm ap90ab_input.txt 
# replace ap90 with ap in several files
sed -i 's/ap90/ap/g' apab.sql
sed -i 's/ap90/ap/g' readme.txt
sed -i 's/ap90/ap/g' redo_apab.sh
sed -i 's/ap90/ap/g' redo.sh

# copy apab_input.txt 
cp /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/apab_input.txt .

# test the construction
sh redo_apab.sh

========================
modify files in csl-pywork local repo:
 modify csl_ptwork/v02/inventory.txt
Add ap to these 5 lines:
old:
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/${dictlo}ab.sql:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/${dictlo}ab_input.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/readme.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/redo.sh:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/redo_${dictlo}ab.sh:CD

new:
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md ap:pywork/${dictlo}ab/${dictlo}ab.sql:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md ap:pywork/${dictlo}ab/${dictlo}ab_input.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md ap:pywork/${dictlo}ab/readme.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md ap:pywork/${dictlo}ab/redo.sh:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md ap:pywork/${dictlo}ab/redo_${dictlo}ab.sh:CD

------------------------
 modify csl_ptwork/v02/makotemplates/pywork/redo_postxml.sh
old:
# abbreviations
%if dictlo in ['ben','stc','bur','cae','mw','pw','pwg','lan','gra','ap90','pwkvn','bhs','md']:

new:
# abbreviations
%if dictlo in ['ben','stc','bur','cae','mw','pw','pwg','lan','gra','ap90','pwkvn','bhs','md','ap']:

<span title="" style="border-bottom: 1px dotted #000; text-decoration: none;">&amp;c.</span>


========================

Do a local install of ap: do abbreviations show tooltips?

cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

====================================================
Installation
----------------------------------------------------
# sync csl-pywork to github 
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "ap: Activate <ab>X</ab> tooltips 
Ref: https://github.com/sanskrit-lexicon/AP/issues/2"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

-----------------------------
# sync to Cologne, pull changed repos, redo display
---------------
ssh login to Cologne
cd csl-pywork #pull

---------------
# update displays for ap
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

--------------
# sync this issue to github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue2/  # home

git pull
git add .
git commit -m "ap: Activate <ab>X</ab> tooltips 
Ref: https://github.com/sanskrit-lexicon/AP/issues/2"
git push
