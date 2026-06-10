"""
Crie um programa que calcule a média dos números em uma lista
usando um loop for.
"""

numeros = [1, 9, 15, 5, 8, 12, 20, 7, 45, 99]

soma = 0

# Loop para percorrer a lista e somar os valores
for numero in numeros:
    soma += numero

# Verifica se a lista não está vazia para evitar divisão por zero
if len(numeros) > 0:
    media = soma / len(numeros)
    print("Lista:", numeros)
    print("Média dos números:", media)
else:
    print("A lista está vazia. Não é possível calcular a média.")