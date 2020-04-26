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
    
    # Primeiro
    grafo = Graph()

    a = grafo.addVertex("a",0)
    b = grafo.addVertex("b",0)
    c = grafo.addVertex("c",0)
    d = grafo.addVertex("d",0)
    e = grafo.addVertex("e",0)

    um = grafo.addEdged("um",6,a,b)
    dois = grafo.addEdged("dois",1,a,d)
    tres = grafo.addEdged("tres",5,b,c)
    quatro = grafo.addEdged("quatro",2,d,b)
    cinco = grafo.addEdged("cinco",1,d,e)
    seis = grafo.addEdged("seis",2,b,e)
    sete = grafo.addEdged("sete",5,e,c)


    print(grafo.dijkstra(a,c))

    # Segundo
    grafo = Graph()

    a = grafo.addVertex("a",0)
    b = grafo.addVertex("b",0)
    c = grafo.addVertex("c",0)
    d = grafo.addVertex("d",0)
    e = grafo.addVertex("e",0)
    f = grafo.addVertex("f",0)
    g = grafo.addVertex("g",0)
    h = grafo.addVertex("h",0)
    i = grafo.addVertex("i",0)

    um = grafo.addEdged("um",2,a,b)
    dois = grafo.addEdged("dois",5,a,c)
    tres = grafo.addEdged("tres",2,a,d)
    quatro = grafo.addEdged("quatro",3,b,c)
    cinco = grafo.addEdged("cinco",1,b,e)
    seis = grafo.addEdged("seis",3,c,d)
    sete = grafo.addEdged("sete",1,c,e)
    oito = grafo.addEdged("oito",1,c,f)
    nove = grafo.addEdged("nove",1,c,h)
    dez = grafo.addEdged("dez",2,d,g)
    onze = grafo.addEdged("onze", 7,e,i)
    doze = grafo.addEdged("doze",2,f,g)
    treze = grafo.addEdged("treze",3,f,h)
    quatorze = grafo.addEdged("quatorze",1,h,i)

    print(grafo.dijkstra(a,i))

    # Terceiro
    grafo = Graph()

    a = grafo.addVertex("a",0)
    b = grafo.addVertex("b",0)
    c = grafo.addVertex("c",0)
    d = grafo.addVertex("d",0)
    e = grafo.addVertex("e",0)

    um = grafo.addEdged("um",1,a,b)
    dois = grafo.addEdged("dois",3,a,c)
    tres = grafo.addEdged("tres",7,b,c)
    quatro = grafo.addEdged("quatro",1,b,e)
    cinco = grafo.addEdged("cinco",5,b,d)
    seis = grafo.addEdged("seis",2,c,d)
    sete = grafo.addEdged("sete",7,d,e)

    print(grafo.dijkstra(a,e))