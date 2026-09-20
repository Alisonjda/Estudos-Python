def soma(a:float, b:float, c:float) ->float:
    return a + b 


def media(a:float,b:float,c=0.0):  # para um ser opcional EX:(=0.0)
    return (a,b,c) / 3



a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

print("media: ", media(a,b))