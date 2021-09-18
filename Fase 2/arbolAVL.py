from nodoAVL import NodoAVL

class AVL:

    def __init__(self):
        self.raiz = None
        self.tamaño = 0

    def insertar(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad, años):
        nodo = NodoAVL(carnet, DPI, nombre, carrera, correo, password, creditos, edad, años)
        if self.raiz is None:
            self.raiz = nodo
            self.raiz.altura = 0
            self.tamaño = 1
        else:
            nodo_padre = None
            nodo_actual = self.raiz

            while True:
                if nodo_actual is not None:

                    nodo_padre = nodo_actual

                    if nodo.carnet < nodo_actual.carnet:
                        nodo_actual = nodo_actual.izquierda
                    else:
                        nodo_actual = nodo_actual.derecha
                else:
                    nodo.altura = nodo_padre.altura
                    nodo_padre.altura += 1
                    if nodo.carnet < nodo_padre.carnet:
                        nodo_padre.izquierda = nodo
                    else:
                        nodo_padre.derecha = nodo
                    self.equilibrar(nodo)
                    self.tamaño += 1
                    break

    def equilibrar(self, nodo):
        n = nodo

        while n is not None:
            altura_derecha = n.altura
            altura_izquierda = n.altura

            if n.derecha is not None:
                altura_derecha = n.derecha.altura

            if n.izquierda is not None:
                altura_izquierda = n.izquierda.altura

            if abs(altura_izquierda - altura_derecha) > 1:
                if altura_izquierda > altura_derecha:
                    hijo_izquierdo = n.izquierda
                    if hijo_izquierdo is not None:
                        a_derecha = (hijo_izquierdo.derecha.altura
                                    if (hijo_izquierdo.derecha is not None) else 0)
                        a_izquierda = (hijo_izquierdo.izquierda.altura
                                    if (hijo_izquierdo.izquierda is not None) else 0)
                    if (a_izquierda > a_derecha):
                        self.rotacion_izquierda(n)
                        break
                    else:
                        self.rotacion_doble_derecha(n)
                        break
                else:
                    hijo_derecho = n.derecha
                    if hijo_derecho is not None:
                        a_derecha = (hijo_derecho.derecha.altura
                            if (hijo_derecho.derecha is not None) else 0)
                        a_izquierda = (hijo_derecho.izquierda.altura
                            if (hijo_derecho.izquierda is not None) else 0)
                    if (a_izquierda > a_derecha):
                        self.rotacion_doble_izquierda(n)
                        break
                    else:
                        self.rotacion_derecha(n)
                        break
            n = n.hijo

    def rotacion_izquierda(self, nodo):
        carnet = nodo.hijo.carnet
        DPI = nodo.hijo.DPI
        nombre = nodo.hijo.nombre
        carrera = nodo.hijo.carrera
        correo = nodo.hijo.correo
        password = nodo.hijo.password
        creditos = nodo.hijo.creditos
        edad = nodo.hijo.edad
        años = nodo.hijo.años

        nodo.hijo.carnet = nodo.carnet
        nodo.hijo.DPI = nodo.DPI
        nodo.hijo.nombre = nodo.nombre
        nodo.hijo.carrera = nodo.carrera
        nodo.hijo.correo = nodo.correo
        nodo.hijo.password = nodo.password
        nodo.hijo.creditos = nodo.creditos
        nodo.hijo.edad = nodo.edad
        nodo.hijo.años = nodo.años

        nodo.hijo.derecha = NodoAVL(carnet, DPI, nombre, carrera, correo, password, creditos, edad, años)
        nodo.hijo.derecha.altura = nodo.hijo.altura + 1
        nodo.hijo.izquierda = nodo.derecha


    def rotacion_derecha(self, nodo):
        carnet = nodo.hijo.carnet
        DPI = nodo.hijo.DPI
        nombre = nodo.hijo.nombre
        carrera = nodo.hijo.carrera
        correo = nodo.hijo.correo
        password = nodo.hijo.password
        creditos = nodo.hijo.creditos
        edad = nodo.hijo.edad
        años = nodo.hijo.años

        nodo.hijo.carnet = nodo.carnet
        nodo.hijo.DPI = nodo.DPI
        nodo.hijo.nombre = nodo.nombre
        nodo.hijo.carrera = nodo.carrera
        nodo.hijo.correo = nodo.correo
        nodo.hijo.password = nodo.password
        nodo.hijo.creditos = nodo.creditos
        nodo.hijo.edad = nodo.edad
        nodo.hijo.años = nodo.años

        nodo.hijo.izquierda = NodoAVL(carnet, DPI, nombre, carrera, correo, password, creditos, edad, años)
        nodo.hijo.izquierda.altura = nodo.hijo.altura + 1
        nodo.hijo.derecha = nodo.derecha

    def rotacion_doble_izquierda(self, nodo):
        self.rotacion_derecha(nodo.getDerecha().getDerecha())
        self.rotacion_izquierda(nodo)

    def rotacion_doble_derecha(self, nodo):
        self.rotacion_izquierda(nodo.getIzquierda().getIzquierda())
        self.rotacion_derecha(nodo)

    def vacio(self):
        if self.raiz is None:
            return True
        return False

    def mostrar(self, nodo_actual):
        if nodo_actual is not None:
            self.mostrar(nodo_actual.izquierda)
            print(nodo_actual.carnet, end=" ")
            self.mostrar(nodo_actual.derecha)

    def preorder(self, nodo_actual):
        if nodo_actual is not None:
            self.mostrar(nodo_actual.izquierda)
            self.mostrar(nodo_actual.derecha)
            print(nodo_actual.carnet, end=" ")

    def getRaiz(self):
        return self.raiz


""" t = AVL()
t.insertar(5, "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba")
t.insertar(9, "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba")
t.insertar(13, "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba")
t.insertar(10, "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba")
t.insertar(17, "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba")
t.mostrar(t.raiz) """