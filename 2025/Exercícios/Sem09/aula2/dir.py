import os
#	Caminho para a pasta com os arquivos
caminho_pasta = "C:/a"
#	Prefixo a ser adicionado aos nomes dos arquivos
prefixo = "novo_"
#	Lista todos os arquivos na pasta
arquivos = os.listdir(caminho_pasta)
#	Itera sobre cada arquivo na Listo e renomeia
for nome_arquivo in arquivos:
    caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
    novo_nome = os.path.join(caminho_pasta, prefixo + nome_arquivo)
    os.rename(caminho_antigo, novo_nome)
print ("Renomea<;ao concluida com sucesso!")