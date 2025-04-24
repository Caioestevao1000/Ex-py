print("\n## Menor Número ##")

print("## Digite Dois Números ##")
num1 = float(input("1° Número:"))
num2 = float(input("2° Número:"))

if num1 < num2:
    print("O Menor Número é:", num1)
elif num2 < num1:
    print("O Menor Número é:", num2)
else:
    print("Os Números são iguais")
input("\nPressione Enter para sair...")