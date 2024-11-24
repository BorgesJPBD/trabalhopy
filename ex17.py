def ordem(l1):
    l1 = [int(x) for x in l1.split()]
    l1.sort()
    return l1

user = input("Digite uma lista de números, separados por espaço: ")
ordem_correta = ordem(user)
print(f"A ordem correta dos números é {ordem_correta}")


