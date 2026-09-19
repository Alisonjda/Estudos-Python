# Escreva um programa que receba uma lista de numero 
# do usuário e conte quantas vezes um numero
# especifico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

# %%
lista= [2, 4, 2, 3, 5, 4, 2 ,3, 4 ,3, 2, 1]

numero = input("entre com um número: ")
numero = int(numero)

contador = 0 
for i in lista:
    if i == numero:
        contador +=1 

print("quantidade de", numero, ":", contador)

