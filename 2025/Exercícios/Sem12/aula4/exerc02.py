"""
2. Calculadora de notas:
Crie uma função que recebe um dicionário de notas de alunos e
retorna a média da turma.
notas_alunos = {'Alice': 90, Bruno': 85, Carlos': 92}
"""

def calcular_media(notas):
    # Soma todas as notas e divide pelo número de alunos
    total_notas = sum(notas.values())  # Soma das notas
    quantidade_alunos = len(notas)     # Número de alunos
    media = total_notas / quantidade_alunos  # Cálculo da média
    return media

# Exemplo de uso
notas_alunos = {'Alice': 90, 'Bruno': 85, 'Carlos': 92}
media_turma = calcular_media(notas_alunos)

# Exibir o resultado
print(f"Média da turma: {media_turma:.2f}")