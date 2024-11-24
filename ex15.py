import random

n1 = int(input("Tente adivinhar o numero que eu escolhi entre 1 e 100:"))
sorte = random.randint(1,100)
tentativa = 1 

def adivinhacao(adivinhar):
    global tentativa
    while adivinhar != sorte: 
        if adivinhar > sorte:
            print ("Esse numero é maior tente denovo")
        elif adivinhar < sorte:
            print ("Esse numero é menor tente outa vez")
            
            
        adivinhar = int(input(f"Tentativa {tentativa}: Digite outro número: "))
        tentativa += 1 
    return adivinhar
    
            
adivinhacao_final = adivinhacao(n1)
print (adivinhacao_final)























import random


sorte = random.randint(1, 100)
tentativa = 1


n1 = int(input("Tente adivinhar o número que eu escolhi entre 1 e 100: "))

def adivinhacao(adivinhar):
    global tentativa  
    while adivinhar != sorte: 
        if adivinhar < sorte:
            print("Esse número é maior. Tente de novo.")
        elif adivinhar > sorte:
            print("Esse número é menor. Tente de novo.")
        
      
        adivinhar = int(input(f"Tentativa {tentativa}: Digite outro número: "))
        tentativa += 1 
    
    return adivinhar  


adivinhacao_final = adivinhacao(n1)


print(f"Parabéns! Você acertou o número {sorte} em {tentativa} tentativas.")


   










            
            

