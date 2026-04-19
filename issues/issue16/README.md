# Initial Statistics

tmp_ap_0.txt is taken as of 1bc3a0825a85b4e18120d872ef93e418e59e18ca in csl-orig repository

1           {@          15364
1.1         {@{         10909
1.1.1       {@{#        10909
1.1.1.1     {@{#\-      10489
1.1.1.1.1   [.]{@{#\-    8117
1.1.1.1.1.1 ^[.]{@{#\-   8117
1.1.1.1.2   [^.]{@{#\-   2380
1.1.1.1.2.1 [(]{@{#\-    2092
1.1.1.1.2.2 [ ]{@{#\-     308
1.1.1.1.2.3 [^( .]{@{#\-    1
1.1.1.2     {@{#[^-]      454
1.1.1.2.1   [ ]{@{#[^-]   280
1.1.1.2.2   [.]{@{#[^-]    19
1.1.1.2.3   ━{@{#[^-]      91
1.1.1.2.4   [(]{@{#[^-]    71
1.1.1.2.5   \[{@{#[^-]      1
1.2         {@<          4454
1.2.1       {@<ab>       4454
1.3         {@[^<{]         1

# Step1

subsumed under step 2. No separate script now.

# Step 2

Correct entries having '^[.]{@{#\-([^ }]+)#}@}' in the regex.
`python3 step2.py tmp_ap_0.txt tmp_ap_2.txt log2.tsv`
This takes tmp_ap_0.txt as input and produces tmp_ap_2.txt as output.
log2.tsv is a tab separated file with Lid, basehw, suffix and resolution fields. If resolution is not found, the answer is shown as 'None'.
It also uses manually_mapped.tsv as a fallback for cases where automatic resolution fails. This file contains manual mappings for cases that cannot be resolved automatically.
Where automatic resolution could not be done, tmp_ap_2.txt file has key1 and key2 marked with '.ABC' as placeholder, so that they can be easily identified and corrected manually.
As there is a high possibility that L numbers may change subsequent to handling of other patterns in future, all new L numbers are marked with '.XYZ' as placeholder in tmp_ap_2.txt. They will be mechanically filled in later, looking at the L numbers of surrounding entries.
Thus the result of `cat tmp_ap_2.txt | grep '.ABC' | wc -l` should be equal to `cat log2.tsv | grep 'None' | wc -l`. Both should be 0 after incorporating manually_mapped.tsv.
`cat tmp_ap_2.txt | grep '<L>.*\.XYZ' | wc -l` should be equal to `cat log2.tsv | wc -l` minus one (the header).
There are additional `{{Lbody=*.XYZ}}` lines added for entries with multiple suffixes. So total `cat tmp_ap_2.txt | grep '.XYZ' | wc -l` = (`cat log2.tsv | wc -l` - 1) + (number of multi-suffix entries).

# Step 3

Check whether resolution column of log2.tsv exists in sanhw1.txt (a list of valid Sanskrit words).
`python3 step3.py`
This reads log2.tsv and produces log3.tsv as output with an additional column 'in_sanhw1' which is True or False.
Additionally, if the resolution ends with 'H' or 'm', it strips that character and checks again in sanhw1.txt for a match.
