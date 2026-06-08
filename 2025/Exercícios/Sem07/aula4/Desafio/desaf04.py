"""
Crie um programa que imprima os elementos de uma lista de números,
pulando de dois em dois, usando um loop for.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando for com step 2
for i in range(0, len(numeros), 2):
    print(numeros[i])