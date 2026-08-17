# Consumidor API

import requests
from ofertas import analyze_offer
url = "http://127.0.0.1:5000/produtos"

try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    data = resposta.json()

    analyze_offer(data)

except requests.RequestException as erro:
    print("Erro ao acessar a API:", erro)

