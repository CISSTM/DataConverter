import csv
import json

infile = open("sample.json", "r")
outfile = open("file2.csv", "w")

writer = csv.writer(outfile)

#Write CSV header
header = '{"s": "sendtime", "t": temperatuur", "p": pressure", "a": "alltitude"}'
#f = csv.writer(["sendtime", "temperatuur", "pressure", "alltitude"])

writer.writerow('ds') #De header

for row in json.loads(infile.read()):
    writer.writerow(row.values())

print("Just completed your csv file!")