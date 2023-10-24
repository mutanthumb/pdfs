
'''
Look for:
RepresentationInformation:
Capture:
    109510021976818847935325256696441957808.pdf
    Status: Well-Formed and valid
    Title: Effective assessment of use of sitters by nurses in inpatient care settings
    Creator: 3B2 Total Publishing System 8.07e/W
    FilterPipeline: FlateDecode'''

import re
import csv

jfile = "../jhove-output.txt"
outputFile = "jhoveParsedResults.csv"

textfile = open(jfile, 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("/(\d+.pdf)\n([\S\n\t\v ]*?) RepresentationInformation", filetext, re.M)

#print(matches)

outputList = []

for pdf in matches:
    # iterate in each tuple element
    #print(pdf[0])
    # find field return info
    '''
    toEncode = re.findall('Encoding: Identity-H\n      ToUnicode: true', pdf[1], re.M)
    noEncode = re.findall('Encoding: Identity-H\n\s+Font: \n', pdf[1], re.M)
    cid = re.findall('CIDFontType0:', pdf[1], re.M)
    '''
    # text represented by (.*?) is captured and returned. re.M means over multiple lines. 
    pdfStatus = re.findall('  Status: (.*?)\n', pdf[1], re.M)
    pdfTitle = re.findall('    Title: (.*?)\n', pdf[1], re.M)
    pdfCreator = re.findall('    Creator: (.*?)\n', pdf[1], re.M)
    pdfFilter = re.findall('   Filters: \n    FilterPipeline: (.*?)\n   Fonts: ', pdf[1], re.M)

    #print(pdf[0])
    #print(noEncode)

    #print(pdf[0], pdfStatus, pdfTitle, pdfCreator, pdfFilter)
    output = (pdf[0], pdfStatus, pdfTitle, pdfCreator, pdfFilter)
    outputList.append(output)
#print(outputList)

with open(outputFile,'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['filename','status', 'title', 'creator', 'filter'])
    for row in outputList:
        csv_out.writerow(row)


