"""
2.
Os alunos de uma escola têm notas em diferentes disciplinas.
Crie uma função chamada calcular_mediaque aceite uma lista de
notas e retorne a média.
notas_alunos= [8, 7, 5, 9, 6]
"""

def calcular_media(notas):
    if len(notas) == 0:
        return 0  # Evita divisão por zero
    return sum(notas) / len(notas)

notas_alunos = [8, 7, 5, 9, 6]
media = calcular_media(notas_alunos)
print(f"Média das notas: {media}")