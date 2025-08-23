print("\n## Preço e Classificação ##")

preco = float(input("Digite o Preço do Produto:"))

if preco <= 50:
    preco = preco + preco * 0.05
elif preco <= 100:
    preco = preco + preco * 0.10
else:
    preco = preco + preco * 0.15

if preco <= 80:
    print(f"O preço é de R${preco:.2f} com classificação:Barata")
elif preco <= 120:
    print(f"O preço é de R${preco:.2f} com classificação:Normal")
elif preco > 120 and preco <= 200:
    print(f"O preço é de R${preco:.2f} com classificação:Caro")
else:
    print(f"O preço é de R${preco:.2f} com classificação:Muito Caro")

input("\nPressione Enter para sair...")