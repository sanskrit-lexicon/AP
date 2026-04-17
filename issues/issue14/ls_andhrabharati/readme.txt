
Begin 04-01-2026 Activate link targs

 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati #home

 Ref: https://github.com/sanskrit-lexicon/AP/issues/14#issuecomment-4246192806
* history of ap tooltips file in csl-pywork/v02
cd /c/xampp/htdocs/cologne/csl-pywork

git log --follow --pretty=format:"%ad %h %an %s" --date=short -- v02/distinctfiles/ap/pywork/apauth/tooltip.txt > temp_history_ap_tooltip.txt

2026-04-13 6dfeba7 funderburkjim AP: Edits of ap ls tooltips Ref: https://github.com/sanskrit-lexicon/AP/issues/14
2026-02-01 2ab228f funderburkjim ap: edits to ls tooltips Ref: https://github.com/sanskrit-lexicon/AP/issues/2#issuecomment-3827450873
2026-01-30 2599fa7 funderburkjim ap: Activate ls tooltips Ref: https://github.com/sanskrit-lexicon/AP/issues/2

* All 3 versions of tooltips.xt for ap in csl-pywork repo
cd /c/xampp/htdocs/cologne/csl-pywork
# 2026-01-30
git show 2599fa7:v02/distinctfiles/ap/pywork/apauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati/temp_tooltip_2599fa7.txt

# 2026-02-01 
git show 2ab228f:v02/distinctfiles/ap/pywork/apauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati/temp_tooltip_2ab228f.txt

diff temp_tooltip_2ab228f.txt ../tooltips_0.txt | wc -l
# 0 

# 2026-04-13
git show 6dfeba7:v02/distinctfiles/ap/pywork/apauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue14/ls_andhrabharati/temp_tooltip_6dfeba7.txt

diff temp_tooltip_6dfeba7.txt ../tooltips_3.txt | wc -l
#542
But
diff -w temp_tooltip_6dfeba7.txt ../tooltips_3.txt | wc -l
# 0
python unixify.py ../tooltips_3.txt  tooltips_3_unix.txt
diff temp_tooltip_6dfeba7.txt tooltips_3_unix.txt | wc -l
# 0

# Andhrabharati's file:
cp ../../issue2/AP57.list.of.sources.as.printed.txt  AP57.list.of.sources.as.printed.txt

# unixify AB's file, make a shorter name
python unixify.py AP57.list.of.sources.as.printed.txt AB_tooltips.txt
# 277 lines written to AB_tooltips.txt

# remove title lines in AB file
cp AB_tooltips.txt AB_tooltips_a.txt
# manual edit of AB_tooltips_a.txt
wc -l AB_tooltips_a.txt
269 AB_tooltips_a.txt


# tooltips_3_sort.txt:  sort of tooltips_3_unix.txt
python tooltip_sort.py tooltips_3_unix.txt tooltips_3_sort.txt
269 lines written to tooltips_3_sort.txt

# AB_tooltips_b.txt: sort of AB_tooltips_a.txt  
python tooltip_sort.py AB_tooltips_a.txt AB_tooltips_b.txt  
# 269 lines

* initial raw comparison of AB_tooltips_b.txt AND tooltips_3_sort.txt
diff AB_tooltips_b.txt  tooltips_3_sort.txt > diff_AB-b_cdsl-3.txt
wc -l diff_AB-b_cdsl-3.txt
375 diff_AB-b_cdsl-3.txt  # so about 100 differences


* compare abbreviations AB_tooltips_b.txt AND tooltips_3_sort.txt
python compare_abbrev.py AB_tooltips_b.txt tooltips_3_sort.txt compare_abbrev_b_3.txt
1 duplicate abbrevs in AB_tooltips_b.txt
0 duplicate abbrevs in tooltips_3_sort.txt
37 unique in AB_tooltips_b.txt
39 unique in tooltips_3_sort.txt
85 lines written to compare_abbrev_b_3.txt


* AB_tooltips_c.txt revision of AB_tooltips_b.txt
cp AB_tooltips_b.txt AB_tooltips_c.txt
**  manual revisions of AB_tooltips_c.txt based on compare_abbrev_b_3.txt
1. remove duplicate abbrev: Uṇ.	Uṇādisūtras.
2. Change Abbrevs based on tooltip

* compare abbreviations AB_tooltips_c.txt AND tooltips_3_sort.txt
python compare_abbrev.py AB_tooltips_c.txt tooltips_3_sort.txt compare_abbrev_c_3.txt
0 duplicate abbrevs in AB_tooltips_c.txt
0 duplicate abbrevs in tooltips_3_sort.txt
24 unique in AB_tooltips_c.txt
26 unique in tooltips_3_sort.txt
60 lines written to compare_abbrev_c_3.txt

