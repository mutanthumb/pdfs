

import csv
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', None)

csv.field_size_limit(100000000)
fullList = "./Files/tikaPDF_full.csv"

"""
HEADERS = next(csv.reader(open(fullList)))
print(HEADERS)
print(len(HEADERS))
z = 0
for item in HEADERS:
    if "PDFAnnotator" in item:
        z += 1

print(z)

"""
total = 0
HEADERS = next(csv.reader(open(fullList)))
pdfList = []
with open(fullList) as f:
    reader = csv.reader(f)
    #print(type(reader))
    for row in reader:
        pdfList.append(row)
#print(total)

data = pdfList
df = pd.DataFrame(data, columns=HEADERS)

'''
for col in df.columns:
    print(col)
'''
#print(df.head())
'''
a = df['pdf:docinfo:creator_tool'].value_counts()
print(a.head(50))
print("number of unique items: ", len(a))


b = df['dc:format'].value_counts()
print(b.head(53))
print("number of unique items: ", len(b))


e = df['pdf:docinfo:producer'].value_counts()
print(e.head(50))
print("number of unique items: ", len(e))
'''

"""
pdf:docinfo:creator_tool
dc:format
creator
Content-Type
pdf:docinfo:producer
producer
"""




