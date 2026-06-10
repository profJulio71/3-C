import os

# Caminho da pasta com os arquivos
pasta = "/mnt/FC6ECC156ECBC71C/a/a"

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    caminho_completo = os.path.join(pasta, nome_arquivo)

    # Verifica se é um arquivo
    if os.path.isfile(caminho_completo):
        # Separa o nome do arquivo e a extensão
        nome_sem_extensao, _ = os.path.splitext(nome_arquivo)

        # Converte para minúsculas
        novo_nome = nome_sem_extensao.lower()

        # Novo caminho com nome minúsculo e sem extensão
        novo_caminho = os.path.join(pasta, novo_nome)

        # Renomeia o arquivo
        os.rename(caminho_completo, novo_caminho)
        print(f'Renomeado: {nome_arquivo} -> {novo_nome}')