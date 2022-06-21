# Tarefa 13: Altura e sexo
# Dev: Gabriela Ottoni Zimmermann
# Data: 15.06.2022

Feminino = 1
Masculino = 2

print("Qual o sexo? (1- Feminino, 2- Masculino)")
Sexo = int(input())
Altura = float(input("Digite a altura:"))
if Sexo == Feminino:
    PesoIdeal = (Altura * 62.1) - 44.7
elif Sexo == Masculino:
    PesoIdeal = (Altura * 72.7) - 58
print("Seu Peso Ideal é:", PesoIdeal)
