from estructuras.TablaHash.nodoHash import NodoHash
import os


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

    def insertar(self, carnet, titulo, contenido):
        posicion = self.metodoDivision(int(carnet))
        if self.porcentajeUso() <= 0.50:
            if str(self.lista_hash[posicion].carnet) == str(carnet):
                self.lista_hash[posicion].id_apunte += 1
                self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)
            elif self.lista_hash[posicion].carnet == '':
                nuevo_nodo = NodoHash(carnet)
                self.lista_hash[posicion] = nuevo_nodo
                self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)
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
                            self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)
                        elif self.lista_hash[posicion].carnet == '':
                            nuevo_nodo = NodoHash(carnet)
                            self.lista_hash[posicion] = nuevo_nodo
                            self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)
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
                self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)
            elif self.lista_hash[posicion].carnet == '':
                nuevo_nodo = NodoHash(carnet)
                self.lista_hash[posicion] = nuevo_nodo
                self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)
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
                            self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)

                        elif self.lista_hash[posicion].carnet == '':
                            nuevo_nodo = NodoHash(carnet)
                            self.lista_hash[posicion] = nuevo_nodo
                            self.lista_hash[posicion].apuntes.insertar(self.lista_hash[posicion].id_apunte, titulo, contenido)
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


    def obtenerApuntes(self, carnet):
        self.data = {"data": []}
        for i in range(self.tamaño_lista_hash):
            if self.lista_hash[i].apuntes.contador > 0:
                for j in range(self.lista_hash[i].apuntes.contador):
                    if str(self.lista_hash[i].carnet) == str(carnet):
                        self.data['data'].append({"id": self.lista_hash[i].apuntes.obtenerId(j), "titulo": self.lista_hash[i].apuntes.obtenerTitulo(j),
                                                  "contenido": self.lista_hash[i].apuntes.obtenerContenido(j)})

        return self.data

    def obtenerApunte(self, carnet, id):
        for i in range(self.tamaño_lista_hash):
            if self.lista_hash[i].apuntes.contador > 0:
                for j in range(self.lista_hash[i].apuntes.contador):
                    print(f'carnet: {self.lista_hash[i].carnet} = {carnet} | id: {self.lista_hash[i].apuntes.obtenerId(j)} = {id}')
                    if str(self.lista_hash[i].carnet) == str(carnet) and str(self.lista_hash[i].apuntes.obtenerId(j)) == str(id):
                        
                        return {"titulo": self.lista_hash[i].apuntes.obtenerTitulo(j), "contenido": self.lista_hash[i].apuntes.obtenerContenido(j)}

    
    def obtenerTabla(self):
        for i in range(self.tamaño_lista_hash):
            if (str(self.lista_hash[i].carnet) != str('')):
                print(f'{i}) {self.lista_hash[i].carnet} - Apuntes: {self.lista_hash[i].apuntes.obtenerListaApuntes()}')
            else:
                print(f'{i})  -   -   -')

    def graficar(self):
        f = open("C:\\Users\\rodri\\OneDrive\\Documents\\GitHub\\EDD_SmartClass_201902781\\Fase 3\\frontend\\src\\pages\\TablaHash\\TablaHash.dot", "w")

        f.write("digraph structs {\n rankdir=LR node[shape=record]; \n")

        f.write("struct1 [label=\"")
        for i in range(self.tamaño_lista_hash):
            if i == self.tamaño_lista_hash - 1:
                f.write(f'<f{i}> {str(self.lista_hash[i].carnet)}')
            else:
                f.write(f'<f{i}> {str(self.lista_hash[i].carnet)}|')
        f.write("\"];")

        for i in range(self.tamaño_lista_hash):
            for j in range(self.lista_hash[i].apuntes.contador):
                f.write(f'n{i}{j} [shape=ellipse, label=\"{str(self.lista_hash[i].apuntes.obtenerTitulo(j))}\"] \n')
                if self.lista_hash[i].apuntes.obtenerId(j) == 0:
                    f.write(f'struct1:f{i} -> n{i}{0} \n')
                else:
                    f.write(f'n{i}{j-1} -> n{i}{j} \n')

        f.write("\n}")

        f.close()
        os.system(f"dot -Nfontname=Arial -Tpng \"C:\\Users\\rodri\\OneDrive\\Documents\\GitHub\\EDD_SmartClass_201902781\\Fase 3\\frontend\\src\\pages\\TablaHash\\TablaHash.dot\" -o \"C:\\Users\\rodri\\OneDrive\\Documents\\GitHub\\EDD_SmartClass_201902781\\Fase 3\\frontend\\src\\pages\\TablaHash\\TablaHash.png\"")