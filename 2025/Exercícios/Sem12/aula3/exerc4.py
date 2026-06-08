# Dicionário com frutas e seus preços
frutas_preco = {
    'maçã': 2.5,
    'banana': 1.0,
    'uva': 3.0,
    'morango': 4.5,
    'laranja': 2.0,
    'abacaxi': 5.0,
    'kiwi': 3.5,
    'melancia': 6.0,
    'pêssego': 4.0,
    'manga': 3.8,
    'melao': 5.4
}

"""
Imprimir o dicionário de frutas e seus preços
for fruta, preco in frutas_preco.items():
    print(f'{fruta}: R${preco:.2f}')
"""

# 5. Qual o valor do abacaxi? Mostre o valor da chave “abacaxi”.

valor_abacaxi = frutas_preco['abacaxi']
print(f'O valor do abacaxi é: R$ {valor_abacaxi:.2f}')

#6. Qual o valor do melão? Mostre o valor da chave “melão”.
valor_melao = frutas_preco['melao']
print(f'O valor do melão é: R$ {valor_melao:.2f}')

# Atualizando o valor do kiwi


frutas_preco['kiwi'] = 4.0

# 7. O preço do kiwi foi alterado para 4. Altere o valor da chave
# “kiwi” no dicionário do exercício anterior para 4.
# Imprimir o dicionário atualizado
for fruta, preco in frutas_preco.items():
    print(f'{fruta}: R$ {preco:.2f}')

# 8. O estoque de manga acabou. Apague a chave “manga” do
# dicionário de frutas.

# Removendo a chave "manga" do dicionário
del frutas_preco['manga']

# Imprimir o dicionário atualizado

for fruta, preco in frutas_preco.items():
    print(f'{fruta}: R$ {preco:.2f}')

# Imprimir o dicionário de frutas e seus preços
print("\n")
for fruta, preco in frutas_preco.items():
    print(f'{fruta}: R$ {preco:.2f}')

# 9. Acabou de chegar no estoque a goiaba ao preço de 2.8.
# Insira a chave “goiaba” com valor 2.8.

frutas_preco["goiaba"] = 2.8

#Imprimir o dicionário de frutas e seus preços
for fruta, preco in frutas_preco.items():
    print(f'{fruta}: R${preco:.2f}')