import os

class NodoTareas:
    def __init__(self, carnet, nombre, descripcion, materia, fecha, hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.siguiente = None

    

class ListaTareas:

    def __init__(self):
        self.cabeza = None
        self.cola = None

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
            self.cola = nuevo_nodo
            return nuevo_nodo

    def recorrer(self):
        if self.cabeza is None:
            print("      "+'Empty list')
        else:
            aux = self.cabeza
            while aux is not None:
                print("                          "+str(aux.nombre), " ")
                aux = aux.siguiente

    def graficarListaTareas(self):
        archivo = open("C:\\Users\\rodri\\Desktop\\Reportes_F2\\Grafica_Lista_Tareas.dot", "w")
        archivo.write("Digraph G {\nrankdir=LR;\n")
        aux = self.cabeza
        contador = 0

        while aux.siguiente is not None:
            aux_carnet = aux.carnet.replace("\"", "")
            aux_nombre = aux.nombre.replace("\"", "")

            archivo.write("\"Node" + str(contador) + "\" -> \"Node" + str(contador + 1) + "\" [constrain=false]; \n")
            archivo.write("\n \t \"Node" + str(contador) + "\"[shape=box, style=filled, color=skyblue, label=\" Carnet: " + str(aux_carnet) + "\n" + "Nombre: " + str(aux_nombre) + "\"]\n")

            contador += 1
            aux = aux.siguiente
        aux_carnet = aux.carnet.replace("\"", "")
        aux_nombre = aux.nombre.replace("\"", "")

        #archivo.write("\"Node" + str(contador) + "\" -> \"Node" + str(0) + "\" [constrain=false]; \n")
        archivo.write("\n \t \"Node" + str(contador) + "\"[shape=box, style=filled, color=skyblue, label=\" Carnet: " + str(aux_carnet) + "\n" + "Nombre: " + str(aux_nombre) + "\"]\n")
        archivo.write("}")
        archivo.close()
        os.system("dot -Tpng C:\\Users\\rodri\\Desktop\\Reportes_F2\\Grafica_Lista_Tareas.dot -o C:\\Users\\rodri\\Desktop\\Reportes_F2\\Grafica_Lista_Tareas.png")

l = ListaTareas()
l.insertar('201902781', 'Rodrigo', 'Hacer tarea', 'Orga', '34234', '4234', 'Incumplida')
""" l.insertar('234234', 'Rodrigoo', 'Hacer tarea', 'Orga', '34234', '4234', 'Incumplida')
l.insertar('234234244', 'Rodrigooo', 'Hacer tarea', 'Orga', '34234', '4234', 'Incumplida')
l.insertar('2019234234202781', 'Rodrigooo', 'Hacer tarea', 'Orga', '34234', '4234', 'Incumplida') """

l.graficarListaTareas()