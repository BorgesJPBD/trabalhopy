



def sequen_fibo(n):
    if n <= 0:
        return []  
    lista = [1, 1]
    for _ in range(n - 2):
        lista.append(lista[-1] + lista[-2])
    return lista[:n]  
n = int(input("Quantos números você deseja ver da sequência de Fibonacci? "))
print(sequen_fibo(n))
    
