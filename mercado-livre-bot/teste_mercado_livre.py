import requests

item_id = "MLB55462541"

url = f"https://api.mercadolibre.com/items/{item_id}"

resposta = requests.get(url)

print(f"status:", resposta.status_code)
print(resposta.text)
