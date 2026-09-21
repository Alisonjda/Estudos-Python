# %%

nome_arquivo = "historia.txt"

#Abrir o arquivo em formato de leitura
open_file = open(nome_arquivo)

# %%

# Lê os dados do arquivos 
conteudo = open_file.read()
print(conteudo)

# %%
#Fecha o arquivo
# Sempre importante fechar após abrir o arquivo
open_file.close()