from nodoPunteroB import NodoPunteroB

class ListaPunteroP:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def isEmpty(self):
        return self.primero == None

    def setPuntero(self, puntero):
        nuevo = NodoPunteroB(puntero)
        if (self.cuenta < 5):
            if (self.isEmpty()):
                self.primero = nuevo
                self.ultimo = self.primero
            else:
                self.ultimo.setSiguienteP(nuevo)
                nuevo.setAnteriorP(self.ultimo)
                self.ultimo = nuevo
            self.cuenta += 1

    def setPunteroP(self, pagina, i):
        aux = self.primero
        while (i != 0):
            i -= 1
            aux = aux.getSiguienteP()
        aux.setPuntero(pagina)

    def getPuntero(self, i):
        aux = self.primero
        while (i != 0):
            i -= 1
            aux = aux.getSiguienteP()
        return aux

    def setPrimero(self, primero):
        self.primero = primero

    def getCuenta(self):
        return self.cuenta

    def setCuenta(self, c):
        self.cuenta = c

    