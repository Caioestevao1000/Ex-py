print("\n## Maior Número ##")

print("## Digite Três Números ##")
num1 = float(input("1° Número:"))
num2 = float(input("2° Número:"))
num3 = float(input("3° Número:"))

if num1 > num2 and num1 > num3:
    print("O maior Número é:", num1)
elif num2 > num1 and num2 > num3:
    print("O maior Número é:", num2)
elif num3 > num1 and num3 > num2:
    print("O maior Número é:", num3)
elif num1 == num2 and num1 == num3:
    print("Os números são iguais")
input("\nPressione Enter para sair...")