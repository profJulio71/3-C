def calcular_media(notas):
    if not notas:
        return 0  # Evita divisão por zero se a lista estiver vazia
    soma = sum(notas)
    media = soma / len(notas)
    return media

# Exemplo de uso
notas_alunos = [8, 7, 5, 9, 6]
media = calcular_media(notas_alunos)
print(f"Média das notas: {media:.2f}")