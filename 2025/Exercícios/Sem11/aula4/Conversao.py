"""
Você está aprimorando seu programa meteorológico e deseja criar uma função chamada converter_temperaturas
Essa função aceita uma lista de temperaturas em Kelvin e outra lista de temperaturas em Fahrenheit.
A função deve imprimir cada temperatura convertida para Celsius, junto com seu índice.
"""
def converter_temperaturas(temperaturas_kelvin, temperaturas_fahrenheit):
    print("Temperaturas em Kelvin convertidas para Celsius:")
    for indice, k in enumerate(temperaturas_kelvin):
        celsius = k - 273.15
        print(f"Índice {indice}: {k} K = {celsius:.2f} °C")

    print("\nTemperaturas em Fahrenheit convertidas para Celsius:")
    for indice, f in enumerate(temperaturas_fahrenheit):
        celsius = (f - 32) * 5 / 9
        print(f"Índice {indice}: {f} °F = {celsius:.2f} °C")

# Exemplo de uso
temperaturas_kelvin = [300, 310, 290, 280]
temperaturas_fahrenheit = [68, 86, 59, 50]

converter_temperaturas(temperaturas_kelvin, temperaturas_fahrenheit)