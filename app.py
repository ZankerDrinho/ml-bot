# API de teste
import os
from flask import Flask, jsonify, request
from produtos import products

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Funcionou :D"


@app.route("/produtos")
def produto():
    return jsonify(products)

@app.route("/oauth/callback")
def oauth_callback():
    code = request.args.get("code")
    state = request.args.gt("state")

    return {
        "mensagem": "Callback recebido!",
        "code": code,
        "state": state
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = "0.0.0.0", port = port)
    