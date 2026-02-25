apfile="$1"
appdir="$2"
# regenerate local displays from "$apfile"
# use revised make_xml.py and revised basicadjust.php
cp make_xml.py /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/make_xml.py
cp basicadjust.php /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php

cp basicadjust.php /c/xampp/htdocs/cologne/csl-apidev/basicadjust.php

cp $apfile /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap ../../${appdir}
# sh xmlchk_xampp.sh ap
python3 ../../xmlvalidate.py ../../${appdir}/pywork/ap.xml ../../${appdir}/pywork/ap.dtd
# restore ap.txt in csl-orig
echo "restoring ap.txt in csl-orig"
cd /c/xampp/htdocs/cologne/csl-orig/v02/ap/
git restore ap.txt

echo "RESTORE make_xml.py"
cd  /c/xampp/htdocs/cologne/csl-pywork/
#git status
git restore .
#git status

echo "RESTORE basicadjust.php in csl-websanlexicon"
cd  /c/xampp/htdocs/cologne/csl-websanlexicon/
#git status
git restore .
#git status

echo "RESTORE basicadjust.php in csl-apidev"
cd  /c/xampp/htdocs/cologne/csl-apidev/
#git status
git restore .
#git status

