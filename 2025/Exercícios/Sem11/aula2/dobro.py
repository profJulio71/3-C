# Lista original
lista_original = [1, 2, 3, 4, 5]

# Criando nova lista com o dobro dos valores
nova_lista = [valor * 2 for indice, valor in enumerate(lista_original)]

print(nova_lista)