def contar_vogais_consoantes(contagem):
    cont_vogais = 0
    cont_consoantes = 0
    vogais = "aeiouAEIOU"
    
    for char in contagem:
     
        if ('a' <= char.lower() <= 'z'):
            cont_vogais += 1 if char in vogais else 0
            cont_consoantes += 1 if char not in vogais else 0
            
    return cont_vogais, cont_consoantes

contagem = input("Digite uma frase: ")
vogais, consoantes = contar_vogais_consoantes(contagem)


print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")