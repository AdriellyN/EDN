""" 1- Classificador de Idade"""

idade = int(input("Digite sua idade: "))

if (idade <= 12) :
    print("Criança")
elif idade >= 60 :
    print("Idoso")
elif idade >= 18 :
    print("Adulto")
else :
    print("Adolescente")