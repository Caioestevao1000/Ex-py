print("## Digite dois números para divisão ##")

n1 = float(input("Digite o número que será dividido:"))
n2 = float(input("Digite um número maior que 0 para a divisão:"))

if n2 <= 0:
    print("O Divisor deve ser maior que 0..")
    n2 = float(input("Digite um número maior que 0 para a divisão:"))
    print("Resultado é", n1/n2)
else:
    print("Resultado é", n1/n2)

input("\nPressione Enter para sair...")