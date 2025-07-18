from flask import Flask, jsonify, request

app = Flask(__name__)

coordenadas_dict = {}
ponto = 0

@app.route("/", methods=["GET"])
def home():
    return "<h1>Primeiro App deployado no Render</h1>"

@app.route("/coordenadas", methods=["GET"])
def coordenadas():
    global ponto
    ponto += 1
    coordenadas_dict[ponto] = {"latitude": -6.423, "longitude": -36.1245}
    return jsonify(coordenadas_dict)

@app.route("/limpar", methods=["GET"])
def limpar():
    global coordenadas_dict, ponto
    coordenadas_dict = {}
    ponto = 0
    return "Dicionário zerado"

@app.route("/novas-coordenadas", methods=["POST"])
def novas_coordenadas():
    dados = request.get_json()

    latitude = dados.get("latitude")
    longitude = dados.get("longitude")

    return jsonify({"messagem": "Dados recebidos", "latitude": latitude, "longitude": longitude}), 200

if __name__ == "__main__":
    app.run()