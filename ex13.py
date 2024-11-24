                                                   
n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))


notas = [n1, n2, n3]


def notas_acima(notas):
    media = sum(notas) / len(notas)
    
    acima_media = []
    for nota in notas:
        if nota > media:
            acima_media.append(nota)
    
    return acima_media


resultado_final = notas_acima(notas)

media = sum(notas) / len(notas)


print(f'As medias das notas foram {media}')
print(f"As notas acima da média foram: {resultado_final}")













            
            

