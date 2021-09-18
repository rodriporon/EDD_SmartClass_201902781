from listaPunteroB import ListaPunteroP
from listaDobleB import ListaDobleB

class PaginaB:

    cuenta = 0
    punteros = ListaPunteroP()
    datos = ListaDobleB()

    def __init__(self):
        for i in range(5):
            if (i != 4):
                self.datos.insertarNodoD("", None)
            self.punteros.setPuntero(None)
        self.maxClaves = 5

    def paginaLlena(self):
        return (self.cuenta == self.maxClaves - 1)

    def paginaSemiLlena(self):
        return (self.cuenta == self.maxClaves / 2)

    def getCuenta(self):
        return self.cuenta

    def setCuenta(self, c):
        self.cuenta = c

    def getMaxClaves(self):
        return self.maxClaves

    def setMaxClaves(self, m):
        self.maxClaves = m

    def getCodigo(self, i):
        return self.datos.getDato(i).getCodigo()

    def setCodigo(self, i, codigo):
        self.datos.setDato(codigo, i)

    def getPais(self, i):
        return self.datos.getDato(i).getPais()

    def setPais(self, i, pais):
        self.datos.getDato(i).setPais(pais)

    def getApuntador(self, i):
        return self.punteros.getPuntero(i).getPuntero()

    def setApuntador(self, i, puntero):
        self.punteros.setPunteroP(puntero, i)

