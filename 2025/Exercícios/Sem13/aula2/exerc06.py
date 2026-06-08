"""
Crie um dicionário com pares chave-valor, representando o mapeamento de números de 1 a 5 para seus quadrados.
"""

print("Programa que exibe um dicionário com pares chave-valor, representando o mapeamento de números de 1 a 5 para seus quadrados.\n")
quadrados = {x: x**2 for x in range(1, 6)}

"""
range(1, 6)
    Gera os números de 1 a 5. (O range vai até um antes do 6.)
for x in range(1, 6)
    Isso significa: "para cada número x entre 1 e 5..."
{x: x**2 ...}
    Cria um par chave-valor no dicionário.
    x será a chave
x**2 será o valor associado a essa chave
"""
# Exibe o dicionário
print("Dicionário de números e seus quadrados:")
# print(quadrados)
for chave, valor in quadrados.items():
    print(f"{chave}² = {valor}")
"""
Laço for que percorre todos os pares chave-valor de um dicionário, quadrados.items() retorna
uma lista de tuplas, onde cada tupla contém: a chave (número de 1 a 5) e o valor (o quadrado
da chave)
"""