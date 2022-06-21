# Tarefa 16: Três Valores e o Maior Deles
# Dev: Gabriela Ottoni Zimmermann
# Data: 17.06.2022

laco1 = True
while laco1:
    n1 = int(input("Digite um Número:"))
    n2 = int(input("Digite um segundo número:"))
    n3 = int(input("Digite um terceiro número:"))
    if n1 == n2 or n2 == n3 or n1 == n3:
        print("ERRO - digite números diferentes")
    else:
        laco1 = False
        print("Os números escolhidos são:", n1, ",", n2, ",", n3, ".")
        if n1 > n2 and n1 > n3:
            print("O maior entre eles é:", n1)
        elif n2 > n1 and n2 > n3:
            print("O maior entre eles é", n2)
        elif n3 > n1 and n3 > n2:
            print("O maior entre eles é:", n3)
        continue
    break


