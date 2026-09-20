# %%

def juros_compostos(aporte, taxa, anos):
    return aporte * (1 + taxa) ** anos

# %%
#Tem que seguir a mesma ordem (Aporte, taxa, anos)
juros_compostos(1000, 0.13, 4)

# Caso queira alterar siga o EX:
# juros_compostos(anos=4, aporte=1000, taxa=0.13)

# Recomenda-se seguir a ordem 

# %%

# documentação da sua função 

def juros_compostos(aporte:int, taxa:float, anos:int)-> float:
    """ Juros compostos servem para calcular o retorno financeiro a partir de um aporte.
Deve-se considerar o valor, a taxa de juros atula e o tempo (em anos) para cálculo do valor a ser retornado.

aporte:
    um número inteiro, que represente o valor em R$

taxa:
    um número float entre 0 e 1 que represente o valor taxa de juros 

anos:
    um número inteiro >= 1 que represente o tempo que o investimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos