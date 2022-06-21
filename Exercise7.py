# Tarefa 7: Conjunto de Valores
# Dev: Gabriela Ottoni Zimmermann
# Data: 15.06.2022

Laco1 = True
Laco2 = True

n = int(input("Digite um Número qualquer:"))
nQuadrado = n * n
nCubo = n * n * n
nRaiz = nQuadrado
print("O número", n, "tem como quadrado:", nQuadrado, ".")
print("Seu cubo é:", nCubo, ", sua raiz quadrada é:", nRaiz)
while Laco1:
    n2 = int(input("Digite um Número negativo:"))
    if n2 < 0:
        Laco1 = False
    else:
        print("Aceitável apenas números negativos, digite novamente...")
        continue
    break

