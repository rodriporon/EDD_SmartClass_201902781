class Nodo:
    def __init__(self, valor=None, semestre=None, mes=None, anterior=None, siguiente=None):
        self.valor = valor
        self.semestre = semestre
        self.mes = mes
        self.anterior = anterior
        self.siguiente = siguiente

    def __str__(self) -> str:
        resultado = str(self.valor)
        return resultado