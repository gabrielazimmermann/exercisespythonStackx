# Tarefa 4: Salário Bruto
# Dev: Gabriela Ottoni Zimmermann
# Data: 01.06.2022

Imposto = 7/100
SalarioBruto = float(input("Digite seu salário:"))
if SalarioBruto <= 350:
    Gratificacao = 100
else:
    if SalarioBruto > 350 and SalarioBruto <= 600:
        Gratificacao = 75
    else:
        if SalarioBruto > 600 and SalarioBruto <= 900:
            Gratificacao = 50
        else:
            Gratificacao = 35

RemuneracaoReal = (SalarioBruto + Gratificacao) - (SalarioBruto * Imposto)
print("Salário Bruto de:", SalarioBruto)
print("Gratificação de:", Gratificacao)
print("Imposto referente:", Imposto)
print("Sua Remuneração será de:", RemuneracaoReal)