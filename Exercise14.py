# Tarefa 14: Polígono
# Dev: Gabriela Ottoni Zimmermann
# Data: 17.06.2022

QuantLados = int(input("Digite Quantos Lados Tem Seu Polígono:"))

if QuantLados == 3:
    print("Seu polígono é um: Triângulo, para calcular sua área informe:")
    altura = int(input("Digite a altura do triângulo:"))
    base = int(input("Digite a base do triângulo:"))
    area = (base * altura) / 2
    print("A area do seu triângulo é de:", area, "cm²")
elif QuantLados == 4:
    print("Seu polígono é um: Quadrado, para calcular sua área informe:")
    lados = float(input("Qual a Medida dos Lados, em cm?"))
    area = lados * lados
    print("A area do seu quadrado é de:", area, "cm²")
elif QuantLados == 5:
    print("Seu polígono é um: Pentágono, para calcular sua área informe:")
    lados = float(input("Informe a medida dos lados, em cm:"))
    aponema = float(input("Informe a medida do seu aponema:"))
    area = 5 * lados * aponema
    print("A área do seu pentágono é de:", area, "cm²")

