echo "FETCHING BASELINE DICTIONARY FROM CSL-ORIG..."
git -C ../../../../sanskrit-lexicon/csl-orig show 34263ba59be878831ab802ee52d17665695bcd5b:v02/ap/ap.txt > temp_ap_0.txt
echo ""
echo "RUNNING STEP 1..."
python3 step1.py temp_ap_0.txt temp_ap_1.txt temp_log1.tsv
echo ""
echo "RUNNING STEP 2..."
python3 step2.py temp_ap_1.txt temp_ap_2.txt temp_log2.tsv
echo ""
echo "COPIED MANUALLY TEMP_AP_2.TXT TO TEMP_AP_3.TXT AND DID MANUAL CORRECTIONS THERE. "
echo "NOT MADE PART OF REDO.SH SCRIPT TO AVOID ACCIDENTAL OVERWRITE."
echo ""

if [ -f temp_ap_3.txt ]; then
    echo "GENERATE AND STORE DIFFS."
    diff temp_ap_0.txt temp_ap_3.txt > work.diff
    echo ""
fi

if [ -f work.diff ]; then
    echo "APPLY THE DIFFS AND GENERATE TEMP_AP_4.TXT."
    patch -i work.diff temp_ap_0.txt -o temp_ap_4.txt
    echo ""
else
    echo "WORK.DIFF NOT FOUND. CANNOT GENERATE TEMP_AP_4.TXT."
    echo ""
fi

if [ -f temp_ap_3.txt ] && [ -f temp_ap_4.txt ]; then
    echo "COMPARE TEMP_AP_3.TXT AND TEMP_AP_4.TXT. IT SHOULD RESULT IN 0 DIFFS."
    echo ""
    if diff -q temp_ap_3.txt temp_ap_4.txt > /dev/null; then
        printf "\e[32mSUCCESS: TEMP_AP_3.TXT AND TEMP_AP_4.TXT ARE IDENTICAL! 👍\e[0m\n"
    else
        printf "\e[31mFAILURE: DIFFERENCES FOUND BETWEEN TEMP_AP_3.TXT AND TEMP_AP_4.TXT!\e[0m\n"
        diff temp_ap_3.txt temp_ap_4.txt
    fi
fi