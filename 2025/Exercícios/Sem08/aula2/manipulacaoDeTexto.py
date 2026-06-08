"""
Exercício: Manipulação de texto
Você está construindo um sistema de gerenciamento de contatos.
Crie um programa que realize as seguintes tarefas:
a) Peça ao usuário para digitar seu nome completo.
b) Concatene “Olá,” com o nome fornecido e exiba o resultado.
c) Conte quantos caracteres existem no nome completo digitado e
exiba o resultado.
d) Peça ao usuário para digitar um sobrenome para procurar na
string do nome completo.
e) Verifique se o sobrenome fornecido está presente no nome
completo e exiba uma mensagem apropriada.
f) Exiba o nome completo em letras maiúsculas.
g) Substitua todas as ocorrências da vogal “a” na string do nome
completo pelo caractere ‘4’ e exiba o resultado.
"""
print("Sistema de gerenciamento de contatos")

# a) Solicita o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# b) Concatena “Olá,” com o nome e exibe
print("Olá, " + nome_completo)

# c) Conta e exibe o número de caracteres no nome completo
total_caracteres = len(nome_completo)
print(f"Seu nome completo tem {total_caracteres} caracteres (contando espaços).")

# d) Solicita um sobrenome para procurar no nome completo
sobrenome = input("Digite um sobrenome para procurar no nome completo: ")

# e) Verifica se o sobrenome está presente e exibe mensagem apropriada
if sobrenome.lower() in nome_completo.lower():
    print(f"O sobrenome '{sobrenome}' está presente no nome completo.")
else:
    print(f"O sobrenome '{sobrenome}' **não** foi encontrado no nome completo.")

# f) Exibe o nome completo em letras maiúsculas
print("Nome completo em maiúsculas:", nome_completo.upper())

# g) Substitui todas as ocorrências da letra 'a' por '4'
nome_modificado = nome_completo.replace("a", "4").replace("A", "4")
print("Nome com 'a' substituído por '4':", nome_modificado)