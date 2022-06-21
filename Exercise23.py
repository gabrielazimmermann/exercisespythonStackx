# Tarefa 23: Compra de produtos (switch case)
# Dev: Gabriela Ottoni Zimmermann
# Data: 20.06.2022

CodProd = int(input("Digite o código do produto desejado:"))
QuantProd = int(input("Digite a quantidade desejada:"))

if CodProd >= 1 and CodProd <= 10:
    print("Preço unitário: R$10,00")
    print("Quantidade Desejada:", QuantProd)
    PrecoNota = QuantProd * 10
    if PrecoNota <= 250:
        PrecoDesc = PrecoNota - (PrecoNota * 0.05)
        print("Preço final com aplicação de desconto fica:", PrecoDesc)
    else:
        print("Preço final, não aplica-se desconto:", PrecoNota)
elif CodProd >= 11 and CodProd <= 20:
    print("Preço unitário: R$15,00")
    print("Quantidade Desejada:", QuantProd)
    PrecoNota = QuantProd * 15
    if PrecoNota >= 250 and PrecoNota <= 500:
        PrecoDesc = PrecoNota - (PrecoNota * 0.10)
        print("Preço final com aplicação de desconto fica:", PrecoDesc)
    else:
        print("Preço final, não aplica-se desconto:", PrecoNota)
elif CodProd >= 21 and CodProd <= 30:
    print("Preço unitário: R$20,00")
    print("Quantidade Desejada:", QuantProd)
    PrecoNota = QuantProd * 20
    if PrecoNota > 50:
        PrecoDesc = PrecoNota - (PrecoNota * 0.15)
        print("Preço final com aplicação de desconto fica:", PrecoDesc)
    else:
        print("Preço final, não aplica-se desconto:", PrecoNota)
elif CodProd >= 31 and CodProd <= 40:
    print("Preço unitário: R$30,00")
    print("Quantidade Desejada:", QuantProd)
    PrecoNota = QuantProd * 30
    print("Preço final, não aplica-se desconto:", PrecoNota)