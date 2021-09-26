""" from nodo import Nodo
from listaDoble import ListaDoble

from Btree import BTree """

""" lista = ListaDoble()

lista.insert(Nodo(4, 3, 4))
lista.insert(Nodo(5, 3, 4))

print(lista[0])
print(lista[5]) """

"""
btree = BTree()
btree.insertarDatos("100", "Guatemala")
btree.insertarDatos("110", "Noruega")
btree.insertarDatos("120", "Alemania")
btree.insertarDatos("130", "Suiza")
btree.insertarDatos("140", "Francia")
btree.insertarDatos("150", "Japon")
btree.insertarDatos("160", "China")
btree.insertarDatos("170", "Singapour")
btree.insertarDatos("180", "Corea del Sur")
btree.insertarDatos("190", "Tailandia")
btree.insertarDatos("200", "Australia")
btree.insertarDatos("210", "Guatemala")
btree.insertarDatos("220", "Noruega")
btree.insertarDatos("230", "Alemania") """


from Analizadores.Sintactico import parser
from Analizadores.Sintactico import user_list, task_list, arbolAVL

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('Reporte.txt',"r", encoding="utf-8")
    mensaje = f.read()
    # print(mensaje)
    f.close()
    # parser.parse('¿ Elements ? ¿Element type = "task"?  ¿item Carnet = "201901425" $? ¿$Element? ¿ $Elements ?')
    parser.parse(mensaje)

    user_list.getList()
    print("------------------------")
    task_list.getList()
    print("------------------------")
    arbolAVL.inorden(arbolAVL.raiz)
    print("------------------------")

    


