lista = [1, 3, 3, 5, 7, 9]
print(f"Os números são: {lista}")

# Remova o valor 3.
lista.remove(3)
print(f"\nRemovido primeiro valor 3\n {lista}")

# Remova o valor da posição (índice) 4
lista.pop(4)
print(f"\nRemovido o valor do índice 4\n {lista}")

# Mostre o valor que será removido da posição (índice) 3
print(f"\nO valor do índice 3 da lista é:\n{lista[3]}")
lista.pop(3)
print(f"\nRemovido o valor do índice 3\n {lista}")