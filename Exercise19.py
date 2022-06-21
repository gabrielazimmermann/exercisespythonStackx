# Tarefa 19: Corrija os erros
# Dev: Gabriela Ottoni Zimmermann
# Data: 17.06.2022

# a

idade = int(input("Digite a idade:"))
if idade >= 65:
    print("Melhor Idade")

# b
feminino = 1
masculino = 2
genero = int(input("Gênero:"))
if genero == masculino:
    print("Masculino")
else:
    print("Feminino")

# c
preco = float(input("Digite o preço:"))
if preco > 10.5:
    PrecoFinal = preco * 1.2
else:
    PrecoFinal = preco * 1.35
print(PrecoFinal)
