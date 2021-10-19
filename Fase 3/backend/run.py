from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.wrappers import UserAgentMixin

app = Flask(__name__)
CORS(app)

users = {
    "data":
    [
        {
            "username": "admin",
            "password": "admin",
            "id": 0
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
    

    return jsonify(users)

if __name__ == "__main__":
    app.run(port=3000, debug=True)