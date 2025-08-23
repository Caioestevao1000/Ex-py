print("\n## Aumento de 30% do Salário ##")

salario = float(input("Digite seu salário:"))

if salario < 500.00:
    print("Reajuste de 30%: R$",(salario * 0.30))
else:
    print("Você não possui direito ao aumento")
input("\nPressione Enter para sair...")