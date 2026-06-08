l = 10
i = 0
lista = []
while i < 10:
    v = int(input("Digite um valor para lista: "))
    lista.insert(i, v)
    i += 1
print(f"Os valores da lista são ",lista)
print("Asoma dos valores da lista é: ", sum(lista))