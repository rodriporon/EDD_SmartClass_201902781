from estructuras.TablaHash.nodoApunte import NodoApunte

class NodoHash:
    def __init__(self, carnet):
        self.carnet = carnet
        self.apuntes = []
        self.siguiente = None
        self.anterior = None