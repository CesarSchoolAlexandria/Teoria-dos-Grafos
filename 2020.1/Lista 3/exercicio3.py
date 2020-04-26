class Position:
    def __init__(self, elemento: int):
        self.elemento = elemento
        self.pai = None
        self.filhoEsquerdo = None
        self.filhoDireito = None

    def getElemento(self):
        return self.elemento

    def setElemento(self, elemento: int):
        self.elemento = elemento

    def getPai(self):
        return self.pai
    
    def setPai(self, pai):
        assert isinstance(pai,Position)
        self.pai = pai

    def getFilhoEsquerdo(self):
        return self.filhoEsquerdo

    def setFilhoEsquerdo(self, filhoEsquerdo):
        assert isinstance(filhoEsquerdo,Position)
        self.filhoEsquerdo = filhoEsquerdo

    def getFilhoDireito(self):
        return self.filhoDireito
    
    def setFilhoDireito(self, filhoDireito):
        assert isinstance(filhoDireito,Position)
        self.filhoDireito = filhoDireito

    pass

class LinkedBinaryTree:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def getRaiz(self):
        return self.raiz

    def setRaiz(self, position):
        assert isinstance(position,Position)
        self.raiz = position

    def getTamanho(self):
        return self.tamanho
    
    def setTamanho(self, tamanho: int):
        self.tamanho = tamanho

    def isEmpty(self):
        if(self.getRaiz() == None):
            return True
        else:
            return False
    
    def isInternal(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        if not any(self.children(v)):
            return False
        else:
            return True

    def isExternal(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        if not any(self.children(v)):
            return True
        else:
            return False

    def isRoot(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        if(self.getRaiz() == v):
            return True
        else:
            return False

    def hasLeft(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        if(v.getFilhoEsquerdo() == None):
            return False
        else:
            return True

    def hasRight(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        if(v.getFilhoDireito() == None):
            return False
        else:
            return True

    def left(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        return v.getFilhoEsquerdo()
    
    def right(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        return v.getFilhoDireito()

    def parent(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        return v.getPai()

    def children(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        return [v.getFilhoEsquerdo(),v.getFilhoDireito()]

    def addRoot(self, i: int):
        raiz = Position(i)
        self.setRaiz(raiz)
        self.setTamanho(1)

    def insertLeft(self, v, i: int):
        assert isinstance(v,Position), ("Argument must be a Position")
        filho = Position(i)
        filho.setPai(v)
        v.setFilhoEsquerdo(filho)
        self.setTamanho(self.getTamanho() + 1)

    def insertRight(self, v, i: int):
        assert isinstance(v,Position), ("Argument must be a Position")
        filho = Position(i)
        filho.setPai(v)
        v.setFilhoDireito(filho)
        self.setTamanho(self.getTamanho() + 1)

    def toStringPreOrder(self):
        raiz = self.getRaiz()
        result = ""

        if raiz:
            arvoreSuppEsquerda = LinkedBinaryTree()
            if self.hasLeft(raiz):
                arvoreSuppEsquerda.setRaiz(self.left(raiz))
        
            arvoreSuppDireita = LinkedBinaryTree()
            if self.hasRight(raiz):
                arvoreSuppDireita.setRaiz(self.right(raiz))
                
            result += " " + str(raiz.getElemento())
            result += arvoreSuppEsquerda.toStringPreOrder()
            result += arvoreSuppDireita.toStringPreOrder()

        return result

    def toStringPosOrder(self):
        raiz = self.getRaiz()
        result = ""

        if raiz:
            arvoreSuppEsquerda = LinkedBinaryTree()
            if self.hasLeft(raiz):
                arvoreSuppEsquerda.setRaiz(self.left(raiz))
        
            arvoreSuppDireita = LinkedBinaryTree()
            if self.hasRight(raiz):
                arvoreSuppDireita.setRaiz(self.right(raiz))
                
            result += arvoreSuppEsquerda.toStringPosOrder()
            result += arvoreSuppDireita.toStringPosOrder()
            result += " " + str(raiz.getElemento())

        return result

    def depth(self, v):
        assert isinstance(v,Position), ("Argument must be a Position")
        res = 0

        if self.parent(v) is not None:
            res += 1 + self.depth(self.parent(v))

        return res

    pass


if __name__ == "__main__":
    arvore = LinkedBinaryTree()

    arvore.addRoot(1)

    arvore.insertLeft(arvore.getRaiz(), 2)
    arvore.insertRight(arvore.getRaiz(),3)
    arvore.insertLeft(arvore.getRaiz().getFilhoEsquerdo(), 4)
    arvore.insertRight(arvore.getRaiz().getFilhoEsquerdo(),5)

    print(arvore.toStringPreOrder())
    print(arvore.toStringPosOrder())
    print(arvore.depth(arvore.getRaiz().getFilhoEsquerdo().getFilhoDireito()))
    pass