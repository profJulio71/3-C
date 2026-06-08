"""
Escreva um programa que receba uma palavra ou frase do usuário
e determine se ela é um palíndromo ou não. O programa deve
ignorar maiúsculas e minúsculas, bem como espaços em branco.

Um palíndromo é uma sequência de caracteres, como uma
palavra, frase ou número, que permanece a mesma quando
lida de trás para frente. Isso ocorre devido à simetria na
disposição dos caracteres.
"""


def verificar_palindromo(texto):
    # Remove espaços em branco e converte para minúsculas
    texto = texto.replace(" ", "").lower()

    # Verifica se a string é igual à sua reversa
    return texto == texto[::-1]


# Solicita uma palavra ou frase ao usuário
texto_usuario = input("Digite uma palavra ou frase: ")

# Verifica se é um palíndromo e imprime o resultado
if verificar_palindromo(texto_usuario):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")