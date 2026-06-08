"""
6. Faça uma função que recebe um nome e um horárioe imprime “Bom dia, [nome]”, caso seja antes de 12h;
“Boa Tarde, [nome]”, caso seja entre 12h e 18h; e “Boa noite, [nome]” caso seja após às 18h.
"""

# Função que exibe uma saudação com base no horário
def saudacao(nome, hora):
    if hora < 12:
        print(f"Bom dia, {nome}")
    elif 12 <= hora < 18:
        print(f"Boa tarde, {nome}")
    else:
        print(f"Boa noite, {nome}")

# Programa principal
nome_usuario = input("Digite seu nome: ")
while True:
    hora_atual = int(input("Digite a hora atual (0 a 23): "))

    # Verificando se a hora é válida
    if 0 <= hora_atual <= 23:
        saudacao(nome_usuario, hora_atual)
        break
    else:
        print("\nHora inválida!\nDigite um valor entre 0 e 23.\n")