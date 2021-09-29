from Años.nodoAños import NodoAños
from graphviz import Digraph

class ListaAños:
    def __init__(self):
        self.nodo_inicial = None


    def insertar(self, valor):
        if self.nodo_inicial is None:
            nuevo_nodo = NodoAños(valor)
            self.nodo_inicial = nuevo_nodo
            return nuevo_nodo
        else:
            aux = self.nodo_inicial
            while aux.siguiente is not None:
                aux = aux.siguiente
            nuevo_nodo = NodoAños(valor)
            aux.siguiente = nuevo_nodo
            nuevo_nodo.anterior = aux
            return nuevo_nodo
    
    
    def showAños(self):
        if self.nodo_inicial is None:
            print("      "+'Empty list')
        else:
            aux = self.nodo_inicial
            while aux is not None:
                print("      "+str(aux.valor), " ")
                print(aux.meses.MostrarAños())
                aux = aux.siguiente

    def graficar(self):
        d = Digraph('listaAños', filename='ListaAños.gv',
                    node_attr={'shape': 'box'})
        cu_nodo = self.raiz
        pila = []
        d.attr(rankdir='TB')
        while True:
            if cu_nodo is not None:
                pila.append(cu_nodo)
                cu_nodo = cu_nodo.izquierda
            elif pila:
                cu_nodo = pila.pop()
                estudiante = ""
                estudiante += str(cu_nodo.carnet) + "\n" + \
                    str(cu_nodo.nombre) + "\n" + cu_nodo.carrera
                d.node(str(cu_nodo.carnet), label=estudiante)
                if cu_nodo.izquierda is not None:
                    d.edge(str(cu_nodo.carnet), str(cu_nodo.izquierda.carnet))
                if cu_nodo.derecha is not None:
                    d.edge(str(cu_nodo.carnet), str(cu_nodo.derecha.carnet))
                cu_nodo = cu_nodo.derecha
            else:
                break
        d.view()

