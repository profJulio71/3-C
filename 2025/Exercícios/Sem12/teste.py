# Criando um dicionário
dados = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo'
}

# Acessando um valor usando o método get()
nome = dados.get('nome')  # Retorna 'João'
print(nome)

# Tentando acessar uma chave que não existe, retornando None
profissao = dados.get('profissao')  # Retorna None
print(profissao)

# Usando um valor padrão caso a chave não exista
profissao = dados.get('profissao', 'Desempregado')  # Retorna 'Desempregado'
print(profissao)

print("*******")
meu_dic = {'a': 1,'b': 2, 'c':3}
valor = meu_dic.get('b', 0)
print(valor)
