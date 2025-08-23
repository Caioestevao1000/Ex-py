print("## Escada em Python ##")

valor = int(input("Digite um número inteiro e positivo:"))
degraus = int(input("Digite a quantidade de degraus:"))

if valor <= 0 and degraus <= 0:
    print("Erro")
else:
    atual = valor
    for linha in range (1, degraus + 1):
        print()
        for i in range (linha):
            print(atual, end=" ")
            atual += 1