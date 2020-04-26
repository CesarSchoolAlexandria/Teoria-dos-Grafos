import networkx as nx
import matplotlib
import matplotlib.pyplot as plt


fig, axes = plt.subplots(nrows=4, ncols=3,figsize=(50,50))

ax = axes.flatten()

# primeiro
g1 = nx.Graph()

g1.add_nodes_from([1,2,3,4])

nx.draw_networkx(g1, ax=ax[0], node_size=100,font_size=10, scale=0.2)


# segundo
g2 = nx.Graph()

g2.add_nodes_from([1,2,3,4])
g2.add_edges_from([(1,2)])

nx.draw_networkx(g2, ax=ax[1], node_size=100,font_size=10, scale=0.2)


# Terceiro
g3 = nx.Graph()

g3.add_nodes_from([1,2,3,4])
g3.add_edges_from([(1,2),(1,3)])

nx.draw_networkx(g3, ax=ax[2], node_size=100,font_size=10, scale=0.2)


# Quarto
g4 = nx.Graph()

g4.add_nodes_from([1,2,3,4])
g4.add_edges_from([(1,2),(3,4)])

nx.draw_networkx(g4, ax=ax[3], node_size=100,font_size=10, scale=0.2)

# Quinto
g5 = nx.Graph()

g5.add_nodes_from([1,2,3,4])
g5.add_edges_from([(1,2),(1,3),(2,3)])

nx.draw_networkx(g5, ax=ax[4], node_size=100,font_size=10, scale=0.2)

# Sexto
g6 = nx.Graph()

g6.add_nodes_from([1,2,3,4])
g6.add_edges_from([(1,2),(2,3),(3,4)])

nx.draw_networkx(g6, ax=ax[5], node_size=100,font_size=10, scale=0.2)

# Setimo
g7 = nx.Graph()

g7.add_nodes_from([1,2,3,4])
g7.add_edges_from([(1,2),(1,3),(1,4)])

nx.draw_networkx(g7, ax=ax[6], node_size=100,font_size=10, scale=0.2)

# Oitavo
g8 = nx.Graph()

g8.add_nodes_from([1,2,3,4])
g8.add_edges_from([(1,2),(2,3),(3,4),(1,4)])

nx.draw_networkx(g8, ax=ax[7], node_size=100,font_size=10, scale=0.2)

# Nono
g9 = nx.Graph()

g9.add_nodes_from([1,2,3,4])
g9.add_edges_from([(1,2),(2,3),(1,3),(2,4)])

nx.draw_networkx(g9, ax=ax[8], node_size=100,font_size=10, scale=0.2)

# Decimo
g10 = nx.Graph()

g10.add_nodes_from([1,2,3,4])
g10.add_edges_from([(1,2),(2,3),(3,4),(1,4),(2,4)])

nx.draw_networkx(g10, ax=ax[9], node_size=100,font_size=10, scale=0.2)

# Decimo Primeiro
g11 = nx.Graph()

g11.add_nodes_from([1,2,3,4])
g11.add_edges_from([(1,2),(2,3),(3,4),(1,4),(2,4),(1,3)])

nx.draw_networkx(g11, ax=ax[10], node_size=100,font_size=10, scale=0.2)

fig.delaxes(ax[11])

fig.suptitle("Existem 11 Grafos Isométricos simples com 4 vértices")

plt.show()