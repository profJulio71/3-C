###  import random

l = 10
i = 0
lista = []
while i < 10:
    v = random.randint(1,30)
    lista.insert(i, v)
    i += 1

resposta = lista
tentativa = 0
chute = 0
i = 0

while resposta != chute:
    tentativa+=1
    chute = int(input('digite seu chute para o numero sorteado: '))
    
    r = lista.pop(0)

    if resposta > r :
        print('o numero sorteado é menor')
    
    if lista.index[i] < resposta:
        print('o numero sorteado é maior')
    i += 1
print("Parabéns! Você acertou!")
print('O numero secreto é:',resposta,'e levou',tentativa,'tentativas')

# print(f"Os valores da lista são ",lista)
#print("Asoma dos valores da lista é: ", sum(lista))