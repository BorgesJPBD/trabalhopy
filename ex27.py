def contar_palavras_frequentes(texto):
    
    texto = ''.join(char if char.isalnum() else ' ' for char in texto).lower()

    palavras = texto.split()


    contagem_palavras = {}
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1


    palavras_ordenadas = sorted(contagem_palavras.items(), key=ordenar_por_frequencia, reverse=True)

    return palavras_ordenadas[:5]

def ordenar_por_frequencia(item):
    return item[1]


texto = input("Digite um texto longo: ")
mais_frequentes = contar_palavras_frequentes(texto)


print("As 5 palavras mais frequentes são:")
for palavra, freq in mais_frequentes:
    print(f"{palavra}: {freq}")