"""
Dado o conjunto animais = {'cachorro', 'gato', 'pássaro'}, crie um novo conjunto chamado animais_domesticos
com apenas os animais que são domésticos. Imprima o novo conjunto.
"""

# Conjunto original
animais = {'cachorro', 'gato', 'pássaro'}

# Lista de animais domésticos conhecidos
domesticos = {'cachorro', 'gato', 'pássaro', 'peixe', 'coelho'}

# Criando o novo conjunto com apenas os animais domésticos
animais_domesticos = animais.intersection(domesticos)

# Imprimindo o novo conjunto
print("Animais domésticos:", animais_domesticos)