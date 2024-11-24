def lista_aninhada(lista):
    return [[*set(sublista)] for sublista in lista]


lista = [
    [7, 9, 2, 3, 7],
    [9, 4, 2, 3, 5],
    [0, 2, 9, 6]
]

nova_lista = lista_aninhada(lista)

print(nova_lista)