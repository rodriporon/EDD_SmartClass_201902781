from nodo import Nodo

class ListaDoble(Nodo):
    def __init__(self):
        super().__init__()
        self.cabeza = Nodo()
        self.contador = 0
        self.valor = self.__str__()


    def insert(self, nuevo_nodo):
        nodo = self.cabeza
        while(nodo.siguiente):
            nodo = nodo.siguiente
        nodo.siguiente = nuevo_nodo
        self.contador += 1
        self.valor = self.__str__()
    
    def get(self, i):
        if (i >= self.contador):
            return 'Limites sobrepasados'
        nodo = self.cabeza.siguiente
        n = 0
        while(nodo):
            if (n == i):
                return nodo
            nodo = nodo.siguiente
            n += 1

    def __getitem__(self, i):
        return self.get(i)