# Tarefa 3: Idade de um Nadador
# Dev: Gabriela Ottoni Zimmermann
# Data: 01.06.2022

Contador = 0

while Contador < 10:
    Contador = Contador + 1
    print(Contador)
    idade = int(input("Digite a idade do nadador:"))
    if idade < 5:
        print("Faixa etária indisponível")
    if idade >= 5 and idade <= 7:
        print("Infantil")
    else:
        if idade >= 8 and idade <= 10:
            print("Juvenil")
        else:
            if idade >= 11 and idade <= 15:
                print("Adolescente")
            else:
                if idade >= 16 and idade <=30:
                    print("Adulto")
                else:
                    if idade > 30:
                        print("Sênior")
