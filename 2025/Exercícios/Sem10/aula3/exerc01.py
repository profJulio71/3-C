"""
1. Faça uma função que recebe um número e imprima seu dobro.
"""

def imprimir_dobro(numero):
    dobro = numero * 2
    print(f"O dobro de {numero} é {dobro}")

# Programa principal
numero = float(input("Digite um número: "))
imprimir_dobro(numero)