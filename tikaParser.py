#!/usr/bin/env python

from sys import argv
import tika
import pprint
from tika import parser
import os
import csv

#pp = pprint.PrettyPrinter(depth=4)
# open folder loop through pdf files creating a dict
"""
    Create a dict with:
    key = 'resourceName' - need to strip b'
    values = list()
    'dcterms:created'
    'dc:format'
    'pdf:PDFVersion'
    'pdf:unmappedUnicodeCharsPerPage'
    'pdf:docinfo:producer'

"""
# create csv file from dict
pFieldnames = []
rootdir = '/Volumes/Passport4Mac/Globus/DigiPres/PDFs/DeepBlueDocsPDFs/'
print(rootdir)
for path, dirs, files in os.walk(rootdir, topdown=False):
    #print(dirs)
    for folder in dirs:
        outputFile = folder + 'output.txt'
        errorFile = folder + 'error.txt'
        newPath = os.path.join(path, folder)
        print(newPath)
        pdfList = []
        errorList = []

        for subPath, subDirs, subfiles in os.walk(newPath):

            for name in subfiles:
                filepath = os.path.join(subPath, name)
                print(filepath)
                #print(path)
                #print(name)

                if filepath.endswith('.pdf'):
                    parsed = parser.from_file(filepath)

                    try:
                        pdfDict = parsed['metadata']
                        pdfDict['filePath'] = folder
                        pdfDict['fileName'] = name
                        for key in pdfDict.keys():
                            if key not in pFieldnames:
                                pFieldnames.append(key)

                        pdfList.append(pdfDict)

                    except KeyError as e:
                        errorDict = {'filename': name, 'error': e}
                        errorList.append(errorDict)

                else:
                    continue

        eFieldNames = ('filename', 'error')

        with open('./TikaOutput/' + outputFile, 'w', newline='') as pdfoutput_file:
            dict_writer = csv.DictWriter(pdfoutput_file, fieldnames=pFieldnames, delimiter='\t', quotechar='"',
                                         escapechar='\\')
            dict_writer.writeheader()
            dict_writer.writerows(pdfList)

        with open('./TikaOutput/' + errorFile, 'w', newline='') as erroutput_file:
            dict_writer = csv.DictWriter(erroutput_file, fieldnames=eFieldNames)
            dict_writer.writeheader()
            dict_writer.writerows(errorList)



#pp.pprint(parsed["metadata"])
#print(parsed["content"])
