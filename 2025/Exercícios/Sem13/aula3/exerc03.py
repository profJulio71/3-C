"""
Utilizando compreensão de lista, crie uma lista com o dobro dos números de 1 a 10, mas apenas para números ímpares.
"""

print('Programa que utiliza a compreensão de lista, Utilizando compreensão de lista,\n'
      'crie uma lista com o dobro dos números de 1 a 10, mas apenas para números ímpares.')
dobro_impares = [x * 2 for x in range(1, 11) if x % 2 != 0]
print(dobro_impares)