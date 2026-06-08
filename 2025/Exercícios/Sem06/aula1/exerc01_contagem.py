""" Programa que peça ao usuário um número positivo.
    Em seguida, contem do 1 até esse número.
    Depois, contem de volta até 1, exibindo os números em cada contagem."""

n = int(input('Digite um número inteiro: '))  # Atribui a variável "n" o valor inteiro que o usuário digitar

c = 1                                         # Atribui a variável c o valor 1

print("contagem de ", c, "até", n)            # Imprime a mensagem de contagem crescente
while c <= n:                                 # Laço while que conta de N até 1
    print(c)                                  # Exibe a contagem
    c += 1                                    # Incrementa a variável c

print("contagem de ", n, "até 1")             # Imprime a mensagem de contagem decrescente
c -= 1                                        # Decrementa a variável c
while c >= 1:                                 # Laço while que conta de N até 1
    print(c)                                  # Exibe a contagem
    c -= 1                                    # Decrementa a variável c