"""
Crie um conjunto chamado alunos_matricula dos com alguns nomes de alunos.
Remova um aluno do conjunto e imprima o conjunto atualizado.
"""

# Criando o conjunto com alguns nomes de alunos
alunos_matriculados = {'ANA BEATRIZ', 'AXEL VINCENT', 'BEATRIZ PAULINO', 'CAROLINA VITÓRIA'}

print("Alunos matriculados:", alunos_matriculados)

# Removendo um aluno do conjunto (por exemplo, 'Carlos')
alunos_matriculados.remove('BEATRIZ PAULINO')

# Imprimindo o conjunto atualizado
print("Alunos matriculados (atualizado):", alunos_matriculados)