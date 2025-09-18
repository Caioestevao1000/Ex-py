qtd_produtos = int(input("Digite a quantidade de produtos para cadastrar: "))

produtos = []

print("\nCadastro de Produtos:")
for i in range(qtd_produtos):
    nome = input(f"Nome do produto {i + 1}: ")
    preco = float(input(f"Preço do produto {i + 1}: "))
    produtos.append({"nome": nome, "preco": preco})

total_compra = 0
nao_encontrados = []

venda = int(input("\nDigite quantos produtos o cliente comprou: "))
for i in range(venda):
    nome_compra = input(f"Digite o nome do item {i + 1} comprado: ")

    encontrado = False
    for p in produtos:
        if p["nome"].lower() == nome_compra.lower():
            total_compra += p["preco"]
            encontrado = True
            break

    if not encontrado:
        nao_encontrados.append(nome_compra)

print(f"\nValor total da compra: R$ {total_compra:.2f}")

if nao_encontrados:
    print("Itens não encontrados no cadastro:")
    for item in nao_encontrados:
        print("-", item)
