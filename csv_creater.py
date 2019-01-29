import csv
import json

infile = open("sample.json", "r")
outfile = open("file2.csv", "w")

writer = csv.writer(outfile)

for row in json.loads(infile.read()):
    writer.writerow(row)
