from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("../database/database/usuarios.json", "r") as f:
    usuarios = json.load(f)

@app.route("/")
def inicio():
    return "GeoPatrol Backend Activo"

@app.route("/login", methods=["POST"])
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
                "rol": usuario["rol"]
            })

    return jsonify({
        "success": False,
        "mensaje": "Credenciales incorrectas"
    })

if __name__ == "__main__":
    app.run(debug=True)
