"""
Você está desenvolvendo um sistema de reservas para um restaurante.
Crie uma função chamada mostrar_mesas_disponiveisque aceite uma lista de mesas reservadas e imprima as mesas disponíveis (índices não reservados).
mesas_reservadas= [2, 4, 6]
"""

def mostrar_mesas_disponiveis(mesas_reservadas, total_mesas):
    mesas_disponiveis = [i for i in range(total_mesas) if i not in mesas_reservadas]
    print("Mesas disponíveis:", mesas_disponiveis)

# Exemplo de uso
mesas_reservadas = [2, 4, 6]
total_mesas = 10  # Suponhamos que o restaurante tenha 10 mesas
mostrar_mesas_disponiveis(mesas_reservadas, total_mesas)