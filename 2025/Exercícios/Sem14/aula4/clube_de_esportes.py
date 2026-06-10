"""
Considere um contexto de um clube esportivo com três times diferentes: futebol, basquete e vôlei.
Cada time tem uma lista de membros que participam do clube.
1. Crie três conjuntos: membros_futebol, membros_basquetee membros_voleirepresentando os membros de cada time.
2. Implemente uma função chamada adicionar_membro que recebe o nome de um membro e o esporte a que deseja se
juntar e adicione esse membro ao conjunto correspondente.
3. Implemente uma função chamada remover_membroque recebe o nome de um membro e remove esse membro de todos os
conjuntos, indicando de qual time ele foi removido.
4. Crie uma função chamada listar_timesque imprime os membros de cada time.
5. Crie uma função chamada verificar_presencaque recebe o nome de um membro e verifica se esse membro está
presente em pelo menos um dos times.
6. Realize algumas chamadas de função para demonstrar o funcionamento do sistema, incluindo a adição, a remoção
e a listagem de membros.
"""

# 1. Criando os conjuntos para cada time
membros_futebol = set()
membros_basquete = set()
membros_volei = set()

# 2. Função para adicionar membro a um time
def adicionar_membro(nome, esporte):
    esporte = esporte.lower()
    if esporte == 'futebol':
        membros_futebol.add(nome)
        print(f"{nome} adicionado ao time de futebol.")
    elif esporte == 'basquete':
        membros_basquete.add(nome)
        print(f"{nome} adicionado ao time de basquete.")
    elif esporte == 'vôlei' or esporte == 'volei':
        membros_volei.add(nome)
        print(f"{nome} adicionado ao time de vôlei.")
    else:
        print("Esporte inválido! Escolha entre: futebol, basquete, vôlei.")

# 3. Função para remover um membro de todos os times
def remover_membro(nome):
    removido = False
    if nome in membros_futebol:
        membros_futebol.remove(nome)
        print(f"{nome} removido do time de futebol.")
        removido = True
    if nome in membros_basquete:
        membros_basquete.remove(nome)
        print(f"{nome} removido do time de basquete.")
        removido = True
    if nome in membros_volei:
        membros_volei.remove(nome)
        print(f"{nome} removido do time de vôlei.")
        removido = True
    if not removido:
        print(f"{nome} não encontrado em nenhum time.")

# 4. Função para listar os membros de cada time
def listar_times():
    print("\n--- Membros dos times ---")
    print("Futebol:", membros_futebol if membros_futebol else "Nenhum membro")
    print("Basquete:", membros_basquete if membros_basquete else "Nenhum membro")
    print("Vôlei:", membros_volei if membros_volei else "Nenhum membro")
    print("-------------------------\n")

# 5. Função para verificar se um membro está em pelo menos um time
def verificar_presenca(nome):
    presente = False
    if nome in membros_futebol:
        print(f"{nome} está no time de futebol.")
        presente = True
    if nome in membros_basquete:
        print(f"{nome} está no time de basquete.")
        presente = True
    if nome in membros_volei:
        print(f"{nome} está no time de vôlei.")
        presente = True
    if not presente:
        print(f"{nome} não está em nenhum time.")

# 6. Demonstração do sistema
"""
adicionar_membro("Lucas", "Futebol")
adicionar_membro("Maria", "Basquete")
adicionar_membro("João", "Vôlei")
adicionar_membro("Ana", "Futebol")
adicionar_membro("Carlos", "Basquete")
"""

def adicionar_membros_interativamente():
    print("Digite 'sair' para encerrar a entrada de membros.")
    while True:
        nome = input("Digite o nome do membro para adicionar: ").strip()
        if nome.lower() == 'sair':
            break
        esporte = input("Digite o esporte (futebol, basquete, vôlei): ").strip()
        if esporte.lower() == 'sair':
            break
        adicionar_membro(nome, esporte)
    print("Entrada de membros finalizada.")

# Demonstração da rotina de entrada
adicionar_membros_interativamente()
# Listar os membros após a entrada
print("\nLista final dos membros nos times:")
print("Futebol:", membros_futebol)
print("Basquete:", membros_basquete)
print("Vôlei:", membros_volei)

listar_times()

verificar_presenca("Maria")
verificar_presenca("Pedro")

remover_membro("Maria")
remover_membro("Pedro")

listar_times()