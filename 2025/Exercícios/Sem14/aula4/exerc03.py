"""
Crie dois conjuntos, conjunto1 e conjunto2, cada um com alguns elementos. Em seguida,
crie um novo conjunto chamado uniao contendo todos os elementos dos dois conjuntos.
"""

# Criando dois conjuntos com alguns elementos
conjunto1 = {11, 33, 55, 77}
conjunto2 = {22, 44, 66, 77}

# Criando um novo conjunto chamado 'uniao' contendo todos os elementos dos dois conjuntos
uniao = conjunto1.union(conjunto2)

# Exibindo os conjuntos e a união
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
print("União dos conjuntos:", uniao)