"""
Crie uma lista contendo os números de 1 a 20, mas substitua os múltiplos de 3 por "Fizz"
e os múltiplos de 5 por "Buzz". Use compreensão de lista.
"""

print('Programa que cria uma lista contendo os números de 1 a 20, mas substitua\n'
      'os múltiplos de 3 por "Fizz" e os múltiplos de 5 por "Buzz". Use compreensão de lista.')

lista_fizzbuzz = [
    "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x
    for x in range(1, 21)
]
"""
for x in range(1, 21)
Gera os números de 1 até 20 (o 21 não é incluído).
Cada número é armazenado temporariamente na variável x.
"Fizz" if x % 3 == 0
Se o número for divisível por 3, retorna "Fizz".
else "Buzz" if x % 5 == 0
Se não for divisível por 3, mas for divisível por 5, retorna "Buzz".
else x
Se não for divisível por 3 nem por 5, retorna o próprio número x.
"""

print(lista_fizzbuzz)