"""
Implemente uma função que receba uma string e um número (chamado de
“deslocamento”) como parâmetros e retorne a string cifrada, usando a Cifra
de César. Cada letra na string deve ser deslocada pelo número fornecido. Por
exemplo, com um deslocamento de 3, “ABC” seria cifrado como “DEF”.
"""

def cifra_cesar(texto, deslocamento):
    resultado = ""

    for char in texto:
        # Verifica se o caractere é uma letra
        if char.isalpha():
            # Determina o valor base (para letras minúsculas ou maiúsculas)
            base = ord('a') if char.islower() else ord('A')

            # Calcula o novo caractere com o deslocamento
            novo_char = chr(base + (ord(char) - base + deslocamento) % 26)
            resultado += novo_char
        else:
            # Se não for uma letra, apenas adiciona o caractere sem modificar
            resultado += char

    return resultado


# Testando a função
texto = input("Digite o texto para cifrar: ")
deslocamento = int(input("Digite o número de deslocamento: "))

texto_cifrado = cifra_cesar(texto, deslocamento)
print("Texto cifrado:", texto_cifrado)

"""
ord() converte uma letra para seu código ASCII (valor numérico correspondente).
chr() converte um código ASCII de volta para o caractere.
O deslocamento é aplicado ao código ASCII da letra, e a operação % 26 garante que o deslocamento ocorra de forma cíclica no alfabeto (de A a Z ou de a a z).
Caracteres não alfabéticos (como espaços, pontuações) são mantidos inalterados.
"""