from nodoAVL import NodoAVL

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertarAño(self, carnet, raiz):
        if raiz is not None:
            if str(raiz.carnet) == str(carnet):
                aux_años = raiz.carnet[1:4]
                año = int(aux_años)
                for i in range(año, 2021):
                    raiz.años.insertar(i)

            

    def insertar(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad):
        self.raiz = self._insertar(carnet, DPI, nombre, carrera, correo, password, creditos, edad, self.raiz)


    def _insertar(self, carnet, DPI, nombre, carrera, correo, password, creditos, edad, aux):
        if aux is None:
            return NodoAVL(carnet, DPI, nombre, carrera, correo, password, creditos, edad)

        elif carnet > aux.carnet:
            aux.derecha = self._insertar(carnet, DPI, nombre, carrera, correo, password, creditos, edad, aux.derecha)
            if (self.verAltura(aux.derecha)-self.verAltura(aux.izquierda) == 2):
                if carnet > aux.derecha.carnet:
                    aux = self.SRR(aux)
                else:
                    aux = self.DRR(aux)
        else:
            aux.izquierda = self._insertar(carnet, DPI, nombre, carrera, correo, password, creditos, edad, aux.izquierda)
            if (self.verAltura(aux.izquierda)-self.verAltura(aux.derecha) == 2):
                if carnet < aux.izquierda.carnet:
                    aux = self.SRL(aux)
                else:
                    aux = self.DRL(aux)
        
        a_derecha = self.verAltura(aux.derecha)
        a_izquierda = self.verAltura(aux.izquierda)
        a_mayor = self.mayor(a_derecha, a_izquierda)
        aux.altura = a_mayor + 1

        return aux

    def mayor(self, a_d, a_i):
        if a_d > a_i:
            return a_d
        return a_i

    def verAltura(self, aux):
        if aux is None:
            return -1
        else:
            return aux.altura

    def SRL(self, nodo_1):
        nodo_2 = nodo_1.izquierda
        nodo_1.izquierda = nodo_2.derecha
        nodo_2.derecha = nodo_1
        a_nodo1_i = self.verAltura(nodo_1.izquierda)
        a_nodo1_d = self.verAltura(nodo_1.derecha)
        a_nodo2_i = self.verAltura(nodo_2.izquierda)
        nodo_1.altura = self.mayor(a_nodo1_i, a_nodo1_d) + 1
        nodo_2.altura = self.mayor(a_nodo2_i, nodo_1.altura) + 1
        return nodo_2

    def SRR(self, nodo_1):
        nodo_2 = nodo_1.derecha
        nodo_1.derecha = nodo_2.izquierda
        nodo_2.izquierda = nodo_1
        a_nodo1_i = self.verAltura(nodo_1.izquierda)
        a_nodo1_d = self.verAltura(nodo_1.derecha)
        a_nodo2_i = self.verAltura(nodo_2.izquierda)
        nodo_1.altura = self.mayor(a_nodo1_i, a_nodo1_d) + 1
        nodo_2.altura = self.mayor(a_nodo2_i, nodo_1.altura) + 1
        return nodo_2

    def DRL(self, aux):
        aux.izquierda = self.SRR(aux.izquierda)
        return self.SRL(aux)
    
    def DRR(self, aux):
        aux.derecha = self.SRL(aux.derecha)
        return self.SRR(aux)

    def preOrden(self):
        self._preOrden(self.raiz)

    
    def _preOrden(self, aux):
        if aux is not None:
            print(aux.carnet, end= ' ')
            print(aux.años.recorrer(), end=' ')
            self._preOrden(aux.izquierda)
            self._preOrden(aux.derecha)


""" arbolAVL = ArbolAVL()
arbolAVL.insertar(5, 34, 234, 234, 234, 234, 234, 234, 234)
arbolAVL.insertar(10, 34, 234, 234, 234, 234, 234, 234, 234)
arbolAVL.insertar(20, 34, 234, 234, 234, 234, 234, 234, 234)
arbolAVL.insertar(25, 34, 234, 234, 234, 234, 234, 234, 234)
arbolAVL.insertar(30, 34, 234, 234, 234, 234, 234, 234, 234)
arbolAVL.insertar(35, 34, 234, 234, 234, 234, 234, 234, 234)
arbolAVL.insertar(50, 34, 234, 234, 234, 234, 234, 234, 234)

arbolAVL.preOrden() """