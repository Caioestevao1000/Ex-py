estoque = {
    "arroz": 5,
    "feijão": 3,
    "macarrão": 7
}

print("Estoque inicial:", estoque)

produto = input("Digite o nome do produto vendido: ")

if produto in estoque:
    estoque[produto] -= 1
    print("Venda realizada! Novo estoque:", estoque[produto])
else:
    print("Produto não encontrado")

print(estoque)
