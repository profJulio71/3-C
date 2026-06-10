"""
numeros = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]
Da lista acima, transforme todos os elementos em string.
"""

numeros = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]

# Transformando todos os elementos em string
numeros_como_strings = [str(numero) for numero in numeros]

print(numeros_como_strings)