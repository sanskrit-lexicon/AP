
02-11-2026 Explore AP57_AB_v4a.txt from Andhrabharati
 https://github.com/sanskrit-lexicon/AP/issues/5#issuecomment-3831267121
 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issuex #home
unzip AP57_AB_v4a.zip
 AP57_AB_v4a.txt
# Remane to temp...
mv AP57_AB_v4a.txt temp_AP57_AB_v4a.txt

# number of lines
wc -l temp_AP57_AB_v4a.txt
# 85200 temp_AP57_AB_v4a.txt

# current ap.txt from csl-orig
#  commit ec0b80a5bd60d228162dd8d948fb26a258496055
git show ec0b80a5:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issuex/temp_ap_0.txt
# number of lines
339763 temp_ap_0.txt


wc -l temp_ap_0.txt
# Extended Ascii code usage
python check_ea1.py temp_AP57_AB_v4a.txt ea_AP57_AB_v4a.txt
85200 lines in temp_AP57_AB_v4a.txt
62 extended ascii codes found in temp_AP57_AB_v4a.txt

python check_ea1.py temp_ap_0.txt ea_cdsl.txt
339763 lines in temp_ap_0.txt
104 extended ascii codes found in temp_ap_0.txt

#compare
python compare_ea1.py  cdsl,v4a ea_cdsl.txt ea_AP57_AB_v4a.txt compare_ea_cdsl_v4a.txt

104 read from ea_cdsl.txt
62 read from ea_AP57_AB_v4a.txt
112 lines written to compare_ea_cdsl_v4a.txt

 grep '<L>' temp_ap_0.txt | wc -l
36691
grep '<L>' temp_AP57_AB_v4a.txt | wc -l
36693
But the lines starting with <L> are quite different.
