"""
Crie um programa que determine se um número fornecido pelo usuário
é primo ou não, usando um loop for para verificar divisores.
"""

# Solicita o número ao usuário
numero = int(input("Digite um número inteiro maior que 1: "))

# Verifica se o número é válido
if numero <= 1:
    print("Números menores ou iguais a 1 não são primos.")
else:
    eh_primo = True  # Assume que é primo até provar o contrário

    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break  # Não precisa continuar se já encontrou um divisor

    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")