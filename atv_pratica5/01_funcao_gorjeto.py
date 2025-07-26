""" 1- Calculadora de Gorjeta """

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta/100)
    return gorjeta

valor_gorjeta = calcular_gorjeta(200, 15)
print(f"O valor da gorjeta é: {valor_gorjeta}")