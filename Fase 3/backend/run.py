from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {
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

#users["data"].append({"carnet": "rodri", "password": "rodri", "id": 1})
#print(users["data"])

""" for user in users["data"]:
    if user["carnet"] == "rodri":
        print(f'password is: {user["password"]}') """
    

@app.route('/')
def index():
    return 'Backend de la Tercera Fase SmartClass EDD'

@app.route('/login', methods=['GET','POST'])
def login():

    carnet_request = request.json.get("carnet", None)
    password_request = request.json.get("password", None)

    for user in users["data"]:
        print(f'carnet: {user["carnet"]}')
        if str(carnet_request) == str(user["carnet"]) and str(password_request) == str(user["password"]):
            return jsonify(user)

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

    print(f'CARNET_REQUEST: {carnet_request}')
    print()
    print()

    users["data"].append({"carnet": carnet_request, "DPI": DPI_request, "nombre": nombre_request, "carrera": carrera_request, "correo": correo_request, "password": password_request, "edad": edad_request, "id": id_request})

    print(users)

    return jsonify({"carnet": carnet_request})

if __name__ == "__main__":
    app.run(port=3000, debug=True)