from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Primeiro App dplyado no Render</h1>"

@app.route("/coordenadas", methods=["GET"])
def coordenadas():
    return jsonify({"latitude": -6, "longitude": -36})

if __name__ == "__main__":
    app.run()