# Tarefa 5: Empresa com 10 funcionarios
# Dev: Gabriela Ottoni Zimmermann
# Data: 02.06.2022

Laco1 = 0
Laco2 = True
Laco3 = True

while Laco1 < 10:
    SalarioMinimo = 450
    SalarioFinal = 0
    Auxilio = 0
    ValorHoraTrab = 0
    print(Laco1)
    CodFunc = int(input("Código do Funcionário: "))
    HorasTrabMes = int(input("Total de Horas Trabalhados no mês: "))
    while Laco2:
        Categoria = input("Digite a categoria: ")
        if Categoria == 'O' or Categoria == 'G':
            Laco2 = False
        else:
            print("As categorias possíveis são O e G, digite novamente...")
            continue
        break
    while Laco3:
        TurnoTrab = input("Turno de Trabalho:")
        if TurnoTrab == 'M' or TurnoTrab == 'V' or TurnoTrab == 'N':
            Laco3 = False
        else:
            print("As categorias possíveis são M, V ou N. Digite novamente...")
            continue
        break
    if Categoria == "G" and TurnoTrab == "N":
        ValorHoraTrab = SalarioMinimo * 0.18
        SalarioInicial = HorasTrabMes * ValorHoraTrab
        if SalarioInicial <= 300:
            Auxilio = 0.2 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            Auxilio = 0.15 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        else:
            Auxilio = 0.05 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
    if Categoria == "G" and TurnoTrab == "M" or TurnoTrab == "V":
        ValorHoraTrab = SalarioMinimo * 0.15
        SalarioInicial = HorasTrabMes * ValorHoraTrab
        if SalarioInicial <= 300:
            Auxilio = 0.2 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            Auxilio = 0.15 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        else:
            Auxilio = 0.05 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
    if Categoria == "O" and TurnoTrab == "N":
        ValorHoraTrab = SalarioMinimo * 0.13
        SalarioInicial = HorasTrabMes * ValorHoraTrab
        if SalarioInicial <= 300:
            Auxilio = 0.2 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            Auxilio = 0.15 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        else:
            Auxilio = 0.05 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
    if Categoria == "G" and TurnoTrab == "M" or TurnoTrab == "V":
        ValorHoraTrab = SalarioMinimo * 0.1
        SalarioInicial = HorasTrabMes * ValorHoraTrab
        if SalarioInicial <= 300:
            Auxilio = 0.2 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            Auxilio = 0.15 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
        else:
            Auxilio = 0.05 * SalarioInicial
            SalarioFinal = Auxilio + SalarioInicial
    print("Código do Funcionário", CodFunc)
    print("Horas Trabalhadas:", HorasTrabMes)
    print("Valor Hora Trabalhada", ValorHoraTrab)
    print("Auxílio Alimentação:", Auxilio)
    print("Salário Final:", SalarioFinal)
    Laco1 = Laco1 + 1
    Laco2 = True
    Laco3 = True
    print("Fim")