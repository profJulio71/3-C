"""
Solicite ao usuário que digite uma string que contenha espaços em branco no
início e no final. Remova esses espaços e imprima a string resultante.
"""

# Solicita ao usuário que digite uma string com espaços no início e no final
texto = input("Digite uma string com espaços no início e no final: ")

# Remove os espaços em branco no início e no final usando strip()
texto_sem_espacos = texto.strip()

# Imprime a string resultante
print("String sem espaços:", texto_sem_espacos)