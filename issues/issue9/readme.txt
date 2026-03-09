
03-02-2026 Begin extra headwords

 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9 #home

* --------------------------------

* ==========================================
* tempwork/ap_0.txt start with this revision of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
# commit 7140e09c08f3addf4a3867ba09759c1d636faf46
git show 7140e09c:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9/tempwork/ap_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9/
* ==========================================
* tempwork/ap_0a.txt
cp tempwork/ap_0.txt tempwork/ap_0a.txt
# manual edit tempwork/ap_0a.txt
----- 19 cases bold devanagari after ¦
make these manual changes
old:
A¦X{@{#Y#}@}Z 
new:
A¦X
{@{#Y#}@}Z 
* bdstats  -- prefix befor {@{#X#}@}
" " 639
"(" 348
"." 42295
".(" 1822
"[" 2
"━" 93
total: 45199

---------------------
4461 matches for "\.━{@<ab>Comp.</ab>@}
4461 matches for "{@<ab>Comp.</ab>@}"

* ==========================================
* prep1_0.txt format
Format tab-delimited fields:
xx : solution code a string. 
   default is 'm?' if adjusted header is non-standard 
   or '?' if xx is default 'not done yet'
L  : Entry identifier from metaline
n1,n2:  counts of bd {@{#X#}@} in entry
        n1 after compstr = '.━{@<ab>Comp.</ab>@}'
        n2 before compstr
header: text before '¦' (in line after metaline)
        adjustments:
        1. remove '<hom>.*?</hom> '
        2. remove ' <ab>&c.</ab>'
        3. remove '{%<lex>.*?</lex>%}
        4. If adjusted header has form '{#.*?#}', then remove '{#' and '#}'
           If header does not have this form, set solution-code='man'
althws  (comma-separated list of k1). 

* prep1_0.txt
python prep1.py 0 tempwork/ap_0a.txt prep1_0.txt

Field-separator is ':'  (could be tab)

Exclude entries where adjusted header is same as k1
  (the included records are expected to generate alternate headwords)

total: 45199
36688 entries from tempwork/ap_0a.txt
3399 records written to prep1_0.txt


* prep1_1.txt 
Format is same as prep1_0.txt
Various programmatic changes to prep1_0.txt
python prep1a.py prep1_0.txt prep1_1.txt

** stats counts per method  651 NOT done (status contains '?')
3399 read from prep1_0.txt
01 869
02 124
03 4
04 102
05 242
06 84
07 29
08 26
09 111
10 47
11 113
12 46
13 35
14 31
15 32
16 24
17 29
18 21
19 41
20 23
21 22
22 427
23 168
24 98
? 335
man? 316
Total 3399
3399 lines written to prep1_1.txt

* tempwork/ap_0b.txt
ap_0b.txt corrections consistent with the edits
cp tempwork/ap_0a.txt tempwork/ap_0b.txt 

* DONE prep1_2.txt manual editing of the 'man?','?' cases

python prep_sort.py stat prep1_1.txt prep1_2.txt

# check round-trip
python prep_sort.py L prep1_2.txt temp.txt
diff prep1_1.txt temp.txt | wc -l
# 0 expected

* change files for ap
python diff_to_changes_dict.py tempwork/ap_0.txt tempwork/ap_0a.txt change_ap_0_0a.txt
85 lines changed

python diff_to_changes_dict.py tempwork/ap_0a.txt tempwork/ap_0b.txt change_ap_0a_0b.txt
83 lines changed

* ==========================================
* INSTALLATION csl-orig
* 03-08-2026 Install tempwork/ap_0b.txt at Github, Cologne

** check repo(s) for pull
cd /c/xampp/htdocs/cologne/csl-orig
git status
# no staged files
git pull
.github/workflows/update-stardict.yml 

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9 #home

------------
** install local displays from tempwork/ap_0j_5.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9 #home
cp tempwork/ap_0b.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9/  # home

-----------------------------
** sync csl-orig to github:
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: alternate headword preparation
Ref: https://github.com/sanskrit-lexicon/AP/issues/9"
#  1 file changed, 153 insertions(+), 153 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9/  # home

---------------------------
** sync Cologne to github
# connect to cologne.
cd csl-orig
git pull

cd ../csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
* sync this repo to Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue9
git add .
git commit -m "AP: alternate headword preparation
Ref: https://github.com/sanskrit-lexicon/AP/issues/9"

git push

* ==========================================
* THE END

