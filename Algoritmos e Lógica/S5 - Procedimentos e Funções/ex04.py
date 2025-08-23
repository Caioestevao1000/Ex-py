print("## Soma dos Divisores do Valor X ##")

def soma_divisores(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += i
    return total

num = int(input("\nDigite o Número X, que seja Inteiro e Positivo: "))
if num < 1:
    print("Digite um Número inteiro e maior que 0")
else:
    resultado = soma_divisores(num)
    print(f"A soma dos divisores de {num} é: {resultado}")

input("Aperte Enter Para Sair...")