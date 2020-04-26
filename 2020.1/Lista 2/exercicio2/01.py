import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adj = [
        [0,0,1,1,1,0],
        [0,0,1,1,1,0],
        [1,1,0,0,1,0],
        [1,1,0,0,1,0],
        [1,1,1,1,0,0],
        [0,0,0,0,0,0]]

print("Matriz de Adjacência")
for linha in adj:
    print(linha)

nadj = np.array(adj)

graph = nx.from_numpy_matrix(nadj)

fig = plt.figure()

#mapping = dict(zip(graph, range(1, 7)))

#graph = nx.relabel_nodes(graph, mapping) 

g = nx.relabel_nodes(graph, lambda x: x + 1)

nx.draw(g, with_labels=True)

plt.show()

