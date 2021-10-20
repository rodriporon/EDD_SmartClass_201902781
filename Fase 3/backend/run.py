from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {
    "data":
    [
        {
            "username": "admin",
            "password": "admin",
            "id": 0
        },
                {
            "username": "rodri",
            "password": "rodri",
            "id": 1
        },
                {
            "username": "admin2",
            "password": "admin2",
            "id": 2
        }
    ]
}

#users["data"].append({"username": "rodri", "password": "rodri", "id": 1})
#print(users["data"])

""" for user in users["data"]:
    if user["username"] == "rodri":
        print(f'password is: {user["password"]}') """
    

@app.route('/')
def index():
    return 'Backend de la Tercera Fase SmartClass EDD'

@app.route('/login', methods=['GET','POST'])
def login():

    username_request = request.json.get("username", None)
    password_request = request.json.get("password", None)

    for user in users["data"]:
        print(f'username: {user["username"]}')
        if str(username_request) == str(user["username"]) and str(password_request) == str(user["password"]):
            return jsonify({"username": user["username"]})

    return jsonify({"msg": "Bad username or password"}), 401

if __name__ == "__main__":
    app.run(port=3000, debug=True)