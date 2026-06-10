"""
Você está criando um jogo e tem uma lista de personagens.
Crie uma função chamada verificar_vidaque aceite uma lista de pontos de vida e imprima se cada personagem está vivo ou morto (vida > 0).
pontos_vida_personagens= [100, 0, 50, 75]
"""

def verificar_vida(pontos_vida):
    for indice, vida in enumerate(pontos_vida):
        status = "VIVO" if vida > 0 else "MORTO"
        print(f"Personagem {indice}: {status} (Vida: {vida})")

# Exemplo de uso
pontos_vida_personagens = [100, 0, 50, 75]
verificar_vida(pontos_vida_personagens)