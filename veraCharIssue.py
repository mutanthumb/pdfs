
'''
Find all pdf files with clause="6.3.8" status="failed" example:
<report><jobs><job><item><name>/Users/sborda/Desktop/PDFbook/0636920021483-master-examples/examples/BritishLibrary-PDF_Assessment_v1.3.pdf</name>
<report><jobs><job><validationReport><details><rule specification="ISO 19005-1:2005" clause="6.3.8" testNumber="1" status="failed" passedChecks="0" failedChecks="1878">
'''

# Import BeautifulSoup
from bs4 import BeautifulSoup as bs
import os
import csv

outputFile = "/Users/sborda/Desktop/Python/ExplorePDFs/OutputFiles/veraXML-G9-Output.csv"

with open("./Files/veraPDF-group9.xml") as fp:
    soup = bs(fp, "xml")
    fileOutput = []
    jobs = soup.find_all('job')
    for job in jobs:
        fName = job.find('name')
        #print(fName)
        head, tail = os.path.split(fName.text)
        #print(tail)

        ruleList = []
        rules = job.find_all('rule')
        for rule in rules:
            #print(rules)
            rClause = rule['clause']
            #print(rClause)
            rFailedCheck = rule['failedChecks']
            ruleClauseCheck = (rClause, rFailedCheck)
            ruleList.append(ruleClauseCheck)
        fileRules = (tail, ruleList)
        #print(fileRules)

        fileOutput.append(fileRules)

#print(fileOutput)
with open(outputFile,'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['filename','clausesFailures'])
    for row in fileOutput:
        csv_out.writerow(row)



