from Tareas.nodoMatriz import NodoMatriz, NodoCabecera, NodoRaiz


class Matriz:
    def __init__(self):
        self.NodoRaiz = None

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
            while(current.derecha is not None and current.derecha.dia < nodo.x):
                current = current.derecha
            nodo.derecha = current.derecha
            current.derecha = nodo

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

    def insertar(self, dia, hora, cantidad_tareas):
        #print('entró a insertar')
        nodoN = NodoMatriz(dia=dia, hora=hora, cantidad_tareas=cantidad_tareas)
        if self.NodoRaiz is None:
            self.NodoRaiz = NodoRaiz()
            self.NodoRaiz.NodoColumnas = NodoCabecera(tipo="Columna", indice=dia)
            self.NodoRaiz.NodoFilas = NodoCabecera(tipo="Fila", indice=hora)
            self.NodoRaiz.NodoColumnas.siguiente = None
            self.NodoRaiz.NodoFilas.siguiente = None
            self.NodoRaiz.NodoColumnas.abajo = nodoN
            self.NodoRaiz.NodoFilas.derecha = nodoN
            return nodoN
        else:
            print('entró a else')
            Nodotemporal = self.NodoRaiz
            if self.existe(dia, hora) is False:
                self.insertar_cabercera(Nodotemporal.NodoFilas, hora, "Fila")
                Nodotemporal = self.NodoRaiz
                self.insertar_cabercera(Nodotemporal.NodoColumnas, dia, "Columna")
                self.insertar_nodo_fila(nodo=nodoN)
                self.insertar_nodo_col(nodo=nodoN)
                return nodoN
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

    def existe(self, dia, hora):
        print('entró a existe')
        nodo = self.NodoRaiz.NodoFilas
        while(nodo is not None):
            nodo_temp = nodo.derecha
            while(nodo_temp is not None):
                if nodo_temp.dia == dia and nodo_temp.hora == hora:
                    nodo_temp.cantidad_tareas += 1
                    print('entró a true')
                    return True
                nodo_temp = nodo_temp.derecha
            nodo = nodo.siguiente
        print('entró a false')
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

    def graficar(self, nueva_matriz):
        grafo = "digraph"
        grafo+=str("{\nnode[shape=record];\n")
        grafo+=str("graph[pencolor=transparent];\n")
        grafo+=str("node [style=filled];\n")
        nodo = nueva_matriz.NodoRaiz.NodoFilas

        for y in range(1, 11):
            nodo_temp = nodo.derecha
            for x in range(1, 11):
                if(nueva_matriz.buscar(x,y)):
                    grafo+=str("p"+str(x)+str(y)+"[label=\"{<data>"+str(x)+","+str(y)+"|<next>}\" pos=\""+str(x)+","+str(10-y)+"!\"];\n")
                    if(nodo_temp.derecha!=None): 
                        nodo_2=nodo_temp
                        nodo_temp=nodo_temp.derecha
                        grafo+=str("p"+str(nodo_2.dia)+str(nodo_2.hora)+"->"+"p"+str(nodo_temp.dia)+str(nodo_temp.hora)+"[dir=both];\n")
                else:
                    pass
                if nodo.siguiente!=None:
                    if nodo.siguiente.indice==y+1:
                        nodo=nodo.siguiente    
        nodo = nueva_matriz.NodoRaiz.NodoColumnas
        for x in range(1, 11):
            nodo_temp = nodo.abajo
            for y in range(1, 11):
                if(nueva_matriz.buscar(x,y)):
                    if(nodo_temp.abajo!=None):
                        nodo_2=nodo_temp
                        nodo_temp=nodo_temp.abajo
                        grafo+=str("p"+str(nodo_2.dia)+str(nodo_2.hora)+"->"+"p"+str(nodo_temp.dia)+str(nodo_temp.hora)+"[dir=both];\n")
                else:
                    pass
                if nodo.siguiente!=None:
                    if nodo.siguiente.indice==x+1:
                        nodo=nodo.siguiente         
        grafo+=str("}\n")
        f= open("ejemplo.dot","w+")
        f.write(grafo)
        f.close() 
        print("********* Se realizo Grafica *********  ")