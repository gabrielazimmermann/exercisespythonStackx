# Tarefa 20: Elimine as redundâncias
# Dev: Gabriela Ottoni Zimmermann
# Data: 17.06.2022

a = int(input("Digite um número:"))
b = int(input("Digite outro número:"))
if a > b:
    print(a, "é maior que", b)
else:
    print(b, "é maior que", a)


x = int(input("Digite um número:"))
if x > 10:
    print("Valor maior que 10")
else:
    if x <= 10 and x > 5:
        print("Valor menor ou igual a 10 e maior que 5")
    else:
        print("Menor ou igual a 5")
