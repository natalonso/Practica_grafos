
import csv

edges_names = open('grafo_edges_names.csv', 'w', newline='', encoding="utf-8-sig")
write_csv = csv.writer(edges_names, delimiter=",")
csvFile = open("resultado_limpio_metro.csv", "r", encoding= "utf-8")
csvReader = csv.reader(csvFile, delimiter=',', lineterminator='\n')

line_number = []
stop_id = []
stop_name = []

for row in csvReader:
    line_number.append(row[1])
    stop_id.append(row[3])
    stop_name.append(row[5])

line = 0
for line in range(len(line_number)):
    if line_number[line] != 'line_number' and line < (len(line_number)-1) and str(line_number[line]) == str(line_number[line+1]):
        write_csv.writerow([stop_name[line], stop_name[line + 1]])
        if stop_name[line + 1] == 'LUCERO':
            write_csv.writerow([stop_name[line + 1], 'LAGUNA'])
        if stop_name[line + 1] == 'SAN NICASIO':
            write_csv.writerow([stop_name[line + 1], 'PUERTA DEL SUR'])

print("terminado TODO")