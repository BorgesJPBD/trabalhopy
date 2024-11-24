palavra = str(input("Digite uma frase para a contagem de palavras unicas que ela possui:"))

def palavras_unicas (frase):
    palavras = frase.split() 
    return set(palavras) 
    

resultado = palavras_unicas(palavra)

print (f"A frase que você digitou exibe essas palavras unicas {resultado}")