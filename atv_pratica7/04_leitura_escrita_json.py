""" 4- Leitura e Escrita de Arquivo JSON """

import json

dados_pessoas = {
        "nome": "Ana",
        "idade": 19,
        "Cidade": "São Paulo"
    }

nome_arquivo = input("Digite o nome para o arquivo json (Exemplo: arquivo.json): ")

try:
    with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
        json.dump(dados_pessoas, arquivo, ensure_ascii=False, indent=4)
except KeyError:
    print("Não foi possível gravar os dados.")

try:
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)
    print(dados_lidos)
except FileExistsError:
    print("O arquivo não existe. Verifique o nome do arquivo e tente novamente.")

arquivo.close()