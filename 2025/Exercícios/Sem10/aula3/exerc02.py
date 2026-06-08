"""
2. Faça uma função que recebe o valor do raio de um círculo e retorna o valor do comprimento
 de sua circunferência C = 2*pi*r.
"""

import math

# Função que calcula o comprimento da circunferência
def comprimento_circunferencia(raio):
    # Fórmula C = 2 * pi * r
    comprimento = 2 * math.pi * raio
    return comprimento

# Programa principal
raio = float(input("Digite o valor do raio do círculo: "))
resultado = comprimento_circunferencia(raio)
print(f"O comprimento da circunferência com raio {raio} é {resultado:.2f}")
