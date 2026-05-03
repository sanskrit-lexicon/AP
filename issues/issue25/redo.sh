echo "Fetching baseline dictionary from csl-orig..."
git -C ../../../../sanskrit-lexicon/csl-orig show 34263ba59be878831ab802ee52d17665695bcd5b:v02/ap/ap.txt > temp_ap_0.txt
echo "Running step 1..."
python3 step1.py temp_ap_0.txt temp_ap_1.txt temp_log1.tsv
echo "Running step 2..."
python3 step2.py temp_ap_1.txt temp_ap_2.txt temp_log2.tsv
