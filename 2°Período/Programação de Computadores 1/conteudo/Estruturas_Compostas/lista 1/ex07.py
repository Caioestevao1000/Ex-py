vendas = []

quantidade = int(input("Informe a quantidade de vendas: "))

for i in range(quantidade):
    print(f"\nVenda {i+1}:")
    cliente = input(f"Cliente: ")
    produto = input(f"Produto: ")
    valor = float(input(f"Valor: "))
    
    vendas.append({
        "cliente": cliente,
        "produto": produto,
        "valor": valor
    })

total = sum(v["valor"] for v in vendas)
print(f"\nValor total vendido: R$ {total:.2f}")

clientes = {v["cliente"] for v in vendas}

print("Clientes cadastrados:")
for c in sorted(clientes):
    print(c)
