from flask import Flask, jsonify

app = Flask(__name__)

coordenadas = {}
ponto = 1

@app.route("/", methods=["GET"])
def home():
    coordenadas[ponto] = {"latitude": -6, "longitude": -36}
    return "<h1>Primeiro App dplyado no Render</h1>"

@app.route("/coordenadas", methods=["GET"])
def coordenadas():
    ponto = 2
    coordenadas[ponto] = {"latitude": -6.423, "longitude": -36.1245}
    return jsonify(coordenadas)

if __name__ == "__main__":
    app.run()