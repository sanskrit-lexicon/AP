
02-22-2026 Explore AP57_AB_v4a.txt from Andhrabharati, continue
Continued from issue8
 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b #home

* --------------------------------
* temp_v4a_0c.txt  Slightly edited version of AP57_AB_v4a.txt
cp ../issue8/temp_v4a_0c.txt temp_v4a_0c.txt
* TODO possible changes to temp_v4a_0c.txt
---
'= {@{#X#}@}' -> '= {#X#}'  (3 instances)
--- L=15600
'to conquer defeat' -> 'to conquer, defeat'
* temp_v4a_0d.txt  
# '〔' -> '<lex>'
# '〕' -> '</lex>' 
#  ('.²' ,  '∙²' ),  (one line changed
#  ('.³' ,  '∙³' ),

python v4a_0d.py temp_v4a_0c.txt temp_v4a_0d.txt
160257 read from temp_v4a_0c.txt
make_newlines_1 finds 28136 cases
make_newlines_1 returns 160257 lines
make_newlines_2 finds 1 cases
make_newlines_2 returns 160257 lines
160257 lines written to temp_v4a_0d.txt

* --------------------------------
* Prepare for changes to make_xml.py
cd /c/xampp/htdocs/cologne/csl-pywork/
git log
# latest commit 2578c2912da026aec06db4ab09500f3aff68a87f (Feb 6, 2026 Dhaval)
cd /c/xampp/htdocs/cologne/csl-pywork/
git show 2578c2912:v02/makotemplates/pywork/make_xml.py > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/make_xml.py
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/

* Prepare for changes to basicadjust.php
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git log 
# latest commit 4a79f79056fe5449328c303f18d64415c249143e Gasuns, FRI
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git show 4a79f79056:v02/makotemplates/web/webtc/basicadjust.php > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/basicadjust.php
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/


* make_xml.py section pertaining to ap
** initial code
%if dictlo == 'ap':
def dig_to_xml_specific(x):
 """ changes particular to digitization"""
 # There is one instance of a 'Poem' tag, under hw=akzOhiRI
 #  <Poem>...
 #  ...
 #   ... </Poem>
 # change this to <div n="Poem">...</div>
 if re.search('Poem>',x):
  x = x.replace('<Poem>','<div n="Poem">')
  # Because of the the 'close_div' logic, we just remove </Poem>.
  # The close-div logic will add the </div>
  #x = x.replace('</Poem>','</div>')
  x = x.replace('</Poem>','')
  return x
 # in AP, ‡ is used in Devanagari text to indicate a line-break hyphen
 # This is different from the usage of this symbol in AP90.
 # Replace with '-'
 x = re.sub(u'‡','-',x)
 # in ap.txt, the Currency symbol € is markup indicating a root. It has no
 # correspondent in the printed text. About 3000+ instances.
 # For now, replace it with an empty '<root/>' element, and do not display
 # it in 'disp.php'
 x = x.replace(u'€','<root/>')
 # Divisions are indicated by lines starting with a period.
 # Three types are seen:
 # .{#-BaH#}
 # .²1 Absence  ...
 # .³({%a%})
 # 07-03-2021.  Drop restriction that the line STARTS with .² or .³
 #if re.search(u'^[.][²]',x):
 if re.search(u'[.][²]',x):
 # there may be nothing else on the line (300+ cases), in particular no space
 # do same thing anyway, not requiring the trailing space.
  x = re.sub(u'[.][²]([^ ]*) ',r'<div n="2" name="\1">\1 ',x)
  x = re.sub(u'[.][²]([^ ]*)',r'<div n="2" name="\1">\1 ',x)
 #elif re.search(u'^[.][³]',x):
 elif re.search(u'[.][³]',x):
  m = re.search('[.][³]([^ ]*) ',x)
  if not m:
   m = re.search('[.][³]([^ ]*)',x)
  assert m ,"adjust_xml. PROBLEM 1:x=\n%s"%x
  data = m.group(1)
  # data = ({%x%})
  m = re.search(r'\(<i>(.)</i>\)',data)
  assert m ,"adjust_xml. PROBLEM 2:x=\n%s"%x
  name=m.group(1)
  x = re.sub(u'[.][³]([^ ]*) ',r'<div n="3" name="%s">\1 '%name,x)
  x = re.sub(u'[.][³]([^ ]*)',r'<div n="3" name="%s">\1 '%name,x)

 # introduce line-break (call it a plain div) at any line starting with
 # a period.  This was the convention used by Thomas to designate
 # divisions. This is the /{#-BaH#} type case
 if x.startswith('.'):
  #print("extra div:",x)
  x = re.sub(r'^[.]','<div n="Q">',x)
 return x
