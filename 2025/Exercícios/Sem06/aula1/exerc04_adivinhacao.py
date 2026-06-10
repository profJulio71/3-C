import random

print("Bem-vindo ao Jogo de Adivinhação!")

num = random.randint(1,100)

resposta = num
tentativa = 0
chute = 0

while resposta != chute:
    tentativa+=1
    chute = int(input('digite seu chute para o numero sorteado: '))
    
    if chute > resposta:
        print('o numero sorteado é menor')
    
    if chute < resposta:
        print('o numero sorteado é maior')
print("Parabéns! Você acertou!")
print('O numero secreto é:',resposta,'e levou',tentativa,'tentativas')
