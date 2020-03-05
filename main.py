
import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('grafo.csv', delimiter=',', data=(('nombre',str),))
print(nx.info(g))

print(g.edges(data = True))

plt
nx.draw(g, with_labels=True)
plt.show()

