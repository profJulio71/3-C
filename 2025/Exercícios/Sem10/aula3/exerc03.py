"""
3. Crie uma função chamada concatenar_palavras, que receba duas stringscomo parâmetros e retorna
a concatenação dessas duas strings, separadas por um espaço.
"""

# Função que concatena duas palavras com um espaço entre elas
def concatenar_palavras(palavra1, palavra2):
    return palavra1 + " " + palavra2

# Programa principal
p1 = input("Digite a primeira palavra: ")
p2 = input("Digite a segunda palavra: ")

resultado = concatenar_palavras(p1, p2)
print("Resultado da concatenação:", resultado)