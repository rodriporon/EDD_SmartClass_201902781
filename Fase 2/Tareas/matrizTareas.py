from Tareas.nodoMatriz import NodoMatriz, NodoCabecera, NodoRaiz


class Matriz:
    def __init__(self):
        self.NodoRaiz = None

    #Se insertan nodos de tipo fila
    def insertar_nodo_fila(self, nodo):
        temporalfila = self.NodoRaiz.NodoFilas
        while(temporalfila.indice != nodo.hora):
            temporalfila = temporalfila.siguiente
        if temporalfila.derecha is None:
            nodo.derecha = temporalfila.derecha
            temporalfila.derecha = nodo
        elif temporalfila.derecha.dia >= nodo.dia:
            nodo.derecha = temporalfila.derecha
            temporalfila.derecha = nodo
        else:
            current = temporalfila.derecha
            while(current.derecha is not None and current.derecha.dia < nodo.dia):
                current = current.derecha
            nodo.derecha = current.derecha
            current.derecha = nodo

    #Se insertan nodos tipo columna
    def insertar_nodo_col(self, nodo):
        temporalcol = self.NodoRaiz.NodoColumnas
        while(temporalcol.indice != nodo.dia):
            temporalcol = temporalcol.siguiente
        if temporalcol.abajo is None:
            nodo.abajo = temporalcol.abajo
            temporalcol.abajo = nodo
        elif temporalcol.abajo.hora >= nodo.hora:
            nodo.abajo = temporalcol.abajo
            temporalcol.abajo = nodo
        else:
            current = temporalcol.abajo
            while(current.abajo is not None and current.abajo.hora < nodo.hora):
                current = current.abajo
            nodo.abajo = current.abajo
            current.abajo = nodo

    def insertar_cabercera(self, nodo, indice, tipo):
        temporalfila = nodo
        if temporalfila.indice > indice:
            nuevaCabecera = NodoCabecera(tipo=tipo, indice=indice)
            nuevaCabecera.siguiente = self.NodoRaiz.NodoFilas
            self.NodoRaiz.NodoFilas = nuevaCabecera
        else:
            current = temporalfila
            while(current.siguiente is not None and current.siguiente.indice <= indice):
                current = current.siguiente
            if current.indice != indice:
                nuevaCabecera = NodoCabecera(tipo=tipo, indice=indice)
                nuevaCabecera.siguiente = current.siguiente
                current.siguiente = nuevaCabecera

    def insertar(self, dia, hora_aux, cantidad_tareas, carnet, nombre, descripcion, materia, fecha, hora, estado):
        #print('entró a insertar')
        nodoN = NodoMatriz(dia=dia, hora=hora_aux, cantidad_tareas=cantidad_tareas)
        if self.NodoRaiz is None:
            self.NodoRaiz = NodoRaiz()
            self.NodoRaiz.NodoColumnas = NodoCabecera(tipo="Columna", indice=dia)
            self.NodoRaiz.NodoFilas = NodoCabecera(tipo="Fila", indice=hora_aux)
            self.NodoRaiz.NodoColumnas.siguiente = None
            self.NodoRaiz.NodoFilas.siguiente = None
            self.NodoRaiz.NodoColumnas.abajo = nodoN
            self.NodoRaiz.NodoFilas.derecha = nodoN
            return nodoN
        else:
            #print('entró a else')
            Nodotemporal = self.NodoRaiz
            if self.existe(dia, hora_aux, carnet, nombre, descripcion, materia, fecha, hora, estado) is False:
                self.insertar_cabercera(Nodotemporal.NodoFilas, hora_aux, "Fila")
                Nodotemporal = self.NodoRaiz
                self.insertar_cabercera(Nodotemporal.NodoColumnas, dia, "Columna")
                self.insertar_nodo_fila(nodo=nodoN)
                self.insertar_nodo_col(nodo=nodoN)
            return nodoN

    def buscar(self, dia, hora):
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                if nodo_temp.dia == dia and nodo_temp.hora == hora:
                    return True
                nodo_temp = nodo_temp.derecha
            nodo = nodo.siguiente
        return False

    def existe(self, dia, hora_aux, carnet, nombre, descripcion, materia, fecha, hora, estado):
        #print('entró a existe')
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                if str(nodo_temp.dia) == str(dia) and str(nodo_temp.hora) == str(hora_aux):
                    nodo_temp.cantidad_tareas += 1
                    nodo_temp.tareas.insertar(carnet, nombre, descripcion, materia, fecha, hora, estado)
                    #print('entró a true')
                    return True
                nodo_temp = nodo_temp.derecha
            nodo = nodo.siguiente
        #print('entró a false')
        return False

    def mostrar(self):
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                print("                 x:  "+str(nodo_temp.dia)+ ", y:  "+str(nodo_temp.hora) +", "  + str(nodo_temp.cantidad_tareas))
                nodo_temp.tareas.recorrer()
                nodo_temp=nodo_temp.derecha
            nodo=nodo.siguiente

    def graficarListaTareas(self, dia, hora):
        #print("entró a la matriz de tareas")
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                if str(nodo_temp.dia) == str(dia) and str(nodo_temp.hora) == str(hora):
                    print("                 dia:  "+str(nodo_temp.dia)+ ", hora:  "+str(nodo_temp.hora) +", cantidad tareas: "  + str(nodo_temp.cantidad_tareas))
                    nodo_temp.tareas.graficarListaTareas()
                    nodo_temp.tareas.recorrer()
                nodo_temp=nodo_temp.derecha
            nodo=nodo.siguiente

    #Método para graficar la matriz dispersa
    def graficar(self, nueva_matriz):
        pass