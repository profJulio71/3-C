"""
Dado o conjunto letras = {'a', 'b', 'c', 'd'}, crie um novo conjunto chamado letras_vogais
contendo apenas as vogais do conjunto original. Imprima o novo conjunto.
"""

# Conjunto original
letras = {'a', 'b', 'c', 'd'}

# Conjunto com vogais para comparação
vogais = {'a', 'e', 'i', 'o', 'u'}

# Criando novo conjunto com apenas as vogais presentes em 'letras'
letras_vogais = {letra for letra in letras if letra in vogais}

# Imprimindo o novo conjunto
print("Letras vogais:", letras_vogais)