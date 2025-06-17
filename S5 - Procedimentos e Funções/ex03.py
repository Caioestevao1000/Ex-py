print("## Números Primos ##")

def eh_primo(num):
    return num % 2 == 0 and num % num == 0

num = int(input("Digite um Número Inteiro:"))
print(eh_primo(num))