""" 3- Calculadora de Desconto em Produto """

preco_original = float(input("Digite o preço original: "))
desconto_percentual = float(input("Digite o percentual do desconto: "))

def aplicar_desconto(preco_original, desconto_percentual):
    desconto_total = preco_original * (desconto_percentual/100)
    preco_final = preco_original - desconto_total
    print(f"Preço final: R$ {preco_final:.2f}")
    return preco_final

valor_pagar = aplicar_desconto(preco_original, desconto_percentual)