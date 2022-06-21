# Tarefa 12: Valores em Ordem
# Dev: Gabriela Ottoni Zimmermann
# Data: 15.06.2022

Laco1 = True
while Laco1:
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    n3 = int(input("Digite o terceiro número:"))
    if n1 == n2 or n2 == n3 or n1 == n3:
        print("Não são aceitáveis números iguais. Digite novamente...")
    else:
        Laco1 = False
        continue
    break
if n1 < n2 < n3:
    print(n1, n2, n3)
elif n1 < n3 < n2:
    print(n1, n3, n2)
elif n2 < n1 < n3:
    print(n2, n1, n3)
elif n2 < n3 < n1:
    print(n2, n3, n1)
elif n3 < n1 < n2:
    print(n3, n1, n2)
elif n3 < n2 < n1:
    print(n3, n2, n1)

