"""
5. Crie uma função chamada calcular_mediaque receba três números como parâmetros e retorne
a média aritmética desses números.
"""

# Função que calcula a média de três números
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Programa principal
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

media = calcular_media(a, b, c)
print(f"A média dos números é: {media:.2f}")