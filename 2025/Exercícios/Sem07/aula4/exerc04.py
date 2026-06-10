"""
lista = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]
Da lista acima, crie uma nova lista copiando cada elemento em
ordem crescente. Obs.: não usar sorted().
"""

numeros = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]

# Criando uma nova lista copiando os elementos da lista original
numeros_copiados = numeros

# Laço de i=0 até o tamanho da lista.
for i in range(len(numeros_copiados)):
    # Encontrando o índice do menor elemento não ordenado
    menor_indice = i
    for j in range(i + 1, len(numeros_copiados)):
        if numeros_copiados[j] < numeros_copiados[menor_indice]:
            menor_indice = j
    # Troca o elemento atual com o menor encontrado
    numeros_copiados[i], numeros_copiados[menor_indice] = numeros_copiados[menor_indice], numeros_copiados[i]

# Exibindo a nova lista ordenada
print(numeros_copiados)