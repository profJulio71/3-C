"""
3. Os funcionários de uma empresa têm salários diferentes.
Crie uma função chamada aumentar_salariosque aceite uma
lista de salários e retorne uma nova lista na qual cada salário foi aumentado em 10%.
salarios= [3000, 5000, 7000]
"""

def aumentar_salarios(salarios):
    return [salario * 1.10 for salario in salarios]

salarios = [3000, 5000, 7000]
salarios_aumentados = aumentar_salarios(salarios)

# Imprimir cada salário formatado com duas casas decimais
print("Salários com aumento:")
for salario in salarios_aumentados:
    print(f"R$ {salario:.2f}")