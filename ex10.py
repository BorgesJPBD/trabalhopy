b = float(input("Digite o valor da base do triângulo:"))
a = float(input("Digite o valor da ârea do triângulo:"))

def area_triangulo():
    area = (b * a) / 2
    return area 


valor_final = area_triangulo()

print (valor_final)