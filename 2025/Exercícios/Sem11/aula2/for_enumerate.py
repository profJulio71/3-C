frutas = ['maçã', 'banana', 'laranja']

for indice, valor in enumerate (frutas):
    print(f'Indice: {indice}, Valor: {valor}')

print('\n')
frase = "Python é incrível!"

for indice, letra in enumerate(frase, start=1):
    print(f'Índice: {indice}, Letra: {letra}')

print('\n')
pessoas = {'João': 25, 'Maria': 30, 'Pedro': 28}

for indice, (nome, idade) in enumerate(pessoas.items(), start=1):
    print(f'Índice: {indice}, Nome: {nome}, Idade: {idade} anos')


