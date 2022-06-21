# Tarefa 17: Triângulo
# Dev: Gabriela Ottoni Zimmermann
# Data: 17.06.2022

print("Classificação de triângulos:")
med1 = float(input("Digite a medida do 1º lado:"))
med2 = float(input("Digite a medida do 2º lado:"))
med3 = float(input("Digite a medida do 3º lado:"))

if med1 == med2 and med1 == med3:
    print("TRIÂNGULO EQUILÁTERO: possui os 3 lados iguais.")
elif med1 == med2 and med1 != med3 or med1 == med3 and med1 != med2:
    print("TRIÂNGULO ISÓCELES: possui dois lados iguais.")
elif med1 != med2 and med1 != med3:
    print("TRIÂNGULO ESCALENO: possui três lados diferentes.")