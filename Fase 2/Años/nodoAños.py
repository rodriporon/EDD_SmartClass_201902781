from Meses.listaMeses import ListaMeses

class NodoAños:
    def __init__(self, valor):
        self.valor = valor
        self.meses = ListaMeses()
        self.siguiente = None
        self.anterior = None 