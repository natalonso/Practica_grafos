import csv
import json


csvfile = open('grafo.csv', 'r', encoding= "utf-8")
jsonfile = open('grafo.json', 'w',encoding ="utf-8")

fieldnames = ("soucre","destination","name_source")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile,ensure_ascii=False)
    jsonfile.write('\n')


