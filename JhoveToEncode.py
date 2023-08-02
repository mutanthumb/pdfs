
'''
Look for:
RepresentationInformation:
Capture: /Volumes/Passport4Mac/Globus/DigiPres/PDFs/DeepBlueDocsPDFs/DeepBluePDFs/10-1/110233194919095639702164001448262758918.pdf
      Encoding: Identity-H
      ToUnicode: true
'''

import re
import csv

jfile = "/Users/sborda/Desktop/DigitalPreservation/PDFs/jhoveOutput/jrcPDFOutput.txt"
outputFile = "/Users/sborda/Desktop/DigitalPreservation/PDFs/jhoveOutput/jrcPDFOutputResults.csv"

textfile = open(jfile, 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("/(\d+.pdf)\n([\S\n\t\v ]*?) RepresentationInformation", filetext, re.M)

#print(matches)

outputList = []

for pdf in matches:
    # iterate in each tuple element
    #print(pdf[0])
    toEncode = re.findall('Encoding: Identity-H\n      ToUnicode: true', pdf[1], re.M)
    noEncode = re.findall('Encoding: Identity-H\n\s+Font: \n', pdf[1], re.M)
    cid = re.findall('CIDFontType0:', pdf[1], re.M)
    #print(pdf[0])
    #print(noEncode)

    if len(noEncode) != 0:
        noEncodeFont = re.findall('BaseFont: (.+)\n\s+Encoding: Identity-H\n\s+Font: \n', pdf[1], re.M)
        #print(noEncodeFont)
        #print(pdf[0])
        echeck = "IdH exists - No mention of ToUnicode: true"
        #print(pdf[0], noEncodeFont[0], echeck, cid)
        output = (pdf[0], noEncodeFont[0], echeck, cid)
        outputList.append(output)
#print(outputList)

with open(outputFile,'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['filename','font', 'echeck', 'cid'])
    for row in outputList:
        csv_out.writerow(row)


