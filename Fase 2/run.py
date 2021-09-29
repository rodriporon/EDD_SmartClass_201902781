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

    elif tipo == 1:
        carnet = data['carnet']
        año = data['año']
        mes = data['mes']

    elif tipo == 2:
        carnet = data['carnet']
        año = data['año']
        mes = data['mes']
        dia = data['dia']
        hora = data['hora']

    
    return (f'Reporte de tipo: {tipo}')




if __name__ == "__main__":
    app.run(port=3000, debug=True)