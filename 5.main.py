
import networkx as nx
import networkx.algorithms.community as nxComm
import json
from networkx.readwrite import json_graph

import matplotlib.pyplot as plt
import csv


g = nx.read_edgelist('grafo_edges_names.csv', delimiter=',', encoding="utf-8")

print(nx.info(g))
print(g.edges(data = True))
print(g.nodes(data=True))

plt
nx.draw(g, with_labels=True)
plt.show()


################################################
# ASIGNAR ATRIBUTOS A LOS NODOS:
################################################

atributos = open("grafo_nodes.csv", "r", encoding= "utf-8")
csvReader = csv.reader(atributos, delimiter=',', lineterminator='\n')


atributos=[]
for line in csvReader:
    atributos.append(line)

nodes = g.nodes(data = True)

for node in nodes:
    for line in atributos:
        if line[1] == node[0]:
            g.nodes[node[0]]["lat"] = line[2]
            g.nodes[node[0]]["lon"] = line[3]
            g.nodes[node[0]]["line"] = line[4]


########################
# ADYACENCIA:
########################

# print("Adyacencia de no dirigido: ")
# for node in g.nodes:
#     print(str(node) + " -> " + str(g.adj[node]))

########################
# GRADO:
########################

# print("Grado: ")
# for node in g.nodes:
#     print(str(node) + " -> " + str(g.degree[node]))

# Idea: Para ver el número de líneas podemos ver los nodos con grado 1 (estaciones finales) y dividir entre 2
# Idea: meter el parámetro ascensor como trabajo futuro
# Las estaciones que más grado tengan serán las que estén en más líneas y las más relevantes

########################
# CAMINOS:
########################

# Idea: ordenar los caminos para proponer una nueva ruta en caso de que alguna estación este en obras o fuera de servicio: all_simple_paths
# Idea: si un nodo está caido, eliminarlo del grafo y ver las rutas alternativas (volver a ejecutar el shortest y daría el más corto)

# print("Caminos más cortos:")
# for path in nx.all_shortest_paths(g, 'GOYA', 'OPERA'):
#     print(str(path))

########################
# CONECTIVIDAD:
########################
#
# print("Es conexo? " + str(nx.is_connected(g)))
# print("Componentes: " + str(nx.number_connected_components(g)))

# Qué pasa si puerta del sur se cae (metro sur se quedaría incomunicado): NODOS CRÍTICOS

########################
# MATRIZ ADYACENCIA:
########################

# # Nos devuelve una matriz dispersa para mejorar la eficiencia en memoria
# m = nx.adj_matrix(g)
# # Para imprimirla como una matriz, la convertimos en densa
# dm = m.todense()
# print("Matriz de adyacencia de grafo no dirigido:")
# print(dm)

########################
# LISTA ADYACENCIA:
########################

# print("Lista de adyacencia: ")
# for line in nx.generate_adjlist(g):
#     print(line)

########################
# DENSIDAD:
########################

# print('Densidad del grafo: ', nx.density(g))
# draw_networkx_labels para los nombre de las estaciones

########################
# DIJKSTRA:
########################

# Es para grafos ponderados: Tampoco aplica en nuestro caso

########################
# ANÁLISIS DESCRIPTIVO:
########################

# Métricas para medir relevancia de nodos: Grado, Closeness centrality, Betweenness centrality, Eigenvector centrality

########################
# Degree centrality:
########################

# degree = nx.degree_centrality(g)
# for node in degree:
#     print("{0:s}({1:.2f})".format(node, degree[node]), end='\n')

########################
# Closeness centrality:
########################

# los nodos que esten más lejos de los extremos tendran mayor centralidad
# Por como está diseñado el metro, sabemos que la parte central de cada línea esta en el centro de la ciudad: sol-closeness centrality alto
# El extremo por ejemplo villaverde alto: será más bajo.
# Podria ayudar a ver las estaciones del centro de la ciudad en casa de querer reforzar esta zona
# Concuerda con que el grafo es conexo

