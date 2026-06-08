"""
Listagem dos arquivos:
Observe a lista arquivos_na_pasta, que conta com variados nomes de arquivos de mídia.
arquivos_na_pasta = ["trailer_fantasia", "entrevista_celebridade", "foto_perfil", "ensaio_fotografico"]
1 - Padronização para maiúsculas:
Utilize um método de string para converter cada nome de arquivo para maiúsculas e imprima os novos nomes.
2 - Verificação e renomeação:
• Itere sobre cada nome de arquivo na lista;
• Verifique o conteúdo do nome do arquivo para determinar a extensão associada;
• Adicione a extensão ao nome do arquivo e imprima o novo nome, simulando a renomeação.
3 - Resultado final:
Após a renomeação, imprima uma mensagem indicando que a organização criativa do projeto de mídia foi
aprimorada com sucesso.
"""

import os

# Caminho da pasta com os arquivos
pasta = "D:/a/a"

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