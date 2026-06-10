"""
Escreva um programa que calcule o fatorial de um número inteiro não
negativo N fornecido pelo usuário usando um loop for.
"""

while True:
    n = int(input("Digite um número inteiro não negativo emaior que 0: "))

    # Verifica se o número é válido
    if n < 0:
        print("Número inválido! \nPor favor, digite um número não negativo.")
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        print(f"O fatorial de {n} é: {fatorial}")
        break