"""
Faça um programa que, dadas duas listas de mesmo tamanho, crie
uma nova lista com cada elemento igual à soma dos elementos da
lista 1 com os da lista 2, na mesma posição.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Criando uma nova lista com a soma dos elementos das duas listas
soma_listas = [lista1[i] + lista2[i] for i in range(len(lista1))]

print(soma_listas)