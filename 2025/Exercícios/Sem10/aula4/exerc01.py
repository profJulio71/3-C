"""
1.
Escreva uma função que retorne o maiorde dois números.
"""

# Função que retorna o maior entre dois números
def maior_numero(a, b):
    return a if a > b else b

# Programa principal
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

maior = maior_numero(num1, num2)
print(f"O maior número é: {maior}")