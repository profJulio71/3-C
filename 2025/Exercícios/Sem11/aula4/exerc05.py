"""
Você está criando um sistema de gerenciamento de tarefas.
Crie uma função chamada imprimir_tarefasque aceite uma lista de tarefas e imprima cada tarefa com seu índice.
tarefas = ['Estudar Python', 'Fazer compras', 'Enviar e-mails']
"""

def imprimir_tarefas(tarefas):
    for indice, tarefa in enumerate(tarefas):
        print(f"Tarefa {indice}: {tarefa}")

# Exemplo de uso
tarefas = ['Estudar Python', 'Fazer compras', 'Enviar e-mails']
imprimir_tarefas(tarefas)