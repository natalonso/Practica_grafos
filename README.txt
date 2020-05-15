########################################
EJECUCIÓN DE LA PRÁCTICA: RED DE METRO:
########################################

1. Ejecución del fichero 1.scraper_version_simplif.py:
    -scraper de la url https://www.crtm.es y creación del txt: resultado_scraper_metro.txt.

2. Obtención del fichero stops_metro.txt (se ha obtenido hace unos meses):
    -descargado de: https://crtm.maps.arcgis.com/home/item.html?id=5c7f2951962540d69ffe8f640d94c246 el fichero .

3. Ejecución del fichero 2.limpiar_csv.py:
    -usa los ficheros resultado_scraper_metro.txt y stops_metro.txt y crea el fichero resultado_limpio_metro.csv.

4. Ejecución del fichero 3.crear_edges_nombres.py:
    -lee el fichero resultado_limpio_metro.csv y crea los csv: grafo_edges_names.csv y grafo_edges.csv.

5. Ejecución del fichero 4.crear_nodes.py:
    -lee del fichero resultado_limpio_metro.csv y crea el csv grafo_nodes.csv.

6. Ejecución del fichero 5.main.py:
    -análisis descriptivo y creación del fichero grafo_completo.json para crear la visualización con d3.js.

7. Ejecución del fichero 6.visualizacion.html:
    -para ver la visualización.
