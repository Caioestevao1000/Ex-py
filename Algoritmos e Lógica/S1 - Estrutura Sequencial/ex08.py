print("## Cálculo de Somatório (Sem Laço) ##")
print("Digite 5 valores para calcular a soma:")

x1 = float(input("Digite o 1º valor: "))
soma1 = x1
print("Soma parcial: ", soma1)

x2 = float(input("Digite o 2º valor: "))
soma2 = soma1 + x2
print("Soma parcial: ", soma2)

x3 = float(input("Digite o 3º valor: "))
soma3 = soma2 + x3
print("Soma parcial: ", soma3)

x4 = float(input("Digite o 4º valor: "))
soma4 = soma3 + x4
print("Soma parcial: ", soma4)

x5 = float(input("Digite o 5º valor: "))
soma5 = soma4 + x5
print("Soma parcial: ", soma5)

print("\nResultado final do somatório: ", soma5)

input("\nPressione Enter para sair...")
