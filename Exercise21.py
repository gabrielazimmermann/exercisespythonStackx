# Tarefa 21: Aumento Salarial (FOR)
# Dev: Gabriela Ottoni Zimmermann
# Data: 17.06.2022

SalarioInicial = PercentualAumento = ReajusteSalarialAnual = SalarioAcumulado = 0
AnoInicial = 2000
AnoFinal = 2018

for i in range(AnoInicial, AnoFinal, 1):
    if i == 2000:
        SalarioInicial = 1000.00
        print(i, "Salário Inicial:", SalarioInicial, "%:", PercentualAumento, "Reajuste Salarial (R$):", ReajusteSalarialAnual, "Salário Acumulado:", SalarioAcumulado)
    elif i == 2001:
        PercentualAumento = 0.015
        ReajusteSalarialAnual = SalarioInicial * PercentualAumento
        SalarioAcumulado = SalarioInicial + ReajusteSalarialAnual
        print(i, "%:", PercentualAumento, "Reajuste Salarial (R$):", ReajusteSalarialAnual, "Salário Acumulado:", SalarioAcumulado)
    else:
        print(i, "Salario Acumulado", round(SalarioAcumulado, 2))
        ReajusteSalarialAnual = SalarioAcumulado + PercentualAumento
        SalarioAcumulado = SalarioAcumulado + ReajusteSalarialAnual
        print(i, "%", PercentualAumento, "Reajuste Salarial (R$):", round(ReajusteSalarialAnual, 2), "Salário Acumulado:", round(SalarioAcumulado, 2))
    PercentualAumento *= 2
