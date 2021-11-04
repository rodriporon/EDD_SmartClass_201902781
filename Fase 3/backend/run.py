from flask import Flask, json, jsonify, request
from flask_cors import CORS
from estructuras.ArbolAVL.arbolAVL import ArbolAVL
from estructuras.TablaHash.tablaHash import TablaHash
from estructuras.AVLPensum.arbolPensum import ArbolPensum

app = Flask(__name__)
CORS(app)

#----------Instanciación Arbol AVL estudiantes----------#
users = ArbolAVL()
users.datosDesencriptados(users.raiz)

#----------Instanciación Arbol Pensum----------#
arbol_pensum = ArbolPensum()
arbol_pensum.inOrden(arbol_pensum.raiz)

#----------Instanciación Tabla Hash----------#
tabla_hash = TablaHash()


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

    print(tabla_hash.obtenerTabla())

    if (str(carnet_request) == "admin" and str(password_request) == "admin"):
        return jsonify({"carnet": "admin", "DPI": "admin", "nombre": "admin", "carrera": "admin", "correo": "admin", "password": "admin", "edad": "admin"})

    else:
        user = users.buscar(users.raiz, carnet_request, password_request)
        print(user)

        if str(user["carnet"]) == str(carnet_request) and str(user["password"]) and str(password_request):
            return jsonify(user)
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

@app.route('/nuevo-apunte', methods=['POST'])
def nuevoApunte():
    carnet_request = request.json.get("carnet")
    titulo_request = request.json.get("titulo")
    contenido_request = request.json.get("contenido")

    tabla_hash.insertar(carnet_request, titulo_request, contenido_request)

    print('------Tabla Hash--------')
    tabla_hash.obtenerTabla()

    return jsonify({"titulo": titulo_request})

@app.route('/obtener-apuntes/<carnet>', methods=['GET'])
def obtenerApuntes(carnet):
    data = tabla_hash.obtenerApuntes(carnet)
    print(data)
    if data:
        print(data)
        return jsonify(data)
    else:
        return jsonify({"msg": "Error en la consulta al server"}), 401

@app.route('/apunte/<carnet>/<id>', methods=['GET'])
def obtenerApunte(carnet, id):
    apunte = tabla_hash.obtenerApunte(carnet, id)
    if apunte:
        print(apunte)
        return jsonify(apunte)
    else:
       return jsonify({"msg": "Error en la consulta al server"}), 401 

@app.route('/carga-estudiantes', methods=['POST'])
def cargaEstudiantes():
    data = request.get_json()
    estudiantes = json.loads(data)

    for estudiante in estudiantes["estudiantes"]:
        carnet = estudiante['carnet']
        DPI = estudiante['DPI']
        nombre = estudiante['nombre']
        carrera = estudiante['carrera']
        correo = estudiante['correo']
        password = estudiante['password']
        edad = estudiante['edad']

        users.insertar(str(carnet), str(DPI), str(nombre), str(carrera), str(correo), str(password), str(edad))

    if data:
        return jsonify({"msg": "Carga exitosa"})
    return jsonify({"msg": "Error en la consulta al server"}), 400

@app.route('/carga-apuntes', methods=['POST'])
def cargaApuntes():
    data = request.get_json()
    usuarios = json.loads(data)

    for usuario in usuarios["usuarios"]:
        carnet = usuario['carnet']
        apuntes = usuario['apuntes']
        for apunte in apuntes:
            print(apunte['Título'])
            titulo = apunte['Título']
            contenido = apunte['Contenido']
            tabla_hash.insertar(carnet, titulo, contenido) 

    if data:
        return jsonify({"msg": "Carga exitosa"})
    return jsonify({"msg": "Error en la consulta al server"}), 400

@app.route('/carga-pensum', methods=['POST'])
def cargaPensum():
    data = request.get_json()
    cursos = json.loads(data)

    for curso in cursos["Cursos"]:
        codigo = curso['Codigo']
        nombre = curso['Nombre']
        creditos = curso['Creditos']
        prerequisitos = curso['Prerequisitos']
        obligatorio = curso['Obligatorio']
        
        arbol_pensum.insertar(codigo, nombre, creditos, prerequisitos, obligatorio)
        arbol_pensum.inOrden(arbol_pensum.raiz)        

    if data:
        return jsonify({"msg": "Carga exitosa"})
    return jsonify({"msg": "Error en la consulta al server"}), 400

@app.route('/carga-cursos-estudiante', methods=['POST'])
def cargaCursosEstudiante():
    data = request.get_json()
    estudiantes = json.loads(data)

    for estudiante in estudiantes["Estudiantes"]:
        carnet = estudiante['Carnet']
        nodo_estudiante = users.buscarEstudiante(users.raiz, carnet)
        for año in estudiante['Años']:
            for semestre in año['Semestres']:
                for curso in semestre['Cursos']:
                    codigo = curso['Codigo']
                    nombre = curso['Nombre']
                    creditos = curso['Creditos']
                    prerequisitos = curso['Prerequisitos']
                    obligatorio = curso['Obligatorio']
                    if nodo_estudiante:
                        nodo_estudiante.cursos_asignados.insertar(codigo, nombre, creditos, prerequisitos, obligatorio)
                    


    if data:
        return jsonify({"msg": "Carga exitosa"})
    return jsonify({"msg": "Error en la consulta al server"}), 400

@app.route('/reporte/<tipo>/<seguridad>', methods=['GET'])
def reportes(tipo, seguridad):

    if str(tipo) == "estudiantes" and str(seguridad) == "encriptado":
        print('Entró a reporte estudiantes encriptado')
        users.graficarEncriptado()

    elif str(tipo) == "estudiantes" and str(seguridad) == "desencriptado":
        print('Entró a reporte estudiantes desencriptado')
        users.graficarDesencriptado()

    elif str(tipo) == "cursos-asignados":
        print('Entró a cursos asignados')
        nodo_estudiante = users.buscarEstudiante(users.raiz, seguridad)
        nodo_estudiante.cursos_asignados.graficar()


    return jsonify({"msg": "all ok"})

@app.route('/graficar-tablahash', methods=['GET'])
def graficarTablaHash():

    tabla_hash.graficar()

    return jsonify({"msg": "all ok"})
    

if __name__ == "__main__":
    app.run(port=3000, debug=True)