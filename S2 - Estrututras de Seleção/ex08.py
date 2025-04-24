print("\n## Reajuste de Salário ##")

salario = float(input("Digite seu salário:"))

if salario <= 300:
    salario = salario + salario * 0.35
    print("Reajuste de 35%: R$",salario)
else:
    salario = salario + salario * 0.15
    print("Reajuste de 15%: R$",salario)
input("\nPressione Enter para sair...")