from typing import Sized
import graphviz

from estructuras.ListaPensum.nodoListaPensum import NodoListaPensum

class ListaPensum:
    def __init__(self):
        self.cabeza = None
        self.dict_prerequisitos = {}

    def insertar(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        nuevo_nodo = NodoListaPensum(codigo, nombre, creditos, prerequisitos, obligatorio)
        if self.cabeza:
            ultimo_nodo = self.cabeza
            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente

            ultimo_nodo.siguiente = nuevo_nodo

        else:
            self.cabeza = nuevo_nodo

    def buscar(self, codigo):
        aux = self.cabeza

        while aux != None:
            if str(aux.codigo) == str(codigo):
                return aux
            aux = aux.siguiente

    def buscarCurso(self, codigo):
        aux = self.cabeza
        while aux != None:
            if str(aux.codigo) == str(codigo):
                return aux
                
            aux = aux.siguiente
        return False

    def imprimir(self):
        aux = self.cabeza
        while aux != None:
            print(f'codigo: {aux.codigo}')
            aux = aux.siguiente

    def obtenerListaAdyacencia(self, codigo):
        lista_adyacencia = []
        nodo_curso = self.buscarCurso(codigo)
        lista_adyacencia.append(nodo_curso)
        for i in lista_adyacencia:
            prerequisitos = i.prerequisitos
            if prerequisitos != '':
                lista_prerequisitos = prerequisitos.split(',')
                for j in lista_prerequisitos:
                    nodo_curso = self.buscarCurso(j)
                    if nodo_curso:
                        if nodo_curso not in lista_adyacencia:
                            lista_adyacencia.append(nodo_curso)
        return lista_adyacencia

    def graficarPrerequisitos(self, codigo):
        lista_adyacencia = self.obtenerListaAdyacencia(codigo)
        f = graphviz.Digraph('grafo_cursos_prerequisitos', filename='C:\\Users\\rodri\\Desktop\\Reportes_F3\\GrafoCursosPrerequisitos.gv')
        f.attr(rankdir='LR', size='5')
        
        for i in lista_adyacencia:
            cadena = i.codigo+"--"+ i.nombre
            f.node(cadena)
            prerequisitos = i.prerequisitos
            lista_prerequisitos = prerequisitos.split(',')
            for prerequisito in lista_prerequisitos:
                for nodo in lista_adyacencia:
                    aux = nodo.codigo
                    if prerequisito == aux:
                        textoB = aux+"--"+nodo.nombre
                        f.edge(cadena,textoB,label=str(nodo.creditos))
        f.view()
            


