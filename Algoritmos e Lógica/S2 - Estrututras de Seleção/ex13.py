print("\n## Cálculo de Novo Salário ##")

salario = float(input("Digite o seu salário:"))

if salario <= 300:
    salario = salario + salario * 0.5
elif salario > 300 and salario <= 500:
    salario = salario + salario * 0.4
elif salario > 500 and salario <= 700:
    salario = salario + salario * 0.3
elif salario > 700 and salario <= 800:
    salario = salario + salario * 0.2
elif salario > 800 and salario <= 1000:
    salario = salario + salario * 0.1
else:
    salario = salario + salario * 0.05

print (f"Seu novo salário é de: R${salario:.2f}")

input("\nPressione Enter para sair...")