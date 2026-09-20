# %%

def calc_imposto(preco:float,tx_base:float, **kwargs): # **kwargs é como se fosse um dicionario 
    imposto =  preco * tx_base                    # ao contrario de *args que é tipo um lista/tuplas 

    for i in kwargs:
        print(i, kwargs[i])
        imposto = preco * kwargs[i]


    return imposto

#%% 


# ou

imposto_geral = {
    "municipio": 0.003,
    "estadual": 0.005,
    "nacional":0.007
}


calc_imposto(100,0.03, **imposto_geral)
