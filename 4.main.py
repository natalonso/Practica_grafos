
import networkx as nx
import matplotlib.pyplot as plt
import csv


g = nx.read_edgelist('grafo_edges_names.csv', delimiter=',', encoding="utf-8")

# print(nx.info(g))
# print(g.edges(data = True))
# print(g.nodes(data=True))

# plt
nx.draw(g, with_labels=True)
plt.show()

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
# Line graph:
################################################

# Transformar nodos en aristas y al reves ----> no nos aporta nada

################################################
# Edges Betweeness:
################################################

# centrality = nx.edge_betweenness_centrality(g)
# for node in centrality:
#     print("{0:s}-{1:s}({2:.2f})".format(node[0], node[1], centrality[node]), end='\n')

################################################
# Cliques:
################################################

# subgrafos cuyos nodos estén todos relacionados entre sí directamente
# En nuestro caso, habría agrupaciones como mucho de 2/3 estaciones ---> No resulta interesante en nuestro caso
#
# print("Todos los cliques maximos:")
# for max_clique in nx.find_cliques(g):
#     print(max_clique)

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