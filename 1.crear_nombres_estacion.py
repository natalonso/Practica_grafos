
import csv

with open('grafo_nodes.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    write_csv = csv.writer(csvfile, delimiter=",")
    csvFile = open("resultado.csv", "r", encoding= "utf-8")
    csvReader = csv.reader(csvFile, delimiter=',', lineterminator='\n')
    write_csv.writerow(["Id", "Label"])

    line_number = []
    stop_id = []
    stop_name = []

    for row in csvReader:
        line_number.append(row[1])
        stop_id.append(row[3])
        stop_name.append(row[5])

    line = 0
    for line in range(len(line_number)):
        if line_number[line] != 'line_number':
            if line < 291:
                if str(line_number[line]) == str(line_number[line+1]):
                    write_csv.writerow([stop_id[line],
                                       stop_name[line]])