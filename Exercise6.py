# Tarefa 6: Receber Nomes e Salários
# Dev: Gabriela Ottoni Zimmermann
# Data: 15.06.2022

Laco1 = 0
DinheiroJoao = 0
DinheiroCarlos = 1
NumMeses = 0
soma = 0

SalarioCarlos = int(input("Digite o Salário de Carlos:"))
SalarioJoao = float(0.33 * SalarioCarlos)
print("O Salário de João é:", SalarioJoao)
print("O salário de Carlos é de:", SalarioCarlos)

while DinheiroJoao < DinheiroCarlos:
    NumMeses = int(input("Inserir Mês de Referência:"))
    DinheiroCarlos = (SalarioCarlos + (SalarioCarlos * 0.02)) * NumMeses
    DinheiroJoao = SalarioJoao + (SalarioJoao * 0.05) * NumMeses
    print("app Joao", DinheiroJoao)
    print("app Carlos", DinheiroCarlos)
    Laco1 = Laco1 + 1
    print(Laco1)

print("Serão necessários", Laco1, "meses para que o valor pertencente a João igualasse ou ultrapasasse o valor pertencente a Carlos.")
