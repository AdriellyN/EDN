""" 2- Escrita de Arquivo CSV """

import csv

dados_pessoas = [
    ["Ana", 19, "São Paulo"],
    ["Teo", 21, "Recife"],
    ["Lua", 30, "Registro"]
]

nome_arquivo = input("Digite o nome para o arquivo csv (Exemplo: arquivo.csv): ")

try:
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Nome", "Idade", "Cidade"])
        escritor.writerows(dados_pessoas)

    print(f"Dados gravados no arquivo '{nome_arquivo}'.")
    arquivo_csv.close()
except Exception:
    print(f"Ocorreu um erro ao gravar o arquivo.")