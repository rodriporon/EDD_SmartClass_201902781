class NodoDobleB:
    def __init__(self, codigo, pais):
        self.codigo = codigo
        self.pais = pais
        self.siguiente = None
        self.anterior = None

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, c):
        self.codigo = c

    def getPais(self):
        return self.pais

    def setPais(self, p):
        self.pais = p

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, s):
        self.siguiente = s

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, a):
        self.anterior = a

            