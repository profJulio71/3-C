"""
Faça um programa que, dadas duas listas de mesmo tamanho,
imprima o produto escalar entre elas.

O produto escalar (ou produto interno) de duas listas é calculado multiplicando os
elementos correspondentes de cada lista e somando os resultados dessas multiplicações.
A fórmula para o produto escalar é:
Produto escalar=a1⋅b1+a2⋅b2+⋯+an⋅bn
Onde a1,a2,…,na,  são os elementos da primeira lista e b1,b2,…,bn são os elementos da
segunda lista.
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Calculando o produto escalar
produto_escalar = sum(lista1[i] * lista2[i] for i in range(len(lista1)))

print("Produto escalar:", produto_escalar)

"""
Saída:
Para as listas fornecidas, o produto escalar será:
(1⋅6)+(2⋅7)+(3⋅8)+(4⋅9)+(5⋅10)=6+14+24+36+50=130
"""