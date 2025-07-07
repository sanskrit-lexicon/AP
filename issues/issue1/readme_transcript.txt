pwd
/c/xampp/htdocs/cologne/csl-orig/v02

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02 (master)
$ cd ap

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cd /c/xampp/htdocs/cologne/csl-orig/v02/ap

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_01.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ap.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../../.gitignore


jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cd ../../

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   v02/ap/ap.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore


jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ git restore --staged v02/ap/ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        v02/ap/

no changes added to commit (use "git add" and/or "git commit -a")

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ git add .gitignore

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ git commit -m "AP: change csl-orig .gitignore to track ap.
> Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 3dc4328] AP: change csl-orig .gitignore to track ap. Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 1 insertion(+), 1 deletion(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        v02/ap/

nothing added to commit but untracked files present (use "git add" to track)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ ls v02/ap/
ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig (master)
$ cd /c/xampp/htdocs/cologne/csl-orig/v02/ap

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_01.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ./

nothing added to commit but untracked files present (use "git add" to track)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add .

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ap.txt


jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap_01.txt  (Fri Jan 24 16:13:52 2020)      initial commit
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 5a7a84a] AP: ap_01.txt  (Fri Jan 24 16:13:52 2020)      initial commit Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 341287 insertions(+)
 create mode 100644 v02/ap/ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_13.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap_13.txt  (Tue Jun 1 16:27:23 2021)       diff_01_02.txt - diff_12_13.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 1c7fdda] AP: ap_13.txt  (Tue Jun 1 16:27:23 2021)       diff_01_02.txt - diff_12_13.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 126 insertions(+), 121 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_14.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add ap.txt
git commit -m "AP: ap_14.txt    (Sun Jun 13 13:25:43 2021)      diff_13_14.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 01a8f08] AP: ap_14.txt  (Sun Jun 13 13:25:43 2021)      diff_13_14.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 61204 insertions(+), 61204 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_15.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap_15.txt  (Sun Jun 13 17:10:22 2021)      diff_14_15.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 78fc3eb] AP: ap_15.txt  (Sun Jun 13 17:10:22 2021)      diff_14_15.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 7724 insertions(+), 7724 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_16.txt ap.txt
git add ap.txt
git commit -m "AP: ap_16.txt    (Sat Jun 19 15:44:14 2021)      diff_ap_15_16.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master b91472c] AP: ap_16.txt  (Sat Jun 19 15:44:14 2021)      diff_ap_15_16.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 2256 insertions(+), 2256 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_17.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap_17.txt  (Wed Jun 23 15:39:27 2021)      diff_ap_16_17.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master a339eb3] AP: ap_17.txt  (Wed Jun 23 15:39:27 2021)      diff_ap_16_17.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 5 insertions(+), 5 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_18.txt ap.txt
git add ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap_18.txt  (Sat Jul 3 20:51:45 2021)       diff_ap_17_18.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 8e8b272] AP: ap_18.txt  (Sat Jul 3 20:51:45 2021)       diff_ap_17_18.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 7811 insertions(+), 7811 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_19.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap_19.txt  (Thu Jul 8 12:31:58 2021)       diff_ap_18_19.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 2102691] AP: ap_19.txt  (Thu Jul 8 12:31:58 2021)       diff_ap_18_19.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 8391 insertions(+), 8391 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp /e/ap_open/commits/ap_28.txt ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add ap.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap_28.txt  (Tue Jul 16 14:08:09 2024)      diff_ap_19_20.txt - diff_27_28.txt
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 966d79f] AP: ap_28.txt  (Tue Jul 16 14:08:09 2024)      diff_ap_19_20.txt - diff_27_28.txt Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 1 file changed, 80 insertions(+), 80 deletions(-)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ ls ../temp_ap_20250701/
ap-meta2.txt  ap.txt  ap_hwextra.txt  apheader.xml  readme.txt  temp_ap_bb14a97e4.txt  temp_verbs01/

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ diff ap.txt ../temp_ap_20250701/ap.txt | wc -l
0

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cd /c/xampp/htdocs/cologne/csl-orig/v02/ap

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp ../temp_ap_20250701/ap-meta2.txt .

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 10 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ap-meta2.txt

nothing added to commit but untracked files present (use "git add" to track)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp ../temp_ap_20250701/ap_hwextra.txt .

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ cp ../temp_ap_20250701/apheader.xml  .

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 10 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ap-meta2.txt
        ap_hwextra.txt
        apheader.xml

nothing added to commit but untracked files present (use "git add" to track)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 10 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ap-meta2.txt
        ap_hwextra.txt
        apheader.xml

nothing added to commit but untracked files present (use "git add" to track)

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git add .

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git commit -m "AP: ap-meta2.txt,  ap_hwextra.txt,  apheader.xml
Ref: https://github.com/sanskrit-lexicon/AP/issues/1"
[master 592843b] AP: ap-meta2.txt,  ap_hwextra.txt,  apheader.xml Ref: https://github.com/sanskrit-lexicon/AP/issues/1
 3 files changed, 231 insertions(+)
 create mode 100644 v02/ap/ap-meta2.txt
 create mode 100644 v02/ap/ap_hwextra.txt
 create mode 100644 v02/ap/apheader.xml

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 11 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 11 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$ git push
Enumerating objects: 58, done.
Counting objects: 100% (58/58), done.
Delta compression using up to 16 threads
Compressing objects: 100% (45/45), done.
Writing objects: 100% (55/55), 5.63 MiB | 1.10 MiB/s, done.
Total 55 (delta 29), reused 1 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (29/29), completed with 2 local objects.
To https://github.com/sanskrit-lexicon/csl-orig.git
   c3cbf0b..592843b  master -> master

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/cologne/csl-orig/v02/ap (master)
$
