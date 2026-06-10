"""
1. Crie um dicionário cujas chaves são os meses do ano e os valores
são a duração (em dias) de cada mês.
Obs.: os meses devem ser escritos com letras minúsculas.
"""

# Dicionário com os meses e a duração em dias
# Função para verificar se o ano é bissexto
def eh_bissexto(ano):
    # Um ano é bissexto se for divisível por 4, mas não divisível por 100,
    # ou se for divisível por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

# Perguntar ao usuário o ano
ano = int(input("Digite o ano: "))

# Verificar se o ano é bissexto
bissexto = eh_bissexto(ano)

# Dicionário com os meses e a duração em dias
meses = {
    'janeiro': 31,
    'fevereiro' : 28 if not bissexto else 29,  # 28 ou 29 dependendo se o ano é bissexto
    'março': 31,
    'abril': 30,
    'maio': 31,
    'junho': 30,
    'julho': 31,
    'agosto': 31,
    'setembro': 30,
    'outubro': 31,
    'novembro': 30,
    'dezembro': 31
}

# Imprimir os meses e suas durações
for mes, dias in meses.items():
    print(f'{mes} - {dias} dias')