diff  AB_tooltips_b.txt  AB_tooltips_c.txt > AB_tooltips_diff_b_c.txt

* AB_tooltips_d.txt, tooltips_4.txt revision of AB_tooltips_c.txt
cp AB_tooltips_c.txt AB_tooltips_d.txt
cp tooltips_3_sort.txt tooltips_4.txt
## manual revisions, primarily of abbreviations.
## purpose is to get versions of AB and CDSL that have identical abbreviations.
** ----- Instance 1
front-matter vol1 page 12 Dāy., Dāy. B  Dāyabhāga
   ap.txt <ls>Dāy. B.</ls> (7)  
AB: Day.	Dayabhāga.   change
AB: Day. B.	Dayabhāga.   change
cdsl: Dāy.	Dāyabhāga.   No instances
cdsl: Dāy. Bh.	Dāyabhāga.   change 
** ----- Instance 2
AB:   Ghat.	Ghatakarparakāvya.
cdsl: Ghaṭ.	Ghaṭakarparakāvya.
Gawakarpara is name of author
ap.txt <ls>Ghat. (22) 
change AB

** ----- Instance 3
AB:   I. B.	Inscriptions of Bengal, Vol. III by N. G. Mujumdar.
cdsl: I B.	Inscriptions of Bengal, Vol. III by N. G. Mujumdar.
  frontmatter vol3, p.4 agrees with cdsl
  change AB
** ----- Instance 4
AB:   Mātaṅga.	Mātaṅgalīlā of Nīlakaṇṭha.
cdsl: Mātaṅga. L.	Mātangalīlā of Nīlakaṇṭha.
frontmatter print: agrees with AB.
ap.txt <ls>Mātaṅga L.  (93)
change AB and cdsl to "Mātaṅga L."
** ----- Instance 5
AB:   Sid. Mukt.	Siddhāntamuktāvali.
      Sid. Muktā.	Siddhāntamuktāvali.
cdsl: Sid. Mukt.	Siddhāntamuktāvalī.
      Muktā.	Siddhāntamuktāvalī.
frontmatter: "Sid. Mukt. or  Muktā. = Siddhāntamuktāvalī"
ap.txt  <ls>Sid. Mukt.</ls> (1)
        <ls>Muktā.</ls>  (4) [hws= apara, amUrta, aBAva, BaktirasaH]
