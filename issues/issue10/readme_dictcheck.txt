These notes pertain to program prep1a_dictcheck.py.
This was used in an earlier version, which was not
used in later version.

* temp_ap90.txt for comparison to ap
cp /c/xampp/htdocs/cologne/csl-orig/v02/ap90/ap90.txt temp_ap90.txt
* temp_mw.txt for comparison to ap
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt 
==========================================
* dictcheck
python prep1a_dictcheck.py prep1a_1.txt temp_ap90.txt temp_mw.txt prep1a_1_dictcheck.txt

507 found in ap90, 352 not found (out of 859)
730 found in mw  , 129 not found (out of 859)
800 found in ap90 or mw, 59 not found
1595 lines written to prep1a_1_dictcheck.txt


Editing prep1a_1_dictcheck_notes.txt for those 59
Use https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/sample/dalglob1.php

10 remain 'notfound' in any dictionary
Some changes to ap_0a.txt 
* prep1a_2_dictcheck_notes.txt  (ap90=no,mw=no)
Use https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/sample/dalglob1.php

** TODO <L>11272<pc>0522-1<k1>kaqambaH<k2>kaqa(la)mbaH
{#kaqa(la)mbaH(mbI)#}¦
  ANS: ?
** DONE <L>13051<pc>0610-2<k1>kOtUhalam<k2>kOtUhalam
{#kOtUhalam(lyam)#}¦ [{#kutUhala-aR#}]
  ANS: kOtUhalyam

** DONE <L>13093<pc>0612-2<k1>kOSalam<k2>kOSalam
{#kOSalam(lyam)#}¦ [{#kuSala-aR zyaY vA#} <ls>P. V. 1. 
  ANS: kOSalyam

** TODO <L>13368<pc>0626-1<k1>kzipatiH<k2>kzipatiH
{#kzipatiH(stiH)#}¦ <ab>Ved.</ab> The arm.

** DONE <L>13620<pc>0638-1<k1>KalUrikA<k2>KalUrikA
{#KalUrikA(rakam)#}
  ans: Kalurakam

** DONE <L>14130<pc>0664-1<k1>gundAlaH<k2>gundA(ndrA)laH
{#gundA(ndrA)laH#}
  ans: gundrAlaH

** DONE <L>15149<pc>0716-1<k1>cEtraraTam<k2>cEtraraTam
{#cEtraraTam(Tyam)#}
 ANS=cEtraraTyam

** DONE <L>15317<pc>0722-a2<k1>jaganuH<k2>jaganuH
{#jaganuH(nnuH)#}¦
 ANS=jagannuH

** DONE <L>15939<pc>0749-a2<k1>wiwiBaH<k2>wiwi(wwi)BaH
{#wiwi(wwi)BaH#}
 ABS=wiwwiBaH

** TODO <L>16308<pc>0766-2<k1>tAjikaH<k2>tAjikaH
{#tAjikaH(taH)#}

** DONE <L>23548<pc>1113-2<k1>praScotanam<k2>praSco(Scyo)tanam
{#praSco(Scyo)tanam#}
 ans=praScyotanam

** TODO <L>27345<pc>1333-1<k1>rasonaH<k2>ra(su)sonaH
{#ra(su)sonaH#}
 ans=?

** DONE <L>28521<pc>1392-1<k1>varivasita<k2>varivasi(syi)ta
{#varivasi(syi)ta#}
 ans=varivasyita

** DONE <L>30021<pc>1458-1<k1>vimarzin<k2>vima(rSi)rzin
{#vima(rSi)rzin#}
 ans=vimarSin

** DONE <L>34871<pc>1675-1<k1>sArpaH<k2>sArpaH
{#sArpaH(rpyaH)#}
 ans=sArpyaH

** DONE <L>35231<pc>1699-2<k1>sUrkz<k2>sUrkz
{#sUrkz(rkzy)#}
 ans=sUrkzy

** DONE <L>35232<pc>1699-2<k1>sUrkzaRam<k2>sUrkza(rkzya)Ram
{#sUrkza(rkzya)Ram#}
 ans=sUrkzyaRam

** TODO <L>35428<pc>1707-1<k1>sOKasuptikaH<k2>sOKa(pra)suptikaH
{#sOKa(pra)suptikaH#}
 ans=?

** DONE <L>36060<pc>1738-1<k1>svaMg<k2>svaM(k)g
{#svaM(k)g#}
 ans=svaMk

