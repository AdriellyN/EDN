""" 1- Gerador de Senhas Seguras """

import random
import string

tamanho = int(input("Digite um tamanho para sua senha: "))

def gerar_senha (tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha
    
print(f"Sua senha: {gerar_senha(tamanho)}")

