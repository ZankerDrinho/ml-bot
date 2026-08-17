# API de teste
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
    app.run(debug=True)
    