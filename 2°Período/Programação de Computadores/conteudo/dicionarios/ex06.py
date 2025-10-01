produtos = {
    "arroz": 25.90,
    "feijão": 8.50,
    "macarrão": 5.20,
    "leite": 4.80,
    "café": 12.00
}

print(produtos)


resposta = str(input(f"Deseja Remover algum produto S/N?"))
resposta = resposta.lower()

if "s" == resposta:
    nome_produto = str(input("Digite o nome do produto para remover:")) 
    print(f"Produto removido {produtos.pop(nome_produto)}")
else:
    print("Produto não encontrado"),

print(produtos)
