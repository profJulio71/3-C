"""
Gere uma lista dos quadrados dos números de 1 a 10 e armazene em um dicionário em que
as chaves são os números,e os valores são seus quadrados. Use compreensão de lista.
"""

print('Programa que cria uma lista de tuplas (número, quadrado) usando compreensão de lista.')
# Cria uma lista de tuplas (número, quadrado) usando compreensão de lista
lista_quadrados = [(x, x**2) for x in range(1, 11)]
"""
Essa linha cria uma lista de tuplas, onde cada tupla contém:
Um número x de 1 a 10
O quadrado desse número (x**2)

for x in range(1, 11)
Gera números de 1 a 10 (o 11 não é incluído).
Cada valor é armazenado temporariamente na variável x.
(x, x**2)
Cria uma tupla com dois elementos:
O número x (como chave).
Seu quadrado x**2 (como valor).
[(x, x**2) for x in range(1, 11)]
Isso é uma compreensão de lista.
Gera uma lista com todos os pares (x, x²) para x de 1 a 10.
"""

# Converte a lista de tuplas em um dicionário
dicionario_quadrados = dict(lista_quadrados)
"""
Essa linha cria um dicionário chamado dicionario_quadrados a partir da lista chamada lista_quadrados.
"""
# Exibe o dicionário
print("Dicionário de quadrados de 1 a 10:")
for chave, valor in dicionario_quadrados.items():
    print(f"{chave}² = {valor}")