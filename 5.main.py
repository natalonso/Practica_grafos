
import networkx as nx
import networkx.algorithms.community as nxComm
import json
from networkx.readwrite import json_graph

import matplotlib.pyplot as plt
import csv


g = nx.read_edgelist('grafo_edges_names.csv', delimiter=',', encoding="utf-8-sig")

nodes = g.nodes(data = True)
edges = g.edges(data = False)

print('ANÁLISIS DESCRIPTIVO: ')

########################
# ADYACENCIA:
########################

for node in g.nodes:
    if node == 'SOL':
        print("Ejemplo: adyacencia de SOL: ", str(node) + " -> " + str(g.adj[node]))

########################
# GRADO:
########################

for node in g.nodes:
    if node == 'SOL':
        print("Ejemplo grado de SOL: ",  str(g.degree[node]))

########################
# CAMINOS:
########################

for path in nx.all_shortest_paths(g, 'GOYA', 'OPERA'):
    print("Ejemplo camino más corto entre Goya y Opera:", str(path))

########################
# CONECTIVIDAD:
########################

print("¿Es conexo? " + str(nx.is_connected(g)))
print("Número de componentes conexas: " + str(nx.number_connected_components(g)))

########################
# DENSIDAD:
########################

print('Densidad del grafo: ', nx.density(g))

########################
# Degree centrality:
########################

degree = nx.degree_centrality(g)
for node in degree:
    if node == 'SOL':
        print("Grado de centralidad de SOL: ", degree[node])


########################
# Closeness centrality:
########################

# Podria ayudar a ver las estaciones del centro de la ciudad en caso de querer reforzar esta zona

closeness = nx.closeness_centrality(g)
for node in closeness:
    if node == 'SOL':
        print("Closeness de SOL: ", closeness[node])

########################
# Betweenness centrality:
########################

# Medir la importancia de un nodo en función de cuántas estaciones (o nodos) dejas din servicio en caso de caerse ese nodo

betweenness = nx.betweenness_centrality(g)
for node in betweenness:
    if node == 'SOL':
        print("Betweenness de SOL: ", betweenness[node])

################################################
# Comparación de todos los métodos:
################################################

maxDG = max(degree, key=lambda key: degree[key])
maxCL = max(closeness, key=lambda key: closeness[key])
maxBT = max(betweenness, key=lambda key: betweenness[key])

print("Máximo Degree: " + maxDG + " -> {0:.2f}".format(degree[maxDG]))
print("Máximo Closeness: " + maxCL + " -> {0:.2f}".format(closeness[maxCL]))
print("Máximo Betweenness: " + maxBT + " -> {0:.2f}".format(betweenness[maxBT]))

################################################
# Edges Betweeness:
################################################

centrality = nx.edge_betweenness_centrality(g)

for edge in centrality:
    if edge[0] == 'GRAN VIA' and edge[1] == 'SOL':
        print("Ejemplo edge betweeness entre Gran Vía y Sol: ", centrality[edge])

#############################################################
# Número medio de saltos en los caminos más cortos y diámetro:
#############################################################

print("Número medio de saltos en los caminos más cortos: " + str(nx.average_shortest_path_length(g)))
print("Número de saltos en el camino más largo en el grafo (diámetro): " + str(nx.diameter(g)))

################################################
# ASIGNAR ATRIBUTOS A LOS NODOS:
################################################

atributos_nodos = open("grafo_nodes.csv", "r", encoding= "utf-8")
csvReader_nodes = csv.reader(atributos_nodos, delimiter=',', lineterminator='\n')

atributos_edges = open("grafo_edges.csv", "r", encoding= "utf-8")
csvReader_edges = csv.reader(atributos_edges, delimiter=',', lineterminator='\n')

atributos_nodes=[]
for line in csvReader_nodes:
    atributos_nodes.append(line)

atributos_edges=[]
for line in csvReader_edges:
    atributos_edges.append(line)

for node in nodes:
    for line in atributos_nodes:
        if line[0] == node[0]:
            if line[0] == 'Fuencarral':
                g.nodes[node[0]]["lat"] = 40.495247
                g.nodes[node[0]]["lon"] = -3.693261
            elif line[0] == 'Manuela Malasaña':
                g.nodes[node[0]]["lat"] = 40.3091
                g.nodes[node[0]]["lon"] = -3.86399
            elif line[0] == 'San Francisco':
                g.nodes[node[0]]["lat"] = 40.3736
                g.nodes[node[0]]["lon"] = -3.73911
            elif line[0] == 'Arturo Soria':
                g.nodes[node[0]]["lat"] = 40.4558
                g.nodes[node[0]]["lon"] = -3.65617
            elif line[0] == 'Mirasierra':
                g.nodes[node[0]]["lat"] = 40.4907
                g.nodes[node[0]]["lon"] = -3.71602
            elif line[0] == 'Guzmán el Bueno':
                g.nodes[node[0]]["lat"] = 40.4463
                g.nodes[node[0]]["lon"] = -3.71224
            elif line[0] == 'Avenida de Guadalajara':
                g.nodes[node[0]]["lat"] = 40.4222
                g.nodes[node[0]]["lon"] = -3.61196
            else:
                g.nodes[node[0]]["lat"] = float(line[1])
                g.nodes[node[0]]["lon"] = float(line[2])

    g.nodes[node[0]]["degree"] = degree[node[0]]
    g.nodes[node[0]]["closeness"] = closeness[node[0]]
    g.nodes[node[0]]["betweenness"] = betweenness[node[0]]


for edge in edges:
    edge = (edge[0],edge[1])
    g.edges[edge]["betweenness"] = centrality[edge]

    for line in atributos_edges:
        line[0] = line[0].replace('\ufeff','')
        source_target = (line[0], line[1])
        target_source = (line[1], line[0])

        if source_target == edge:
            g.edges[edge]["line"] = line[2]
            g.edges[edge]["source_lat"] = float(g.nodes[line[0]]["lat"])
            g.edges[edge]["source_lon"] = float(g.nodes[line[0]]["lon"])
            g.edges[edge]["target_lat"] = float(g.nodes[line[1]]["lat"])
            g.edges[edge]["target_lon"] = float(g.nodes[line[1]]["lon"])

        if target_source == edge:
            g.edges[edge]["line"] = line[2]
            g.edges[edge]["source_lat"] = float(g.nodes[line[1]]["lat"])
            g.edges[edge]["source_lon"] = float(g.nodes[line[1]]["lon"])
            g.edges[edge]["target_lat"] = float(g.nodes[line[0]]["lat"])
            g.edges[edge]["target_lon"] = float(g.nodes[line[0]]["lon"])

################################################
# EXPORTAR NODOS A JSON:
################################################

json_data = json_graph.node_link_data(g)
with open('grafo_completo.json', 'w') as file:
    json.dump(json_data, file, indent='\t')


print('Terminado análisis descriptivo y creación del json')