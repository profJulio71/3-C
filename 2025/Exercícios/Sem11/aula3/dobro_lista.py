numeros = [1, 3, 5, 7, 19]

# Utilizando enumerate para iterar e criar a nova lista
nova_lista = [valor * 2 for indice, valor in enumerate(numeros)]
"""
    enumerate(numeros)
    A função enumerate() serve para iterar sobre uma lista (ou outro iterável)
    fornecendo dois valores a cada passo:
    o índice do elemento (posição na lista), e o valor do elemento em si.
    A estrutura [valor * 2 for indice, valor in enumerate(numeros)] é uma forma
    compacta de criar uma nova lista.
    Para cada par (indice, valor) em enumerate(numeros), pegue valor * 2 e coloque
    na nova lista.
"""

print(nova_lista)