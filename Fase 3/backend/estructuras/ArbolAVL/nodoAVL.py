class NodoAVL:
    def __init__(self, carnet, DPI, nombre, carrera, correo, password, edad):
        self.carnet = carnet
        self.DPI = DPI
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.edad = edad
        self.izquierda = None
        self.derecha = None
        self.altura = 0