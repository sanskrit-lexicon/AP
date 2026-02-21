apfile="$1"
appdir="$2"
# regenerate local displays from "$apfile"

cp $apfile /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap ../../${appdir}
# sh xmlchk_xampp.sh ap
python3 ../../xmlvalidate.py ../../${appdir}/pywork/ap.xml ../../${appdir}/pywork/ap.dtd
# restore ap.txt in csl-orig
echo "restoring ap.txt in csl-orig"
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap/
git restore  ap.txt
