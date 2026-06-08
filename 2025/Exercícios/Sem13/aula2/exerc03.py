"""
Crie uma lista contendo apenas os números ímpares de 1 a 20.
"""

print("Programa que exibe uma lista dos números ímpares de 1 a 20.\n")
impares = [x for x in range(1, 21) if x % 2 != 0]

# Exibe a lista
print("Números ímpares de 1 a 20:")
print(impares)