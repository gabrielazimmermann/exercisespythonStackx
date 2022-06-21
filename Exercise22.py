# Tarefa 22: Preço de Produtos
# Dev: Gabriela Ottoni Zimmermann
# Data: 20.06.2022

Preco = float(input("Digite o preço do produto desejado:"))
Categoria = input("Qual a categoria do produto desejado:")

if Preco <= 25 and Categoria == '1':
    PrecoFinal = Preco + (Preco * 0.05)
    print("Preço final:", PrecoFinal, ", para produtos da categoria Limpeza.")
elif Preco <= 25 and Categoria == '2':
    PrecoFinal = Preco + (Preco * 0.08)
    print("Preço final:", PrecoFinal, ", para produtos da categoria Alimentação.")
elif Preco <= 25 and Categoria == '3':
    PrecoFinal = Preco + (Preco * 0.110)
    print("Preço final:", PrecoFinal, ", para produtos da categoria Vestuário.")

if Preco > 25 and Categoria == '1':
    PrecoFinal = Preco + (Preco * 0.12)
    print("Preço final:", PrecoFinal, ", para produtos da categoria Limpeza.")
elif Preco > 25 and Categoria == '2':
    PrecoFinal = Preco + (Preco * 0.15)
    print("Preço final:", PrecoFinal, ", para produtos da categoria Alimentação")
elif Preco > 25 and Categoria == '3':
    PrecoFinal = Preco + (Preco * 0.18)
    print("Preço final:", PrecoFinal, ", para produtos da categoria Limpeza")



if PrecoFinal <= 50:
    print("Categoria: Barato")
elif PrecoFinal > 50 and PrecoFinal < 120:
    print("Categoria: Normal")
else:
    print("Categoria: Caro")