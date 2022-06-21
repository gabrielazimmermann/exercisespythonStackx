# Tarefa 11: Receber Nomes e Salários
# Dev: Gabriela Ottoni Zimmermann
# Data: 15.06.2022

QuantMacas = int(input("Digite a quantidade de maçãs compradas:"))
if QuantMacas >= 12:
    GrandeQuant = 0.25
    ValorPagar = QuantMacas * GrandeQuant
else:
    PoucaQuant = 0.30
    ValorPagar = QuantMacas * PoucaQuant

print("O valor de", QuantMacas, "maçãs é de", ValorPagar, "reais.")