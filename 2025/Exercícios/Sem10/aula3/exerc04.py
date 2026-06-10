"""
4. Crie uma função chamada verificar_parque receba um número como parâmetro e retorne True,
se o número for par, e False,em caso contrário.
"""

# Função que verifica se um número é par
def verificar_par(numero):
    return numero % 2 == 0

# Programa principal
n = int(input("Digite um número: "))

if verificar_par(n):
    print(f"O número {n} é par.")
else:
    print(f"O número {n} é ímpar.")