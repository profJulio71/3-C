"""
Crie um conjunto chamado frutas com algumas frutas. Crie um segundo conjunto chamado frutas_exoticas
com frutas diferentes. Verifique e imprima se há alguma fruta em comum entre os dois conjuntos.
"""

# Criando os conjuntos
frutas = {'laranja', 'morango', 'maçã', 'banana', 'laranja', 'uva', 'romã'}
frutas_exoticas = {'mangostim', 'guabiroba', 'romã','kiwi', 'lichia', 'banana', 'pitaya'}

# Verificando a interseção (elementos em comum)
frutas_em_comum = frutas.intersection(frutas_exoticas)

# Imprimindo o resultado
if frutas_em_comum:
    print("Frutas em comum:", frutas_em_comum)
else:
    print("Não há frutas em comum entre os dois conjuntos.")