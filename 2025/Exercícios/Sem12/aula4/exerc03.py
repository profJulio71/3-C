"""
3. Contagem de caracteres:
Implemente uma função que conta a frequência de cada
caractere em uma string e retorna um dicionário.
texto_exemplo = "python"
"""


def contar_caracteres(texto):
    # Dicionário para armazenar a contagem de caracteres
    contagem = {}

    # Contagem de cada caractere
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    return contagem


# Exemplo de uso
texto_exemplo = "python"
resultado = contar_caracteres(texto_exemplo)

# Exibir o resultado
print(resultado)