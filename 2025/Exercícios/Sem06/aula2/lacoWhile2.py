# Cria uma lista
minha_lista = [1, 2, 3 , 4, 5]

# Peça para o usuário inserir um número inteiro
n = int(input('Digite um valor de 0 a 10: '))
resultado = n in minha_lista

# Imprime o resultado
print (f"O valor está na lista?", resultado) # Isso imprimirá true (verdadeiro), pois 3 está na lista