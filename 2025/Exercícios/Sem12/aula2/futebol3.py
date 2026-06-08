"""
Agora, crie um dicionário quantidade_times,
cuja chave é a quantidade e o valor, o nome do time.
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

# Criar o dicionário quantidade_times
quantidade_times = {}
for time, quantidade in times_futebol.items():
    if quantidade in quantidade_times:
        quantidade_times[quantidade].append(time)
    else:
        quantidade_times[quantidade] = [time]

# Exibir o resultado
print("\nQuantidade de torcedores por time (invertido):")
for quantidade, times in quantidade_times.items():
    print(f"{quantidade} torcedor(es): {', '.join(times)}")