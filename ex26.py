def mesclar_dicionarios(d1, d2):
    for chave, valor in d2.items():
        if chave in d1:
            d1[chave] += valor  
        else:
            d1[chave] = valor   
    return d1

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 15, 'c': 25, 'd': 35}


mesclar_dicionarios(d1, d2)


print(d1)