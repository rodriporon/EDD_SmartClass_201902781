class NodoAVL:
    def __init__(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad, años):
        self.carnet = carnet
        self.DPI = DPI
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.años = años
        self._hijo = None
        self._izquierda = None
        self._derecha = None
        self.altura = 0

    @property
    def derecha(self):
        return self._derecha

    @derecha.setter
    def derecha(self, nodo):
        if nodo is not None:
            nodo._hijo = self
            self._derecha = nodo

    @property
    def izquierda(self):
        return self._izquierda

    @izquierda.setter
    def izquierda(self, nodo):
        if nodo is not None:
            nodo._hijo = self
            self._izquierda = nodo

    @property
    def hijo(self):
        return self._hijo

    @hijo.setter
    def hijo(self, nodo):
        if nodo is not None:
            self._hijo = nodo
            self.altura = self.hijo.altura + 1
        else:
            self.altura = 0