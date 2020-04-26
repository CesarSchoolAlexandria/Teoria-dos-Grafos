import itertools

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

class Vertex:
    def __init__(self, label, info):
        self.label = label
        self.info = info
        self.edged = []

    def __eq__(self, other):
        return self.label == other.label

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

    #Grafo 1
    g = Graph()
    g.addVertex("a","um")

    #Grafo 2
    gr = Graph()
    a = gr.addVertex("a","um")
    b = gr.addVertex("b","dois")
    gr.addEdged("1","vermelho",a,b)

    #Grafo 3
    gra = Graph()
    a = gra.addVertex("a","um")
    b = gra.addVertex("b","dois")
    c = gra.addVertex("c", "tres")
    gra.addEdged("1","vermelho",a,b)
    gra.addEdged("2","azul",a,c)
    gra.addEdged("3","laranja",b,c)

    #Grafo 4
    graf = Graph()
    a = graf.addVertex("a","um")
    b = graf.addVertex("b","dois")
    c = graf.addVertex("c", "tres")
    d = graf.addVertex("d","quatro")
    graf.addEdged("1","vermelho",a,b)
    graf.addEdged("2","azul",a,c)
    graf.addEdged("3","branco",a,d)
    graf.addEdged("4","laranja",b,c)
    graf.addEdged("5","preto",b,d)
    graf.addEdged("6","roxo",c,d)

    #Grafo 5
    grafo = Graph()
    a = grafo.addVertex("a","um")
    b = grafo.addVertex("b","dois")
    c = grafo.addVertex("c", "tres")
    d = grafo.addVertex("d","quatro")
    e = grafo.addVertex("e","cinco")
    um = grafo.addEdged("1","vermelho",a,b)
    dois = grafo.addEdged("2","azul",a,c)
    tres = grafo.addEdged("3","branco",a,d)
    quatro = grafo.addEdged("4","verde",a,e)
    cinco = grafo.addEdged("5","laranja",b,c)
    seis = grafo.addEdged("6","preto",b,d)
    sete = grafo.addEdged("7","rosa",b,e)
    oito = grafo.addEdged("8","roxo",c,d)
    nove = grafo.addEdged("9","cinza",c,e)
    dez = grafo.addEdged("10","Ouro",d,e)

    # Testes de funções

    #print([vertice.label for vertice in grafo.vertices()])
    #print([vertice.info for vertice in grafo.vertices()])
    #print([aresta.label for aresta in grafo.edges()])
    #print([aresta.info for aresta in grafo.edges()])
    #print(grafo.endVertices(um)[0].label)
    #print(grafo.incidentEdges(a)[0].label)
    #print(Edged.opposite("a",g.incidentEdges("a")[0]))
    print(grafo.opposite(b,um))
    print(grafo.opposite(c,seis))
    #print(grafo.areAdajacent(a,b))
    #print(g.areAdajacent(a,e))
    #Vertex.replace(a,"seis")
    #Edged.replace(um,"Prata")
    #print(a.info)
    #print(um.info)