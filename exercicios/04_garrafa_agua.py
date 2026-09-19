# faça um programa que vende uma garrafa de agua
# Se o cliente escolher agua mineral natural, será cobrado R$1,50
# Se o cliente escolher agua mineral com gás, será cobrado R$2,50


texto = """ 
Escolha a sua água para comprar 
(1) Àgua mineral natural 
(2) Àgua mineral com gás
 """

opcao = input((texto))

if opcao == "1":
    print("Sua compra deu R$1,50")

elif opcao == "2":
    print("Sua compra deu R$2,50")

else:
    print("entre com a opção correta, por favor")