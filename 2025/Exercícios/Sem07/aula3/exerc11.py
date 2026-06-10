""" Agora, usando o método max(), faça um programa que imprima os três
maiores números de uma lista. """

def tres_maiores(lista):
    maiores = []

    # Repete o processo três vezes para encontrar os três maiores
    c = 0
    while c < 3:
        maior = max(lista)  # Encontra o maior número
        maiores.append(maior)
        lista.remove(maior)  # Remove o maior número da lista
        c += 1
    """for _ in range(3):
        maior = max(lista)  # Encontra o maior número
        maiores.append(maior)
        lista.remove(maior)  # Remove o maior número da lista
    """

    return maiores


# Exemplo de lista
numeros = [10, 23, 5, 19, 32, 77, 4, 9, 18]

# Chama a função e imprime os três maiores números
print("Os três maiores números são:", tres_maiores(numeros))