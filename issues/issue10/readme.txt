
03-10-2026  Begin compounds

 
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10 #home

* --------------------------------
* temp_v4a_0g.txt -- latest Jim revision of AB version v4a.
cp ../issue8e/temp_v4a_0g.txt temp_v4a_0g.txt
* ==========================================
* tempwork/ap_0.txt start with this revision of ap.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git log | head -n 1
# commit 4d8780b431fcb32d61a00334420549e6d9544aaa

git show 4d8780b4:v02/ap/ap.txt > /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10/tempwork/ap_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10/
* ==========================================
* explore1.py option 1 format
filter all entries with compounds (4455 such entries)
1 line per entry
3 fields (colon separated)
L cologne entry id 
k1 cologne entry citation word
nc number of compounds (using regex: ^\.{@{#(.*?)#}@})
* Explore 1 tempwork/ap_0.txt
4461 matches for "^\.━{@<ab>Comp.</ab>@}" in buffer: ap_0.txt
 (there is one other <ab>Comp.</ab>, but not related to compound headwords

#python explore1.py 1 tempwork/ap_0.txt tempwork/temp_explore1_1.txt

* tempwork/ap_0a.txt
cp tempwork/ap_0.txt tempwork/ap_0a.txt
Manual changes 
-------
25 matches for ".━{@<ab>Comp.</ab>@} {@{#.*?#}@}
 Put ".{@{#X#}@} on next line
-------
remove duplicate .━{@<ab>Comp.</ab>@}   print changes
<L>4331<pc>0211-1<k1>ayAta<k2>ayAta
<L>11860<pc>0552-1<k1>kAkaH
<L>12031<pc>0560-2<k1>kAraka
<L>27309<pc>1330-1<k1>ramBA
<L>33058<pc>1599-2<k1>sakala
<L>33353<pc>1612-2<k1>satata

python diff_to_changes_dict.py tempwork/ap_0.txt tempwork/ap_0a.txt change_ap_0_0a.txt
85 lines changed

* Explore 1 tempwork/ap_0a.txt
4455 matches for "^\.━{@<ab>Comp.</ab>@}" in buffer: ap_0.txt
 (there is one other <ab>Comp.</ab>, but not related to compound headwords

python explore1.py 1 tempwork/ap_0a.txt tempwork/temp_explore1_1.txt
# 4455 entries from tempwork/ap_0a.txt
** 33 entries with 100+ compounds
243:agniH:147
2334:antar:137
4564:arTaH:106
4582:arDa:103
5890:aSvaH:120
6780:Atman:111
10632:eka:247
11989:kAmaH:103
12123:kAla:126
14268:go:185
15466:jala:170
16848:tri:196
17389:dur:222
17517:deva:192
17799:dvi:129
17918:DarmaH:145
18923:nir:324
19379:nis:144
19732:paYcan:158
19937:para:136
22345:prati:196
24298:Palam:104
24530:bahu:137
24789:brahman:202
25237:BUta:109
25646:maDu:118
25943:mahA:465
26885:yaTA:139
27379:rAjan:161
28143:lokaH:114
28407:vanam:107
34421:sarva:120
35088:su:389

**  8 entries with 90-99 compounds
* tempwork/ap_0b.txt
cp tempwork/ap_0a.txt tempwork/ap_0b.txt
Manual changes to tempwork/ap_0b.txt
 In conjunction
-------
<L>138<pc>0007-1<k1>akzaH
.{@{#-kovida#}@}, {#-jYa#} -> .{@{#-kovida, -jYa#}@}
-------
22 matches for "[^0-9]:[a-zA-Z]" in buffer: temp_explore1_2.txt
 Most compound entries start with '-'
17 changes
-------
8 matches in 7 lines for ", [^-]" in buffer: temp_explore1_2.txt
<L>2335<pc>0122-1<k1>antara
old: 
.{@{#-diSA, antarA dik#}@}
new:
.{@{#-diSA#}@}, {@{#antarA dik#}@}
-------
22 matches in 21 lines for "˚" in buffer: temp_explore1_2b.txt
THESE NOT YET HANDLED

-----------------------------------------------------------
python diff_to_changes_dict.py tempwork/ap_0a.txt tempwork/ap_0b.txt change_ap_0a_0b.txt
85 lines changed


* explore1.py option 2 format
filter for entries with compounds (4455 such entries)
one line per each compound (identified '^\.{@{#(.*?)#}@}'(
4 fields (colon separated)
L cologne entry id 
k1 cologne entry citation word
b  '^\.{@{#b#}@}'
p  k1+b computed (initially empty string) [a comma-separated list]

* tempwork/temp_explore1_2a.txt

python explore1.py 2 tempwork/ap_0a.txt tempwork/temp_explore1_2a.txt
4455 records written to tempwork/temp_explore1_2a.txt
wc -l tempwork/temp_explore1_2a.txt
34176 

* tempwork/temp_explore1_2b.txt

python explore1.py 2 tempwork/ap_0b.txt tempwork/temp_explore1_2b.txt
4455 records written to tempwork/temp_explore1_2b.txt
wc -l tempwork/temp_explore1_2b.txt
34176 

* tempwork/ap_0c.txt
# expand compound-headwords with parenthetical alternates
# There are about 130 such
# prepare an intermediate version ap_0c_prep.txt which
# marks the lines such lines.  
#  (the 'mark' is a '_' at start of such lines.)
# This makes the revision process more efficient.
python explore1_variant.py 2 tempwork/ap_0b.txt temp.txt tempwork/ap_0c_prep.txt

# Now ap_0c_prep.txt is manually edited.
# When done, remove the 'mark', and save as 
# tempwork/ap_0c.txt

# change file
python diff_to_changes_dict.py tempwork/ap_0b.txt tempwork/ap_0c.txt change_ap_0b_0c.txt
136 changes written to change_ap_0b_0c.txt

* tempwork/temp_explore1_2_0c.txt
python explore1.py 2 tempwork/ap_0c.txt tempwork/temp_explore1_2_0c.txt
* tempwork/parse2_0c.txt
# Construct purvapada from k1
# Use ScharfSandhi code to join purva-pada and para-padas
python parse2.py tempwork/temp_explore1_2_0c.txt tempwork/parse2_0c.txt
4455 records written to tempwork/temp_explore1_2_0d.txt
* tempwork/ap_0d.txt
# Recode compounds with '˚' symbol. About 30 instances.
cp tempwork/ap_0c.txt tempwork/ap_0d.txt
Manual edit tempwork/ap_0d.txt in lines matching
 "^\.{@{#[^#]*˚.*?#}@}"   (34 matches)
  [Note some of these 34 do NOT occur after <ab>Comp.</ab>]

# change file
python diff_to_changes_dict.py tempwork/ap_0c.txt tempwork/ap_0d.txt change_ap_0c_0d.txt
24 changes written to change_ap_0c_0d.txt
* tempwork/temp_explore1_2_0d.txt
python explore1.py 2 tempwork/ap_0d.txt tempwork/temp_explore1_2_0d.txt
* tempwork/parse2_0d.txt  All are parsed
# Construct purvapada from k1
# Use ScharfSandhi code to join purva-pada and para-padas
python parse2.py tempwork/temp_explore1_2_0d.txt tempwork/parse2_0d.txt

* parse2_0d_dictcheck.txt
# dictcheck using dalglob
python dalglobpy/dictcheck.py tempwork/parse2_0d.txt tempwork/parse2_0d_dictcheck.txt

3473 matches in 3310 lines for "\?" in buffer: parse2_0d_dictcheck.txt

* parse2_0d_dictcheck.txt observations
 akutas  
91:akutaH:-calaH:akutacalaH?   akutaScalaH
91:akutaH:-Baya:akutaBaya?     akutoBaya
243:agniH:-carRam:agnicarRam?  gunpowder  cUrRa  changed
255:agra:-nIH:agranIH? how to code? .{@{#-nIH#}@} ({@{#-RIH#}@})
255:agra:-BUH:agraBUH?  agraBU why not found by dictcheck?
305:aNgam:-BUH:aNgaBUH? aNgaBU why not found by dictcheck?
1022:aDas:-BUH:aDoBUH?  aDoBU f. pd
260:agre:-pAH:agrepAH?  agrepA why not found by dictcheck?
260:agre:-pUH:agrepUH?  agrepU why not found by dictcheck?
1249:aDvara:-SrIH:aDvaraSrIH? aDvaraSrI why not found by dictcheck?
1249:aDvara:-samizwayajuH:aDvarasamizwayajuH? aDvarasamizwayajus why not found by dictcheck?
260:agre:-vanam, -Ram:agrevanam,agreRam
300:aNkowaH:-sAra:aNkowasAra?  mw aNkollasAra
341:aNguliH:-tAraRam:aNgulitAraRam?  toraRa  print chg.
360:acala:-patiH, -rAw:acalapatiH,acalarAw?  acalarAj
419:ajara:-drumaH:ajaradrumaH?
419:ajara:-rA:ajararA?   not a compound but ajarA
419:ajara:-ram:ajararam? not a compound but ajaram
449:ajIta:-punarvarRyam:ajItapunarvarRyam?   print change --vaRyam pw,pd,sch
489:aYjas:-pA:aYjaHpA?  mw aYjaspA  (sandhi optional Hp or sp ?)
531:aRu:-vratAni:aRuvratAni?  pl. of aRuvrata
889:aTa:-ataH, -anantaram:aTAtaH?,aTAnantaram   aTAtas  how to change?
896:aTarvan:-BUtAH:aTarvaBUtAH?  pl. aTarvaBUta not found by dictcheck
971:adDA:-boDeyAH:adDAboDeyAH?  pl. not found
1022:aDas:-Saya, -Sayya:aDaSSaya?,aDoyya?  MW aDaHSaya, aDaHSayya
1022:aDas:-sTa, -sTita:aDassTa?,aDassTita?  MW aDaHsTa,aDaHsTita
1022:aDas:-svastikam:aDassvastikam?  MW aDaHsvastikam

1251:aDvaryuH:-kARqamaM:aDvaryukARqamaM? print change -kARqamaM -> -kARqam
2408:anyataH:-araRyam:anyatAraRyam?  anyatoraRya
2408:anyataH:-eta, -etas, -enI:anyatEta?,anyatEtas?,anyatEnI?
2704:aparAYc:-muKa:aparAYNmuKa? sandhi err? aparANmuKa  
3414:aBitas:-asTi:aBito'sTi   Avagraha should be removed in citation key1
4190:amitraH:-KAd:amitraKAd?  KAd -> KAda print change
4289:amla:-jambIraH, -nimbakaH:amlajambIraH,amlanimbakaH? nimbakaH -> nimbUkaH print change

4662:alam:-karmIRa:alakarmIRa?   Error in parse2 and dictcheck. alam+
5428:avAk:-SAKaH:avAkCAKaH?  MW avAkSAKa  optional sandhi?
5428:avAk:-Siras:avAkCiras?  MW avAkSiras optional sandhi?
5890:aSvaH:-cikisA:aSvacikisA?  -cikitsA pring change

10255:uBayataH:-kzRut:uBayatakzRut?  Don't drop 'H'
10273:uraRaH:-Ram:uraRaRam?  Not a compound.  How to code?
11989:kAmaH:-aDizwita:kAmADizwita? Dizwita -> DizWita print change
12240:kim:-ja:kija?  don't drop 'm'
13772:gaRita:-tam:gaRitatam?  Not a compound: gaRitam
udvigna compounds not marked  <L>9231<pc>0434-1<k1>udvigna<k2>udvigna
go subcompounds of -paH  <L>14268<pc>0671-1<k1>go
14641:catur:-zkAzWam:catuzzkAzWam?
14716:cara:-ram:cararam?
15140:cEtanyam:-nyaH:cEtanyanyaH?  not a compound: cEtanyaH
15344:jawa:-cIraH, -waNkaH, -wIraH, -DaraH etc. cpds of jawA?
16748:tejas:-kara:tejaHkara?  tejaskara
16748:tejas:-padam:tejaHpadam? tejaspada 
16835:trayas:-zazwiH:trayazzazwiH?  trayaHzazwiH  MW
16835:trayas:-saptAtiH:trayassaptAtiH? trayaHsaptAtiH  MW
17421:dus:-SaMsa:duSSaMsa? MW duHSaMsa
17421:dus:-zWu:duzzWu?  MW duHzWu
17421:dus:-saMcAra:dussaMcAra?  MW duHsaMcAra
17611:dos:-SAlin:doSSAlin?  MW doHSAlin
17611:dos:-sahasraBft:dossahasraBft?  MW doHsahasraBft
17793:dvAr:-sTaH, -sTitaH:dvAssTaH?,dvAssTitaH?   MW dvAHs...
17881:Danus:-stamBaH:DanusstamBaH?  MW DanuHstamBaH
18319:naBas:-SvAsaH:naBaSSvAsaH? MW naBaHSvAsa
18319:naBas:-sad:naBassad? MW naBaHsad
18331:namas:-kAraH, -kftiH:namaHkAraH?,namaHkftiH? MW namaskAra, namaskfti
18400:navan:-SAktiH:navaSAktiH?   SAkti -> Sakti  print change
19379:nis:-kzatra:nizkzatra?  MW niHkzatra
19379:nis:-SaNka:niSSaNka?  MW niHSaNka
19379:nis:-sattva:nissattva?  MW niHsattva
19886:pad:-nadDA, -naDrI :  naDrI -> nadDrI  print change
19953:paraMpara:-ram:paraMpararam?  paraMparam  NOT a compound
21050:pAduka:-kAraH  -> -AkAraH  print change
21372:piRqiH:-puzpaH:piRqipuzpaH?  MW piRqIxx
21372:piRqiH:-lepaH:piRqilepaH? MW piRqIxx
21372:piRqiH:-SUraH:piRqiSUraH? MW piRqIxx
21495:puMs:-anuja:puMranuja?  pumanuja MW  (cpd base 'pum')
21558:punar:-saMBavaH:punassaMBavaH?  MW : punar + s -> punaHs
21575:puras:-karaRam, -kAraH:puraHkaraRam?,puraHkAraH MW purask...
21575:puras:-saraH:purassaraH?  MW puraHsaraH
21816:peSas:-kft:peSaHkft MW peSaskft
22297:praRipatanam:-puraHsaram, -pUrvakam:
     praRipatanapuraHsaram?,praRipatanapUrvakam?
     alternate headword praRipAta  
     MW praRipAtapuraHsaram

22791:pratyaYc:-akzam:pratyaYgakzam?  
  where are cpds of pratyaYc?
  Try changing spelling to pratyac
23824:prAc:-Siras:prAkCiras MW prAkSiras
23865:prAtar:-saMDyA:prAtassaMDyA? MW prAtaHsaMDyA
  .{@{#-saMDyA#}@} ({#prAtaHsaMDyA#})  How to exploit?
  522 matches for "^\.{@{#[^#]*#}@} ({#[^# ]*#})" in buffer: ap_0e.txt
24464:barhis:-Suzman:barhiSSuzman? MW barhiHSuzman
24464:barhis:-sad:barhissad? MW barhiHzad  NOTE 'z'!
24522:bahis:-saMsTa:bahissaMsTa?  MW bahiHsaMsTa
.{@{#BAvaMgama#}@}  not a cpd! of BAvaH
25250:BUyas:-kara:BUyaHkara?  MW BUyaskara
25359:Bos:-kAraH:BoHkAraH? MW BoskAra
25684:manas:-SIGra:manaSSIGra? MW manaHSIGra
26193:mAlatiH:-kzArakaH, -tIrajam:mAlatikzArakaH,mAlatitIrajam?
    -tIrajam -> mAlatIrajam  print change
26276:miTas:-samayaH:miTassamayaH? MW miTaHsamayaH
26276:miTas:-asambanDanyAyaH:miTo'sambanDanyAyaH? remove avagraha in k1
26650:medas:-kft:medaHkft? : MW medaskft
26650:medas:-piRqaH:medaHpiRqaH? MW medaspiRqaH
26844:yaN:-antam:yaNNantam? MW yaNantam
26946:yaSas:-kara:yaSaHkara? : MW yaSaskara
26946:yaSas:-kAyam, -SarIram:yaSaHkAyam  but MW also 26946:yaSas:-kAyam, -SarIram:yaSaHkAyam
27198:rakzas:-pASaH:rakzaHpASaH? MW rakzaspASa
27230:rajas:-SayaH:rajaSSayaH? MW rajaHSayaH
27615:retas:-sekaH:retassekaH? MW retaHsekaH
28292:vacas:-kara:vacaHkara? MW vacaskara
28456:vapus:-sravaH:vapussravaH? MW vapuHsravaH
28478:vayas:-kara:vayaHkara? MW vayaskara
28478:vayas:-saMDiH:vayassaMDiH? MW vayaHsaMDi
28994:vAr:-sTa:vAssTa? MW vaHsTa
32025:SiKaRqaH:-KaRqikA:SiKaRqaKaRqikA?  
   Not a compound. Print change remove <ab>Comp.</ab>
32591:Sreyas:-kara:SreyaHkara? MW Sreyaskara
32674:Svas:-Sreyasa:SvaSSreyasa MW SvaHSreyas
32708:zaz:-SAstrin:zawCAstrin? MW zawSAstrin
33411:sadyas:-kAlaH:sadyaHkAlaH   Note next is 'sk'
33411:sadyas:-kAlIna:sadyaHkAlIna? MW sadyaskAlIna
33411:sadyas:-SudDiH, -SOcam:sadyaSSudDiH?,sadyaSSOcam?
  MW sadyaHSudDiH, sadyaHSOcam
33411:sadyas:-snehanam:sadyassnehanam? MW sadyaHsnehana
34150:saMpUrRa:-rRaH:saMpUrRarRaH? Not cpd, 
34150:saMpUrRa:-rRam:saMpUrRarRam? Not cpd
34424:sarvatas:-SuBA:sarvataSSuBA? MW sarvataHSuBA
34778:sAmAnyataH:-dfzwam:sAmAnyatadfzwam? MW sAmAnyatodfzwa
35710:sTalam:-sTalakamalaH:sTalasTalakamalaH?
  print change: -sTalakamalaH -> -kamalaH
6089:svar:-zA:svazzA?  MW svarzA
36089:svar:-sinDu:svassinDu? MW svaHsinDu
36226:hata:-cCAyA:hatacCAyA? MW hataCAyA

* *********** ap_0e
* tempwork/ap_0e.txt
cp tempwork/ap_0d.txt tempwork/ap_0e.txt
# manual edit -- changes re dictcheck of ap_0d

python diff_to_changes_dict.py tempwork/ap_0d.txt tempwork/ap_0e.txt change_ap_0d_0e.txt
526 changes written to change_ap_0d_0e.txt

python diff_to_changes_dict.py tempwork/ap_0.txt tempwork/ap_0e.txt change_ap_0_0e.txt
842 changes written to change_ap_0_0e.txt
* tempwork/temp_explore1_2_0e.txt
python explore1.py 2 tempwork/ap_0e.txt tempwork/temp_explore1_2_0e.txt
4454 records written to tempwork/temp_explore1_2_0e.txt
* tempwork/parse2_0e.txt  
# Construct purvapada from k1
# Use ScharfSandhi code to join purva-pada and para-padas
python parse2.py tempwork/temp_explore1_2_0e.txt tempwork/parse2_0e.txt
34177 lines written to tempwork/parse2_0e.txt

* parse2_0e_dictcheck.txt
# dictcheck using dalglob
python dalglobpy/dictcheck.py tempwork/parse2_0e.txt tempwork/parse2_0e_dictcheck.txt

3010 matches in 2876 lines for "\?" in buffer: parse2_0e_dictcheck.txt
* parse3.py  Several revisions
** cleanup  remove unused code
Remove functions:
  vowel_sandhi, join_cpd_aH, join_cpd_am, join_cpd_a, 
  get_antyafunctions, unused_cpdsandhi, unusedget_parapada1
** based on 'parse2_0d_dictcheck.txt observations' above
6300:aham:-agrikA:ahAgrikA?   ahamagrikA.  aham-x compounds don't drop 'm'
8140:itTam:-kAram:itTakAram?  don't drop 'm' for compounds
8146:idam:-kAryA:idakAryA?  don't drop 'm' for compounds
10715:evam:-avasTa:evAvasTa?  Don't drop 'm'
11378:kaTam:-kaTikaH:kaTakaTikaH?  Don't drop 'm'
16670:tUzRIm:-daRqaH:tUzRIdaRqaH?  : tUzRIm don't drop 'm'
18222:naktam:-caraH:naktacaraH?  naktam Don't drop 'm'
31658:Sam:-kara:Sakara  : don't drop 'm' in Sam
34817:sAyam:-kAlaH:sAyakAlaH? MW sAyaMkAlaH don't drop 'm'
  exception 34817:sAyam:-maRqanam:sAyamaRqanam
36087:svayam:-aDigata:svayADigata? svayamaDigata don't drop 'm'
36503:hum:-kftam:hukftam? MW huMkfta  don't drop 'm'
38404:uccEH:-kara:uccEkara?  don't drop 'H' for compounds

* tempwork/parse3_0e.txt  
# Construct purvapada from k1
# Use ScharfSandhi code to join purva-pada and para-padas
python parse3.py tempwork/temp_explore1_2_0e.txt tempwork/parse3_0e.txt
34177 lines written to tempwork/parse3_0e.txt

* parse3_0e_dictcheck.txt
# dictcheck using dalglob
python dalglobpy/dictcheck.py tempwork/parse3_0e.txt tempwork/parse3_0e_dictcheck.txt

2915 matches in 2788 lines for "\?" in buffer: parse3_0e_dictcheck.txt

* parse3_0e_dictcheck1.txt
# dictcheck1 using dalglob
python dalglobpy/dictcheck1.py tempwork/parse3_0e.txt tempwork/parse3_0e_dictcheck1.txt
34177 lines written to tempwork/parse3_0e_dictcheck1.txt
2455 keys not found

cp tempwork/parse3_0e_dictcheck1.txt parse3_0e_dictcheck1.txt
* parse3_0e_dictcheck1  observations
17137:dAhaH:-hara, -haraRa:dAhahara?,dAhaharaRa   NOT compounds
21922:pOra:-aNnA, -yozit:pOrANnA?,pOrayozit  aNnA -> aNganA print change (cf. mw)
* not needed? tempwork/parse1.txt
python parse1.py tempwork/temp_explore1_2b.txt tempwork/parse1.txt

u:13210:krozwu:-SIrzam, -krozwukaSiras:krozwuSIrzam,krozwukrozwukaSiras
185 matches for "[0-9]:\([^:][^:][^:]\).*?:.*?-\1" in buffer: parse1.txt
* ==========================================
* ==========================================
* INSTALLATION csl-orig tempwork/ap_0e.txt
* 03-19-2026 Install tempwork/ap_0e.txt at Github, Cologne

** check repo(s) for pull
cd /c/xampp/htdocs/cologne/csl-orig
git status
# no staged files
git pull
#  Already up to date

cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10 #home

------------
** install local displays from tempwork/ap_0e.txt
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10 #home
cp tempwork/ap_0e.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap/ap.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh ap  ../../ap
sh xmlchk_xampp.sh ap
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10/  # home

-----------------------------
** sync csl-orig to github:
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "AP: compound headwords preparation
Ref: https://github.com/sanskrit-lexicon/AP/issues/10"
#   1 file changed, 821 insertions(+), 821 deletions(-)
git push
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10/  # home

---------------------------
** sync Cologne to github
# connect to cologne.
cd csl-orig
git pull

cd ../csl-pywork/v02
sh generate_dict.sh ap  ../../APScan/2020/

---------------------------
* sync this repo to Github
cd /c/xampp/htdocs/sanskrit-lexicon/AP/issues/issue10
git add .
git commit -m "AP: compound headwords preparation
Ref: https://github.com/sanskrit-lexicon/AP/issues/10"

git push

* ==========================================
* THE END

