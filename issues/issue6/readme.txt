
2026-02-01
readme.txt for /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6

Change {%X%} to <lex>X</lex> for the 'gender' abbreviations X

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6

# temp_ap_0.txt =  latest version of ap.txt

------------------------
# gender_to_lex.py makes the following replacements:
replacements = [
 ('{%m.%}','{%<lex>m.</lex>%}'),
 ('{%f.%}','{%<lex>f.</lex>%}'),
 ('{%n.%}','{%<lex>n.</lex>%}'),
 ('{%a.%}','{%<lex>a.</lex>%}'),

 ('{%ind.%}','{%<lex>ind.</lex>%}'),
 ('{%adv.%}','{%<lex>adv.</lex>%}'),
 # two genders
 ('{%m. f.%}', '{%<lex>m.</lex> <lex>f.</lex>%}'),
 ('{%m. n.%}', '{%<lex>m.</lex> <lex>n.</lex>%}'),
 ('{%f. n.%}', '{%<lex>f.</lex> <lex>n.</lex>%}'),

 ]


python gender_to_lex.py temp_ap_0.txt temp_ap_1.txt
27621 lines changed

---------------------------------------
# Treat <lang> tag like <ab> in Cologne displays
# Small change to basicadjust.php in csl-websanlexicon
# <lex>X</lex>  ->  <ab>X</lex>
# Then in displays, X will get tooltip like other abbreviations.

# also change to basicadjust.php in csl-apidev
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh

=======================================
# remake xml from temp_ap_1.txt and check xml structure
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6
cp temp_ap_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6

----------------------
# construct change file
python diff_to_changes_dict.py temp_ap_0.txt temp_ap_1.txt change_0_1.txt
27621 lines changed

================================================

This needs further action -- not yet done.
only instance of 'cl.' in ap.txt
{#izita#}¦ {%<ab>p. p.</ab>%} (<ab>fr.</ab> {#iz#} €4 <ab>cl.</ab>)
 
================================================
INSTALLATION
sync to github:

------------------
# csl-orig
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6
diff temp_ap_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: <lex> markup:
Ref: https://github.com/sanskrit-lexicon/AP/issues/6"
git push


------------------------
#csl-websanlexicon sync to Github

cd /c/xampp/htdocs/cologne/csl-websanlexicon
git pull
git add .
git commit -m "AP: <lang> markup displays as abbreviation.
Ref: https://github.com/sanskrit-lexicon/AP/issues/6"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6

------------------------
#csl-apidev sync to Github

cd /c/xampp/htdocs/cologne/csl-apidev
git pull
git add .
git commit -m "AP: <lang> markup displays as abbreviation.
Ref: https://github.com/sanskrit-lexicon/AP/issues/6"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6

---------------------------------------------------
# sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
csl-websanlexicon # pull
csl-apidev # pull
---------------
# update displays for ap
cd csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

-----------------------------------------------------
# sync this repo to github

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6
git pull
git add .
git commit -m "AP: <lex>, <lang> markup.
Ref: https://github.com/sanskrit-lexicon/AP/issues/6"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue6

-----------------------------------------------------
THE END
-----------------------------------------------------
