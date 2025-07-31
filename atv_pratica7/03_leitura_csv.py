""" 3- Leitura de Arquivo CSV """

import csv

nome_arquivo = input("Digite o nome do arquivo que você quer abrir (exemplo: arquivo.csv): ")

with open(nome_arquivo, mode='r', newline='', encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(f"Linha CSV: {linha}")

arquivo.close()