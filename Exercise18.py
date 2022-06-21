# Tarefa 18: Ângulos do Triângulo
# Dev: Gabriela Ottoni Zimmermann
# Data: 17.06.2022

ang1 = int(input("Primeiro ângulo:"))
ang2 = int(input("Segundo ângulo:"))
ang3 = int(input("Terceiro ângulo:"))

if ang1 == 90 or ang2 == 90 or ang3 == 90:
    print("TRIÂNGULO RETÂNGULO: possui um ângulo reto. (igual a 90º).")
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print("TRIÂNGULO OBTUSÂNGULO: possui um ângulo obtuso. (maior que 90º).")
elif ang1 < 90 or ang2 < 90 or ang3 < 90:
    print("TRIÂNGULO ACUTÂNGULO: possui três ângulos agudos. (menor que 90º).")
