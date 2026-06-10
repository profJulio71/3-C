"""
Crie uma lista com os números de 1 a 20. Transforme-a em um dicionário em que as chaves são
os números,e os valores são "par" ou "ímpar".Use compreensão de lista.
"""

print('Programa que cria uma lista com os números de 1 a 20. Transforme-a em um dicionário')
print('em que as chaves são os números,e os valores são "par" ou "ímpar".Use compreensão de lista.')
# Cria a lista de números de 1 a 20
numeros = list(range(1, 21))

# Usa compreensão de lista para criar lista de tuplas (número, "par"/"ímpar")
classificacao_lista = [(x, "par" if x % 2 == 0 else "ímpar") for x in numeros]

# Converte a lista de tuplas em dicionário
classificacao_dict = dict(classificacao_lista)

# Exibe o dicionário
print("Classificação dos números de 1 a 20:")
for chave, valor in classificacao_dict.items():
    print(f"{chave} → {valor}")