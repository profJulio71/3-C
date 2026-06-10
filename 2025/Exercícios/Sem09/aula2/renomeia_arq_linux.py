import os
#	Caminho para a pasta com os arquivos
caminho_pasta = "/mnt/FC6ECC156ECBC71C/a/a"
#	Lista todos os arquivos na pasta
arquivos = os.listdir(caminho_pasta)
#	Itera sobre cada arquivo na Listo e renomeia
for nome_arquivo in arquivos:  # nova variável "nome do arquivo - loop na lista dos arquivos da pasta
    caminho_antigo = os.path.join(caminho_pasta, nome_arquivo) # caminho antigo recebe o diretório e nome do arquivo
    nome_maiusculo = nome_arquivo.upper() # converte o nome dos arquivos para maiúsculo
    if "ENTREVISTA" in nome_maiusculo:  # encontrando arquivo com nome ENTREVISTA entra no laço
        prefixo = ".mp3"  # coloca na inognita prefixo o valor .mp3
        novo_nome = os.path.join(caminho_pasta, nome_maiusculo + prefixo)  # variável novo_nome recebe a string
        # concatenada com nome do arquivo ao valor da variável prefixo.
        os.rename(caminho_antigo, novo_nome) # Renomeia o arquivo para o novo nome
    elif "TRAILER" in nome_maiusculo: # encontrando arquivo com nome TRAILER entra no laço
        prefixo = ".mp4" # coloca na inognita prefixo o valor .mp4
        novo_nome = os.path.join(caminho_pasta, nome_maiusculo + prefixo) # variável novo_nome recebe a string
        # concatenada com nome do arquivo ao valor da variável prefixo.
        os.rename(caminho_antigo, novo_nome) # Renomeia o arquivo para o novo nome
    else:
        prefixo = ".jpg" # coloca na inognita prefixo o valor .jpg
        novo_nome = os.path.join(caminho_pasta, nome_maiusculo + prefixo) # variável novo_nome recebe a string
        # concatenada com nome do arquivo ao valor da variável prefixo.
        os.rename(caminho_antigo, novo_nome) # Renomeia o arquivo para o novo nome
print ("Renomeação concluida com sucesso!")
