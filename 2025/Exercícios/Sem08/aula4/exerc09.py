"""
Crie uma função que receba um número inteiro e retorne uma string que o
represente com separadores de milhares. Por exemplo, para o número 1234567,
a função deve retornar “1,234,567”.
"""

def formatar_com_separador_milhares(numero):
    # Utiliza a função format() para adicionar separadores de milhares
    return "{:,}".format(numero)

# Testando a função
numero = int(input("Digite um número inteiro: "))
resultado = formatar_com_separador_milhares(numero)
print(f"Número formatado: {resultado}")