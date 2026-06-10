"""
Gere uma lista com os cubos dos números pares de 1 a 10.
"""

print("Programa que exibe o cubo de uma lista de 1 a 10.\n")
cubos = [x**3 for x in range(1, 11)]

# Exibe a lista
print("Lista dos cubos de 1 a 10:")
print(cubos)