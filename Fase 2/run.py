from flask import Flask, request
from flask_cors import CORS
from Analizadores.Sintactico import parser, arbolAVL

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return 'Segunda Fase SmartClass EDD'

@app.route('/carga', methods=['POST'])
def carga():
    data = request.get_json()
    tipo = data['tipo']
    path = data['path']
    if (tipo == 'estudiante' or 'recordatorio'):
        f = open(path,"r", encoding="utf-8")
        mensaje = f.read()
        f.close()
        parser.parse(mensaje)
        arbolAVL.inOrden(arbolAVL.raiz)
    return (f'Carga Masiva. Tipo: {tipo}, path: {path}')


@app.route('/reporte', methods=['GET'])
def reporte():
    data = request.get_json()
    tipo = data['tipo']

    if tipo == 0:
        arbolAVL.graficar()

    #Tipo 1, grafica matriz dispersa
    elif tipo == 1:
        carnet = data['carnet']
        año = data['año']
        mes = data['mes']
    #Método del AVL que se conecta con las demás estructuras hasta encontrar la matriz a graficar
        arbolAVL.buscar(arbolAVL.raiz, carnet, año, mes)
        #print('entró a tipo 1')

    elif tipo == 2:
        carnet = data['carnet']
        año = data['año']
        mes = data['mes']
        dia = data['dia']
        hora = data['hora']
        arbolAVL.graficarListaTareas(arbolAVL.raiz, carnet, año, mes, dia, hora)

        
    return (f'Reporte de tipo: {tipo}')

@app.route('/estudiante', methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    carnet = data['carnet']
    DPI = data['DPI']
    nombre = data['nombre']
    carrera = data['carrera']
    correo = data['correo']
    password = data['password']
    creditos = data['creditos']
    edad = data['edad']

    arbolAVL.insertar(carnet, DPI, nombre, carrera, correo, password, creditos, edad)

    return (f'Se creó el estudiante: {nombre}')

@app.route('/estudiante', methods=['PUT'])
def modificarEstudiante():
    data = request.get_json()
    carnet = data['carnet']
    DPI = data['DPI']
    nombre = data['nombre']
    carrera = data['carrera']
    correo = data['correo']
    password = data['password']
    creditos = data['creditos']
    edad = data['edad']

    arbolAVL.modificarEstudiante(arbolAVL.raiz, carnet, DPI, nombre, carrera, correo, password, creditos, edad)

    return (f'Se modificó al estudiante: {nombre}')

@app.route('/estudiante', methods=['GET'])
def obtenerEstudiante():
    data = request.get_json()
    carnet = data['carnet']

    arbolAVL.obtenerEstudiante(arbolAVL.raiz, carnet)

    return ('Se envió la solicitud')

@app.route('/recordatorios', methods=['POST'])
def crearRecordatorio():
    data = request.get_json()
    Carnet = data['Carnet']
    Nombre = data['Nombre']
    Descripcion = data['Descripcion']
    Materia = data['Materia']
    Fecha = data['Fecha']
    Hora = data['Hora']
    Estado = data['Estado']

    aux = Hora.split(':')
    hora_aux = aux[0]

    #Auxiliares para fecha
    aux1 = Fecha[6:10]
    
    mes = Fecha[3:5]

    dia = Fecha[0:2]

    #Conversión a enteros
    año = int(aux1)

    arbolAVL.crearRecordatorio(arbolAVL.raiz, Carnet, Nombre, Descripcion, Materia, Fecha, Hora, Estado, año, mes, dia, hora_aux)

    return (f'Se creó el recordatorio')

@app.route('/recordatorios', methods=['PUT'])
def modificarRecordatorio():
    data = request.get_json()
    Carnet = data['Carnet']
    Nombre = data['Nombre']
    Descripcion = data['Descripcion']
    Materia = data['Materia']
    Fecha = data['Fecha']
    Hora = data['Hora']
    Estado = data['Estado']

    return (f'Se modificó el recordatorio')

@app.route('/recordatorios', methods=['GET'])
def obtenerRecordatorio():
    data = request.get_json()
    Carnet = data['Carnet']
    Fecha = data['Fecha']
    Hora = data['Hora']

    arbolAVL.obtenerRecordatorio(arbolAVL.raiz, Carnet, Fecha, Hora)
    

    return (f'Se envió la solicitud')








if __name__ == "__main__":
    app.run(port=3000, debug=True)