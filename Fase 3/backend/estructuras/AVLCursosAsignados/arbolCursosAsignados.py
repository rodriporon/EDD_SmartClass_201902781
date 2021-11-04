from estructuras.AVLCursosAsignados.nodoCursosAsignados import NodoCursosAsignados
from graphviz import Digraph

class ArbolCursosAsignados:
    def __init__(self):

        self.raiz = None

    def insertar(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        nuevo_nodo = NodoCursosAsignados(codigo, nombre, creditos, prerequisitos, obligatorio)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return nuevo_nodo
        else:
            self.raiz = self._insertar(nuevo_nodo, self.raiz)
            return nuevo_nodo

    def _insertar(self, new_nodo, cu_raiz):
        if cu_raiz is not None:
            if cu_raiz.codigo > new_nodo.codigo:
                cu_raiz.izquierda = self._insertar(
                    new_nodo, cu_raiz.izquierda)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == -2):
                    if (new_nodo.codigo < cu_raiz.izquierda.codigo):
                        cu_raiz = self.RI(cu_raiz)
                    else:
                        cu_raiz = self.RID(cu_raiz)

            elif cu_raiz.codigo < new_nodo.codigo:
                cu_raiz.derecha = self._insertar(
                    new_nodo, cu_raiz.derecha)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == 2):
                    if new_nodo.codigo > cu_raiz.derecha.codigo:
                        cu_raiz = self.RD(cu_raiz)
                    else:
                        cu_raiz = self.RDI(cu_raiz)

            cu_raiz.altura = self.datoMayor(self.verAltura(
                cu_raiz.derecha), self.verAltura(cu_raiz.izquierda)) + 1
            return cu_raiz
        else:
            cu_raiz = new_nodo
            return cu_raiz

    def datoMayor(self, a, b):
        if a > b:
            return a
        return b

    #Mostrar en recorrido inOrden la estructura del ArbolAVL
    def inOrden(self, cu_raiz):
        if cu_raiz is not None:
            #Función recursiva para mostrar todos los nodos izquierdos
            self.inOrden(cu_raiz.izquierda)
            print('-------------------------------------')
            #Codigo
            print(cu_raiz.codigo)
            #Nombre
            print(cu_raiz.nombre)
            #Creditos
            print(cu_raiz.creditos)
            #Prerequisitos
            print(cu_raiz.prerequisitos)
            #Obligatorio
            print(cu_raiz.obligatorio)
            #Función recursiva para mostrar todos los nodos derechos
            self.inOrden(cu_raiz.derecha)
    
    #metodo que buscar la matriz dispersa a graficar
    def buscar(self, cu_raiz, carnet, año, mes):
        if cu_raiz is not None:
            self.buscar(cu_raiz.izquierda, carnet, año, mes)
            if str(cu_raiz.carnet) == str(carnet):
                #print(cu_raiz.carnet)
                cu_raiz.años.buscar(año, mes) #buscar año
                return cu_raiz
            self.buscar(cu_raiz.derecha, carnet, año, mes)



    def verAltura(self, nodo):
        if nodo:
            return nodo.altura
        else:
            return -1

    def RI(self, nodo): #Rotación por la izquierda
        aux = nodo.izquierda
        nodo.izquierda = aux.derecha
        aux.derecha = nodo
        nodo.altura = self.datoMayor(self.verAltura(nodo.derecha),
                               self.verAltura(nodo.izquierda)) + 1
        aux.altura = self.datoMayor(nodo.altura, self.verAltura(nodo.izquierda)) + 1
        return aux

    def RD(self, nodo): #Rotación por la derecha
        aux = nodo.derecha
        nodo.derecha = aux.izquierda
        aux.izquierda = nodo
        nodo.altura = self.datoMayor(self.verAltura(nodo.derecha),
                               self.verAltura(nodo.izquierda)) + 1
        aux.altura = self.datoMayor(nodo.altura, self.verAltura(nodo.derecha)) + 1
        return aux

    def RID(self, nodo): #Rotación izquierda-derecha
        nodo.izquierda = self.RD(nodo.izquierda)
        aux = self.RI(nodo)
        return aux

    def RDI(self, nodo): #Rotación derecha-izquierda
        nodo.derecha = self.RI(nodo.derecha)
        aux = self.RD(nodo)
        return aux


    def graficar(self):
        d = Digraph('arbolavl', filename='C:\\Users\\rodri\\Desktop\\Reportes_F3\\CursosAsignados.gv',
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
                estudiante += str(cu_nodo.codigo) + "\n" + \
                    str(cu_nodo.nombre) + "\n" + str(cu_nodo.creditos)
                d.node(str(cu_nodo.codigo), label=estudiante)
                if cu_nodo.izquierda is not None:
                    d.edge(str(cu_nodo.codigo), str(cu_nodo.izquierda.codigo))
                if cu_nodo.derecha is not None:
                    d.edge(str(cu_nodo.codigo), str(cu_nodo.derecha.codigo))
                cu_nodo = cu_nodo.derecha
            else:
                break
        d.view()