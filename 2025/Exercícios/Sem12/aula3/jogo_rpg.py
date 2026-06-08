"""
Imagine que você está jogando um jogo de RPG (role-playing game), em que os jogadores têm inventários
para armazenar itens como armas, poções, armaduras etc. Você conseguiu acessar o dicionário do seu perfil
e quer fazer algumas alterações para trapacear no jogo.
inventario_jogador = {'armas': 3, 'poções': 5, 'armaduras': 2, 'moedas': 100, energia: [2, 1, 5]}
No dicionário acima, aumente o número de moedas para 500.
Imprima o valor de armas que você tem.
Apague a chave “armaduras”.
Insira ‘armaduras_poderosas': 10.
Acesse e substitua a energia 1 por 3.
"""
inventario_jogador = {'armas': 3, 'poções': 5, 'armaduras': 2, 'moedas': 100, 'energia': [2, 1, 5]}

# Aumentar o número de moedas para 500
inventario_jogador['moedas'] = 500

# Imprimir o valor de armas que você tem
print(f"Você tem {inventario_jogador['armas']} armas.")

# Apagar a chave “armaduras”
del inventario_jogador['armaduras']

# Inserir ‘armaduras_poderosas': 10
inventario_jogador['armaduras_poderosas'] = 10

# Acessar e substituir a energia 1 por 3
inventario_jogador['energia'][1] = 3

print(inventario_jogador)