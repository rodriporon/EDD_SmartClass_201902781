from ArbolAVL.nodoDoble import NodoDoble

class ListaDoble:
    def __init__(self):
        self.nodo_inicial = None


    def insertar(self, valor):
        if self.nodo_inicial is None:
            nuevo_nodo = NodoDoble(valor)
            self.nodo_inicial = nuevo_nodo
        else:
            aux = self.nodo_inicial
            while aux.siguiente is not None:
                aux = aux.siguiente
            nuevo_nodo = NodoDoble(valor)
            aux.siguiente = nuevo_nodo
            nuevo_nodo.anterior = aux

    def MostrarAños(self):
        if self.nodo_inicial is None:
            print('Empty list')
        else:
            aux = self.nodo_inicial
            while aux is not None:
                print(aux.valor, " ")
                aux = aux.siguiente

