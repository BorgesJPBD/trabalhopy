def soma_matriz(matriz):
    soma = 0 
    m = len(matriz)
    
    
    for i in range(m):
        soma += matriz[i][i]  
        soma += matriz[i][m - 1 - i]
     
     
    if m % 2 != 0:
        meio = m // 2
        soma -= matriz[meio][meio]
    return soma
    
matriz = [
    [77, 78, 89],
    [90, 40, 63],
    [27, 68, 91]
]
    
    
matriz_final = soma_matriz(matriz)
print (matriz_final)