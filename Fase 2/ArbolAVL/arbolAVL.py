from ArbolAVL.nodoAVL import NodoAVL
from graphviz import Digraph

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    #metodos del arbol
    def insertar(self,carnet,DPI,nombre,carrera,correo,password,creditos,edad):
        nuevo = NodoAVL(carnet,DPI,nombre,carrera,correo,password,creditos,edad)
        if self.raiz == None:
            self.raiz = nuevo
            return nuevo
        else:
            self.raiz = self.nodo_insertar(nuevo,self.raiz)
            return nuevo

    def nodo_insertar(self,nuevo,raiz_actual):
        if raiz_actual:
            if raiz_actual.carnet > nuevo.carnet:
                raiz_actual.izquierda = self.nodo_insertar(nuevo,raiz_actual.izquierda)
                #validar si necesita rotacion
                if (self.altura(raiz_actual.derecha)-self.altura(raiz_actual.izquierda)== -2):
                    if nuevo.carnet < raiz_actual.izquierda.carnet:
                        raiz_actual = self.R_izquierda(raiz_actual)
                    else:
                        raiz_actual = self.R_izquierda_derecha(raiz_actual)

            elif raiz_actual.carnet < nuevo.carnet:
                raiz_actual.derecha = self.nodo_insertar(nuevo,raiz_actual.derecha)
                #validar si necesita rotacion
                if (self.altura(raiz_actual.derecha)-self.altura(raiz_actual.izquierda)== 2):
                    if nuevo.carnet > raiz_actual.derecha.carnet:
                        raiz_actual = self.R_derecha(raiz_actual)
                    else:
                        raiz_actual = self.R_derecha_izquierda(raiz_actual)

            #calcular nueva altura
            raiz_actual.altura = self.max(self.altura(raiz_actual.derecha),self.altura(raiz_actual.izquierda)) + 1
            return raiz_actual
        else:
            raiz_actual = nuevo
            return raiz_actual

    #Concatenar la lista años a los estudiantes
    def insert_años(self,raiz_actual, carnet, año):
        if raiz_actual:
            if str(raiz_actual.carnet) == str(carnet):
                raiz_actual.años.insertar(año)

    def inorden(self,raiz_actual):
        if raiz_actual:
            self.inorden(raiz_actual.izquierda)
            print(raiz_actual.carnet)
            print(raiz_actual.DPI)
            print(raiz_actual.nombre)
            print(raiz_actual.correo)
            print(raiz_actual.password)
            print(raiz_actual.creditos)
            print(raiz_actual.edad)
            print("... List años")
            print(raiz_actual.años.MostrarAños())
            print(".....................................")
            
            self.inorden(raiz_actual.derecha)

    #metodos para alturas
    def max(self, v1, v2):
        if v1> v2:
            return v1
        else:
            return v2

    def altura(self, nodo):
        if nodo:
            return nodo.altura
        else:
            return -1


    #ROTACIONES
    #SIMPLE izquierda 
    def R_izquierda(self, nodo):
        aux = nodo.izquierda
        nodo.izquierda = aux.derecha
        aux.derecha = nodo
        nodo.altura = self.max(self.altura(nodo.derecha), self.altura(nodo.izquierda)) +1
        aux.altura = self.max(nodo.altura, self.altura(nodo.izquierda)) +1
        return aux

    #SIMPLE derecha
    def R_derecha(self, nodo):
        aux = nodo.derecha
        nodo.derecha = aux.izquierda
        aux.izquierda = nodo
        nodo.altura = self.max(self.altura(nodo.derecha), self.altura(nodo.izquierda)) +1
        aux.altura = self.max(nodo.altura, self.altura(nodo.derecha)) +1
        return aux

    #izquierda-derecha
    def R_izquierda_derecha(self, nodo):
        nodo.izquierda = self.R_derecha(nodo.izquierda)
        aux = self.R_izquierda(nodo)
        return aux

    #derecha-izquierda
    def R_derecha_izquierda(self, nodo):
        nodo.derecha = self.R_izquierda(nodo.derecha)
        aux = self.R_derecha(nodo)
        return aux

    def graficar(self):
        cadena = "digraph arbol {\n"
        if(self.raiz != None):
            cadena += self.listar(self.raiz)
            cadena += "\n"
            cadena += self.enlazar(self.raiz)
        cadena += "}"
        Archivo = open("ejemplo.dot","w+")
        Archivo.write(cadena)
        Archivo.close()

    def listar(self, raiz_actual):
        if raiz_actual:
            cadena = "n"+str(raiz_actual.cadena)+"[label= \""+str(raiz_actual.carnet)+"\"];\n"
            cadena += self.listar(raiz_actual.izquierda)
            cadena += self.listar(raiz_actual.derecha)
            return cadena
        else:
            return ""
    
    def enlazar(self,raiz_actual):
        cadena =""
        if raiz_actual:
            if raiz_actual.izquierda:
                cadena+= "n"+str(raiz_actual.carnet)+" -> n"+str(raiz_actual.izquierda.carnet)+"\n"
            if raiz_actual.derecha:
                cadena+= "n"+str(raiz_actual.carnet)+" -> n"+str(raiz_actual.derecha.carnet)+"\n"

            cadena += self.enlazar(raiz_actual.izquierda)
            cadena += self.enlazar(raiz_actual.derecha)
        
        return cadena
    
    def graph(self):
        s = Digraph('structs', filename='tree.gv', node_attr={'shape': 'record'})
        current = self.raiz
        stack = []  # initialize stack
        done = 0
        s.attr(rankdir='TB')
        while True:
            if current is not None:
                stack.append(current)
                current = current.izquierda
            elif stack:
                current = stack.pop()
                user = ""
                user += str(current.carnet) + "\n" + str(current.DPI) + "\n" + current.nombre
                s.node(str(current.carnet), label=user)
                if current.izquierda is not None:
                    s.edge(str(current.carnet), str(current.izquierda.carnet))
                if current.derecha is not None:
                    s.edge(str(current.carnet), str(current.derecha.carnet))
                current = current.derecha
            else:
                break
        s.view()