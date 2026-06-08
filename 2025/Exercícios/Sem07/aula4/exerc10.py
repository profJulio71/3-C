"""
Usando listas, faça um programa que peça as 4 notas bimestrais e
mostre a média.
"""

notas = []

# Pedindo ao usuário para digitar as 4 notas bimestrais
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota bimestral: "))
    notas.append(nota)

# Calculando a média das notas
media = sum(notas) / len(notas)

print(f"A média das notas bimestrais é: {media:.2f}")