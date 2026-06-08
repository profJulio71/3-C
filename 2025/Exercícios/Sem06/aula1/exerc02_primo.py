"""
Exercício 2: Verificação de primo
Peça ao usuário um número inteiro.
Determinem se ele é primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
"""

num = int(input('Digite um número positivo, para verificar se é primo ou não: '))

contador, divisores = 1, 0
"""
contador = 1
divisores = 0
"""
while True:
        if num % contador == 0: # Verifica se não sobra resto na divisão do num pelo contador.
                divisores += 1 # Se não sobrou, adiciona + 1 para variável divisores.
        contador += 1 # Depois do if, aumenta + 1 no contador
        if contador == num+1: # Se o contador for igual o número + 1 que vc quis verificar, entre neste bloco.
                if divisores == 2: # Verifica se tem só 2 divisores (Dividido por 1 e por ele mesmo).
                        print('É primo.')
                        break # Se for primo, diga que é primo e pare o programa.
                else:
                        print('Não é primo.')
                        break # Senão, diga que não é primo e pare o programa