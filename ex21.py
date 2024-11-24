
def inteiros(lista):
    elementos_vistos = set()
    return [x for x in lista if x not in elementos_vistos and not elementos_vistos.add(x)]

entrada = input("Digite uma lista de números separados por vírgula: ")
numeros = entrada.split(",")

resultado = inteiros(numeros)
print("Lista sem números repetidos:", resultado)
