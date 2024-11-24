n1 = float(input("Digite uma nota:"))
n2 = float(input("Digite outra nota:"))
n3 = float(input("Digite mais uma nota para finalizar a sua média:"))

def média():
    resultado = (n1 + n2 + n3) / 3
    return resultado

mediana = média()

print(f'A média final é: {mediana}')
   
