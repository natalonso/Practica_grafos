import csv
import pandas as pd
import requests
from io import StringIO
import re

def normalize(s):
    replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"))
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


f_scraper = open("resultado_scraper_metro.txt", 'r', encoding='utf-8')
dicc_metro = csv.DictReader(open("stops_metro.txt", 'r', encoding="utf-8-sig"))
diccionario_iterable = []
for line in dicc_metro:
    diccionario_iterable.append(line)

######################################
# CREAMOS CSV
######################################

with open('resultado_limpio_metro.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    write_csv = csv.writer(csvfile, delimiter=",")
    write_csv.writerow(["transportmean_name",
                        "line_number",
                        "order_number",
                        "stop_id",
                        "stop_code",
                        "stop_name",
                        "stop_desc",
                        "stop_lat",
                        "stop_lon",
                        "zone_id" ,
                        "stop_url",
                        "location_type",
                        "parent_station",
                        "stop_timezone",
                        "wheelchair_boarding"])


    for linea in f_scraper:
        if "Linea metro: " in linea:
            transporte = "METRO"
            nombre_linea = linea[13:len(linea)]
            numero_estacion = 0
        else:
            nombre_estacion = linea
            numero_estacion = numero_estacion + 1
            cadena2 = normalize(nombre_estacion).lower().rstrip("\n").strip()


            if cadena2 == "avenida de la ilustracion":
                cadena2 = "avdadelailustracion"
            if cadena2 == "rda. de la comunicacion":
                cadena2 = "rondadelacomunicacion"

            cadena2 = re.sub('[^A-Za-z0-9]+', '', cadena2)  # estacion del fichero resultado del scraper de metro

            for linea_diccionario in diccionario_iterable:
                cadena1 = normalize(linea_diccionario["stop_name"]).lower().rstrip("\n").strip()
                cadena1 = re.sub('[^A-Za-z0-9]+', '', cadena1)  # estacion del fichero de metro procesado

                if cadena1 == cadena2:
                    break

            if cadena2 != "":
                write_csv.writerow([transporte,
                                    str(nombre_linea).rstrip("\n"),
                                    str(nombre_linea).rstrip("\n") + ":" + str(numero_estacion),
                                    linea_diccionario['stop_id'],
                                    linea_diccionario['stop_code'],
                                    linea_diccionario['stop_name'],
                                    linea_diccionario['stop_desc'],
                                    linea_diccionario['stop_lat'],
                                    linea_diccionario['stop_lon'],
                                    linea_diccionario['zone_id'],
                                    linea_diccionario['stop_url'],
                                    linea_diccionario['location_type'],
                                    linea_diccionario['parent_station'],
                                    str("-" if linea_diccionario['stop_timezone'] is None else linea_diccionario['stop_timezone']),
                                    str("-" if linea_diccionario['wheelchair_boarding'] is None else linea_diccionario['wheelchair_boarding'])])

print("terminado TODO")