"""
Crie um dicionário com os números de 1 a 10 como chaves e seus quadrados como valores, mas apenas para números ímpares.
"""

print("Programa que exibe um dicionário com os números de 1 a 10 como chaves e seus quadrados como valores, mas apenas para números ímpares.\n")
quadrados_impares = {x: x**2 for x in range(1, 11) if x % 2 != 0}

# Exibe os pares chave-valor
print("Números ímpares e seus quadrados:")
for chave, valor in quadrados_impares.items():
    print(f"{chave}² = {valor}")