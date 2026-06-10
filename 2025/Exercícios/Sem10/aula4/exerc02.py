"""
2. Escreva uma função que receba dois números e retorne True, se o primeiro número for múltiplo do segundo.
"""

# Função que verifica se o primeiro número é múltiplo do segundo

def eh_multiplo(a, b):
    if b == 0:
        return False  # Evita divisão por zero
    return a % b == 0

# Programa principal
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if eh_multiplo(num1, num2):
    print(f"{num1} é múltiplo de {num2}")
else:
    print(num1," não é múltiplo de ",num2)
