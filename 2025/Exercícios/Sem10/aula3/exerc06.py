"""
6. Faça uma função para cada operação matemática básica (soma, subtração, multiplicação e divisão).
As funções devem receber dois números e retornar o resultado da operação.
"""

# Função de soma
def somar(a, b):
    return a + b

# Função de subtração
def subtrair(a, b):
    return a - b

# Função de multiplicação
def multiplicar(a, b):
    return a * b

# Função de divisão
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Programa principal
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Soma: {somar(num1, num2)}")
print(f"Subtração: {subtrair(num1, num2)}")
print(f"Multiplicação: {multiplicar(num1, num2)}")
print(f"Divisão: {dividir(num1, num2)}")