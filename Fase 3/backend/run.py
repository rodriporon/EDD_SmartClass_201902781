from flask import Flask, jsonify, request
from flask_cors import CORS
from estructuras.ArbolAVL.arbolAVL import ArbolAVL

app = Flask(__name__)
CORS(app)

users = ArbolAVL()
users.datosDesencriptados(users.raiz)


users_json = {
    "data":
    [
        {
            "carnet": "admin",
            "password": "admin",
            "id": 0
        },
        {
            "carnet": "201902781",
            "DPI": "3065713820401",
            "nombre": "Rodrigo Poron",
            "carrera": "Ingenieria en Ciencias y Sistemas",
            "correo": "rodriporon2@gmail.com",
            "password": "1244",
            "edad": "22"
        }
    ]
}

    

@app.route('/')
def index():
    return 'Backend de la Tercera Fase SmartClass EDD'

@app.route('/login', methods=['GET','POST'])
def login():

    carnet_request = request.json.get("carnet", None)
    password_request = request.json.get("password", None)
    print(carnet_request)
    print(password_request)

    if (str(carnet_request) == "admin" and str(password_request) == "password"):
        return jsonify({"carnet": "admin", "DPI": "admin", "nombre": "admin", "carrera": "admin", "correo": "admin", "password": "admin", "edad": "admin"})

    else:
        user = users.buscar(users.raiz, carnet_request, password_request)

    if user:
        return jsonify(carnet=user.carnet, DPI=user.DPI, nombre=user.nombre, carrera=user.carrera, correo=user.correo, password=user.password, edad=user.edad)
    else:
        return jsonify({"msg": "Bad carnet or password"}), 401

@app.route('/register', methods=['POST'])
def register():



    id_request = 0

    carnet_request = request.json.get("carnet")
    DPI_request = request.json.get("DPI")
    nombre_request = request.json.get("nombre")
    carrera_request = request.json.get("carrera")
    correo_request = request.json.get("correo")
    password_request = request.json.get("password")
    edad_request = request.json.get("edad")
    id_request += 1


    users.insertar(carnet_request, DPI_request, nombre_request, carrera_request, correo_request, password_request, edad_request)
    print()
    print('----AVL encriptado----')
    users.datosEncriptados(users.raiz)
    print()

    print()
    print('----AVL Desencriptado----')
    users.datosDesencriptados(users.raiz)
    print()
    

    return jsonify({"carnet": carnet_request})

@app.route('/password-maestro', methods=['POST'])
def passwordMaestro():
    password_maestro = request.json.get("password_maestro")



if __name__ == "__main__":
    app.run(port=3000, debug=True)