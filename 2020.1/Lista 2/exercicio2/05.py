import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adj = [
        [0,0,0,1,1,0],
        [0,0,1,1,1,1],
        [0,1,0,0,1,0],
        [1,1,0,0,1,1],
        [1,1,1,1,0,0],
        [0,1,0,1,0,0]]

print("Matriz de Adjacência")
for linha in adj:
    print(linha)

nadj = np.array(adj)

graph = nx.from_numpy_matrix(nadj)

fig, axes = plt.subplots(nrows=3, ncols=2,figsize=(50,50))

ax = axes.flatten()

g = nx.relabel_nodes(graph, lambda x: x + 1)

# Grafo
nx.draw_networkx(g, ax=ax[0], node_size=100,font_size=10, scale=0.2)
ax[0].set_title('Grafo')

#Caminho
# (1,4) - (1,5) - (2,3) - (2,4) - (2,5) - (2,6) - (3,5) - (4,5) - (4,6)
caminho = ('r','r','b','b','r','b','b','r','b')

nx.draw_networkx(g, ax=ax[1], node_size=100,font_size=10, scale=0.2, edge_color = caminho)
ax[1].set_title('Caminho - (2,5),(5,1),(1,4),(4,5)')

# Trilha
# (1,4) - (1,5) - (2,3) - (2,4) - (2,5) - (2,6) - (3,5) - (4,5) - (4,6)
trilha = ('r','r','b','b','b','r','b','b','r')

nx.draw_networkx(g, ax=ax[2], node_size=100,font_size=10, scale=0.2, edge_color = trilha)
ax[2].set_title('Trilha - (2,5),(5,1),(1,4),(4,6)')

# Ciclo
# (1,4) - (1,5) - (2,3) - (2,4) - (2,5) - (2,6) - (3,5) - (4,5) - (4,6)
trilha = ('r','r','b','r','r','b','b','b','b')

nx.draw_networkx(g, ax=ax[3], node_size=100,font_size=10, scale=0.2, edge_color = trilha)
ax[3].set_title('Ciclo - (1,5),(5,2),(2,4),(4,1)')

# Ciclo hamiltoniano 
# (1,4) - (1,5) - (2,3) - (2,4) - (2,5) - (2,6) - (3,5) - (4,5) - (4,6)
cicloh = ('r','r','r','b','b','r','r','b','r')

nx.draw_networkx(g, ax=ax[4], node_size=100,font_size=10, scale=0.2, edge_color = cicloh)
ax[4].set_title('Ciclo Hamiltoniano - (1,4),(4,6),(6,2),(2,3),(3,5),(5,1)')

# Ciclo Euclidiano 
# (1,4) - (1,5) - (2,3) - (2,4) - (2,5) - (2,6) - (3,5) - (4,5) - (4,6)
cicloh = ('r','r','r','r','r','r','r','r','r')

nx.draw_networkx(g, ax=ax[5], node_size=100,font_size=10, scale=0.2, edge_color = cicloh)
ax[5].set_title('Ciclo Euclidiano -  (4,6),(6,2),(2,3),(3,5),(5,2),(2,4),(4,5),(5,1),(1,4)')

plt.show()