"""
Programa que simule a partida Par ou Ímpar entre você e o computador.
"""
import random

print("Bem-vindo ao jogo Par ou Ímpar!")

while True:
    # Escolha do jogador
    escolha = input("Você quer PAR ou ÍMPAR? ").strip().lower() # .strip() é uma função que remove espaços em branco
    # .lower() é uma chamada de método que converte todos os caracteres maiúsculos da string.
    while escolha not in ["par", "ímpar", "impar"]:
        escolha = input("Escolha inválida. Digite PAR ou ÍMPAR: ").strip().lower()

    numero_jogador = int(input("Digite um número entre 0 e 10: "))

    # Gera um número aleatório entre 0 e 10 positivo
    numero_computador = random.randint(0, 10)

    print(f"Você escolheu {numero_jogador}")
    print(f"O computador escolheu {numero_computador}")

    soma = numero_jogador + numero_computador
    # resultado = "par" if soma % 2 == 0 else "ímpar"

    resultado = ""
    resto = soma % 2
    if resto == 0:
        resultado = "par"
    else:
        resultado = "impar"

    print(f"A soma é {soma}, que é {resultado.upper()}!")

    # Verificar quem ganhou
    if resultado == escolha or (resultado == "ímpar" and escolha == "impar"):
        print("Você venceu! 🎉")
    else:
        print("O computador venceu!")

    jogar = str(input("Deseja jogar novamente? (s/n): "))
    jogar = jogar.lower()
    if jogar == "n":
        print("Obrigado por jogar!\nAté a próxima.")
        break
