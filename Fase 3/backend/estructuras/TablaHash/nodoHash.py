from estructuras.TablaHash.ListaApuntes import ListaApuntes

class NodoHash:
    def __init__(self, carnet):
        self.carnet = carnet
        self.apuntes = ListaApuntes()
        self.id_apunte = 0
        self.siguiente = None
        self.anterior = None