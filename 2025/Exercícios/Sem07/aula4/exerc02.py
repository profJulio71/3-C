"""
lista = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]
Com a mesma lista, diga quais deles são pares.
"""

numeros = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]

# pares é um variável para armazenar os números pares
# numero variável de contagem
pares = [numero for numero in numeros if numero % 2 == 0]

# Exibindo os números pares
print("Os números pares são:\n",pares)