idade = int(input("Qual sua idade?:"))

def idade_user ():
    idade_user = idade 
    
    
    if idade > 18:
        return ('Você é maior de idade')
    
    else:
        return ('Você é menor de idade')
    
    
idade_final = idade_user()

print (idade_final)
    