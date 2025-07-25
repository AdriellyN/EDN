""" 2- Registro de Notas e Cálculo da Média """

soma_medias = 0
i = 0

while True:
    entrada = input("Digite a média do aluno, ou a palavra 'fim' para encerrar: ")

    if entrada.lower() == "fim":
        break

    try:
        media_aluno = float(entrada)
        if (media_aluno >= 0) and (media_aluno <= 10):
            soma_medias = soma_medias + media_aluno
            i = i + 1
        else:
            print("Digite um valor válido")
    except ValueError:
        print("Entrada inválida. Digite um número de 0 a 10. Ou 'fim' para finalizar o programa.")

if i > 0:
    media_turma = soma_medias / i
    print(f"A média da turma é: {media_turma:.2f}")
else:
    ("Não há valores para cálculo da média")