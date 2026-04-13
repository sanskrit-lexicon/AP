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

# Step 1

Correct entries having '^[.]{@{#\-([^ }]+)#}@}' in the regex.
There were around 7412 such cases where the line starts with a word having the above regex. 
They were easier to handle.
`python3 step1.py tmp_ap_0.txt tmp_ap_1.txt log1.tsv`
This takes tmp_ap_0.txt as input and produces tmp_ap_1.txt as output.
log1.tsv is a tab separated file the Lid, basehw, suffix and resolution fields. If resolution is not found, the answer is shown as 'None'.
Where automatic resolution could not be done, temp_ap_1.txt file has key1 and key2 marked with '.ABC' as placeholder, so that they can be easily identified and corrected manually.
As there is a high possibility that L numbers may change subsequent to handling of other patterns in future, all new L numbers are marked with '.XYZ' as placeholder in tmp_ap_1.txt. They will be mechanically filled in later, looking at the L numbers of surrounding entries.
Thus the result of `cat tmp_ap_1.txt | grep '.ABC' | wc -l` should be equal to `cat log1.tsv | grep 'None' | wc -l`.
Result of `cat tmp_ap_1.txt | grep '.XYZ' | wc -l` should be equal to the lines of log1.tsv minus one.




