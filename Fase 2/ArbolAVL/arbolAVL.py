from ArbolAVL.nodoAVL import NodoAVL
from graphviz import Digraph


class ArbolAVL:
    def __init__(self):

        self.raiz = None

    def insertar(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad):
        nuevo_nodo = NodoAVL(carnet, DPI, nombre, carrera,
                        correo, password, creditos, edad)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return nuevo_nodo
        else:
            self.raiz = self._insertar(nuevo_nodo, self.raiz)
            return nuevo_nodo

    def _insertar(self, new_nodo, cu_raiz):
        if cu_raiz is not None:
            if cu_raiz.carnet > new_nodo.carnet:
                cu_raiz.izquierda = self._insertar(
                    new_nodo, cu_raiz.izquierda)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == -2):
                    if (new_nodo.carnet < cu_raiz.izquierda.carnet):
                        cu_raiz = self.RI(cu_raiz)
                    else:
                        cu_raiz = self.RID(cu_raiz)

            elif cu_raiz.carnet < new_nodo.carnet:
                cu_raiz.derecha = self._insertar(
                    new_nodo, cu_raiz.derecha)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == 2):
                    if new_nodo.carnet > cu_raiz.derecha.carnet:
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

    def inOrden(self, cu_raiz):
        if cu_raiz is not None:
            self.inOrden(cu_raiz.izquierda)
            print(cu_raiz.carnet)
            print(cu_raiz.DPI)
            print(cu_raiz.nombre)
            print(cu_raiz.correo)
            print(cu_raiz.password)
            print(cu_raiz.creditos)
            print(cu_raiz.edad)
            print("---------- Listas Años --------------")
            print(cu_raiz.años.showAños())
            print("-------------------------------------")

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

    def graficarListaTareas(self, cu_raiz, carnet, año, mes, dia, hora):
        #print('entró a graficar de arbolAVL')
        if cu_raiz is not None:
            self.graficarListaTareas(cu_raiz.izquierda, carnet, año, mes, dia, hora)
            if str(cu_raiz.carnet) == str(carnet):
                #print(cu_raiz.carnet)
                cu_raiz.años.graficarListaTareas(año, mes, dia, hora) #buscar año
                return cu_raiz
            self.graficarListaTareas(cu_raiz.derecha, carnet, año, mes, dia, hora)

    def insertar_matriz(self, cu_raiz, carnet, nombre, descripcion, materia, fecha, hora, estado, año, mes, dia, hora_aux):
        if cu_raiz is not None:
            self.insertar_matriz(cu_raiz.izquierda, carnet, nombre, descripcion, materia, fecha, hora, estado, año, mes, dia, hora_aux)
            if str(cu_raiz.carnet) == str(carnet):
                cu_raiz.años.insertar_matriz_años(carnet, nombre, descripcion, materia, fecha, hora, estado, año, mes, dia, hora_aux)                
                return cu_raiz
            self.insertar_matriz(cu_raiz.derecha, carnet, nombre, descripcion, materia, fecha, hora, estado, año, mes, dia, hora_aux)

    def modificarEstudiante(self, cu_raiz, carnet, DPI, nombre, carrera, correo, password, creditos, edad):
        if cu_raiz is not None:
            self.modificarEstudiante(cu_raiz.izquierda, carnet, DPI, nombre, carrera, correo, password, creditos, edad)
            if str(cu_raiz.carnet) == str(carnet):
                cu_raiz.carnet = carnet
                cu_raiz.DPI = DPI
                cu_raiz.nombre = nombre
                cu_raiz.carrera = carrera
                cu_raiz.password = password
                cu_raiz.creditos = creditos
                cu_raiz.edad = edad
            self.modificarEstudiante(cu_raiz.derecha, carnet, DPI, nombre, carrera, correo, password, creditos, edad)

    def obtenerEstudiante(self, cu_raiz, carnet):
        if cu_raiz is not None:
            self.obtenerEstudiante(cu_raiz.izquierda, carnet)
            if str(cu_raiz.carnet) == str(carnet):
                print('------------------------------------')
                print(f'Los datos del carnet: {cu_raiz.carnet} son:')
                print(f'DPI: {cu_raiz.DPI}, nombre: {cu_raiz.nombre}, carrera: {cu_raiz.carrera}')
                print(f'correo: {cu_raiz.correo}, password: {cu_raiz.password}, creditos: {cu_raiz.creditos}, edad: {cu_raiz.edad}')
                print('------------------------------------')
            self.obtenerEstudiante(cu_raiz.derecha, carnet)
        



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
        d = Digraph('arbolavl', filename='C:\\Users\\rodri\\Desktop\\Reportes_F2\\ArbolAVL.gv',
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
