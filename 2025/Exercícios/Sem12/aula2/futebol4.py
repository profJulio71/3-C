"""
Acesse o time “Palmeiras” nos dois dicionários.
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

# Acessando o time "Palmeiras" nos dois dicionários

# No dicionário times_futebol
if "Palmeiras" in times_futebol:
    print(f"\nNo dicionário 'times_futebol', o time Palmeiras tem {times_futebol['Palmeiras']} torcedor(es).")
else:
    print("\nNo dicionário 'times_futebol', o time Palmeiras não foi encontrado.")

# No dicionário quantidade_times
for quantidade, times in quantidade_times.items():
    if "Palmeiras" in times:
        print(f"No dicionário 'quantidade_times', o time Palmeiras tem {quantidade} torcedor(es).")