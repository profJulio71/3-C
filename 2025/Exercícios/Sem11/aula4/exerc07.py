"""
Você tem uma lista de palavras.
Crie uma função chamada contar_letrasque aceite a lista de palavras e imprima o número de letras em cada palavra junto com seu índice.
palavras = ['python', 'exemplo', 'programacao’]
"""

def contar_letras(palavras):
    for indice, palavra in enumerate(palavras):
        print(f"Palavra {indice}: '{palavra}' tem {len(palavra)} letras")

# Exemplo de uso
palavras = ['python', 'exemplo', 'programacao']
contar_letras(palavras)