#!/usr/bin/env python
import tika
from tika import parser
import pprint
from csv import DictWriter


pp = pprint.PrettyPrinter(depth=4)
parsed = parser.from_file('/Users/sborda/Desktop/DigitalPreservation/PDFs/ALA-Check/diversity-freereport.pdf')


#pp.pprint(parsed)
pp.pprint(parsed["metadata"])
#pp.pprint(parsed["content"])
#pp.pprint(parsed["status"])

#metaKeys = list(parsed["metadata"].keys())
#print(metaKeys)




