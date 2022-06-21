# Tarefa 9: Idade para Voto
# Dev: Gabriela Ottoni Zimmermann
# Data: 15.06.2022

print("Faça parte da construção da democracia brasileira!")
print("Consulte se você está apto a votar pela sua idade:")
AnoNasc = int(input("Digite seu ano de nascimento:"))
AnoCorrente = 2022
IdadePessoa = AnoCorrente - AnoNasc
if IdadePessoa >= 16 and IdadePessoa < 18:
    print("Seu voto não é obrigatório, porém, é importante!")
    print("Faça parte do processo democrático!")
else:
    if IdadePessoa >= 16:
        print("Com", IdadePessoa, "anos você está apto a votar!")
        print("Regularize seu título de eleitor, e nos vemos em outubro!")
    else:
        print("Esse ano não será possível! Mas em breve nos encontarmos nas urnas!")

if IdadePessoa > 70:
    print("Seu voto não é obrigatório, mas é muito importante!")
