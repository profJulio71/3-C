"""
Dada uma lista de strings, utilize um loop for para criar uma nova lista
contendo o comprimento de cada string.
"""

# Lista original de strings
palavras = ["python", "laço", "for", "exemplo", "lista"]

# Nova lista com os comprimentos
comprimentos = []

for palavra in palavras:
    comprimentos.append(len(palavra))

# Exibindo o resultado
print("Lista original:", palavras)
print("Comprimentos:  ", comprimentos)