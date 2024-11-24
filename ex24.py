def verificar_anagramas(p1, p2):
    return sorted(p1.lower()) == sorted(p2.lower())

p1 = input("Digite a primeira palavra: ")
p2 = input("Digite a segunda palavra: ")

anagramas = verificar_anagramas(p1,p2)

if anagramas:
    print("As palavras são Anagramas")

else:
    print("As palavras não são anagramas")
