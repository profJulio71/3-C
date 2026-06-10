"""
Gere um dicionário em que as chavess ão os números de 1 a 10, e os valores são seus cubos.
"""

print("Programa que exibe um dicionário em que as chavessão os números de 1 a 10, e os valores são seus cubos.\n")
cubos = {x: x**3 for x in range(1, 11)}

# Exibe um par chave-valor por linha
print("Números e seus cubos:")
for chave, valor in cubos.items():
    print(f"{chave}³ = {valor}")