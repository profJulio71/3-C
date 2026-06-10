"""
Crie um dicionário em que as chaves são os números de 1 a 10, e os valores são True se o
número for par, e False se o número for ímpar.
"""

print('Programa que cria um dicionário em que as chaves são os números de 1 a 10, e os valores'
      'são True se o número for par, e False se o número for ímpar.\n')
par_ou_nao = {x: True if x % 2 == 0 else False for x in range(1, 11)}

# Imprime os pares chave-valor
print("Números de 1 a 10: par (True) ou ímpar (False)")
for chave, valor in par_ou_nao.items():
    print(f"{chave} → {valor}")