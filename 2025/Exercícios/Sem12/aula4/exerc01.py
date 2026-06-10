"""
1. Contagem de palavras:
Crie uma função que recebe uma string como entrada e retorna um
dicionário com a contagem de cada palavra da string.
frase_exemplo = "python é uma linguagem de programação poderosa e versátil"
"""


def contar_palavras(frase):
    # Converte a frase para minúsculas e divide em palavras
    palavras = frase.lower().split()

    # Dicionário para armazenar a contagem das palavras
    contagem = {}

    # Conta cada palavra na lista
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem


# Exemplo de uso
frase_exemplo = "python é uma linguagem de programação poderosa e versátil"
resultado = contar_palavras(frase_exemplo)

# Exibir o resultado
print(resultado)