# closeness = nx.closeness_centrality(g)
# for node in closeness:
#     print("{0:s}({1:.2f})".format(node, closeness[node]), end='\n')

########################
# Betweenness centrality:
########################

# Es una manera de ver los nodos más importantes, midiendo la importancia como cuantas estaciones (o nodos) dejas
# sin servicio en caso de caerse ese nodo, por ejemplo, aviación española dejaría inalcanzable metro sur con el resto de la red
# En cambio, si sol se cae la estaciones que comunica podrían ser alcanzables por otros caminos.

# betweenness = nx.betweenness_centrality(g)
# for node in betweenness:
#     print("{0:s}({1:.2f})".format(node, betweenness[node]), end='\n')

#######################
# Eigenvector centrality:
########################

# Mide la cercanía a estaciones que tengan muchas conexiones (conecten varias líneas): creemos que aquí no es aplicable

# eigenvector = nx.eigenvector_centrality(g, max_iter = 1000)
# for node in eigenvector:
#     print("{0:s}({1:.2f})".format(node, eigenvector[node]), end='\n')

########################
# Page rank:
########################

# Es algoritmo da más importancia a las que tienen varias líneas pero apenas hay diferencia con las que solo tienen una línea

# pagerank = nx.pagerank(g)
# for node in pagerank:
#     print("{0:s}({1:.2f})".format(node, pagerank[node]), end='\n')

################################################
# Comparación de todos los métodos:
################################################

# print("ND\tDG\t\tCLS\t\tBTW\t\tEGN\t\tPR")
# for node in g.nodes:
#     print("{0:s}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}\t{5:.2f}"
#           .format(node, degree[node], closeness[node], betweenness[node], eigenvector[node], pagerank[node]))
#
# bestDG = max(degree, key=lambda key: degree[key])
# bestCL = max(closeness, key=lambda key: closeness[key])
# bestBT = max(betweenness, key=lambda key: betweenness[key])
# bestEG = max(eigenvector, key=lambda key: eigenvector[key])
# bestPR = max(pagerank, key=lambda key: pagerank[key])
#
# print("Degree: " + bestDG + " -> {0:.2f}".format(degree[bestDG]))
# print("Closeness: " + bestCL + " -> {0:.2f}".format(closeness[bestCL]))
# print("Betweenness: " + bestBT + " -> {0:.2f}".format(betweenness[bestBT]))
# print("Eigenvector: " + bestEG + " -> {0:.2f}".format(eigenvector[bestEG]))
# print("PageRank: " + bestPR + " -> {0:.2f}".format(pagerank[bestPR]))



################################################
# Edges Betweeness:
################################################

# centrality = nx.edge_betweenness_centrality(g)
# for node in centrality:
#     print("{0:s}-{1:s}({2:.2f})".format(node[0], node[1], centrality[node]), end='\n')

################################################
# Line graph:
################################################

# Transformar nodos en aristas y al reves ----> no nos aporta nada


################################################
# Cliques:
################################################

# subgrafos cuyos nodos estén todos relacionados entre sí directamente
# En nuestro caso, habría agrupaciones como mucho de 2/3 estaciones ---> No resulta interesante en nuestro caso
#
# print("Todos los cliques maximos:")
# for max_clique in nx.find_cliques(g):
#     print(max_clique)

# lista_cliques = list(nx.find_cliques(g))
# print('Cliques mayores que dos: ')
# for i in range(len(lista_cliques)):
#     if len(lista_cliques[i]) > 2:
#         print(lista_cliques[i])

################################################
# k-core:
################################################

# subgrafos cuyos nodos tengan al menos grado k (contando solo las arista dentro del subgrafo)
# Esto tampoco tendría sentido en nuestro caso

