""" 4- Analisador de Números Pares e Ímpares """

numero_par = 0
numero_impar = 0

while True:
    entrada = input("Digite um número inteiro ou digite 'fim' para finalizar o programa: ")
    
    if entrada.lower() == "fim":
            print(f"Quantidade de números pares: {numero_par}")
            print(f"Quantidade de números ímpares: {numero_impar}")
            break
        
    try:
        numero = int(entrada)
        if (numero % 2 == 0):
            print("Número par")
            numero_par = numero_par + 1
        else:
            print("Número ímpar")
            numero_impar = numero_impar + 1
    except ValueError:
        print("Digite um número válido, ou digite 'fim' para finalizar o programa")