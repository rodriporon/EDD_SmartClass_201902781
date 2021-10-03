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
        #arbolAVL.inOrden(arbolAVL.raiz)
    return (f'Carga Masiva. Tipo: {tipo}, path: {path}')


@app.route('/reporte', methods=['GET'])
def reporte():
    data = request.get_json()
    tipo = data['tipo']

    if tipo == 0:
        arbolAVL.graficar()

    elif tipo == 1:
        carnet = data['carnet']
        año = data['año']
        mes = data['mes']

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








if __name__ == "__main__":
    app.run(port=3000, debug=True)