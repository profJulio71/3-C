"""
7. Faça uma função que recebe um númeroe retorna True, se ele for par, ou False, se ele for ímpar.
"""

# Função que verifica se um número é par ou ímpar
def verificar_par_ou_impar(numero):
    return numero % 2 == 0  # Retorna True se o número for par, False se for ímpar

# Programa principal
n = int(input("Digite um número: "))

if verificar_par_ou_impar(n):
    print(f"{n} é par.")
else:
    print(f"{n} é ímpar.")
