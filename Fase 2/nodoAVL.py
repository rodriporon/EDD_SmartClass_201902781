from listaDoble import ListaDoble

class NodoAVL:
    def __init__(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad):
        self.carnet = carnet
        self.DPI = DPI
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.años = ListaDoble()
        self.izquierda = None
        self.derecha = None
        self.altura = 0