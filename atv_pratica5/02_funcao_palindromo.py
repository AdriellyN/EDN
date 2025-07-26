""" 2- Verificador de Palíndromos """

def verificar_palindromo (texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    tamanho = len(texto)
    for i in range(tamanho//2):
        if texto[i] != texto[-(i+1)]:
            print(f"Não.")
            return 0
    print("Sim.")
    return 1    

palindromo = verificar_palindromo("A cara rajada da jararaca")