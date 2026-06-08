def calcular_total_transacoes_positivas(transacoes):
    transacoes_positivas = [valor for valor in transacoes if valor > 0]
    total_transacoes_positivas = sum(transacoes_positivas)
    quantidade_transacoes_positivas = len(transacoes_positivas)
    return total_transacoes_positivas, quantidade_transacoes_positivas

def calcular_total_transacoes_negativas(transacoes):
    transacoes_negativas = [valor for valor in transacoes if valor < 0]
    total_transacoes_negativas = sum(transacoes_negativas)
    quantidade_transacoes_negativas = len(transacoes_negativas)
    return total_transacoes_negativas, quantidade_transacoes_negativas

#	Lista de transações financeiras de um cLiente
transacoes = [100, -50, 200, -20, 150, -30, 180]

#	Chamando as funções para caLcuLar os totais

total_positivas, quantidade_positivas = calcular_total_transacoes_positivas(transacoes)
total_negativas, quantidade_negativas = calcular_total_transacoes_negativas(transacoes)

#	Impressão dos resuLtados
print("Total das transações positivas:", total_positivas)
print("Quantidade de transações positivas:", quantidade_positivas)
print("Total das transações negativas:", total_negativas)
print("Quantidade de transações negativas:", quantidade_negativas)
