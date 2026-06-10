"""
Gere uma lista com os números de 1 a 50, excluindo os divisíveis por 5.
"""

print("Programa que exibe uma lista dos números de 1 a 50, excluindoos divisíveis por 5.\n")
numeros = [x for x in range(1, 51) if x % 5 != 0]

"""
    range(1, 51)
        Gera os números de 1 até 50 (o 51 não é incluído, porque o range vai até um antes do limite superior).
    x for x in range(...)
        Isso é uma compreensão de lista, que cria uma nova lista iterando sobre cada valor x no intervalo de 1 a 50.
    if x % 5 != 0
        Esse filtro dentro da compreensão de lista diz:
        “Inclua x apenas se ele NÃO for divisível por 5”.
        O operador % (módulo) retorna o resto da divisão de x por 5.
    Se x % 5 == 0, o número é divisível por 5 e será excluído da lista.
"""

# Exibe a lista
print("Números de 1 a 50, excluindo os divisíveis por 5:")
print(numeros)