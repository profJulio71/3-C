"""
Crie uma tupla chamada nomes com alguns nomes de pessoas. Converta a tupla em uma lista
e adicione um novo nome. Em seguida, converta a lista de volta para uma tupla e imprima.
"""

# Passo 1: Criar a tupla
nomes = ('João', 'Júlio', 'Pedro')

# Passo 2: Converter para lista
nomes_lista = list(nomes)

# Passo 3: Adicionar um novo nome
nomes_lista.append('Rafaela')

# Passo 4: Converter de volta para tupla
nomes = tuple(nomes_lista)

# Passo 5: Imprimir a nova tupla
print(nomes)