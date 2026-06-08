"""
Dada a tupla notas = (7, 8, 6, 9, 5), crie uma nova tupla chamada notas_ajustadas,
em que cada elemento seja a nota acrescida de 1 ponto. Imprima a nova tupla.
"""

print('Programa que cria uma nova tupla com as notas \najustadas em 1 ponto e imprime a nova tupla.')
notas = (7, 8, 6, 9, 5)
notas_ajustadas = tuple(nota + 1 for nota in notas)
print(notas_ajustadas)