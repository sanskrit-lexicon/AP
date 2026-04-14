
Start with Printed "abbreviations of names of works or authors"
https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/_static/ap57_vol1_frontmatter.pdf


-------------------
ap57vol1 folder: 
extract pdf individual pages using acrobat 9

The works/authors pages are 12, 13, 14
-------------------
Try Google DOC OCR -  unusable!
-------------------
copilot folder:
Windows Copilot constructed tab-delimited files from the images.
  This is NOT OCR, but the end-result is like OCR!
Files:
page12.txt page13.txt page14.txt vol3page4.txt
-------------------
proof folder:
Jim edits the Copilot pages, using the pdfs in ap57frontmatter folder.

Concatenate to get auth_tooltips.txt
cd proof
cat page12.txt page13.txt page14.txt vol3page4.txt> ../auth_tooltips.txt
# revised for supplementary abbreviations in vol3page4.txt
---------------------------------
material from vol 3 page 4
"A supplementary List of Abbreviations"
https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/_static/ap57_vol1_frontmatter.pdf

