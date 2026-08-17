import requests

url = "https://httpbin.org/get"

resposta = requests.get(url)

dados = resposta.json()

print(dados["headers"].keys())
print(dados["headers"].get("Host"))
