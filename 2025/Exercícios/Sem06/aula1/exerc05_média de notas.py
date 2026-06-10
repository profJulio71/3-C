"""
Exercício 5: Média das notas
Peça ao usuário que insira uma série de notas de estudantes (em uma escala de 0 a 10) até que eles
digitem um valor negativo.
Calculem e exibam a média das notas inseridas.
"""

print('''
Bem vindo ao programa que
calcula a média das notas
''')

notas = []
m, i = 0, 0

while True:
    n = float(input('Digite a {}a nota, para finalizar, digite -1: '.format(i + 1)))
    if n == -1:
        break
    notas.append(n)
    i += 1
print("As notas são:\n", notas)

i = 0

while(i < len(notas)):
    m = m + notas[i]
    i += 1
print('Média:',m / i,'\n')