"""
lista = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]
Faça um programa que olhe todos os itens da lista acima e diga
quantos deles são ímpares.
"""

lista = [8, 20, 50, 40, 1, 43,
         32, 29, 47, 12, 9, 4]       # declaração e atribuição de valores na lista
contador = 0                         # Declaração da variável e atribuição de valor
for numero in lista:                 # Laço for, percorre a lista
    if numero % 2 != 0:              # Se resto da divisão por 2 diferente de zero, entra na condição
        contador += 1                # incrementa valor 1 na variável
print(f'A quantidade de números'
      f' ímpares é: {contador}')     # Imprime valor da variável