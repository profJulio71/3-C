"""
Peça ao usuário que digite uma frase. Conte o número de palavras na frase e
imprima o resultado.
"""

# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

"""
    Conta o número de palavras na frase
    O método split() divide a frase em uma lista de palavras
"""
palavras = frase.split()

# Imprime o número de palavras
print("Número de palavras na frase:", len(palavras))