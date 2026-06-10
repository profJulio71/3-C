"""
Crie dois conjuntos, conjunto_A e conjunto_B, com alguns elementos em comum. Crie um novo conjunto
chamado diferenca, contendo os elementos que estão em conjunto_Amas não estão em conjunto_B.
"""

# Criando os conjuntos
conjunto_A = {'a', 'b', 'c', 'd', 'e'}
conjunto_B = {'d', 'e', 'f', 'g', 'h'}

# Criando um novo conjunto com a diferença: elementos de A que não estão em B
diferenca = conjunto_A.difference(conjunto_B)
diferenca2 = conjunto_B.difference(conjunto_A)

# Imprimindo o resultado
print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)
print("\nDiferença (A - B):", diferenca)
print("Diferença (B - A):", diferenca2)