
import csv

nodos = open('grafo_nodes.csv', 'w', newline='', encoding="utf-8-sig")
write_csv = csv.writer(nodos, delimiter=",")
csvFile = open("resultado_limpio_metro.csv", "r", encoding= "utf-8")
csvReader = csv.reader(csvFile, delimiter=',', lineterminator='\n')

line_number = []
stop_id = []
stop_name = []
stop_lat = []
stop_lon = []


for row in csvReader:
    line_number.append(row[1])
    stop_id.append(row[3])
    stop_name.append(row[5])
    stop_lat.append(row[7])
    stop_lon.append(row[8])


line = 0
for line in range(len(line_number)):
    if line_number[line] != 'line_number' and line < (len(line_number)-1) and str(line_number[line]) == str(line_number[line+1]):
        write_csv.writerow([stop_id[line], stop_name[line], stop_lat[line], stop_lon[line], line_number[line]])
write_csv.writerow([stop_id[line], stop_name[line], stop_lat[line], stop_lon[line], line_number[line]])

print("terminado TODO")