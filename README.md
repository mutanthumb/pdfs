# pdfs
PDF exploration

An ongoing project for the Digital Preservation Unit at the UMich Library has been to get more information about our PDF files in Deep Blue Documents than what is readily available from the system itself. We are interested in "preservation metadata", what version of PDF is it, what system created it, etc. 

The initial set is 134643 files. 

This GitHub repo contains the various scripts I used to analyze the results of running various PDF tools on these files, Tika, JHOVE, and veraPDF as well as sample result files. 

Tika (https://github.com/chrismattmann/tika-python):
change file path in python script 

      python3 basicTikaParser.py

JHOVE (https://jhove.openpreservation.org/getting-started/):

      /Applications/JHOVE/jhove ../PDF_Assessment_v1.3-1.pdf

Run JHOVE on folders:

      /Applications/JHOVE/jhove -m PDF-hul ./SamplePile/10-1/ > jhove-output.txt

PDFinfo (https://www.xpdfreader.com/pdfinfo-man.html):

      ./xpdf-tools-mac-4.03/bin64/pdfinfo ../PDF_Assessment_v1.3-1.pdf

ExifTool (https://exiftool.org/):

      exiftool ../PDF_Assessment_v1.3-1.pdf

PDFBox (https://pdfbox.apache.org/download.html):

      java -jar preflight-app-3.0.0.jar ../PDF_Assessment_v1.3-1.pdf

VeraPDF (https://docs.verapdf.org/cli/validation/):

      /Applications/veraPDF/verapdf -f 0 ../PDF_Assessment_v1.3-1.pdf

Run VeraPDF on folders:

      /Applications/veraPDF/verapdf -f ua1 --recurse ../SamplePile/10-1/ > veraPDF-output.txt


JHOVE parser (run within /apps):

      python3 JhoveOutputParser.py
