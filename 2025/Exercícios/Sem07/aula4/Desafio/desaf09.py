"""
Crie um programa que calcule a média dos números em uma lista
usando um loop for.
"""

numeros = [15, 25, 35, 45, 55]

soma = 0

# Loop para somar os números
for numero in numeros:
    soma += numero

# Calcula a média
media = soma / len(numeros)

print("Números:", numeros)
print("Média:", media)