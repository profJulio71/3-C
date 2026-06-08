"""
Faça um programa que imprima o maior número de uma lista, sem usar o
método max().
"""

numeros = [4, 10, 23, 7, 5, 88, 32, 1]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número da lista é:", maior)