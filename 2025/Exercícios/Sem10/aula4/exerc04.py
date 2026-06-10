"""
4. Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2).
"""

# Função que calcula a área de um triângulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Programa principal
b = float(input("Digite a base do triângulo: "))
h = float(input("Digite a altura do triângulo: "))

area = calcular_area_triangulo(b, h)
print(f"A área do triângulo é: {area}")
