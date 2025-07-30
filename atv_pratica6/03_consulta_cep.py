""" 3- Consulta de CEP """

import requests

cep = input("Digite um cep: ")

try:
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code == 200:
        logradouro = response.json()["logradouro"]
        bairro = response.json()["bairro"]
        cidade = response.json()["localidade"]
        estado = response.json()["uf"]
        cep = response.json()["cep"]
        print(f"Endereço: {logradouro}, {bairro}, {cidade}, {estado} - {cep}")
except KeyError:
        print("CEP não encontrado. Tente novamente.")
