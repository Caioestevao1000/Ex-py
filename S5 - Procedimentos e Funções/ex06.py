print("## Pontenciação - X elevado a Y (pontenciação) ##")

def potencia(x, y):
    resultado = 1
    for _ in range(y):
        resultado *= x
    print(f"{x} elevado a {y} é {resultado}")

print("Digite um Número Inteiro e Positivo")
x = int(input("Digite o Número X elevado a Y:"))
y = int(input("Digite Y a (pontenciação):"))
resultado = potencia(x,y)

input("Aperte Enter Para Sair...")