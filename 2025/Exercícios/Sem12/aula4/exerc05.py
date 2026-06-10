"""
5. Pesquisa de livros:
Crie um programa que simula um catálogo de livros usando um dicionário.
Permita que o usuário pesquise livros pelo título.
catalogo_livros = {'Python Cookbook': 'Livro sobre Python', 'Java
Programming': 'Livro sobre Java’}
"""

def pesquisar_livro(catalogo, titulo):
    # Pesquisa o livro pelo título
    if titulo in catalogo:
        return catalogo[titulo]  # Retorna a descrição do livro
    else:
        return "Livro não encontrado."  # Caso o livro não esteja no catálogo

# Catálogo de livros
catalogo_livros = {
    'Python Cookbook': 'Livro sobre Python',
    'Java Programming': 'Livro sobre Java',
    'A Culpa é das Estrelas': 'Livro sobre romance'
}

# Solicitar ao usuário para pesquisar um livro
titulo_pesquisa = input("Digite o título do livro que deseja pesquisar: ")

# Chamar a função para pesquisar o livro
descricao = pesquisar_livro(catalogo_livros, titulo_pesquisa)

# Exibir o resultado
print(descricao)