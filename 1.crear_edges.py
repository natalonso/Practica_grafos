
import csv

# Crea las aristas/estaciones contiguas: estacion_a-estacion_b

with open('grafo_edges.csv', 'w', newline='', encoding="utf-8-sig") as edges:
    write_csv = csv.writer(edges, delimiter=",")
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

        if line_number[line] != 'line_number' and line < 290 and str(line_number[line]) == str(line_number[line+1]):
            write_csv.writerow([stop_id[line], stop_id[line + 1]])
            if stop_id[line + 1] == 'par_4_130':
                write_csv.writerow([stop_id[line + 1], 'par_4_104'])
            if stop_id[line + 1] == 'par_4_236':
                write_csv.writerow([stop_id[line + 1], 'par_4_205'])

print("terminado TODO")


