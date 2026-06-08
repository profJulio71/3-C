"""
Crie um dicionário com o nome times_futebol, usando, como chave, o nome do time de futebol e, como valor,
a quantidade de estudantes que torcem por aquele time.
"""
def coletar_times_preferidos():
    quantidade_alunos = int(input("Quantos alunos serão entrevistados? "))
    times_futebol = {}

    for i in range(quantidade_alunos):
        time = input(f"Digite o time preferido do aluno {i + 1}: ").strip().title()

        if time in times_futebol:
            times_futebol[time] += 1
        else:
            times_futebol[time] = 1

    return times_futebol

# Coletar os dados
times_futebol = coletar_times_preferidos()

# Exibir o resultado
print("\nQuantidade de torcedores por time:")
for time, quantidade in times_futebol.items():
    print(f"{time}: {quantidade} estudante(s)")