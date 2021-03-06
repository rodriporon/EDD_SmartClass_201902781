from estructuras.ArbolAVL.nodoAVL import NodoAVL
from estructuras.SHA256.sha256 import generarHash
from cryptography.fernet import Fernet
from graphviz import Digraph



class ArbolAVL:
    def __init__(self):

        self.raiz = None
        self.user_cursos = None
        self.user_login = None
        self.f = None
        self.key = None

    def generarKey(self):
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)

    def insertar(self, carnet, DPI, nombre, carrera, correo, password, edad):

        carnet_encrypt = self.f.encrypt(carnet.encode())
        DPI_encrypt = self.f.encrypt(DPI.encode())
        nombre_encrypt = self.f.encrypt(nombre.encode())
        carrera_encrypt = self.f.encrypt(carrera.encode())
        correo_encrypt = self.f.encrypt(correo.encode())

        #Proceso de generacion de Hash para password
        password_sha256 = generarHash(password.encode())
        password_encrypt = self.f.encrypt(password_sha256.encode())

        edad_encrypt = self.f.encrypt(edad.encode())

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
            if str(self.f.decrypt(cu_raiz.carnet).decode()) > str(self.f.decrypt(new_nodo.carnet).decode()):
                cu_raiz.izquierda = self._insertar(
                    new_nodo, cu_raiz.izquierda)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == -2):
                    if (str(self.f.decrypt(new_nodo.carnet).decode()) < str(self.f.decrypt(cu_raiz.izquierda.carnet).decode())):
                        cu_raiz = self.RI(cu_raiz)
                    else:
                        cu_raiz = self.RID(cu_raiz)

            elif str(self.f.decrypt(cu_raiz.carnet).decode()) < str(self.f.decrypt(new_nodo.carnet).decode()):
                cu_raiz.derecha = self._insertar(
                    new_nodo, cu_raiz.derecha)
                if (self.verAltura(cu_raiz.derecha)-self.verAltura(cu_raiz.izquierda) == 2):
                    if (str(self.f.decrypt(new_nodo.carnet).decode()) > str(self.f.decrypt(cu_raiz.derecha.carnet).decode())):
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
            # Funci??n recursiva para mostrar todos los nodos izquierdos
            self.datosEncriptados(cu_raiz.izquierda)
            print('-------------------------------------')
            # Carnet
            print(self.f.decrypt(cu_raiz.carnet).decode())
            # DPI
            print(self.f.decrypt(cu_raiz.DPI).decode())
            # Nombre
            print(self.f.decrypt(cu_raiz.nombre).decode())
            # Carrera
            print(self.f.decrypt(cu_raiz.carrera).decode())
            # Correo
            print(self.f.decrypt(cu_raiz.correo).decode())
            # Password
            print(self.f.decrypt(cu_raiz.password).decode())
            # Edad
            print(self.f.decrypt(cu_raiz.edad).decode())
            # Funci??n recursiva para mostrar todos los nodos derechos
            self.datosEncriptados(cu_raiz.derecha)

    def datosDesencriptados(self, cu_raiz):
        if cu_raiz is not None:
            # Funci??n recursiva para mostrar todos los nodos izquierdos
            self.datosDesencriptados(cu_raiz.izquierda)
            print('-------------------------------------')
            # Carnet
            print(self.f.decrypt(cu_raiz.carnet))
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
            # Funci??n recursiva para mostrar todos los nodos derechos
            self.datosDesencriptados(cu_raiz.derecha)

    def getMinValueNode(self, root):
        if root is None or root.izquierda is None:
            return root

        return self.getMinValueNode(root.izquierda)

    def buscar(self, cu_raiz, carnet, password):
        if cu_raiz is not None:
            self.buscar(cu_raiz.izquierda, carnet, password)
            if str(self.f.decrypt(cu_raiz.carnet).decode()) == str(carnet) and str(self.f.decrypt(cu_raiz.password).decode()) == str(password):
                global user_login
                print('ENCONTRADO')
                self.user_login = {
                    "carnet": self.f.decrypt(cu_raiz.carnet).decode(),
                    "DPI": self.f.decrypt(cu_raiz.DPI).decode(),
                    "nombre": self.f.decrypt(cu_raiz.nombre).decode(),
                    "carrera": self.f.decrypt(cu_raiz.carrera).decode(),
                    "correo": self.f.decrypt(cu_raiz.correo).decode(),
                    "password": self.f.decrypt(cu_raiz.password).decode(),
                    "edad": self.f.decrypt(cu_raiz.edad).decode()
                }
                return self.user_login
            self.buscar(cu_raiz.derecha, carnet, password)
        return self.user_login

    def buscarEstudiante(self, cu_raiz, carnet):
        if cu_raiz is not None:
            self.buscarEstudiante(cu_raiz.izquierda, carnet)
            if str(self.f.decrypt(cu_raiz.carnet).decode()) == str(carnet):
                global user_cursos
                print('ENCONTRADO')
                self.user_cursos = cu_raiz
                return self.user_cursos
            self.buscarEstudiante(cu_raiz.derecha, carnet)
        return self.user_cursos

    def verAltura(self, nodo):
        if nodo:
            return nodo.altura
        else:
            return -1

    def RI(self, nodo):  # Rotaci??n por la izquierda
        aux = nodo.izquierda
        nodo.izquierda = aux.derecha
        aux.derecha = nodo
        nodo.altura = self.datoMayor(self.verAltura(nodo.derecha),
                                     self.verAltura(nodo.izquierda)) + 1
        aux.altura = self.datoMayor(
            nodo.altura, self.verAltura(nodo.izquierda)) + 1
        return aux

    def RD(self, nodo):  # Rotaci??n por la derecha
        aux = nodo.derecha
        nodo.derecha = aux.izquierda
        aux.izquierda = nodo
        nodo.altura = self.datoMayor(self.verAltura(nodo.derecha),
                                     self.verAltura(nodo.izquierda)) + 1
        aux.altura = self.datoMayor(
            nodo.altura, self.verAltura(nodo.derecha)) + 1
        return aux

    def RID(self, nodo):  # Rotaci??n izquierda-derecha
        nodo.izquierda = self.RD(nodo.izquierda)
        aux = self.RI(nodo)
        return aux

    def RDI(self, nodo):  # Rotaci??n derecha-izquierda
        nodo.derecha = self.RI(nodo.derecha)
        aux = self.RD(nodo)
        return aux

    def graficarDesencriptado(self):
        d = Digraph('arbolavl', filename='C:\\Users\\rodri\\Desktop\\Reportes_F3\\ArbolAVLDesencriptado.gv',
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
                estudiante += f'carnet: {str(self.f.decrypt(cu_nodo.carnet).decode())}' + "\n" + \
                    f'nombre: {str(self.f.decrypt(cu_nodo.nombre).decode())}' + "\n" + f'password: {str(self.f.decrypt(cu_nodo.password).decode())}' + "\n" + f'correo: {str(self.f.decrypt(cu_nodo.correo).decode())}'
                d.node(str(self.f.decrypt(cu_nodo.carnet).decode()), label=estudiante)
                if cu_nodo.izquierda is not None:
                    d.edge(str(self.f.decrypt(cu_nodo.carnet).decode()), str(self.f.decrypt(cu_nodo.izquierda.carnet).decode()))
                if cu_nodo.derecha is not None:
                    d.edge(str(self.f.decrypt(cu_nodo.carnet).decode()), str(self.f.decrypt(cu_nodo.derecha.carnet).decode()))
                cu_nodo = cu_nodo.derecha
            else:
                break
        d.view()

    def graficarEncriptado(self):
        d = Digraph('arbolavl', filename='C:\\Users\\rodri\\Desktop\\Reportes_F3\\ArbolAVLEncriptado.gv',
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
                estudiante += f'carnet: {str(cu_nodo.carnet.decode())}' + "\n" + \
                    f'nombre: {str(cu_nodo.nombre.decode())}' + "\n" + f'password: {str(cu_nodo.password.decode())}' + "\n" + f'correo: {str(cu_nodo.correo.decode())}'
                d.node(str(cu_nodo.carnet.decode()), label=estudiante)
                if cu_nodo.izquierda is not None:
                    d.edge(str(cu_nodo.carnet.decode()), str(cu_nodo.izquierda.carnet.decode()))
                if cu_nodo.derecha is not None:
                    d.edge(str(cu_nodo.carnet.decode()), str(cu_nodo.derecha.carnet.decode()))
                cu_nodo = cu_nodo.derecha
            else:
                break
        d.view()
