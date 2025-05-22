print("### Conversor Manual de Bases (sem funções) ###")

decimal = int(input("Digite um número decimal: "))

print("\nEscolha uma opção de conversão:")
print("1 - Decimal para Binário")
print("2 - Decimal para Octal")
print("3 - Decimal para Hexadecimal")

opcao = int(input("Digite a opção (1, 2 ou 3): "))

if opcao == 1:
    resultado = ""
    num = decimal
    if num == 0:
        resultado = "0"
    else:
        while num > 0:
            resto = num % 2
            resultado = str(resto) + resultado
            num = num // 2
    print(f"\n{decimal} em binário é: {resultado}")


elif opcao == 2:
    resultado = ""
    num = decimal
    if num == 0:
        resultado = "0"
    else:
        while num > 0:
            resto = num % 8
            resultado = str(resto) + resultado
            num = num // 8
    print(f"\n{decimal} em octal é: {resultado}")

elif opcao == 3:
    resultado = ""
    num = decimal
    hex_digitos = "0123456789ABCDEF"
    if num == 0:
        resultado = "0"
    else:
        while num > 0:
            resto = num % 16
            resultado = hex_digitos[resto] + resultado
            num = num // 16
    print(f"\n{decimal} em hexadecimal é: {resultado}")

else:
    print("\nOpção inválida!")

input("Aperte Enter Para Sair...")
