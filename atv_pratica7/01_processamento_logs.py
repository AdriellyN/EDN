""" 1- Processamento de Logs de Treinamento """
"""Crie um programa que analisa um arquivo CSV contendo dados de execução de um processo de treinamento. O programa deve:

* Solicitar ao usuário o nome do arquivo CSV (ex: logs_treinamento.csv).  
* Ler os dados usando a biblioteca `pandas`.  
* Calcular a média e o desvio padrão da coluna `tempo_execucao`.  
* Exibir os resultados com duas casas decimais.  
* Tratar erros como arquivo inexistente ou formatação incorreta.

Dica: Use `df['coluna'].mean()` e `df['coluna'].std()` para obter os resultados estatísticos."""

import pandas as pd

nome_arquivo = input("Digite o nome do arquivo desejado (exemplo: arquivo.csv): ")

leitura_dados = pd.read_csv(nome_arquivo)
print(leitura_dados)