# kg = nx.k_core(g, k=3)
# print(len(kg))
# kg = nx.k_core(g, k=2)
# print(len(kg))
# nx.draw(kg, with_labels=True)
# plt.show()

################################################
# coeficiente de clustering:
################################################

# Número de "triangulos que hay" entre los que podrían crearse si unimos algunos nodos
# Nos de como resultado 0.0333: podría concluirse que tenemos 5 cliques (3 nodos)  / 150 que se podrían conseguirse

# print("Coeficiente clustering: " + str(nx.transitivity(g)))

################################################
# reciprocidad:
################################################

# para grafos dirigidos: no tiene sentido en nuestro caso

################################################
# Conectividad o componentes conexas:
################################################

# Se considerará una conectividad óptima cuando la comunicación entre dos vértices o nodos se realiza a través de un sólo salto
# En el caso del metro lo normal es que no todas las estaciones estén conectadas con un solo salto al resto de estaciones.

# El grado de conectividad se utiliza como indicador de desarrollo de los países al existir una
# relación directa entre el grado de conectividad de la red de transporte de un Estado y su renta per cápita.

# Media de caminos más cortos, de cualquier vértice a cualquier vértice
# print("AVG LENGTH: " + str(nx.average_shortest_path_length(g)))

# Camino más largo en el grafo (entre las dos estaciones más alejadas)
# print("DIAMETER: " + str(nx.diameter(g)))

################################################
# Deteccion de comunidades:
################################################

# La modularidad es una medida de la estructura de las redes o grafos.
# Fue diseñado para medir la fuerza de la división de una red en módulos (también llamados grupos, agrupamientos o comunidades).

pos=nx.spring_layout(g) # positions for all nodes

commGreedy = list(nxComm.greedy_modularity_communities(g)) #----> este podría mostrarnos el "centro" como una "comunidad"
# con el greedy vemos los extremos de las líneas (poca densidad) y "el centro de la ciudad" con más densidad

# commLabel = list(nxComm.label_propagation_communities(g)) ---> este en nuestro caso no tendría sentido

# print("GREEDY")
# for c in commGreedy:
#     print(sorted(c))

# print("LABEL")
# for c in commLabel:
#     print(sorted(c))

# print("COVERAGE:")
# print("\tGREEDY: "+str(nxComm.coverage(g, commGreedy)))
# print("\tLABEL: "+str(nxComm.coverage(g, commLabel)))
# print("PERFORMANCE:")
# print("\tGREEDY: "+str(nxComm.performance(g, commGreedy)))
# print("\tLABEL: "+str(nxComm.performance(g, commLabel)))
# print("MODULARITY")
# print("\tGREEDY: "+str(nxComm.modularity(g, commGreedy)))
# print("\tLABEL: "+str(nxComm.modularity(g, commLabel)))


