from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(name)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(file))
USUARIOS_FILE = os.path.join(BASE_DIR, “..”, “database”, “usuarios.json”)

with open(USUARIOS_FILE, “r”, encoding=“utf-8”) as f:
usuarios = json.load(f)

GPS en memoria

ubicaciones = {}

@app.route(”/”)
def inicio():
return “GeoPatrol Backend Activo”

@app.route(”/login”, methods=[“POST”])
def login():

datos = request.json
cc = datos.get("cc")
password = datos.get("password")
for usuario in usuarios:
    if usuario["cc"] == cc and usuario["password"] == password:
        return jsonify({
            "success": True,
            "nombre": usuario["nombre"],
            "cai": usuario["cai"],
            "cuadrantes": usuario["cuadrantes"],
            "rol": usuario["rol"],
            "cc": usuario["cc"]
        })
return jsonify({
    "success": False,
    "mensaje": "Credenciales incorrectas"
})

@app.route(”/crear_usuario”, methods=[“POST”])
def crear_usuario():

global usuarios
datos = request.json
nuevo_usuario = {
    "cc": datos.get("cc"),
    "nombre": datos.get("nombre"),
    "password": datos.get("password"),
    "cai": datos.get("cai"),
    "rol": datos.get("rol"),
    "cuadrantes": []
}
usuarios.append(nuevo_usuario)
with open(USUARIOS_FILE, "w", encoding="utf-8") as f:
    json.dump(
        usuarios,
        f,
        ensure_ascii=False,
        indent=4
    )
return jsonify({
    "success": True,
    "mensaje": "Usuario creado correctamente"
})

@app.route(”/usuarios”, methods=[“GET”])
def obtener_usuarios():

return jsonify({
    "success": True,
    "usuarios": usuarios
})

@app.route(”/actualizar_gps”, methods=[“POST”])
def actualizar_gps():

datos = request.json
cc = datos.get("cc")
lat = datos.get("lat")
lon = datos.get("lon")
ubicaciones[cc] = {
    "lat": lat,
    "lon": lon
}
return jsonify({
    "success": True
})

@app.route(”/gps”, methods=[“GET”])
def obtener_gps():

return jsonify({
    "success": True,
    "ubicaciones": ubicaciones
})

if name == “main”:
app.run(debug=True)
