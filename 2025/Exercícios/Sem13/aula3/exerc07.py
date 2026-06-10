"""
Crie um dicionário com as letras de uma string como chaves,e o número de vezes
que cada letra aparece como valores.
"""

texto = "Gosto de estudar python!"

# Cria um dicionário vazio
contador_letras = {}


for letra in texto:
    if letra in contador_letras:
        contador_letras[letra] += 1
    else:
        contador_letras[letra] = 1

print(contador_letras)