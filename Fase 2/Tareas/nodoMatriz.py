from Tareas.listaTareas import ListaTareas


class NodoMatriz:
    def __init__(self, dia=None, hora=None, cantidad_tareas=None, arriba=None, abajo=None, izquierda=None, derecha=None):
        self.dia = dia
        self.hora = hora
        self.cantidad_tareas = cantidad_tareas
        self.tareas = ListaTareas()
        self.arriba = arriba
        self.abajo = abajo
        self.izquierda = izquierda
        self.derecha = derecha


class NodoCabecera:
    def __init__(self, tipo=None, indice=None, siguiente=None, derecha=None, abajo=None):
        self.tipo = tipo
        self.indice = indice
        self.siguiente = siguiente
        self.derecha = derecha
        self.abajo = abajo


class NodoRaiz:
    def __init__(self):
        self.NodoFilas = None
        self.NodoColumnas = None
