
cp ../issue3/temp_ap_history/ap_20260112_107338c.txt  temp_cdsl.txt
cp ../issue3/temp_ABuploads/AP57_AB_v3a2.txt temp_v3a2.txt

python ../diff_to_changes_dict.py temp_cdsl.txt temp_v3a2.txt change.txt
88513 changes written to change.txt

wc -l temp_*.txt
  341291 temp_cdsl.txt
  341291 temp_v3a2.txt

(/ 88513.0 341291.0)  26%

--------------------------------
#extended ascii comparison
python check_ea1.py temp_cdsl.txt check_ea1_cdsl.txt
41 extended ascii codes found in temp_cdsl.txt

python check_ea1.py temp_v3a2.txt check_ea1_v3a2.txt
57 extended ascii codes found in temp_v3a2.txt

# compare the ea1 files
python compare_ea1.py  cdsl,v3a2 check_ea1_cdsl.txt check_ea1_v3a2.txt compare_ea1_cdsl_v3a2.txt

