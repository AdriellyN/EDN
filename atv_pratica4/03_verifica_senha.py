""" 3- Verificador de Senhas Fortes """

while True:
    senha = input("Digite uma senha: ")
    numero = False
    tamanho = False
    if (senha.lower() == "sair"):
        break
    else:
        if len(senha) >= 8:
            tamanho = True
        if any(char.isdigit() for char in senha):
            numero = True
        if tamanho == True and numero == True:
            print("Senha forte \nFim do programa.")
            break
        else:
            print("Senha Fraca. Tente de novo.\n")