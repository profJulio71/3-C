"""
Considere um sistema de registro de alunos em uma escola. Cada aluno é representado por um registro
contendo as seguintes informações em uma tupla: nome, idade, média das notas e lista de disciplinas cursadas.

1.
Use a lista chamada registros_alunos, que contém tuplas representando três alunos. Cada tupla inclui o nome do aluno, sua idade, a média das notas e a lista de disciplinas cursadas.
registros_alunos= [
("Alice", 18, 8.5, ["Matemática", "História"]),
("Bob", 17, 7.2, ["Inglês", "Ciências"]),
("Charlie", 16, 6.8, ["Matemática", "Inglês"])]
"""

print('Programa que cria uma lista de alunos e imprime a lista.')
registros_alunos = [
    ("Alice", 18, 8.5, ["Matemática", "História"]),
    ("Bob", 17, 7.2, ["Inglês", "Ciências"]),
    ("Charlie", 16, 6.8, ["Matemática", "Inglês"])
]

"""
2. Crie uma função chamada imprimir_alunos_aprovadosque recebe a lista de registros de alunos
e imprime apenas os nomes dos alunos que têm uma média de notas igual ou superior a 7,0.
"""
def imprimir_alunos_aprovados(registros_alunos):
    for aluno in registros_alunos:
        if aluno[2] >= 7.0:
            print(aluno[0])

print("Parte 2")
imprimir_alunos_aprovados(registros_alunos)

"""
3. Crie uma função chamada encontrar_aluno_disciplina que recebe a lista de registros de alunos e o
nome de uma disciplina. A função deve retornar uma lista contendo os nomes dos alunos que cursaram
a disciplina fornecida. 
"""
def encontrar_aluno_disciplina(registros_alunos, disciplina):
    alunos_disciplina = []
    for aluno in registros_alunos:
        if disciplina in aluno[3]:
            alunos_disciplina.append(aluno[0])
    return alunos_disciplina

d = "Matemática"
print("Parte 3")
disciplina = encontrar_aluno_disciplina(registros_alunos, d)
print('Alunos do curso de', d, '!')
print (disciplina)

"""
4. Utilize a função imprimir_alunos_aprovados para imprimir os nomes dos alunos aprovados na lista registros_alunos.
"""
print("\n")
print("Parte 4")
imprimir_alunos_aprovados(registros_alunos)

"""
5. Utilize a função encontrar_aluno_disciplina para encontrar os alunos que cursaram a disciplina de "Matemática"
e imprima o resultado.
"""
print("\n")
print("Parte 5")
def encontrar_aluno_disciplina(registros, disciplina):
    for nome, idade, media, disciplinas in registros:
        if disciplina in disciplinas:
            print(nome)

# Chamada da função para encontrar alunos que cursam "Matemática"
encontrar_aluno_disciplina(registros_alunos, "Matemática")
