"""
Os alunos de uma turma têm alturas diferentes.
Utilize enumeratepara imprimir a altura de cada aluno junto com seu índice.
alturas_alunos= [160, 175, 150, 180]
"""

alturas_alunos = [160, 175, 150, 180]

for indice, altura in enumerate(alturas_alunos):
    print(f"Aluno {indice}: {altura} cm")