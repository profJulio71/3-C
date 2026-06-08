"""
Gere um dicionário em que as chaves são os números de 1 a 10, e os valores são True se o
número for primo e False se não for. Use compreensão de dicionário.
"""

print('Programa que gera um dicionário em que as chaves são os números de 1 a 10, e os valores'
'são True se o número for primo e False se não for. Usando compreensão de dicionário.')
# Função simples para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Compreensão de dicionário
primos = {x: eh_primo(x) for x in range(1, 11)}

# Exibe o dicionário
print("Dicionário: número → é primo?")
for chave, valor in primos.items():
    print(f"{chave} → {valor}")