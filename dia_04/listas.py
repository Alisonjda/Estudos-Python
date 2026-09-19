# %% 


# Lista é um conjunto de elementos e pode ser de qualquer tipo 
# Uma maneira de definir listas
idades = [25, 34, 23, 11, 13, 46, 43]

print(idades)

# %% 

Alison = ["Alison", "Anjos", 21, "solteiro", 1200.50]

print( Alison)

# %%

type(Alison)

# %%

# renda
print(Alison[4])

#Nome
print(Alison[0])


# %%

idades = [25, 34, 23, 11, 13, 46, 43]

# soma
print("Soma idades: ", sum(idades))
# Media (Nao existe um comando para a Media :( )
print("qtde idades: ", len(idades))
# forma para calcular a media
print("Media de idades: ", sum(idades) / len(idades))
# Menor idade
print("Menor idade: ", min(idades))
# Maior idades
print("Maior idades: ", max(idades))


# %%
Alison = [
    "Alison Anjos",
    21,
    "solteiro",
    True,
    ["Ana", "Marli", "luan","lucas"],
    [1000, 1500, 2000, 5000]


]

# Alison [START : STOP]
Alison[4][0:3]

#Alison[START : STOP : STEP]
Alison[5][::-1]

