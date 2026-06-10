"""
Gere um dicionárioem que as chaves são os meses do ano,
e os valores são o número de dias em cada mês.
"""

dias_por_mes = {
    "janeiro": 31,
    "fevereiro": 28,
    "março": 31,
    "abril": 30,
    "maio": 31,
    "junho": 30,
    "julho": 31,
    "agosto": 31,
    "setembro": 30,
    "outubro": 31,
    "novembro": 30,
    "dezembro": 31
}

print(dias_por_mes,"\n")

# Impressão linha por linha
for mes, dias in dias_por_mes.items():
    print(f"{mes.capitalize()}: {dias} dias")