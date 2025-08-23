print("## Cálculo de Salário ##")
salariofx = float(input("Digite o seu salário fixo:"))
comissao = float(input("Digite o valor total de suas vendas:"))

comissao = comissao * 4 / 100
salario = comissao + salariofx

print("\nO seu salário total será de:", salario)

input("\nPressione Enter para sair...")
