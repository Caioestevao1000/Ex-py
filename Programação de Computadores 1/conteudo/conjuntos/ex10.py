estoque = set(str(input("Digite o Estoque:")).split())
pedidos = set(str(input("Digite o Pedido:")).split())

presente_nos_conjuntos = estoque & pedidos
indisponivel = pedidos - estoque

print("Atendidos:", presente_nos_conjuntos)
print("Indiponíveis:", indisponivel)
