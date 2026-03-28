
readme_hwnorm1.txt

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12  # home


Update sanhw1.txt, hwnorm1c.txt, and hwnorm1c.sqlite
This is done in local hwnorm1 repo

cd /c/xampp/htdocs/cologne/hwnorm1/sanhw1/
git pull
# 
# Follow instructions in readme.txt:
sh redo.sh
mv hwnorm1c.sqlite ../../csl-apidev/simple-search/hwnorm1/

-------------------------------------------------------
# push hwnorm1 to Github
git add .
git commit -m "Revise hwnorm1 for AP alternate and compound headwords.
Ref: https://github.com/sanskrit-lexicon/ap/issues/12"
git push

-------------------------------------------------------
cd /c/xampp/htdocs/cologne/csl-apidev
# push csl-apidev to Github
git pull
# Already up to date
git add .
git commit -m "Revise hwnorm1c.sqlite for AP alternate and compound headwords.
Ref: https://github.com/sanskrit-lexicon/ap/issues/12"
git push

---------------------------------------------------------
# connect to Cologne
cd hwnorm1
git pull
cd ../csl-apidev
git pull



