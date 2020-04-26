import networkx as nx
import matplotlib
import matplotlib.pyplot as plt


fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(50,50))

ax = axes.flatten()

# Primeiro
g = nx.Graph()

g.add_nodes_from([1,2,3,4,5])
g.add_edges_from([(1,2),(1,3),(2,4),(3,4),(3,5),(4,5)])

nx.draw_networkx(g, ax=ax[0], node_size=100,font_size=10, scale=0.2)

# Segundo
c = nx.Graph()
c.add_nodes_from([1,2,3,4,5])
c.add_edges_from([(1,4),(1,5),(2,3),(2,5)])
nx.draw_networkx(c, ax=ax[1], node_size=100,font_size=10, scale=0.2)

fig.suptitle("Grafos Simples Complementares com 5 vértices")

plt.show()