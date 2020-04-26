import networkx as nx
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=2)
ax = axes.flatten()

# Grau 1
g1 = nx.Graph()

g1.add_node(1)

nx.draw_networkx(g1, ax=ax[0], node_size=100,font_size=10, scale=0.2)
ax[0].set_axis_off()

# Grau 2
g2 = nx.Graph()

g2.add_nodes_from([1,2])

g2.add_edge(1,2)

nx.draw_networkx(g2, ax=ax[1], node_size=100,font_size=10, scale=0.2)
ax[1].set_axis_off()


# Grau 3

g3 = nx.Graph()

g3.add_nodes_from([1,2,3])

g3.add_edges_from([(1,2),(1,3),(2,3)])

nx.draw_networkx(g3, ax=ax[2], node_size=100,font_size=10, scale=0.2)
ax[2].set_axis_off()


# Grau 4
g4 = nx.Graph()

g4.add_nodes_from([1,2,3,4])

g4.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])

nx.draw_networkx(g4, ax=ax[3], node_size=100,font_size=10, scale=0.2)
ax[3].set_axis_off()

plt.show()