"""
Você está desenvolvendo um programa de inventário para uma loja.
Crie uma função chamada imprimir_produtosque aceite uma lista de produtos e imprima cada produto com seu índice.
produtos = ['Computador', 'Mouse', 'Teclado']
"""

def imprimir_produtos(produtos):
    for indice, produto in enumerate(produtos):
        print(f"{indice}: {produto}")

# Exemplo de uso
produtos = ['Computador', 'Mouse', 'Teclado']
imprimir_produtos(produtos)