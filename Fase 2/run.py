from flask import Flask, request
from flask_cors import CORS

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
    return (f'Carga Masiva. Tipo: {tipo}, path: {path}')


if __name__ == "__main__":
    app.run(port=3000, debug=True)