# nodes
nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALCORCON CENTRAL', 'ALONSO DE MENDOZA', 'ARROYO CULEBRO', 'AVIACION ESPAÑOLA', 'CASA DEL RELOJ', 'COLONIA JARDIN', 'CONSERVATORIO', 'CUATRO VIENTOS', 'EL BERCIAL', 'EL CARRASCAL', 'EL CASAR', 'FUENLABRADA CENTRAL', 'GETAFE CENTRAL', 'HOSPITAL DE FUENLABRADA', 'HOSPITAL DE MOSTOLES', 'HOSPITAL SEVERO OCHOA', 'JOAQUIN VILUMBRALES', 'JUAN DE LA CIERVA', 'JULIAN BESTEIRO', 'LEGANES CENTRAL', 'LORANCA', 'LOS ESPARTALES', 'MOSTOLES CENTRAL', 'Manuela Malasaña', 'PARQUE DE LOS ESTADOS', 'PARQUE EUROPA', 'PARQUE LISBOA', 'PARQUE OESTE', 'PRADILLO', 'PUERTA DEL SUR', 'SAN NICASIO', 'UNIVERSIDAD REY JUAN CARLOS'],
                       node_color='orange',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALSACIA', 'Avenida de Guadalajara', 'BANCO DE ESPAÑA', 'COLON', 'CONDE DE CASAL', 'DIEGO DE LEON', 'EL CARMEN', 'GOYA', 'IBIZA', 'LA ALMUDENA', 'LA ELIPA', 'LAS ROSAS', 'LISTA', 'MANUEL BECERRA', 'NUÑEZ DE BALBOA', 'ODONNELL', 'PRINCIPE DE VERGARA', 'QUINTANA', 'RETIRO', 'RUBEN DARIO', 'SAINZ DE BARANDA', 'SERRANO', 'SEVILLA', 'VELAZQUEZ', 'VENTAS'],
                       node_color='red',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALAMEDA DE OSUNA', 'ASCAO', 'BARRIO DE LA CONCEPCION', 'BARRIO DEL PUERTO', 'CANILLEJAS', 'CARTAGENA', 'CIUDAD LINEAL', 'COSLADA CENTRAL', 'EL CAPRICHO', 'ESTADIO METROPOLITANO', 'GARCIA NOBLEJAS', 'HENARES', 'HOSPITAL DEL HENARES', 'JARAMA', 'LA RAMBLA', 'LAS MUSAS', 'PARQUE DE LAS AVENIDAS', 'PUEBLO NUEVO', 'SAN BLAS', 'SAN FERNANDO', 'SIMANCAS', 'SUANZES', 'TORRE ARIAS'],
                       node_color='green',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALONSO MARTINEZ', 'ALTO DE EXTREMADURA', 'ARGÜELLES', 'BILBAO', 'CALLAO', 'CHUECA', 'CIUDAD UNIVERSITARIA', 'GRAN VIA', 'IGLESIA', 'MONCLOA', 'NOVICIADO', 'OPERA', 'PLAZA DE ESPAÑA', 'PRINCIPE PIO', 'PUERTA DEL ANGEL', 'QUEVEDO', 'RIOS ROSAS', 'SAN BERNARDO', 'SANTO DOMINGO', 'SOL', 'TRIBUNAL', 'VENTURA RODRIGUEZ'],
                       node_color='blue',
                       node_size=500,
                   alpha=0.8)


nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALONSO CANO', 'ALVARADO', 'AVENIDA DE AMERICA', 'CANAL', 'COLOMBIA', 'CONCHA ESPINA', 'CRUZ DEL RAYO', 'CUATRO CAMINOS', 'CUZCO', 'DUQUE DE PASTRANA', 'ESTRECHO', 'GREGORIO MARAÑON', 'Guzmán el Bueno', 'ISLAS FILIPINAS', 'NUEVOS MINISTERIOS', 'PIO XII', 'PLAZA DE CASTILLA', 'REPUBLICA ARGENTINA', 'SANTIAGO BERNABEU', 'TETUAN', 'VALDEACEDERAS', 'VICENTE ALEIXANDRE'],
                       node_color='sienna',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALTO DEL ARENAL', 'ANTON MARTIN', 'ARGANZUELA-PLANETARIO', 'ATOCHA-RENFE', 'BUENOS AIRES', 'CONGOSTO', 'ESTACION DEL ARTE', 'LA GAVIA', 'LAS SUERTES', 'MENDEZ ALVARO', 'MENENDEZ PELAYO', 'MIGUEL HERNANDEZ', 'NUEVA NUMANCIA', 'PACIFICO', 'PORTAZGO', 'PUENTE DE VALLECAS', 'SIERRA DE GUADALUPE', 'TIRSO DE MOLINA', 'VALDECARROS', 'VILLA DE VALLECAS'],
                       node_color='gold',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ABRANTES', 'ACACIAS', 'CARABANCHEL ALTO', 'CARPETANA', 'LA FORTUNA', 'LA LATINA', 'LA PESETA', 'LAGUNA', 'LUCERO', 'MARQUES DE VADILLO', 'OPAÑEL', 'OPORTO', 'PAN BENDITO', 'PIRAMIDES', 'PLAZA ELIPTICA', 'PUERTA DE TOLEDO', 'San Francisco', 'URGEL', 'USERA'],
                       node_color='m',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['AEROPUERTO T1 T2 T3', 'AEROPUERTO T4', 'ALFONSO XIII', 'AVENIDA DE LA PAZ', 'Arturo Soria', 'BARAJAS', 'CANILLAS', 'ESPERANZA', 'FERIA DE MADRID', 'HORTALEZA', 'MANOTERAS', 'MAR DE CRISTAL', 'PARQUE DE SANTA MARIA', 'PINAR DE CHAMARTIN', 'PINAR DEL REY', 'PROSPERIDAD', 'SAN LORENZO'],
                       node_color='coral',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['BAMBU', 'BAUNATAL', 'BEGOÑA', 'CHAMARTIN', 'Fuencarral', 'HOSPITAL INFANTA SOFÍA', 'LA GRANJA', 'LA MORALEJA', 'LAS TABLAS', 'MANUEL DE FALLA', 'MARQUES DE LA VALDAVIA', 'MONTECARMELO', 'REYES CATOLICOS', 'RONDA DE LA COMUNICACION', 'TRES OLIVOS', '\ufeffPINAR DE CHAMARTIN'],
                       node_color='khaki',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ARGANDA DEL REY', 'ARTILLEROS', 'ESTRELLA', 'LA POVEDA', 'PAVONES', 'PUERTA DE ARGANDA', 'RIVAS FUTURA', 'RIVAS URBANIZACIONES', 'RIVAS VACIAMADRID', 'SAN CIPRIANO', 'VALDEBERNARDO', 'VICALVARO', 'VINATEROS'],
                       node_color='cyan',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALMENDRALES', 'CIUDAD DE LOS ANGELES', 'DELICIAS', 'EMBAJADORES', 'HOSPITAL 12 DE OCTUBRE', 'LAVAPIES', 'LEGAZPI', 'PALOS DE LA FRONTERA', 'SAN CRISTOBAL', 'SAN FERMIN-ORCASUR', 'VILLAVERDE ALTO', 'VILLAVERDE BAJO-CRUCE'],
                       node_color='indigo',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ALUCHE', 'BATAN', 'CAMPAMENTO', 'CARABANCHEL', 'CASA DE CAMPO', 'EMPALME', 'EUGENIA DE MONTIJO', 'LAGO', 'VISTA ALEGRE'],
                       node_color='grey',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,
                       nodelist=['ANTONIO MACHADO', 'ARROYOFRESNO', 'AVDA. DE LA ILUSTRACION', 'FRANCOS RODRIGUEZ', 'LACOMA', 'PEÑAGRANDE', 'PITIS', 'VALDEZARZA'],
                       node_color='brown',
                       node_size=500,
                   alpha=0.8)

nx.draw_networkx_nodes(g,pos,data = True,
                       nodelist=['BARRIO DEL PILAR', 'HERRERA ORIA', 'Mirasierra', 'PACO DE LUCIA', 'VENTILLA'],
                       node_color='teal',
                       node_size=500,
                   alpha=0.8, label =True)


labels = {}
for node in g.nodes():
    labels[node] = node

nx.draw_networkx_labels(g,pos,labels,font_size=8,font_color='b')
#
nx.draw_networkx_edges(g,pos,width=1.0,alpha=0.5)
# plt.show()

print('Asortatividad: ', nx.degree_assortativity_coefficient(g))

################################################
# EXPORTAR NODOS A JSON:
################################################

json_data = json_graph.node_link_data(g)
with open('grafo_completo.json', 'w') as file:
    json.dump(json_data, file, indent='\t')