texto = """ 
Escolha a sua água para comprar 
(1) Àgua mineral natural 
(2) Àgua mineral com gás
 """

opcao = input((texto))

valor_iten = 0 
if opcao == "1":
    print("Sua compra deu R$1,50")
    valor_iten = 1,50 
elif opcao == "2":
    print("Sua compra deu R$2,50")
    valor_iten = 2,50

if valor_iten == 0:
    print("entre com a opção correta, por favor")

else:
    qtde = input("Quantas garrafas? ")
    qtde = int(qtde)
    valor_total = valor_iten * qtde
    print("sua conta deu: ", valor_total)