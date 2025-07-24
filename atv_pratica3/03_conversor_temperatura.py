""" 3- Conversor de Temperatura """

temperatura = float(input("Digite a temperatura: "))
print("C - Celsius | K - Kelvin | F - Fahrenheit")
unidade_origem = input("Digite a unidade de origem: ")
unidade_destino = input("Digite a unidade final: ")

if (unidade_origem == "C") and (unidade_destino == "K"):
    temperatura = temperatura + 273.15
    print(f"A temperatura convertida é: {temperatura:.2f} K")
elif(unidade_origem == "C") and (unidade_destino == "F"):
    temperatura = temperatura + 32
    print(f"A temperatura convertida é: {temperatura:.2f} °F")
elif(unidade_origem == "K") and (unidade_destino == "C"):
    temperatura = temperatura - 273.15
    print(f"A temperatura convertida é: {temperatura:.2f} °C")
elif(unidade_origem == "K") and (unidade_destino == "F"):
    temperatura = temperatura - 459.67
    print(f"A temperatura convertida é: {temperatura:.2f} °F")
elif(unidade_origem == "F") and (unidade_destino == "C"):
    temperatura = temperatura - 17.7778
    print(f"A temperatura convertida é: {temperatura:.2f} °C")
elif(unidade_origem == "F") and (unidade_destino == "K"):
    temperatura = temperatura + 255.372
    print(f"A temperatura convertida é: {temperatura:.2f} K")