print("\n## Soma dos Elementos Anteriores ##")

def soma(valor):
    soma_total = 0
    for i in range(1, valor + 1):
        soma_total += i
    return soma_total

num = int(input("Digite um valor inteiro:"))
resultado = soma(num)
print(f"A soma dos números 1 e {num} é: {resultado}")




input("Pressione Enter para sair...")

