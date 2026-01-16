ymd="$1"
commit="$2"

if [ -z "$ymd" ] || [ -z "$commit" ]; then
    echo "Usage: $0 <ymd> <commit>"
    echo "Both parameters are required."
    exit 1
fi

echo "ymd = $ymd, commit = $commit"
dir="/c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue3/temp_ap_history"
outfile="ap_${ymd}_${commit}.txt"
out="$dir/$outfile"
cd /c/xampp/htdocs/cologne/csl-orig
cmd="git show $commit:v02/ap/ap.txt > $out"

git show $commit:v02/ap/ap.txt > $out
cd $dir
wc -l $outfile



