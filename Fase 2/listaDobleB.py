from nodoDobleB import NodoDobleB

class ListaDobleB:
    def __init__(self):
        self.cuenta = 0
        self.primero = None
        self.ultimo = None

    def isEmpty(self):
        return self.primero == None

    def insertarNodoD(self, codigo, pais):
        nuevo = NodoDobleB(codigo, pais)
        if (self.cuenta < 4):
            if (self.isEmpty()):
                self.primero = nuevo
                self.ultimo = self.primero
            else:
                self.ultimo.setSiguiente(nuevo)
                nuevo.setAnterior(self.ultimo)
                self.ultimo = nuevo
            self.cuenta += 1
        else:
            print('Limites superados')

    def setDato(self, codigo, posicion):
        aux = self.primero
        while(posicion != 0):
            posicion -= 1
            aux = aux.getSiguiente()
        aux.setCodigo(codigo)

    def getDato(self, posicion):
        aux = self.primero
        while(posicion != 0):
            posicion -= 1
            aux = aux.getSiguiente()
        return aux

    def showDatos(self):
        aux = self.primero
        while(aux != None):
            print(f'Dato {aux.getCodigo()}')
            aux = aux.getSiguiente()