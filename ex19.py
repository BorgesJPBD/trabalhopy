def contar_caracteres(frase):
    dicionario = {}

    for caractere in frase:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1

    return dicionario


frase = input("Digite uma frase: ")
resultado = contar_caracteres(frase)
print("Contagem de caracteres:", resultado)