
import csv

csvFile = open("resultado_limpio_metro.csv", "r", encoding= "utf-8-sig")
csvReader = csv.reader(csvFile, delimiter=',', lineterminator='\n')

nodos = open('grafo_nodes.csv', 'w', newline='', encoding="utf-8-sig")
write_csv = csv.writer(nodos, delimiter=",")

line_number = []
stop_id = []
stop_name = []
stop_lat = []
stop_lon = []
zona = []

for row in csvReader:
    line_number.append(row[1])
    stop_id.append(row[3])
    stop_name.append(row[5])
    stop_lat.append(row[7])
    stop_lon.append(row[8])

for line in range(len(line_number)):
    if line_number[line] != 'line_number':
        write_csv.writerow([stop_name[line], stop_lat[line], stop_lon[line]])


print("terminada creación de nodos con atributos (latitud y longitud)")