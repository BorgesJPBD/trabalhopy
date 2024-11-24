palavra = str(input("Digite a palavra que queira sair de forma invertida:"))

def palavr_invert():
    inverter = palavra [::-1]
    return inverter

saida = palavr_invert()
print (f'A palavra invertida é:{saida}')