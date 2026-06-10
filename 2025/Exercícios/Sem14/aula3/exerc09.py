"""
Crie uma tupla chamada num_tupla com números de 1 a 10. Imprima os números pares da tupla.
"""

print('Programa que imprime os pares de uma tupla de 1 a 10.')
# Criando a tupla com números de 1 a 10
num_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Imprimindo apenas os números pares
pares = tuple(num for num in num_tupla if num % 2 == 0)

print(pares)