print("\n## Aumento de Salário ##")

salario = float(input("Digite seu salário:"))

if salario <= 300:
    salario = salario + salario * 0.15
    print(f"Reajuste de 15%: R${salario:.2f}")
elif salario > 300 and salario <= 600:
    salario = salario + salario * 0.10
    print(f"Reajuste de 10%: R${salario:.2f}")
elif salario > 600 and salario <= 900:
    salario = salario + salario * 0.05
    print(f"Reajuste de 15%: R${salario:.2f}")
else:
    print(f"Sem Aumento de Salário: R${salario:.2f}")

input("\nPressione Enter para sair...")
