""" Faça um programa que imprima o maior número da lista [-8, -6, 3, -1, 7],
sem usar o método max(). """

lista = [-8, 18, 3, -1, 7]
i = 0
maior_numero = lista[i]
i = 0
for i in range(1, len(lista)):
  if lista[i] > maior_numero:
    maior_numero = lista[i]
print("O maior número da lista é: ", maior_numero)