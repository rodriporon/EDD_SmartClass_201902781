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
            "carnet": "rodri",
            "password": "rodri",
            "id": 1
        },
                {
            "carnet": "admin2",
            "password": "admin2",
            "id": 2
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
            return jsonify({"carnet": user["carnet"]})

    return jsonify({"msg": "Bad carnet or password"}), 401

@app.route('/register', methods=['POST'])
def register():

    return jsonify({"msg": "register"})

if __name__ == "__main__":
    app.run(port=3000, debug=True)