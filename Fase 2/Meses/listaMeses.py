from Meses.nodoMeses import NodoMeses

class ListaMeses:
    def __init__(self):
        self.nodo_inicial = None


    def insertar(self, valor):
        if self.nodo_inicial is None:
            nuevo_nodo = NodoMeses(valor)
            self.nodo_inicial = nuevo_nodo
            return nuevo_nodo
        else:
            aux = self.nodo_inicial
            while aux.siguiente is not None:
                aux = aux.siguiente
            nuevo_nodo = NodoMeses(valor)
            aux.siguiente = nuevo_nodo
            nuevo_nodo.anterior = aux
            return nuevo_nodo

    def MostrarAños(self):
        if self.nodo_inicial is None:
            print("      "+'Empty list')
        else:
            aux = self.nodo_inicial
            while aux is not None:
                print("             "+str(aux.valor), " ")
                aux = aux.siguiente