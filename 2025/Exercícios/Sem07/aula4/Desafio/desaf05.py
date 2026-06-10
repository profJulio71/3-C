"""
Dado um dicionário de produtos e seus preços, utilize um loop for para
calcular o preço total da compra de uma lista de produtos fornecida.
"""

# Dicionário com produtos e preços
precos = {
    "maçã": 12.50,
    "banana": 9.20,
    "leite": 4.50,
    "pão": 12.00,
    "queijo": 55.50
}

# Lista de produtos comprados
carrinho = ["maçã", "leite", "pão", "banana", "banana", "queijo"]

# Calculando o total
total = 0.0

for produto in carrinho:
    if produto in precos:
        total += precos[produto]
    else:
        print(f"Produto '{produto}' não encontrado na lista de preços.")

print(f"Total da compra: R$ {total:.2f}")