""" 1- Calculadora Simples """

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("|(*) - Multiplicação | (/) - Divisão |")
print("|(+) - Soma          | (-) Subtração |")
operacao = input("Digite a operação desejada: ")
resultado = 0

try:
    if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
        if operacao == "*":
            resultado = numero1*numero2
        elif operacao == "/":
            resultado = numero1/numero2
        elif operacao == "+":
            resultado = numero1+numero2
        elif operacao == "-":
            resultado = numero1-numero2
        print(f"{numero1}{operacao}{numero2} = {resultado:.2f}")
    else:
        print("Você deve digitar um operador válido")
except ValueError:
    print("Você deve digitar número e operador válido.")
except ZeroDivisionError:
    print("Não é possível realizar divisões com denominador zero.")