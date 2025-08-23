print("## Operações ##\n")
print("### Menu ###")
print("Escolha do Usuário\t\tOperação")
print("        1\t\tMédia entre os números digitados")
print("        2\t\tDiferença do Maior pelo Menor")
print("        3\t\tProduto entre os números digitados")

escolha = int(input("Escolha a Operação Desejada:"))

if escolha == 1:
    print("\nMédia entre os Números")
    num1 = float(input("1° Número:"))
    num2 = float(input("2° Número:"))
    print("A média entre eles é igual:",(num1 + num2)/2)
elif escolha == 2:
    print("\nDiferença do Maior pelo Menor")
    num1 = float(input("1° Número:"))
    num2 = float(input("2° Número:"))
    if num1 > num2:
        print("A diferença é:", (num1 - num2))
    else: print("A diferença é:", (num2 - num1))
elif escolha == 3:
    print("\nProduto dos Números")
    num1 = float(input("1° Número:"))
    num2 = float(input("2° Número:"))
    print("O Produto é:", num1 * num2)

else: print("Opção Inválida. Escolha entre 1 e 3.")

print("Pressione Enter para Finalizar...")