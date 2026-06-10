"""
4. Invertendo chaves e valores:
Escreva um programa que recebe um dicionário e inverte as
chaves pelos valores e vice-versa.
dicionario_exemplo = {'um': 1, 'dois': 2, 'três': 3}
"""

def inverter_dicionario(dicionario):
    # Inverte as chaves e valores
    dicionario_invertido = {valor: chave for chave, valor in dicionario.items()}
    return dicionario_invertido

# Exemplo de uso
dicionario_exemplo = {'um': 1, 'dois': 2, 'três': 3}
dicionario_invertido = inverter_dicionario(dicionario_exemplo)

# Exibir o resultado
print(dicionario_invertido)