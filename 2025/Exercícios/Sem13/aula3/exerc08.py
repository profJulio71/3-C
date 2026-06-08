"""
Utilizando compreensão de lista, crie uma lista de todas as palavras
com mais de cinco letras em uma frase.
"""

print('Programa que cria uma lista de todas as palavras'
'com mais de cinco letras em uma frase.')
frase = "Gosto de estudar Python na Escola Francisco Pereira da Silva"

# Divide a frase em palavras e filtra as que têm mais de 5 letras
palavras_grandes = [palavra for palavra in frase.split() if len(palavra) > 5]

print(palavras_grandes)