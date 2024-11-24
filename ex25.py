def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]

entrada = input("Digite os números inteiros (separados por espaço): ")

lista = [int(x) for x in entrada.split()]


pares = filtrar_pares(lista)


print(f"Números pares: {pares}")