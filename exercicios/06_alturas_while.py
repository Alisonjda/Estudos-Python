# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

# %%

soma = 0                # Valor final 
qtde_de_entradas = 4    # Contador de entradas 

while qtde_de_entradas >0:
    altura = input("Insira altura: ")
    altura = float(altura)
    soma += altura
    qtde_de_entradas -= 1 


print ("Soma das alturas: ", soma)

