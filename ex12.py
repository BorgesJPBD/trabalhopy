def num_primos(inicio, fim):
    primos = []  
    
    for num in range(inicio, fim + 1):  
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):  
                if num % i == 0: 
                    break
            else:
                primos.append(num)  
    
    return primos 


inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))


print(num_primos(inicio, fim))