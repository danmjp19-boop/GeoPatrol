from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "GeoPatrol Backend Activo"

if __name__ == "__main__":
    app.run()
