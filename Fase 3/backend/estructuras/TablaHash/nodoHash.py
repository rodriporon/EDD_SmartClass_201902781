from estructuras.TablaHash.nodoApunte import NodoApunte

class NodoHash:
    def __init__(self, carnet):
        self.carnet = carnet
        self.apuntes = []
        self.id_apunte = 0
        self.siguiente = None
        self.anterior = None