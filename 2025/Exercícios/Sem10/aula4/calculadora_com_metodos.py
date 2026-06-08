# Funções da calculadora
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

# Função principal
def calculadora():
    print("Calculadora Simples")
    while True:
        a = float(input("\nDigite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        b = float(input("Digite o segundo número: "))

        if operador == '+':
            resultado = somar(a, b)
        elif operador == '-':
            resultado = subtrair(a, b)
        elif operador == '*':
            resultado = multiplicar(a, b)
        elif operador == '/':
            resultado = dividir(a, b)
        else:
            resultado = "Operador inválido!"

        print(f"Resultado: {resultado}")

        c = input("\nDeseja realizar novo calculo? (s/n): ").strip().lower()
        if c == 'n':
            break

# Executa a calculadora
calculadora()