# Tarefa 10: Validar Senha
# Dev: Gabriela Ottoni Zimmermann
# Data: 15.06.2022

laco1 = True
login = input("Login:")
senha = int(input("Senha:"))
while laco1 == True:
    if senha == 1234:
        print("ACESSO PERMITIDO")
        laco1 = False
    else:
        print("ACESSO NEGADO")
        print("Tente novamente")
    break


