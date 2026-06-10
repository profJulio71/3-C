"""
Crie uma função que receba uma frase como parâmetro e retorne a mesma
frase com as palavras invertidas. Por exemplo, “Olá Mundo” deve ser
transformado em “Mundo Olá”.
"""


def inverter_palavras(frase):
    # Divide a frase em uma lista de palavras
    palavras = frase.split()

    # Inverte a ordem das palavras
    palavras_invertidas = palavras[::-1]

    # Junta as palavras invertidas de volta em uma string
    frase_invertida = ' '.join(palavras_invertidas)

    return frase_invertida


# Testando a função
frase = input("Digite uma frase: ")
resultado = inverter_palavras(frase)
print("Frase com as palavras invertidas:", resultado)