%endif # ap dictionary
* basicadjust.php  ( csl-websanlexicon AND csl-apidev
** initial code for ap
  else if ($this->getParms->dict == "ap") {
   // replace -- with mdash : perhaps should be part of ap.txt
   $line = preg_replace('/--/','&#8212;',$line);
   // 03-12-2017.  Put 'b' (bold) tag around the first word of a div
   $line = preg_replace('|(<div[^>]*>)(\(<i>.</i>\))|','\\1<b>\\2</b>',$line);
   // 11-29-2018.  Also pattern '<s>--X</b>' 
   $line = preg_replace('|(<div[^>]*>)([0-9]+)|','\\1<b>\\2</b>',$line);
   // Remove <root/> tag -- it plays no part in display
   $line = preg_replace('|<root/>|','',$line);
  }
* ==========================================
* Start with temp_ap_0f.txt 
(issue8a ended with temp_ap_0f.txt)
current  commit f82bddd83c0
cd /c/xampp/htdocs/cologne/csl-orig/
git show f82bddd83c0:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/temp_ap_0f.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b 
* ==========================================
* db_comp.6 r'━{@[^@]*?@}', # U+2501 Box Drawings Heavy Horizontal
em dash —  &#8212; U+2014
 not present in temp_v4a_0c.txt
━U+2501 Box Drawings Heavy Horizontal  02-22-2026
basicadjust.php

# option 6 is sequence of ━
4554 matches in 4508 lines for "━{@" in buffer: temp_v4a_0c.txt

− U+2212 Minus Sign

* tempwork/ap_0g_0.txt intermediate prepare for db_comp.6
python ap_0g.py temp_ap_0f.txt tempwork/ap_0g_0.txt
339763 read from temp_ap_0f.txt
make_newlines_1 finds 5853 cases
make_newlines_1 returns 339763 lines
339763 lines written to tempwork/ap_0g_0.txt

* tempwork/ap_0g_1.txt corrections db_comp.py option 6
python db_comp.py 6 tempwork/ap_0g_0.txt temp_v4a_0d.txt tempwork/6_work1.txt tempwork/ap_0g_1.txt

compare_groups finds 4 problem entries
4 records written to tempwork/6_work1.txt
marking 0 lines
339763 lines written to tempwork/ap_0g_1.txt

work with tempwork/6_work1.txt 
edit tempwork/ap_0g_1.txt
When done, '_' -> '' and save tempwork/ap_0g_1.txt

sh redo_ap.sh tempwork/ap_0g_1.txt ap  # check validation

python db_comp.py 6 tempwork/ap_0g_1.txt temp_v4a_0d.txt tempwork/6_work2.txt tempwork/ap_0g_2.txt
diff tempwork/ap_0g_1.txt tempwork/ap_0g_2.txt
0
rm tempwork/ap_0g_2.txt

* ==========================================
* tempwork/ap_0g_2.txt intermediate prepare db_comp option 7
python ap_0g_2.py tempwork/ap_0g_1.txt tempwork/ap_0g_2.txt

make_newlines_1 finds 984 cases
make_newlines_1 returns 339763 lines
make_newlines_2 finds 156 cases
make_newlines_2 returns 339763 lines
339763 lines written to tempwork/ap_0g_2.txt

* tempwork/ap_0g_3 intermediate. db_comp.py option 7 r'━{%.*?%}'
db_comp.py option 7: r'━{%.*?%}'

python db_comp.py 7 tempwork/ap_0g_2.txt temp_v4a_0d.txt tempwork/7_work1.txt tempwork/ap_0g_3.txt

compare_groups finds 232 problem entries
232 records written to tempwork/7_work1.txt
marking 50 lines
339763 lines written to tempwork/ap_0g_3.txt

work with tempwork/7_work1.txt 
edit tempwork/ap_0g_3.txt
When done, '_' -> '' and save tempwork/ap_0g_3.txt

sh redo_ap.sh tempwork/ap_0g_3.txt ap  # check validation

* tempwork/ap_0g_4 intermediate
python db_comp.py 7 tempwork/ap_0g_3.txt temp_v4a_0d.txt tempwork/7_work2.txt tempwork/ap_0g_4.txt
compare_groups finds 3 problem entries
3 records written to tempwork/7_work2.txt
marking 1 lines
339763 lines written to tempwork/ap_0g_4.txt

work with tempwork/7_work2.txt 
edit tempwork/ap_0g_4.txt
When done, '_' -> '' and save tempwork/ap_0g_4.txt

sh redo_ap.sh tempwork/ap_0g_4.txt ap  # check validation

* tempwork/ap_0g_5 corrected
python db_comp.py 7 tempwork/ap_0g_4.txt temp_v4a_0d.txt tempwork/7_work3.txt tempwork/ap_0g_5.txt

compare_groups finds 1 problem entries
1 records written to tempwork/7_work3.txt
marking 1 lines
339763 lines written to tempwork/ap_0g_5.txt

work with tempwork/7_work3.txt 
edit tempwork/ap_0g_5.txt
When done, '_' -> '' and save tempwork/ap_0g_4.txt

sh redo_ap.sh tempwork/ap_0g_4.txt ap  # check validation

python db_comp.py 7 tempwork/ap_0g_5.txt temp_v4a_0d.txt tempwork/7_work4.txt tempwork/ap_0g_6.txt
0 records written to tempwork/7_work4.txt
# tempwork/ap_0g_6.txt not needed, same as tempwork/ap_0g_5.txt
rm tempwork/ap_0g_6.txt
* ==========================================
* tempwork/ap_0g_6 intermediate. db_comp.py option 8 r'━.....',

python db_comp.py 8 tempwork/ap_0g_5.txt temp_v4a_0d.txt tempwork/8_work1.txt tempwork/ap_0g_6.txt

compare_groups finds 92 problem entries
92 records written to tempwork/8_work1.txt
marking 48 lines
339763 lines written to tempwork/ap_0g_6.txt


339763 lines written to tempwork/ap_0g_3.txt

work with tempwork/8_work1.txt 
edit tempwork/ap_0g_6.txt
When done, '_' -> '' and save tempwork/ap_0g_6.txt

sh redo_ap.sh tempwork/ap_0g_6.txt ap  # check validation

* tempwork/ap_0g_7 intermediate. db_comp.py option 8
python db_comp.py 8 tempwork/ap_0g_6.txt temp_v4a_0d.txt tempwork/8_work2.txt tempwork/ap_0g_7.txt

compare_groups finds 17 problem entries
17 records written to tempwork/8_work2.txt
marking 10 lines
339763 lines written to tempwork/ap_0g_7.txt

work with tempwork/8_work2.txt 
edit tempwork/ap_0g_7.txt
When done, '_' -> '' and save tempwork/ap_0g_7.txt

sh redo_ap.sh tempwork/ap_0g_7.txt ap  # check validation

* tempwork/ap_0g_8 corrected. db_comp.py option 8
python db_comp.py 8 tempwork/ap_0g_7.txt temp_v4a_0d.txt tempwork/8_work3.txt tempwork/ap_0g_8.txt

compare_groups finds 4 problem entries
4 records written to tempwork/8_work3.txt
marking 4 lines
339763 lines written to tempwork/ap_0g_8.txt

work with tempwork/8_work3.txt 
edit tempwork/ap_0g_8.txt
When done, '_' -> '' and save tempwork/ap_0g_8.txt

sh redo_ap.sh tempwork/ap_0g_8.txt ap  # check validation


python db_comp.py 8 tempwork/ap_0g_8.txt temp_v4a_0d.txt tempwork/8_work4.txt tempwork/ap_0g_9.txt
compare_groups finds 0 problem entries
0 records written to tempwork/8_work4.txt
marking 0 lines
339763 lines written to tempwork/ap_0g_9.txt


Done!  
rm tempwork/ap_0g_9.txt  # it is sames as tempwork/ap_0g_8.txt

* ==========================================
* tempwork/ap_0g_9.txt intermediate  db_comp.py option 9: r'[∙][²³]([^ ]*)'
db_comp.py option 9: r'[∙][²³]([^ ]*)'

 ('.²' ,  '∙²' ),
 ('.³' ,  '∙³' ),

python ap_0g_9.py tempwork/ap_0g_8.txt tempwork/ap_0g_9.txt
339763 read from tempwork/ap_0g_8.txt
make_newlines_1 finds 92221 cases
make_newlines_1 returns 339763 lines
339763 lines written to tempwork/ap_0g_9.txt

#make_xml.py revised  so handles '∙²', '∙³'

sh redo_ap.sh tempwork/ap_0g_9.txt ap  # check validation

* tempwork/ap_0g_10.txt corrected db_comp.py option 9
python db_comp.py 9 tempwork/ap_0g_9.txt temp_v4a_0d.txt tempwork/9_work1.txt tempwork/ap_0g_10.txt

compare_groups finds 11 problem entries
11 records written to tempwork/9_work1.txt
marking 11 lines
339763 lines written to tempwork/ap_0g_10.txt

work with tempwork/9_work1.txt 
edit tempwork/ap_0g_10.txt
When done, '_' -> '' and save tempwork/ap_0g_10.txt

sh redo_ap.sh tempwork/ap_0g_10.txt ap  # check validation

python db_comp.py 9 tempwork/ap_0g_10.txt temp_v4a_0d.txt tempwork/9_work2.txt tempwork/ap_0g_11.txt
compare_groups finds 0 problem entries

Done with option 9
rm tempwork/ap_0g_11.txt  # same as tempwork/ap_0g_10.txt
* ==========================================
* change files
python diff_to_changes_dict.py temp_ap_0f.txt tempwork/ap_0g_1.txt change_ap_0f_0g_1.txt
5856 changes written to change_ap_0f_0g_1.txt

python diff_to_changes_dict.py tempwork/ap_0g_1.txt tempwork/ap_0g_5.txt change_ap_0g_1_0g_5.txt
1226 changes written to change_ap_0g_1_0g_5.txt

python diff_to_changes_dict.py tempwork/ap_0g_5.txt tempwork/ap_0g_8.txt change_ap_0g_5_0g_8.txt
176 changes written to change_ap_0g_5_0g_8.txt

python diff_to_changes_dict.py tempwork/ap_0g_8.txt tempwork/ap_0g_10.txt change_ap_0g_8_0g_10.txt
92224 changes written to change_ap_0g_8_0g_10.txt

* ==========================================
*  DO INSTALLATION csl-orig, csl-websanlexicon, csl-apidev, csl-pywork
* 02-23-2026 Install tempwork/ap_0g_10.txt at Github, Cologne

cd /c/xampp/htdocs/cologne/csl-orig
git status
git pull
# Already up to date.
# and similarly for csl-pywork, csl-websanlexicon, csl-apidev
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b #home

# copy local
cp make_xml.py /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py
cp basicadjust.php /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

cp basicadjust.php /c/xampp/htdocs/cologne/csl-apidev/basicadjust.php

------------
# install local version from tempwork/ap_0g_10.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b #home
cp tempwork/ap_0g_10.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/  # home

-----------------------------
** sync csl-orig to github:
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: changes based on comparisons with  AP57_AB_v4a.txt. version ap_0g_10.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
# 1 file changed, 98216 insertions(+), 98216 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/  # home

---------------------------
** sync csl-pywork to github:
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull
git add .
git commit -m "AP: pywork make_xml.py 
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
# 1 file changed, 98216 insertions(+), 98216 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/  # home

---------------------------
** sync csl-websanlexicon to github:
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
# note wrong commit message!
git commit -m "AP: websanlexicon make_xml.py 
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
# 1 file changed, 3 insertions(+), 2 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/  # home

---------------------------
** sync csl-apidev to github:
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "AP: apidev basicadjust.php
Ref: https://github.com/sanskrit-lexicon/AP/issues/8"
# 1 file changed, 3 insertions(+), 2 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b/  # home

---------------------------
** sync Cologne to github
# connect to cologne.
cd csl-orig
git pull
--
cd ../csl-pywork
git pull
cd ../csl-websanlexicon
git pull
cd ../csl-apidev
git pull

cd ../csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
* sync this repo to Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue8b
git add .
git commit -m "#8 merging AP57_AB_v4a.txt and cdsl ap.txt (ap_0g_10.txt)"
git push

* ==========================================
* THE END

