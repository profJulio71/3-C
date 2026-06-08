"""
Dada uma lista de nomes, utilize um loop for e a função enumerate()
para imprimir cada nome junto ao seu índice.
"""

nomes = ["Amanda", "Ana", "Bruno", "André", "Carlos",
         "Daniela", "Eduardo", "João", "Paulo", "Pedro"]

for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")