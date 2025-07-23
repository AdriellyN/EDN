""" 2- Calculadora de Desconto """

nome_produto = "Camiseta"
preco_original = 50.00
desconto = 0.2

valor_desconto = preco_original * desconto
preco_final = preco_original * (1 - desconto)

print(f"Preço original: {preco_original:.2f}")
print(f"Valor do desconto: {valor_desconto:.2f}")
print(f"Valor final: {preco_final:.2f}")