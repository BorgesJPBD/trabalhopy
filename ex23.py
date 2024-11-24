def calcular(n1,n2,operacao):
    if operacao == 'adição':
        return n1 + n2
    elif operacao == 'subtração':
        return n1 - n2
    elif operacao == 'multiplicação':
        return n1 * n2
    elif operacao == 'divisão':
        return n1 / n2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha uma operação (adição, subtração, multiplicação ou divisão): ").lower()


resultado = calcular(num1, num2 ,operacao)
print(f"O resultado da {operacao} é: {resultado}")
