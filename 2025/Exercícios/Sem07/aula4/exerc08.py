"""
Faça um programa que peça para o usuário digitar 5 números e, ao
final, imprima uma lista com os 5 números digitados pelo usuário (sem
converter os números para int ou float).
"""

numeros = []

# Pedindo ao usuário para digitar 5 números
for i in range(5):
    numero = input(f"Digite o {i+1}º número: ")
    numeros.append(numero)

print("Lista com os números digitados:", numeros)