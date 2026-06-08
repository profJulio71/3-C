"""
Dado o conjunto pares = {2, 4, 6, 8, 10}, crie um novo conjunto chamado pares_multiplicado
sem que cada elemento seja o dobro dos elementos do conjunto original. Imprima o novo conjunto.
"""

# Conjunto original
pares = {2, 4, 6, 8, 10}

# Criando um novo conjunto com o dobro de cada elemento
pares_multiplicados = {x * 2 for x in pares}

# Imprimindo o novo conjunto
print("Conjunto original:", pares)
print("Conjunto com elementos multiplicados por 2:", pares_multiplicados)