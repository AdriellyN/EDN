""" 4- Calculadora de Idade em Dias """

ano_nascimento = int(input("Digite o ano de seu nascimento: "))

def calcular_idade_dias (ano_nascimento):
    idade_dias = ((2025 - ano_nascimento) * 365)
    print(f"Idade aproximada em dias: {idade_dias}")
    return idade_dias

idade = calcular_idade_dias(ano_nascimento)