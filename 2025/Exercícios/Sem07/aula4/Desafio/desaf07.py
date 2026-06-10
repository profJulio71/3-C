"""
Escreva um programa que imprima os primeiros N termos da sequência
de Fibonacci usando um loop for.
"""

# Solicita ao usuário quantos termos da sequência exibir
n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

# Verifica se o número é válido
if n <= 0:
    print("Por favor, digite um número maior que 0.")
else:
    a, b = 0, 1
    print("Sequência de Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b