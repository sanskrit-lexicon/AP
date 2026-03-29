
readme_dalglob1.txt

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue12  # home


# cd to local hwnorm2 repo
cd /c/xampp/htdocs/cologne/hwnorm2/

git pull
# Already up to date
-----------------------------
Add fri to dictlist.txt.

-----------------------------
# make all data/xxx_hws.txt files
cd keydoc/distincthws
sh redo.sh
# note for ap, there are 4 instances with unknown characters
# note for fri, there are numerous instances with unknown characters.

------------------------------
## remake keydoc/keydoc_glob1.sqlite locally
cd /c/xampp/htdocs/cologne/hwnorm2/
sh redo.sh xampp  # local

-------------------------------------------------------
# push hwnorm2 to Github
cd /c/xampp/htdocs/cologne/hwnorm2/
git add .
git commit -m "Revise hwnorm1 for ap,fri"
Ref: https://github.com/sanskrit-lexicon/ap/issues/12"
git push

------------------------------------------------------
# Cologne installation:
# connect to Cologne server
# cd to hwnorm2 repo
git pull
# remake keydoc/keydoc_glob1.sqlite
# this takes a while!
sh redo.sh cologne


