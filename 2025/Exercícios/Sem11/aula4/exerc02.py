"""
Você tem uma lista de temperaturas em graus Celsius.
Crie uma função chamada converter_para_fahrenheitque aceite a lista de temperaturas e retorne uma nova lista com as temperaturas convertidas para Fahrenheit.
temperaturas_celsius= [20, 25, 30]
Dica:
C = (F –32) X 5/9
"""

def converter_para_fahrenheit(temperaturas_celsius):
    return [(c * 9/5) + 32 for c in temperaturas_celsius]

# Exemplo de uso
temperaturas_celsius = [20, 25, 30]
temperaturas_fahrenheit = converter_para_fahrenheit(temperaturas_celsius)

print(temperaturas_fahrenheit)