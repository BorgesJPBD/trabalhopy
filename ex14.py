palavra = (input("Digite uma palavra:"))

def palindromo_false_true(palavra):
    
    palindromo = palavra
    
    if palavra == palavra [::-1]: 
        return("Essa palavra é um palindromo")
    else:
        return("Essa palavra não um palindromo")
    
    
é_ou_não_é = palindromo_false_true(palavra)

print(é_ou_não_é)
        
