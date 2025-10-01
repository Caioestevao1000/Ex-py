# Exercício 3 - Vendas
vendas = []
qnt = int(input("Quantas vendas? "))

for i in range(qnt):
    dic = {}
    dic['cliente'] = input(f"Venda {i+1} - Cliente: ")
    dic['produto'] = input(f"Venda {i+1} - Produto: ")
    dic['valor'] = float(input(f"Venda {i+1} - Valor: "))
    vendas.append(dic)

# Total vendido
total = 0
for v in vendas:
    total += v['valor']

print(f"\nValor total vendido: R$ {total:.2f}")

# Clientes sem repetição
clientes = set()
for v in vendas:
    clientes.add(v['cliente'])

print("\nClientes (sem repetição):")
for c in clientes:
    print("-", c)

# Total por cliente
print("\nTotal por cliente:")
totais = {}
for c in clientes:
    soma = 0
    for v in vendas:
        if v['cliente'] == c:
            soma += v['valor']
    totais[c] = soma
    print(f"- {c}: R$ {soma:.2f}")

# Cliente que mais comprou
maior_nome = ""
maior_valor = 0
for cliente, valor in totais.items():
    if valor > maior_valor:
        maior_valor = valor
        maior_nome = cliente

print(f"\nCliente que mais comprou: {maior_nome} (R$ {maior_valor:.2f})")
