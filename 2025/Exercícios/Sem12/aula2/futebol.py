"""
Faça uma pesquisa, na sala de aula, com todos os estudantes anotando o time de futebol de preferência.
"""

def coletar_times_preferidos():
    quantidade_alunos = int(input("Quantos alunos serão entrevistados? "))
    times = []

    for i in range(quantidade_alunos):
        time = input(f"Digite o time preferido do aluno {i + 1}: ").strip().title()
        times.append(time)

    return times

# Coletar os dados
times_preferidos = coletar_times_preferidos()

# Exibir os resultados
print("\nTimes preferidos pelos alunos:")
for indice, time in enumerate(times_preferidos, start=1):
    print(f"Aluno {indice}: {time}")