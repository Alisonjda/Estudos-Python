def par_impar(numero:int):
    if numero %2 == 0:
        print("É par")
    else:
        print("É impar")


numero = input("Entre com o valor: ")
numero = int(numero)

par_impar(numero)