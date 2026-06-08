"""
Utilizando compreensão de lista, obtenha os primeiros cinco múltiplos de 3.
"""

print("Programa que exibe uma lista dos primeiros cinco múltiplos de 3.\n")
multiplos_de_3 = [3 * x for x in range(1, 6)]

# Exibe a lista
print("Primeiros cinco múltiplos de 3:")
print(multiplos_de_3)