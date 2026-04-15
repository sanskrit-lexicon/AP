
Begin 04-01-2026 Activate link targs

 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati #home

 Ref: https://github.com/sanskrit-lexicon/AP/issues/14#issuecomment-4246192806
* history of ap tooltips file in csl-pywork/v02
cd /c/xampp/htdocs/cologne/csl-pywork

git log --follow --pretty=format:"%ad %h %an %s" --date=short -- v02/distinctfiles/ap/pywork/apauth/tooltip.txt > temp_history_ap_tooltip.txt

2026-04-13 6dfeba7 funderburkjim AP: Edits of ap ls tooltips Ref: https://github.com/sanskrit-lexicon/AP/issues/14
2026-02-01 2ab228f funderburkjim ap: edits to ls tooltips Ref: https://github.com/sanskrit-lexicon/AP/issues/2#issuecomment-3827450873
2026-01-30 2599fa7 funderburkjim ap: Activate ls tooltips Ref: https://github.com/sanskrit-lexicon/AP/issues/2

* All 3 versions of tooltips.xt for ap in csl-pywork repo
cd /c/xampp/htdocs/cologne/csl-pywork
# 2026-01-30
git show 2599fa7:v02/distinctfiles/ap/pywork/apauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati/temp_tooltip_2599fa7.txt

# 2026-02-01 
git show 2ab228f:v02/distinctfiles/ap/pywork/apauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati/temp_tooltip_2ab228f.txt

diff temp_tooltip_2ab228f.txt ../tooltips_0.txt | wc -l
# 0 

# 2026-04-13
git show 6dfeba7:v02/distinctfiles/ap/pywork/apauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati/temp_tooltip_6dfeba7.txt

diff temp_tooltip_6dfeba7.txt ../tooltips_3.txt | wc -l
#542
But
diff -w temp_tooltip_6dfeba7.txt ../tooltips_3.txt | wc -l
# 0
python unixify.py ../tooltips_3.txt  tooltips_3_unix.txt
diff temp_tooltip_6dfeba7.txt tooltips_3_unix.txt | wc -l
# 0

# Andhrabharati's file:
cp ../../issue2/AP57.list.of.sources.as.printed.txt  AP57.list.of.sources.as.printed.txt

# unixify AB's file, make a shorter name
python unixify.py AP57.list.of.sources.as.printed.txt AB_tooltips.txt
# 277 lines written to AB_tooltips.txt

# remove title lines in AB file
cp AB_tooltips.txt AB_tooltips_a.txt
# manual edit of AB_tooltips_a.txt
wc -l AB_tooltips_a.txt
269 AB_tooltips_a.txt


# tooltips_3_sort.txt:  sort of tooltips_3_unix.txt
python tooltip_sort.py tooltips_3_unix.txt tooltips_3_sort.txt
269 lines written to tooltips_3_sort.txt

# AB_tooltips_b.txt: sort of AB_tooltips_a.txt  
python tooltip_sort.py AB_tooltips_a.txt AB_tooltips_b.txt  
# 269 lines

* initial raw comparison of AB_tooltips_b.txt AND tooltips_3_sort.txt
diff AB_tooltips_b.txt  tooltips_3_sort.txt > diff_AB-b_cdsl-3.txt
wc -l diff_AB-b_cdsl-3.txt
375 diff_AB-b_cdsl-3.txt  # so about 100 differences


* compare abbreviations AB_tooltips_b.txt AND tooltips_3_sort.txt
python compare_abbrev.py AB_tooltips_b.txt tooltips_3_sort.txt compare_abbrev_b_3.txt
1 duplicate abbrevs in AB_tooltips_b.txt
0 duplicate abbrevs in tooltips_3_sort.txt
37 unique in AB_tooltips_b.txt
39 unique in tooltips_3_sort.txt
85 lines written to compare_abbrev_b_3.txt


* AB_tooltips_c.txt revision of AB_tooltips_b.txt
cp AB_tooltips_b.txt AB_tooltips_c.txt
**  manual revisions of AB_tooltips_c.txt based on compare_abbrev_b_3.txt
1. remove duplicate abbrev: Uṇ.	Uṇādisūtras.
2. Change Abbrevs based on tooltip

* compare abbreviations AB_tooltips_c.txt AND tooltips_3_sort.txt
python compare_abbrev.py AB_tooltips_c.txt tooltips_3_sort.txt compare_abbrev_c_3.txt
0 duplicate abbrevs in AB_tooltips_c.txt
0 duplicate abbrevs in tooltips_3_sort.txt
24 unique in AB_tooltips_c.txt
26 unique in tooltips_3_sort.txt
60 lines written to compare_abbrev_c_3.txt

diff  AB_tooltips_b.txt  AB_tooltips_c.txt > AB_tooltips_diff_b_c.txt

* tooltips_4.txt revision of tooltips_3_sort.txt
cp tooltips_3_sort.txt tooltips_4.txt

* THE END
