"""
numeros = ['8', '9', '45', '26', '12']
Pegue a lista gerada no exercício anterior e transforme cada um dos
itens dessa lista em um float.
"""

# Lista com os números digitados (como strings)
numeros = ['8', '9', '45', '26', '12']

# Transformando cada item da lista em float
numeros_float = [float(numero) for numero in numeros]

print("Lista com os números como floats:", numeros_float)