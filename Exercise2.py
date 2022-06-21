# Tarefa 2: Idade e Peso
# Dev: Gabriela Ottoni Zimmermann
# Data: 01.06.2022

peso = float(input("Digite o peso:"))
idade = float(input("Digite a Idade:"))

if idade < 20 and peso <= 60:
    print("Grupo de Risco 9")
else:
    if idade >= 20 and idade <= 50 and peso <= 60:
        print("Grupo de Risco 6")
    else:
        if idade > 50 and peso <= 60:
            print("Grupo de Risco 7")
        else:
            if idade < 20 and peso > 60 and peso <= 90:
                print("Grupo de Risco 8")
            else:
                if idade >= 20 and idade <= 50 and peso > 60 and peso <= 90:
                    print("Grupo de Risco 5")
                else:
                    if idade > 50 and peso > 60 and peso <= 90:
                        print("Grupo de Risco 2")
                    else:
                        if idade < 20 and peso > 90:
                            print("Grupo de Risco 7")
                        else:
                            if idade >= 20 and idade <= 50 and peso > 90:
                                print("Grupo de Risco 4")
                            else:
                                print("Grupo de Risco 1")