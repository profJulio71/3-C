def aumentar_salarios(salarios):
    return [salario * 1.10 for salario in salarios]

# Exemplo de uso
salarios = [3000, 5000, 7000]
salarios_ajustados = aumentar_salarios(salarios)
print(salarios_ajustados)