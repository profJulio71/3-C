"""
3. Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado²).
"""

# Função que calcula a área de um quadrado
def calcular_area_quadrado(lado):
    return lado ** 2

# Programa principal
l = float(input("Digite o valor do lado do quadrado: "))
area = calcular_area_quadrado(l)

print(f"A área do quadrado de lado {l} é {area}")
print("A área do quadrado de lado",l, "é",area)