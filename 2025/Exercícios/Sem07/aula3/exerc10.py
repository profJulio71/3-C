""" Faça um programa que imprima o maior número de uma lista, sem usar o
método max(). """

lista = [-18, -6, 3, -1, 7]

listas = sorted(lista, reverse=True)
print(listas[0],"\n")

l = 0

while l < 3:
    print(listas[l])
    l += 1