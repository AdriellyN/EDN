""" 2- Gerador de Usuário Aleatório """

import requests

response = requests.get("https://randomuser.me/api/")

if response.status_code == 200:
    dados = response.json()['results'][0]
    nome = f"{dados['name']['first']} {dados['name']['last']}"
    email = dados['email']
    pais = dados['location']['country']

print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"País: {pais}")