import collections

inf = float('inf')

class Graph:
    def __init__(self):
        self.vertex = []
        self.edged = []

    def vertices(self):
        return [vertice for vertice in self.vertex]
    
    def edges(self):
        return [edge for edge in self.edged]

    def incidentEdges(self, v):
        return v.edged

    def endVertices(self, e):
        return e.conecta

    def areAdajacent(self, v, w):
        for aresta in v.edged:
            if w in aresta.conecta:
                return True
        return False

    def replace(self, v, x):
        if v in self.vertices():
            v.info = x        
        return

    def addVertex(self, label, info):
        vertice = Vertex(label, info)
        self.vertex.append(vertice)
        return vertice

    def addEdged(self, label, info, conecta1, conecta2):
        e = Edged(label, info, conecta1, conecta2)
        conecta1.edged.append(e)
        self.edged.append(e)
        return e

    def opposite(self, v, e):
        if v not in e.conecta:
            raise Exception("Aresta não é incidente do vertice.")

        else:
            if v == e.conecta[0]:
                return e.conecta[1]
            
            else:
                return e.conecta[0]

    def BellmanFord(self, start, end):
        assert start in self.vertex, 'O vertice de inicio não existe'
        assert end in self.vertex, 'O vertice de destino não existe'

        distancia = dict.fromkeys([v.label for v in self.vertex],inf)
        anteriores = {
            vertex.label: [] for vertex in self.vertex
        }

        distancia[start.label] = 0

        for i in range(len(self.vertex) - 1):
            for v in self.vertex:
                for adjacente, e in [(self.opposite(v,e),e) for e in v.edged]:
                    if distancia[adjacente.label] > distancia[v.label] + e.info:
                        distancia[adjacente.label] = distancia[v.label] + e.info
                        anteriores[adjacente.label] = v.label

        for v in self.vertex:
            for adjacente, e in [(self.opposite(v,e),e) for e in v.edged]:
                assert distancia[adjacente.label] <= distancia[v.label] + e.info, "Ciclo de Peso Negativo"

        caminho = [end.label]
        atual = end
        while True:
            if anteriores[atual.label] == start.label:
                caminho.append(anteriores[atual.label])
                break
            else:
                caminho.append(anteriores[atual.label])
                atual = [v for v in self.vertex if v.label == anteriores[atual.label]].pop()
        
        caminho.reverse()

        return (distancia[end.label], caminho)


class Vertex:
    def __init__(self, label, info):
        self.label = label
        self.info = info
        self.edged = []

    def __eq__(self, other):
        return self.label == other.label

    
    def __hash__(self):
        return hash(self.label)

    def replace(v, x):
        v.info = x        
        return

class Edged:
    def __init__(self, label, info, conecta, connecta2):
        self.label = label
        self.info = info
        self.conecta = [conecta,connecta2]
    
    def __eq__(self, other):
        return self.label == other.label

    def replace(e, x):
        e.info = x        
        return

if __name__ == "__main__":

    grafo = Graph()

    # Vertices
    a = grafo.addVertex("A",0)
    b = grafo.addVertex("B",0)
    c = grafo.addVertex("C",0)
    d = grafo.addVertex("D",0)
    e = grafo.addVertex("E",0)


    # Arestas
    um = grafo.addEdged("um",6,a,b)
    dois = grafo.addEdged("dois",7,a,c)
    tres = grafo.addEdged("tres",8,b,c)
    quatro = grafo.addEdged("quatro",2,a,e)
    cinco = grafo.addEdged("cinco",5,b,d)
    seis = grafo.addEdged("seis",9,c,e)
    sete = grafo.addEdged("sete",-4,b,e)
    oito = grafo.addEdged("oito",-3,c,d)
    nove = grafo.addEdged("nove",7,e,d)
    dez  = grafo.addEdged("dez",-2,d,b)

    print("De A para B: " + str(grafo.BellmanFord(a,b)))
    print("De A para C: " + str(grafo.BellmanFord(a,c)))
    print("De A para D: " + str(grafo.BellmanFord(a,d)))
    print("De A para E: " + str(grafo.BellmanFord(a,e)))