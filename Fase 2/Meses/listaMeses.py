from Meses.nodoMeses import NodoMeses

class ListaMeses:
    def __init__(self):
        self.nodo_inicial = None

    def existe(self, mes):
        if self.nodo_inicial is None:
            return False
        else:
            aux = self.nodo_inicial
            while aux is not None:
                if (str(mes) == str(aux.valor)):
                    return True
                aux = aux.siguiente
        return False

    def insertar(self, valor):
        nuevo_nodo = NodoMeses(valor)
        if self.nodo_inicial is None:
            self.nodo_inicial = nuevo_nodo
            return nuevo_nodo
        else:
            aux = self.nodo_inicial
            while aux.siguiente is not None:
                aux = aux.siguiente
            if not self.existe(valor):
                nuevo_nodo = NodoMeses(valor)
                aux.siguiente = nuevo_nodo
                nuevo_nodo.anterior = aux
                return nuevo_nodo
            return nuevo_nodo

    def mostrarMeses(self):
        if self.nodo_inicial is None:
            print("      "+'Empty list')
        else:
            aux = self.nodo_inicial
            while aux is not None:
                print("             "+str(aux.valor), " ")
                #Acá se recorre la matriz dispersa
                aux.matriz_dispersa.mostrar()
                aux = aux.siguiente

    #método que busca la matriz a graficar
    def buscar(self, mes):
        #print('entró al buscar de listaMeses')
        if self.nodo_inicial is not None:
            aux = self.nodo_inicial
            while aux is not None:
                if str(aux.valor) == str(mes):
                    #METODO QUE GRAFICA LA MATRIZ DISPERSA
                    aux.matriz_dispersa.graficar(aux.matriz_dispersa)
                    aux.matriz_dispersa.mostrar()
                aux = aux.siguiente

    def graficarListaTareas(self, mes, dia, hora):
        #print('entró al graficar de listaMeses')
        if self.nodo_inicial is not None:
            aux = self.nodo_inicial
            while aux is not None:
                if str(aux.valor) == str(mes):
                    #print('entró al if de comparar')
                    #aux.matriz_dispersa.recorrer(aux.matriz_dispersa)
                    aux.matriz_dispersa.graficarListaTareas(dia, hora)
                aux = aux.siguiente

    def insertar_matriz_meses(self, carnet, nombre, descripcion, materia, fecha, hora, estado, mes, dia, hora_aux):
        #print('entró al buscar de listaMeses')
        if self.nodo_inicial is not None:
            aux = self.nodo_inicial
            while aux is not None:
                if str(aux.valor) == str(mes):
                    #aux.matriz_dispersa.recorrer(aux.matriz_dispersa)
                    nodo_matriz_dispersa = aux.matriz_dispersa.insertar(dia, hora_aux, 1, carnet, nombre, descripcion, materia, fecha, hora, estado)
                    nodo_matriz_dispersa.tareas.insertar(carnet, nombre, descripcion, materia, fecha, hora, estado)
                    
                aux = aux.siguiente