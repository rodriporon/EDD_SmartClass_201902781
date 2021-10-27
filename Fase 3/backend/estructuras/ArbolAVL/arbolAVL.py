from flask.globals import current_app
from estructuras.ArbolAVL.nodoAVL import NodoAVL
from cryptography.fernet import Fernet
from graphviz import Digraph

key = Fernet.generate_key()

f = Fernet(key)

user_login = None


class ArbolAVL:
    def __init__(self):

        self.raiz = None

    def insertar(self, carnet, DPI, nombre, carrera, correo, password, edad):

        carnet_encrypt = f.encrypt(carnet.encode())
        DPI_encrypt = f.encrypt(DPI.encode())
        nombre_encrypt = f.encrypt(nombre.encode())
        carrera_encrypt = f.encrypt(carrera.encode())
        correo_encrypt = f.encrypt(correo.encode())
        password_encrypt = f.encrypt(password.encode())
        edad_encrypt = f.encrypt(edad.encode())

        nuevo_nodo = NodoAVL(carnet_encrypt, DPI_encrypt, nombre_encrypt,
                             carrera_encrypt, correo_encrypt, password_encrypt, edad_encrypt)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return nuevo_nodo
        else:
            self.raiz = self._insertar(nuevo_nodo, self.raiz)
            return nuevo_nodo

    def _insertar(self, new_nodo, cu_raiz):
        if cu_raiz is not None:
            if str(f.decrypt(cu_raiz.carnet).decode()) > str(f.decrypt(new_nodo.carnet).decode()):
                cu_raiz.izquierda = self._insertar(
                    new_nodo, cu_raiz.izquierda)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == -2):
                    if (str(f.decrypt(new_nodo.carnet).decode()) < str(f.decrypt(cu_raiz.izquierda.carnet).decode())):
                        cu_raiz = self.RI(cu_raiz)
                    else:
                        cu_raiz = self.RID(cu_raiz)

            elif str(f.decrypt(cu_raiz.carnet).decode()) < str(f.decrypt(new_nodo.carnet).decode()):
                cu_raiz.derecha = self._insertar(
                    new_nodo, cu_raiz.derecha)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == 2):
                    if (str(f.decrypt(new_nodo.carnet).decode()) > str(f.decrypt(cu_raiz.derecha.carnet).decode())):
                        cu_raiz = self.RD(cu_raiz)
                    else:
                        cu_raiz = self.RDI(cu_raiz)

            cu_raiz.altura = self.datoMayor(self.verAltura(
                cu_raiz.derecha), self.verAltura(cu_raiz.izquierda)) + 1
            return cu_raiz
        else:
            cu_raiz = new_nodo
            return cu_raiz

    def datoMayor(self, a, b):
        if a > b:
            return a
        return b

    # Mostrar en recorrido inOrden la estructura del ArbolAVL
    def datosEncriptados(self, cu_raiz):
        if cu_raiz is not None:
            # Función recursiva para mostrar todos los nodos izquierdos
            self.datosEncriptados(cu_raiz.izquierda)
            print('-------------------------------------')
            # Carnet
            print(f.decrypt(cu_raiz.carnet).decode())
            print(type(f.decrypt(cu_raiz.carnet).decode()))
            # DPI
            print(f.decrypt(cu_raiz.DPI).decode())
            # Nombre
            print(f.decrypt(cu_raiz.nombre).decode())
            # Carrera
            print(f.decrypt(cu_raiz.carrera).decode())
            # Correo
            print(f.decrypt(cu_raiz.correo).decode())
            # Password
            print(f.decrypt(cu_raiz.password).decode())
            # Edad
            print(f.decrypt(cu_raiz.edad).decode())
            # Función recursiva para mostrar todos los nodos derechos
            self.datosEncriptados(cu_raiz.derecha)

    def datosDesencriptados(self, cu_raiz):
        if cu_raiz is not None:
            # Función recursiva para mostrar todos los nodos izquierdos
            self.datosDesencriptados(cu_raiz.izquierda)
            print('-------------------------------------')
            # Carnet
            print(f.decrypt(cu_raiz.carnet))
            # DPI
            print(cu_raiz.DPI)
            # Nombre
            print(cu_raiz.nombre)
            # Carrera
            print(cu_raiz.carrera)
            # Correo
            print(cu_raiz.correo)
            # Password
            print(cu_raiz.password)
            # Edad
            print(cu_raiz.edad)
            # Función recursiva para mostrar todos los nodos derechos
            self.datosDesencriptados(cu_raiz.derecha)

    def getMinValueNode(self, root):
        if root is None or root.izquierda is None:
            return root

        return self.getMinValueNode(root.izquierda)

    def buscar(self, cu_raiz, carnet, password):
        if cu_raiz is not None:
            self.buscar(cu_raiz.izquierda, carnet, password)
            if str(f.decrypt(cu_raiz.carnet).decode()) == str(carnet) and str(f.decrypt(cu_raiz.password).decode()) == str(password):
                global user_login
                print('ENCONTRADO')
                user_login = {
                    "carnet": f.decrypt(cu_raiz.carnet).decode(),
                    "DPI": f.decrypt(cu_raiz.DPI).decode(),
                    "nombre": f.decrypt(cu_raiz.nombre).decode(),
                    "carrera": f.decrypt(cu_raiz.carrera).decode(),
                    "correo": f.decrypt(cu_raiz.correo).decode(),
                    "password": f.decrypt(cu_raiz.password).decode(),
                    "edad": f.decrypt(cu_raiz.edad).decode()
                }
                return user_login
            self.buscar(cu_raiz.derecha, carnet, password)
        return user_login

    def verAltura(self, nodo):
        if nodo:
            return nodo.altura
        else:
            return -1

    def RI(self, nodo):  # Rotación por la izquierda
        aux = nodo.izquierda
        nodo.izquierda = aux.derecha
        aux.derecha = nodo
        nodo.altura = self.datoMayor(self.verAltura(nodo.derecha),
                                     self.verAltura(nodo.izquierda)) + 1
        aux.altura = self.datoMayor(
            nodo.altura, self.verAltura(nodo.izquierda)) + 1
        return aux

    def RD(self, nodo):  # Rotación por la derecha
        aux = nodo.derecha
        nodo.derecha = aux.izquierda
        aux.izquierda = nodo
        nodo.altura = self.datoMayor(self.verAltura(nodo.derecha),
                                     self.verAltura(nodo.izquierda)) + 1
        aux.altura = self.datoMayor(
            nodo.altura, self.verAltura(nodo.derecha)) + 1
        return aux

    def RID(self, nodo):  # Rotación izquierda-derecha
        nodo.izquierda = self.RD(nodo.izquierda)
        aux = self.RI(nodo)
        return aux

    def RDI(self, nodo):  # Rotación derecha-izquierda
        nodo.derecha = self.RI(nodo.derecha)
        aux = self.RD(nodo)
        return aux

    def graficar(self):
        d = Digraph('arbolavl', filename='C:\\Users\\rodri\\Desktop\\Reportes_F3\\ArbolAVL.gv',
                    node_attr={'shape': 'box'})
        cu_nodo = self.raiz
        pila = []
        d.attr(rankdir='TB')
        while True:
            if cu_nodo is not None:
                pila.append(cu_nodo)
                cu_nodo = cu_nodo.izquierda
            elif pila:
                cu_nodo = pila.pop()
                estudiante = ""
                estudiante += str(cu_nodo.carnet) + "\n" + \
                    str(cu_nodo.nombre) + "\n" + cu_nodo.carrera
                d.node(str(cu_nodo.carnet), label=estudiante)
                if cu_nodo.izquierda is not None:
                    d.edge(str(cu_nodo.carnet), str(cu_nodo.izquierda.carnet))
                if cu_nodo.derecha is not None:
                    d.edge(str(cu_nodo.carnet), str(cu_nodo.derecha.carnet))
                cu_nodo = cu_nodo.derecha
            else:
                break
        d.view()