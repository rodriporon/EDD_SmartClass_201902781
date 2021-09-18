from paginaB import PaginaB


def compareTo(a, b):
    if (a < b):
        return -1
    elif (a == b):
        return 0
    elif (a > b):
        return 1


class BTree:

    raiz = None #Posible error, puede que sea raiz = PaginaB()
    codigo = ""
    pais = ""
    auxiliar_1 = False
    auxiliar_2 = PaginaB()
    subeArriba = False
    estado = False
    comparador = False
    nodos = 0

    def isEmpty(self, raiz):
        return (raiz == None or raiz.getCuenta() == 0)

    def insertarDatos(self, codigo, pais):
        self.insertarDatos2(self.raiz, codigo, pais)

    def insertarDatos2(self, raiz, codigo, pais):
        self.empujar(raiz, codigo, pais)
        if (self.subeArriba):
            self.raiz = PaginaB()
            self.raiz.setCuenta(1)
            self.raiz.setCodigo(0, self.codigo)
            self.raiz.setPais(0, self.pais)
            self.raiz.setApuntador(0, raiz)
            self.raiz.setApuntador(1, self.auxiliar_2)

    def empujar(self, raiz, codigo, pais):
        posicion = 0
        self.estado = False

        if (self.isEmpty(raiz) and self.comparador == False):
            self.subeArriba = True
            self.codigo = codigo
            self.pais = pais
            self.auxiliar_2 = None

        else:
            posicion = self.buscarNodoB(codigo, raiz)
            if (self.comparador == False):
                if (self.estado):
                    self.subeArriba = False
                else:
                    self.empujar(raiz.getApuntador(posicion), codigo, pais)
                    if (self.subeArriba):
                        if(raiz.getCuenta() < 4):
                            self.subeArriba = False
                            self.meterHoja(
                                raiz, posicion, self.codigo, self.pais)
                        else:
                            self.subeArriba = True
                            self.dividirPaginaB(
                                raiz, posicion, self.codigo, self.pais)
            else:
                print(f'Dato repetido: {codigo}')
                self.comparador = False

    def buscarNodoB(self, codigo, raiz):
        auxContador = 0
        if (compareTo(codigo, raiz.getCodigo(0)) < 0):
            self.estado = False
            auxContador = 0
        else:
            while (auxContador != raiz.getCuenta()):
                if (codigo == raiz.getCodigo(auxContador)):
                    self.comparador = True
                auxContador += 1
            auxContador = raiz.getCuenta()

            while (compareTo(codigo, raiz.getCodigo(auxContador - 1)) < 0 and auxContador > 1):
                auxContador -= 1 #Posible error, realmente es --auxContador
                if (codigo == raiz.getCodigo(auxContador - 1)):
                    self.estado = True
                else:
                    self.estado = False

        return auxContador

    def meterHoja(self, raiz, posicion, codigo, pais):
        auxC = raiz.getCuenta()

        while (auxC != posicion):
            if (auxC != 0):
                raiz.setCodigo(auxC, raiz.getCodigo(auxC - 1))
                raiz.setPais(auxC, raiz.getPais(auxC - 1))
                raiz.setApuntador(auxC + 1, raiz.getApuntador(auxC))
            auxC -= 1

        raiz.setCodigo(posicion, codigo)
        raiz.setPais(posicion, pais)
        raiz.setApuntador(posicion + 1, self.auxiliar_2)
        raiz.setCuenta(raiz.getCuenta() + 1)

    def dividirPaginaB(self, raiz, posicion, codigo, pais):
        posicion_2 = 0
        posicion_media = 0

        if (posicion <= 2):
            posicion_media = 2
        else:
            posicion_media = 3
        
        pagina_derecha = PaginaB()
        posicion_2 = posicion_media + 1

        while (posicion_2 != 5):
            if ((posicion_2 - posicion_media) != 0):
                pagina_derecha.setCodigo((posicion_2 - posicion_media) - 1, raiz.getCodigo(posicion_2 - 1))
                pagina_derecha.setPais((posicion_2 - posicion_media) - 1, raiz.getPais(posicion_2 - 1))
                pagina_derecha.setApuntador(posicion_2 - posicion_media, raiz.getApuntador(posicion_2))

            posicion_2 += 1
        
        pagina_derecha.setCuenta(4 - posicion_media)
        raiz.setCuenta(posicion_media)

        if (posicion <= 2):
            self.auxiliar_1 = True
            self.meterHoja(raiz, posicion, codigo, pais)
        else:
            self.auxiliar_1 = True
            self.meterHoja(pagina_derecha, (posicion - posicion_media), codigo, pais)

        self.codigo = raiz.getCodigo(raiz.getCuenta() - 1)
        self.pais = raiz.getPais(raiz.getCuenta() - 1)

        pagina_derecha.setApuntador(0, raiz.getApuntador(raiz.getCuenta()))

        raiz.setCuenta(raiz.getCuenta() - 1)
        self.auxiliar_2 = pagina_derecha

        if (self.auxiliar_1):
            raiz.setCodigo(3, "")
            raiz.setPais(3, "")
            raiz.setApuntador(4, None)

            raiz.setCodigo(2, "")
            raiz.setPais(2, "")
            raiz.setApuntador(3, None)

    def preOrden(self):
        self.preOrden2(self.raiz)

    def preOrden2(self, pagina):
        if (pagina != None):

            for i in range(pagina.getCuenta()):
                if (pagina.getCodigo(i) != None):
                    if (pagina.getCodigo(i) != ""):
                        print(f'{pagina.getCodigo(i)}_')

            print("")

            self.preOrden2(pagina.getApuntador(0))
            self.preOrden2(pagina.getApuntador(1))
            self.preOrden2(pagina.getApuntador(2))
            self.preOrden2(pagina.getApuntador(3))
            self.preOrden2(pagina.getApuntador(4))
