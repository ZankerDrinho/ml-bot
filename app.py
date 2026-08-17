# API de teste
import os
from flask import Flask, jsonify
from produtos import products

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Olá! Meu bot está funcionando"


@app.route("/produtos")
def produto():
    return jsonify(products)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = "0.0.0.0", port = port)
    