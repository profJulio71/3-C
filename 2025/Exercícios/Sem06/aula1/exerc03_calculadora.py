print('''
           Bem vindo
              ao
      Programa Calculadora
      ''')

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

op = input('''
Por favor, digite a operação matemática que você gostaria de concluir:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

if op == '+':
    print('{} + {} = '.format(numero_1, numero_2))
    print(numero_1 + numero_2)

elif op == '-':
    print('{} - {} = '.format(numero_1, numero_2))
    print(numero_1 - numero_2)

elif op == '*':
    print('{} * {} = '.format(numero_1, numero_2))
    print(numero_1 * numero_2)

elif op == '/':
    print('{} / {} = '.format(numero_1, numero_2))
    print(numero_1 / numero_2)

else:
    print('Você digitou um operador inválido, execute o programa novamente.')