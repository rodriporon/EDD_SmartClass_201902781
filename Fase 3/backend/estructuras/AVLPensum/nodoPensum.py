class NodoPensum:
    def __init__(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio
        self.derecha = None
        self.izquierda = None
        self.altura = 0