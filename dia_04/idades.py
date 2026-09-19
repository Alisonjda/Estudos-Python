# %%

idades = []

while True:
    idade = input("Digite uma idades: ")
    

    if idade == "":
        break

    idades.append (int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
máximo = max(idades)
qtde = len(idades)

print(media)
print(minimo)
print(máximo)
print(qtde)

