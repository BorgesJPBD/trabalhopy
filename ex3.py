
C = float(input("Digite a temperatura em Graus Celsius para a conversão em Fahrenheit:"))

def conversão_c_em_f(fahrenheit):
    fahrenheit = C * 1.8 + 32 
    return(f'A conversão de Graus Celsius para Fahrenheit é de {fahrenheit} F')

conversão = conversão_c_em_f(C)
print (conversão)

    

