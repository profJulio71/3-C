"""
Você está desenvolvendo um programa meteorológico e precisa converter as temperaturas de uma lista de graus Celsius
para Kelvin.
Crie uma função chamada converter_para_kelvinque aceite a lista de temperaturas em graus Celsius e imprima cada
temperatura convertida para Kelvin, junto com seu índice.
Dica: A fórmula de conversão de Celsius para Kelvin é K = C + 273.15, em que K é a temperatura em Kelvin e C é a
temperatura em graus Celsius.
temperaturas_celsius= [25, 30, 15, 10]
"""

def converter_para_kelvin(temperaturas_celsius):
    for indice, celsius in enumerate(temperaturas_celsius):
        kelvin = celsius + 273.15
        print(f"Temperatura {indice}: {celsius}°C = {kelvin:.2f} K")

# Exemplo de uso
temperaturas_celsius = [25, 30, 15, 10]
converter_para_kelvin(temperaturas_celsius)