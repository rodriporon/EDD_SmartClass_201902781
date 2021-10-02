#Aquí va la dispersa
from Tareas.matrizTareas import Matriz

class NodoMeses:
    def __init__(self, valor):
        self.valor = valor
        self.matriz_dispersa = Matriz()
        self.siguiente = None
        self.anterior = None 