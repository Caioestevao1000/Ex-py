produtos = {}

qtd = int(input("Quantos produtos no cadastro? "))
for i in range(1, qtd + 1):
    nome = input(f"Produto {i} - Nome: ")
    preco = float(input(f"Produto {i} - Preço: "))
    estoque = int(input(f"Produto {i} - Quantidade em estoque: "))
    produtos[nome] = {"preco": preco, "estoque": estoque}

total = 0
compras = int(input("Quantos itens serão comprados? "))
for i in range(1, compras + 1):
    nome = input(f"Compra {i} - Produto: ")
    qtd_compra = int(input(f"Compra {i} - Quantidade: "))
    if nome not in produtos:
        print("Produto não existe.")
    else:
        if qtd_compra <= produtos[nome]["estoque"]:
            produtos[nome]["estoque"] -= qtd_compra
            total += produtos[nome]["preco"] * qtd_compra
            print("Item registrado.")
        else:
            print("Quantidade insuficiente em estoque.")

print(f"Valor total da compra: R$ {total:.2f}")
print("Estoque atualizado:")
for nome, dados in produtos.items():
    print(f"- {nome}: {dados['estoque']} un | R$ {dados['preco']:.2f}")
