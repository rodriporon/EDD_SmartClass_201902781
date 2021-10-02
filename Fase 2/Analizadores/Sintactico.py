
from Analizadores.Lexico import tokens
from Estructuras.Lista import Lista
from Estructuras.Nodo import Nodo
from ArbolAVL.arbolAVL import ArbolAVL
from Tareas.matrizTareas import Matriz

# Lists for save the information about users and tasks
user_list = Lista()
task_list = Lista()
#Incersión de Estudiantes
arbolAVL = ArbolAVL()
#Matriz de Tareas
matriz_tareas = Matriz()

# This node allows to store information about one user or task
element_node = Nodo()

# dictionary of names
names = {}

def años():
    aux_años = element_node.Carnet[1:4]
    año = int(aux_años)
    for i in range(año, 2021):
        print(i)
        return i

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """
    # t[0] = t[1]
    # if len(t) == 2:
    #     t[0] = [t[1]]
    # else:
    #     t[0] = t[1]
    #     t[0].append(t[2])

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'
    global Matriz,Matriz2
    global Carnet
    if t[3] == "user":
        user_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              element_node.Creditos, element_node.Edad, element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, element_node.Hora, element_node.Estado)
        Matriz = arbolAVL.insertar(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Correo, element_node.Password, element_node.Creditos, element_node.Edad)
        #Año
        año = element_node.Carnet[0:4]
        a = int(año)
        for i in range(a,2022):
            Matriz2 = Matriz.años.insertar(i)
            
        Carnet = element_node.Carnet
    if t[3] == "task":

            #variable hora matriz dispersa
            hora = element_node.Hora
            #variable dia matriz dispersa
            dia = element_node.Fecha[0:2]

            CarnetT = element_node.Carnet
            Fecha = element_node.Fecha[3:5]
            
            #Auxiliares para fecha
            aux1 = element_node.Fecha[6:10]
            aux2= Carnet[0:4]
            fecha_mes = element_node.Fecha[3:5]

            #Conversión a enteros
            añoTarea = int(aux1)
            añoEstud = int(aux2)
            #Calcular el mes
            if (Carnet == CarnetT):
                for i in range(añoEstud,2022):
                    #Calcular la posicion
                    if i == añoTarea:
                        nodo_mes = Matriz2.meses.insertar(Fecha)
                        #print(f'el nodo mes es: {nodo_mes}')
                        #incersión matriz dispersa:
                        """ for x in range(12):
                            if x <= 9:
                                comparar_mes = '0'+str(x)
                            else:
                                comparar_mes = str(x)
                            #print(comparar_mes)
                            if str(comparar_mes) == str(fecha_mes):
                                print(f'dia: {dia}, hora: {hora}, en el mes: {nodo_mes.valor} y en el año: {i}') """
                        
                        
            
            #Aqui debería de ingresar las tareas a la dispersa y enlazarla con los meses
            """ task_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              element_node.Creditos, element_node.Edad, element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, element_node.Hora, element_node.Estado) """

    if t[3] == "task":
        #variable hora matriz dispersa
        aux = element_node.Hora.split(':')
        hora = aux[0]
        #variable dia matriz dispersa
        dia = element_node.Fecha[0:2]

        CarnetT = element_node.Carnet
        Fecha = element_node.Fecha[3:5]
        
        #Auxiliares para fecha
        aux1 = element_node.Fecha[6:10]
        aux2= Carnet[0:4]
        fecha_mes = element_node.Fecha[3:5]

        #Conversión a enteros
        añoTarea = int(aux1)
        añoEstud = int(aux2)

        arbolAVL.insertar_matriz(arbolAVL.raiz, element_node.Carnet, element_node.Nombre, element_node.Descripcion, element_node.Materia,
                            element_node.Fecha, element_node.Hora, element_node.Estado, añoTarea, Fecha, dia, hora)


            
    element_node.clean_values()



def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    t[0] = t[3].replace('"', '').replace(' ', '')


def p_items(t):
    """items : items item
    """
    t[0] = t[2]

def p_items_2(t):
    """items : item
    """
    t[0] = t[1]

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    if t[3].lower() == "carnet":
        element_node.Carnet = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "dpi":
        element_node.DPI = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "nombre":
        element_node.Nombre = t[5].replace('"', '')
    elif t[3].lower() == "carrera":
        element_node.Carrera = t[5].replace('"', '')
    elif t[3].lower() == "password":
        element_node.Password = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "creditos":
        element_node.Creditos = t[5]
    elif t[3].lower() == "edad":
        element_node.Edad = t[5]
    elif t[3].lower() == "correo":
        element_node.Correo = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "descripcion":
        element_node.Descripcion = t[5].replace('"', '')
    elif t[3].lower() == "materia":
        element_node.Materia = t[5].replace('"', '')
    elif t[3].lower() == "fecha":
        element_node.Fecha = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "hora":
        element_node.Hora = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "estado":
        element_node.Estado = t[5].replace('"', '').replace(' ', '')

    t[0] = element_node

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                | TCORREO
                """
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()