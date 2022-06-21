# Tarefa 1: Gratificação de natal
# Dev: Gabriela Ottoni Zimmermann
# Data: 01.06.2022

# var:
# Faltas
# var = Extra
# h = Extra - (2 / 3 (Faltas))

Extras = float(input("Número de horas extras, em minutos:"))
Faltas = float(input("Número de horas Faltadas, em minutos:"))

h = Extras - (2 / 3 * (Faltas))

if h >= 2401:
    print("Prêmio= R$500,00")
else:
    if h < 2401 and h > 1800:
        print("Prêmio= R$400,00")
    else:
        if h < 1801 and h >1200:
            print("Prêmio= R$300,00")
        else:
            if h < 1201 and h >= 600:
                print("Prêmio= R$200,00")
            else:
                print("Prêmio= R$100,00")

