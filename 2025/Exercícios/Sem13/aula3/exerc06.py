"""
Reescreva os exercícios de 1 a 5 sem usar compreensão de lista.
"""
print('Programa que cria uma lista contendo os números de 1 a 5, mas substitua\n'
      'os múltiplos de 3 por "Fizz" e os múltiplos de 5 por "Buzz". Sem usar a compreensão de lista.')
resultado = []

for x in range(1, 6):
    if x % 3 == 0:
        resultado.append("Fizz")
    elif x % 5 == 0:
        resultado.append("Buzz")
    else:
        resultado.append(x)

print(resultado)