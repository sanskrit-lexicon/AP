
changes to ap.txt.  These are all print changes
21864.020  : powagalaH : Abh. Cin. 11. 93 : Abh. Cin. 1193 : print change
22137      : praGaRaH  : Abh. Cin. 10. 10 : Abh. Cin. 1010 : print change
9016       : udgraBaRam : Ts. 1. 1. 13 : Ts. 1. 1. 13. 1 : print change
9788       : upayA : Ts. 1. 4. 15 : Ts. 1. 4. 15. 1 : print change
10467      : Urj : Ts. 1. 1. 1  : Ts. 1. 1. 1. 1 : print change
10472      : Urjasvat : Ts. 1. 1. 1 : Ts. 1. 1. 1. 1 : print change
138.032    : akzAvApaH : Ts. I, 8. 9. 1. 2 : TS. 1. 8. 9. 2 : print change
3247       : abAla  : Nir. IX. 10 : Nir. 9. 10 : print change
4542       : arcita : Ms. 4, 235 : Ms. 4. 235 : print change
11667.110  : karmadozaH : Ms. 1, 104 : Ms. 1. 104 : print change
12290.026  : kIwajam : Ms. 168 : Ms. 11. 168 : print change
16423      : tAskaryam : Ms. 9 : Ms. 9. 222 : print change. cf PWG
19379.094  : niSCandas : Ms. 3, 7 : Ms. 3. 7 : print change
19653      : nyAyya : Ms. 2, 152 : Ms. 2. 152 : print change
7227       : ABUtiH : Ait. Br. 8. 13. 8 : Ait. Br. 7. 13. 8 : print change
--------------------------------

csl-orig at github revised.

Installation:

python diff_to_changes_dict.py ap_0.txt ap_1.txt change_0_1.txt
15 changes written to change_0_1.txt

# get current ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git pull  # 8 files changed

cp /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt ap_2.txt
python updateByLine.py ap_2.txt change_0_1.txt ap_3.txt
15 change transactions from change_0_1.txt

cp ap_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cp /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "AP: link corrections.
Ref: https://github.com/sanskrit-lexicon/AP/issues/19"
git push
-------------------------------------------
Post print changes to csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections/
git pull
etc.
