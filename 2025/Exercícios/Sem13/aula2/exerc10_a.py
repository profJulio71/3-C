"""
Crie um dicionário em que as chaves são os números de 1 a 10, e os valores são Truese o
número for par, e Falsese o número for ímpar.
"""

print('Programa que cria um dicionário em que as chaves são os números de 1 a 10, e os valores')
print('são True se o número for par, e False se o número for ímpar.')
par_ou_nao = {x: x % 2 == 0 for x in range(1, 11)}

# Separa os números em listas diferentes com base no valor booleano
pares = [chave for chave, valor in par_ou_nao.items() if valor]
impares = [chave for chave, valor in par_ou_nao.items() if not valor]

# Exibe os resultados
print("Lista de números ímpares:", impares)
print("Lista de números pares:", pares)