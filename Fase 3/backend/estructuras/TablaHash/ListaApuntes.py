from estructuras.TablaHash.nodoApuntes import NodoApuntes

class ListaApuntes:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.contador = 0

    def obtenerTamaño(self):
        aux = self.primero
        contador = 0
        while aux is not None:
            contador += 1
            aux = aux.siguiente

        return contador

    def isEmpty(self):
        return self.primero is None

    def obtenerListaApuntes(self):
        cadena = ''
        aux = self.primero
        while aux is not None:
            cadena += f'{aux.id} - {aux.titulo} - {aux.contenido} | '
            aux = aux.siguiente
        return cadena

    def obtenerId(self, i):
        if (i >= self.contador):
            return None
        aux = self.primero
        n = 0
        while aux is not None:
            if (n == i):
                return aux.id
            aux = aux.siguiente
            n += 1

    def obtenerTitulo(self, i):
        if (i >= self.contador):
            return None
        aux = self.primero
        n = 0
        while aux is not None:
            if (n == i):
                return aux.titulo
            aux = aux.siguiente
            n += 1

    def obtenerContenido(self, i):
        if (i >= self.contador):
            return None
        aux = self.primero
        n = 0
        while aux is not None:
            if (n == i):
                return aux.contenido
            aux = aux.siguiente
            n += 1
        

    def insertar(self, id, titulo, contenido):
        nuevo_nodo = NodoApuntes(id, titulo, contenido)

        if self.isEmpty():
            self.ultimo = nuevo_nodo
            self.primero = self.ultimo
            self.contador += 1
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
            self.contador += 1