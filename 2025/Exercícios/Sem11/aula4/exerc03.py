"""
Os alunos de uma turma têm notas em diferentes disciplinas.
Crie uma função chamada verificar_aprovacao que aceite uma lista de notas e imprima se cada aluno foi
aprovado ou reprovado (nota >= 6).
notas_alunos= [7, 5, 8, 4, 6]
"""

def verificar_aprovacao(notas):
    for indice, nota in enumerate(notas):
        status = "Aprovado" if nota >= 6 else "Reprovado"
        print(f"Aluno {indice}: {status} (Nota: {nota})")

# Exemplo de uso
notas_alunos = [7, 5, 8, 4, 6]
verificar_aprovacao(notas_alunos)