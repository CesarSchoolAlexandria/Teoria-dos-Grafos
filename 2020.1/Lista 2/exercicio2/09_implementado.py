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
        conecta2.edged.append(e)
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

    def dijkstra(self, start, end):
        assert start in self.vertex, 'O vertice de inicio não existe'
        assert end in self.vertex, 'O vertice de destino não existe'

        passou = set(self.vertex)
        distancia = dict.fromkeys([v.label for v in self.vertex])
        anteriores = {
            vertex.label: [] for vertex in self.vertex
        }

        for v in self.vertex:
            distancia[v.label] = inf
        distancia[start.label] = 0

        while passou != set():
            closest = min(passou, key=lambda k: distancia[k.label])

            passou.remove(closest)
    
            for adjacente, e in [(self.opposite(closest,e),e) for e in closest.edged]:
                if adjacente in passou:
                    nova_distancia = distancia[closest.label] + e.info
                    if distancia[adjacente.label] > nova_distancia:
                        distancia[adjacente.label] = nova_distancia
                        anteriores[adjacente.label] = closest.label                       

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
    o = grafo.addVertex("O",0)
    a = grafo.addVertex("A",0)
    b = grafo.addVertex("B",0)
    c = grafo.addVertex("C",0)
    d = grafo.addVertex("D",0)
    e = grafo.addVertex("E",0)
    t = grafo.addVertex("T",0)

    # Arestas
    um = grafo.addEdged("um",2,o,a)
    dois = grafo.addEdged("dois",5,o,b)
    tres = grafo.addEdged("tres",4,o,c)
    quatro = grafo.addEdged("quatro",2,a,b)
    cinco = grafo.addEdged("cinco",7,a,d)
    seis = grafo.addEdged("seis",1,b,c)
    sete = grafo.addEdged("sete",4,b,d)
    oito = grafo.addEdged("oito",3,b,e)
    nove = grafo.addEdged("nove",4,c,e)
    dez  = grafo.addEdged("dez",1,d,e)
    onze = grafo.addEdged("onze",5,d,t)
    doze = grafo.addEdged("doze",7,e,t)

    print("De O para A: " + str(grafo.dijkstra(o,a)))
    print("De O para B: " + str(grafo.dijkstra(o,b)))
    print("De O para C: " + str(grafo.dijkstra(o,c)))
    print("De O para D: " + str(grafo.dijkstra(o,d)))
    print("De O para E: " + str(grafo.dijkstra(o,e)))
    print("De O para T: " + str(grafo.dijkstra(o,t)))