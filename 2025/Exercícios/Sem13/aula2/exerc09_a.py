"""
Utilizando compreensão de dicionário, mapeie os números de 1 a 5 para "par" se forem pares, e "ímpar" se forem ímpares.
"""

print('Programa que utiliza compreensão de dicionário, mapeie os números de 1 a 5 para "par" se forem pares, e "ímpar" se forem ímpares.\n')
classificacao = {x: "par" if x % 2 == 0 else "ímpar" for x in range(1, 6)}
"""
for x in range(1, 6)
Gera os números de 1 até 5 (o 6 não é incluído).
Cada número é representado pela variável x.
"par" if x % 2 == 0 else "ímpar"
Isso é uma expressão condicional (também chamada de operador ternário).
Avalia se o número x é par usando x % 2 == 0:
Se for verdadeiro, retorna "par".
Caso contrário, retorna "ímpar".
{x: ... for x in ...}
A estrutura {chave: valor for item in iterable} cria um dicionário por compreensão.
Aqui, x é a chave, e "par" ou "ímpar" é o valor.
"""
# Separa os números em listas diferentes com base na classificação
pares = [chave for chave, valor in classificacao.items() if valor == "par"]
impares = [chave for chave, valor in classificacao.items() if valor == "ímpar"]
"""
classificacao.items()
Isso retorna todos os pares chave-valor do dicionário classificacao como tuplas.
Exemplo (considerando que classificacao foi criado assim:
{1: "ímpar", 2: "par", 3: "ímpar", 4: "par", 5: "ímpar"}):

for chave, valor in classificacao.items()
Esse for percorre cada par do dicionário.
A variável chave recebe o número (por exemplo, 3) e valor recebe a string correspondente (por exemplo, "ímpar").
if valor == "ímpar"
Este filtro garante que só os itens com valor "ímpar" serão incluídos na nova lista.
chave for ...
Isso indica que a lista vai conter apenas as chaves (números ímpares, no caso).
"""

# Exibe os resultados
print("Números ímpares:", impares)
print("Números pares:", pares)