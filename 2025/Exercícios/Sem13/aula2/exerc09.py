"""
Utilizando compreensão de dicionário, mapeie os números de 1 a 5 para "par" se forem pares, e "ímpar" se forem ímpares.
"""

print('Programa que utiliza compreensão de dicionário, mapeie os números')
print(' de 1 a 5, para "par" se forem pares, e "ímpar" se forem ímpares.\n')
par_ou_impar = {x: "par" if x % 2 == 0 else "ímpar" for x in range(1, 6)}

# Exibe os resultados
print("Classificação de par ou ímpar:")
for chave, valor in par_ou_impar.items():
    print(f"{chave} → {valor}")