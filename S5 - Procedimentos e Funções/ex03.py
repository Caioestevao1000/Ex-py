print("## Números Primos ##")

def eh_primo(num):

    contador = 0

    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1

    if contador == 2:
        print("O número é primo")
        return True
    else:
        print("O número não é primo")
        return False

num = int(input("\nDigite um número: "))
resultado = eh_primo(num)
print(resultado)
input("Aperte Enter Para Sair...")