solution: change AB "Sid. Muktā." to "Muktā."
** ----- Instance 6
AB:   Muṇḍa.	Muṇḍakopaniṣad, ({#सार्थ उपनिषत्संग्रह, ह. र. भागवत, १९१४#}).
cdsl: Muṇḍ.	Muṇḍakopaniṣad, (सार्थ उपनिषत्संग्रह—ह. र. भागवत, १९१४).
frontmatter: agrees with AB
ap.txt <ls>Muṇḍ.  (49)      (no matches for <ls>Muṇḍa.)
Solution: change AB to Muṇḍ.
** ----- Instance 8
AB:   Pād. D.	Pādaṅkadūta.
cdsl: Pad. D.	Padānkadūta.
frontmatter print: = cdsl
  MW: padANkadUta  name of poem
ap.txt <ls>Pād. D.   (0) no instances
ap.txt <ls>Pad. D.   (3)
abbrev = "Pad. D."  (change AB)
change cdsl: Pad. D.	Padāṅkadūta.
change   ab:   the same
** ----- Instance 9
cdsl: MW.	Monier-Williams Sanskrit-English Dictionary, 1899
 not in frontmatter.  cdsl addition.
Add to AB
** ----- Instance 10
AB:   Pari. Śekh.	Paribhāṣeṇḍūśekhara.
      Pbh.	Paribhāṣeṇḍūśekhara.
cdsl: Pari. Śekh, Pbh.	Paribhāṣenduśekhara.
front-matter same as cdsl
ap.txt <ls>Pari. Śekh.  (4)
       <ls>Pbh.   (0)
change cdsl to AB
** ----- Instance 11
AB:   Pradīp.	Mahābhāsya-Pradīpa (Kaiyaṭa).
cdsl: Pradip.	Mahābhāṣya‑Pradīpa (Kaiyaṭa).
frontmatter print = cdsl
change cdsl abbrev to "radīp."
change AB tooltip to "Mahābhāṣya‑Pradīpa (Kaiyaṭa)."
no ap.txt matches for either "<ls>Pradīp." or "<ls>Pradīp."
** ----- Instance 12
AB:   Praśna Up.	Praśnopaniṣad, ({#सार्थ उपनिषत्संग्रह, ह. र. भागवत, १९१४#}).
cdsl: Praśna. Up.	Praśnopaniṣad, (सार्थ उपनिषत्संग्रह—ह. र. भागवत, १९१४).
frontmatter print: "Praśna, Up."
ap.txt: <ls>Praśna. Up.   (28)
       <ls>Praśna. 2. 6</ls> (1)
changes:
1. change AB abbrev to "Praśna. Up."
2. change cdsl tooltip to AB
3. add new line to AB and cdsl:
Praśna.	Praśnopaniṣad, ({#सार्थ उपनिषत्संग्रह, ह. र. भागवत, १९१४#}).
** ----- Instance 13 Ṛitusaṃhāra
AB:   Ṛ. S.	Ṛtusamhāra, (V.R. Nerurkar, Bombay, 1916).
cdsl: R. S.	Ṛtusamhāra, (V.R. Nerurkar, Bombay, 1916).
frontmatter:
   print "R. S. = cdsl (fm vol. 1)   
     
ap.txt <ls>Ṛs.  (224)
       <ls>Rs.  (0)
       <ls>R. S. (0)
       <ls>Ṛ. S. (0)
Solution: change  cdsl to AB
** ----- Instance 14 Rv.
AB:   Ṛv.	Ṛgveda, (Pandita Satawalekar and V. S. Mandala, Poona).
cdsl: Rv.	Ṛigveda, (Pandita Satawalekar and V. S. Mandala, Poona).
fronmatter agrees with cdsl. 
ap.txt uses Rv.  abbreviation.
changes:
 - AB abbrev -> Rv.
 - cdsl tooltip Ṛigveda -> Ṛgveda
** ----- Instance 15 Rv. Pr.
AB:   Ṛv. Pr.	Ṛgveda Prātiśākhya.
cdsl: Rv. Pr.	Ṛigveda Prātiśākhya.
frontmatter agrees with cdsl
ap.txt uses Rv. Pr.
changes:
 - AB abbrev -> Rv. Pr.
 - cdsl tooltip Ṛigveda -> Ṛgveda
** ----- Instance 16 
AB:   Śabda. ch.	Śabdachintāmaṇi (Sanskṛt-Gujrati Dictionary by Ramanabhai Nilkanth, 1899).
cdsl: Śabda Ch.	Śabdachintāmaṇi (Sanskrit–Gujarati Dictionary by Ramanabhai Nilkanth, 1899).
front matter: Śabda. ch.
ap.txt "Śabda. ch." (0)    "Śabda Ch." (14)
changes:
 AB: abbrev -> Śabda Ch.
Tooltip for AB/cdsl:
Śabdacintāmaṇi (Sanskṛt-Gujrati Dictionary by Ramanabhai Nilkanth, 1899).
** ----- Instance 17
AB:   Śalihotra	Śalihotra of Bhoja, edited by Dr. E. D. Kulkarni.
cdsl: Śālihotra	Śālihotra of Bhoja, edited by Dr. E. D. Kulkarni.
frontmatter abbrev: (vol 3) Śālihotra
ap.txt Śālihotra (24)
MW has SAlihotra as author/work
change: AB -> cdsl
** ----- Instance 18
AB:   Sān. K.	Sānkhyakārikā.
cdsl: Sāṅ. K.	Sāṅkhyakārikā.
frontmatter: Sān. K.
ap.txt "<ls>Sān. K."  (0) ;   "<ls>Sāṅ\. K\." (94)
MW: sāṃkhyakārikā   (uses ṃ instead of ṅ -- optional)
change:  AB -> cdsl
** ----- Instance 19 ?
AB:   Sān. S.	Sānkhyasūtra.
cdsl: Sāṅ. S.	Sāṅkhyasūtra.
frontmatter: 
ap.txt Sān. S. (0);  Sāṅ. S. (2)
BUT: AP print differs from AP txt
  abudDa  AP print  Sān. S.
  BOtika  AP print  Sāṅkhya S.
change AB -> cdsl: Questionable!

** ----- Instance 20
AB:   Sānkhya. K.	Sānkhyakārikā.
cdsl: Sāṅkhya. K.	Sāṅkhyakārikā.
frontmatter = AB
ap.txt "Sānkhya. K."  (0); "Sāṅkhya. K."  (0)
change:  AB -> cdsl.  The Abbreviation is irrelevant (no instances)
        The tooltip spelling is corrected to IAST
** ----- Instance 21
AB:   Tarka. K.	Tarkakaumudī, (Bombay).
cdsl: Tarka K.	Tarkakaumudī, (Bombay).
frontmatter: Tarka. K.  
ap.txt  Tarka. K.  (0);  Tarka K. (32)
  ap print check (4 random of the 32)
   arTApattiH  "Tarka. K."  disagree with cdsl
   upanayaH "Tarka K."      agree with cdsl
   liNgam  "Tarka K."       agree with cdsl
   sAmAnyalakzaRam "Tarka K." agree with cdsl
conclude: AP inconsistency.  cdsl acceptable
change: AB -> cdsl
** ----- Instance 22
AB:   Vai. Bhū. ({#वै˚ भू˚#}).[tab]Vaiyākaraṇabhūṣaṇasāra.
cdsl: Vai. Bhū.[tab](वै. भू.) Vaiyākaraṇa‑bhūṣaṇa‑sāra.
frontmatter: "Vai. Bhū. ({#वै भू#})"
ap.txt  no instances found of "Vai" or "वै"  
change: cdsl -> ab
** ----- Instance 23
AB:   Viś. Guṇa.	Viśvaguṇādarśachampū, (Nirṇaya Sāgara, 1915).
cdsl: Viś. Guṇā.	Viśvaguṇādarśacampū, (Nirṇaya Sāgara, 1915).
frontmatter: Viś. Guṇa.
ap.txt "Viś. Guṇa." (0);  "Viś. Guṇā." (55)
  ap print checks (6 of 55)
   anDa  Viś. Guṇa.     = AB
   uditvara Viś. Guṇā.  = cdsl
   GumaGumita Viś. Guṇā.= cdsl
   prakaraH Viś. Guṇa.  = AB
   vanI     Viś. Guṇa.  = AB
   sOmuKyam Viś. Guṇa.  = AB
conclude: AP print inconsistent.
   ap.txt consistent.  and "Guṇā." consistent with tooltip
change: AP -> cdsl
** ----- Instance 24
AB:   Vṛnd. Ś.	Vṛndāvanaśataka.
cdsl: Vṛind. S.	Vṛndāvanaśataka.
frontmatter: abbrev = Vṛind. S.
ap.txt "Vṛind. S." (0);  "Vṛnd. Ś." no instances
conclude:  cdsl -> AB
** ----- Instance 25
AB  (not present)
cdsl: Wilson	Wilson Sanskrit-English Dictionary
not present in AB.
ap.txt <ls>Wilson</ls> (9)
change: add to AB
** ----- Instance 26
cdsl: X	Chap. II and III, (Oriental Publishing Company, Bombay, 1912).
The tooltip is part of Pt. abbreviation.
change:  drop from cdsl
* compare abbreviations AB_tooltips_d.txt AND tooltips_4.txt DONE!
python compare_abbrev.py AB_tooltips_d.txt tooltips_4.txt compare_abbrev_d_4.txt

0 duplicate abbrevs in AB_tooltips_d.txt
0 duplicate abbrevs in tooltips_4.txt
0 unique in AB_tooltips_d.txt
0 unique in tooltips_4.txt
10 lines written to compare_abbrev_d_4.txt

Abbreviations match.
diff AB_tooltips_c.txt AB_tooltips_d.txt > diff_AB_tooltips_c_d.txt
# 69 lines in file

diff tooltips_3_sort.txt tooltips_4.txt > diff_tooltips_3sort_4.txt
# 46 lines in file

* compare tooltips_d_4.txt
# we know AB_tooltips_d.txt and tooltips_4.txt  agree in abbreviation.
# Now compare the tooltip for each abbreviation.

python compare_tooltips.py AB_tooltips_d.txt tooltips_4.txt compare_tooltips_d_4.txt
100 differences
3
* AB_tooltips_e.txt and tooltips_5.txt agree in abbrev and tooltips
cp AB_tooltips_d.txt AB_tooltips_e.txt
cp tooltips_4.txt tooltips_5.txt
# manually edit both using the 100 differences in 
# compare_tooltips_d_4.txt
# then do further review, focusing on iast spellings of works and authors
# after a couple of iterations the differences removed
python compare_tooltips.py AB_tooltips_e.txt tooltips_5.txt compare_tooltips_e_5.txt

0 differences
0 lines written to compare_tooltips_e_5.txt

diff AB_tooltips_d.txt AB_tooltips_e.txt > diff_AB_tooltips_d_e.txt
# 253 lines in diff_AB_tooltips_d_e.txt
diff tooltips_4.txt tooltips_5.txt > diff_tooltips_4_5.txt
# 321 lines in diff_tooltips_4_5.txt

* cp tooltips_5.txt ../tooltips_5.txt 
  return to issue14/readme.txt to install
* ap.txt 1 change 
 <L>16848.308<pc>0791-1<k1>trimaDu<k2
old: 
three verses of the Ṛgveda (<ls n="Ṛv.">1. 90. 6-8</ls>
new:
three verses of the Ṛgveda (<ls n="Rv.">1. 90. 6-8</ls>
* ap.txt change ? Instance 19

* THE END
