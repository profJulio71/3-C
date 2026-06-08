"""
Você tem uma lista de produtos e seus preços.
Crie uma função chamada calcular_totalque aceite a lista de preços e retorne o preço total dos produtos.
precos= [10.5, 5.2, 8.0, 12.99]
"""

def calcular_total(precos):
    return sum(precos)

# Exemplo de uso
precos = [10.5, 5.2, 8.0, 12.99]
total = calcular_total(precos)
print(f"Total: R$ {total:.2f}")