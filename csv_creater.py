import csv
import json

infile = open("sample.json", "r")
outfile = open("export.csv", "w")

writer = csv.writer(outfile)

#Write CSV header
header = '{"s": "sendtime", "t": temperatuur", "p": pressure", "a": "alltitude"}'
#f = csv.writer(["sendtime", "temperatuur", "pressure", "alltitude"])

writer.writerow(header) #De header

for row in json.loads(infile.read()):
    topic = None
    for value_name in row.keys():
        if not value_name == "s":
            topic = value_name
    to_save = {
        topic: row[topic]
    }
    writer.writerow(to_save.values())

print("Just completed your csv file!")