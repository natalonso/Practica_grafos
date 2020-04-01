# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re


###############################
#ACCEDER A LA PAGINA PRINCIPAL
###############################

url="https://www.crtm.es/tu-transporte-publico.aspx"
html = requests.get(url)
bsObj = BeautifulSoup(html.text, "html.parser")

#########################################################################
#CONSEGUIR LOS LINKS DE LAS LINEAS PARA METRO
#########################################################################

enlace=bsObj.find("a",{"title":"Líneas Metro"})
txt_metro = open('resultado_scraper_metro.txt', 'w', newline='', encoding="utf-8")

url = enlace.attrs["href"]
html_lineas = requests.get("https://www.crtm.es" + url)
bsObj = BeautifulSoup(html_lineas.text, "html.parser")

for link in bsObj.findAll("div",{"class":re.compile("listaBotones" + ".*")}):
    lineas = link.findAll("a", {"title": re.compile("Línea" + ".*")})
    for linea in lineas:
        nombre_linea = linea.find("span", {"class": True})
        txt_metro.write("Linea metro: " + nombre_linea.text + "\n")

        url_linea_x = linea.attrs["href"]
        html_linea_x = requests.get("https://www.crtm.es" + url_linea_x)
        bsObj_linea_x = BeautifulSoup(html_linea_x.text, "html.parser")

        for parada in bsObj_linea_x.findAll("a", {"href" : re.compile("/tu-transporte-publico/" + ".*" + "/estaciones/" + ".*" + ".aspx")}):
            txt_metro.write(str(parada.text) + "\n")


print('Terminado scraper metro')
