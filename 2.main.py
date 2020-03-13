
import networkx as nx
import matplotlib.pyplot as plt
import csv

with open('grafo_nodes.csv', 'r', newline='', encoding="utf-8") as csvfile:
    contenido = csv.reader(csvfile, delimiter=',')
    next(contenido, None)

    g = nx.read_edgelist('grafo_edges.csv', delimiter=',', encoding="utf-8")

    print(nx.info(g))
    print(g.edges(data = True))

    for line in contenido:
        print(line[0], line[1])
        g.nodes[line[0]]['labels'] = line[1]

    print(g.edges)
    print(g.nodes(data=True))

    # plt
    nx.draw(g, with_labels=True)
    # plt.show()

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
    # Las estaciones que más grado tengan serán las que estén en más líneas y las más relevantes

    ########################
    # CAMINOS:
    ########################

    # Idea: ordenar los caminos para proponer una nueva ruta en caso de que alguna estación este en obras o fuera de servicio: all_simple_paths
    # Idea: si un nodo está caido, eliminarlo del grafo y ver las rutas alternativas (volver a ejecutar el shortest y daría el más corto)

    # print("Caminos más cortos:")
    # for path in nx.all_shortest_paths(g, 'par_4_120', 'par_4_50'):
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
    #
    # for line in nx.generate_adjlist(g):
    #     print(line)
    ########################
    # DENSIDAD:
    ########################

    # print('Densidad del grafo: ', nx.density(g))


    # draw_networkx_labels para los nombre de las estaciones





