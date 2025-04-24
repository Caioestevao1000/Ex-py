print("## Cálculo de Horas Trabalhadas ##")

ht = float(input("Digite o número de horas trabalhadas:"))
het = float(input("Digite o número de horas extras:"))
salariomin = float(input("Digite o Salário Mínimo:"))

valor_hora_trabalhada = salariomin / 8

valor_hora_extra = salariomin / 4

salario_bruto = ht * valor_hora_trabalhada

qta_receber = valor_hora_extra * het

salario_total = salario_bruto + qta_receber

print("\nVocê receberá:",salario_total)

input("\nPressione Enter para sair...")