"""
6. Classificação de palavras:
Implemente uma função que recebe uma lista de palavras e retorna um
dicionário no qual as chaves são o comprimento das palavras e os valores
são listas de palavras com aquele comprimento.
lista_palavras_exemplo = ['python', 'java', 'ruby', 'c', 'javascript', 'swift']
"""

def classificar_palavras_por_comprimento(lista_palavras):
    # Dicionário para armazenar as palavras classificadas por comprimento
    classificacao = {}

    # Itera sobre a lista de palavras
    for palavra in lista_palavras:
        comprimento = len(palavra)  # Obtém o comprimento da palavra

        # Se o comprimento já existe no dicionário, adiciona a palavra à lista
        if comprimento in classificacao:
            classificacao[comprimento].append(palavra)
        else:
            # Se o comprimento não existir no dicionário, cria uma nova entrada
            classificacao[comprimento] = [palavra]

    return classificacao

# Exemplo de uso
lista_palavras_exemplo = ['python', 'java', 'ruby', 'c', 'javascript', 'swift', 'alunosdeprogramação']
resultado = classificar_palavras_por_comprimento(lista_palavras_exemplo)

# Exibir o resultado
print(resultado)