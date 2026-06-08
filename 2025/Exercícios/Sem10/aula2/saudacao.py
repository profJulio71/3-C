"""
Programa saudação com função.
"""

def saudacao(nome):
    mensagem = f"Olá, {nome}!\nBem vindo à nossa aula de Python."
    return mensagem
# Chamando a função
n = str(input("Digite o seu nome: "))
resultado = saudacao(n)
print(resultado)