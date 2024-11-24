lista_cont = input("Escreva os numeros para a contagem, Separados por espaços:")

def contagem ():   
    lista =  lista_cont.split() 
    return len (lista)

qtd_num = contagem()

print (f'A quantidade presente nessa lista é de {qtd_num} numeros')