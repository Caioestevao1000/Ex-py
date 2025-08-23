print("\n## Custo do Carro ##")

custo = float(input("Digite o Custo de Fábrica do carro:"))

if custo <= 12000:
    preco = custo + custo * 0.05
elif custo > 12000 and custo <= 25000:
    preco = custo + custo * 0.10 + custo * 0.15
else:
    preco= custo + custo * 0.15 + custo * 0.20

print (f"O Preço Final do Carro é de:R${preco:.2f}")

input("\nPressione Enter para sair...")