from estructuras.TablaHash.nodoHash import NodoHash
from estructuras.TablaHash.nodoApunte import NodoApunte


class TablaHash:
    def __init__(self):
        self.tamaño_lista_hash = 7
        self.lista_hash = [None, None, None, None, None, None, None]
        self.colisiones = 0
        self.bucle_exploracion = 0
        self.data = {"data": []}

        for i in range(self.tamaño_lista_hash):
            nuevo_nodo = NodoHash('')
            self.lista_hash[i] = nuevo_nodo

    def obtenerTabla(self):
        cadena = ''
        for i in range(self.tamaño_lista_hash):
            cadena += f'{i}) {self.lista_hash[i].carnet}'
            if len(self.lista_hash[i].apuntes) > 0:
                for j in range(len(self.lista_hash[i].apuntes)):
                    cadena += f' id: {self.lista_hash[i].apuntes[j].id} - {self.lista_hash[i].apuntes[j].titulo} '
                cadena += '\n'
            else:
                cadena += '\n'
        return print(cadena)

    def insertar(self, carnet, titulo, contenido):
        posicion = self.metodoDivision(int(carnet))
        if self.porcentajeUso() <= 0.50:
            if str(self.lista_hash[posicion].carnet) == str(carnet):
                self.lista_hash[posicion].id_apunte += 1
                nodo_apunte = NodoApunte(
                    self.lista_hash[posicion].id_apunte, titulo, contenido)
                self.lista_hash[posicion].apuntes.append(nodo_apunte)
            elif self.lista_hash[posicion].carnet == '':
                nuevo_nodo = NodoHash(carnet)
                nodo_apunte = NodoApunte(
                    self.lista_hash[posicion].id_apunte, titulo, contenido)
                self.lista_hash[posicion] = nuevo_nodo
                self.lista_hash[posicion].apuntes.append(nodo_apunte)
            else:
                while True:
                    self.bucle_exploracion += 1
                    if posicion < self.tamaño_lista_hash - 1:
                        # Cambiar por metodo de exploración cuadrática
                        self.colisiones += 1
                        posicion = posicion + (self.colisiones*self.colisiones)
                        print(posicion)
                    if posicion < self.tamaño_lista_hash - 1:
                        if str(self.lista_hash[posicion].carnet) == str(carnet):
                            self.lista_hash[posicion].id_apunte += 1
                            nodo_apunte = NodoApunte(
                                self.lista_hash[posicion].id_apunte, titulo, contenido)
                            self.lista_hash[posicion].apuntes.append(nodo_apunte)
                        elif self.lista_hash[posicion].carnet == '':
                            nuevo_nodo = NodoHash(carnet)
                            nodo_apunte = NodoApunte(
                                self.lista_hash[posicion].id_apunte, titulo, contenido)
                            self.lista_hash[posicion] = nuevo_nodo
                            self.lista_hash[posicion].apuntes.append(nodo_apunte)
                            break
                    else:
                        posicion = 0
                        self.colisiones = 0
                    if self.bucle_exploracion >= self.tamaño_lista_hash:
                        posicion = posicion + 1
        else:
            if self.esPrimo(self.tamaño_lista_hash):
                primo_proximo = self.esPrimo(self.tamaño_lista_hash+1)
            for i in range(primo_proximo - self.tamaño_lista_hash):
                nuevo_nodo = NodoHash('')
                self.lista_hash.append(nuevo_nodo)

            self.tamaño_lista_hash = primo_proximo
            if str(self.lista_hash[posicion].carnet) == str(carnet):
                self.lista_hash[posicion].id_apunte += 1
                nodo_apunte = NodoApunte(
                    self.lista_hash[posicion].id_apunte, titulo, contenido)
                self.lista_hash[posicion].apuntes.append(nodo_apunte)
            elif self.lista_hash[posicion].carnet == '':
                nuevo_nodo = NodoHash(carnet)
                nodo_apunte = NodoApunte(
                    self.lista_hash[posicion].id_apunte, titulo, contenido)
                self.lista_hash[posicion] = nuevo_nodo
                self.lista_hash[posicion].apuntes.append(nodo_apunte)
            else:
                while True:
                    self.bucle_exploracion += 1
                    if posicion < self.tamaño_lista_hash:
                        # Cambiar por metodo de exploración cuadrática
                        self.colisiones += 1
                        posicion = posicion + (self.colisiones*self.colisiones)

                    if posicion < self.tamaño_lista_hash:
                        if str(self.lista_hash[posicion].carnet) == str(carnet):
                            self.lista_hash[posicion].id_apunte += 1
                            nodo_apunte = NodoApunte(
                            self.lista_hash[posicion].id_apunte, titulo, contenido)
                            self.lista_hash[posicion].apuntes.append(nodo_apunte)

                        elif self.lista_hash[posicion].carnet == '':
                            nuevo_nodo = NodoHash(carnet)
                            nodo_apunte = NodoApunte(
                                self.lista_hash[posicion].id_apunte, titulo, contenido)
                            self.lista_hash[posicion] = nuevo_nodo
                            self.lista_hash[posicion].apuntes.append(nodo_apunte)
                            break
                    else:
                        self.colisiones = 0
                        posicion = 0
                    if self.bucle_exploracion >= self.tamaño_lista_hash:
                        posicion = posicion + 1

    def metodoDivision(self, carnet):
        return carnet % self.tamaño_lista_hash

    def esPrimo(self, num):
        if num == 1:
            return 2
        for n in range(2, num):
            if num % n == 0:
                return self.esPrimo(num+1)
        return num

    def porcentajeUso(self):
        contador = 0
        for i in range(self.tamaño_lista_hash):
            if self.lista_hash[i].carnet != '':
                contador += 1

        return contador/self.tamaño_lista_hash

    def insertarApunte(self, carnet, titulo, contenido):
        for i in range(self.tamaño_lista_hash):
            if str(self.lista_hash[i].carnet) == str(carnet):
                self.lista_hash[i].id_apunte += 1
                nodo_apunte = NodoApunte(
                    self.lista_hash[i].id_apunte, titulo, contenido)
                self.lista_hash[i].apuntes.append(nodo_apunte)
            else:
                pass

    def obtenerApuntes(self, carnet):
        self.data = {"data": []}
        for i in range(self.tamaño_lista_hash):
            if len(self.lista_hash[i].apuntes) > 0:
                for j in range(len(self.lista_hash[i].apuntes)):
                    if str(self.lista_hash[i].carnet) == str(carnet):
                        self.data['data'].append({"id": self.lista_hash[i].apuntes[j].id, "titulo": self.lista_hash[i].apuntes[j].titulo,
                                                  "contenido": self.lista_hash[i].apuntes[j].contenido})

        return self.data

    def obtenerApunte(self, carnet, id):
        for i in range(self.tamaño_lista_hash):
            if len(self.lista_hash[i].apuntes) > 0:
                for j in range(len(self.lista_hash[i].apuntes)):
                    print(f'carnet: {self.lista_hash[i].carnet} = {carnet} | id: {self.lista_hash[i].apuntes[j].id} = {id}')
                    if str(self.lista_hash[i].carnet) == str(carnet) and str(self.lista_hash[i].apuntes[j].id) == str(id):
                        
                        return {"titulo": self.lista_hash[i].apuntes[j].titulo, "contenido": self.lista_hash[i].apuntes[j].contenido}
