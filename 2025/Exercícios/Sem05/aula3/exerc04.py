lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Busque o elemento que está no índice 5 da lista.
print(f"\nO valor do índice 5 da lista é:\n{lista[5]}")

# Qual é o tamanho da lista?
print(f"\nO tamanho da lista é:\n{len(lista)}")

# Qual é o valor máximo da lista?
print(f"\nO valor máximo da lista é:\n{max(lista)}")

# Qual é o valor mínimo da lista?
print(f"\nO valor máximo da lista é:\n{min(lista)}")

# Como obter o resultado [4, 5]?
i1 = lista.index(4)
print(f"\nO índice de 4 é: {i1}")
i2 = lista.index(5)
print(f"\nO índice de 5 é: {i2}")
print(f"\nOs valores dos índices acima são: [{i1}, {i2}]")