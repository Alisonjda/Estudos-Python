# %%

lista = [2,132,"Alison", ["ds", "de","da"], True]

lista[2]

# %%

# Pares de chave/valor

dados_alison = {
    "nome" : "alison",
    "filhos" : False,
    "Sobrenome" : "anjos",
    "formação" : ["Sistemas de informação", "curso Udemy"],
    "cargo" : [
        {"funçao" : "Telemarkting"},
        {"funçao" : "jovem aprendiz"},
        {"funçao" : "Operador"},
    ]
    }

print(dados_alison)
dados_alison["cargo"][-1]
# %%

# Forma de atribuir uma chave nova para o dicionário

dados_alison["estado civil"] = "solteiro"
print(dados_alison)

# %%

# lsita de chaves que podemos acessar.
print("chaves: ", dados_alison.keys())
# Lista de valores que podemos acessar.
print("Chaves: ", dados_alison.values())
print("Lista: ", dados_alison.items())

# %%

for chave in dados_alison:
    print(chave, "->", dados_alison[chave])

# %%

for chave, valor in dados_alison.items():
    print(chave,":", valor)
