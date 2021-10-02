from Tareas.nodoTareas import NodoTareas

class ListaTareas:

    def __init__(self):
        self.cabeza = None

    def insertar(self, carnet, nombre, descripcion, materia, fecha, hora, estado):
        if self.cabeza is None:
            nuevo_nodo = NodoTareas(carnet, nombre, descripcion, materia, fecha, hora, estado)
            self.cabeza = nuevo_nodo
            return nuevo_nodo
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux = aux.siguiente
            nuevo_nodo = NodoTareas(carnet, nombre, descripcion, materia, fecha, hora, estado)
            aux.siguiente = nuevo_nodo
            return nuevo_nodo

    def recorrer(self):
        if self.cabeza is None:
            print("      "+'Empty list')
        else:
            aux = self.cabeza
            while aux is not None:
                print("                          "+str(aux.carnet), " ")
                aux = aux.siguiente