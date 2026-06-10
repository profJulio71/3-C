"""
Crie um programa que calcule a soma dos múltiplos de 3 entre 1 e 100
usando um loop for.
"""

soma = 0

for numero in range(1, 101):
    if numero % 3 == 0:
        soma += numero

print("A soma dos múltiplos de 3 entre 1 e 100 é:", soma)